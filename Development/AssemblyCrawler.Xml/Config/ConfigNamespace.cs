// ConfigNamespace.cs
// Copyright (c) 2021 Kristopher L. Culin See LICENSE for details

using System.Collections.Generic;
using System.Xml.Serialization;

namespace AssemblyCrawler.Support.Config
{
	[XmlType("Namespace")]
	public class ConfigNamespace
	{
		#region Constructor
		public ConfigNamespace()
		{
		}
		#endregion

		#region Public Properties
		public string Name { get; set; }
		public ClassType ClassType { get; set; }
		public List<ConfigClass> Classes { get; } = new List<ConfigClass>();
		#endregion
	}
}
