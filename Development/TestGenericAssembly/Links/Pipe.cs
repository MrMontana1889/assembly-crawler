// Pipe.cs
// Copyright (c) 2021 Kristopher L. Culin See LICENSE for details

using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;
using Test.TestGenericAssembly;

namespace Test.TestGenericAssembly.Links
{
	internal class Pipe : IPipe, IPipeInput, IPipeResults
	{
		public IPipeInput Input => this;
		public IPipeResults Results => this;
		public IPipes Manager { get; }
		public int Id { get; }
		public string Label { get; set; }
		public string Notes { get; set; }

		public void Delete()
		{
			throw new System.NotImplementedException();
		}
	}
}
