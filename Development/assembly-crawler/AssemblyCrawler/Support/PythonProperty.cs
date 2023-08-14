// PythonProperty.cs
// Copyright (c) 2022 Kristopher L. Culin See LICENSE for details

using AssemblyCrawler.Library;
using System.Collections.Generic;
using System.IO;
using System.Reflection;
using System.Text;
using static AssemblyCrawler.Library.TypeConvertLibrary;
using static AssemblyCrawler.Library.WriterLibrary;
using static AssemblyCrawler.Support.Constants;

namespace AssemblyCrawler.Support
{
    public class PythonProperty : WriterBase
    {
		#region Constructor
		public PythonProperty(PythonClass pythonClass, PropertyInfo propertyInfo)
			: base(pythonClass)
		{
			PropertyInfo = propertyInfo;
			Initialize();
		}
		#endregion

		#region Public Methods
		public void Update()
		{
			if (PropertyInfo.CanRead)
			{
				AddReferenceImports(Class.Module, PropertyInfo.PropertyType);
			}
		}
		public override void Write(StreamWriter sw)
		{
			StringBuilder sb = new StringBuilder();

			var indentation = GetIndentation(1);

			if (PropertyInfo.CanRead)
			{
				var mi = PropertyInfo.GetMethod;

				sb.AppendLine();

				if (mi.IsStatic)
					sb.AppendLine($"{indentation}{STATIC_METHOD}");
				sb.AppendLine($"{indentation}{PROPERTY}");

				AddReferenceImports(Class.Module, mi.ReturnType);
				Class.Module.AddGenericArgumentType(mi.ReturnType);

				var selfKeyword = mi.IsStatic ? string.Empty : SELF;

				var adjustedReturnType = ToDefReturnType(mi.ReturnType, Class.Module);


                var docString = new PythonPropertyDocStringWriterLibrary(
					type: mi.ReturnType,
					member: Class.Module.XmlDocument?.GetMember(PropertyInfo),
					indentLevel: 2).ToString();

				sb.AppendLine($"{indentation}{DEF} {GetName(PropertyInfo.Name)}({selfKeyword}) -> {adjustedReturnType}:");
				sb.AppendLine($"{indentation}{docString}");
				sb.AppendLine($"{GetIndentation(2)}{PASS}");
			}

			if (PropertyInfo.CanWrite)
			{
				sb.AppendLine();

				sb.AppendLine($"{indentation}@{PropertyInfo.Name}{SETTER}");

				var mi = PropertyInfo.SetMethod;
				if (mi.IsStatic)
					sb.AppendLine($"{indentation}{STATIC_METHOD}");

				string propertyType = ToPythonType(PropertyInfo.PropertyType);
				if (PropertyInfo.PropertyType.IsGenericType)
				{
					var arguments = new List<string>();
					foreach (var genArgType in PropertyInfo.PropertyType.GetGenericArguments())
					{
						arguments.Add(ToPythonType(genArgType));
						AddReferenceImports(Class.Module, genArgType);
						Class.Module.AddGenericArgumentType(genArgType);
					}

					if (!propertyType.Contains(string.Join(",", arguments)))
						propertyType = $"{ToPythonType(PropertyInfo.PropertyType)}[{string.Join(",", arguments)}]";

				}

				sb.AppendLine($"{indentation}{DEF} {PropertyInfo.Name}({SELF}, {PropertyInfo.Name.ToLowerInvariant()}: " +
					$"{propertyType}) -> {NONETYPE}:");
				sb.AppendLine($"{GetIndentation(2)}{PASS}");
			}

			sw.Write(sb.ToString());
		}
		#endregion

		#region Protected Methods
		protected override void Initialize()
		{
			if (PropertyInfo.CanRead)
			{
				AddReferenceImports(Class.Module, PropertyInfo.PropertyType);
			}
		}
		#endregion

		#region Private Methods
		private object GetName(string name)
		{
			if (name == "None")
				return "_None";
			return name;
		}
		private PythonMethodDocStringWriterLibrary NewPythonmethodDocStringWriterLibrary(XmlDocumentaitonParserLibrary xmlDocument, MethodInfo m)
		{
			return new PythonMethodDocStringWriterLibrary(methodInfo: m, member: xmlDocument?.GetMember(m), indentLevel: 2);
		}
		#endregion

		#region Private Properties
		private PropertyInfo PropertyInfo { get; }
		#endregion
	}
}
