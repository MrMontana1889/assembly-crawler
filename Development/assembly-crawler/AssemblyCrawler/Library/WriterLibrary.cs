// WriterLibrary.cs
// Copyright (c) 2021 Kristopher L. Culin see LICENSE for details

using System;
using System.Linq;
using AssemblyCrawler.Support;
using static AssemblyCrawler.Support.Constants;

namespace AssemblyCrawler.Library
{
	public static class WriterLibrary
	{
		#region Public Methods
		public static string GetIndentation(int count)
		{
			var tabs = string.Empty;
			for (int i = 0; i < count; i++) tabs += $"{TAB}";
			return tabs;
		}
		public static string CorrectClassName(string name, int count)
		{
			return name.Replace($"`{count}", "");
		}
		public static string CorrectClassName(string name)
		{
			var tokens = name.Split('`');
			if (tokens.Length == 0) return name;
			return tokens.First();
		}
		public static void AddReferenceImports(PythonModule module, Type interf)
		{
			if (interf == typeof(void))
				return;

			TypeConvertLibrary.AddImportForPythonType(module, interf);
		}
		#endregion
	}
}
