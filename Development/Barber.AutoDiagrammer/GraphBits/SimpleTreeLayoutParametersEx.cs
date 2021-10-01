// SimpleTreeLayoutParametersEx.cs

using System;
using System.Globalization;
using System.Linq;
using System.Xml.Linq;
using GraphSharp.Algorithms.Layout;
using GraphSharp.Algorithms.Layout.Simple.Tree;

namespace Barber.AutoDiagrammer.GraphBits
{
	public class SimpleTreeLayoutParametersEx : SimpleTreeLayoutParameters, ISetting
    {

        public void SetFromXmlFragment(XElement fragment)
        {
            LayerGap = double.Parse(fragment.Descendants().Where(x => x.Name.LocalName == "LayerGap").Single().Value, CultureInfo.InvariantCulture);
            VertexGap = double.Parse(fragment.Descendants().Where(x => x.Name.LocalName == "VertexGap").Single().Value, CultureInfo.InvariantCulture);
            SpanningTreeGeneration = (SpanningTreeGeneration)Enum.Parse(typeof(SpanningTreeGeneration), fragment.Descendants().Where(x => x.Name.LocalName == "SpanningTreeGeneration").Single().Value);
            Direction = (LayoutDirection)Enum.Parse(typeof(LayoutDirection), fragment.Descendants().Where(x => x.Name.LocalName == "Direction").Single().Value);
        }



        public XElement GetXmlFragement()
        {
            return
                new XElement("setting", new XAttribute("type", "Tree"),
                        new XElement("LayerGap", LayerGap),
                        new XElement("VertexGap", VertexGap),
                        new XElement("SpanningTreeGeneration", SpanningTreeGeneration),
                        new XElement("Direction", Direction));
        }

    }
}
