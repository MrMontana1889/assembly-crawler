// PythonImport.cs
// Copyright (c) 2022 Kristopher L. Culin See LICENSE for details

using System.Collections.Generic;
using System.Diagnostics;
using System.IO;

namespace AssemblyCrawler.Support
{
	[DebuggerDisplay("{Module} : {PythonTypes}")]
	public class PythonImport
	{
		#region Constructor
		public PythonImport(string module)
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
		public bool HasType(string pythonType)
		{
			return PythonTypes.Find(t => t == pythonType) != null;
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
