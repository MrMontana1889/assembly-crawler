// InterfacesOnlyTypeFilter.cs
// Copyright (c) 2021 See LICENSE for details

using System;

namespace Barber.AutoDiagrammer.Support
{
    /// <summary>
    /// Filters the assembly so it only includes interfaces, static classes and enum types
    /// Excludes classes that are in a namespace starting with System or Haestad
    /// </summary>
	[Serializable]
    public class InterfacesOnlyTypeFilter : ITypeFilter
	{
		#region Constructor
		public InterfacesOnlyTypeFilter(bool overrideHaestadNamespace)
		{
            OverrideHaestadNamespace = overrideHaestadNamespace;
		}
		#endregion

		#region Public Methods
		public bool IncludeType(Type t)
		{
            if (t == null)
                return false;

            if (t.IsNotPublic)
                return false;       // Exclude all non-public types

            //check to see if the class lives in a namespace
            if (t.Namespace != null && !string.IsNullOrEmpty(t.Namespace))
            {
                //dont really want user to trawl the standard System namespaces
                if (t.Namespace.StartsWith("System"))
                    return false;

                if (!OverrideHaestadNamespace && t.Namespace.StartsWith("Haestad"))
                    return false;       // Ignore all types in haestad assemblies
            }

            if (!t.IsClass && t.IsInterface)
                return true;

            if (t.IsEnum)
                return true;

            if (t.IsClass && t.IsPublic && t.IsAbstract)
                return true;

            return false;
        }
		#endregion

		#region Private Properties
        private bool OverrideHaestadNamespace { get; }
        #endregion
    }
}
