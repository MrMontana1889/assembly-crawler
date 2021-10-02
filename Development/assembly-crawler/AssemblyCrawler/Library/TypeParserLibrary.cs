// TypeParserLibrary.cs
// Copyright (c) 2021 Kristopher L. Culin See LICENSE for details

using System;
using System.Collections.Generic;
using System.Linq;
using System.Reflection;

namespace AssemblyCrawler.Library
{
	public class TypeParserLibrary
	{
		#region Constructor
		public TypeParserLibrary(Type type)
		{
			Type = type;

			AllMethods = new List<MethodInfo>();
			SimpleMethods = new List<MethodInfo>();
			OverloadedMethods = new List<MethodInfo>();
			ReadOnlyProperties = new List<MethodInfo>();
			WriteOnlyProperties = new List<MethodInfo>();

			StaticFields = new List<MethodInfo>();
			//StaticNonOverloadedMethods = new List<MethodInfo>();
			//StaticOverloadedMethods = new List<MethodInfo>();
			//StaticReadOnlyProperties = new List<MethodInfo>();
			//StaticWriteOnlyProperties = new List<MethodInfo>();

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
			// Methods
			AllMethods = new List<MethodInfo>(Type.GetMethods());

			OverloadedMethodsName = AllMethods
				.GroupBy(m => m.Name)
				.Where(g => g.Count() > 1)
				.Select(m => m.Key)
				.ToList();

			foreach (var method in AllMethods)
			{
				if (method.Name.StartsWith("get_"))
					ReadOnlyProperties.Add(method);


				else if (method.Name.StartsWith("set_"))
					WriteOnlyProperties.Add(method);

				else if (OverloadedMethodsName.Contains(method.Name))
					OverloadedMethods.Add(method);

				else if (!OverloadedMethodsName.Contains(method.Name))
					SimpleMethods.Add(method);

				// +
				else if (method.Name == "op_Addition")
					OperatorAddition.Add(method);

				// -
				else if (method.Name == "op_Subtraction")
					OperatorSubtraction.Add(method);

				// *
				else if (method.Name == "op_Multiply")
					OperatorMultiplication.Add(method);

				// /
				else if (method.Name == "op_Division")
					OperatorDivision.Add(method);

				// %
				else if (method.Name == "op_Modulus")
					OperatorModulo.Add(method);

				// ==
				else if (method.Name == "op_Equality")
					OperatorEquality.Add(method);

				// !=
				else if (method.Name == "op_Inequality")
					OperatorInequality.Add(method);

				// >
				else if (method.Name == "op_GreaterThan")
					OperatorGreaterThan.Add(method);

				// <
				else if (method.Name == "op_LessThan")
					OperatorLessThan.Add(method);

				// >=
				else if (method.Name == "op_GreaterThanOrEqual")
					OperatorGreaterOrEqualTo.Add(method);

				// <=
				else if (method.Name == "op_LessThanOrEqual")
					OperatorLessOrEqualTo.Add(method);

				// &
				else if (method.Name == "op_BitwiseAnd")
					OperatorBitwiseAnd.Add(method);

				// |
				else if (method.Name == "op_BitwiseOr")
					OperatorBitwiseOr.Add(method);

				// ^
				else if (method.Name == "op_ExclusiveOr")
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

		public List<KeyValuePair<string, Type>> GetConstructorArguments()
		{
			var parameters = new List<ParameterInfo>();
			foreach (var c in Type.GetConstructors())
				parameters.AddRange(new List<ParameterInfo>(c.GetParameters()));

			return parameters.Select(p => new KeyValuePair<string, Type>(p.Name ?? "", p.ParameterType)).ToList();
		}

		public List<KeyValuePair<string, Type>> GetMethodArguments(MethodInfo method)
		{
			var parameters = new List<ParameterInfo>(method.GetParameters());
			return parameters.Select(p => new KeyValuePair<string, Type>(p.Name ?? "", p.ParameterType)).ToList();
		}

		public string GetPropertyName(MethodInfo methodInfo) => methodInfo.Name.Substring(4);
		#endregion


		#region Public Properties
		public Type Type { get; }
		public string Name => Type.Name;
		public bool IsInterface { get; private set; }
		public bool IsGenericType { get; private set; }
		public List<MethodInfo> AllMethods { get; private set; }
		public List<MethodInfo> OverloadedMethods { get; private set; }
		public List<MethodInfo> SimpleMethods { get; }
		public List<MethodInfo> ReadOnlyProperties { get; }
		public List<MethodInfo> WriteOnlyProperties { get; }
		public List<MethodInfo> StaticFields { get; }

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


		public List<Type> GenericInterfaces { get; private set; }
		public List<Type> NonGenericInterfaces { get; private set; }
		#endregion

		#region Private Properties
		private List<string> OverloadedMethodsName { get; set; }
		#endregion
	}
}
