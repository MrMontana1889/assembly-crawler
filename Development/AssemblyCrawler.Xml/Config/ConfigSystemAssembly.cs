// ConfigSystemAssembly.cs
// Copyright (c) 2022 Kristopher L. Culin See LICENSE for details

using System.Collections.Generic;
using System.Diagnostics;
using System.Xml.Serialization;

namespace AssemblyCrawler.Xml.Config
{
	[XmlType("SystemAssembly")]
	[DebuggerDisplay("{AssemblyName}")]
	public class ConfigSystemAssembly
	{
		#region Public Properties
		public string Name { get; set; }
		public string XmlDoc { get; set; } = "";
		[XmlIgnore]
		public string AssemblyName => Name;
		[XmlIgnore]
		public string XmlDocument => string.Empty;
		public List<ConfigNamespace> Namespaces { get; } = new List<ConfigNamespace>();
		#endregion
	}
}
