// AssemblyCrawler.cs
// Copyright (c) 2021 Kristopher L. Culin See LICENSE for details

using System;
using System.Collections.Generic;
using System.IO;
using System.Linq;
using System.Reflection;
using System.Security.Policy;
using AssemblyCrawler.Support;
using Barber.AutoDiagrammer;
using Barber.AutoDiagrammer.GraphBits;
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
		public void Crawl(PythonPackage package, string assemblyFilename,
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

			if (assemblyFilename.StartsWith("System") || DotNetObject.IsValidDotNetAssembly(assemblyFilename))
			{
				// Valid.  Continue.

				IAssemblyManipulationService assemblyManipulationService = new AssemblyManipulationService();

				SettingsViewModel.Instance.SetGraphObject(null);
				SettingsViewModel.Instance.LayoutAlgorithmType = "Tree";
				SettingsViewModel.Instance.IncludeConstructorParametersAsAssociations = false;
				SettingsViewModel.Instance.IncludeFieldTypesAsAssociations = false;
				SettingsViewModel.Instance.IncludeMethodArgumentAsAssociations = false;
				SettingsViewModel.Instance.IncludePropertyTypesAsAssociations = false;

				SimpleTreeLayoutParametersEx settings = (SimpleTreeLayoutParametersEx)SettingsViewModel.Instance.LayoutParameters;
				settings.Direction = GraphSharp.Algorithms.Layout.LayoutDirection.LeftToRight;

				assemblyManipulationService.LoadNameSpacesAndTypesAsync(assemblyFilename, typeFilter);

				if (assemblyManipulationService.TreeValues.Count == 1)
				{
					// Loaded successfully.
					assemblyManipulationService.TreeValues[0].IsChecked = true;
					RecursivelyAddItems(assemblyManipulationService, assemblyManipulationService.TreeValues[0]);

					var graphResults = assemblyManipulationService.CreateGraph();

					Assembly assembly = null;
					if (!assemblyFilename.Contains("System"))
					{
						AssemblyName assemblyName = AssemblyName.GetAssemblyName(assemblyFilename);
						assembly = Assembly.Load(assemblyName);
					}
					else
					{
						switch (assemblyFilename)
						{
							case "System":
								assembly = Assembly.GetAssembly(typeof(Type));
								break;
							default:
								Console.WriteLine($"{assemblyFilename} unknown.");
								return;
						}
					}

					if (assembly == null)
						return;

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

						string joinedFilename = string.Join(@"\", tokens);
						if (IsInvalidFilename(joinedFilename, Path.GetInvalidPathChars()))
							continue;

						if (joinedFilename == "std")
							continue;

						string path = Path.Combine(outputPath, joinedFilename);
						if (!Directory.Exists(path))
							Directory.CreateDirectory(path);

						if (filename == "std")
							continue;

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

						PythonModule module = assemblyDef.AddModule(type.Value.First().Namespace, pyiFilename, xmlDocumentFileName);
						foreach (Type t in type.Value)
							module.AddClassDefinition(t);
					}
				}
			}
		}

		private bool IsInvalidFilename(string joinedFilename, char[] invalidChars)
		{
			foreach (var c in invalidChars)
				if (joinedFilename.Contains(c.ToString()))
					return true;
			return false;
		}
		#endregion

		#region Private Methods
		private void RecursivelyAddItems(IAssemblyManipulationService assemblyManipulationService, AssemblyTreeViewModel model)
		{
			if (model.NodeType != RepresentationType.Class)
			{
				foreach (var child in model.Children)
				{
					if (child.NodeType == RepresentationType.Class)
						assemblyManipulationService.SelectedTreeValues.Add(child);
					else
						RecursivelyAddItems(assemblyManipulationService, child);
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
	}
}
