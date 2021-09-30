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

			using (var fileStream = new FileStream(filePath, FileMode.OpenOrCreate, FileAccess.ReadWrite, FileShare.ReadWrite))
			{
				using(var streamWriter = new StreamWriter(fileStream, Encoding.ASCII))
				{
					Assembly testAssembly = Assembly.GetAssembly(typeof(OpenFlowsWater));
					var testType = typeof(IPipeInput);
					testType = typeof(IBaseLinkInput);
					testType = typeof(IPipeResults);

					var inheretedTypes = new List<Type>();

					foreach (var interf in testType.GetInterfaces())
					{
						if (!interf.IsGenericType)
							inheretedTypes.Add(interf);
					}


					// Write class
					PythonStubWriterLibrary.WritePythonClassDefinition(streamWriter, testType, inheretedTypes, PythonStubWriterLibrary.BlankDocString);

					// Write Constructor
					if (testType.IsInterface)
						PythonStubWriterLibrary.WritePytonConstructorUnsupported(streamWriter);

					
					// Get methods
					var methods = testType.GetMethods();
					foreach (var method in methods)
					{
						// skip property methods
						if (method.Name.StartsWith("set_") || method.Name.StartsWith("get__"))
							continue; 

						// TODO: Find a way to handle overloaded methodss
					}


					// Write properties
					foreach (var method in methods)
					{
						if (method.Name.StartsWith("get_"))
							PythonStubWriterLibrary.WritePythonProperty(streamWriter, method.Name.Substring(4), method.ReturnType, PythonStubWriterLibrary.BlankDocString);


						if (method.Name.StartsWith("set_"))
							PythonStubWriterLibrary.WritePythongPropertySetter(streamWriter, method.Name.Substring(4), method.GetParameters()[0].ParameterType);
					}



					streamWriter.Flush();
				}
			}
		}
		#endregion
	}
}
