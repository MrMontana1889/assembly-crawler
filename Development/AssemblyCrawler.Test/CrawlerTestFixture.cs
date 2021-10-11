// CrawlerTestFixture.cs
// Copyright (c) 2021 Kristopher L. Culin See LICENSE for details

using System.IO;
using System.Reflection;
using AssemblyCrawler.Support;
using Barber.AutoDiagrammer.Support;
using NUnit.Framework;
using TestAssemblyNET48.Water;
using TestAssemblyNET48.Water.Domain.ModelingObjects.NetworkElements;

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
			Assembly testAssembly = Assembly.GetAssembly(typeof(OpenFlowsWater));
			Assert.IsNotNull(testAssembly);

			PythonPackage package = new PythonPackage("OpenFlowsWater");

			IAssemblyCrawler crawler = new AssemblyCrawler();
			crawler.Crawl(package, testAssembly.Location, string.Empty, Path.GetTempPath(), new InterfacesOnlyTypeFilter(false));
		}


		[Test]
		public void TestWriteStub()
		{

			Assembly testAssembly = Assembly.GetAssembly(typeof(OpenFlowsWater));
			var testType = typeof(IPipeInput);
			testType = typeof(IBaseLinkInput);
			testType = typeof(IPipeResults);
			testType = typeof(INetwork);
			testType = typeof(Pipes);
			testType = typeof(System.Drawing.Size);

			var tempDir = Path.Combine(Path.GetTempPath(), "pythonStubs");
			if (!Directory.Exists(tempDir))
				Directory.CreateDirectory(tempDir);

			var filePath = Path.Combine(Path.GetTempPath(), "pythonStubs", $"{testType.Name}.pyi");
			if (File.Exists(filePath))
				File.Delete(filePath);


			PythonPackage package = new PythonPackage("TestWriteStub");
			var assemblyDef = package.AddAssembly(testAssembly, Path.GetTempPath());
			var module = assemblyDef.AddModule(testType.Namespace, filePath, string.Empty);
			module.Write();
		}
		#endregion
	}
}
