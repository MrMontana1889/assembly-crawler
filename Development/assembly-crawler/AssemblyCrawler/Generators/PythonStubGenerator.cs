// AssemblyStubGenerator.cs
// Copyright (c) 2021 Kristopher L. Culin See LICENSE for details

using System;
using System.Collections.Generic;
using System.IO;
using AssemblyCrawler.Library;

namespace AssemblyCrawler.Generators
{
	internal class PythonStubGenerator : IStubGenerator
	{
		#region Constructor
		public PythonStubGenerator(StreamWriter writer)
		{
			Writer = writer;
		}
		#endregion

		#region Public Methods
		public void GenerateTypeStub(Type type)
		{
			var parentTypes = new List<Type>();
			foreach (var t in type.GetInterfaces())
			{
				if (!t.IsGenericType)
					parentTypes.Add(t);
			}

			PythonStubWriterLibrary.WritePythonClassDefinition(Writer, type.Name, parentTypes, PythonStubWriterLibrary.BlankDocString);

			var methods = type.GetMethods();
			foreach (var method in methods)
			{
				if (method.IsPublic)
				{
					if (!method.IsGenericMethod)
					{
						if (!method.Name.StartsWith("get_") && !method.Name.StartsWith("set_"))
						{
							var parameters = method.GetParameters();
							List<KeyValuePair<string, Type>> arguments = new List<KeyValuePair<string, Type>>();
							foreach (var p in parameters)
							{
								arguments.Add(new KeyValuePair<string, Type>(p.Name, p.ParameterType));
							}

							PythonStubWriterLibrary.WritePythonMethod(Writer, method.Name, arguments, method.ReturnType, PythonStubWriterLibrary.BlankDocString);
						}
					}
				}
			}
		}
		#endregion

		#region Private Properties
		private StreamWriter Writer { get; }
		#endregion
	}
}
