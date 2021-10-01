using System;
using System.Collections.Generic;
using System.Linq;
using System.Reflection;
using System.Text;

namespace AssemblyCrawler.Library
{
    public class PythonDocStringWriterLibrary
    {
        #region Constants
        private string ArgsDocString = "Args:";
        private string ReturnsDocString = "Returns:";
        private string RaisesDocString = "Raises:";
        #endregion

        #region Constructor
        public PythonDocStringWriterLibrary(int indentLevel = 1, string description = "")
        {
            Description = description;
            IndentLevel = indentLevel;
            ExceptionNames = new List<KeyValuePair<string, string>>();
            Args = new List<KeyValuePair<string, Type>>();
            Attributes = new List<KeyValuePair<string, Type>>();
            Returns = new List<KeyValuePair<string, Type>>();
        }
        #endregion

        #region Public Properties
        public List<KeyValuePair<string, string>> ExceptionNames { get; }
        public List<KeyValuePair<string, Type>> Args { get; }

        public List<KeyValuePair<string, Type>> Attributes { get; }
        public List<KeyValuePair<string, Type>> Returns { get; }

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
            if (Description?.Length > 0)
                sb.AppendLine(Description);

            // Args
            if (Args.Count > 0)
            {
                sb.AppendLine();
                sb.Append(indentation).AppendLine(ArgsDocString);

                foreach (var kvp in Args)
                    sb.Append(indentation).Append(Tab).Append(kvp.Key).AppendLine($"({TypeConvertLibrary.ToPythonType(kvp.Value)}): {kvp.Key}");
            }


            // Returns            
            //if (Returns.Count == 1)
            //    sb.AppendLine($" {TypeConvertLibrary.ToPythonType(Returns[0].Value)}: {Returns[0].Key}");

            else if (Returns.Count > 0)
            {
                sb.AppendLine();
                sb.Append(indentation).AppendLine(ReturnsDocString);

                foreach (var kvp in Returns)
                    sb.Append(indentation).Append(Tab).Append(TypeConvertLibrary.ToPythonType(kvp.Value)).Append(": ").AppendLine(kvp.Key);
            }



            // Exceptions
            if (ExceptionNames.Count > 0)
            {
                sb.AppendLine();
                sb.AppendLine();
                sb.Append(indentation).AppendLine(RaisesDocString);

                foreach (var kvp in ExceptionNames)
                    sb.Append(indentation).Append(Tab).Append(kvp.Key).AppendLine($": {kvp.Value}");
            }

            //sb.Append(Tab).Append(DocStringEnd);
            //sb.Append(indentation).Append(Tab).Append(DocStringEnd);
            //sb.Append(indentation);
            //sb.Length -= 1;
            //sb.Append(DocStringEnd);
            sb.Append(indentation).Append(DocStringEnd);

            return sb.ToString();
        }
        #endregion

        #region Private Properties
        private int IndentLevel { get; }
        private string Description { get; }
        private string DocStringStart => "\"\"\"";
        private string DocStringEnd => "\"\"\"";
        private string Tab => "\t";
        #endregion
    }

    public class PythonPropertyDocStringWriterLibrary : PythonDocStringWriterLibrary
    {
        #region Constructor
        public PythonPropertyDocStringWriterLibrary(Type type, string description, int indentLevel = 2)
            : base(indentLevel)
        {
            Returns.Add(new KeyValuePair<string, Type>(description, type));
        }
        #endregion
    }

    public class PythonClassDocStringWriterLibrary : PythonDocStringWriterLibrary
    {
        #region Constructor
        public PythonClassDocStringWriterLibrary(string description, int indentLevel = 1)
            : base(indentLevel, description)
        {
        }
        #endregion
    }

    public class PythonConstructorDocStringWriterLibrary : PythonDocStringWriterLibrary
    {
        #region Constructor
        public PythonConstructorDocStringWriterLibrary(
            string description, 
            List<KeyValuePair<string, Type>> arguments, 
            int indentLevel=2)
            :base(description: description, indentLevel: indentLevel)
        {
            Args.AddRange(arguments);
        }
        #endregion
    }


    public class PythonConstructorUnsupportedDocStringWriterLibrary : PythonDocStringWriterLibrary
    {
        #region Constructor
        public PythonConstructorUnsupportedDocStringWriterLibrary(int indentLevel = 2)
            : base(indentLevel, "Creating a new Instance of this class is not allowed")
        {
            ExceptionNames.Add(new KeyValuePair<string, string>("Exception", "if this class is instanciated"));
        }
        #endregion
    }

    public class PythonMethodDocStringWriterLibrary : PythonDocStringWriterLibrary
    {
        #region Constructor
        public PythonMethodDocStringWriterLibrary(MethodInfo methodInfo, string description, int indentLevel = 2)
            : base(indentLevel, description)
        {
            // Args
            var paramsKvps = methodInfo.GetParameters().Select(p => new KeyValuePair<string, Type>(p.Name, p.ParameterType)).ToList();
            Args.AddRange(paramsKvps);

            // Returns
            var returnKvps = new List<KeyValuePair<string, Type>>();
            returnKvps.Add(new KeyValuePair<string, Type>(methodInfo.ReturnParameter.Name, methodInfo.ReturnType));
            Returns.AddRange(returnKvps);
        }
        #endregion
    }

}
