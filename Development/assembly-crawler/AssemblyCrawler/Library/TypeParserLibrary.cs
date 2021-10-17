// TypeParserLibrary.cs
// Copyright (c) 2021 Kristopher L. Culin See LICENSE for details

using System;
using System.Collections.Generic;
using System.Linq;
using System.Reflection;
using AssemblyCrawler.Extensions;

namespace AssemblyCrawler.Library
{
	public class TypeParserLibrary
	{
		#region Constructor
		public TypeParserLibrary(Type type)
		{
			if (type == null)
				throw new ArgumentNullException(nameof(type));

			Type = type;

			AllMethods = new List<MethodInfo>();
			SimpleMethods = new List<MethodInfo>();
			OverloadedMethods = new List<MethodInfo>();
			Constructors = new List<ConstructorInfo>();
			ReadOnlyProperties = new List<MethodInfo>();
			WriteOnlyProperties = new List<MethodInfo>();

			StaticFields = new List<FieldInfo>();

			OperatorAddition = new List<MethodInfo>();
			OperatorSubtraction = new List<MethodInfo>();
			OperatorMultiplication = new List<MethodInfo>();
			OperatorDivision = new List<MethodInfo>();
			OperatorModulo = new List<MethodInfo>();
			OperatorEquality = new List<MethodInfo>();
			OperatorInequality = new List<MethodInfo>();
			OperatorGreaterThan = new List<MethodInfo>();
			OperatorLessThan = new List<MethodInfo>();
			OperatorGreaterOrEqualTo = new List<MethodInfo>();
			OperatorLessOrEqualTo = new List<MethodInfo>();
			OperatorBitwiseAnd = new List<MethodInfo>();
			OperatorBitwiseOr = new List<MethodInfo>();
			OperatorBitwiseXor = new List<MethodInfo>();


			GenericInterfaces = new List<Type>();
			NonGenericInterfaces = new List<Type>();

			OverloadedMethodsName = new List<string>();
		}
		#endregion

		#region Public Methods
		public TypeParserLibrary Parse()
		{
			// Member Info is used to extract information from xml document 
            foreach (var member in Type.GetMembers())
				MemberInfoMap.Add(member.XmlMemberName(), member);

            // Static Fields
            foreach (var field in Type.GetFields())
            {
				if (field.IsStatic)
					StaticFields.Add(field);
            }

			// Constructors
			Constructors.AddRange(Type.GetConstructors());

			// Methods
			AllMethods = new List<MethodInfo>(Type.GetMethods());

			OverloadedMethodsName = AllMethods
				.GroupBy(m => m.Name)
				.Where(g => g.Count() > 1)
				.Select(m => m.Key)
				.ToList();

			foreach (var method in AllMethods)
			{
				if (method.Name.StartsWith(GETTER_PREFIX))
					ReadOnlyProperties.Add(method);


				else if (method.Name.StartsWith(SETTER_PREFIX))
					WriteOnlyProperties.Add(method);

				else if (OverloadedMethodsName.Contains(method.Name))
					OverloadedMethods.Add(method);

				else if (!OverloadedMethodsName.Contains(method.Name))
					SimpleMethods.Add(method);

				// +
				else if (method.Name == OP_ADDITION)
					OperatorAddition.Add(method);

				// -
				else if (method.Name == OP_SUBTRACTION)
					OperatorSubtraction.Add(method);

				// *
				else if (method.Name == OP_MULTIPLICATION)
					OperatorMultiplication.Add(method);

				// /
				else if (method.Name == OP_DIVISION)
					OperatorDivision.Add(method);

				// %
				else if (method.Name == OP_MODULUS)
					OperatorModulo.Add(method);

				// ==
				else if (method.Name == OP_EQUALITY)
					OperatorEquality.Add(method);

				// !=
				else if (method.Name == OP_INEQUALITY)
					OperatorInequality.Add(method);

				// >
				else if (method.Name == OP_GREATERTHAN)
					OperatorGreaterThan.Add(method);

				// <
				else if (method.Name == OP_LESSTHAN)
					OperatorLessThan.Add(method);

				// >=
				else if (method.Name == OP_GREATERTHANOREQUAL)
					OperatorGreaterOrEqualTo.Add(method);

				// <=
				else if (method.Name == OP_LESSTHANOREQUAL)
					OperatorLessOrEqualTo.Add(method);

				// &
				else if (method.Name == OP_BITWISEAND)
					OperatorBitwiseAnd.Add(method);

				// |
				else if (method.Name == OP_BITWISEOR)
					OperatorBitwiseOr.Add(method);

				// ^
				else if (method.Name == OP_EXCLUSIVEOR)
					OperatorBitwiseXor.Add(method);

			}

			IsGenericType = Type.IsGenericType;
			IsInterface = Type.IsInterface;

			// Interfaces
			foreach (var interf in Type.GetInterfaces())
			{
				if (interf.IsGenericType)
					GenericInterfaces.Add(interf);
				else
					NonGenericInterfaces.Add(interf);
			}

			return this;
		}

		//// TODO: Handle overloaded constructors
		//public List<KeyValuePair<string, Type>> GetConstructorArguments()
		//{
		//	var parameters = new List<ParameterInfo>();
		//	foreach (var c in Type.GetConstructors())
		//		parameters.AddRange(new List<ParameterInfo>(c.GetParameters()));

		//	return parameters.Select(p => new KeyValuePair<string, Type>(p.Name ?? "", p.ParameterType)).ToList();
		//}

		public List<KeyValuePair<string, KeyValuePair<Type, object>>> GetMethodArguments(MethodInfo method)
		{
			string methodName = method.Name;
			var parameters = new List<ParameterInfo>(method.GetParameters());
			return parameters.Select(p => new KeyValuePair<string, KeyValuePair<Type, object>>(p.Name ?? "", 
				new KeyValuePair<Type, object>(p.ParameterType, p.HasDefaultValue ? p.DefaultValue : null))).ToList();
		}
		public List<KeyValuePair<string, KeyValuePair<Type, object>>> GetConstructorArguments(ConstructorInfo constructorInfo)
        {
			var parameters = new List<ParameterInfo>(constructorInfo.GetParameters());
			return parameters.Select(p => 
				new KeyValuePair<string, KeyValuePair<Type, object>>(
					p.Name ?? "", 
					new KeyValuePair<Type, object>(
						p.ParameterType, 
						p.HasDefaultValue
							? p.DefaultValue
							: null))).ToList();
		}

		public string GetPropertyName(MethodInfo methodInfo) => methodInfo.Name.Substring(4);
		#endregion

		#region Public Properties
		public Type Type { get; }
		public string Name => Type.Name; // TODO: get rid of this
		public bool IsInterface { get; private set; }
		public bool IsGenericType { get; private set; }
		public List<ConstructorInfo> Constructors { get; private set; }
		public List<MethodInfo> AllMethods { get; private set; }
		public List<MethodInfo> OverloadedMethods { get; private set; }
		public List<MethodInfo> SimpleMethods { get; }
		public List<MethodInfo> ReadOnlyProperties { get; }
		public List<MethodInfo> WriteOnlyProperties { get; }
		public List<FieldInfo> StaticFields { get; }

		public List<MethodInfo> OperatorAddition { get; private set; }
		public List<MethodInfo> OperatorSubtraction { get; private set; }
		public List<MethodInfo> OperatorMultiplication { get; private set; }
		public List<MethodInfo> OperatorDivision { get; private set; }
		public List<MethodInfo> OperatorModulo { get; private set; }
		public List<MethodInfo> OperatorEquality { get; private set; }
		public List<MethodInfo> OperatorInequality { get; private set; }
		public List<MethodInfo> OperatorGreaterThan { get; private set; }
		public List<MethodInfo> OperatorLessThan { get; private set; }
		public List<MethodInfo> OperatorGreaterOrEqualTo { get; private set; }
		public List<MethodInfo> OperatorLessOrEqualTo { get; private set; }
		public List<MethodInfo> OperatorBitwiseAnd { get; private set; }
		public List<MethodInfo> OperatorBitwiseOr { get; private set; }
		public List<MethodInfo> OperatorBitwiseXor { get; private set; }


		// Are these two needed?
		public List<Type> GenericInterfaces { get; private set; }
		public List<Type> NonGenericInterfaces { get; private set; }

		public Dictionary<string, MemberInfo> MemberInfoMap { get; } = new Dictionary<string, MemberInfo>();
		#endregion

		#region Private Properties
		private List<string> OverloadedMethodsName { get; set; }
		#endregion

		#region Private Constants
		private const string OP_ADDITION = "op_Addition";
		private const string OP_SUBTRACTION = "op_Subtraction";
		private const string OP_MULTIPLICATION = "op_Multiply";
		private const string OP_DIVISION = "op_Division";
		private const string OP_MODULUS = "op_Modulus";
		private const string OP_EQUALITY = "op_Equality";
		private const string OP_INEQUALITY = "op_Inequality";
		private const string OP_GREATERTHAN = "op_GreaterThan";
		private const string OP_LESSTHAN = "op_LessThan";
		private const string OP_GREATERTHANOREQUAL = "op_GreaterThanOrEqual";
		private const string OP_LESSTHANOREQUAL = "op_LessThanOrEqual";
		private const string OP_BITWISEAND = "op_BitwiseAnd";
		private const string OP_BITWISEOR = "op_BitwiseOr";
		private const string OP_EXCLUSIVEOR = "op_ExclusiveOr";
		private const string GETTER_PREFIX = "get_";
		private const string SETTER_PREFIX = "set_";
		#endregion
	}
}
