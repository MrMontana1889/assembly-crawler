// Program.cs
// Copyright (c) 2021 Kristopher L. Culin See LICENSE for details

using System.Collections.Generic;
using System.IO;
using System.Linq;
using AssemblyCrawler.Console.Support;
using AssemblyCrawler.Support;
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
			try { Read(); }
			catch { }
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
			if (obj.ConfigFile == null)
			{
				PythonPackageDefinition package = new PythonPackageDefinition("Package");

				// make usre obj.Assemblies and obj.XML document are same size
				if (obj.Assemblies.Count() != obj.XmlDocuments.Count())
				{
					WriteLine($"Error: Number of assemblies must match with number of xml documet files. Pass empty string if xml document is missing");
					return;
				}

				var assemblyAndXmlDocPairs = obj.Assemblies.Zip(obj.XmlDocuments, (a, x) => new { Assembly = a, XmlDocument = x });
				foreach (var pair in assemblyAndXmlDocPairs)
				{
					if (!File.Exists(pair.Assembly))
					{
						WriteLine($"The assembly {pair.Assembly} does not exist.");
						continue;
					}

					if (DotNetObject.IsValidDotNetAssembly(pair.Assembly))
					{
						if (!Directory.Exists(obj.OutputPath))
							Directory.CreateDirectory(obj.OutputPath);

						IAssemblyCrawler crawler = new AssemblyCrawler();
						crawler.Crawl(package, pair.Assembly, pair.XmlDocument, obj.OutputPath, new InterfacesOnlyTypeFilter());
					}
				}

				package.Write();
			}
			else
			{
				// Using a config file.
			}
		}
		#endregion
	}
}
