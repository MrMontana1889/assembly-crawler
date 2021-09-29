using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace AssemblyCrawler.Library
{
	public static class TypeLibrary
	{
		public static string ConvertTypeToPythonType(Type type)
		{
			if (type == null) return "None";

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
	}
}
