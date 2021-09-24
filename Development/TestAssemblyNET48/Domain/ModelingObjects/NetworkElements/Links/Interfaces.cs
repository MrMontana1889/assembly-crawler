// Interfaces.cs
// Copyright (c) 2021 Kristopher L. Culin See LICENSE for details

using System.Collections.Generic;

namespace TestAssemblyNET48.Domain.ModelingObjects.NetworkElements
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

	public interface IPipes : IElementManager
	{
		IPipe Create();
		IPipe Element(int id);
		IPipe Element(string label);
		List<IPipe> Elements();
		void Delete(int id);

		IPipesInput Input { get; }
		IPipesResults Results { get; }
	}

	public interface IPipe : IElement
	{
		IPipeInput Input { get; }
		IPipeResults Results { get; }
	}
}
