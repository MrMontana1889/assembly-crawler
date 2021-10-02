// PythonPackageDefinition.cs
// Copyright (c) 2021 Kristopher L. Culin See LICENSE for details

using System.Collections.Generic;

namespace AssemblyCrawler.Support
{
	/// <summary>
	/// Contains a list of modules that make up the package
	/// The modules can span multiple assemblies
	/// </summary>
	public class PythonPackageDefinition
	{
		#region Constructor
		public PythonPackageDefinition(string name)
		{
			PackageName = name;
		}
		#endregion

		#region Public Methods
		public PythonModuleDefinition AddModule(string moduleNamespace, string filename)
		{
			if (Modules.Find(m => m.Filename == filename) == null)
				Modules.Add(new PythonModuleDefinition(this, moduleNamespace, filename));
			return GetModule(filename);
		}
		public PythonModuleDefinition GetModule(string filename)
		{
			return Modules.Find(m => m.Filename == filename);
		}
		#endregion

		#region Public Properties
		public string PackageName { get; }
		public List<PythonModuleDefinition> Modules { get; } = new List<PythonModuleDefinition>();
		#endregion
	}
}
