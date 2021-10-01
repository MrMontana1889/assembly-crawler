// EfficientSugiyamaLayoutParametersEx.cs

using System;
using System.Globalization;
using System.Linq;
using System.Xml.Linq;
using GraphSharp.Algorithms.Layout.Simple.Hierarchical;

namespace Barber.AutoDiagrammer.GraphBits
{
	public class EfficientSugiyamaLayoutParametersEx : EfficientSugiyamaLayoutParameters, ISetting
    {

        public void SetFromXmlFragment(XElement fragment)
        {
            LayerDistance = double.Parse(fragment.Descendants().Where(x => x.Name.LocalName == "LayerDistance").Single().Value, CultureInfo.InvariantCulture);
            VertexDistance = double.Parse(fragment.Descendants().Where(x => x.Name.LocalName == "VertexDistance").Single().Value, CultureInfo.InvariantCulture);
            PositionMode = int.Parse(fragment.Descendants().Where(x => x.Name.LocalName == "PositionMode").Single().Value, CultureInfo.InvariantCulture);
            MinimizeEdgeLength = bool.Parse(fragment.Descendants().Where(x => x.Name.LocalName == "MinimizeEdgeLength").Single().Value);
            EdgeRouting = (SugiyamaEdgeRoutings)Enum.Parse(typeof(SugiyamaEdgeRoutings), fragment.Descendants().Where(x => x.Name.LocalName == "EdgeRouting").Single().Value);
            OptimizeWidth = bool.Parse(fragment.Descendants().Where(x => x.Name.LocalName == "OptimizeWidth").Single().Value);
        }



        public XElement GetXmlFragement()
        {
            return
                new XElement("setting", new XAttribute("type", "EfficientSugiyama"),
                        new XElement("LayerDistance", LayerDistance),
                        new XElement("VertexDistance", VertexDistance),
                        new XElement("PositionMode", PositionMode),
                        new XElement("MinimizeEdgeLength", MinimizeEdgeLength),
                        new XElement("EdgeRouting", EdgeRouting),
                        new XElement("OptimizeWidth", OptimizeWidth));
        }

    }
}
