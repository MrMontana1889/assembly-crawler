// Elementbase.cs
// Copyright (c) 2021 Kristopher L. Culin See LICENSE for detalis

namespace TestAssemblyNET48.Water.Domain.ModelingObjects
{
	public abstract class ElementBase<TElementTypeManager, TElementType, TElementInputType, TElementResultsType, TElementsInputType, TElementsResultsType> 
		: IModelingElementBase<TElementTypeManager, TElementType, TElementInputType, TElementResultsType, TElementsInputType, TElementsResultsType>
		where TElementTypeManager : class, IModelingElementsBase<TElementTypeManager, TElementType, TElementInputType, TElementResultsType, TElementsInputType, TElementsResultsType>
		where TElementType : class, IModelingElementBase<TElementTypeManager, TElementType, TElementInputType, TElementResultsType, TElementsInputType, TElementsResultsType>
		where TElementInputType: class, IElementInput
		where TElementResultsType : class, IElementResults
		where TElementsInputType : class, IElementsInput
		where TElementsResultsType : class, IElementsResults
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
		public TElementTypeManager Manager { get; }
		public abstract TElementInputType Input { get; }
		public abstract TElementResultsType Results { get; }
		#endregion
	}
}
