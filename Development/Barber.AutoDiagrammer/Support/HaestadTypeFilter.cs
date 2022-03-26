// HaestadTypeFilter.cs
// Copyright (c) 2021 Sacha Barber See LICENSE for details

using System;

namespace Barber.AutoDiagrammer.Support
{
	/// <summary>
	/// Similar to the interface only filter but includes types
	/// in namespaces starting with Haestad
	/// </summary>
	[Serializable]
	public class HaestadTypeFilter : ITypeFilter
	{
		#region Constructor
		public HaestadTypeFilter()
		{

		}
		#endregion

		#region Public Methods
		public bool IncludeType(Type t)
		{
			if (t == null)
				return false;

			if (t.IsNotPublic)
				return false;       // Exclude all non-public types

			//check to see if the class lives in a namespace
			if (t.Namespace != null && !string.IsNullOrEmpty(t.Namespace))
			{
				if (t.Namespace.StartsWith("System"))
					return false;       // Ignore all types in system assemblies
			}

			if (!t.IsClass && t.IsInterface)
				return true;

			if (t.IsEnum)
				return true;

			if (t.IsClass && t.IsPublic && t.IsAbstract)
				return true;

			return false;
		}
		#endregion
	}
}
