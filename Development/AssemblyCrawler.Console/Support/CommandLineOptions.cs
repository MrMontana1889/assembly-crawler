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

	public class CommandLineOptions : IAssemblyFileOptions, IConfigFileOptions
	{
		public IEnumerable<string> Assemblies
		{
			get;
			set;
		}
		public IEnumerable<string> XmlDocuments
		{
			get;
			set;
		}
		public string OutputPath
		{
			get;
			set;
		}

		public string ConfigFile { get; set; }

		[Option('t', "StubType", Required = false, HelpText = "Specify the type of stub.  Python is default.")]
		public StubType StubType
		{
			get;
			set;
		}
	}
}
