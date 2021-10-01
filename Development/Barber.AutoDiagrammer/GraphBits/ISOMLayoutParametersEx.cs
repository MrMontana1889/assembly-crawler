// ISOMLayoutParametersEx.cs

using System.Globalization;
using System.Linq;
using System.Xml.Linq;
using GraphSharp.Algorithms.Layout.Simple.FDP;

namespace Barber.AutoDiagrammer.GraphBits
{
	public class ISOMLayoutParametersEx : ISOMLayoutParameters, ISetting
    {

        public void SetFromXmlFragment(XElement fragment)
        {
            Width = double.Parse(fragment.Descendants().Where(x => x.Name.LocalName == "Width").Single().Value, CultureInfo.InvariantCulture);
            Height = double.Parse(fragment.Descendants().Where(x => x.Name.LocalName == "Height").Single().Value, CultureInfo.InvariantCulture);
            InitialAdaption = double.Parse(fragment.Descendants().Where(x => x.Name.LocalName == "InitialAdaption").Single().Value, CultureInfo.InvariantCulture);
            MinAdaption = double.Parse(fragment.Descendants().Where(x => x.Name.LocalName == "MinAdaption").Single().Value, CultureInfo.InvariantCulture);
            CoolingFactor = double.Parse(fragment.Descendants().Where(x => x.Name.LocalName == "CoolingFactor").Single().Value, CultureInfo.InvariantCulture);
            MaxEpoch = int.Parse(fragment.Descendants().Where(x => x.Name.LocalName == "MaxEpoch").Single().Value, CultureInfo.InvariantCulture);
            RadiusConstantTime = int.Parse(fragment.Descendants().Where(x => x.Name.LocalName == "RadiusConstantTime").Single().Value, CultureInfo.InvariantCulture);
            InitialRadius = int.Parse(fragment.Descendants().Where(x => x.Name.LocalName == "InitialRadius").Single().Value, CultureInfo.InvariantCulture);
            MinRadius = int.Parse(fragment.Descendants().Where(x => x.Name.LocalName == "MinRadius").Single().Value, CultureInfo.InvariantCulture);
        }



        public XElement GetXmlFragement()
        {
            return
                new XElement("setting", new XAttribute("type", "ISOM"),
                        new XElement("Width", Width),
                        new XElement("Height", Height),
                        new XElement("InitialAdaption", InitialAdaption),
                        new XElement("MinAdaption", MinAdaption),
                        new XElement("CoolingFactor", CoolingFactor),
                        new XElement("MaxEpoch", MaxEpoch),
                        new XElement("RadiusConstantTime", RadiusConstantTime),
                        new XElement("InitialRadius", InitialRadius),
                        new XElement("MinRadius", MinRadius));
        }

    }
}
