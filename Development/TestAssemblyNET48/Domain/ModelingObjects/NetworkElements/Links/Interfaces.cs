// Interfaces.cs
// Copyright (c) 2021 Kristopher L. Culin See LICENSE for details

using System.Collections.Generic;

namespace TestAssemblyNET48.Water.Domain.ModelingObjects.NetworkElements
{
	public interface IPipeInput : IBaseLinkInput
	{ 
		double Diameter { get; set; }
	}
	public interface IPipesInput : IElementsInput
	{
		IDictionary<int, double> Diameters();
	}
	public interface IPipeResults : IElementResults
	{
		double? Flow();
		double? Flow(int timeStepIndex);
	}
	public interface IPipesResults : IElementsResults
	{
		IDictionary<int, double?> Flows();
		IDictionary<int, double?> Flows(int timeStepIndex);
		IDictionary<int, double?> Flows(int timeStepIndex, List<int> ids);
	}

	public interface IPipes : IModelingElementsBase<IPipes, IPipe, IPipeInput, IPipeResults, IPipesInput, IPipesResults>
	{
	}

	public interface IPipe : IModelingElementBase<IPipes, IPipe, IPipeInput, IPipeResults, IPipesInput, IPipesResults>
	{
	}
}
