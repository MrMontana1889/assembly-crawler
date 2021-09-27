// Interfaces.cs
// Copyright (c) 2021 Kristopher L. Culin See LICENSE for details

using TestAssemblyNET48.Water.Domain.ModelingObjects.NetworkElements;

namespace TestAssemblyNET48.Water.Domain.DataObjects
{
	public interface IWaterModel
	{
		INetwork Network { get; }
	}
}
