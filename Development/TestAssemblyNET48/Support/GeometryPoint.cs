// GeometryPoint.cs
// Copyright (c) 2021 Kristopher L. Culin See LICENSE for details

namespace TestAssemblyNET48.Support
{
	public struct GeometryPoint
	{
		#region Constructor
		public GeometryPoint(double x, double y, double z)
		{
			X = x;
			Y = y;
			Z = z;
		}
		#endregion

		#region Public Properties
		public double X
		{
			get => x;
			set => x = value;
		}
		public double Y
		{
			get => y;
			set => y = value;
		}
		public double Z
		{
			get => z;
			set => z = value;
		}
		#endregion

		#region Public Fields
		public double x;
		public double y;
		public double z;
		#endregion
	}
}
