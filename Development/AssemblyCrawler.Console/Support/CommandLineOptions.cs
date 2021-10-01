// CommandLineOptions.cs
// Copyright (c) 2021 Kristopher L. Culin See LICENSE for details

using System.Collections.Generic;
using CommandLine;

namespace AssemblyCrawler.Console.Support
{
	public enum StubType
	{
		Python,
		NET,
	}

	public class CommandLineOptions
	{
		[Option('a', "assemblies", Required = true, HelpText = "Specify the assemblies to crawl", Min = 1)]
		public IEnumerable<string> Assemblies
		{
			get;
			set;
		}
		[Option('o', "output", Required = true, HelpText = "Full path to generate the stub files")]
		public string OutputPath
		{
			get;
			set;
		}

		[Option('t', "StubType", Required = false, HelpText = "Specify the type of stub.  Python is default.")]
		public StubType SubType
		{
			get;
			set;
		}
	}
}
