// GeneratorLibrary.cs
// Copyright (c) 2021 Kristopher L. Culin See LICENSE for details

using System.IO;

namespace AssemblyCrawler.Generators
{
	public static class GeneratorLibrary
	{
		#region Public Methods
		public static IStubGenerator NewPythonStubGenerator(StreamWriter writer)
		{
			return new PythonStubGenerator(writer);
		}
		#endregion
	}
}
