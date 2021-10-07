// ConfigPackage.cs
// Copyright (c) 2021 Kristopher L. Culin See LICENSE for details

using System.Collections.Generic;
using System.Xml.Serialization;

namespace AssemblyCrawler.Support.Config
{
	[XmlRoot]
	public class ConfigPackage
	{
		#region Constructor
		public ConfigPackage(string outputPath)
		{
			OutputPath = outputPath;
		}
		#endregion

		#region Public Properties
		public string OutputPath { get; }
		public List<ConfigAssembly> Assemblies { get; } = new List<ConfigAssembly>();
		#endregion
	}
}
