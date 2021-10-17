// TestEntry.cs
// Copyright (c) 2021 Kristopher L. Culin See LICENSE for details

using System.Collections.Generic;
using System.Drawing;
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

		public static IPipes GetPipes(List<int> Ids)
        {
			return new Pipes();
        }

		// TODO: Need to support nested Types

		/// <summary>
		/// This is a nested class, parent is TestEntry
		/// </summary>
		public class NestedClass
		{
			public static Size Size => new Size(100, 100);
		}
	}

	/// <summary>
	/// An example class with multiple constructor
	/// </summary>
	public class MultiCtorClass
    {
		public static string STATIC_STRING = "STATIC_STRING";

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
        /// <param name="label">Default value is Default</param>
        public MultiCtorClass(int id, string label ="Default"):base()
        {
			Id = id;
			Label = label;
        }

        public MultiCtorClass(Numbers numbers):base()
        {
			Numbers = numbers;
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
        /// <param name="one"></param>
        /// <returns>True/False</returns>
        public bool Contains(string label, out int id, string one = "one")
        {
			id = 1;
			return string.IsNullOrEmpty(label);
        }

		public Numbers Numbers { get; }
    }

	/// <summary>
	/// Enum of numbers
	/// </summary>
	public enum Numbers
    {
		Zero=0,
		/// <summary>
		/// One 1
		/// </summary>
		One=1,
		Two=2
    }
}
