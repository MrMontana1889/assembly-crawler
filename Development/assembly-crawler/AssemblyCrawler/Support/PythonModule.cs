// PythonStubFile.cs
// Copyright (c) 2021 Kristopher L. Culin See LICENSE for details

using System;
using System.Collections.Generic;
using System.Diagnostics;
using System.IO;
using System.Text;
using AssemblyCrawler.Library;

namespace AssemblyCrawler.Support
{
	[DebuggerDisplay("{ModuleNamespace} : {Filename}")]
	public class PythonModule : StubFileBase
	{
		#region Constructor
		public PythonModule(PythonAssembly assembly, string moduleNamespace, string filename, string xmlDocumentFilename)
			: base(filename)
		{
			Assembly = assembly;
			ModuleNamespace = moduleNamespace;
			XmlDocument = new XmlDocumentaitonParserLibrary(xmlDocumentFilename).Parse();
		}
		#endregion

		#region Public Methods
		public override void Write()
		{
			// Before writing, verify that all possible imports are included.
			foreach (var arg in GenericArgumentTypes)
			{
				string typeName = arg.Name;
				TypeConvertLibrary.AddImportForPythonType(this, arg);
			}

			foreach (var pythonClass in Classes)
				pythonClass.Update();

			using (FileStream fileStream = new FileStream(Filename, FileMode.Create, FileAccess.ReadWrite, FileShare.ReadWrite))
			{
				using (StreamWriter sw = new StreamWriter(fileStream, Encoding.ASCII))
				{
					bool shouldImportTypeVar = false;
					foreach (var typeVar in TypeVars)
					{
						if (!HasImportedType(typeVar.TypeVarName))
						{
							shouldImportTypeVar = true;
							break;
						}
					}

					if (shouldImportTypeVar)
						AddImportModule("typing").AddType("TypeVar");

					if (Imports.Count > 0)
					{
						foreach (var import in Imports)
							import.Write(sw);

						sw.WriteLine();
					}

					if (TypeVars.Count > 0)
					{
						foreach (var typeVar in TypeVars)
						{
							if (!HasImportedType(typeVar.TypeVarName))
								typeVar.Write(sw);
						}
						sw.WriteLine();
					}

					var enums = Classes.FindAll(c => c.ClassType.IsEnum);
					var pythonClasses = Classes.FindAll(c => !c.ClassType.IsEnum);

					foreach (var pythonEnum in enums)
						pythonEnum.Write(sw);

					foreach (var pythonClass in pythonClasses)
						pythonClass.Write(sw);
				}
			}
		}
		public PythonImport AddImportModule(string module)
		{
			if (Imports.Find(m => m.Module == module) == null)
			{
				Imports.Add(new PythonImport(module));
			}
			return GetImport(module);
		}
		public PythonImport GetImport(string module)
		{
			return Imports.Find(m => m.Module == module);
		}
		public bool HasImportedType(string type)
		{
			foreach (var import in Imports)
			{
				if (import.HasType(type))
					return true;
			}

			return false;
		}
		public PythonTypeVar AddTypeVar(string typeVarName, params Type[] constraints)
		{
			if (TypeVars.Find(tv => tv.TypeVarName == typeVarName) == null)
			{
				TypeVars.Add(new PythonTypeVar(typeVarName, constraints));
			}
			return GetTypeVar(typeVarName);
		}
		public PythonTypeVar GetTypeVar(string typeVarName)
		{
			return TypeVars.Find(t => t.TypeVarName == typeVarName);
		}
		public PythonClass AddClassDefinition(Type classType)
		{
			string fullName = classType.FullName;
			string className = classType.Name;
			if (fullName == null) throw new InvalidOperationException($"{nameof(fullName)} parameter is null");

			if (Classes.Find(c => c.FullName == fullName && c.ClassName == className) == null)
				Classes.Add(new PythonClass(this, classType));
			return GetPythonClass(fullName, className);
		}
		public PythonClass GetPythonClass(Type classType)
		{
			return GetPythonClass(classType.FullName, classType.Name);
		}
		public PythonClass GetPythonClass(string fullName, string className)
		{
			return Classes.Find(c => c.FullName == fullName && c.ClassName == className);
		}
		public void AddGenericArgumentType(Type type)
		{
			if (!string.IsNullOrEmpty(type.Namespace) && type.Namespace.StartsWith("System"))
				return;

			if (type.IsGenericParameter)
				return;

			if (type.IsEnum)
				return;

			if (GenericArgumentTypes.Find(t => t.Name == type.Name) == null)
				GenericArgumentTypes.Add(type);
		}
		#endregion

		#region Public Properties
		public List<PythonImport> Imports { get; } = new List<PythonImport>();
		public List<PythonClass> Classes { get; } = new List<PythonClass>();
		public List<PythonTypeVar> TypeVars { get; } = new List<PythonTypeVar>();
		public PythonAssembly Assembly { get; }
		public string ModuleNamespace { get; }
		public List<Type> GenericArgumentTypes { get; } = new List<Type>();
		public XmlDocumentaitonParserLibrary XmlDocument { get; }
		#endregion
	}
}
