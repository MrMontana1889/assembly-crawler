// ElementManagerBase.cs
// Copyright (c) 2021 Kristopher L. Culin See LICENSE for details

using System.Collections.Generic;
using System.Linq;

namespace TestAssemblyNET48.Water
{
	public abstract class ElementManagerBase<TElementType> : IElementManager<TElementType>
		where TElementType : class, IElement
	{
		#region Constructor
		public ElementManagerBase()
		{

		}
		#endregion

		#region Public Methods
		public List<int> ElementIDs()
		{
			if (Count == 0) return new List<int>();

			return new List<int>(ElementList.Select(e => e.Id));
		}
		public bool Exists(int id)
		{
			if (Count == 0) return false;

			foreach (TElementType element in ElementList)
				if (element.Id == id) return true;

			return false;
		}

		public TElementType Create()
		{
			ElementList.Add(NewElement());
			return ElementList.Last();
		}
		public TElementType Element(int id)
		{
			if (Count == 0) return default;

			return ElementList.Find(e => e.Id == id);
		}

		public TElementType Element(string label)
		{
			if (Count == 0) return default;

			return ElementList.Find(e => e.Label == label);
		}

		public List<TElementType> Elements()
		{
			return ElementList;
		}
		public void Delete(int id)
		{
			if (Count == 0) return;

			var element = Element(id);
			if (element != null)
				ElementList.Remove(element);
		}
		#endregion

		#region Public Properties
		public int Count => ElementList.Count;
		#endregion

		#region Protected Methods
		protected abstract TElementType NewElement();
		#endregion

		#region Protected Properties
		protected List<TElementType> ElementList { get; } = new List<TElementType>();
		#endregion

	}
}
