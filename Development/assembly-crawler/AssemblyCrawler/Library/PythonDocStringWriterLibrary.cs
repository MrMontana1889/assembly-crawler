using System;
using System.Collections.Generic;
using System.Text;

namespace AssemblyCrawler.Library
{
    public class PythonDocStringWriterLibrary
    {
        #region Constructor
        public PythonDocStringWriterLibrary(int indentLevel=1, string description="")
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
        private string ReturnsDocString()
        {            
            var indentation = GetIndentation();

            if (Returns.Count == 0) 
                return string.Empty;
                
            else if(Returns.Count == 1)
                return $"{indentation}{TypeLibrary.ConvertTypeToPythonType(Returns[0].Key)}: {Returns[0].Value}";

            var str = new StringBuilder().Append(indentation).AppendLine("Returns:");

            indentation += Tab;
            foreach (var kvp in Returns)
                str.Append(indentation).Append(TypeLibrary.ConvertTypeToPythonType(kvp.Key)).Append(": ").AppendLine(kvp.Value);
            
            return str.ToString();
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
            if(Args.Count > 0)
            {
                sb.AppendLine();
                sb.AppendLine();
                sb.Append(indentation).AppendLine("Args:");

                foreach (var kvp in Args)
                    sb.Append(indentation).Append(Tab).Append(kvp.Key.Name).AppendLine($"({TypeLibrary.ConvertTypeToPythonType(kvp.Key)}): {kvp.Value}");
            }

            // Returns
            var returnDocStr = ReturnsDocString();
            if(returnDocStr?.Length > 0)
                sb.AppendLine();

            // Exceptions
            if(ExceptionNames.Count > 0)
            {
                sb.AppendLine();
                sb.AppendLine();
                sb.Append(indentation).AppendLine("Raises:");

                foreach (var kvp in ExceptionNames)
                    sb.Append(indentation).Append(Tab).Append(kvp.Key).AppendLine($": {kvp.Value}");
            }

            sb.Append(indentation).AppendLine(DocStringEnd).AppendLine();
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

    public class PythonPropertyDocStringWriterLibrary: PythonDocStringWriterLibrary
    {
        #region Constructor
        public PythonPropertyDocStringWriterLibrary(Type type, string description) :base()
        {
            Returns.Add(new KeyValuePair<Type, string>(type, description));
        }
        #endregion
    }

    public class PythonClassDocStringWriterLibrary: PythonDocStringWriterLibrary
    {
        #region Constructor
        public PythonClassDocStringWriterLibrary(string description, int indentLevel=0)
            :base(indentLevel, description)
        {            
        }
        #endregion
    }

    public class PythonConstructorUnsupportedDocStringWriterLibrary: PythonDocStringWriterLibrary
    {
        #region Constructor
        public PythonConstructorUnsupportedDocStringWriterLibrary(int indentLevel=2)
            :base(indentLevel, "Creating a new Instance of this class is not allowed")
        {
            ExceptionNames.Add(new KeyValuePair<string, string>("Exception", "if this class instanciated"));
        }
        #endregion
    }

    public class PythonFunctionDocStringWriterLibrary : PythonDocStringWriterLibrary
    {
        #region Constructor
        public PythonFunctionDocStringWriterLibrary(string description, int indentLevel = 1)
            :base(indentLevel, description)
        {
            // TODO: Find out best way to pass method information
        }
        #endregion
    }

}
