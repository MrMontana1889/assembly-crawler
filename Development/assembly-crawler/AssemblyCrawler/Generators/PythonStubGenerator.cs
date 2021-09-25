// AssemblyStubGenerator.cs
// Copyright (c) 2021 Kristopher L. Culin See LICENSE for details

using System;
using System.IO;

namespace AssemblyCrawler.Generators
{
	internal class PythonStubGenerator : IStubGenerator
	{
		#region Constructor
		public PythonStubGenerator(StreamWriter writer)
		{
			Writer = writer;
		}
		#endregion

		#region Public Methods
		public void GenerateTypeStub(Type type)
		{
			
		}
		#endregion

		#region Private Properties
		private StreamWriter Writer { get; }
		#endregion
	}
}
