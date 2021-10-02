using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace Test.TestGenericAssembly.Links
{
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
	public interface IPipes : IWaterNetworkElements<IPipes, IPipe, IPipeInput, IPipeResults, IPipesInput, IPipesResults>, IElementManager
	{

	}
	public interface IPipe : IWaterNetworkElement<IPipes, IPipe, IPipeInput, IPipeResults, IPipesInput, IPipesResults>, IElement
	{

	}
}
