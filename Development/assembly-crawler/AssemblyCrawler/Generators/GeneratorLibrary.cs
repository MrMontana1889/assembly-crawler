// GeneratorLibrary.cs
// Copyright (c) 2021 Kristopher L. Culin See LICENSE for details

using System.IO;
using AssemblyCrawler.Support;

namespace AssemblyCrawler.Generators
{
	public static class GeneratorLibrary
	{
		#region Public Methods
		public static IStubGenerator NewPythonStubGenerator(PythonModuleDefinition stubFile)
		{
			return new PythonStubGenerator(stubFile);
		}
		#endregion
	}
}
