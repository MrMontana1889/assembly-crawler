// PythonAssemblyDefinition.cs
// Copyright (c) 2021 Kristopher L. Culin See LICENSE for details

using System;
using System.Collections.Generic;
using System.Reflection;

namespace AssemblyCrawler.Support
{
	public class PythonAssembly
	{
		#region Constructor
		public PythonAssembly(PythonPackage package, Assembly assembly, string outputPath)
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
		public PythonModule AddModule(string moduleNamespace, string filename, string xmlFilename)
		{
			if (Modules.Find(m => m.Filename == filename) == null)
				Modules.Add(new PythonModule(this, moduleNamespace, filename, xmlFilename));
			return GetModule(filename);
		}
		public PythonModule GetModule(string filename)
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
		public List<PythonModule> Modules { get; } = new List<PythonModule>();
		public List<Type> Enumerations { get; } = new List<Type>();
		public PythonPackage Package { get; }
		public Assembly Assembly { get; }
		public string OutputPath { get; }
		#endregion
	}
}
