// AssemblyManipulationService.cs
// Copyright (c) 2021 Sacha Barber See LICENSE for details

using System;
using System.Collections.Generic;
using System.ComponentModel.Composition;
using System.Linq;
using System.Threading.Tasks;
using Barber.AutoDiagrammer.GraphBits;
using Barber.AutoDiagrammer.Models;
using Barber.AutoDiagrammer.Support;

namespace Barber.AutoDiagrammer.Services
{
	/// <summary>
	/// This class implements the IPrintXPSFileService
	/// </summary>
	[PartCreationPolicy(CreationPolicy.Shared)]
	public class AssemblyManipulationService : IAssemblyManipulationService
	{
		#region Data
		private ITreeCreator treeCreator;
		private List<AssemblyTreeViewModel> treeValues;
		private List<AssemblyTreeViewModel> selectedTreeValues = new List<AssemblyTreeViewModel>();
		#endregion

		#region Ctor
		// private to prevent direct instantiation.
		public AssemblyManipulationService()
		{
			treeCreator = new TreeCreator();
		}
		#endregion

		#region Public Properties

		public List<AssemblyTreeViewModel> TreeValues
		{
			get { return treeValues; }
		}


		public List<AssemblyTreeViewModel> SelectedTreeValues
		{
			get
			{
				return selectedTreeValues;
			}
		}
		#endregion

		#region Public Methods
		public GraphResults CreateGraph()
		{
			List<PocVertex> vertices = new List<PocVertex>();
			for (int i = 0; i < selectedTreeValues.Count; ++i)
			{
				SerializableVertex serializableVertex = selectedTreeValues[i].Vertex;
				PocVertex vertex = new PocVertex(
					serializableVertex.Name,
					serializableVertex.ShortName,
					serializableVertex.Constructors,
					serializableVertex.Fields,
					serializableVertex.Properties,
					serializableVertex.Interfaces,
					TranslateMethods(serializableVertex.Methods),
					serializableVertex.Events,
					serializableVertex.Associations,
					serializableVertex.HasConstructors,
					serializableVertex.HasFields,
					serializableVertex.HasProperties,
					serializableVertex.HasInterfaces,
					serializableVertex.HasMethods,
					serializableVertex.HasEvents);

				vertices.Add(vertex);
			}

			List<PocEdge> edges = new List<PocEdge>();
			foreach (var x in vertices)
			{
				PocVertex vertex1 = x;

				foreach (string associationName in vertex1.Associations)
				{
					var matchinVertices = from vert in vertices
										  where vert.Name == associationName
										  select vert;
					PocVertex vertex2 = matchinVertices.SingleOrDefault();

					if (vertex2 != null)
					{
						if (vertex1.Name != vertex2.Name)
						{
							//TODO : Need to make sure both of these are in the
							//list of selected items in the tree before they are added
							edges.Add(AddNewGraphEdge(vertex1, vertex2));
							vertex1.NumberOfEdgesFromThisVertex += 1;
							vertex2.NumberOfEdgesToThisVertex += 1;
						}
					}

				}
			}

			return new GraphResults(vertices, edges);
		}

		public void ReInitialise()
		{
			selectedTreeValues = new List<AssemblyTreeViewModel>();
			treeValues = new List<AssemblyTreeViewModel>();
		}

		public void CalculateSelectedTreeValues()
		{
			List<AssemblyTreeViewModel> results = new List<AssemblyTreeViewModel>();

			if (treeValues != null && treeValues.Count > 0)
				RecurseTreeLookingForSelected(treeValues[0], results);

			selectedTreeValues = results;
		}


		public Task LoadNameSpacesAndTypes(String assemblyFileName, ITypeFilter typeFilter)
		{
			Task task = Task.Factory.StartNew(() =>
			{

				try
				{
					treeValues = treeCreator.ScanAssemblyAndCreateTree(assemblyFileName, typeFilter);
					return treeValues;
				}
				catch (Exception ex)
				{
					treeValues = null;
					throw ex;
				}
			});
			return task;
		}
		public void LoadNameSpacesAndTypesAsync(String assemblyFileName, ITypeFilter typeFilter)
		{
			try
			{
				treeValues = treeCreator.ScanAssemblyAndCreateTree(assemblyFileName, typeFilter);
			}
			catch (Exception ex)
			{
				treeValues = null;
				throw ex;
			}
		}

		#endregion

		#region Private Methods

		private List<MethodData> TranslateMethods(List<SerializableMethodData> serializedMethods)
		{
			return (from x in serializedMethods
					select new MethodData(x.MethodName, x.MethodBodyIL)).ToList();

		}


		private void RecurseTreeLookingForSelected(AssemblyTreeViewModel parent, List<AssemblyTreeViewModel> selectedTreeValues)
		{
			if (parent.IsChecked == true && parent.NodeType == RepresentationType.Class)
			{
				if (!selectedTreeValues.Contains(parent))
					selectedTreeValues.Add(parent);
			}

			foreach (AssemblyTreeViewModel child in parent.Children)
			{
				if (child.IsChecked == true && child.NodeType == RepresentationType.Class)
				{
					if (!selectedTreeValues.Contains(child))
						selectedTreeValues.Add(child);
				}
				RecurseTreeLookingForSelected(child, selectedTreeValues);
			}
		}

		private PocEdge AddNewGraphEdge(PocVertex from, PocVertex to)
		{
			string edgeString = string.Format("{0}-{1} Connected", from.Name, to.Name);
			PocEdge newEdge = new PocEdge(edgeString, from, to);
			return newEdge;
		}
		#endregion
	}
}
