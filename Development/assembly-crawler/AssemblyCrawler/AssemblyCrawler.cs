// AssemblyCrawler.cs
// Copyright (c) 2021 Kristopher L. Culin See LICENSE for details

using System.Linq;
using System;
using System.Collections.Generic;
using System.IO;
using System.Reflection;
using System.Security.Policy;
using AssemblyCrawler.Generators;
using AssemblyCrawler.Support;
using Barber.AutoDiagrammer;
using Barber.AutoDiagrammer.Models;
using Barber.AutoDiagrammer.Services;
using Barber.AutoDiagrammer.Support;
using Barber.AutoDiagrammer.GraphBits;

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
		public void Crawl(PythonPackageDefinition package, string assemblyFilename, 
			string xmlDocumentFileName, string outputPath, ITypeFilter typeFilter)
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

				SettingsViewModel.Instance.SetGraphObject(null);
				SettingsViewModel.Instance.LayoutAlgorithmType = "Tree";
				SettingsViewModel.Instance.IncludeConstructorParametersAsAssociations = false;
				SettingsViewModel.Instance.IncludeFieldTypesAsAssociations = false;
				SettingsViewModel.Instance.IncludeMethodArgumentAsAssociations = false;
				SettingsViewModel.Instance.IncludePropertyTypesAsAssociations = false;

				SimpleTreeLayoutParametersEx settings = (SimpleTreeLayoutParametersEx)SettingsViewModel.Instance.LayoutParameters;
				settings.Direction = GraphSharp.Algorithms.Layout.LayoutDirection.LeftToRight;

				AssemblyManipulationService.LoadNameSpacesAndTypesAsync(assemblyFilename, typeFilter);

				if (AssemblyManipulationService.TreeValues.Count == 1)
				{
					// Loaded successfully.
					AssemblyManipulationService.TreeValues[0].IsChecked = true;
					RecursivelyAddItems(AssemblyManipulationService.TreeValues[0]);

					var graphResults = AssemblyManipulationService.CreateGraph();

					AssemblyName assemblyName = AssemblyName.GetAssemblyName(assemblyFilename);
					Assembly assembly = Assembly.Load(assemblyName);

					var assemblyDef = package.AddAssembly(assembly, outputPath);

					IDictionary<string, List<Type>> typeMap = new Dictionary<string, List<Type>>(graphResults.Vertices.Count);

					foreach (var v in graphResults.Vertices)
					{
						// Determine the filename.
						string[] tokens = v.Name.Split(Type.Delimiter);

						// Last one is the interface name, second to last is the module name to use
						string filename = tokens[tokens.Length - 2];

						if (tokens.Length > 2)
							Array.Resize(ref tokens, tokens.Length - 2);
						else
							Array.Resize(ref tokens, tokens.Length - 1);

						string path = Path.Combine(outputPath, string.Join(@"\", tokens));
						if (!Directory.Exists(path))
							Directory.CreateDirectory(path);

						filename += ".pyi";

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

						PythonModuleDefinition module = assemblyDef.AddModule(type.Value.First().Namespace, pyiFilename);
						IStubGenerator generator = GeneratorLibrary.NewPythonStubGenerator(module);

						foreach (Type t in type.Value)
							generator.GenerateTypeStub(t, xmlDocumentFileName);
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
