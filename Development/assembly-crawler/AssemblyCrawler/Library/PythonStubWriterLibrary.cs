using System;
using System.Collections.Generic;
using System.IO;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace AssemblyCrawler.Library
{
    public static class PythonStubWriterLibrary
    {
        public static string BlankDocString => "\t\"\"\" \"\"\"";

        public static void WritePythonClassDefinition(
            StreamWriter writer,
            string className,
            List<Type>inheritedTypes,
            string docString,
            int indentLevel = 0)
        {
            var inhertedTypesString = string.Join(", ", inheritedTypes.Select(t => TypeLibrary.ConvertTypeToPythonType(t)));
            var classString = $"class {className}({inhertedTypesString}):";

            var indentaiton = GetIndentation(indentLevel);

            writer.WriteLine();
            writer.WriteLine();
            writer.WriteLine($"{indentaiton}class {className}({inhertedTypesString}):");
            writer.WriteLine($"{indentaiton}{docString}");
            writer.WriteLine($"{indentaiton}\tpass");
        }

        public static void WritePythonMethod(
            StreamWriter writer, 
            string methodName, 
            List<KeyValuePair<string, Type>> arguments,
            Type returnType,
            string docString,
            int indentLevel=1)
        {
            var pythonArgumentList = new List<string>();

            for (int i = 0; i < arguments.Count; i++)
            {
                var pair = arguments[i];
                pythonArgumentList.Add($"{pair.Key}: {TypeLibrary.ConvertTypeToPythonType(pair.Value)}");
            }

            var pythonArguments = string.Join(", ", pythonArgumentList);
            pythonArguments = String.IsNullOrEmpty(pythonArguments) ? pythonArguments : $", {pythonArguments}";

            var method = $"def {methodName}(self {pythonArguments}) -> {TypeLibrary.ConvertTypeToPythonType(returnType)}:";

            var indentaiton = GetIndentation(indentLevel);

            writer.WriteLine();
            writer.WriteLine($"{indentaiton}{method}");
            writer.WriteLine($"{indentaiton}{docString}");
            writer.WriteLine($"{indentaiton}\tpass");
        }

        public static void WritePythonProperty(
            StreamWriter writer,
            string propertyName,
            Type returnType,
            string docString,
            int indentLevel = 1)
        {
            var indentaiton = GetIndentation(indentLevel);

            writer.WriteLine();
            writer.WriteLine($"{indentaiton}@property");
            writer.WriteLine($"{indentaiton}def {propertyName}(self) -> {TypeLibrary.ConvertTypeToPythonType(returnType)}:");
            writer.WriteLine($"{indentaiton}{docString}");
            writer.WriteLine($"{indentaiton}\tpass");
        }

        public static void WritePythongPropertySetter(StreamWriter writer,
            string propertyName,            
            Type returnType,
            int indentLevel = 1)
        {
            var indentaiton = GetIndentation(indentLevel);

            writer.WriteLine();
            writer.WriteLine($"{indentaiton}@{propertyName}.setter");
            writer.WriteLine($"{indentaiton}def {propertyName}(self, {propertyName.ToLower()}: {TypeLibrary.ConvertTypeToPythonType(returnType)}) -> None:");
            writer.WriteLine($"{indentaiton}\tpass");
        }

        public static void WritePythonGenericClassDefinition(StreamWriter writer)
        {
            //
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
