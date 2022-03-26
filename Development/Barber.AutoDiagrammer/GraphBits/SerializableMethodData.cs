// SerializableMethodData.cs
// Copyright (c) 2021 Sacha Barber See LICENSE for details

using System;

namespace Barber.AutoDiagrammer.GraphBits
{
	[Serializable]
	public class SerializableMethodData
	{
		#region Ctor
		public SerializableMethodData(string methodName, string methodBodyIL)
		{
			MethodName = methodName;
			MethodBodyIL = methodBodyIL;
		}
		#endregion

		#region Public Properties

		public string MethodName { get; }
		public string MethodBodyIL { get; }

		#endregion
	}
}
