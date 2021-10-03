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
	public class PythonModuleDefinition : StubFileBase
	{
		#region Constructor
		public PythonModuleDefinition(PythonAssemblyDefinition assembly, string moduleNamespace, string filename)
			: base(filename)
		{
			Assembly = assembly;
			ModuleNamespace = moduleNamespace;
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

					foreach (var pythonClass in ClassDefinitions)
						pythonClass.Write(sw);
				}
			}
		}
		public ImportDefinition AddImportModule(string module)
		{
			if (Imports.Find(m => m.Module == module) == null)
			{
				Imports.Add(new ImportDefinition(module));
			}
			return GetImport(module);
		}
		public ImportDefinition GetImport(string module)
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
		public TypeVarDefinition AddTypeVar(string typeVarName, params Type[] constraints)
		{
			if (TypeVars.Find(tv => tv.TypeVarName == typeVarName) == null)
			{
				TypeVars.Add(new TypeVarDefinition(typeVarName, constraints));
			}
			return GetTypeVar(typeVarName);
		}
		public TypeVarDefinition GetTypeVar(string typeVarName)
		{
			return TypeVars.Find(t => t.TypeVarName == typeVarName);
		}
		public PythonClassDefinition AddClassDefinition(string fullName, string className)
		{
			if (fullName == null) throw new InvalidOperationException($"{nameof(fullName)} parameter is null");

			if (ClassDefinitions.Find(c => c.FullName == fullName && c.ClassName == className) == null)
				ClassDefinitions.Add(new PythonClassDefinition(this, fullName, className));
			return GetClassDefinition(fullName, className);
		}
		public PythonClassDefinition GetClassDefinition(string fullName, string className)
		{
			return ClassDefinitions.Find(c => c.FullName == fullName && c.ClassName == className);
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
		public List<ImportDefinition> Imports { get; } = new List<ImportDefinition>();
		public List<PythonClassDefinition> ClassDefinitions { get; } = new List<PythonClassDefinition>();
		public List<TypeVarDefinition> TypeVars { get; } = new List<TypeVarDefinition>();
		public PythonAssemblyDefinition Assembly { get; }
		public string ModuleNamespace { get; }
		public List<Type> GenericArgumentTypes { get; } = new List<Type>();
		#endregion
	}
}
