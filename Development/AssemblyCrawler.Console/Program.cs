// Program.cs
// Copyright (c) 2021 Kristopher L. Culin See LICENSE for details

using System.Collections.Generic;
using System.IO;
using AssemblyCrawler.Console.Support;
using Barber.AutoDiagrammer.Support;
using CommandLine;
using static System.Console;

namespace AssemblyCrawler.Console
{
	internal static class Program
	{
		#region Public Methods
		static void Main(string[] args)
		{
			Parser.Default.ParseArguments<CommandLineOptions>(args)
				.WithParsed(RunOptions)
				.WithNotParsed(HandleParserErrors);


			Write("Press any key to continue...");
			ReadKey();
		}
		#endregion

		#region Private Methods
		private static void HandleParserErrors(IEnumerable<Error> obj)
		{
			if (!obj.IsVersion() && !obj.IsHelp())
				WriteLine("Error!");
		}

		private static void RunOptions(CommandLineOptions obj)
		{
			foreach (var assemblyFile in obj.Assemblies)
			{
				if (!File.Exists(assemblyFile))
				{
					WriteLine($"The assembly {assemblyFile} does not exist.");
					continue;
				}

				if (DotNetObject.IsValidDotNetAssembly(assemblyFile))
				{
					if (!Directory.Exists(obj.OutputPath))
						Directory.CreateDirectory(obj.OutputPath);

					IAssemblyCrawler crawler = new AssemblyCrawler();
					crawler.Crawl(assemblyFile, obj.OutputPath);
				}
			}
		}
		#endregion
	}
}
