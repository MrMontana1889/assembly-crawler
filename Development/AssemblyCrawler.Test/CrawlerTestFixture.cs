// CrawlerTestFixture.cs
// Copyright (c) 2021 Kristopher L. Culin See LICENSE for details

using System.Reflection;
using AssemblyCrawler.Generators;
using NUnit.Framework;
using TestAssemblyNET48.Water;

namespace AssemblyCrawler.Test
{
	[TestFixture]
	public class CrawlerTestFixture
	{
		#region Constructor
		public CrawlerTestFixture()
		{

		}
		#endregion

		#region Tests
		[Test]
		public void TestSimpleCrawl()
		{
			IStubGenerator generator = GeneratorLibrary.NewPythonStubGenerator(null);
			Assert.IsNotNull(generator);

			Assembly testAssembly = Assembly.GetAssembly(typeof(OpenFlowsWater));
			Assert.IsNotNull(testAssembly);

			IAssemblyCrawler crawler = new AssemblyCrawler();
			crawler.Crawl(testAssembly, generator);
		}
		#endregion
	}
}
