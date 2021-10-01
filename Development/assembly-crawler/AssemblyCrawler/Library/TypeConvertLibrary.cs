// TypeLibrary.cs
// Copyright (c) 2021 Kristopher L. Culin See LICENSE for details

using System;
using System.Collections.Generic;
using System.Linq;

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
        #endregion

        #region Private Static Methdos

        private static string ToPythonPrimitiveType(Type type)
        {
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
                    return type.Name;

            }
        }
        #endregion
    }
}
