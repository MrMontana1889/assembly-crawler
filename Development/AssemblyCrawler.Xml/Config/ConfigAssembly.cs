// ConfigAssembly.cs
// Copyright (c) 2022 Kristopher L. Culin See LICENSE for details

using System.Collections.Generic;
using System.Diagnostics;
using System.IO;
using System.Xml.Serialization;

namespace AssemblyCrawler.Xml.Config
{
	[XmlType("Assembly")]
	[DebuggerDisplay("{AssemblyName}")]
	public class ConfigAssembly
	{
		#region Constructor
		public ConfigAssembly()
		{

		}
		#endregion

		#region Public Properties
		public string Folder { get; set; }
		public string Name { get; set; }
		public string XmlDoc { get; set; } = "";
		[XmlIgnore]
		public string AssemblyName => Path.Combine(Folder, Name);
		[XmlIgnore]
		public string XmlDocument => Path.Combine(Folder, XmlDoc);
		public List<ConfigNamespace> Namespaces { get; } = new List<ConfigNamespace>();
		#endregion
	}
}
