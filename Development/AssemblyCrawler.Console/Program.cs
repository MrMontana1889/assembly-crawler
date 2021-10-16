// Program.cs
// Copyright (c) 2021 Kristopher L. Culin See LICENSE for details

using System;
using System.Collections.Generic;
using System.IO;
using System.Linq;
using System.Reflection;
using AssemblyCrawler.Console.Support;
using AssemblyCrawler.Support;
using AssemblyCrawler.Xml.Config;
using AssemblyCrawler.Xml.Helpers;
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
				PythonPackage package = new PythonPackage("Package");

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
						crawler.Crawl(package, pair.Assembly, pair.XmlDocument, obj.OutputPath, new InterfacesOnlyTypeFilter(false));
					}
				}

				package.Write();
			}
			else
			{
				// Using a config file.
				// D:\repos\python\OpenFlows.config
				ConfigPackage pkg = XmlHelper.DeserializeFromFile<ConfigPackage>(obj.ConfigFile);
				if (pkg != null)
				{
					if (string.IsNullOrWhiteSpace(pkg.OutputPath))
					{
						WriteLine($"The output path was not specified.  This is a required attribute in the config file.");
						return;
					}
					if (string.IsNullOrWhiteSpace(pkg.DefaultAssemblyFolder))
					{
						WriteLine($"the default assembly folder is not specified.  This is a required attribute in the config file.");
						return;
					}

					if (!Directory.Exists(pkg.OutputPath))
						Directory.CreateDirectory(pkg.OutputPath);      // Make sure the output path exists.

					PythonPackage package = new PythonPackage("Package");

					// System assemblies should be processed first
					foreach (var assembly in pkg.SystemAssemblies)
					{
						Assembly netAssembly = null;
						if (assembly.Namespaces.Count == 0) continue;       // Ignore any without namespaces specified

						switch (assembly.AssemblyName)
						{
							case "System":
								netAssembly = Assembly.GetAssembly(typeof(Type));
								break;
							default:
								continue;
						}

						foreach (var assemblyNamespace in assembly.Namespaces)
						{
							if (assemblyNamespace.ClassType != ClassType.ClassListOnly) continue;       // Ignore in this case.
							if (assemblyNamespace.Classes.Count == 0) continue;                         // Ignore any where classes aren't specified.

							List<Type> classTypes = new List<Type>();
							foreach (var assemblyClass in assemblyNamespace.Classes)
							{
								string className = string.Join(Type.Delimiter.ToString(), assemblyNamespace.Name, assemblyClass.Name);
								Type classType = netAssembly.GetType(className);
								if (classType != null)
									classTypes.Add(classType);
							}

							ITypeFilter filter = new NamespaceTypeFilter(assemblyNamespace.ClassType,
								assemblyNamespace.Name, classTypes);
							IAssemblyCrawler crawler = new AssemblyCrawler();
							crawler.Crawl(package, assembly.AssemblyName, assembly.XmlDocument,
								pkg.OutputPath, filter);
						}
					}

					foreach (var assembly in pkg.Assemblies)
					{
						if (!string.IsNullOrWhiteSpace(pkg.DefaultAssemblyFolder) &&
							string.IsNullOrWhiteSpace(assembly.Folder))
							assembly.Folder = pkg.DefaultAssemblyFolder;

						if (File.Exists(assembly.AssemblyName))
						{
							// The file exists.  Verify it is valid .NET assembly
							if (DotNetObject.IsValidDotNetAssembly(assembly.AssemblyName))
							{
								/*
								 * Now need to check to see if any namespaces are specified.
								 * If there are NO namespaces, then the full assembly will be
								 * processed - and use the InterfaceOnly type filter (same as above)
								 * 
								 * If there are namespaces, then need to get the list of namespaces
								 * specified plus any classes, especially if the ClassType is set to
								 * InterfacesOnly.  if the class type is all, then all classes in
								 * the namespace are used.
								*/

								Assembly netAssembly = Assembly.LoadFrom(assembly.AssemblyName);

								if (assembly.Namespaces.Count == 0)
								{
									// Process the entier assembly

									ITypeFilter typeFilter = new InterfacesOnlyTypeFilter(false);
									if (assembly.Name.StartsWith("Haestad"))
										typeFilter = new HaestadTypeFilter();

									IAssemblyCrawler crawler = new AssemblyCrawler();
									crawler.Crawl(package, assembly.AssemblyName, assembly.XmlDocument,
										pkg.OutputPath, typeFilter);
								}
								else
								{
									// Need to crawl each individual namespace.
									foreach (var assemblyNamespace in assembly.Namespaces)
									{
										ITypeFilter filter = null;
										if (assemblyNamespace.Classes.Count == 0)
										{
											// There are no specific classes to process.
											filter = new NamespaceTypeFilter(assemblyNamespace.ClassType,
												assemblyNamespace.Name, new List<Type>());
										}
										else
										{
											List<Type> classTypes = new List<Type>();
											//Create the list of types from the list of classes.
											foreach (var assemblyClass in assemblyNamespace.Classes)
											{
												string className = string.Join(Type.Delimiter.ToString(), assemblyNamespace.Name, assemblyClass.Name);
												Type classType = netAssembly.GetType(className, false, true);
												if (classType != null)
													classTypes.Add(classType);
											}

											filter = new NamespaceTypeFilter(assemblyNamespace.ClassType,
												assemblyNamespace.Name, classTypes);
										}

										if (filter != null)
										{
											IAssemblyCrawler crawler = new AssemblyCrawler();
											crawler.Crawl(package, assembly.AssemblyName, assembly.XmlDocument,
												pkg.OutputPath, filter);
										}
									}
								}
							}
						}
						else
						{
							WriteLine($"The assembly {assembly.AssemblyName} was not found.");
						}
					}

					package.Write();
				}
			}
		}
		#endregion
	}
}
