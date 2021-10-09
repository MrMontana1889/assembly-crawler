// Interfaces.cs
// Copyright (c) 2021 See LICENSE for details

using System;

namespace Barber.AutoDiagrammer.Support
{
	public interface ITypeFilter
	{
		bool IncludeType(Type t);
	}
}
