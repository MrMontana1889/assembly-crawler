// LoadAssemblyTestFixture.cs
// Copyright (c) 2021 Kristopher L. Culin See LICENSE for details

using System.Reflection;
using NUnit.Framework;
using TestAssemblyNET48;

namespace AssemblyCrawler.Test
{
	public class LoadAssemblyTestFixture
	{
		#region Setup/Teardown
		[SetUp]
		public void Setup()
		{
		}
		#endregion


		#region Tests
		[Test]
		public void TestLoadTestASsembly()
		{
			Assembly testAssembly = Assembly.GetAssembly(typeof(EntryPoint));
			Assert.IsNotNull(testAssembly);
		}
		#endregion
	}
}