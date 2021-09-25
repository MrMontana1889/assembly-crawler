// Interfaces.cs
// Copyright (c) 2021 Kristopher L. Culin See LICENSE for details

using System.Collections.Generic;
using TestAssemblyNET48.Support;

namespace TestAssemblyNET48.Domain.ModelingObjects.NetworkElements
{
	public interface INetwork
	{
		IPipes Pipes { get; }
	}

	public interface IActiveElementInput : IElementInput
	{
		bool IsActive { get; set; }
	}
	public interface IBaseLinkInput : IActiveElementInput, IElementInput
	{
		IElement StartNode { get; set; }
		IElement StopNode { get; set; }
		bool IsUserDefinedLength { get; set; }
		double Length { get; set; }

		List<GeometryPoint> GetPoints();
		void SetPoints(List<GeometryPoint> points);
	}
}
