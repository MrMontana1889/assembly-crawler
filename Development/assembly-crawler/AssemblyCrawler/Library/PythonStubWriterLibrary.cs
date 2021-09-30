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

		#region Public Methods
		public static void WritePythonClassDefinition(
			StreamWriter writer,
			string className,
			List<Type> inheritedTypes,
			string docString,
			int indentLevel = 0)
		{
			var inhertedTypesString = string.Join(", ", inheritedTypes.Select(t => TypeLibrary.ConvertTypeToPythonType(t)));
			var classString = $"{CLASS} {className}({inhertedTypesString}):";

			var indentaiton = GetIndentation(indentLevel);

			writer.WriteLine();
			writer.WriteLine();
			writer.WriteLine($"{indentaiton}{CLASS} {className}({inhertedTypesString}):");
			writer.WriteLine($"{indentaiton}{docString}");
			writer.WriteLine($"{indentaiton}\t{PASS}");
		}

		public static void WritePythonMethod(
			StreamWriter writer,
			string methodName,
			List<KeyValuePair<string, Type>> arguments,
			Type returnType,
			string docString,
			int indentLevel = 1)
		{
			var pythonArgumentList = new List<string>();

			for (int i = 0; i < arguments.Count; i++)
			{
				var pair = arguments[i];
				pythonArgumentList.Add($"{pair.Key}: {TypeLibrary.ConvertTypeToPythonType(pair.Value)}");
			}

			var pythonArguments = string.Join(", ", pythonArgumentList);
			pythonArguments = string.IsNullOrEmpty(pythonArguments) ? pythonArguments : $", {pythonArguments}";

			var method = $"{DEF} {methodName}({SELF} {pythonArguments}) -> {TypeLibrary.ConvertTypeToPythonType(returnType)}:";

			var indentaiton = GetIndentation(indentLevel);

			writer.WriteLine();
			writer.WriteLine($"{indentaiton}{method}");
			writer.WriteLine($"{indentaiton}{docString}");
			writer.WriteLine($"{indentaiton}\t{PASS}");
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
			writer.WriteLine($"{indentaiton}{PROPERTY}");
			writer.WriteLine($"{indentaiton}{DEF} {propertyName}({PASS}) -> {TypeLibrary.ConvertTypeToPythonType(returnType)}:");
			writer.WriteLine($"{indentaiton}{docString}");
			writer.WriteLine($"{indentaiton}\t{PASS}");
		}

		public static void WritePythongPropertySetter(StreamWriter writer,
			string propertyName,
			Type returnType,
			int indentLevel = 1)
		{
			var indentaiton = GetIndentation(indentLevel);

			writer.WriteLine();
			writer.WriteLine($"{indentaiton}@{propertyName}{SETTER}");
			writer.WriteLine($"{indentaiton}{DEF} {propertyName}({SELF}, {propertyName.ToLower()}: {TypeLibrary.ConvertTypeToPythonType(returnType)}) -> {NONETYPE}:");
			writer.WriteLine($"{indentaiton}\t{PASS}");
		}

		public static void WritePythonGenericClassDefinition(StreamWriter writer)
		{
			//
		}
		#endregion

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
