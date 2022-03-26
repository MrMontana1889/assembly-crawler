// Pipe.cs
// Copyright (c) 2022 Kristopher L. Culin See LICENSE for details

using System;
using System.Security.Permissions;

namespace Test.TestGenericAssembly.Links
{
	internal class Pipe : IPipe, IPipeInput, IPipeResults
	{
		public IPipeInput Input => this;
		public IPipeResults Results => this;
		public IPipes Manager { get; }
		public int Id { get; }
		public string Label { get; set; }

		/// <summary>
		/// Long text about the element goes here. 
		/// If Id and Lable shows the doc string then they
		/// came from base type
		/// </summary>
		public string Notes { get; set; }

		/// <summary>
		/// Delete a Pipe
		/// </summary>
		/// <exception cref="NotImplementedException">Throws not implemented exception</exception>
		/// <permission cref="PermissionSetAttribute">No all user profile can delete</permission>
		/// <remarks>No undo available</remarks>
		[PermissionSet(SecurityAction.LinkDemand, Name = "FullTrust")]
		public void Delete()
		{
			throw new System.NotImplementedException();
		}
	}
}
