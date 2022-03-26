// Pipe.cs
// Copyright (c) 2022 Kristopher L. Culin See LICENSE for details

using System.Collections.Generic;
using TestAssemblyNET48.Water.Support;

namespace TestAssemblyNET48.Water.Domain.ModelingObjects.NetworkElements
{
	public class Pipe : ElementBase<IPipes, IPipe, IPipeInput, IPipeResults, IPipesInput, IPipesResults>, IPipe, IPipeInput, IPipeResults
	{
		#region Constructor
		public Pipe(int id) 
			: base(id)
		{
		}
		#endregion

		#region Public Methods
		public double? Flow()
		{
			return Flow(0);
		}
		public double? Flow(int timeStepIndex)
		{
			return double.NaN;
		}
		public List<GeometryPoint> GetPoints()
		{
			return new List<GeometryPoint>();
		}
		public void SetPoints(List<GeometryPoint> points)
		{
			// no-op
		}
		#endregion

		#region Public Properties
		public override IPipeInput Input => this;
		public override IPipeResults Results => this;
		public double Diameter { get; set; }
		public IElement StartNode { get; set; }
		public IElement StopNode { get; set; }
		public bool IsUserDefinedLength { get; set; }
		public double Length { get; set; }
		public bool IsActive { get; set; }
		#endregion
	}
}
