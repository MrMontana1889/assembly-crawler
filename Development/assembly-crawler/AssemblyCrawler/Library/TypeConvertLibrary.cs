// TypeConvertLibrary.cs
// Copyright (c) 2021 Kristopher L. Culin See LICENSE for details

using System;
using System.Collections;
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
			if (type.IsByRef)
				if (type.HasElementType)
					type = type.GetElementType();

			if (type == typeof(void)) return "None";
			if (type == typeof(Enum)) return "Enum";

			if (type.IsArray)
			{
				var typeName = type.Name.Replace("[]", "");
				if (typeName == "Double")
					return $"array(float)";

				return $"array({ToPythonType(type.GetElementType())})";
			}

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
			else
			{
				if (type == typeof(IDictionary))
					return "Dict";
				else if (type == typeof(ArrayList) || type == typeof(IList))
					return "List";
				else if (type == typeof(IEnumerable))
					return "Iterator";
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
			else if (pythonType.StartsWith("array"))
				module.AddImportModule("array").AddType("array");
			else if (pythonType == PythonStubWriterLibrary.CorrectClassName(type.Name, type.GetGenericArguments().Length))
			{
				// One of the types being written to the package.
				// Need to find the module where the type is located so it can be imported
				// IF it is not part of the current module.
				if (!type.IsGenericParameter)
				{
					foreach (var assem in module.Assembly.Package.Assemblies)
					{
						foreach (var mod in assem.Modules)
						{
							if (mod.Filename != module.Filename)
							{
								var classD = mod.ClassDefinitions.Find(c => c.ClassName == type.Name);
								if (classD != null)
									module.AddImportModule(type.Namespace).AddType(pythonType);
							}
						}
					}
				}
				else
				{
					var typeVar = module.GetTypeVar(type.Name);
					if (typeVar == null)
					{
						bool typeVarFound = false;
						foreach (var assem in module.Assembly.Package.Assemblies)
						{
							foreach (var mod in assem.Modules)
							{
								if (mod.ModuleNamespace != module.ModuleNamespace)
								{
									var modTypeVar = mod.GetTypeVar(type.Name);
									if (modTypeVar != null)
									{
										module.AddImportModule(mod.ModuleNamespace).AddType(modTypeVar.TypeVarName);
										typeVarFound = true;
										break;
									}
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
				}

				if (!type.IsGenericType && !type.IsGenericParameter && type.IsEnum)
				{
					module.Assembly.AddEnum(type);
				}
			}
		}
		#endregion

		#region Private Static Methdos

		private static string ToPythonPrimitiveType(Type type)
		{
			if (type.IsEnum)
				return type.Name;

			if (type.IsByRef)
			{
				if (type.HasElementType)
					type = type.GetElementType();
			}

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

					if (type.Name == "Object")
						return "object";

					return PythonStubWriterLibrary.CorrectClassName(type.Name, type.GetGenericArguments().Length);

			}
		}
		#endregion
	}
}
