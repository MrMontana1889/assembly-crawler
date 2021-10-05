// LoadAssemblyTestFixture.cs
// Copyright (c) 2021 Kristopher L. Culin See LICENSE for details

using System.IO;
using System.Reflection;
using System.Xml.Serialization;
using AssemblyCrawler.Support.XmlDocumentMember;
using NUnit.Framework;
using TestAssemblyNET48.Water;

namespace AssemblyCrawler.Test
{
    public class XmlDocumentParseTestFixture
    {
        #region Setup/Teardown
        [SetUp]
        public void Setup()
        {
            XmlFilePath = Path.Combine(TestContext.CurrentContext.TestDirectory + "/..", "TestGenericAssembly.xml");
        }
        #endregion

        #region Tests
        [Test]
        public void TestLoadXmlDocument()
        {
            Assert.True(File.Exists(XmlFilePath));

            // load xml content
            var serializer = new XmlSerializer(typeof(Doc));
            using (StringReader reader = new StringReader(File.ReadAllText(XmlFilePath)))
            {
                Doc = (Doc)serializer.Deserialize(reader);
            }

            Assert.NotNull(Doc);

            Assert.Equals(Doc.Assembly.Name, "OpenFlows.Water");
            Assert.Equals(Doc.Members.Member.Count, 3);
        }


        #endregion

        #region Private Properties
        private Doc Doc { get; set; }
        private string XmlFilePath { get; set; }
        #endregion
    }
}
