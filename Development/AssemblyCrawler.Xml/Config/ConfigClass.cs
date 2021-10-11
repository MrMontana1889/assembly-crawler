// ConfigClass.cs
// Copyright (c) 2021 Kristopher L. Culin See LICENSE for details

using System.Diagnostics;
using System.Xml.Serialization;

namespace AssemblyCrawler.Xml.Config
{
	[XmlType("Class")]
	[DebuggerDisplay("{Name}")]
	public class ConfigClass
	{
		#region Constructor
		public ConfigClass()
		{

		}
		#endregion

		#region Public Properties
		public string Name { get; set; }
		#endregion
	}
}
