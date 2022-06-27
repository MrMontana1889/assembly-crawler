// OpenFlowsWater.cs
// Copyright (c) 2022 Kristopher L. Culin See LICENSE for details

using TestAssemblyNET48.Water.Domain.DataObjects;

namespace TestAssemblyNET48.Water
{
	public static class OpenFlowsWater
    {
		#region Public Methods
		public static void StartSession()
		{
			_sessionStarted = true;
		}
		public static IWaterModel Open(string filename)
		{
			if (!_sessionStarted) return null;

			return new WaterModel(filename);
		}
		public static IWaterModel GetModel()
		{
			if (!_sessionStarted) return null;

			return new WaterModel(string.Empty);
		}
		public static void EndSession()
		{
			_sessionStarted = false;
		}
		#endregion

		#region Private Fields
		private static bool _sessionStarted;
		#endregion
	}
}
