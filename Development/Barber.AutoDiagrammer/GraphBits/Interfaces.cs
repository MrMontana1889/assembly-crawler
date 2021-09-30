// Interfaces.cs

using System.Xml.Linq;

namespace Barber.AutoDiagrammer.GraphBits
{
	public interface ISetting
    {
        void SetFromXmlFragment(XElement fragment);
        XElement GetXmlFragement();
    }
}
