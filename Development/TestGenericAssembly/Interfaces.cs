// Interfaces.cs
// Copyright (c) 2021 Kristopher L. Culin See LICENSE for details

using System.Collections.Generic;

namespace Test.TestGenericAssembly
{
	public interface IElementInput { }
	public interface IElementsInput { }
	public interface IElementResults { }
	public interface IElementsResults { }

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

	public interface IModelingElementBase<TElementTypeManager, TElementType, TElementInputType, TElementResultsType, TElementsInputType, TElementsResultsType> : IElement
		where TElementTypeManager : class, IElementManager
		where TElementType : class, IElement
		where TElementInputType : class, IElementInput
		where TElementResultsType : class, IElementResults
		where TElementsInputType : class, IElementsInput
		where TElementsResultsType : class, IElementsResults
	{
		TElementTypeManager Manager { get; }
		void Delete();
	}

	public interface IModelingElementsBase<TElementTypeManager, TElementType, TElementInputType, TElementResultsType, TElementsInputType, TElementsResultsType> : IElementManager
		where TElementTypeManager : class, IElementManager
		where TElementType : class, IElement
		where TElementInputType : class, IElementInput
		where TElementResultsType : class, IElementResults
		where TElementsInputType : class, IElementsInput
		where TElementsResultsType : class, IElementsResults
	{
		TElementType Create();
		TElementType Element(int id);
		TElementType Element(string label);
		List<TElementType> Elements();
	}

	public interface INetworkElement<TElementTypeManager, TElementType, TElementInputType, TElementResultsType, TElementsInputType, TElementsResultsType>
		: IModelingElementBase<TElementTypeManager, TElementType, TElementInputType, TElementResultsType, TElementsInputType, TElementsResultsType>
		where TElementTypeManager : class, IElementManager
		where TElementType : class, IElement
		where TElementInputType : class, IElementInput
		where TElementResultsType : class, IElementResults
		where TElementsInputType : class, IElementsInput
		where TElementsResultsType : class, IElementsResults
	{

	}

	public interface INetworkElements<TElementTypeManager, TElementType, TElementInputType, TElementResultsType, TElementsInputType, TElementsResultsType>
		: IModelingElementsBase<TElementTypeManager, TElementType, TElementInputType, TElementResultsType, TElementsInputType, TElementsResultsType>
		where TElementTypeManager : class, IElementManager
		where TElementType : class, IElement
		where TElementInputType : class, IElementInput
		where TElementResultsType : class, IElementResults
		where TElementsInputType : class, IElementsInput
		where TElementsResultsType : class, IElementsResults
	{
		TElementsInputType Input { get; }
		TElementsResultsType Results { get; }
	}

	public interface IWaterNetworkElement<TElementTypeManager, TElementType, TElementInputType, TElementResultsType, TElementsInputType, TElementsResultsType>
		: INetworkElement<TElementTypeManager, TElementType, TElementInputType, TElementResultsType, TElementsInputType, TElementsResultsType>
		where TElementTypeManager : class, IElementManager
		where TElementType : class, IElement
		where TElementInputType : class, IElementInput
		where TElementResultsType : class, IElementResults
		where TElementsInputType : class, IElementsInput
		where TElementsResultsType : class, IElementsResults

	{
		TElementInputType Input { get; }
		TElementResultsType Results { get; }
	}

	public interface IWaterNetworkElements<TElementTypeManager, TElementType, TElementInputType, TElementResultsType, TElementsInputType, TElementsResultsType>
		: INetworkElements<TElementTypeManager, TElementType, TElementInputType, TElementResultsType, TElementsInputType, TElementsResultsType>
		where TElementTypeManager : class, IElementManager
		where TElementType : class, IElement
		where TElementInputType : class, IElementInput
		where TElementResultsType : class, IElementResults
		where TElementsInputType : class, IElementsInput
		where TElementsResultsType : class, IElementsResults
	{

	}
 }
