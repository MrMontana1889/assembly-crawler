// CrawlerTestFixture.cs
// Copyright (c) 2021 Kristopher L. Culin See LICENSE for details

using System;
using System.Collections.Generic;
using System.IO;
using System.Reflection;
using System.Text;
using AssemblyCrawler.Generators;
using AssemblyCrawler.Library;
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
			IStubGenerator generator = GeneratorLibrary.NewPythonStubGenerator(null);
			Assert.IsNotNull(generator);

			Assembly testAssembly = Assembly.GetAssembly(typeof(OpenFlowsWater));
			Assert.IsNotNull(testAssembly);

			IAssemblyCrawler crawler = new AssemblyCrawler();
			crawler.Crawl(testAssembly, generator);
		}


		[Test]
		public void TestWriteStub()
		{
			var filePath = @"D:\Temp\pythonStybText.pyi";
			if (File.Exists(filePath))
				File.Delete(filePath);			



			//var fileStream = new FileStream(filePath, FileMode.OpenOrCreate, FileAccess.ReadWrite, FileShare.ReadWrite);
			//var streamWriter = new StreamWriter(fileStream, Encoding.ASCII);
			//try
			//{
				

			//}
			//finally
			//{
			//	streamWriter.Flush();
			//	streamWriter.Close();
			//}


            using (var fileStream = new FileStream(filePath, FileMode.OpenOrCreate, FileAccess.ReadWrite, FileShare.ReadWrite))
            {
                using (var streamWriter = new StreamWriter(fileStream, Encoding.ASCII))
                {

					Assembly testAssembly = Assembly.GetAssembly(typeof(OpenFlowsWater));
					var testType = typeof(IPipeInput);
					testType = typeof(IBaseLinkInput);
					//testType = typeof(IPipeResults);
					//testType = typeof(INetwork);

					IStubGenerator generator = GeneratorLibrary.NewPythonStubGenerator(streamWriter);
					Assert.IsNotNull(generator);

					generator.GenerateTypeStub(testType);

					streamWriter.Flush();
                }
            }
        }
		#endregion
	}
}
