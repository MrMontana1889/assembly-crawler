// ImportDefinition.cs
// Copyright (c) 2021 Kristopher L. Culin See LICENSE for details

using System.Collections.Generic;
using System.Diagnostics;
using System.IO;

namespace AssemblyCrawler.Support
{
	[DebuggerDisplay("{MOdule} : {PythonTypes}")]
	public class ImportDefinition
	{
		#region Constructor
		public ImportDefinition(string module)
		{
			Module = module;
		}
		#endregion

		#region Public Methods
		public void AddType(string pythonType)
		{
			if (PythonTypes.Find(t => t == pythonType) == null)
			{
				PythonTypes.Add(pythonType);
			}
		}
		public void Write(StreamWriter sw)
		{
			sw.Write($"from {Module} import ");
			string types = string.Join(", ", PythonTypes.ToArray());
			sw.WriteLine(types);
		}
		#endregion

		#region Public Properties
		public string Module { get; }
		#endregion

		#region Private Properties
		private List<string> PythonTypes { get; } = new List<string>();
		#endregion
	}
}
