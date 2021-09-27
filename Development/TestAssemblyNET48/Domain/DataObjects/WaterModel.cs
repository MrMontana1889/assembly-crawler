// WaterModel.cs
// Copyright (c) 2021 Kristopher L. Culin See LICENSE for details

using TestAssemblyNET48.Water.Domain.ModelingObjects.NetworkElements;

namespace TestAssemblyNET48.Water.Domain.DataObjects
{
	public class WaterModel : IWaterModel
	{
		#region Constructor
		public WaterModel(string filenmae)
		{

		}
		#endregion

		#region Public Properties
		public INetwork Network { get; } = new Network();
		#endregion
	}
}
