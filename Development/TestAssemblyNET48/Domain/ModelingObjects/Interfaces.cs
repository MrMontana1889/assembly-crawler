// Interfaces.cs
// Copyright (c) 2021 Kristopher L. Culin See LICENSE for details

using System.Collections.Generic;

namespace TestAssemblyNET48.Domain.ModelingObjects
{
	public interface IElementInput
	{

	}
	public interface IElementsInput
	{

	}
	public interface IElementResults
	{

	}
	public interface IElementsResults
	{

	}
	public interface IElement
	{
		int Id { get; }
		string Label { get; set; }
		string Notes { get; set; }
	}

	public interface IElementManager
	{ 
		int Count { get; }
		List<int> ElementIDs();
		bool Exists(int id);
	}

}
