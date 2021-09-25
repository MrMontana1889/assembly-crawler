// Elementbase.cs
// Copyright (c) 2021 Kristopher L. Culin See LICENSE for detalis

namespace TestAssemblyNET48.Domain.ModelingObjects
{
	public abstract class ElementBase : IElement
	{
		#region Constructor
		public ElementBase(int id)
		{
			Id = id;
		}
		#endregion

		#region Public Properties
		public int Id { get; }
		public string Label { get; set; }
		public string Notes { get; set; }
		#endregion
	}
}
