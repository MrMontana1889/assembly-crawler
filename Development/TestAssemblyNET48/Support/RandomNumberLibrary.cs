// RandomNumberLibrary.cs
// Copyright (c) 2022 Kristopher L. Culin See LICENSE for details

using System;
using System.Collections.Generic;

namespace TestAssemblyNET48.Water.Support
{
	internal static class RandomNumberLibrary
	{
		#region Public Methods
		public static int GetNextID()
		{
			int id = int.MinValue;
			while (!IDs.Contains(id))
			{
				id = rnd.Next(1, int.MaxValue);
				if (!IDs.Contains(id))
				{
					IDs.Add(id);
					break;
				}
			}

			return id;
		}
		#endregion

		#region Private Properties
		private static List<int> IDs { get; } = new List<int>();
		#endregion

		#region Private Fields
		private static Random rnd = new Random(8);
		#endregion
	}
}
