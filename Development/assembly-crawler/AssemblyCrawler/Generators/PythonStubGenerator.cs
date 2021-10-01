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
        #region Constants
        string DefAddition = "__add__";
        string DefSubtraction = "__sub__";
        string DefMultiplication = "__mul__";
        string DefDivision = "__truediv__";
        string DefModulo = "__mod__";
        string DefEquality = "__eq__";
        string DefInEquality = "__ne__";
        string DefGreaterThan = "__gt__";
        string DefLessThan = "__lt__";
        string DefGreaterOrEqualTo = "__ge__";
        string DefLessOrEqualTo = "__le__";
        string DefBitwiseAnd = "__and__";
        string DefBitwisOr = "__or__";
        string DefBitwiseXor = "__xor__";

        string DocStringSummaryAddition = "Mathematical operation of Addition";
        string DocStringSummarySubtraction = "Mathematical operation of Subtraction";
        string DocStringSummaryMultiplication = "Mathematical operation of Multiplication";
        string DocStringSummaryDivision = "Mathematical operation of Division";
        string DocStringSummaryModulo = "Mathematical operation of Modulo";
        string DocStringSummaryEquality = "Mathematical operation of Equality";
        string DocStringSummaryInEquality = "Mathematical operation of InEquality";
        string DocStringSummaryGreaterThan = "Mathematical operation of GreaterThan";
        string DocStringSummaryLessThan = "Mathematical operation of LessThan";
        string DocStringSummaryGreaterOrEqualTo = "Mathematical operation of GreaterOrEqual";
        string DocStringSummaryLessOrEqualTo = "Mathematical operation of LessOrEqual";
        string DocStringSummaryBitwiseAnd = "Mathematical operation of BitwiseAnd";
        string DocStringSummaryBitwisOr = "Mathematical operation of BitwisOr";
        string DocStringSummaryBitwiseXor = "Mathematical operation of BitwiseXor";
        #endregion

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
                docString: new PythonClassDocStringWriterLibrary("Class Description").ToString(),
                isGenericType: typeParser.IsGenericType
                );

            #region Constructor
            // Write Constructor
            if (typeParser.IsInterface || typeParser.Type.IsAbstract)
                PythonStubWriterLibrary.WritePythonConstructorUnsupported(Writer);

            else if (typeParser.Type.IsClass)
            {
                var args = typeParser.GetConstructorArguments();
                PythonStubWriterLibrary.WritePythonConstructor(
                    writer: Writer,
                    arguments: args,
                    docString: new PythonConstructorDocStringWriterLibrary(
                        description: "Constructor Description",
                        arguments: args,
                        indentLevel: 2).ToString(),
                    indentLevel: 1);
            }
            #endregion


            #region Methods
            // Overloaded methods
            foreach (var m in typeParser.OverloadedMethods)
            {
                PythonStubWriterLibrary.WritePythonMethod(
                    writer: Writer,
                    methodName: typeParser.Name,
                    arguments: typeParser.GetMethodArguments(m),
                    returnType: m.ReturnType,
                    docString: new PythonMethodDocStringWriterLibrary(
                        methodInfo: m,
                        description: "Method Description",
                        indentLevel: 2).ToString(),
                    isStatic: m.IsStatic,
                    exception: String.Empty,
                    isOverloaded: true,
                    indentLevel: 1
                    );
            }

            // Simple (non-overloaded) methods
            foreach (var m in typeParser.SimpleMethods)
            {
                PythonStubWriterLibrary.WritePythonMethod(
                    writer: Writer,
                    methodName: m.Name,
                    arguments: typeParser.GetMethodArguments(m),
                    returnType: m.ReturnType,
                    docString: new PythonMethodDocStringWriterLibrary(
                        methodInfo: m,
                        description: "Method Description").ToString(),
                    isStatic: m.IsStatic,
                    exception: String.Empty,
                    isOverloaded: false,
                    indentLevel: 1
                    );
            }

            // Operators +
            foreach (var m in typeParser.OperatorAddition)
            {
                PythonStubWriterLibrary.WritePythonMethod(
                    writer: Writer,
                    methodName: DefAddition,
                    arguments: typeParser.GetMethodArguments(m),
                    returnType: m.ReturnType,
                    docString: new PythonMethodDocStringWriterLibrary(
                        methodInfo: m,
                        description: DocStringSummaryAddition).ToString(),
                    isStatic: m.IsStatic,
                    exception: String.Empty,
                    isOverloaded: false,
                    indentLevel: 1
                    );
            }
            // Operators -
            foreach (var m in typeParser.OperatorSubtraction)
            {
                PythonStubWriterLibrary.WritePythonMethod(
                    writer: Writer,
                    methodName: DefSubtraction,
                    arguments: typeParser.GetMethodArguments(m),
                    returnType: m.ReturnType,
                    docString: new PythonMethodDocStringWriterLibrary(
                        methodInfo: m,
                        description: DocStringSummarySubtraction).ToString(),
                    isStatic: m.IsStatic,
                    exception: String.Empty,
                    isOverloaded: false,
                    indentLevel: 1
                    );
            }
            // Operators *
            foreach (var m in typeParser.OperatorMultiplication)
            {
                PythonStubWriterLibrary.WritePythonMethod(
                    writer: Writer,
                    methodName: DefMultiplication,
                    arguments: typeParser.GetMethodArguments(m),
                    returnType: m.ReturnType,
                    docString: new PythonMethodDocStringWriterLibrary(
                        methodInfo: m,
                        description: DocStringSummaryMultiplication).ToString(),
                    isStatic: m.IsStatic,
                    exception: String.Empty,
                    isOverloaded: false,
                    indentLevel: 1
                    );
            }
            // Operators /
            foreach (var m in typeParser.OperatorDivision)
            {
                PythonStubWriterLibrary.WritePythonMethod(
                    writer: Writer,
                    methodName: DefDivision,
                    arguments: typeParser.GetMethodArguments(m),
                    returnType: m.ReturnType,
                    docString: new PythonMethodDocStringWriterLibrary(
                        methodInfo: m,
                        description: DocStringSummaryDivision).ToString(),
                    isStatic: m.IsStatic,
                    exception: String.Empty,
                    isOverloaded: false,
                    indentLevel: 1
                    );
            }
            // Operators %
            foreach (var m in typeParser.OperatorModulo)
            {
                PythonStubWriterLibrary.WritePythonMethod(
                    writer: Writer,
                    methodName: DefModulo,
                    arguments: typeParser.GetMethodArguments(m),
                    returnType: m.ReturnType,
                    docString: new PythonMethodDocStringWriterLibrary(
                        methodInfo: m,
                        description: DocStringSummaryModulo).ToString(),
                    isStatic: m.IsStatic,
                    exception: String.Empty,
                    isOverloaded: false,
                    indentLevel: 1
                    );
            }
            // Operators ==
            foreach (var m in typeParser.OperatorEquality)
            {
                PythonStubWriterLibrary.WritePythonMethod(
                    writer: Writer,
                    methodName: DefEquality,
                    arguments: typeParser.GetMethodArguments(m),
                    returnType: m.ReturnType,
                    docString: new PythonMethodDocStringWriterLibrary(
                        methodInfo: m,
                        description: DocStringSummaryEquality).ToString(),
                    isStatic: m.IsStatic,
                    exception: String.Empty,
                    isOverloaded: false,
                    indentLevel: 1
                    );
            }
            // Operators !=
            foreach (var m in typeParser.OperatorInequality)
            {
                PythonStubWriterLibrary.WritePythonMethod(
                    writer: Writer,
                    methodName: DefInEquality,
                    arguments: typeParser.GetMethodArguments(m),
                    returnType: m.ReturnType,
                    docString: new PythonMethodDocStringWriterLibrary(
                        methodInfo: m,
                        description: DocStringSummaryInEquality).ToString(),
                    isStatic: m.IsStatic,
                    exception: String.Empty,
                    isOverloaded: false,
                    indentLevel: 1
                    );
            }
            // Operators >
            foreach (var m in typeParser.OperatorGreaterThan)
            {
                PythonStubWriterLibrary.WritePythonMethod(
                    writer: Writer,
                    methodName: DefGreaterThan,
                    arguments: typeParser.GetMethodArguments(m),
                    returnType: m.ReturnType,
                    docString: new PythonMethodDocStringWriterLibrary(
                        methodInfo: m,
                        description: DocStringSummaryGreaterThan).ToString(),
                    isStatic: m.IsStatic,
                    exception: String.Empty,
                    isOverloaded: false,
                    indentLevel: 1
                    );
            }
            // Operators <
            foreach (var m in typeParser.OperatorLessThan)
            {
                PythonStubWriterLibrary.WritePythonMethod(
                    writer: Writer,
                    methodName: DefLessThan,
                    arguments: typeParser.GetMethodArguments(m),
                    returnType: m.ReturnType,
                    docString: new PythonMethodDocStringWriterLibrary(
                        methodInfo: m,
                        description: DocStringSummaryLessThan).ToString(),
                    isStatic: m.IsStatic,
                    exception: String.Empty,
                    isOverloaded: false,
                    indentLevel: 1
                    );
            }
            // Operators >=
            foreach (var m in typeParser.OperatorGreaterOrEqualTo)
            {
                PythonStubWriterLibrary.WritePythonMethod(
                    writer: Writer,
                    methodName: DefGreaterOrEqualTo,
                    arguments: typeParser.GetMethodArguments(m),
                    returnType: m.ReturnType,
                    docString: new PythonMethodDocStringWriterLibrary(
                        methodInfo: m,
                        description: DocStringSummaryGreaterOrEqualTo).ToString(),
                    isStatic: m.IsStatic,
                    exception: String.Empty,
                    isOverloaded: false,
                    indentLevel: 1
                    );
            }
            // Operators <=
            foreach (var m in typeParser.OperatorLessOrEqualTo)
            {
                PythonStubWriterLibrary.WritePythonMethod(
                    writer: Writer,
                    methodName: DefLessOrEqualTo,
                    arguments: typeParser.GetMethodArguments(m),
                    returnType: m.ReturnType,
                    docString: new PythonMethodDocStringWriterLibrary(
                        methodInfo: m,
                        description: DocStringSummaryLessOrEqualTo).ToString(),
                    isStatic: m.IsStatic,
                    exception: String.Empty,
                    isOverloaded: false,
                    indentLevel: 1
                    );
            }
            // Operators &
            foreach (var m in typeParser.OperatorBitwiseAnd)
            {
                PythonStubWriterLibrary.WritePythonMethod(
                    writer: Writer,
                    methodName: DefBitwiseAnd,
                    arguments: typeParser.GetMethodArguments(m),
                    returnType: m.ReturnType,
                    docString: new PythonMethodDocStringWriterLibrary(
                        methodInfo: m,
                        description: DocStringSummaryBitwiseAnd).ToString(),
                    isStatic: m.IsStatic,
                    exception: String.Empty,
                    isOverloaded: false,
                    indentLevel: 1
                    );
            }
            // Operators |
            foreach (var m in typeParser.OperatorBitwiseOr)
            {
                PythonStubWriterLibrary.WritePythonMethod(
                    writer: Writer,
                    methodName: DefBitwisOr,
                    arguments: typeParser.GetMethodArguments(m),
                    returnType: m.ReturnType,
                    docString: new PythonMethodDocStringWriterLibrary(
                        methodInfo: m,
                        description: DocStringSummaryBitwisOr).ToString(),
                    isStatic: m.IsStatic,
                    exception: String.Empty,
                    isOverloaded: false,
                    indentLevel: 1
                    );
            }
            // Operators ^
            foreach (var m in typeParser.OperatorBitwiseXor)
            {
                PythonStubWriterLibrary.WritePythonMethod(
                    writer: Writer,
                    methodName: DefBitwiseXor,
                    arguments: typeParser.GetMethodArguments(m),
                    returnType: m.ReturnType,
                    docString: new PythonMethodDocStringWriterLibrary(
                        methodInfo: m,
                        description: DocStringSummaryBitwiseXor).ToString(),
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
                    docString: new PythonPropertyDocStringWriterLibrary(
                        type: p.ReturnType,
                        description: "No Description").ToString(),
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

            #endregion
        }
        #endregion

        #region Private Properties
        private StreamWriter Writer { get; }
        #endregion
    }
}
