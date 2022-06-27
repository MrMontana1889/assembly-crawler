// PythonTypeVar.cs
// Copyright (c) 2022 Kristopher L. Culin See LICENSE for details

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

				// 2022-03-26 - It turns out that by providing a list of types in the TypeVar definition, the "IntelliSense"
				// restricts the information to ONLY this list.  So by providing the lowest level types, the other properties
				// in IWaterNetwork, for example, won't show.  By only defining the TypeVar with no restrictions, will the
				// full list of properties/methods actually show up consistently.
				// Maybe in the future, some code can be written to figure out the "highest" level interfaces to restrict by
				// (highest meaning something like IWaterNetwork is included since it is essentially the "concrete" class) but
				// not INetwork whichi s the class in OpenFlows, not OpenFlows.Water
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
