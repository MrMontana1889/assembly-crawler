// TestModel.cs
// Copyright (c) 2021 Kristopher L. Culin See LICENSE for details

namespace TestAssemblyNET48.Water
{
	public class TestModel : ITestModel
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
