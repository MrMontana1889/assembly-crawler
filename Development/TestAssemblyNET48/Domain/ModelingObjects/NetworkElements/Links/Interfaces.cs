// Interfaces.cs
// Copyright (c) 2021 Kristopher L. Culin See LICENSE for details

using System.Collections.Generic;

namespace TestAssemblyNET48.Water
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

	public interface IPipes : IElementManager<IPipe>
	{
		IPipesInput Input { get; }
		IPipesResults Results { get; }
	}

	public interface IPipe : IElement
	{
		IPipeInput Input { get; }
		IPipeResults Results { get; }
	}
}
