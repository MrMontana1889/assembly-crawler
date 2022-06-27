// SerializableVertex.cs
// Copyright (c) 2021 Sacha Barber See LICENSE for details

using System;
using System.Collections.Generic;

namespace Barber.AutoDiagrammer.GraphBits
{
	/// <summary>
	/// A simple Serializable vertex.
	/// </summary>
	[Serializable]
	public class SerializableVertex
	{
		#region Ctor
		public SerializableVertex
			(
				string name,
				string shortName,
				List<string> constructors,
				List<string> fields,
				List<string> properties,
				List<string> interfaces,
				List<SerializableMethodData> methods,
				List<string> events,
				List<string> associations,
				bool hasConstructors,
				bool hasFields,
				bool hasProperties,
				bool hasInterfaces,
				bool hasMethods,
				bool hasEvents
			)
		{
			Name = name;
			ShortName = shortName;
			Constructors = constructors;
			Fields = fields;
			Properties = properties;
			Interfaces = interfaces;
			Methods = methods;
			Events = events;
			Associations = associations;
			HasConstructors = hasConstructors;
			HasFields = hasFields;
			HasProperties = hasProperties;
			HasInterfaces = hasInterfaces;
			HasMethods = hasMethods;
			HasEvents = hasEvents;
		}
		#endregion

		#region Public Properties

		public string Name { get; }
		public string ShortName { get; }
		public List<string> Constructors { get; }
		public List<string> Fields { get; }
		public List<string> Properties { get; }
		public List<string> Interfaces { get; }
		public List<SerializableMethodData> Methods { get; }
		public List<string> Events { get; }
		public List<string> Associations { get; }
		public bool HasConstructors { get; }
		public bool HasFields { get; }
		public bool HasProperties { get; }
		public bool HasInterfaces { get; }
		public bool HasMethods { get; }
		public bool HasEvents { get; }
		#endregion

		#region Overrides
		public override string ToString()
		{
			return Name;
		}
		#endregion
	}
}
