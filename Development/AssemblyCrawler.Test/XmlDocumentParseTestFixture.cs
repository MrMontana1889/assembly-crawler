// LoadAssemblyTestFixture.cs
// Copyright (c) 2021 Kristopher L. Culin See LICENSE for details

using System.IO;
using System.Reflection;
using System.Xml.Serialization;
using AssemblyCrawler.Support.XmlDocumentMember;
using NUnit.Framework;
using AssemblyCrawler.Support;
using Test.TestGenericAssembly;
using AssemblyCrawler.Generators;
using AssemblyCrawler.Library;
using AssemblyCrawler.Extensions;
using TestGenericAssembly;
using System.Linq;
using System;

namespace AssemblyCrawler.Test
{
    public class XmlDocumentParseTestFixture
    {
        #region Setup/Teardown
        [SetUp]
        public void Setup()
        {
            var testXmlFilePath = Path.Combine(TestContext.CurrentContext.TestDirectory + @"\..\..\..\..\..", "TestGenericAssembly", "Test.TestGenericAssembly.xml");
            testXmlFilePath = Path.GetFullPath(testXmlFilePath);

            Assert.IsTrue(File.Exists(testXmlFilePath));
            XmlDocumentParserLib = new XmlDocumentaitonParserLibrary(testXmlFilePath).Parse();
        }

        #endregion

        #region Tests
        [Test]
        public void TestTypeParser()
        {
            var testIElementManagerType = typeof(IElementManager);
            var typeParser = new TypeParserLibrary(testIElementManagerType).Parse();
            Assert.IsNotNull(typeParser);

            Assert.IsTrue(typeParser.IsInterface);
            Assert.IsTrue(typeParser.GenericInterfaces.Count == 0);
            Assert.IsTrue(typeParser.NonGenericInterfaces.Count == 0);
            Assert.IsTrue(typeParser.AllMethods.Count == 3);
            Assert.IsTrue(typeParser.MemberInfoMap.Count == 4);
            Assert.IsTrue(typeParser.ReadOnlyProperties.Count == 1);
            Assert.IsTrue(typeParser.SimpleMethods.Count == 2);
            Assert.IsTrue(typeParser.WriteOnlyProperties.Count == 0);
            Assert.IsTrue(typeParser.GetPropertyName(typeParser.ReadOnlyProperties[0]) == "Count");

            // test for static members
            typeParser = new TypeParserLibrary(typeof(TestEntry)).Parse();
            Assert.IsNotNull(typeParser);
            Assert.IsTrue(typeParser.AllMethods.Where(m => m.IsStatic).Count() == 3);
            Assert.IsTrue(typeParser.OverloadedMethods.Count == 2);

            // test for nested Type(class)
            Assert.IsTrue(typeParser.MemberInfoMap.Where(m => (m.Value is Type)).Count() == 1);

            // TODO: Need to test members of nested Types
            // TODO: Need to test operators

            //// TODO: Test on overloaded/non-overloaded constructors
            //// constructor arguments
            typeParser = new TypeParserLibrary(typeof(MultiCtorClass)).Parse();
            Assert.IsTrue(typeParser.StaticFields.Count == 1);
            Assert.IsTrue(typeParser.Constructors.Count == 3);


            // Method Arguments
            var containsMethod = typeParser.AllMethods.Where(m => m.Name == "Contains").FirstOrDefault();
            var methodArgs = typeParser.GetMethodArguments(containsMethod);
            Assert.IsTrue(methodArgs.Count == 3);
            Assert.IsTrue(methodArgs.Where(m => m.Key == "label").Count() == 1);
            Assert.IsTrue(methodArgs.Where(m => m.Key == "id").Count() == 1);
            Assert.IsTrue(methodArgs.Where(m => m.Key == "one").Count() == 1);
        }


        [Test]
        public void TestIElementManager_XmlDocContent()
        {
            var testIElementManagerType = typeof(IElementManager);

            var typeParser = new TypeParserLibrary(testIElementManagerType).Parse();
            Assert.IsNotNull(typeParser);


            Assert.NotNull(XmlDocumentParserLib);
            var iElementManagerMember = XmlDocumentParserLib.GetMember(testIElementManagerType);
            Assert.IsNull(iElementManagerMember);


            // Count
            var countMethod = typeParser.AllMethods.Find(m => m.Name == "get_Count");
            var countMember = XmlDocumentParserLib.GetMember(countMethod);
            Assert.IsNull(countMember);


            // ElementIDs
            var elementIdsMethod = typeParser.AllMethods.Find(m => m.Name == "ElementIDs");
            var elementIdMember = XmlDocumentParserLib.GetMember(elementIdsMethod);
            var elementIdDocString = new PythonPropertyDocStringWriterLibrary(testIElementManagerType, elementIdMember, 2).ToString();

            Assert.IsNotNull(elementIdMember);
            Assert.IsTrue(elementIdsMethod.XmlMemberName() == elementIdMember.Name);
            Assert.IsTrue(elementIdMember.Summary.Content.Trim() == "Get all the IDs");
            Assert.IsTrue(elementIdMember.Returns.Content == "List of element Ids");
            Assert.IsTrue(elementIdDocString == "\t\"\"\"Get all the IDs\r\n\r\n\t\tReturns:\r\n\t\t\tIElementManager: List of element Ids\r\n\t\t\"\"\"");


            // Exists
            var exitsMethod = typeParser.AllMethods.Find(m => m.Name == "Exists");
            var exitsMember = XmlDocumentParserLib.GetMember(exitsMethod);
            var exitsDocString = new PythonMethodDocStringWriterLibrary(exitsMethod, exitsMember, 2).ToString();

            Assert.IsNotNull(exitsMember);
            Assert.IsTrue(exitsMethod.XmlMemberName() == exitsMember.Name);
            Assert.IsTrue(exitsMember.Summary.Content.Trim() == "Evaulates if an id exists");
            Assert.IsTrue(exitsMember.Param.Count == 1);
            Assert.IsTrue(exitsMember.Param[0].Name == "id");
            Assert.IsTrue(exitsMember.Param[0].Text == "The id whose existance has to be checked");
            Assert.IsTrue(exitsMember.Returns.Content == "True if found, otherwise false ");
            // TODO Example

            Assert.IsTrue(exitsDocString == "\t\"\"\"Evaulates if an id exists\r\n\r\n\t\tArgs:\r\n\t\t\tid(int): The id whose existance has to be checked\r\n\r\n\t\tReturns:\r\n\t\t\tbool: True if found, otherwise false \r\n\t\t\"\"\"");

        }

        [Test]
        public void TestTestEntryClass_XmlDocContent()
        {
            var testEntryType = typeof(MultiCtorClass);

            var typeParser = new TypeParserLibrary(testEntryType).Parse();
            Assert.IsNotNull(typeParser);

            // TODO
            var ctorIdLabel = typeParser.Constructors.Find(c => c.GetParameters().Where(p=>p.Name == "id" || p.Name == "label").Any());
            var ctorIdLabelMember = XmlDocumentParserLib.GetMember(ctorIdLabel);
            //var ctroIdLabelDocString = new PythonConstructorDocStringWriterLibrary(ctorIdLabelMember, typeParser.GetConstructorArgements(ctorIdLabel), 2);

            // TODO double check the returned doctring with default value in the arguments

        }
        #endregion

        #region Private Properties
        private Doc Doc { get; set; }
        private XmlDocumentaitonParserLibrary XmlDocumentParserLib { get; set; }
        #endregion
    }
}
