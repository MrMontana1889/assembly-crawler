// PythonStubGenerator.cs
// Copyright (c) 2021 Kristopher L. Culin See LICENSE for details

using System;
using System.Linq;
using System.Reflection;
using AssemblyCrawler.Extensions;
using AssemblyCrawler.Library;
using AssemblyCrawler.Support;

namespace AssemblyCrawler.Generators
{
    internal class PythonStubGenerator : IStubGenerator
    {
        #region Constants
        const string DefAddition = "__add__";
        const string DefSubtraction = "__sub__";
        const string DefMultiplication = "__mul__";
        const string DefDivision = "__truediv__";
        const string DefModulo = "__mod__";
        const string DefEquality = "__eq__";
        const string DefInEquality = "__ne__";
        const string DefGreaterThan = "__gt__";
        const string DefLessThan = "__lt__";
        const string DefGreaterOrEqualTo = "__ge__";
        const string DefLessOrEqualTo = "__le__";
        const string DefBitwiseAnd = "__and__";
        const string DefBitwisOr = "__or__";
        const string DefBitwiseXor = "__xor__";

        const string DocStringSummaryAddition = "Mathematical operation of Addition";
        const string DocStringSummarySubtraction = "Mathematical operation of Subtraction";
        const string DocStringSummaryMultiplication = "Mathematical operation of Multiplication";
        const string DocStringSummaryDivision = "Mathematical operation of Division";
        const string DocStringSummaryModulo = "Mathematical operation of Modulo";
        const string DocStringSummaryEquality = "Mathematical operation of Equality";
        const string DocStringSummaryInEquality = "Mathematical operation of InEquality";
        const string DocStringSummaryGreaterThan = "Mathematical operation of GreaterThan";
        const string DocStringSummaryLessThan = "Mathematical operation of LessThan";
        const string DocStringSummaryGreaterOrEqualTo = "Mathematical operation of GreaterOrEqual";
        const string DocStringSummaryLessOrEqualTo = "Mathematical operation of LessOrEqual";
        const string DocStringSummaryBitwiseAnd = "Mathematical operation of BitwiseAnd";
        const string DocStringSummaryBitwisOr = "Mathematical operation of BitwisOr";
        const string DocStringSummaryBitwiseXor = "Mathematical operation of BitwiseXor";
        #endregion

        #region Constructor
        public PythonStubGenerator(PythonModuleDefinition module)
        {
            Module = module;
        }
        #endregion

        #region Public Methods
        public void GenerateTypeStub(Type type, string xmlDocumentFileName)
        {
            if (type == null)
                throw new ArgumentNullException(nameof(type));

            var typeParser = new TypeParserLibrary(type).Parse();
            var xmlDocument = new XmlDocumentaitonParserLibrary(xmlDocumentFileName).Parse();

            string typeName = type.Name;

            if (type == typeof(Enum))
            {
                Console.WriteLine($"Create Enum: {typeParser.Type.Name}");
            }
            else
            {
                var classDocStringWriter = new PythonClassDocStringWriterLibrary(
                            member: xmlDocument?.GetMember(type as MemberInfo),
                            indentLevel: 0);


                PythonStubWriterLibrary.WritePythonClassDef(
                    Module,
                    type,
                    classDocStringWriter.ToString(),
                    0);

                #region Constructor

                PythonClassDefinition classDef = Module.GetClassDefinition(type.AssemblyQualifiedName, type.Name);

                // Write Constructor
                if (typeParser.IsInterface || typeParser.Type.IsAbstract)
                {
                    PythonStubWriterLibrary.WritePythonConstructorUnsupported(classDef);
                }

                else if (typeParser.Type.IsClass)
                {
                    // TODO: Debugger never hit this locaiton.
                    var args = typeParser.GetConstructorArguments();
                    var memberInfo = type.GetConstructor(new Type[] { });

                    var docStringWriter = new PythonConstructorDocStringWriterLibrary(
                            member: xmlDocument?.GetMember(memberInfo),
                            arguments: args,
                            indentLevel: 2);

                    PythonStubWriterLibrary.WritePythonConstructor(
                        classDef: classDef,
                        arguments: args,
                        docString: docStringWriter?.ToString(),
                        indentLevel: 1);
                }
                #endregion

                #region Methods
                // Overloaded methods
                foreach (var m in typeParser.OverloadedMethods)
                {
                    Module.AddImportModule("typing").AddType("overload");

                    PythonStubWriterLibrary.WritePythonMethod(
                        classDef: classDef,
                        methodName: typeParser.Name,
                        arguments: typeParser.GetMethodArguments(m),
                        returnType: m.ReturnType,
                        docString: NewPythonmethodDocStringWriterLibrary(xmlDocument, m)?.ToString(),
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
                        classDef: classDef,
                        methodName: m.Name,
                        arguments: typeParser.GetMethodArguments(m),
                        returnType: m.ReturnType,
                        docString: NewPythonmethodDocStringWriterLibrary(xmlDocument, m)?.ToString(),
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
                        classDef: classDef,
                        methodName: DefAddition,
                        arguments: typeParser.GetMethodArguments(m),
                        returnType: m.ReturnType,
                        docString: NewPythonmethodDocStringWriterLibrary(xmlDocument, m)?.ToString(),
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
                        classDef: classDef,
                        methodName: DefSubtraction,
                        arguments: typeParser.GetMethodArguments(m),
                        returnType: m.ReturnType,
                        docString: NewPythonmethodDocStringWriterLibrary(xmlDocument, m)?.ToString(),
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
                        classDef: classDef,
                        methodName: DefMultiplication,
                        arguments: typeParser.GetMethodArguments(m),
                        returnType: m.ReturnType,
                        docString: NewPythonmethodDocStringWriterLibrary(xmlDocument, m)?.ToString(),
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
                        classDef: classDef,
                        methodName: DefDivision,
                        arguments: typeParser.GetMethodArguments(m),
                        returnType: m.ReturnType,
                        docString: NewPythonmethodDocStringWriterLibrary(xmlDocument, m)?.ToString(),
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
                        classDef: classDef,
                        methodName: DefModulo,
                        arguments: typeParser.GetMethodArguments(m),
                        returnType: m.ReturnType,
                        docString: NewPythonmethodDocStringWriterLibrary(xmlDocument, m)?.ToString(),
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
                        classDef: classDef,
                        methodName: DefEquality,
                        arguments: typeParser.GetMethodArguments(m),
                        returnType: m.ReturnType,
                        docString: NewPythonmethodDocStringWriterLibrary(xmlDocument, m)?.ToString(),
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
                        classDef: classDef,
                        methodName: DefInEquality,
                        arguments: typeParser.GetMethodArguments(m),
                        returnType: m.ReturnType,
                        docString: NewPythonmethodDocStringWriterLibrary(xmlDocument, m)?.ToString(),
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
                        classDef: classDef,
                        methodName: DefGreaterThan,
                        arguments: typeParser.GetMethodArguments(m),
                        returnType: m.ReturnType,
                        docString: NewPythonmethodDocStringWriterLibrary(xmlDocument, m)?.ToString(),
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
                        classDef: classDef,
                        methodName: DefLessThan,
                        arguments: typeParser.GetMethodArguments(m),
                        returnType: m.ReturnType,
                        docString: NewPythonmethodDocStringWriterLibrary(xmlDocument, m)?.ToString(),
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
                        classDef: classDef,
                        methodName: DefGreaterOrEqualTo,
                        arguments: typeParser.GetMethodArguments(m),
                        returnType: m.ReturnType,
                        docString: NewPythonmethodDocStringWriterLibrary(xmlDocument, m)?.ToString(),
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
                        classDef: classDef,
                        methodName: DefLessOrEqualTo,
                        arguments: typeParser.GetMethodArguments(m),
                        returnType: m.ReturnType,
                        docString: NewPythonmethodDocStringWriterLibrary(xmlDocument, m)?.ToString(),
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
                        classDef: classDef,
                        methodName: DefBitwiseAnd,
                        arguments: typeParser.GetMethodArguments(m),
                        returnType: m.ReturnType,
                        docString: NewPythonmethodDocStringWriterLibrary(xmlDocument, m)?.ToString(),
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
                        classDef: classDef,
                        methodName: DefBitwisOr,
                        arguments: typeParser.GetMethodArguments(m),
                        returnType: m.ReturnType,
                        docString: NewPythonmethodDocStringWriterLibrary(xmlDocument, m)?.ToString(),
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
                        classDef: classDef,
                        methodName: DefBitwiseXor,
                        arguments: typeParser.GetMethodArguments(m),
                        returnType: m.ReturnType,
                        docString: NewPythonmethodDocStringWriterLibrary(xmlDocument, m)?.ToString(),
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
                {
                    var docStringWriter = new PythonPropertyDocStringWriterLibrary(
                        type: type,
                        member: xmlDocument?.GetMember(p as MethodInfo),
                        indentLevel: 2);

                    PythonStubWriterLibrary.WritePythonProperty(
                            classDef: classDef,
                            propertyName: typeParser.GetPropertyName(p),
                            returnType: p.ReturnType,
                            docString: docStringWriter?.ToString(),
                            isStatic: p.IsStatic,
                            indentLevel: 1
                            );
                }

                // Write WriteOnly properties
                foreach (var p in typeParser.WriteOnlyProperties)
                {
                    PythonStubWriterLibrary.WritePythonPropertySetter(
                        classDef: classDef,
                        propertyName: typeParser.GetPropertyName(p),
                        returnType: p.GetParameters()[0].ParameterType,
                        isStatic: p.IsStatic,
                        indentLevel: 1
                        );
                }

                #endregion
            }
        }
        #endregion

        #region Private Methods
        private PythonMethodDocStringWriterLibrary NewPythonmethodDocStringWriterLibrary(XmlDocumentaitonParserLibrary xmlDocument, MethodInfo m)
        {
            return new PythonMethodDocStringWriterLibrary(
                    methodInfo: m,
                    member: xmlDocument?.GetMember(m),
                    indentLevel: 2);
        }


        #endregion

        #region Private Properties
        private PythonModuleDefinition Module { get; }
        #endregion
    }
}
