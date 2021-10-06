// PythonAssemblyDefinition.cs
// Copyright (c) 2021 Kristopher L. Culin See LICENSE for details

using System;
using System.Collections.Generic;
using System.IO;
using System.Reflection;
using System.Text;

namespace AssemblyCrawler.Support
{
	public class PythonAssemblyDefinition
	{
		#region Constructor
		public PythonAssemblyDefinition(PythonPackageDefinition package, Assembly assembly, string outputPath)
		{
			Package = package;
			Assembly = assembly;
			OutputPath = outputPath;
		}
		#endregion

		#region Public Methods
		public void Write()
		{
			foreach (var module in Modules)
				module.Write();
		}
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
		public void AddEnum(Type enumType)
		{
			if (Enumerations.Find(e => e.Name == enumType.Name) == null)
				Enumerations.Add(enumType);
		}
		#endregion

		#region Public Properties
		public List<PythonModuleDefinition> Modules { get; } = new List<PythonModuleDefinition>();
		public List<Type> Enumerations { get; } = new List<Type>();
		public PythonPackageDefinition Package { get; }
		public Assembly Assembly { get; }
		public string OutputPath { get; }
		#endregion
	}
}
