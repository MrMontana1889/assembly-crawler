﻿// EntryPoint.cs
// Copyright (c) 2021 Kristopher L. Culin See LICENSE for details

namespace TestAssemblyNET48.Water
{
	public static class EntryPoint
    {
		#region Public Methods
		public static void StartSession()
		{
			_sessionStarted = true;
		}
		public static ITestModel Open(string filename)
		{
			if (!_sessionStarted) return null;

			return new TestModel(filename);
		}
		public static TestModel GetModel()
		{
			if (!_sessionStarted) return null;

			return new TestModel(string.Empty);
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
