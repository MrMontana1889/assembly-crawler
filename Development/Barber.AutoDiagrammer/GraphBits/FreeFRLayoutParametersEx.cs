// FreeFRLayoutParametersEx.cs
// Copyright (c) 2021 Sacha Barber See LICENSE for details

using System.Globalization;
using System.Linq;
using System.Xml.Linq;
using GraphSharp.Algorithms.Layout.Simple.FDP;

namespace Barber.AutoDiagrammer.GraphBits
{
	public class FreeFRLayoutParametersEx : FreeFRLayoutParameters, ISetting
	{

		public void SetFromXmlFragment(XElement fragment)
		{

			IdealEdgeLength = double.Parse(fragment.Descendants().Where(x => x.Name.LocalName == "IdealEdgeLength").Single().Value, CultureInfo.InvariantCulture);
		}



		public XElement GetXmlFragement()
		{
			return
				new XElement("setting", new XAttribute("type", "FR"),
						new XElement("IdealEdgeLength", IdealEdgeLength));
		}

	}
}
