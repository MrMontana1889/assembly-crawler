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

		/// <summary>
		/// Get all the IDs
		/// </summary>
		/// <returns>List of element Ids</returns>
		List<int> ElementIDs();

		/// <summary>
		/// Evaulates if an id exists
		/// </summary>
		/// <param name="id">The id whose existance has to be checked</param>
		/// <returns>True if found, otherwise false </returns>
		/// <example>Here's an example.
		/// var isInModel = WaterModel.Network.Pipes.Exists(420);
		/// </example>
		bool Exists(int id);
	}

	/// <summary>
	/// The lowest level interface for element with <code>Id, Label and Notes</code>.
	/// </summary>
	public interface IElement
	{
		/// <summary>
		/// Id of an element
		/// </summary>
		int Id { get; }

		/// <summary>
		/// User friendly text for an element
		/// </summary>
		string Label { get; set; }
		string Notes { get; set; }
	}

	/// <summary>
	/// The lowest level interface for a modeling element.
	/// </summary>
	/// <typeparam name="TElementTypeManager"></typeparam>
	/// <typeparam name="TElementType"></typeparam>
	/// <typeparam name="TElementInputType"></typeparam>
	/// <typeparam name="TElementResultsType"></typeparam>
	/// <typeparam name="TElementsInputType"></typeparam>
	/// <typeparam name="TElementsResultsType"></typeparam>
	public interface IModelingElementBase<TElementTypeManager, TElementType, TElementInputType, TElementResultsType, TElementsInputType, TElementsResultsType> : IElement
		where TElementTypeManager : class, IElementManager
		where TElementType : class, IElement
		where TElementInputType : class, IElementInput
		where TElementResultsType : class, IElementResults
		where TElementsInputType : class, IElementsInput
		where TElementsResultsType : class, IElementsResults
	{
		TElementTypeManager Manager { get; }

		/// <summary>
		/// 
		/// </summary>
		void Delete();
	}

	/// <summary>
	/// The lowest level interface for modeling elements.
	/// <para>&#160;</para>
	/// <see cref="IModelingElementBase{TElementTypeManager, TElementType, TElementInputType, TElementResultsType, TElementsInputType, TElementsResultsType}">IModelingElementBase for single element</see>
	/// </summary>
	/// <typeparam name="TElementTypeManager"></typeparam>
	/// <typeparam name="TElementType"></typeparam>
	/// <typeparam name="TElementInputType"></typeparam>
	/// <typeparam name="TElementResultsType"></typeparam>
	/// <typeparam name="TElementsInputType"></typeparam>
	/// <typeparam name="TElementsResultsType"></typeparam>
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

	/// <summary>
	/// The lowest level interface for a network element.
	/// </summary>
	/// <typeparam name="TElementTypeManager">A class inherited from <c>IEementManager</c> </typeparam>
	/// <typeparam name="TElementType"></typeparam>
	/// <typeparam name="TElementInputType"></typeparam>
	/// <typeparam name="TElementResultsType"></typeparam>
	/// <typeparam name="TElementsInputType"></typeparam>
	/// <typeparam name="TElementsResultsType"></typeparam>
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

	/// <summary>
	/// The lowest level interface for network elements.
	/// <para>&#160;</para>
	/// </summary>
	/// <typeparam name="TElementTypeManager"></typeparam>
	/// <typeparam name="TElementType"></typeparam>
	/// <typeparam name="TElementInputType"></typeparam>
	/// <typeparam name="TElementResultsType"></typeparam>
	/// <typeparam name="TElementsInputType"></typeparam>
	/// <typeparam name="TElementsResultsType"></typeparam>
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
