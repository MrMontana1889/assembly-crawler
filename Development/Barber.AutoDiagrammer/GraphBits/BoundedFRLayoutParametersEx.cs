// BoundedFRLayoutParametersEx.cs

using System.Globalization;
using System.Linq;
using System.Xml.Linq;
using GraphSharp.Algorithms.Layout.Simple.FDP;

namespace Barber.AutoDiagrammer.GraphBits
{
	public class BoundedFRLayoutParametersEx : BoundedFRLayoutParameters, ISetting
    {

        public void SetFromXmlFragment(XElement fragment)
        {
            Width = double.Parse(fragment.Descendants().Where(x => x.Name.LocalName == "Width").Single().Value, CultureInfo.InvariantCulture);
            Height = double.Parse(fragment.Descendants().Where(x => x.Name.LocalName == "Height").Single().Value, CultureInfo.InvariantCulture);
            AttractionMultiplier = double.Parse(fragment.Descendants().Where(x => x.Name.LocalName == "AttractionMultiplier").Single().Value, CultureInfo.InvariantCulture);
            RepulsiveMultiplier = double.Parse(fragment.Descendants().Where(x => x.Name.LocalName == "RepulsiveMultiplier").Single().Value, CultureInfo.InvariantCulture);
            IterationLimit = int.Parse(fragment.Descendants().Where(x => x.Name.LocalName == "IterationLimit").Single().Value, CultureInfo.InvariantCulture);
        }



        public XElement GetXmlFragement()
        {
            return
                new XElement("setting", new XAttribute("type", "BoundedFR"),
                        new XElement("Width", Width),
                        new XElement("Height", Height),
                        new XElement("AttractionMultiplier", AttractionMultiplier),
                        new XElement("RepulsiveMultiplier", RepulsiveMultiplier),
                        new XElement("IterationLimit", IterationLimit));
        }

    }
}
