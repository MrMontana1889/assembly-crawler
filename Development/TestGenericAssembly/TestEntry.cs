// TestEntry.cs
// Copyright (c) 2021 Kristopher L. Culin See LICENSE for details

using Test.TestGenericAssembly;
using Test.TestGenericAssembly.Links;

namespace TestGenericAssembly
{
	public static class TestEntry
	{
		public static IElement GetElement()
		{
			return new Pipe();
		}

		public static IPipes GetPipes()
		{
			return new Pipes();
		}
	}
}
