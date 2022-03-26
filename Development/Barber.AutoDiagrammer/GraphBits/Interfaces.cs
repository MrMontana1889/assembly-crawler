// Interfaces.cs
// Copyright (c) 2021 Sacha Barber See LICENSE for details

using System.Xml.Linq;

namespace Barber.AutoDiagrammer.GraphBits
{
	public interface ISetting
	{
		void SetFromXmlFragment(XElement fragment);
		XElement GetXmlFragement();
	}
}
