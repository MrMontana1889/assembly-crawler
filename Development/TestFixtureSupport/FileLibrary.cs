// FileLibrary.cs
// Copyright (c) 2022 Kristopher L. Culin See LICENSE for details

using System.Diagnostics;
using System.IO;

namespace TestFixtureSupport
{
	public static class FileLibrary
	{
		#region Public Methods
		public static void SetReadWriteSafely(string path)
		{
			try
			{
				File.SetAttributes(path,
					File.GetAttributes(path) & (FileAttributes.ReadOnly ^ (FileAttributes)0xffff));
			}
			catch
			{
				Trace.WriteLine($"Unable to set attributes for file {path}");
			}
		}
		#endregion
	}
}
