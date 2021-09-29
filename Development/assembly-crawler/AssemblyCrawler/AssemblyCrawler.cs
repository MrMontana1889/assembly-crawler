// Crawler.cs
// Copyright (c) 2021 Kristopher L. Culin.  See LICENSE for details.

using System.Linq;
using System;
using System.Diagnostics;
using System.Reflection;
using System.Text;

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
					Console.WriteLine($"{RemoveNamespace(type)}:");
					var interfaces = type.GetInterfaces();
					foreach (var interf in interfaces)
						Console.WriteLine($"\t\t{interf.Name}");

					var methods = type.GetMethods();
					foreach (var method in methods)
					{
						if (method.Name.StartsWith("get_") ||
							method.Name.StartsWith("set_"))
							continue;
						if (method.IsConstructor) continue;

						Console.WriteLine($"\t{RemoveNamespace(method)}");
					}

					var properties = type.GetProperties();
					foreach (var property in properties)
					{
						Console.WriteLine($"\t{RemoveNamespace(property)}");
					}
				}
			}
		}

		private object RemoveNamespace(PropertyInfo property)
		{
			string? retVal = property.ToString();
			if (retVal == null)
				return "<unknown>";

			string? ns = property.PropertyType.Namespace;
			if (ns != null)
			{
				int index = retVal.IndexOf(ns);
				if (index > -1)
					retVal = retVal.Remove(index, ns.Length + 1);
			}
			return retVal;
		}

		private object RemoveNamespace(Type type)
		{
			string? retVal = type.ToString();
			if (retVal == null)
				return "<unknown>";

			string? ns = type.Namespace;
			if (ns != null)
			{
				int index = retVal.IndexOf(ns);
				if (index > -1)
					retVal = retVal.Remove(index, ns.Length + 1);
			}
			return retVal;
		}

		private string RemoveNamespace(MethodInfo method)
		{
			string? retVal = method.ToString();

			if (retVal == null)
				return "<unknown>";

			string? ns = method.ReturnType.Namespace;
			if (ns != null)
			{
				int index = retVal.IndexOf(ns);
				if (index > -1)
					retVal = retVal.Remove(index, ns.Length + 1);
			}

			var parameters = method.GetParameters();
			foreach (var parameter in parameters)
			{
				ns = parameter.ParameterType.Namespace;
				if (ns != null)
				{
					int index = retVal.IndexOf(ns);
					if (index > -1)
						retVal = retVal.Remove(index, ns.Length + 1);
				}
			}

			var genericArguments = method.ReturnType.GetGenericArguments();
			foreach (var arg in genericArguments)
			{
				if (arg != null)
				{
					ns = arg.Namespace;
					if (ns != null)
					{
						int index = retVal.IndexOf(ns);
						if (index > -1)
							retVal = retVal.Remove(index, ns.Length + 1);
					}
				}
			}

			retVal = retVal.Replace("Int32", "int");

			return retVal;

		}
		#endregion
	}
}
