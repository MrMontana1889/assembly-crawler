// PythonDocStringWriterLibrary.cs
// Copyright (c) 2021 Kristopher L. Culin See LICENSE for details

using System;
using System.Collections.Generic;
using System.Linq;
using System.Reflection;
using System.Text;
using AssemblyCrawler.Support.XmlDocumentMember;

namespace AssemblyCrawler.Library
{
    public class PythonDocStringWriterLibrary
    {
        #region Constants
        public static string ArgsDocString = "Args:";
        public static string ReturnsDocString = "Returns:";
        public static string RaisesDocString = "Raises:";
        public static string NoteDocString = "Note:";
        public static string NoDescription = "No Description";
        #endregion

        #region Constructor
        public PythonDocStringWriterLibrary(Member member, int indentLevel = 1)
        {
            XmlMember = member;
            IndentLevel = indentLevel;
            ExceptionNames = new List<KeyValuePair<string, string>>();
            Args = new List<KeyValuePair<string, KeyValuePair<Type, object>>>();
            Attributes = new List<KeyValuePair<string, Type>>();
            Returns = new List<KeyValuePair<string, Type>>();
        }
        #endregion

        

        #region Public Properties
        public List<KeyValuePair<string, string>> ExceptionNames { get;  }
        public List<KeyValuePair<string, KeyValuePair<Type, object>>> Args { get;  }

        public List<KeyValuePair<string, Type>> Attributes { get;  }
        public List<KeyValuePair<string, Type>> Returns { get;  }

        #endregion

        #region Public Methods

        #endregion

        #region Private Methods       

        private string GetIndentation()
        {
            var tabs = string.Empty;
            for (int i = 0; i < IndentLevel; i++) tabs += Tab;
            return tabs;
        }

        #endregion

        #region Overrides
        public override string ToString()
        {
            var indentation = GetIndentation();
            var sb = new StringBuilder().Append(Tab).Append(DocStringStart);


            // Description
            // TODO: Figure out how to handle para
            var description = XmlMember?.Summary.Content?.Trim() ?? "No Description";

            // TypeParam
            if (XmlMember?.Typeparam?.Count > 0)
            {
                sb.Append(indentation).AppendLine(ArgsDocString);
                foreach (var param in XmlMember.Typeparam)
                {
                    sb.Append(indentation).Append(Tab).Append(param.Name).Append(":").Append(param.Name);
                }
            }

            sb.AppendLine(description);


            // Args
            if (Args.Count > 0)
            {
                sb.AppendLine();

                sb.Append(indentation).AppendLine(ArgsDocString);
                foreach (var kvp in Args)
                {
                    var argsName = kvp.Key;
                    var argType = kvp.Value.Key;

                    var param = XmlMember?.Param.Where(p => p.Name == kvp.Key)?.FirstOrDefault();
                    sb.Append(indentation).Append(Tab).Append(argsName).AppendLine($"({TypeConvertLibrary.ToPythonType(argType)}): {param?.Text ?? argsName}");
                }
            }

            // Remarks / Nodes
            if (!string.IsNullOrEmpty(XmlMember?.Remarks))
            {
                sb.AppendLine();
                sb.Append(indentation).AppendLine(NoteDocString);
                sb.Append(indentation).Append(Tab).AppendLine(XmlMember?.Remarks);
            }


            if (Returns.Count > 0)
            {
                sb.AppendLine();
                sb.Append(indentation).AppendLine(ReturnsDocString);
                var returnMessage = XmlMember?.Returns?.Content ?? string.Empty;
                // TODO: Figure out how to handle TypeParamRef
                
                foreach (var kvp in Returns)
                {
                    sb.Append(indentation).Append(Tab).Append(TypeConvertLibrary.ToPythonType(kvp.Value)).Append(": ").AppendLine(returnMessage);
                }
            }



            // Exceptions
            if (ExceptionNames.Count > 0)
            {
                sb.AppendLine();
                sb.AppendLine();
                sb.Append(indentation).AppendLine(RaisesDocString);

                var exceptionMessage = XmlMember?.Exception?.ToString();

                foreach (var kvp in ExceptionNames)
                {
                    exceptionMessage = string.IsNullOrEmpty(exceptionMessage) ? kvp.Value : exceptionMessage;
                    sb.Append(indentation).Append(Tab).Append(kvp.Key).AppendLine($": {exceptionMessage}");
                }
            }

            sb.Append(indentation).Append(DocStringEnd);

            return sb.ToString();
        }
        #endregion

        #region Private Properties
        private int IndentLevel { get; }
        private Member XmlMember { get; }
        private string DocStringStart => "\"\"\"";
        private string DocStringEnd => "\"\"\"";
        private string Tab => "\t";
        #endregion
    }

    public class PythonPropertyDocStringWriterLibrary : PythonDocStringWriterLibrary
    {
        #region Constructor
        public PythonPropertyDocStringWriterLibrary(Type type, Member member, int indentLevel = 2)
            : base(member, indentLevel)
        {
            var info = member?.Summary.Content ?? NoDescription;
            Returns.Add(new KeyValuePair<string, Type>(info, type));
        }
        #endregion
    }

    public class PythonClassDocStringWriterLibrary : PythonDocStringWriterLibrary
    {
        #region Constructor
        public PythonClassDocStringWriterLibrary(Member member, int indentLevel = 1)
            : base(member, indentLevel)
        {
        }
        #endregion
    }

    public class PythonConstructorDocStringWriterLibrary : PythonDocStringWriterLibrary
    {
        #region Constructor
        public PythonConstructorDocStringWriterLibrary(
            Member member,
            List<KeyValuePair<string, KeyValuePair<Type, object>>> arguments,
            int indentLevel = 2)
            : base(member, indentLevel)
        {
            Args.AddRange(arguments);
        }
        #endregion
    }


    public class PythonConstructorUnsupportedDocStringWriterLibrary : PythonDocStringWriterLibrary
    {
        #region Constructor
        public PythonConstructorUnsupportedDocStringWriterLibrary(int indentLevel = 2)
            : base(new Member() {Summary = new Summary() { Content = "Creating a new Instance of this class is not allowed" } }, indentLevel)
        {
            ExceptionNames.Add(new KeyValuePair<string, string>("Exception", "if this class is instanciated"));
        }
        #endregion
    }

    public class PythonMethodDocStringWriterLibrary : PythonDocStringWriterLibrary
    {
        #region Constructor
        public PythonMethodDocStringWriterLibrary(MethodInfo methodInfo, Member member, int indentLevel = 2)
            : base(member, indentLevel)
        {
            // Args
            var paramsKvps = methodInfo.GetParameters().Select(p => new KeyValuePair<string, KeyValuePair<Type, object>>(p.Name, 
                new KeyValuePair<Type, object>(p.ParameterType, p.HasDefaultValue ? p.DefaultValue : null))).ToList();
            Args.AddRange(paramsKvps);

            // Returns
            var returnKvps = new List<KeyValuePair<string, Type>>();
            returnKvps.Add(new KeyValuePair<string, Type>(methodInfo.ReturnType.Name, methodInfo.ReturnType));
            Returns.AddRange(returnKvps);
        }
        #endregion
    }

}
