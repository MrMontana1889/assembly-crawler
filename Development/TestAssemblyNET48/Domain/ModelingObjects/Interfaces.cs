// Interfaces.cs
// Copyright (c) 2021 Kristopher L. Culin See LICENSE for details

using System.Collections.Generic;

namespace TestAssemblyNET48.Water.Domain.ModelingObjects
{
	public interface IElementInput
	{

	}
	public interface IElementsInput
	{

	}
	public interface IElementResults
	{

	}
	public interface IElementsResults
	{

	}

	public interface IElementManager
	{
		int Count { get; }
		List<int> ElementIDs();
		bool Exists(int id);
	}

	public interface IElement
	{
		int Id { get; }
		string Label { get; set; }
		string Notes { get; set; }
	}

	public interface IModelingElementBase<TElementTypeManager, TElementType, TElementInputType, TElementResultsType,
		TElementsInputType, TElementsResultsType> : IElement
		where TElementTypeManager : class, IModelingElementsBase<TElementTypeManager, TElementType, TElementInputType, TElementResultsType, TElementsInputType, TElementsResultsType>
		where TElementType : class, IModelingElementBase<TElementTypeManager, TElementType, TElementInputType, TElementResultsType, TElementsInputType, TElementsResultsType>
		where TElementInputType : class, IElementInput
		where TElementResultsType : class, IElementResults
		where TElementsInputType : class, IElementsInput
		where TElementsResultsType : class, IElementsResults
	{
		TElementTypeManager Manager { get; }

		TElementInputType Input { get; }
		TElementResultsType Results { get; }
	}

	public interface IModelingElementsBase<TElementTypeManager, TElementType, TElementInputType, TElementResultsType,
		TElementsInputType, TElementsResultsType> : IElementManager
		where TElementTypeManager : class, IModelingElementsBase<TElementTypeManager, TElementType, TElementInputType, TElementResultsType, TElementsInputType, TElementsResultsType>
		where TElementType : class, IModelingElementBase<TElementTypeManager, TElementType, TElementInputType, TElementResultsType, TElementsInputType, TElementsResultsType>
		where TElementInputType : class, IElementInput
		where TElementResultsType : class, IElementResults
		where TElementsInputType : class, IElementsInput
		where TElementsResultsType : class, IElementsResults
	{
		TElementType Create();
		TElementType Element(int id);
		TElementType Element(string label);
		List<TElementType> Elements();
		void Delete(int id);

		TElementsInputType Input { get; }
		TElementsResultsType Results { get; }
	}

}
