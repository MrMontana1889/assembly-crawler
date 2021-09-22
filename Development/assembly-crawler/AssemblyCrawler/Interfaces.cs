// Interfaces.cs
// Copyright (c) 2021 Kristopher L. Culin See LICENSE for details.

using System;
using System.Reflection;

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
		void GenerateTypeStub(Type type);
	}

	public interface IAssemblyCrawler
	{
		/// <summary>
		/// Crawls thru the assembly looking for public, internal, protected classes
		/// and generates the stubs for those classes.
		/// </summary>
		/// <param name="assembly"></param>
		/// <param name="generator">Used to generate the stub file(s) for the assembly</param>
		void Crawl(Assembly assembly, IStubGenerator generator);
	}
}
