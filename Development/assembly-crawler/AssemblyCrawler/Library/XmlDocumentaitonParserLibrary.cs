// XmlDocumentaitonParserLibrary.cs
// Copyright (c) 2022 Kristopher L. Culin See LICENSE for details

using System.Collections.Generic;
using System.IO;
using System.Reflection;
using System.Xml.Serialization;
using AssemblyCrawler.Extensions;
using AssemblyCrawler.Support.XmlDocumentMember;

namespace AssemblyCrawler.Library
{
	public class XmlDocumentaitonParserLibrary
	{
		#region Constructor
		public XmlDocumentaitonParserLibrary(string xmlFilePath)
		{
			XmlFilePath = xmlFilePath;
		}
		#endregion

		#region Public Methods
		public XmlDocumentaitonParserLibrary Parse()
		{
			if (!File.Exists(XmlFilePath))
				return null;

			XmlSerializer serializer = new XmlSerializer(typeof(Doc));
			using (StringReader reader = new StringReader(File.ReadAllText(XmlFilePath)))
			{
				Doc = (Doc)serializer.Deserialize(reader);
			}

			// Build the dictionary of members
			if (Doc != null)
			{
				foreach (var memeber in Doc.Members.Member)
				{
					MembersMap.Add(memeber.Name, memeber);
				}
			}


			return this;
		}
		public Member GetMember(MemberInfo memberInfo)
		{
			Member member;
			MembersMap.TryGetValue(memberInfo.XmlMemberName(), out member);

			return member;
		}
		#endregion

		#region Public Properties
		public Dictionary<string, Member> MembersMap { get; } = new Dictionary<string, Member>();
		#endregion


		#region Private Properties
		private string XmlFilePath { get; }
		private Doc Doc { get; set; }
		#endregion
	}



}
