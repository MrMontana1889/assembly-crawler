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
	public class PythonPackage
	{
		#region Constructor
		public PythonPackage(string name)
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
		public PythonAssembly AddAssembly(Assembly assembly, string outputPath)
		{
			if (Assemblies.Find(a => a.Assembly.FullName == assembly.FullName) == null)
				Assemblies.Add(new PythonAssembly(this, assembly, outputPath));
			return Assemblies.Find(a => a.Assembly.FullName == assembly.FullName);
		}
		#endregion

		#region Public Properties
		public string PackageName { get; }
		public List<PythonAssembly> Assemblies { get; } = new List<PythonAssembly>();
		#endregion
	}
}
