// Crawler.cs
// Copyright (c) 2021 Kristopher L. Culin.  See LICENSE for details.

using System;
using System.Collections.Generic;
using System.IO;
using System.Reflection;
using System.Security.Policy;
using System.Text;
using AssemblyCrawler.Generators;
using Barber.AutoDiagrammer;
using Barber.AutoDiagrammer.Models;
using Barber.AutoDiagrammer.Services;
using Barber.AutoDiagrammer.Support;

namespace AssemblyCrawler
{
	public class AssemblyCrawler : IAssemblyCrawler
	{
		#region Constructor
		public AssemblyCrawler()
		{

		}
		#endregion

		#region Public Methods
		public void Crawl(string assemblyFilename, string outputPath)
		{
			/*
			 * First crawl the assembly and generate the interface tree using Barber.AutoDiagrammer.
			 * Then create the graph hierarchy which produces the list of interfaces from the bottom up.
			 * 
			 * Create a child domain to load the assembly given the full path and filename.
			 * Loop through the list of interfaces and create a dictionary of filename to list of classes
			 * The key will be the name of the pyi file to write to.  The value will be the list of
			 * interfaces, in order, to write to that file.
			*/

			if (DotNetObject.IsValidDotNetAssembly(assemblyFilename))
			{
				// Valid.  Continue.

				AssemblyManipulationService.LoadNameSpacesAndTypesAsync(assemblyFilename);

				if (AssemblyManipulationService.TreeValues.Count == 1)
				{
					// Loaded successfully.
					AssemblyManipulationService.TreeValues[0].IsChecked = true;
					RecursivelyAddItems(AssemblyManipulationService.TreeValues[0]);

					var graphResults = AssemblyManipulationService.CreateGraph();

					//AppDomain childDomain = BuildChildDomain(AppDomain.CurrentDomain, assemblyFilename);

					try
					{
						AssemblyName assemblyName = AssemblyName.GetAssemblyName(assemblyFilename);
						//Assembly assembly = childDomain.Load(assemblyFilename);
						Assembly assembly = Assembly.Load(assemblyName);

						IDictionary<string, List<Type>> typeMap = new Dictionary<string, List<Type>>(graphResults.Vertices.Count);

						foreach (var v in graphResults.Vertices)
						{
							// Determine the filename.
							string[] tokens = v.Name.Split(Type.Delimiter);
							// Last one is the interface name, second to las tis the filename to use

							string filename = filename = tokens[tokens.Length - 2];

							if (tokens.Length > 2)
								Array.Resize(ref tokens, tokens.Length - 2);
							else
								Array.Resize(ref tokens, tokens.Length - 1);

							string path = Path.Combine(outputPath, string.Join(@"\", tokens));
							if (!Directory.Exists(path))
								Directory.CreateDirectory(path);

							filename = filename + ".pyi";

							filename = Path.Combine(path, filename);

							if (!typeMap.ContainsKey(filename))
								typeMap.Add(filename, new List<Type>());

							Type t = assembly.GetType(v.Name);
							typeMap[filename].Add(t);
						}

						foreach (KeyValuePair<string, List<Type>> type in typeMap)
						{
							string pyiFilename = Path.Combine(outputPath, type.Key);
							Console.WriteLine(pyiFilename);
							using (FileStream fileStream = new FileStream(pyiFilename, FileMode.Create, FileAccess.ReadWrite, FileShare.ReadWrite))
							{
								using (StreamWriter sw = new StreamWriter(fileStream, Encoding.ASCII))
								{
									IStubGenerator generator = GeneratorLibrary.NewPythonStubGenerator(sw);

									foreach (Type t in type.Value)
									{
										generator.GenerateTypeStub(t);
									}
								}
							}
						}
					}
					finally
					{
						//AppDomain.Unload(childDomain);
					}
				}
			}
		}
		#endregion

		#region Private Methods
		private void RecursivelyAddItems(AssemblyTreeViewModel model)
		{
			if (model.NodeType != RepresentationType.Class)
			{
				foreach (var child in model.Children)
				{
					if (child.NodeType == RepresentationType.Class)
						AssemblyManipulationService.SelectedTreeValues.Add(child);
					else
						RecursivelyAddItems(child);
				}
			}
		}
		private AppDomain BuildChildDomain(AppDomain parentDomain, string fileName)
		{
			Evidence evidence = new Evidence(parentDomain.Evidence);
			AppDomainSetup setup = parentDomain.SetupInformation;
			FileInfo fi = new FileInfo(fileName);
			AppDomain newAppDomain = AppDomain.CreateDomain("DiscoveryRegion", evidence, setup);


			return newAppDomain;
		}
		#endregion

		#region Private Properties
		private IAssemblyManipulationService AssemblyManipulationService { get; } = new AssemblyManipulationService();
		#endregion
	}
}
