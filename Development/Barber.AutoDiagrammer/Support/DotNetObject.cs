// DotNetObject.cs
// Copyright (c) 2021 Sacha Barber See LICENSE for details

// DotNetObject.cs

using System;
using System.IO;
using System.Reflection;
using System.Windows.Shapes;

namespace Barber.AutoDiagrammer.Support
{
	/// <summary>
	/// A simple helper class, that one has one method, that
	/// is used to determine if an input file is an actual
	/// CLR type file.
	/// </summary>
	public class DotNetObject
	{
		#region Public Methods
		public static bool IsValidDotNetAssembly(String file)
		{
			// Using a suggested appoach from
			// https://docs.microsoft.com/en-us/dotnet/standard/assembly/identify
			try
			{
				AssemblyName.GetAssemblyName(file);
				return true;
			}
			catch (BadImageFormatException)
			{
				return false;
			}
			catch (Exception)
			{
				return false;
			}
		}
		#endregion
	}
}
