// Crawler.cs
// Copyright (c) 2021 Kristopher L. Culin.  See LICENSE for details.

using System;
using System.Diagnostics;
using System.Reflection;

namespace AssemblyCrawler
{
	public class AssemblyCrawler : IAssemblyCrawler
	{
		#region Constructor
		public AssemblyCrawler()
		{

		}
		#endregion

		#region Public Methods
		public void Crawl(Assembly assembly, IStubGenerator generator)
		{
			var types = assembly.GetTypes();

			foreach (Type type in types)
			{
				// Ignore abstract classes
				if (type.IsAbstract && !type.IsInterface)
					continue;

				if (type.IsInterface)
				{
					Console.Write($"{type.FullName}");
					if (type.IsGenericType)
						Console.WriteLine(" (Generic)");
					else
						Console.WriteLine("");

					var methods = type.GetMethods();
					foreach (var method in methods)
					{
						if (method.Name.StartsWith("get_") ||
							method.Name.StartsWith("set_"))
							continue;
						Console.WriteLine($"\t{method.Name}");
					}

					var properties = type.GetProperties();
					foreach (var property in properties)
						Console.WriteLine($"\t{property.Name}");

					var interfaces = type.GetInterfaces();
					foreach (var interf in interfaces)
						Console.WriteLine($"\t\t{interf.Name}");
				}
			}
		}
		#endregion
	}
}
