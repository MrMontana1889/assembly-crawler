// TestEntry.cs
// Copyright (c) 2021 Kristopher L. Culin See LICENSE for details

using Test.TestGenericAssembly;
using Test.TestGenericAssembly.Links;

namespace TestGenericAssembly
{
	public static class TestEntry
	{
		/// <summary>
		/// A static method to get an Element
		/// </summary>
		/// <returns></returns>		
		public static IElement GetElement()
		{
			return new Pipe();
		}

		public static IPipes GetPipes()
		{
			return new Pipes();
		}

		/// <summary>
		/// This is a nested class, parent is TestEntry
		/// </summary>
		public class NestedClass
		{

		}
	}

	/// <summary>
	/// An example class with multiple constructor
	/// </summary>
	public class MultiCtorClass
    {
		/// <summary>
		/// Constructor with no parameters
		/// </summary>
        public MultiCtorClass()
        {
        }

		/// <summary>
		/// You will need <paramref name="id"/> to create an instance
		/// </summary>
		/// <param name="id">Id of the element</param>
        public MultiCtorClass(int id):base()
        {
			Id = id;
        }

		/// <summary>
		/// You will need <paramref name="label"/> to create an instance
		/// </summary>
		/// <param name="label">Label of the element</param>
		public MultiCtorClass(string label):base()
        {
			Label = label;
        }

		/// <summary>
		/// A read-only field for Id
		/// </summary>
		public int Id { get; }

		/// <summary>
		/// Read/Write Property
		/// </summary>
		public string Label { get; set; }

		/// <summary>
		/// Method with out parameter
		/// </summary>
		/// <param name="label">Input label</param>
		/// <param name="id">This Id will be inizalied</param>
		/// <returns>True/False</returns>
		public bool Contains(string label, out int id)
        {
			id = 1;
			return string.IsNullOrEmpty(label);
        }
    }
}
