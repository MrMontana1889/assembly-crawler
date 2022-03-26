// PocGraph.cs
// Copyright (c) 2021 Sacha Barber See LICENSE for details

using QuickGraph;

namespace Barber.AutoDiagrammer.GraphBits
{
	public class PocGraph : BidirectionalGraph<PocVertex, PocEdge>
	{
		public PocGraph() { }

		public PocGraph(bool allowParallelEdges)
			: base(allowParallelEdges) { }

		public PocGraph(bool allowParallelEdges, int vertexCapacity)
			: base(allowParallelEdges, vertexCapacity) { }
	}
}
