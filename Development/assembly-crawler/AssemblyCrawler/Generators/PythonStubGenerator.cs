// AssemblyStubGenerator.cs
// Copyright (c) 2021 Kristopher L. Culin See LICENSE for details

using System;
using System.Collections.Generic;
using System.IO;
using AssemblyCrawler.Library;

namespace AssemblyCrawler.Generators
{
    internal class PythonStubGenerator : IStubGenerator
    {
        #region Constructor
        public PythonStubGenerator(StreamWriter writer)
        {
            Writer = writer;
        }
        #endregion

        #region Public Methods
        public void GenerateTypeStub(Type type)
        {
            var typeParser = new TypeParserLibrary(type).Parse();

            // TODO: Find out how reflection can give generics
            // Write Generics
            if (typeParser.IsGenericType)
            {
                Writer.WriteLine();
                Writer.WriteLine();
                PythonStubWriterLibrary.WritePythonGenericVariables(
                    writer: Writer,
                    typeName: "TNameType",
                    type: typeof(string)
                    );
            }


            // Write class
            PythonStubWriterLibrary.WritePythonClassDefinition(
                writer: Writer,
                classType: type,
                inheritedTypes: typeParser.NonGenericInterfaces,
                docString: PythonStubWriterLibrary.BlankDocString,
                isGenericType: typeParser.IsGenericType
                );


            // Write Constructor
            if (typeParser.IsInterface)
                PythonStubWriterLibrary.WritePytonConstructorUnsupported(Writer);


            #region Methods
            // TODO overloaded methods
            foreach (var m in typeParser.OverloadedMethods)
            {
                PythonStubWriterLibrary.WritePythonMethod(
                    writer: Writer,
                    methodName: typeParser.Name,
                    arguments: typeParser.GetMethodArguments(m),
                    returnType: m.ReturnType,
                    docString: new PythonMethodDocStringWriterLibrary(methodInfo: m, description: "Method Description", indentLevel: 3).ToString(),
                    isStatic: m.IsStatic,
                    exception: String.Empty,
                    isOverloaded: true,
                    indentLevel: 1
                    );
            }

            foreach (var m in typeParser.SimpleMethods)
            {
                PythonStubWriterLibrary.WritePythonMethod(
                    writer: Writer,
                    methodName: m.Name,
                    arguments: typeParser.GetMethodArguments(m),
                    returnType: m.ReturnType,
                    docString: new PythonMethodDocStringWriterLibrary(methodInfo: m, description: "Method Description").ToString(),
                    isStatic: m.IsStatic,
                    exception: String.Empty,
                    isOverloaded: false,
                    indentLevel: 1
                    );
            }
            #endregion


            #region Properties
            // Write ReadOnly properties
            foreach (var p in typeParser.ReadOnlyProperties)
                PythonStubWriterLibrary.WritePythonProperty(
                    writer: Writer,
                    propertyName: typeParser.GetPropertyName(p),
                    returnType: p.ReturnType,
                    docString: new PythonPropertyDocStringWriterLibrary(p.ReturnType, "No Description").ToString(),
                    isStatic: p.IsStatic,
                    indentLevel: 1
                    );

            // Write WriteOnly properties
            foreach (var p in typeParser.WriteOnlyProperties)
                PythonStubWriterLibrary.WritePythonPropertySetter(
                    writer: Writer,
                    propertyName: typeParser.GetPropertyName(p),
                    returnType: p.GetParameters()[0].ParameterType,
                    isStatic: p.IsStatic,
                    indentLevel: 1
                    );

            //// Write Static ReadOnly properties
            //foreach (var p in typeParser.StaticReadOnlyProperties)
            //    PythonStubWriterLibrary.WritePythonProperty(
            //        writer: Writer,
            //        propertyName: typeParser.GetPropertyName(p),
            //        returnType: p.ReturnType,
            //        docString: new PythonPropertyDocStringWriterLibrary(p.ReturnType, "No Description").ToString(),
            //        isStatic: true
            //        );

            //// Write Static WriteOnly properties
            //foreach (var p in typeParser.StaticWriteOnlyProperties)
            //    PythonStubWriterLibrary.WritePythonPropertySetter(
            //        writer: Writer,
            //        propertyName: typeParser.GetPropertyName(p),
            //        returnType: p.GetParameters()[0].ParameterType,
            //        isStatic: true
            //        );

            #endregion
        }
        #endregion

        #region Private Properties
        private StreamWriter Writer { get; }
        #endregion
    }
}
