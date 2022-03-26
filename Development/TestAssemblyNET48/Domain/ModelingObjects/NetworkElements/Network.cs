// Network.cs
// Copyright (c) 2022 Kristopher L. Culin See LICENSE for details

namespace TestAssemblyNET48.Water.Domain.ModelingObjects.NetworkElements
{
	public class Network : INetwork
	{
		#region Constructor
		public Network()
		{

		}
		#endregion

		#region Public Properties
		public IPipes Pipes { get; } = new Pipes();
		#endregion
	}
}
