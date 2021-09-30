// CreateAssemblyTreeTestFixture.cs

using System;
using System.Reflection;
using System.Threading.Tasks;
using Barber.AutoDiagrammer;
using Barber.AutoDiagrammer.GraphBits;
using Barber.AutoDiagrammer.Models;
using Barber.AutoDiagrammer.Services;
using Barber.AutoDiagrammer.Support;
using NUnit.Framework;
using TestAssemblyNET48.Water;

namespace AssemblyCrawler.Test
{
	[TestFixture]
	public class CreateAssemblyTreeTestFixture
	{
		#region Setup/Teardown
		[SetUp]
		public void Setup()
		{
			assemblyManipulationService = new AssemblyManipulationService();
		}
		[TearDown]
		public void Teardown()
		{

		}
		#endregion

		#region Tests
		[Test]
		public void TestCreateAssemblyTree()
		{
			Assembly testAssembly = Assembly.GetAssembly(typeof(OpenFlowsWater));
			Assert.IsTrue(DotNetObject.IsValidDotNetAssembly(testAssembly.Location));

			if (DotNetObject.IsValidDotNetAssembly(testAssembly.Location))
			{
				Task task = assemblyManipulationService.LoadNameSpacesAndTypes(testAssembly.Location);
				bool finishedOk = task.Wait(20000);

				if (finishedOk)
				{
					var treeValues = assemblyManipulationService.TreeValues;
					Assert.IsTrue(treeValues.Count > 0);
				}
			}
		}
		[Test]
		public /*async*/ void TestCreateAssemblyTreeAndGraph()
		{
			Assembly testAssembly = Assembly.GetAssembly(typeof(OpenFlowsWater));
			Assert.IsTrue(DotNetObject.IsValidDotNetAssembly(testAssembly.Location));

			SettingsViewModel.Instance.SetGraphObject(null);
			SettingsViewModel.Instance.LayoutAlgorithmType = "Tree";
			SettingsViewModel.Instance.IncludeConstructorParametersAsAssociations = false;
			SettingsViewModel.Instance.IncludeFieldTypesAsAssociations = false;
			SettingsViewModel.Instance.IncludeMethodArgumentAsAssociations = false;
			SettingsViewModel.Instance.IncludePropertyTypesAsAssociations = false;

			SimpleTreeLayoutParametersEx settings = (SimpleTreeLayoutParametersEx)SettingsViewModel.Instance.LayoutParameters;
			settings.Direction = GraphSharp.Algorithms.Layout.LayoutDirection.RightToLeft;

			if (DotNetObject.IsValidDotNetAssembly(testAssembly.Location))
			{
				Task task = assemblyManipulationService.LoadNameSpacesAndTypes(testAssembly.Location);
				bool finishedOk = task.Wait(20000);

				if (finishedOk)
				{
					var treeValues = assemblyManipulationService.TreeValues;
					Assert.IsTrue(treeValues.Count > 0);

					treeValues[0].IsChecked = true;

					RecursivelyAddItems(treeValues[0]);

					var graphResults = assemblyManipulationService.CreateGraphAsync();

					Assert.IsNotNull(graphResults);

					foreach (var v in graphResults.Vertices)
						Console.WriteLine(v.Name);
				}
			}
		}

		private void RecursivelyAddItems(AssemblyTreeViewModel model)
		{
			if (model.NodeType != RepresentationType.Class)
			{
				foreach (var child in model.Children)
				{
					if (child.NodeType == RepresentationType.Class)
						assemblyManipulationService.SelectedTreeValues.Add(child);
					else
						RecursivelyAddItems(child);
				}
			}
		}
		#endregion

		#region Private Fields
		private IAssemblyManipulationService assemblyManipulationService;
		#endregion
	}
}
