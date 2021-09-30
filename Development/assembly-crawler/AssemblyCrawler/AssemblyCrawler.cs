// Crawler.cs
// Copyright (c) 2021 Kristopher L. Culin.  See LICENSE for details.

using System;
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
					string shortType = $"{RemoveNamespace(type)}";
					var interfaces = type.GetInterfaces();
					if (interfaces.Length > 0)
					{
						Console.Write($"{shortType} : ");
						foreach (var interf in interfaces)
						{
							if (interf.IsGenericType)
							{
								shortType = interf.Name + "[";
								var args = interf.GetGenericArguments();
								foreach (var arg in args)
								{
									if (arg.FullName != null)
									{
										string? a = arg.FullName;
										if (a != null)
										{
											a = a.Replace(arg.FullName, arg.Name);
											shortType += a + ",";
										}
									}
								}
								if (shortType.EndsWith(","))
									shortType = shortType.Remove(shortType.Length - 1, 1);
								shortType += "]";
							}
							else
							{
								shortType += interf.Name + ", ";
							}
						}
						if (shortType.EndsWith(","))
							shortType = shortType.Remove(shortType.Length - 1, 1);
						else if (shortType.EndsWith(", "))
							shortType = shortType.Remove(shortType.Length - 2, 2);
						Console.WriteLine($"{shortType}");
					}
					else
					{
						Console.WriteLine($"{shortType}");
					}

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
		#endregion

		#region Private Methods
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

			var returnType = method.ReturnType;
			if (returnType.FullName != null)
				retVal = retVal.Replace(returnType.FullName, returnType.Name);

			if (returnType.IsGenericType)
			{
				string? ns = returnType.Namespace;
				if (ns != null)
				{
					retVal = retVal.Replace(ns + ".", "");
				}

				var returnTypeParameters = returnType.GetGenericArguments();
				foreach (var rtParam in returnTypeParameters)
				{
					if (rtParam.FullName != null)
						retVal = retVal.Replace(rtParam.FullName, rtParam.Name);

					ns = rtParam.Namespace;
					if (ns != null)
					{
						int index = retVal.IndexOf(ns);
						if (index > -1)
							retVal = retVal.Remove(index, ns.Length + 1);
					}
				}
			}

			var parameters = method.GetParameters();
			foreach (var parameter in parameters)
			{
				var pType = parameter.ParameterType;
				if (pType.FullName != null)
					retVal = retVal.Replace(pType.FullName, pType.Name);

				if (pType.IsGenericType)
				{
					string? ns = pType.Namespace;
					if (ns != null)
					{
						int index = retVal.IndexOf(ns);
						if (index > -1)
							retVal = retVal.Remove(index, ns.Length + 1);
					}

					var pTypes = pType.GetGenericArguments();
					foreach (var t in pTypes)
					{
						if (t.FullName != null)
							retVal = retVal.Replace(t.FullName, t.Name);

						ns = t.Namespace;
						if (ns != null)
						{
							int index = retVal.IndexOf(ns);
							if (index > -1)
								retVal = retVal.Remove(index, ns.Length + 1);
						}
					}
				}
			}

			var genericArguments = method.ReturnType.GetGenericArguments();
			foreach (var arg in genericArguments)
			{
				if (arg != null)
				{
					if (arg.FullName != null)
						retVal = retVal.Replace(arg.FullName, arg.Name);

					var paramArgs = arg.GetGenericArguments();
					foreach (var pArg in paramArgs)
					{
						if (pArg.FullName != null)
							retVal = retVal.Replace(pArg.FullName, pArg.Name);
					}
				}
			}

			return retVal;
		}
		#endregion
	}
}
