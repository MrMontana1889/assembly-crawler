// PythonClassDefinition.cs
// Copyright (c) 2021 Kristopher L. Culin See LICENSE for details

using System;
using System.Collections.Generic;
using System.Diagnostics;
using System.IO;
using System.Linq;
using System.Reflection;
using System.Text;
using AssemblyCrawler.Library;
using static AssemblyCrawler.Library.WriterLibrary;
using static AssemblyCrawler.Support.Constants;

namespace AssemblyCrawler.Support
{
	[DebuggerDisplay("{FullName}:{ClassName}")]
	public class PythonClass
	{
		#region Constructor
		public PythonClass(PythonModule module, Type classType)
		{
			Module = module;
			ClassType = classType;
			TypeParser = new TypeParser(this).Parse();
			Initialize();
		}
		#endregion

		#region Public Methods
		public void Write(StreamWriter sw)
		{
			WriteClass(sw);
			WriteConstructor(sw);

			if (!ClassType.IsEnum)
			{
				// Enums do not have methods and properties
				foreach (var method in Methods)
					method.Write(sw);

				foreach (var property in Properties)
					property.Write(sw);
			}

			sw.WriteLine();
		}
		public void Update()
		{
			// Go through the methods and properties and ensure that any return types and parameter types are correctly imported.
			// This is required as some types may be generated after it is used (due to order in which modules are written)

			if (!ClassType.IsEnum)
			{
				// Consider the parent interfaces as well as the constructor argument types.
				foreach (var interf in ClassType.GetInterfaces())
					TypeConvertLibrary.AddImportForPythonType(Module, interf);

				foreach (var ctor in ClassType.GetConstructors())
				{
					foreach (var parameter in ctor.GetParameters())
						TypeConvertLibrary.AddImportForPythonType(Module, parameter.ParameterType);
				}

				// Only update if NOT an Enum
				foreach (var method in Methods)
					method.Update();

				foreach (var property in Properties)
					property.Update();
			}
		}
		#endregion

		#region Public Properties
		public PythonModule Module { get; }
		public Type ClassType { get; }
		public string FullName => ClassType.FullName;
		public string ClassName => ClassType.Name;
		public TypeParser TypeParser { get; }
		public List<PythonMethod> Methods { get; } = new List<PythonMethod>();
		public List<PythonProperty> Properties { get; } = new List<PythonProperty>();
		#endregion

		#region Private Methods
		private void Initialize()
		{
			if (ClassType.IsEnum)
				CreateEnumClass();
			else
				CreateClassDef();

			// Populate the methods and properties lists.
			Methods.AddRange(TypeParser.Methods);
			Methods.AddRange(TypeParser.OperatorAddition);
			Methods.AddRange(TypeParser.OperatorBitwiseAnd);
			Methods.AddRange(TypeParser.OperatorBitwiseOr);
			Methods.AddRange(TypeParser.OperatorBitwiseXor);
			Methods.AddRange(TypeParser.OperatorDivision);
			Methods.AddRange(TypeParser.OperatorEquality);
			Methods.AddRange(TypeParser.OperatorGreaterOrEqualTo);
			Methods.AddRange(TypeParser.OperatorGreaterThan);
			Methods.AddRange(TypeParser.OperatorInequality);
			Methods.AddRange(TypeParser.OperatorLessOrEqualTo);
			Methods.AddRange(TypeParser.OperatorLessThan);
			Methods.AddRange(TypeParser.OperatorModulo);
			Methods.AddRange(TypeParser.OperatorMultiplication);
			Methods.AddRange(TypeParser.OperatorSubtraction);

			Properties.AddRange(TypeParser.Properties);
		}
		private void CreateClassDef()
		{
			var interfaceNames = new List<string>();
			var implementedInterfaces = new List<string>();

			foreach (var interf in ClassType.GetInterfaces())
			{
				TypeInfo typeInfo = interf as TypeInfo;
				if (typeInfo != null)
				{
					foreach (var ii in typeInfo.ImplementedInterfaces)
						implementedInterfaces.Add(ii.Name);
				}
			}

			foreach (var interf in ClassType.GetInterfaces())
			{
				if (implementedInterfaces.Count > 0 && implementedInterfaces.Find(i => i == interf.Name) != null)
					continue;

				if (interf.IsGenericType)
				{
					string parentInterface = CreateGenericParentClass(interf);
					if (!string.IsNullOrWhiteSpace(parentInterface))
						interfaceNames.Add(parentInterface);
				}
				else
				{
					if (interf.Name.Contains($"{DISPOSABLE}"))
						continue;

					interfaceNames.Add(TypeConvertLibrary.ToPythonType(interf));
					AddReferenceImports(Module, interf);
				}
			}

			if (ClassType.IsGenericType)
			{
				// Must inherit from Generic.
				Module.AddImportModule($"{TYPING}").AddType($"{GENERIC}");

				var genericArguments = new List<string>();
				foreach (var ga in ClassType.GetGenericArguments())
					genericArguments.Add(ga.Name);

				interfaceNames.Insert(0, $"{GENERIC}[{string.Join(", ", genericArguments)}]");

				foreach (var arg in ClassType.GetGenericArguments())
				{
					Module.AddGenericArgumentType(arg);

					// We need to make sure the TypeVar does not constraint to the same type as the current interface
					// Python does NOT like this approach.
					var constraintTypes = new List<Type>();
					foreach (var t in arg.GetGenericParameterConstraints())
					{
						if (t.FullName == FullName)
						{
							// The constraint type is the same as the current class.
							// Get the inherited interfaces and use the first one instead.
							TypeInfo ti = t as TypeInfo;
							var ii = ti.ImplementedInterfaces.First();
							if (ti != null)
								constraintTypes.Add(ii);
						}
						else
						{
							constraintTypes.Add(t);
						}
					}

					Module.AddTypeVar(arg.Name, constraintTypes.ToArray());
					AddReferenceImports(Module, arg);
				}
			}

			ClassDefinition.Append($"{CLASS} {CorrectClassName(ClassType.Name)}");
			var parent = string.Join(", ", interfaceNames);

			if (!string.IsNullOrWhiteSpace(parent))
				ClassDefinition.AppendLine($"({parent}):");
			else
				ClassDefinition.AppendLine(":");
		}

		private string CreateGenericParentClass(Type interf)
		{
			string cn = WriterLibrary.CorrectClassName(ClassType.Name);

			AddReferenceImports(Module, interf);
			Module.AddGenericArgumentType(interf);

			var arguments = new List<string>();
			foreach (var arg in interf.GetGenericArguments())
			{
				arguments.Add(TypeConvertLibrary.ToPythonType(arg));
				AddReferenceImports(Module, arg);
				Module.AddGenericArgumentType(arg);
			}

			string parent = TypeConvertLibrary.ToPythonType(interf);
			if (!parent.Contains(string.Join(",", arguments)))
				return $"{CorrectClassName(interf.Name)}[{string.Join(", ", arguments)}]";
			else
				return parent;
		}
		private void CreateEnumClass()
		{
			Module.AddImportModule($"{ENUM_MODULE}").AddType($"{ENUM}");

			ClassDefinition.AppendLine($"{CLASS} {ClassType.Name}({ENUM}):");

			var members = Enum.GetNames(ClassType);
			var values = Enum.GetValues(ClassType);

			for (int i = 0; i < members.Length; ++i)
			{
				try { ClassDefinition.AppendLine($"{GetIndentation(1)}{members[i]} = {Convert.ToInt32(values.GetValue(i))}"); }
				catch { ClassDefinition.AppendLine($"{GetIndentation(1)}{members[i]} = {i}"); }
			}

			if (members.Length == 0)
				ClassDefinition.AppendLine($"{GetIndentation(2)}{PASS}");
		}
		private void WriteClass(StreamWriter sw)
		{
			sw.Write(ClassDefinition.ToString());
		}
		private void WriteConstructor(StreamWriter sw)
		{
			if (ClassType.IsEnum)
				return;

			string exceptionText = null;

			if (ClassType.IsInterface || ClassType.IsAbstract)
				exceptionText = "raise Exception(\"Creating a new Instance of this class is not allowed\")";

			var constructors = ClassType.GetConstructors();
			foreach (var constructorInfo in constructors)
			{
				PythonMethod constructorMethod = new PythonMethod(this, constructorInfo, constructors.Length > 1, exceptionText);
				constructorMethod.Write(sw);
			}

			if (constructors.Length == 0)
			{
				PythonMethod constructorMethod = new PythonMethod(this, null, false, exceptionText);
				constructorMethod.Write(sw);
			}
		}
		#endregion

		#region Private Properties
		private StringBuilder ClassDefinition { get; } = new StringBuilder();
		#endregion
	}
}
