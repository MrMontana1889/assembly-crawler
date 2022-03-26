// KKLayoutParametersEx.cs
// Copyright (c) 2021 Sacha Barber See LICENSE for details

using System.Globalization;
using System.Linq;
using System.Xml.Linq;
using GraphSharp.Algorithms.Layout.Simple.FDP;

namespace Barber.AutoDiagrammer.GraphBits
{
	public class KKLayoutParametersEx : KKLayoutParameters, ISetting
	{

		public void SetFromXmlFragment(XElement fragment)
		{
			Width = double.Parse(fragment.Descendants().Where(x => x.Name.LocalName == "Width").Single().Value, CultureInfo.InvariantCulture);
			Height = double.Parse(fragment.Descendants().Where(x => x.Name.LocalName == "Height").Single().Value, CultureInfo.InvariantCulture);
			DisconnectedMultiplier = double.Parse(fragment.Descendants().Where(x => x.Name.LocalName == "DisconnectedMultiplier").Single().Value, CultureInfo.InvariantCulture);
			K = double.Parse(fragment.Descendants().Where(x => x.Name.LocalName == "K").Single().Value, CultureInfo.InvariantCulture);
			LengthFactor = double.Parse(fragment.Descendants().Where(x => x.Name.LocalName == "LengthFactor").Single().Value, CultureInfo.InvariantCulture);
			MaxIterations = int.Parse(fragment.Descendants().Where(x => x.Name.LocalName == "MaxIterations").Single().Value, CultureInfo.InvariantCulture);
			ExchangeVertices = bool.Parse(fragment.Descendants().Where(x => x.Name.LocalName == "ExchangeVertices").Single().Value);
			AdjustForGravity = bool.Parse(fragment.Descendants().Where(x => x.Name.LocalName == "AdjustForGravity").Single().Value);
		}



		public XElement GetXmlFragement()
		{
			return
				new XElement("setting", new XAttribute("type", "KK"),
						new XElement("Width", Width),
						new XElement("Height", Height),
						new XElement("DisconnectedMultiplier", DisconnectedMultiplier),
						new XElement("K", K),
						new XElement("LengthFactor", LengthFactor),
						new XElement("MaxIterations", MaxIterations),
						new XElement("ExchangeVertices", ExchangeVertices),
						new XElement("AdjustForGravity", AdjustForGravity));
		}

	}
}
