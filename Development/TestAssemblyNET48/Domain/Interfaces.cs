// Interfaces.cs
// Copyright (c) 2021 Kristopher L. Culin See LICENSE for details

using TestAssemblyNET48.Domain.ModelingObjects.NetworkElements;

namespace TestAssemblyNET48.Domain
{
	public interface INetwork
	{
		IPipes Pipes { get; }
	}
}
