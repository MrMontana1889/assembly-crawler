// ConfigClass.cs
// Copyright (c) 2021 Kristopher L. Culin See LICENSE for details

using System;
using System.Xml.Serialization;

namespace AssemblyCrawler.Support.Config
{
	[XmlType("Class")]
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
