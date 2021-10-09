// Interfaces.cs
// Copyright (c) 2021 Sacha Barber  See LICENSE for details

using System.Collections.Generic;
using System.Threading.Tasks;
using Barber.AutoDiagrammer.GraphBits;
using Barber.AutoDiagrammer.Models;
using Barber.AutoDiagrammer.Support;

namespace Barber.AutoDiagrammer
{
	public interface IAssemblyManipulationService
	{
		List<AssemblyTreeViewModel> TreeValues { get; }
		List<AssemblyTreeViewModel> SelectedTreeValues { get; }
		GraphResults CreateGraph();
		void ReInitialise();
		void CalculateSelectedTreeValues();
		Task LoadNameSpacesAndTypes(string assemblyFileName, ITypeFilter typeFilter);

		void LoadNameSpacesAndTypesAsync(string assemblyFileName, ITypeFilter typeFilter);
	}

	public interface ITreeCreator
	{
		List<AssemblyTreeViewModel> ScanAssemblyAndCreateTree(string assemblyFileName, ITypeFilter typeFitler);
	}
}
