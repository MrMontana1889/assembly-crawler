// PythonPackageDefinition.cs
// Copyright (c) 2021 Kristopher L. Culin See LICENSE for details

using System.Collections.Generic;
using System.Reflection;

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
		public void Write()
		{
			foreach (var assembly in Assemblies)
				assembly.Write();
		}
		public PythonAssemblyDefinition AddAssembly(Assembly assembly, string outputPath)
		{
			if (Assemblies.Find(a => a.Assembly.FullName == assembly.FullName) == null)
				Assemblies.Add(new PythonAssemblyDefinition(this, assembly, outputPath));
			return Assemblies.Find(a => a.Assembly.FullName == assembly.FullName);
		}
		#endregion

		#region Public Properties
		public string PackageName { get; }
		public List<PythonAssemblyDefinition> Assemblies { get; } = new List<PythonAssemblyDefinition>();
		#endregion
	}
}
