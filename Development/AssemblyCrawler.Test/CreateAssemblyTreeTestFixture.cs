// CreateAssemblyTreeTestFixture.cs

using System;
using System.IO;
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
				var treeTask = assemblyManipulationService.LoadNameSpacesAndTypes(testAssembly.Location);
				bool finishedOk = treeTask.Wait(10000);
				Assert.IsTrue(finishedOk);

				Assert.IsNotNull(assemblyManipulationService.TreeValues, "TreeValues are null.");
				var treeValues = assemblyManipulationService.TreeValues;
				Assert.IsTrue(treeValues.Count > 0);
			}
		}
		[Test]
		public void TestCreateAssemblyTreeAndGraph()
		{
			Assembly testAssembly = Assembly.GetAssembly(typeof(OpenFlowsWater));
			Assert.IsTrue(DotNetObject.IsValidDotNetAssembly(testAssembly.Location));

			ConfigureSettings();

			if (DotNetObject.IsValidDotNetAssembly(testAssembly.Location))
			{
				assemblyManipulationService.LoadNameSpacesAndTypesAsync(testAssembly.Location);

				var treeValues = assemblyManipulationService.TreeValues;
				Assert.IsTrue(treeValues.Count > 0);

				treeValues[0].IsChecked = true;

				RecursivelyAddItems(treeValues[0]);

				var graphResults = assemblyManipulationService.CreateGraph();

				Assert.IsNotNull(graphResults);

				foreach (var v in graphResults.Vertices)
					Console.WriteLine(v.Name);

			}
		}

		[Test]
		public void TestOFTreeAndGraph()
		{
			string sourcePath = @"D:\p4\Glacier\Products\WaterGEMS\Output\_Starter\x64\Debug";
			if (!Directory.Exists(sourcePath))
			{
				Assert.Pass($"{sourcePath} does not exist on this computer.  Unable to run unit test.");
				return;
			}

			string openFlowsAssemblyFilename = Path.Combine(sourcePath, "OpenFlows.dll");
			Assert.IsTrue(DotNetObject.IsValidDotNetAssembly(openFlowsAssemblyFilename));

			assemblyManipulationService.LoadNameSpacesAndTypesAsync(openFlowsAssemblyFilename);

			Assert.IsNotNull(assemblyManipulationService.TreeValues, "TreeValues is null");
			Assert.AreEqual(1, assemblyManipulationService.TreeValues.Count);

			ConfigureSettings();

			var treeValues = assemblyManipulationService.TreeValues;
			treeValues[0].IsChecked = true;

			RecursivelyAddItems(treeValues[0]);

			var graphResults = assemblyManipulationService.CreateGraph();
			Assert.IsNotNull(graphResults);

			foreach (var v in graphResults.Vertices)
				Console.WriteLine(v.Name);
		}
		[Test]
		public void TestOFWTreeAndGraph()
		{
			string sourcePath = @"D:\p4\Glacier\Products\WaterGEMS\Output\_Starter\x64\Debug";
			if (!Directory.Exists(sourcePath))
			{
				Assert.Pass($"{sourcePath} does not exist on this computer.  Unable to run unit test.");
				return;
			}

			string openFlowsAssemblyFilename = Path.Combine(sourcePath, "OpenFlows.Water.dll");
			Assert.IsTrue(DotNetObject.IsValidDotNetAssembly(openFlowsAssemblyFilename));

			assemblyManipulationService.LoadNameSpacesAndTypesAsync(openFlowsAssemblyFilename);

			Assert.IsNotNull(assemblyManipulationService.TreeValues, "TreeValues is null");
			Assert.AreEqual(1, assemblyManipulationService.TreeValues.Count);

			ConfigureSettings();

			var treeValues = assemblyManipulationService.TreeValues;
			treeValues[0].IsChecked = true;

			RecursivelyAddItems(treeValues[0]);

			var graphResults = assemblyManipulationService.CreateGraph();
			Assert.IsNotNull(graphResults);

			foreach (var v in graphResults.Vertices)
				Console.WriteLine(v.Name);
		}
		#endregion

		#region Private Methods
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
		private static void ConfigureSettings()
		{
			SettingsViewModel.Instance.SetGraphObject(null);
			SettingsViewModel.Instance.LayoutAlgorithmType = "Tree";
			SettingsViewModel.Instance.IncludeConstructorParametersAsAssociations = false;
			SettingsViewModel.Instance.IncludeFieldTypesAsAssociations = false;
			SettingsViewModel.Instance.IncludeMethodArgumentAsAssociations = false;
			SettingsViewModel.Instance.IncludePropertyTypesAsAssociations = false;

			SimpleTreeLayoutParametersEx settings = (SimpleTreeLayoutParametersEx)SettingsViewModel.Instance.LayoutParameters;
			settings.Direction = GraphSharp.Algorithms.Layout.LayoutDirection.RightToLeft;
		}
		#endregion

		#region Private Fields
		private IAssemblyManipulationService assemblyManipulationService;
		#endregion
	}
}
