// Interfaces.cs
// Copyright (c) 2021 Kristopher L. Culin See LICENSE for details

using System.Collections.Generic;
using CommandLine;

namespace AssemblyCrawler.Console.Support
{
	public interface IAssemblyFileOptions
	{
		[Option('a', "assemblies", SetName = "AssemblyFile", Min = 1, HelpText = "Specify the assemblies to crawl")]
		IEnumerable<string> Assemblies { get; set; }

		[Option('x', "xmldoc", SetName = "AssemblyFile", Min = 1, HelpText = "Specify the xml documents to extract")]
		IEnumerable<string> XmlDocuments { get; set; }

		[Option('o', "output", SetName = "AssemblyFile", HelpText = "Full path to generate the stub files")]
		string OutputPath { get; set; }
	}

	public interface IConfigFileOptions
	{
		[Option('c', "config", SetName = "ConfigFile", HelpText = "Specify the full path and filename of the options file.")]
		string ConfigFile { get; set; }
	}
}
