// ConfigNamespace.cs
// Copyright (c) 2021 Kristopher L. Culin See LICENSE for details

using System.Collections.Generic;

namespace AssemblyCrawler.Support.Config
{
	public class ConfigNamespace
	{
		#region Constructor
		public ConfigNamespace(string name, ClassType classType)
		{
			Name = name;
			ClassType = classType;
		}
		#endregion

		#region Public Properties
		public string Name { get; }
		public ClassType ClassType { get; }
		public List<ConfigClass> Classes { get; } = new List<ConfigClass>();
		#endregion
	}
}
