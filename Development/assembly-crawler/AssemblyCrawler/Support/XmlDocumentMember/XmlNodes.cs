// XmlNodes.cs
// Copyright (c) 2022 Kristopher L. Culin See LICENSE for details

using System.Collections.Generic;
using System.Xml.Serialization;

namespace AssemblyCrawler.Support.XmlDocumentMember
{
	#region Xml Nodes
	[XmlRoot(ElementName = "assembly")]
	public class Assembly
	{

		[XmlElement(ElementName = "name")]
		public string Name { get; set; }
	}

	[XmlRoot(ElementName = "member")]
	public class Member
	{

		[XmlElement(ElementName = "summary")]
		public Summary Summary { get; set; }

		[XmlAttribute(AttributeName = "name")]
		public string Name { get; set; }

		[XmlText]
		public string Text { get; set; }

		[XmlElement(ElementName = "param")]
		public List<Param> Param { get; set; }

		[XmlElement(ElementName = "returns")]
		public Returns Returns { get; set; }

		[XmlElement(ElementName = "exception")]
		public Exception Exception { get; set; }

		[XmlElement(ElementName = "typeparam")]
		public List<Typeparam> Typeparam { get; set; }

		[XmlElement(ElementName = "remarks")]
		public string Remarks { get; set; }
	}

	[XmlRoot(ElementName = "summary")]
	public class Summary
	{
		[XmlText]
		public string Content { get; set; }

		[XmlElement(ElementName = "para")]
		public List<string> Para { get; set; }
	}

	[XmlRoot(ElementName = "returns")]
	public class Returns
	{
		[XmlText]
		public string Content { get; set; }

		[XmlElement(ElementName = "typeparamref")]
		public List<Typeparam> TypeParamRef { get; set; }
	}

	[XmlRoot(ElementName = "param")]
	public class Param
	{

		[XmlAttribute(AttributeName = "name")]
		public string Name { get; set; }

		[XmlText]
		public string Text { get; set; }
	}

	[XmlRoot(ElementName = "exception")]
	public class Exception
	{

		[XmlAttribute(AttributeName = "cref")]
		public string Cref { get; set; }

		[XmlText]
		public string Text { get; set; }
	}

	[XmlRoot(ElementName = "typeparam")]
	public class Typeparam
	{

		[XmlAttribute(AttributeName = "name")]
		public string Name { get; set; }
	}

	[XmlRoot(ElementName = "members")]
	public class Members
	{

		[XmlElement(ElementName = "member")]
		public List<Member> Member { get; set; }
	}

	[XmlRoot(ElementName = "doc")]
	public class Doc
	{

		[XmlElement(ElementName = "assembly")]
		public Assembly Assembly { get; set; }

		[XmlElement(ElementName = "members")]
		public Members Members { get; set; }
	}


	#endregion
}
