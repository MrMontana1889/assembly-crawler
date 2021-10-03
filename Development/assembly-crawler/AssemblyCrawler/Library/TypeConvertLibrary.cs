// TypeConvertLibrary.cs
// Copyright (c) 2021 Kristopher L. Culin See LICENSE for details

using System;
using System.Collections.Generic;
using System.Linq;
using AssemblyCrawler.Support;

namespace AssemblyCrawler.Library
{
	public static class TypeConvertLibrary
	{

		#region Public Static Methods

		public static string ToPythonType(Type type)
		{
			if (type == typeof(void)) return "None";
			if (type == typeof(Enum)) return "Enum";

			if (type.IsGenericType)
			{
				if (type.GetGenericTypeDefinition() == typeof(List<>)
				|| type.GetGenericTypeDefinition() == typeof(IList<>))
				{
					var itemType = type.GetGenericArguments().Single();
					return $"List[{ToPythonPrimitiveType(itemType)}]";
				}

				if (type.GetGenericTypeDefinition() == typeof(Dictionary<,>)
				|| type.GetGenericTypeDefinition() == typeof(IDictionary<,>))
				{
					var keyType = type.GetGenericArguments()[0];
					var valueType = type.GetGenericArguments()[0];
					return $"Dict[{ToPythonPrimitiveType(keyType)},{ToPythonPrimitiveType(valueType)}]";
				}

				if (type.GetGenericTypeDefinition() == typeof(IEnumerable<>))
				{
					var itemType = type.GetGenericArguments().Single();
					return $"Iterator[{ToPythonPrimitiveType(itemType)}]";
				}

				if (type.GetGenericTypeDefinition() == typeof(IComparer<>))
				{
					var itemType = type.GetGenericArguments().Single();
					return $"Comparer[{ToPythonPrimitiveType(itemType)}]"; // Is Comparer a thing in python?
				}

				// TODO: Predicate, Action, Converter, ReadOnlyCollection, Comparison
			}


			return ToPythonPrimitiveType(type);
		}
		public static void AddImportForPythonType(PythonModuleDefinition module, Type type)
		{
			string pythonType = ToPythonType(type);
			if (pythonType.StartsWith("List"))
				module.AddImportModule("typing").AddType("List");
			else if (pythonType.StartsWith("Dict"))
				module.AddImportModule("typing").AddType("Dict");
			else if (pythonType.StartsWith("Iterator"))
				module.AddImportModule("typing").AddType("Iterator");
			else if (pythonType.StartsWith("Comparer"))
				module.AddImportModule("typing").AddType("Comparer");
			else if (pythonType == "Enum")
				module.AddImportModule("enum").AddType("Enum");
			else if (pythonType == "datetime")
				module.AddImportModule("datetime").AddType("datetime");
			else if (pythonType == PythonStubWriterLibrary.CorrectClassName(type.Name, type.GetGenericArguments().Length))
			{
				// One of the types being written to the package.
				// Need to find the module where the type is located so it can be imported
				// IF it is not part of the current module.
				if (!type.IsGenericParameter)
				{
					var classDef = module.ClassDefinitions.Find(c => c.ClassName == type.Name);
					if (classDef == null)
					{
						// The class definition is not part of the current module.
						foreach (var mod in module.Package.Modules)
						{
							if (mod.Filename != module.Filename)
							{
								// Don't look at the current module.
								classDef = mod.ClassDefinitions.Find(c => c.ClassName == type.Name);
								if (classDef != null)
								{
									module.AddImportModule(type.Namespace).AddType(pythonType);
								}
							}
						}
					}
				}
				else
				{
					var typeVar = module.GetTypeVar(type.Name);

					if (typeVar == null)
					{
						//foreach (var mod in module.Package.Modules)
						bool typeVarFound = false;
						foreach (var mod in module.Package.Modules)
						{
							if (mod.ModuleNamespace != module.ModuleNamespace)
							{
								typeVar = mod.GetTypeVar(type.Name);
								if (typeVar != null)
								{
									module.AddImportModule(mod.ModuleNamespace).AddType(typeVar.TypeVarName);
									typeVarFound = true;
									break;
								}
							}
						}

						if (!typeVarFound)
						{
							module.AddTypeVar(type.Name, type.GetGenericParameterConstraints());
						}
					}
					else
					{
						var constraints = type.GetGenericParameterConstraints();
						foreach (var c in constraints)
						{
							AddImportForPythonType(module, c);
						}
					}

					//// This is a type parameer.  Still needs to be imported if needed
					//var typeVar = module.TypeVars.Find(t => t.TypeVarName == type.Name);
					//if (typeVar == null)
					//{
					//	// Search through other modules.
					//	foreach (var mod in module.Package.Modules)
					//	{
					//		if (mod.Filename != module.Filename)
					//		{
					//			typeVar = mod.TypeVars.Find(t => t.TypeVarName == type.Name);
					//			if (typeVar != null)
					//			{
					//				// Found
					//				Console.WriteLine($"Add import for {typeVar.TypeVarName} from {mod.Filename}");
					//				break;
					//			}
					//		}
					//	}
					//}
				}
			}
		}
		#endregion

		#region Private Static Methdos

		private static string ToPythonPrimitiveType(Type type)
		{
			if (type.IsEnum)
				return type.Name;

			switch (Type.GetTypeCode(type))
			{
				case TypeCode.Byte:
				case TypeCode.SByte:
				case TypeCode.UInt16:
				case TypeCode.UInt32:
				case TypeCode.UInt64:
				case TypeCode.Int16:
				case TypeCode.Int32:
				case TypeCode.Int64:
					return "int";

				case TypeCode.Single:
				case TypeCode.Decimal:
				case TypeCode.Double:
					return "float";

				case TypeCode.Boolean:
					return "bool";

				case TypeCode.Char:
				case TypeCode.String:
					return "str";

				case TypeCode.DateTime:
					return "datetime"; // must have "from datetime import datetime"

				//case TypeCode.Object:
				//	return "Any"; // must have "from typing import Any"

				default:
					return PythonStubWriterLibrary.CorrectClassName(type.Name, type.GetGenericArguments().Length);

			}
		}
		#endregion
	}
}
