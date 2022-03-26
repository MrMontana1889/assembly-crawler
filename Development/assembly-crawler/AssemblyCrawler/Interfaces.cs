// Interfaces.cs
// Copyright (c) 2022 Kristopher L. Culin See LICENSE for details

using System;
using AssemblyCrawler.Support;
using Barber.AutoDiagrammer.Support;

namespace AssemblyCrawler
{
	public interface IStubGenerator
	{
		/// <summary>
		/// Geneates the stub given the type.
		/// All classes will be included whether public, protected, private or internal
		/// Public methods, properties and fields will then be processed.
		/// </summary>
		/// <param name="type">The type to crawl and generate stubs for</param>
		/// <param name="xmlDocumentFileName">The full path and filename of the xml documentation.</param>
		void GenerateTypeStub(Type type, string xmlDocumentFileName);
	}

	public interface IAssemblyCrawler
	{
		/// <summary>
		/// Crawls thru the assembly looking for public, internal, protected classes
		/// and generates the stubs for those classes.
		/// </summary>
		/// <param name="assemblyFilename">The full path and filename of the assembly to crawl.</param>
		/// <param name="xmlDocumentFileName">The full path and filename of the xml documentation.</param>
		/// <param name="outputPath">The path where the stub files will be written</param>
		void Crawl(PythonPackage package, string assemblyFilename,
			string xmlDocumentFileName, string outputPath, ITypeFilter typeFilter);
	}
}
