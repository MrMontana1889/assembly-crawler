// PythonStubWriterLibrary.cs
// Copyright (c) 2021 Kristopher L. Culin See LICENSE for details

using System;
using System.Collections.Generic;
using System.IO;
using System.Linq;

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

		public static void WritePythingClassDef(
			StreamWriter sw,
			Type classType,
			string docString,
			int indentLevel = 0)
		{
			/*
			 * For generic interfaces, they need to either inherit from Generic[] or a generic interface.
			 * So need to determine upfront which parent to use.
			 * 
			 * 
			*/
		}

		public static void WritePythonClassDefinition(
			StreamWriter writer,
			Type classType,
			List<Type> inheritedTypes,
			string docString,
			bool isGenericType,
			int indentLevel = 0)
		{
			var className = classType.Name.Split('`')[0];
			var inheritedTypesString = string.Join(", ", inheritedTypes.Select(t => TypeConvertLibrary.ToPythonType(t)));

			if (isGenericType)
				inheritedTypesString = $"{GENERIC}[{inheritedTypesString}]";

			var classString = $"{CLASS} {className}({inheritedTypesString}):";

			var indentation = GetIndentation(indentLevel);

			writer.WriteLine();
			writer.WriteLine();
			writer.WriteLine($"{indentation}{CLASS} {className}({inheritedTypesString}):");
			writer.WriteLine($"{indentation}{docString}");

			writer.WriteLine($"{indentation}{TAB}{PASS}");
		}

		public static void WritePythonConstructor(
			StreamWriter writer,
			List<KeyValuePair<string, Type>> arguments,
			string docString,
			int indentLevel = 1)
		{
			WritePythonMethod(
				writer: writer,
				methodName: INIT,
				arguments: arguments,
				returnType: typeof(void),
				docString: docString,
				isStatic: false,
				indentLevel: indentLevel
				);
		}

		public static void WritePythonConstructorUnsupported(
			StreamWriter writer,
			int indentLevel = 1)
		{
			var docString = new PythonConstructorUnsupportedDocStringWriterLibrary().ToString();

			WritePythonMethod(
				writer: writer,
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
			StreamWriter writer,
			string methodName,
			List<KeyValuePair<string, Type>> arguments,
			Type returnType,
			string docString,
			bool isStatic,
			string exception = "",
			bool isOverloaded = false,
			int indentLevel = 1)
		{
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
			if (Nullable.GetUnderlyingType(returnType) != null)
			{
				returnType = Nullable.GetUnderlyingType(returnType) ?? typeof(void);
				var actualPythonType = TypeConvertLibrary.ToPythonType(returnType);
				returnTypeString = $"{UNION}[{actualPythonType}, {NONETYPE}]";
			}

			// definition
			var method = $"{DEF} {methodName}({selfKeyword}{pythonArguments}) -> {returnTypeString}:";

			var indentation = GetIndentation(indentLevel);

			writer.WriteLine();

			if (isStatic)
				writer.WriteLine($"{indentation}{STATIC_METHOD}");

			if (isOverloaded)
				writer.WriteLine($"{indentation}{OVERLOAD}");

			writer.WriteLine($"{indentation}{method}");
			writer.WriteLine($"{indentation}{docString}");

			if (exception?.Length > 0)
				writer.WriteLine($"{indentation}\t{exception}");

			writer.WriteLine($"{indentation}{TAB}{PASS}");
		}

		public static void WritePythonProperty(
			StreamWriter writer,
			string propertyName,
			Type returnType,
			string docString,
			bool isStatic,
			int indentLevel = 1)
		{
			var indentation = GetIndentation(indentLevel);

			writer.WriteLine();
			writer.WriteLine($"{indentation}{PROPERTY}");

			if (isStatic)
				writer.WriteLine($"{indentation}{STATIC_METHOD}");

			var selfKeyword = isStatic ? string.Empty : SELF;
			writer.WriteLine($"{indentation}{DEF} {propertyName}({selfKeyword}) -> {TypeConvertLibrary.ToPythonType(returnType)}:");
			writer.WriteLine($"{indentation}{docString}");
			writer.WriteLine($"{indentation}{TAB}{PASS}");
		}

		public static void WritePythonPropertySetter(StreamWriter writer,
			string propertyName,
			Type returnType,
			bool isStatic,
			int indentLevel = 1)
		{
			var indentation = GetIndentation(indentLevel);

			writer.WriteLine();
			writer.WriteLine($"{indentation}@{propertyName}{SETTER}");

			if (isStatic)
				writer.WriteLine($"{indentation}{STATIC_METHOD}");

			writer.WriteLine($"{indentation}{DEF} {propertyName}({SELF}, {propertyName.ToLower()}: {TypeConvertLibrary.ToPythonType(returnType)}) -> {NONETYPE}:");
			writer.WriteLine($"{indentation}{TAB}{PASS}");
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


		#region Private Static Methods
		private static string GetIndentation(int count)
		{
			var tabs = string.Empty;
			for (int i = 0; i < count; i++) tabs += $"{TAB}";
			return tabs;
		}
		#endregion
	}
}
