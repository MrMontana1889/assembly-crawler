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
		#endregion

        public static void WritePythonClassDefinition(
            StreamWriter writer,
            Type classType,
            List<Type>inheritedTypes,
            string docString,
            bool isGenericType,
            int indentLevel = 0)
        {
            var className = classType.Name;
            var inhertedTypesString = string.Join(", ", inheritedTypes.Select(t => TypeConvertLibrary.ToPythonType(t)));

            if (isGenericType)
                inhertedTypesString = $"[{inhertedTypesString}]";

            var classString = $"class {className}({inhertedTypesString}):";                        

			var indentaiton = GetIndentation(indentLevel);

            writer.WriteLine();
            writer.WriteLine();
            writer.WriteLine($"{indentaiton}class {className}({inhertedTypesString}):");
            writer.WriteLine($"{indentaiton}{docString}");

            writer.WriteLine($"{indentaiton}\tpass");
        }

        public static void WritePytonConstructor(
            StreamWriter writer,
            List<KeyValuePair<string, Type>> arguments,
            string docString,
            int indentLevel = 1)
        {
            WritePythonMethod(
                writer: writer,
                methodName: "__init__",
                arguments: arguments,
                returnType: typeof(void),
                docString: docString,
                isStatic: false,
                indentLevel: indentLevel
                );
        }

        public static void WritePytonConstructorUnsupported(
            StreamWriter writer,
            int indentLevel = 1)
        {
            var docString = new PythonConstructorUnsupportedDocStringWriterLibrary().ToString();

            WritePythonMethod(
                writer: writer,
                methodName: "__init__",
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
            var indentaiton = GetIndentation(indentLevel);
            writer.WriteLine($"{indentaiton}{typeName} = TypeVar(\"{typeName}\", {TypeConvertLibrary.ToPythonType(type)})");
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
            int indentLevel=1)
        {
            var pythonArgumentList = new List<string>();

            for (int i = 0; i < arguments.Count; i++)
            {
                var pair = arguments[i];
                pythonArgumentList.Add($"{pair.Key}: {TypeConvertLibrary.ToPythonType(pair.Value)}");
            }

			var pythonArguments = string.Join(", ", pythonArgumentList);
			pythonArguments = string.IsNullOrEmpty(pythonArguments) ? pythonArguments : $", {pythonArguments}";

            // self keywork
            var selfKeyword = isStatic ? string.Empty : "self";

            // return type
            var returnTypeString = TypeConvertLibrary.ToPythonType(returnType);
            if (Nullable.GetUnderlyingType(returnType) != null)
            {
                returnType = Nullable.GetUnderlyingType(returnType) ?? typeof(void);
                var actualPythonType = TypeConvertLibrary.ToPythonType(returnType);
                returnTypeString = $"Union[{actualPythonType}, None]";
            }

            // definition
            var method = $"def {methodName}({selfKeyword}{pythonArguments}) -> {returnTypeString}:";

            var indentaiton = GetIndentation(indentLevel);

            writer.WriteLine();

            if(isOverloaded)
                writer.WriteLine($"{indentaiton}@overload");

            writer.WriteLine($"{indentaiton}{method}");
            writer.WriteLine($"{indentaiton}{docString}");

            if (exception?.Length > 0)
                writer.WriteLine($"{indentaiton}\t{exception}");

            writer.WriteLine($"{indentaiton}\tpass");
        }

        public static void WritePythonProperty(
            StreamWriter writer,
            string propertyName,
            Type returnType,
            string docString,
            bool isStatic,
            int indentLevel = 1)
        {
            var indentaiton = GetIndentation(indentLevel);

            writer.WriteLine();
            writer.WriteLine($"{indentaiton}@property");

            if(isStatic)
                writer.WriteLine($"{indentaiton}@staticmethod");

            var selfKeyword = isStatic ? string.Empty : "self";
            writer.WriteLine($"{indentaiton}def {propertyName}({selfKeyword}) -> {TypeConvertLibrary.ToPythonType(returnType)}:");
            writer.WriteLine($"{indentaiton}{docString}");
            writer.WriteLine($"{indentaiton}\tpass");
        }

        public static void WritePythonPropertySetter(StreamWriter writer,
            string propertyName,            
            Type returnType,
            bool isStatic,
            int indentLevel = 1)
        {
            var indentaiton = GetIndentation(indentLevel);

            writer.WriteLine();
            writer.WriteLine($"{indentaiton}@{propertyName}.setter");

            if (isStatic)
                writer.WriteLine($"{indentaiton}@staticmethod");

            writer.WriteLine($"{indentaiton}def {propertyName}(self, {propertyName.ToLower()}: {TypeConvertLibrary.ToPythonType(returnType)}) -> None:");
            writer.WriteLine($"{indentaiton}\tpass");
        }

        public static void WritePythonGenericClassDefinition(StreamWriter writer)
        {
            //
        }

        public static void WritePythonNotAllowedConstructor(
            StreamWriter writer,
            int indentLevel = 1)
        {
            var indentaiton = GetIndentation(indentLevel);

            writer.WriteLine($"{indentaiton}def __init__(self):");

        } 


		#region Private Static Methods
		private static string GetIndentation(int count)
		{
			var tabs = "";
			for (int i = 0; i < count; i++) tabs += "\t";
			return tabs;
		}
		#endregion
	}
}
