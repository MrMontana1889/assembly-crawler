// ConfigClass.cs
// Copyright (c) 2021 Kristopher L. Culin See LICENSE for details

using System;

namespace AssemblyCrawler.Support.Config
{
	public class ConfigClass
	{
		#region Constructor
		public ConfigClass(ConfigNamespace classNamespace, string name)
		{
			ClassNamespace = classNamespace;
			Name = name;
		}
		#endregion

		#region Public Properties
		public ConfigNamespace ClassNamespace { get; }
		public string Name { get; }
		public string ClassName => string.Join(Type.Delimiter.ToString(), ClassNamespace.Name, Name);
		#endregion
	}
}
