// PythonClassDefinition.cs
// Copyright (c) 2021 Kristopher L. Culin See LICENSE for details

using System.IO;
using System.Text;

namespace AssemblyCrawler.Support
{
	public class PythonClassDefinition
	{
		#region Constructor
		public PythonClassDefinition(PythonModuleDefinition module, string fullName, string className)
		{
			Module = module;
			FullName = fullName;
			ClassName = className;
		}
		#endregion

		#region Public Methods
		public void Write(StreamWriter sw)
		{
			sw.Write(ClassDefinition.ToString());
			sw.Write(Methods.ToString());
			sw.Write(Properties.ToString());
			sw.WriteLine();
		}
		#endregion

		#region Public Properties
		public PythonModuleDefinition Module { get; }
		public string FullName { get; }
		public string ClassName { get; }
		public StringBuilder ClassDefinition { get; } = new StringBuilder();
		public StringBuilder Methods { get; } = new StringBuilder();
		public StringBuilder Properties { get; } = new StringBuilder();
		#endregion
	}
}
