// PythonStubFile.cs
// Copyright (c) 2021 Kristopher L. Culin See LICENSE for details

using System;
using System.Collections.Generic;
using System.Diagnostics;
using System.IO;
using System.Text;

namespace AssemblyCrawler.Support
{
	[DebuggerDisplay("{ModuleNamespace} : {Filename}")]
	public class PythonModuleDefinition : StubFileBase
	{
		#region Constructor
		public PythonModuleDefinition(PythonPackageDefinition package, string moduleNamespace, string filename)
			: base(filename)
		{
			Package = package;
			ModuleNamespace = moduleNamespace;
		}
		#endregion

		#region Public Methods
		public override void Write()
		{
			using (FileStream fileStream = new FileStream(Filename, FileMode.Create, FileAccess.ReadWrite, FileShare.ReadWrite))
			{
				using (StreamWriter sw = new StreamWriter(fileStream, Encoding.ASCII))
				{
					if (Imports.Count > 0)
					{
						foreach (var import in Imports)
							import.Write(sw);

						sw.WriteLine();
					}

					if (TypeVars.Count > 0)
					{
						foreach (var typeVar in TypeVars)
							typeVar.Write(sw);
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
		public TypeVarDefinition AddTypeVar(string typeVarName, Type[] constraints)
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
		#endregion

		#region Public Properties
		public List<ImportDefinition> Imports { get; } = new List<ImportDefinition>();
		public List<PythonClassDefinition> ClassDefinitions { get; } = new List<PythonClassDefinition>();
		public List<TypeVarDefinition> TypeVars { get; } = new List<TypeVarDefinition>();
		public PythonPackageDefinition Package { get; }
		public string ModuleNamespace { get; }
		#endregion
	}
}
