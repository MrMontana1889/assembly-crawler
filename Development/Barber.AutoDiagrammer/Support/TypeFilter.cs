// TypeFilter.cs
// Copyright (c) 2021 Sacha Barber See LICENSE for details

using System;
using System.Collections.Generic;

namespace Barber.AutoDiagrammer.Support
{
	/// <summary>
	/// Filter used to include specific types ignore any not
	/// in the provided list.
	/// </summary>
	[Serializable]
	public class TypeFilter : ITypeFilter
	{
		#region Constructor
		public TypeFilter(List<Type> types)
		{
			Types = types;
		}
		#endregion

		#region Public Methods
		public bool IncludeType(Type t)
		{
			if (t == null)
				return false;

			return Types.Find(type => type.FullName == t.FullName) != null;
		}
		#endregion

		#region Private Properties
		private List<Type> Types { get; }
		#endregion
	}
}
