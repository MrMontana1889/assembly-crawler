// Pipes.cs
// Copyright (c) 2021 Kristopher L. Culin See LICENSE for details

using System.Collections.Generic;
using TestAssemblyNET48.Water.Support;

namespace TestAssemblyNET48.Water.Domain.ModelingObjects.NetworkElements
{
	public class Pipes : ElementManagerBase<IPipe>, IPipes, IPipesInput, IPipesResults
	{
		#region Constructor
		public Pipes()
		{

		}
		#endregion

		#region Public Methods
		public IDictionary<int, double> Diameters()
		{
			IDictionary<int, double> retval = new Dictionary<int, double>(Count);
			foreach (int id in ElementIDs())
				retval[id] = double.NaN;
			return retval;
		}
		public IDictionary<int, double?> Flows()
		{
			return Flows(0);
		}
		public IDictionary<int, double?> Flows(int timeStepIndex)
		{
			return Flows(timeStepIndex, ElementIDs());
		}
		public IDictionary<int, double?> Flows(int timeStepIndex, List<int> ids)
		{
			IDictionary<int, double?> retVal = new Dictionary<int, double?>(Count);
			foreach (int id in ids)
				retVal[id] = double.NaN;
			return retVal;
		}
		#endregion

		#region Public Porperties
		public IPipesInput Input => this;
		public IPipesResults Results => this;
		#endregion

		#region Protected Methods
		protected override IPipe NewElement()
		{
			return new Pipe(RandomNumberLibrary.GetNextID());
		}
		#endregion
	}
}
