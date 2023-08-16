// PythonMethod.cs
// Copyright (c) 2022 Kristopher L. Culin See LICENSE for details

using System;
using System.Collections.Generic;
using System.IO;
using System.Reflection;
using System.Text;
using AssemblyCrawler.Library;
using static AssemblyCrawler.Library.WriterLibrary;
using static AssemblyCrawler.Support.Constants;

namespace AssemblyCrawler.Support
{
    public class PythonMethod : WriterBase
    {
        #region Constructor
        public PythonMethod(PythonClass pythonClasse, MethodBase method,
            bool isOverloaded = false, string exceptionMessage = null)
            : base(pythonClasse)
        {
            Method = method;
            IsOverloaded = isOverloaded;
            ExceptionMessage = exceptionMessage;
            Initialize();
        }
        #endregion

        #region Public Methods
        public void Update()
        {
            // Need to check the return type and each parameter type
            // along with generic types.
            if (IsMethod)
            {
                // Only process if a method.
                AddReferenceImports(Class.Module, MethodInfo.ReturnType);

                foreach (var parameter in MethodInfo.GetParameters())
                    AddReferenceImports(Class.Module, parameter.ParameterType);
            }
        }
        public override void Write(StreamWriter sw)
        {
            string methodName = null;
            if (Method != null)
                methodName = CorrectClassName(Method.Name);
            if (Method == null || Method.IsConstructor)
                methodName = $"{NEW}";

            var selfKeyword = SELF;

            var argumentList = new List<string>();
            if (Method != null)
            {
                selfKeyword = Method.IsStatic ? string.Empty : SELF;
                foreach (var arg in Method.GetParameters())
                {
                    string parameterName = arg.Name;
                    if (!arg.HasDefaultValue)
                    {
                        // No default value.  Check to see if a generic type.
                        if (arg.ParameterType.IsGenericType)
                        {
                            var arguments = new List<string>();
                            foreach (var genArgType in arg.ParameterType.GetGenericArguments())
                            {
                                arguments.Add(TypeConvertLibrary.ToPythonType(genArgType));
                                AddReferenceImports(Class.Module, genArgType);
                                Class.Module.AddGenericArgumentType(genArgType);
                            }

                            string genericType = TypeConvertLibrary.ToPythonType(arg.ParameterType);
                            if (!genericType.Contains(string.Join(",", arguments)))
                                argumentList.Add($"{arg.Name}: {TypeConvertLibrary.ToPythonType(arg.ParameterType)}[{string.Join(",", arguments)}]");
                            else
                                argumentList.Add($"{arg.Name}: {genericType}");
                        }
                        else
                        {
                            // Not a generic type.  Write as-is.
                            // Standard argument, no default value assigned.
                            argumentList.Add($"{arg.Name}: {TypeConvertLibrary.ToPythonType(arg.ParameterType)}");
                        }
                    }
                    else
                    {
                        if (arg.ParameterType.IsEnum)
                        {
                            // Parameter has a defualt value.  Type is an Enum.
                            argumentList.Add($"{arg.Name}: {TypeConvertLibrary.ToPythonType(arg.ParameterType)} = {arg.ParameterType.Name}.{arg.DefaultValue}");
                        }
                        else
                        {
                            // Parameter has a default value, not an Enum
                            if (arg.DefaultValue != null)
                                argumentList.Add($"{arg.Name}: {TypeConvertLibrary.ToPythonType(arg.ParameterType)} = {arg.DefaultValue}");
                            else
                                argumentList.Add($"{arg.Name}: {TypeConvertLibrary.ToPythonType(arg.ParameterType)} = {NONETYPE}");
                        }
                    }

                    TypeConvertLibrary.AddImportForPythonType(Class.Module, arg.ParameterType);
                    Class.Module.AddGenericArgumentType(arg.ParameterType);
                }
            }

            var pythonArguments = string.Join(", ", argumentList);
            pythonArguments = string.IsNullOrEmpty(pythonArguments) || Method.IsStatic ? pythonArguments : $", {pythonArguments}";

            var returnType = typeof(void);
            if (IsMethod)
                returnType = MethodInfo.ReturnType;

            var returnTypeString = TypeConvertLibrary.ToDefReturnType(returnType, Class.Module);

            StringBuilder sb = new StringBuilder();

            var method = $"{DEF} {methodName}({selfKeyword}{pythonArguments}) -> {returnTypeString}:";
            var indentation = GetIndentation(1);

            sb.AppendLine();
            if (Method != null && Method.IsStatic)
                sb.AppendLine($"{indentation}{STATIC_METHOD}");

            if (IsOverloaded)
                sb.AppendLine($"{indentation}{OVERLOAD}");

            var docString = string.Empty;
            if (IsMethod)
                docString = NewPythonmethodDocStringWriterLibrary(Class.Module.XmlDocument, MethodInfo).ToString();
            else
            {
                if (Class.ClassType.IsInterface || Class.ClassType.IsAbstract)
                {
                    docString = new PythonConstructorUnsupportedDocStringWriterLibrary().ToString();
                }
                else
                {
                    var args = Class.TypeParser.GetConstructorArguments();
                    docString = new PythonConstructorDocStringWriterLibrary(
                        member: Class.Module.XmlDocument?.GetMember(ConstructorInfo),
                        arguments: args,
                        indentLevel: 2).ToString();
                }
            }

            sb.AppendLine($"{indentation}{method}");
            sb.AppendLine($"{GetIndentation(1)}{docString}");

            if (!string.IsNullOrWhiteSpace(ExceptionMessage))
                sb.AppendLine($"{GetIndentation(2)}{ExceptionMessage}");

            sb.AppendLine($"{GetIndentation(2)}{PASS}");

            sw.Write(sb.ToString());
        }
        private PythonMethodDocStringWriterLibrary NewPythonmethodDocStringWriterLibrary(XmlDocumentaitonParserLibrary xmlDocument, MethodInfo m)
        {
            return new PythonMethodDocStringWriterLibrary(methodInfo: m, member: xmlDocument?.GetMember(m), indentLevel: 2);
        }
        #endregion

        #region Public Properties
        public string MethodName => Method.Name;
        public bool IsOverloaded { get; set; }
        public MethodBase Method { get; }
        #endregion

        #region Protected Methods
        protected override void Initialize()
        {
            if (Method == null)
                return;

            if (IsMethod)
                AddReferenceImports(Class.Module, MethodInfo.ReturnType);

            if (IsOverloaded)
                Class.Module.AddImportModule($"{TYPING}").AddType($"{OVERLOAD_TYPE}");

            foreach (var parameter in Method.GetParameters())
            {
                AddReferenceImports(Class.Module, parameter.ParameterType);
            }
        }
        #endregion

        #region Private Properties
        private MethodInfo MethodInfo => Method as MethodInfo;
        private ConstructorInfo ConstructorInfo => Method as ConstructorInfo;
        private bool IsMethod => Method != null ? Method.MemberType == MemberTypes.Method : false;
        private bool IsConstructor => Method.IsConstructor;
        private string ExceptionMessage { get; }
        #endregion
    }
}
