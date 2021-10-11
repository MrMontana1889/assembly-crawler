using System.Collections.Generic;
using TestAssemblyNET48.Water.Domain.ModelingObjects;

namespace TestAssemblyNET48.Domain.ModelingObjects
{
	public class ElementsBase<TElementType> : IElements<TElementType>
		where TElementType : class, IElement
	{
		#region Constructor
		public ElementsBase()
		{

		}

		public int Count { get; }

		public List<int> ElementIDs()
		{
			throw new System.NotImplementedException();
		}
		#endregion

		#region Public Methods
		public List<TElementType> Elements(ElementStateType state)
		{
			return new List<TElementType>();
		}

		public List<TElementType> Elements()
		{
			throw new System.NotImplementedException();
		}

		public bool Exists(int id)
		{
			throw new System.NotImplementedException();
		}
		#endregion
	}
}
