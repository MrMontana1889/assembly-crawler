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
                if (method.Name.StartsWith("get_") /*&& !method.IsStatic*/)
                    ReadOnlyProperties.Add(method);


                else if (method.Name.StartsWith("set_") /*&& !method.IsStatic*/)
                    WriteOnlyProperties.Add(method);

                //else if (method.Name.StartsWith("get_") && method.IsStatic)
                //    StaticReadOnlyProperties.Add(method);


                //else if (method.Name.StartsWith("set_") && method.IsStatic)
                //    StaticWriteOnlyProperties.Add(method);


                
                else if(OverloadedMethodsName.Contains(method.Name) /*&& !method.IsStatic*/)
                    OverloadedMethods.Add(method);

                else if (!OverloadedMethodsName.Contains(method.Name) /*&& !method.IsStatic*/)
                    SimpleMethods.Add(method);

                //else if (OverloadedMethodsName.Contains(method.Name) && method.IsStatic)
                //    StaticOverloadedMethods.Add(method);

                //else if (!OverloadedMethodsName.Contains(method.Name) && method.IsStatic)
                //    StaticNonOverloadedMethods.Add(method);

            }

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
            var parameters = new List<ParameterInfo> (method.GetParameters());
            return parameters.Select(p => new KeyValuePair<string, Type>(p.Name ?? "", p.ParameterType)).ToList();
        }

        public string GetPropertyName(MethodInfo methodInfo) => methodInfo.Name.Substring(4);
        #endregion


        #region Public Properties
        public Type Type { get; }
        public string Name => Type.Name;
        public bool IsInterface => Type.IsInterface;
        public bool IsGenericType => Type.IsGenericType;
        public List<MethodInfo> AllMethods { get; private set; }
        public List<MethodInfo> OverloadedMethods { get; private set; }
        public List<MethodInfo> SimpleMethods { get; }
        public List<MethodInfo> ReadOnlyProperties { get; }
        public List<MethodInfo> WriteOnlyProperties { get; }
        //public List<MethodInfo> StaticReadOnlyProperties { get; }
        //public List<MethodInfo> StaticWriteOnlyProperties { get; }
        //public List<MethodInfo> StaticOverloadedMethods { get; }
        //public List<MethodInfo> StaticNonOverloadedMethods { get; }
        public List<MethodInfo> StaticFields { get; }
        public List<Type> GenericInterfaces { get; private set; }
        public List<Type> NonGenericInterfaces { get; private set; }
        #endregion

        #region Private Properties
        private List<string> OverloadedMethodsName { get; set; }
        #endregion
    }
}
