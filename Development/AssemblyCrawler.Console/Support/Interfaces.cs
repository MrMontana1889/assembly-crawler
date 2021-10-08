// Interfaces.cs
// Copyright (c) 2021 Kristopher L. Culin See LICENSE for details

using System.Collections.Generic;
using CommandLine;

namespace AssemblyCrawler.Console.Support
{
	public interface IAssemblyFileOptions
	{
		[Option('a', "assemblies", SetName = "AssemblyFile", Required = true, HelpText = "Specify the assemblies to crawl", Min = 1)]
		IEnumerable<string> Assemblies { get; set; }

		[Option('x', "xmldoc", SetName = "AssemblyFile", Required = false, HelpText = "Specify the xml documents to extract", Min = 1)]
		IEnumerable<string> XmlDocuments { get; set; }

		[Option('o', "output", SetName = "AssemblyFile", Required = true, HelpText = "Full path to generate the stub files")]
		string OutputPath { get; set; }
	}

	public interface IConfigFileOptions
	{
		[Option('c', "config", SetName = "ConfigFile", Required = true, HelpText = "Specify the full path and filename of the options file.")]
		string ConfigFile { get; set; }
	}
}
