// TestModel.cs
// Copyright (c) 2021 Kristopher L. Culin See LICENSE for details

using TestAssemblyNET48.Domain.ModelingObjects.NetworkElements;

namespace TestAssemblyNET48.Domain.DataObjects
{
	internal class TestModel : ITestModel
	{
		#region Constructor
		public TestModel(string filenmae)
		{

		}
		#endregion

		#region Public Properties
		public INetwork Network { get; } = new Network();
		#endregion
	}
}
