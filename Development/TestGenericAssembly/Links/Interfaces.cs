using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace Test.TestGenericAssembly.Links
{
	/// <summary>
	/// Contains commonly available inputs for a <c>Pipe</c>.
	/// </summary>
	public interface IPipeInput : IElementInput
	{

	}
	public interface IPipesInput : IElementsInput
	{

	}
	public interface IPipeResults : IElementResults
	{
	}
	public interface IPipesResults : IElementsResults
	{

	}

	/// <summary>
	/// 
	/// </summary>
	public interface IPipes : IWaterNetworkElements<IPipes, IPipe, IPipeInput, IPipeResults, IPipesInput, IPipesResults>, IElementManager
	{

	}
	public interface IPipe : IWaterNetworkElement<IPipes, IPipe, IPipeInput, IPipeResults, IPipesInput, IPipesResults>, IElement
	{

	}
}
