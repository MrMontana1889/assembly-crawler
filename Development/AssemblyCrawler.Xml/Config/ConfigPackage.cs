// ConfigPackage.cs
// Copyright (c) 2021 Kristopher L. Culin See LICENSE for details

using System.Collections.Generic;
using System.Xml.Serialization;

namespace AssemblyCrawler.Support.Config
{
	[XmlType("Package")]
	public class ConfigPackage
	{
		#region Constructor
		public ConfigPackage()
		{
			
		}
		#endregion

		#region Public Properties
		public string OutputPath { get; set; }
		public List<ConfigAssembly> Assemblies { get; } = new List<ConfigAssembly>();
		#endregion
	}
}
