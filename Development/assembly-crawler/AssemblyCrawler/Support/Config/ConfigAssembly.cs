// ConfigAssembly.cs
// Copyright (c) 2021 Kristopher L. Culin See LICENSE for details

using System.Collections.Generic;
using System.IO;

namespace AssemblyCrawler.Support.Config
{
	public class ConfigAssembly
	{
		#region Constructor
		public ConfigAssembly(string folder, string name, string xmlDoc)
		{
			Folder = folder;
			Name = name;
			XmlDoc = xmlDoc;
		}
		#endregion

		#region Public Properties
		public string Folder { get; }
		public string Name { get; }
		public string XmlDoc { get; }
		public string AssemblyName => Path.Combine(Folder, Name);
		public string XmlDocument => Path.Combine(Folder, XmlDoc);
		public List<ConfigNamespace> Namespaces { get; } = new List<ConfigNamespace>();
		#endregion
	}
}
