// TypeVarDefinition.cs
// Copyright (c) 2021 Kristopher L. Culin See LICENSE for details

using System;
using System.Collections.Generic;
using System.Diagnostics;
using System.IO;
using AssemblyCrawler.Library;

namespace AssemblyCrawler.Support
{
	[DebuggerDisplay("{TypeVarName} : {Constraints}")]
	public class PythonTypeVar
	{
		#region Constructor
		public PythonTypeVar(string name, params Type[] constraints)
		{
			TypeVarName = name;

			List<Type> nonSystemConstraints = new List<Type>();
			if (constraints != null)
			{
				foreach (var t in constraints)
				{
					var typeNamespace = t.Namespace;
					if (!typeNamespace.Contains("IEnumerable") || t == typeof(Enum))
						nonSystemConstraints.Add(t);
				}
				Constraints = nonSystemConstraints.ToArray();
			}
			else
				Constraints = new Type[] { };
		}
		#endregion

		#region Public Methods
		public void Write(StreamWriter sw)
		{
			if (Constraints != null)
			{
				List<string> constraintNames = new List<string>();
				foreach (var t in Constraints)
					constraintNames.Add(WriterLibrary.CorrectClassName(t.Name, t.GetGenericArguments().Length));

				if (constraintNames.Count > 0)
					sw.WriteLine($"{TypeVarName} = TypeVar(\"{TypeVarName}\", {string.Join(",", constraintNames)})");
				else
					sw.WriteLine($"{TypeVarName} = TypeVar(\"{TypeVarName}\")");
			}
			else
			{
				sw.WriteLine($"{TypeVarName} = TypeVar(\"{TypeVarName}\")");
			}
		}
		#endregion

		#region Public Properties
		public string TypeVarName { get; }
		public Type[] Constraints { get; }
		#endregion
	}
}
