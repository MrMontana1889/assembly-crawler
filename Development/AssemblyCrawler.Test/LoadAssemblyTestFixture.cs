// LoadAssemblyTestFixture.cs
// Copyright (c) 2022 Kristopher L. Culin See LICENSE for details

using System.Reflection;
using NUnit.Framework;
using TestAssemblyNET48.Water;

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
			Assembly testAssembly = Assembly.GetAssembly(typeof(OpenFlowsWater));
			Assert.IsNotNull(testAssembly);
		}
		#endregion
	}
}