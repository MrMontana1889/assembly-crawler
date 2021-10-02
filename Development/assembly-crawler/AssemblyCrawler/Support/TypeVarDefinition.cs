// TypeVarDefinition.cs
// Copyright (c) 2021 Kristopher L. Culin See LICENSE for details

using System;
using System.Collections.Generic;
using System.IO;
using AssemblyCrawler.Library;

namespace AssemblyCrawler.Support
{
	public class TypeVarDefinition
	{
		#region Constructor
		public TypeVarDefinition(string name, Type[] constraint)
		{
			TypeVarName = name;
			Constraints = constraint;
		}
		#endregion

		#region Public Methods
		public void Write(StreamWriter sw)
		{
			if (Constraints != null)
			{
				List<string> constraintNames = new List<string>();
				foreach (var t in Constraints)
					constraintNames.Add(PythonStubWriterLibrary.CorrectClassName(t.Name, t.GetGenericArguments().Length));
				sw.WriteLine($"{TypeVarName} = TypeVar(\"{TypeVarName}\", {string.Join(",", constraintNames)})");
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
