// PythonStubWriterLibrary.cs
// Copyright (c) 2021 Kristopher L. Culin See LICENSE for details

using System;
using System.Collections.Generic;
using System.IO;
using System.Reflection;
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
		public const string EQUALS = "Equals";
		public const string GETHASHCODE = "GetHashCode";
		public const string GETTYPE = "GetType";
		public const string TOSTRING = "ToString";

		#endregion

		public static void WritePythonEnumDef(
			PythonModuleDefinition module,
			Type enumType,
			string docString,
			int indentLevel = 0)
		{
			PythonClassDefinition classDef = module.AddClassDefinition(enumType.AssemblyQualifiedName, enumType.Name);

			module.AddImportModule("enum").AddType("Enum");
			classDef.ClassDefinition.AppendLine($"{CLASS} {enumType.Name}(Enum):");

			var members = Enum.GetNames(enumType);
			var values = Enum.GetValues(enumType);

			for (int i = 0; i < members.Length; ++i)
			{
				classDef.ClassDefinition.AppendLine($"{GetIndentation(1)}{members[i]} = {(int)values.GetValue(i)}");
			}
		}

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

			string className = CorrectClassName(classType.Name, classType.GetGenericArguments().Length);

			// Process the interfaces this interface inherits from.  One or more can be generic.
			List<string> interfaceNames = new List<string>();

			// First need to determine the implemented interfaces.  We want to exclude these from the parent hierarchy since they
			// are technically already included.  Plus, python doesn't like it much (MRO (method rendering order)) gets pretty whacked.

			List<string> implementedInterfaces = new List<string>();
			foreach (var interf in classType.GetInterfaces())
			{
				TypeInfo typeInfo = interf as TypeInfo;
				if (typeInfo != null)
				{
					foreach (var ti in typeInfo.ImplementedInterfaces)
						implementedInterfaces.Add(ti.Name);
				}
			}

			foreach (var interf in classType.GetInterfaces())
			{
				if (implementedInterfaces.Count > 0 && implementedInterfaces.Find(i => i == interf.Name) != null)
					continue;

				if (interf.IsGenericType)
				{
					string parentInterface = CreateGenericParentClass(module, interf);
					if (!string.IsNullOrEmpty(parentInterface))
						interfaceNames.Add(parentInterface);
				}
				else
				{
					if ((interf.Namespace.Contains("IEnumerable") || interf.Name.Contains("IDisposable"))
						&& interf != typeof(Enum))
						continue;

					interfaceNames.Add(interf.Name);

					// Check to see if this type needs to be imported.
					AddReferenceImports(module, interf);
				}
			}

			if (classType.IsGenericType)
			{
				module.AddImportModule("typing").AddType("Generic");

				List<string> genericArguments = new List<string>();
				foreach (var ga in classType.GetGenericArguments())
					genericArguments.Add(ga.Name);

				interfaceNames.Insert(0, $"{GENERIC}[{string.Join(", ", genericArguments)}]");

				// This is a generic type with no parent generic interfaces.  So inherit from GENERIC
				foreach (var arg in classType.GetGenericArguments())
				{
					module.AddGenericArgumentType(arg);

					// Check to see if we are already importing this TypeVar.  if so, do not define it again.
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

			switch(methodName)
			{
				case EQUALS:
				case GETHASHCODE:
				case GETTYPE:
				case TOSTRING:
					return;
			}

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

				TypeConvertLibrary.AddImportForPythonType(classDef.Module, pair.Value);
				classDef.Module.AddGenericArgumentType(pair.Value);
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

				classDef.Module.AddImportModule("typing").AddType($"{UNION}");
			}
			else if (returnType.IsArray)
			{
				var genericArguments = returnType.GetGenericArguments();
				if (genericArguments.Length == 1)
				{
					returnTypeString = $"array({UNION}[{TypeConvertLibrary.ToPythonType(genericArguments[0])}, {NONETYPE}])";
					classDef.Module.AddImportModule("array").AddType("array");
				}
			}

			classDef.Module.AddGenericArgumentType(returnType);

			if ((returnType.IsEnum || returnType == typeof(Enum)) && (!returnType.IsGenericType && !returnType.IsGenericParameter))
				classDef.Module.Assembly.AddEnum(returnType);

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
				classDef.Methods.AppendLine($"{indentation}{TAB}{exception}");

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

			AddReferenceImports(classDef.Module, returnType);
			classDef.Module.AddGenericArgumentType(returnType);

			if ((returnType.IsEnum || returnType == typeof(Enum)) && (!returnType.IsGenericType && !returnType.IsGenericParameter))
				classDef.Module.Assembly.AddEnum(returnType);

			var selfKeyword = isStatic ? string.Empty : SELF;
			var adjustedReturnType = CorrectClassName(TypeConvertLibrary.ToPythonType(returnType),
				returnType.GetGenericArguments().Length);

			if (returnType.IsArray)
				classDef.Module.AddImportModule("array").AddType("array");

			classDef.Properties.AppendLine($"{indentation}{DEF} {propertyName}({selfKeyword}) -> {adjustedReturnType}:");
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

			TypeConvertLibrary.AddImportForPythonType(module, interf);
		}

		private static string CreateGenericParentClass(PythonModuleDefinition module, Type interf)
		{
			if (interf.Namespace.Contains("IEnumerable") && interf != typeof(Enum))
				return string.Empty;

			AddReferenceImports(module, interf);
			module.AddGenericArgumentType(interf);

			List<string> arguments = new List<string>();
			foreach (var arg in interf.GetGenericArguments())
			{
				if (arg == typeof(Enum) || !arg.Namespace.Contains("IEnumerable"))
				{
					arguments.Add(arg.Name);
					AddReferenceImports(module, arg);
					module.AddGenericArgumentType(arg);
				}
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
