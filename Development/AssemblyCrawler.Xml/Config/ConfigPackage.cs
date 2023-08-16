// ConfigPackage.cs
// Copyright (c) 2022 Kristopher L. Culin See LICENSE for details

using System;
using System.Collections.Generic;
using System.Diagnostics;
using System.Xml.Serialization;

namespace AssemblyCrawler.Xml.Config
{
    [XmlType("Package")]
    [DebuggerDisplay("{OutputPath}")]
    public class ConfigPackage
    {
        #region Constructor
        public ConfigPackage()
        {

        }
        #endregion

        #region Public Properties
        public string OutputPath
        {
            get { return outputPath; }
            set
            {
                outputPath = value.Contains("%")
                    ? Environment.ExpandEnvironmentVariables(value)
                    : value;
            }

        }
        public string DefaultAssemblyFolder { get; set; }
        public List<ConfigAssembly> Assemblies { get; } = new List<ConfigAssembly>();
        public List<ConfigSystemAssembly> SystemAssemblies { get; } = new List<ConfigSystemAssembly>();
        #endregion

        #region Fields
        private string outputPath;
        #endregion
    }
}
