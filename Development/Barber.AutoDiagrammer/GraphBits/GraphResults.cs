// GraphResults.cs
// Copyright (c) 2021 Sacha Barber  See LICENSE for details

using System.Collections.Generic;

namespace Barber.AutoDiagrammer.GraphBits
{
	public class GraphResults
    {
        #region Data
        public List<PocVertex> Vertices { get; private set; }
        public List<PocEdge> Edges { get; private set; }
        #endregion

        #region Ctor
        public GraphResults(List<PocVertex> vertices, List<PocEdge> edges)
        {
            this.Vertices = vertices;
            this.Edges = edges;
        }
        #endregion
    }
}
