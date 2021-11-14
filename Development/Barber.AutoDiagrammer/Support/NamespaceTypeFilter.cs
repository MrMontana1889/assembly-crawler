// NamespaceTypeFilter.cs
// Copyright (c) 2021 see LICENSE for details

using System;
using System.Collections.Generic;
using AssemblyCrawler.Xml.Config;

namespace Barber.AutoDiagrammer.Support
{
	/// <summary>
	/// Used to fitler to a specific namespace and exclude all other types
	/// not in the specified namespace.
	/// </summary>
	[Serializable]
	public class NamespaceTypeFilter : ITypeFilter
	{
		#region Constructor
		public NamespaceTypeFilter(ClassType classType, string assemblyNamespace, List<Type> classes, bool hasNamespace = true)
		{
			ClassType = classType;
			AssemblyNamespace = assemblyNamespace;
			Classes = classes;
			HasNamespace = hasNamespace;
		}
		#endregion

		#region Public Methods
		public bool IncludeType(Type t)
		{
			if (t == null)
				return false;

			// The namespace is not specified.  Exclude (no way to compare)
			if (HasNamespace && t.Namespace == null)
				return false;

			// Determine if the type is in one of the include namespaces
			string typeNamespace = t.Namespace;
			string typeName = t.Name;

			if (!HasNamespace)
				typeNamespace = string.Empty;

			if (ClassType == ClassType.All)
			{
				// All types in the specified namespace are included.
				return typeNamespace == AssemblyNamespace;
			}
			else if (ClassType == ClassType.ClassListOnly)
			{
				// Only consider the types specified for this namespace.
				return typeNamespace == AssemblyNamespace &&
					(Classes.Find(c => c.FullName == t.FullName) != null ||
					t.IsEnum);
			}
			else if (ClassType == ClassType.InterfacesOnly)
			{
				bool isInterface = !t.IsClass && t.IsInterface;
				if (Classes.Count > 0)
				{
					// Namespace must match and the type be in the list of classes
					return (typeNamespace == AssemblyNamespace && (isInterface || t.IsEnum)) ||
						Classes.Find(c => c.FullName == t.FullName) != null;
				}
				else
				{
					// No classes specified.  Make sure the type is in the namespace AND
					// it is an interface and not a class.
					return typeNamespace == AssemblyNamespace && (isInterface || t.IsEnum);
				}
			}

			return false;
		}
		#endregion

		#region Private Properties
		private ClassType ClassType { get; }
		private string AssemblyNamespace { get; }
		private List<Type> Classes { get; }
		private bool HasNamespace { get; }
		#endregion
	}
}
