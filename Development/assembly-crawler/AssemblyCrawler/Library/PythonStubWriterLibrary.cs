// PythonStubWriterLibrary.cs
// Copyright (c) 2021 Kristopher L. Culin See LICENSE for details

using System;
using System.Collections.Generic;
using System.IO;
using AssemblyCrawler.Support;

namespace AssemblyCrawler.Library
{
	public static class PythonStubWriterLibrary
	{
		#region Constants
		public static string BlankDocString => "\t\"\"\" \"\"\"";
		public static string NONETYPE = "None";
		public static string CLASS = "class";
		public static string PASS = "pass";
		public static string DEF = "def";
		public static string SELF = "self";
		public static string PROPERTY = "@property";
		public static string SETTER = ".setter";
		public static string INIT = "__init__";
		public static string TAB = "\t";
		public static string TYPE_VAR = "TypeVar";
		public static string UNION = "Union";
		public static string OVERLOAD = "@overload";
		public static string STATIC_METHOD = "@staticmethod";
		public static string GENERIC = "Generic";

		#endregion

		public static void WritePythonClassDef(
			PythonModuleDefinition module,
			Type classType,
			string docString,
			int indentLevel = 0)
		{
			/*
			 * For generic interfaces, they need to either inherit from Generic[] or a generic interface and provide the types via Typevar.
			 * So need to determine upfront which parent to use.
			 * 
			 * IsGenericType will determine if this type is generic.  Then check the list of interfaces for any generic interfaces it may inherit from.
			*/

			PythonClassDefinition classDef = module.AddClassDefinition(classType.AssemblyQualifiedName, classType.Name);

			// Process the interfaces this interface inherits from.  One or more can be generic.
			List<string> interfaceNames = new List<string>();
			bool hasGenericParent = false;
			foreach (var interf in classType.GetInterfaces())
			{
				if (interf.IsGenericType)
				{
					interfaceNames.Add(CreateGenericParentClass(module, interf));
					hasGenericParent = true;
				}
				else
				{
					//interfaceNames.Add(CorrectClassName(interf.Name, interf.GetGenericArguments().Length));
					interfaceNames.Add(interf.Name);

					// Check to see if this type needs to be imported.
					AddReferenceImports(module, interf);
				}
			}

			if (classType.IsGenericType && !hasGenericParent)
			{
				module.AddImportModule("typing");
				module.GetImport("typing").AddType("TypeVar");

				List<string> genericArguments = new List<string>();
				foreach (var ga in classType.GetGenericArguments())
					genericArguments.Add(ga.Name);

				interfaceNames.Insert(0, $"Generic[{string.Join(", ", genericArguments)}]");

				// This is a generic type with no parent generic interfaces.  So inherit from GENERIC
				List<string> argumentTypes = new List<string>();
				foreach (var arg in classType.GetGenericArguments())
				{
					argumentTypes.Add(arg.Name);
					module.AddTypeVar(arg.Name, arg.GetGenericParameterConstraints());

					AddReferenceImports(module, arg);
				}
			}

			classDef.ClassDefinition.Append($"{CLASS} {CorrectClassName(classType.Name, classType.GetGenericArguments().Length)}");
			string parent = string.Join(", ", interfaceNames);

			if (!string.IsNullOrEmpty(parent))
				classDef.ClassDefinition.AppendLine($"({parent}):");
			else
				classDef.ClassDefinition.AppendLine(":");
		}

		public static void WritePythonConstructor(
			PythonClassDefinition classDef,
			List<KeyValuePair<string, Type>> arguments,
			string docString,
			int indentLevel = 1)
		{
			WritePythonMethod(
				classDef: classDef,
				methodName: INIT,
				arguments: arguments,
				returnType: typeof(void),
				docString: docString,
				isStatic: false,
				indentLevel: indentLevel
				);
		}

		public static void WritePythonConstructorUnsupported(
			PythonClassDefinition classDef,
			int indentLevel = 1)
		{
			var docString = new PythonConstructorUnsupportedDocStringWriterLibrary().ToString();

			WritePythonMethod(
				classDef: classDef,
				methodName: INIT,
				arguments: new List<KeyValuePair<string, Type>>(),
				returnType: typeof(void),
				docString: docString,
				isStatic: false,
				exception: "raise Exception(\"Creating a new Instance of this class is not allowed\")",
				isOverloaded: false,
				indentLevel: indentLevel
				);
		}

		public static void WritePythonGenericVariables(
			StreamWriter writer,
			string typeName,
			Type type,
			int indentLevel = 0
			)
		{
			var indentation = GetIndentation(indentLevel);
			writer.WriteLine($"{indentation}{typeName} = {TYPE_VAR}(\"{typeName}\", {TypeConvertLibrary.ToPythonType(type)})");
		}

		public static void WritePythonMethod(
			PythonClassDefinition classDef,
			string methodName,
			List<KeyValuePair<string, Type>> arguments,
			Type returnType,
			string docString,
			bool isStatic,
			string exception = "",
			bool isOverloaded = false,
			int indentLevel = 1)
		{
			AddReferenceImports(classDef.Module, returnType);

			// To handle generic type name better
			methodName = methodName.Split('`')[0];

			// self keyword
			var selfKeyword = isStatic ? string.Empty : SELF;


			var pythonArgumentList = new List<string>();
			for (int i = 0; i < arguments.Count; i++)
			{
				var pair = arguments[i];
				pythonArgumentList.Add($"{pair.Key}: {TypeConvertLibrary.ToPythonType(pair.Value)}");
			}

			var pythonArguments = string.Join(", ", pythonArgumentList);
			pythonArguments = string.IsNullOrEmpty(pythonArguments) || isStatic ? pythonArguments : $", {pythonArguments}";


			// return type
			var returnTypeString = TypeConvertLibrary.ToPythonType(returnType);
			TypeConvertLibrary.AddImportForPythonType(classDef.Module, returnType);
			if (Nullable.GetUnderlyingType(returnType) != null)
			{
				returnType = Nullable.GetUnderlyingType(returnType) ?? typeof(void);
				var actualPythonType = TypeConvertLibrary.ToPythonType(returnType);
				returnTypeString = $"{UNION}[{actualPythonType}, {NONETYPE}]";
			}

			// definition
			var method = $"{DEF} {methodName}({selfKeyword}{pythonArguments}) -> {returnTypeString}:";

			var indentation = GetIndentation(indentLevel);

			classDef.Methods.AppendLine();

			if (isStatic)
				classDef.Methods.AppendLine($"{indentation}{STATIC_METHOD}");

			if (isOverloaded)
				classDef.Methods.AppendLine($"{indentation}{OVERLOAD}");

			classDef.Methods.AppendLine($"{indentation}{method}");
			classDef.Methods.AppendLine($"{indentation}{docString}");

			if (exception?.Length > 0)
				classDef.Methods.AppendLine($"{indentation}\t{exception}");

			classDef.Methods.AppendLine($"{indentation}{TAB}{PASS}");
		}

		public static void WritePythonProperty(
			PythonClassDefinition classDef,
			string propertyName,
			Type returnType,
			string docString,
			bool isStatic,
			int indentLevel = 1)
		{
			var indentation = GetIndentation(indentLevel);

			classDef.Properties.AppendLine();
			classDef.Properties.AppendLine($"{indentation}{PROPERTY}");

			if (isStatic)
				classDef.Properties.AppendLine($"{indentation}{STATIC_METHOD}");

			var selfKeyword = isStatic ? string.Empty : SELF;
			classDef.Properties.AppendLine($"{indentation}{DEF} {propertyName}({selfKeyword}) -> {TypeConvertLibrary.ToPythonType(returnType)}:");
			classDef.Properties.AppendLine($"{indentation}{docString}");
			classDef.Properties.AppendLine($"{indentation}{TAB}{PASS}");
		}

		public static void WritePythonPropertySetter(
			PythonClassDefinition classDef,
			string propertyName,
			Type returnType,
			bool isStatic,
			int indentLevel = 1)
		{
			var indentation = GetIndentation(indentLevel);

			classDef.Properties.AppendLine();
			classDef.Properties.AppendLine($"{indentation}@{propertyName}{SETTER}");

			if (isStatic)
				classDef.Properties.AppendLine($"{indentation}{STATIC_METHOD}");

			classDef.Properties.AppendLine($"{indentation}{DEF} {propertyName}({SELF}, {propertyName.ToLower()}: {TypeConvertLibrary.ToPythonType(returnType)}) -> {NONETYPE}:");
			classDef.Properties.AppendLine($"{indentation}{TAB}{PASS}");
		}

		public static void WritePythonGenericClassDefinition(StreamWriter writer)
		{
			//
		}

		public static void WritePythonNotAllowedConstructor(
			StreamWriter writer,
			int indentLevel = 1)
		{
			var indentation = GetIndentation(indentLevel);

			writer.WriteLine($"{indentation}{DEF} {INIT}({SELF}):");

		}

		#region Private Methods
		private static string GetIndentation(int count)
		{
			var tabs = string.Empty;
			for (int i = 0; i < count; i++) tabs += $"{TAB}";
			return tabs;
		}
		private static void AddReferenceImports(PythonModuleDefinition module, Type interf)
		{
			if (interf == typeof(void))
				return;

			if (!interf.IsGenericParameter)
			{
				var refClassDef = module.ClassDefinitions.Find(c => c.FullName == interf.AssemblyQualifiedName && c.ClassName == interf.Name);
				if (refClassDef == null)
				{
					// Not found.  check entire package.
					foreach (var mod in module.Package.Modules)
					{
						if (mod.Filename != module.Filename)
						{
							refClassDef = mod.ClassDefinitions.Find(c => c.FullName == interf.AssemblyQualifiedName && c.ClassName == interf.Name);
							if (refClassDef != null)
								module.AddImportModule(interf.Namespace).AddType(interf.Name);
						}
					}
				}
			}
			else if (interf.IsGenericParameter)
			{
				var typeVar = module.GetTypeVar(interf.Name);

				if (typeVar == null)
				{
					//foreach (var mod in module.Package.Modules)
					for(int i = 0; i < module.Package.Modules.Count; ++i)
					{
						var mod = module.Package.Modules[i];
						if (mod.ModuleNamespace != module.ModuleNamespace)
						{
							typeVar = mod.GetTypeVar(interf.Name);
							if (typeVar != null)
							{
								module.AddImportModule(mod.ModuleNamespace).AddType(typeVar.TypeVarName);
								break;
							}
						}
					}
				}
			}
		}

		private static string CreateGenericParentClass(PythonModuleDefinition stubFile, Type interf)
		{
			stubFile.AddImportModule("typing");
			stubFile.GetImport("typing").AddType("Generic");

			List<string> arguments = new List<string>();
			foreach (var arg in interf.GetGenericArguments())
			{
				arguments.Add(arg.Name);
				AddReferenceImports(stubFile, arg);
			}
			return $"{CorrectClassName(interf.Name, interf.GetGenericArguments().Length)}[{string.Join(", ", arguments)}]";
		}

		public static string CorrectClassName(string name, int count)
		{
			return name.Replace($"`{count}", "");
		}
		#endregion
	}
}
