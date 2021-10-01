// Enumerations.cs

using System.ComponentModel;

namespace Barber.AutoDiagrammer.Models
{
	public enum AccessModifierTypes : int
    {
        [Description(@"All")]
        All = 1,

        [Description(@"Public")]
        Public = 2,

        [Description(@"Public And Static")]
        PublicAndStatic = 3
    }
}
