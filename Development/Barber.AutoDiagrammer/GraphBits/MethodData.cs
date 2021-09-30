// MethodData.cs

using System;

namespace Barber.AutoDiagrammer.GraphBits
{
	public class MethodData
    {
        #region Ctor
        public MethodData(String methodName, String methodBodyIL)
        {
            this.MethodName = methodName;
            this.MethodBodyIL = methodBodyIL;
        }
        #endregion

        #region Public Properties

        public String MethodName { get; private set; }
        public String MethodBodyIL { get; private set; }
        #endregion
    }
}
