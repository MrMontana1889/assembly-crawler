﻿// WriterBase.cs
// Copyright (c) 2021 Kristopher L. Culin see LICENSE for details

using System.IO;

namespace AssemblyCrawler.Support
{
	public abstract class WriterBase
	{
		#region Constructor
		public WriterBase(PythonClass pythonClass)
		{
			Class = pythonClass;
		}
		#endregion

		#region Public Methods
		public abstract void Write(StreamWriter writer);
		#endregion

		#region Protected Methods
		protected abstract void Initialize();
		#endregion

		#region Proected Properties
		protected PythonClass Class { get; }
		#endregion
	}
}
