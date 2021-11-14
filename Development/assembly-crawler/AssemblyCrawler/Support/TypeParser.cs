// TypeParser.cs
// Copyright (c) 2021 Kristopher L. Culin see LICENSE for details

using static AssemblyCrawler.Support.Constants;
using System;
using System.Collections.Generic;
using System.Linq;
using System.Reflection;
using AssemblyCrawler.Extensions;

namespace AssemblyCrawler.Support
{
	//Based on Akshaya's TypeParserLibrary
	public class TypeParser
	{
		#region Constructor
		public TypeParser(PythonClass pythonClass)
		{
			Class = pythonClass;
		}
		#endregion

		#region Public Methods
		public TypeParser Parse()
		{
			foreach (var member in Type.GetMembers())
			{
				if (!MemberInfoMap.ContainsKey(member.XmlMemberName()))
					MemberInfoMap.Add(member.XmlMemberName(), member);
			}

			foreach (var property in Type.GetProperties())
				Properties.Add(new PythonProperty(Class, property));

			AllMethods = new List<MethodInfo>(Type.GetMethods());

			OverloadedMethodNames = AllMethods
				.GroupBy(m => m.Name)
				.Where(g => g.Count() > 1)
				.Select(m => m.Key)
				.ToList();

			foreach (var method in AllMethods)
			{
				if (method.Name.StartsWith(GETTER_PREFIX))
					continue;       // Skip getters

				if (method.Name.StartsWith(SETTER_PREFIX))
					continue;       // Skip setters

				switch (method.Name)
				{
					case EQUALS:
					case GETHASHCODE:
					case GETTYPE:
					case TOSTRING:
						continue;
				}

				if (OverloadedMethodNames.Contains(method.Name))
					Methods.Add(new PythonMethod(Class, method, true));

				if (!OverloadedMethodNames.Contains(method.Name))
					Methods.Add(new PythonMethod(Class, method, false));

				// +
				if (method.Name == OP_ADDITION)
					OperatorAddition.Add(new PythonMethod(Class, method));

				// -
				if (method.Name == OP_SUBTRACTION)
					OperatorSubtraction.Add(new PythonMethod(Class, method));

				// *
				if (method.Name == OP_MULTIPLICATION)
					OperatorMultiplication.Add(new PythonMethod(Class, method));

				// /
				if (method.Name == OP_DIVISION)
					OperatorDivision.Add(new PythonMethod(Class, method));

				// %
				if (method.Name == OP_MODULUS)
					OperatorModulo.Add(new PythonMethod(Class, method));

				// ==
				if (method.Name == OP_EQUALITY)
					OperatorEquality.Add(new PythonMethod(Class, method));

				// !=
				if (method.Name == OP_INEQUALITY)
					OperatorInequality.Add(new PythonMethod(Class, method));

				// >
				if (method.Name == OP_GREATERTHAN)
					OperatorGreaterThan.Add(new PythonMethod(Class, method));

				// <
				if (method.Name == OP_LESSTHAN)
					OperatorLessThan.Add(new PythonMethod(Class, method));

				// >=
				if (method.Name == OP_GREATERTHANOREQUAL)
					OperatorGreaterOrEqualTo.Add(new PythonMethod(Class, method));

				// <=
				if (method.Name == OP_LESSTHANOREQUAL)
					OperatorLessOrEqualTo.Add(new PythonMethod(Class, method));

				// &
				if (method.Name == OP_BITWISEAND)
					OperatorBitwiseAnd.Add(new PythonMethod(Class, method));

				// |
				if (method.Name == OP_BITWISEOR)
					OperatorBitwiseOr.Add(new PythonMethod(Class, method));

				// ^
				if (method.Name == OP_EXCLUSIVEOR)
					OperatorBitwiseXor.Add(new PythonMethod(Class, method));
			}

			if (AllMethods.Count > 0)
				AddInheritedOverloadedMethods(Type);

			foreach (var interf in Type.GetInterfaces())
			{
				if (interf.IsGenericType)
					GenericInterfaces.Add(interf);
				else
					Interfaces.Add(interf);
			}

			return this;
		}
		public List<KeyValuePair<string, KeyValuePair<Type, object>>> GetConstructorArguments()
		{
			var parameters = new List<ParameterInfo>();
			foreach (var c in Type.GetConstructors())
				parameters.AddRange(new List<ParameterInfo>(c.GetParameters()));

			return parameters.Select(p => new KeyValuePair<string, KeyValuePair<Type, object>>(p.Name ?? "",
				new KeyValuePair<Type, object>(p.ParameterType, p.HasDefaultValue ? p.DefaultValue : null))).ToList();
		}

		public List<KeyValuePair<string, KeyValuePair<Type, object>>> GetMethodArguments(MethodInfo method)
		{
			string methodName = method.Name;
			var parameters = new List<ParameterInfo>(method.GetParameters());
			return parameters.Select(p => new KeyValuePair<string, KeyValuePair<Type, object>>(p.Name ?? "",
				new KeyValuePair<Type, object>(p.ParameterType, p.HasDefaultValue ? p.DefaultValue : null))).ToList();
		}
		#endregion

		#region Public Properties
		public Type Type => Class.ClassType;
		public string Name => Type.Name;
		public bool IsInterface => Type.IsInterface;
		public bool IsGenericType => Type.IsGenericType;
		public List<MethodInfo> AllMethods { get; private set; } = new List<MethodInfo>();
		public List<PythonMethod> Methods { get; private set; } = new List<PythonMethod>();
		public List<PythonProperty> Properties { get; } = new List<PythonProperty>();

		public List<PythonMethod> OperatorAddition { get; } = new List<PythonMethod>();
		public List<PythonMethod> OperatorSubtraction { get; } = new List<PythonMethod>();
		public List<PythonMethod> OperatorMultiplication { get; } = new List<PythonMethod>();
		public List<PythonMethod> OperatorDivision { get; } = new List<PythonMethod>();
		public List<PythonMethod> OperatorModulo { get; } = new List<PythonMethod>();
		public List<PythonMethod> OperatorEquality { get; } = new List<PythonMethod>();
		public List<PythonMethod> OperatorInequality { get; } = new List<PythonMethod>();
		public List<PythonMethod> OperatorGreaterThan { get; } = new List<PythonMethod>();
		public List<PythonMethod> OperatorLessThan { get; } = new List<PythonMethod>();
		public List<PythonMethod> OperatorGreaterOrEqualTo { get; } = new List<PythonMethod>();
		public List<PythonMethod> OperatorLessOrEqualTo { get; } = new List<PythonMethod>();
		public List<PythonMethod> OperatorBitwiseAnd { get; } = new List<PythonMethod>();
		public List<PythonMethod> OperatorBitwiseOr { get; } = new List<PythonMethod>();
		public List<PythonMethod> OperatorBitwiseXor { get; } = new List<PythonMethod>();

		public List<Type> GenericInterfaces { get; } = new List<Type>();
		public List<Type> Interfaces { get; } = new List<Type>();

		public Dictionary<string, MemberInfo> MemberInfoMap { get; } = new Dictionary<string, MemberInfo>();
		#endregion

		#region Private Methods
		private string GetIndentation(int indentLevel)
		{
			var tabs = string.Empty;
			for (int i = 0; i < indentLevel; i++) tabs += "\t";
			return tabs;
		}

		private void AddInheritedOverloadedMethods(Type type, int indentation = 1)
		{
			/*
			 * This method will be complicated.  It needs to look at the inherited types of the current type
			 * to determine if there are methods that are named the same as in this type but overloads it by
			 * having different parameters.  Overloaded methods will have the same return type.
			*/

			level += 1;

			//Console.WriteLine($"\tProcessing inherited interfaces (Level: {level})");

			string typeName = type.Name;
			TypeInfo typeInfo = type as TypeInfo;
			if (typeInfo != null)
			{
				foreach (var interf in typeInfo.ImplementedInterfaces)
				{
					if (interf.Namespace.StartsWith("System"))
						continue;

					if (interf == type)
						continue;
					CheckInterface(interf);
					AddInheritedOverloadedMethods(interf, indentation + 2);
				}
			}

			level -= 1;
		}

		private int level;

		private void CheckInterface(Type interf)
		{
			string interfName = interf.Name;
			foreach (var method in interf.GetMethods())
			{
				if (method.Name.StartsWith($"{SETTER_PREFIX}") ||
					method.Name.StartsWith($"{GETTER_PREFIX}"))
					continue;       // Ignore properties

				string interfMethodName = method.Name;
				var currentMethod = AllMethods.Find(m => m.Name == method.Name && !method.Name.StartsWith($"{GETTER_PREFIX}")
					 && !method.Name.StartsWith($"{SETTER_PREFIX}"));
				if (currentMethod != null)
				{
					string methodName = currentMethod.Name;

					// Check to see if the argument list differs.
					var method1Arguments = new List<ParameterInfo>(currentMethod.GetParameters());
					var method2Arguments = new List<ParameterInfo>(method.GetParameters());

					if (method1Arguments.Count == 0 && method2Arguments.Count == 0)
						continue;

					// If the parameter count differs, then include it.
					if (method1Arguments.Count != method2Arguments.Count)
					{
						// Change the IsOverload status of the existing method from false to true.
						var pythonMethods = Methods.FindAll(m => m.MethodName == currentMethod.Name);
						bool addMethod = true;
						foreach (var pythonMethod in pythonMethods)
						{
							if (pythonMethod.Method == method)
							{
								addMethod = false;
								break;
							}
						}
						if (addMethod)
						{
							Methods.Add(new PythonMethod(Class, method, true));
							foreach (var pythonMethod in pythonMethods)
								pythonMethod.IsOverloaded = true;
						}
					}
					else
					{
						if (method1Arguments.Count() > 0 && method1Arguments.Count() == method2Arguments.Count())
						{
							bool isDifferent = false;
							// There is more than 1 argument and the count matches.
							for (int i = 0; i < method1Arguments.Count; ++i)
							{
								var p1 = method1Arguments[i];
								var p2 = method2Arguments[i];

								if (p1.Name != p2.Name)
								{
									isDifferent = true;
									break;
								}
								else if (p1.ParameterType != p2.ParameterType)
								{
									isDifferent = true;
									break;
								}
							}

							if (isDifferent)
							{
								// the interface has a method of the same name as in the AllMethods list
								// of the current type.  Add as an overloaded method.
								var pythonMethod = Methods.Find(m => m.MethodName == currentMethod.Name && m.IsOverloaded == false);
								if (pythonMethod != null)
								{
									pythonMethod.IsOverloaded = true;
									Methods.Add(new PythonMethod(Class, method, true));
								}
							}
						}
					}
				}
			}
		}
		#endregion

		#region Private Properties
		private PythonClass Class { get; }
		private List<string> OverloadedMethodNames { get; set; }
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
