// NamespaceTypeFilter.cs
// Copyright (c) 2021 see LICENSE for details

using System;
using System.Collections.Generic;

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
		public NamespaceTypeFilter(List<string> namespaces)
		{
			Namespaces = namespaces;
		}
		#endregion

		#region Public Methods
		public bool IncludeType(Type t)
		{
			if (t == null)
				return false;

			// The namespace is not specified.  Exclude (no way to compare)
			if (t.Namespace == null)
				return false;

			// Determine if the type is in one of the include namespaces
			string typeNamespace = t.Namespace;
			return Namespaces.Contains(typeNamespace);
		}
		#endregion

		#region Private Properties
		private List<string> Namespaces { get; }
		#endregion
	}
}
