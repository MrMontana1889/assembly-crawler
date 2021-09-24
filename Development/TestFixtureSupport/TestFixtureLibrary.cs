// TestFixtureLibrary.cs
// Copyright (c) 2021 Kristopher L. Culin See LICENSE for details.

using System;
using System.Collections.Specialized;
using System.Diagnostics;
using System.IO;

namespace TestFixtureSupport
{
	public static class TestFixtureLibrary
	{
		#region Public Methods
		public static void CopyTestFile(string source)
		{
			CopyTestFile(source, Path.GetFileName(source));
		}
		public static void CopyTestFile(string source, string filename)
		{
			DeleteFile(filename);
			Debug.Assert(!File.Exists(filename));
			File.Copy(source, filename, true);
			FileLibrary.SetReadWriteSafely(filename);
		}
		public static void DeleteFile(string path, bool showOutput)
		{
			try
			{
				if (File.Exists(path))
				{
					FileLibrary.SetReadWriteSafely(path);
					File.Delete(path);
					if (showOutput)
						Trace.WriteLine($"Delete: {path}");
				}
			}
			catch (Exception) { }
		}
		public static void DeleteFile(string path)
		{
			DeleteFile(path, true);
		}
		public static void FlushCache()
		{
			m_preparedFiles = null;
		}
		public static void PrepareTestFile(string filename, string source)
		{
			if (!WasPrepared(source))
			{
				CopyTestFile(source, filename);
				MarkPrepared(source);
			}
		}
		#endregion

		#region Private Methods
		private static void MarkPrepared(string path)
		{
			PreparedFiles.Add(path.ToLowerInvariant());
		}
		private static bool WasPrepared(string path)
		{
			return PreparedFiles.Contains(path.ToLowerInvariant());
		}
		#endregion

		#region Private Properties
		private static StringCollection PreparedFiles
		{
			get
			{
				if (m_preparedFiles == null)
					m_preparedFiles = new StringCollection();
				return m_preparedFiles;
			}
		}
		#endregion

		#region Private Fields
		private static StringCollection m_preparedFiles;
		#endregion
	}
}
