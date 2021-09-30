using System;
using System.Collections.Generic;
using System.Reflection;
using System.Text;

namespace AssemblyCrawler.Library
{
    public class PythonDocStringWriterLibrary
    {
        #region Constructor
        public PythonDocStringWriterLibrary(int indentLevel = 1, string description = "")
        {
            Description = description;
            IndentLevel = indentLevel;
            ExceptionNames = new List<KeyValuePair<string, string>>();
            Args = new List<KeyValuePair<Type, string>>();
            Attributes = new List<KeyValuePair<Type, string>>();
            Returns = new List<KeyValuePair<Type, string>>();
        }
        #endregion

        #region Public Properties
        public List<KeyValuePair<string, string>> ExceptionNames { get; }
        public List<KeyValuePair<Type, string>> Args { get; }

        public List<KeyValuePair<Type, string>> Attributes { get; }
        public List<KeyValuePair<Type, string>> Returns { get; }

        #endregion

        #region Public Methods

        #endregion

        #region Private Methods       

        private string GetIndentation()
        {
            var tabs = "";
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
                sb.AppendLine();
                sb.Append(indentation).AppendLine("Args:");

                foreach (var kvp in Args)
                    sb.Append(indentation).Append(Tab).Append(kvp.Key.Name).AppendLine($"({TypeConvertLibrary.ToPythonType(kvp.Key)}): {kvp.Value}");
            }


            // Returns            
            if (Returns.Count == 1)
                sb.AppendLine($" {TypeConvertLibrary.ToPythonType(Returns[0].Key)}: {Returns[0].Value}");

            else if (Returns.Count > 1)
            {
                sb.Append(indentation).AppendLine("Returns:");

                foreach (var kvp in Returns)
                    sb.Append(indentation).Append(Tab).Append(TypeConvertLibrary.ToPythonType(kvp.Key)).Append(": ").AppendLine(kvp.Value);
            }



            // Exceptions
            if (ExceptionNames.Count > 0)
            {
                sb.AppendLine();
                sb.AppendLine();
                sb.Append(indentation).AppendLine("Raises:");

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
            Returns.Add(new KeyValuePair<Type, string>(type, description));
        }
        #endregion
    }

    public class PythonClassDocStringWriterLibrary : PythonDocStringWriterLibrary
    {
        #region Constructor
        public PythonClassDocStringWriterLibrary(string description, int indentLevel = 0)
            : base(indentLevel, description)
        {
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

            // Returns
        }
        #endregion
    }

}
