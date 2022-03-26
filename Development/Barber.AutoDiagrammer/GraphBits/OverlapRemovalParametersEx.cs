// OverlapRemovalParametersEx.cs
// Copyright (c) 2021 Sacha Barber See LICENSE for details

using System.Globalization;
using System.Linq;
using System.Xml.Linq;
using GraphSharp.Algorithms.OverlapRemoval;

namespace Barber.AutoDiagrammer.GraphBits
{
	public class OverlapRemovalParametersEx : OverlapRemovalParameters, ISetting
	{

		public void SetFromXmlFragment(XElement fragment)
		{
			HorizontalGap = float.Parse(fragment.Descendants().Where(x => x.Name.LocalName == "HorizontalGap").Single().Value, CultureInfo.InvariantCulture);
			VerticalGap = float.Parse(fragment.Descendants().Where(x => x.Name.LocalName == "VerticalGap").Single().Value, CultureInfo.InvariantCulture);
		}



		public XElement GetXmlFragement()
		{
			return
				new XElement("setting", new XAttribute("type", "Overlap"),
						new XElement("HorizontalGap", HorizontalGap),
						new XElement("VerticalGap", VerticalGap));
		}

	}
}
