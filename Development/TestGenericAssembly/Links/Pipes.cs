// Pipes.cs
// Copyright (c) 2022 Kristopher L. Culin See LICENSE for details

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

		/// <summary>
		/// There is an overload method to this.
		/// <see cref="Element(string)"/>
		/// which searched by Label
		/// </summary>
		/// <param name="id">Search Id</param>
		/// <returns></returns>
		public IPipe Element(int id)
		{
			return new Pipe();
		}

		/// <summary>
		/// Find a pipe based on given <paramref name="label"/>.
		/// </summary>
		/// <param name="label">Wild card search is supported</param>
		/// <returns><c>IPipe</c> if found, otherwise returns <c>null</c></returns>
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
