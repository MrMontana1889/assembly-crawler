// ReflectionExtensions.cs
// Copyright (c) 2022 Kristopher L. Culin See LICENSE for details

using System;
using System.Linq;
using System.Reflection;

namespace AssemblyCrawler.Extensions
{
	public static class ReflectionExtensions
	{
		#region Constants
		public static class MemberType
		{
			public const string Ctor = ".ctor";
			public const string PoundCtor = "#ctor";

			public const char TypeInfo = 'T';
			public const char Property = 'P';
			public const char Method = 'M';
			public const char Event = 'E';
			public const char Field = 'E';
			public const char Error = '!';

		}
		#endregion

		public static string XmlMemberName(this MethodInfo methodInfo)
		{
			return XmlMemberName(methodInfo as MemberInfo);
		}

		public static string XmlMemberName(this MemberInfo memberInfo)
		{
			char prefixCode;
			string memberName = (memberInfo is Type)
				? ((Type)memberInfo).FullName                               // member is a Type
				: (memberInfo.DeclaringType.FullName + "." + memberInfo.Name);  // member belongs to a Type

			switch (memberInfo.MemberType)
			{
				case MemberTypes.Constructor:
					// XML documentation uses slightly different constructor names
					memberName = memberName.Replace(MemberType.Ctor, MemberType.PoundCtor);
					goto case MemberTypes.Method;
				case MemberTypes.Method:
					prefixCode = MemberType.Method;

					// parameters are listed according to their type, not their name
					string paramTypesList = String.Join(
						",",
						((MethodBase)memberInfo).GetParameters()
							.Cast<ParameterInfo>()
							.Select(x => x.ParameterType.FullName
						).ToArray()
					);
					if (!String.IsNullOrEmpty(paramTypesList)) memberName += "(" + paramTypesList + ")";
					break;

				case MemberTypes.Event:
					prefixCode = MemberType.Event;
					break;

				case MemberTypes.Field:
					prefixCode = MemberType.Field;
					break;

				case MemberTypes.NestedType:
					// XML documentation uses slightly different nested type names
					memberName = memberName.Replace('+', '.');
					goto case MemberTypes.TypeInfo;
				case MemberTypes.TypeInfo:
					prefixCode = MemberType.TypeInfo;
					break;

				case MemberTypes.Property:
					prefixCode = MemberType.Property;
					break;

				default:
					throw new ArgumentException("Unknown member type", "member");
			}

			// elements are of the form "M:Namespace.Class.Method"
			return $"{prefixCode}:{memberName}";
		}
	}
}
