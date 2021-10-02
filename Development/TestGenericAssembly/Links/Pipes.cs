// Pipes.cs
// Copyright (c) 2021 Kristopher L. Culin See LICENSE for details

using System.Collections.Generic;

namespace Test.TestGenericAssembly.Links
{
	internal class Pipes : IPipes, IPipesInput, IPipesResults
	{
		public IPipesInput Input => this;
		public IPipesResults Results => this;
		public int Count { get; }

		public IPipe Create()
		{
			return new Pipe();
		}

		public IPipe Element(int id)
		{
			return new Pipe();
		}

		public IPipe Element(string label)
		{
			return new Pipe();
		}

		public List<int> ElementIDs()
		{
			return new List<int>();
		}

		public List<IPipe> Elements()
		{
			return new List<IPipe>();
		}

		public bool Exists(int id)
		{
			return false;
		}
	}
}
