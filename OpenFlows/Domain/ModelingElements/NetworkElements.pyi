from OpenFlows.Domain.ModelingElements import IModelingElementBase, TElementManagerType, TElementType, TElementTypeEnum, IElementUnits, IElementInput, IElementResults, IElementsInput, IElementsResults, IModelingElementsBase, IElement, IGeometryUnits
from typing import Generic, List, overload, Dict, TypeVar
from enum import Enum
from OpenFlows.Domain.ModelingElements.Support import IFieldManager
from OpenFlows.Units import IUnit
from OpenFlows.Enumerations import *

TUnitsType = TypeVar("TUnitsType", IElementUnits)
TElementInputType = TypeVar("TElementInputType", IElementInput)
TElementResultsType = TypeVar("TElementResultsType", IElementResults)
TElementsInputType = TypeVar("TElementsInputType", IElementsInput)
TElementsResultsType = TypeVar("TElementsResultsType", IElementsResults)

class INetworkElement(Generic[TElementManagerType, TElementType, TUnitsType, TElementTypeEnum, TElementInputType, TElementResultsType, TElementsInputType, TElementsResultsType], IModelingElementBase[TElementManagerType, TElementType, TElementTypeEnum]):

	def __init__(self) -> None:
		"""Creating a new Instance of this class is not allowed


		Raises:
			Exception: if this class is instanciated
		"""
		raise Exception("Creating a new Instance of this class is not allowed")
		pass

	@property
	def GISIDs(self) -> str:
		"""No Description

		Returns:
			INetworkElement: 
		"""
		pass

	@property
	def Input(self) -> TElementInputType:
		"""No Description

		Returns:
			INetworkElement: 
		"""
		pass

	@property
	def Results(self) -> TElementResultsType:
		"""No Description

		Returns:
			INetworkElement: 
		"""
		pass

	@property
	def Units(self) -> TUnitsType:
		"""No Description

		Returns:
			INetworkElement: 
		"""
		pass

	@GISIDs.setter
	def GISIDs(self, gisids: str) -> None:
		pass

class INetworkElements(Generic[TElementManagerType, TElementType, TUnitsType, TElementTypeEnum, TElementInputType, TElementResultsType, TElementsInputType, TElementsResultsType], IModelingElementsBase[TElementManagerType, TElementType, TElementTypeEnum]):

	def __init__(self) -> None:
		"""Creating a new Instance of this class is not allowed


		Raises:
			Exception: if this class is instanciated
		"""
		raise Exception("Creating a new Instance of this class is not allowed")
		pass

	def Elements(self, state: ElementStateType = ElementStateType.All) -> List[TElementType]:
		"""Returns a list of elements of the given state.

		Args:
			state(ElementStateType): Determines the state of the element to include

		Returns:
			List[TElementType]: Returns a list of 
		"""
		pass

	@property
	def Results(self) -> TElementsResultsType:
		"""No Description

		Returns:
			INetworkElements: 
		"""
		pass

	@property
	def Input(self) -> TElementsInputType:
		"""No Description

		Returns:
			INetworkElements: 
		"""
		pass

	@property
	def ResultFields(self) -> IFieldManager:
		"""No Description

		Returns:
			INetworkElements: 
		"""
		pass

class IActiveElementInput(IElementInput):

	def __init__(self) -> None:
		"""Creating a new Instance of this class is not allowed


		Raises:
			Exception: if this class is instanciated
		"""
		raise Exception("Creating a new Instance of this class is not allowed")
		pass

	@property
	def IsActive(self) -> bool:
		"""No Description

		Returns:
			IActiveElementInput: 
		"""
		pass

	@IsActive.setter
	def IsActive(self, isactive: bool) -> None:
		pass

class IActiveElementsInput(IElementsInput):

	def __init__(self) -> None:
		"""Creating a new Instance of this class is not allowed


		Raises:
			Exception: if this class is instanciated
		"""
		raise Exception("Creating a new Instance of this class is not allowed")
		pass

	@overload
	def IActiveElementsInput(self) -> Dict[int,int]:
		"""Gets all IsActive values for all elements of this type.

		Returns:
			Dict[int,int]: 
		"""
		pass

	@overload
	def IActiveElementsInput(self, ids: List[int]) -> Dict[int,int]:
		"""No Description

		Args:
			ids(List[int]): ids

		Returns:
			Dict[int,int]: 
		"""
		pass

class IPointNodeInput(IActiveElementInput):

	def __init__(self) -> None:
		"""Creating a new Instance of this class is not allowed


		Raises:
			Exception: if this class is instanciated
		"""
		raise Exception("Creating a new Instance of this class is not allowed")
		pass

	def GetPoint(self) -> GeometryPoint:
		"""Gets the geometry of the node.

		Returns:
			GeometryPoint: 
		"""
		pass

	def SetPoint(self, point: GeometryPoint) -> None:
		"""Sets the geometry of the node.

		Args:
			point(GeometryPoint): The point location of the node.

		Returns:
			None: 
		"""
		pass

class IPointNodesInput(IActiveElementsInput):

	def __init__(self) -> None:
		"""Creating a new Instance of this class is not allowed


		Raises:
			Exception: if this class is instanciated
		"""
		raise Exception("Creating a new Instance of this class is not allowed")
		pass

	@overload
	def IPointNodesInput(self) -> Dict[int,int]:
		"""Gets the geometry of all nodes of this type.

		Returns:
			Dict[int,int]: 
		"""
		pass

	@overload
	def IPointNodesInput(self, ids: List[int]) -> Dict[int,int]:
		"""No Description

		Args:
			ids(List[int]): ids

		Returns:
			Dict[int,int]: 
		"""
		pass

class IBaseLinkInput(IActiveElementInput):

	def __init__(self) -> None:
		"""Creating a new Instance of this class is not allowed


		Raises:
			Exception: if this class is instanciated
		"""
		raise Exception("Creating a new Instance of this class is not allowed")
		pass

	def GetPoints(self) -> List[GeometryPoint]:
		"""Gets the list of geometry for the link.  The first point is the geometry of the start node.  The last point
            is the geometry of the stop node.

		Returns:
			List[GeometryPoint]: 
		"""
		pass

	def SetPoints(self, points: List[GeometryPoint]) -> None:
		"""No Description

		Args:
			points(List[GeometryPoint]): points

		Returns:
			None: 
		"""
		pass

	@property
	def StartNode(self) -> IElement:
		"""No Description

		Returns:
			IBaseLinkInput: 
		"""
		pass

	@property
	def StopNode(self) -> IElement:
		"""No Description

		Returns:
			IBaseLinkInput: 
		"""
		pass

	@property
	def IsUserDefinedLength(self) -> bool:
		"""No Description

		Returns:
			IBaseLinkInput: 
		"""
		pass

	@property
	def Length(self) -> float:
		"""No Description

		Returns:
			IBaseLinkInput: 
		"""
		pass

	@StartNode.setter
	def StartNode(self, startnode: IElement) -> None:
		pass

	@StopNode.setter
	def StopNode(self, stopnode: IElement) -> None:
		pass

	@IsUserDefinedLength.setter
	def IsUserDefinedLength(self, isuserdefinedlength: bool) -> None:
		pass

	@Length.setter
	def Length(self, length: float) -> None:
		pass

class IBaseLinksInput(IActiveElementsInput):

	def __init__(self) -> None:
		"""Creating a new Instance of this class is not allowed


		Raises:
			Exception: if this class is instanciated
		"""
		raise Exception("Creating a new Instance of this class is not allowed")
		pass

	@overload
	def IBaseLinksInput(self) -> Dict[int,int]:
		"""Gets the polyline geometries for all base links.

		Returns:
			Dict[int,int]: 
		"""
		pass

	@overload
	def IBaseLinksInput(self, ids: List[int]) -> Dict[int,int]:
		"""No Description

		Args:
			ids(List[int]): ids

		Returns:
			Dict[int,int]: 
		"""
		pass

	@overload
	def IBaseLinksInput(self) -> Dict[int,int]:
		"""Gets start nodes for all base links.

		Returns:
			Dict[int,int]: 
		"""
		pass

	@overload
	def IBaseLinksInput(self, ids: List[int]) -> Dict[int,int]:
		"""No Description

		Args:
			ids(List[int]): ids

		Returns:
			Dict[int,int]: 
		"""
		pass

	@overload
	def IBaseLinksInput(self) -> Dict[int,int]:
		"""Gets stop nodes for all base links.

		Returns:
			Dict[int,int]: 
		"""
		pass

	@overload
	def IBaseLinksInput(self, ids: List[int]) -> Dict[int,int]:
		"""No Description

		Args:
			ids(List[int]): ids

		Returns:
			Dict[int,int]: 
		"""
		pass

	@overload
	def IBaseLinksInput(self) -> Dict[int,int]:
		"""Gets user defined lengths for all base links.

		Returns:
			Dict[int,int]: 
		"""
		pass

	@overload
	def IBaseLinksInput(self, ids: List[int]) -> Dict[int,int]:
		"""No Description

		Args:
			ids(List[int]): ids

		Returns:
			Dict[int,int]: 
		"""
		pass

	@overload
	def IBaseLinksInput(self) -> Dict[int,int]:
		"""Gets lengths for all base links.

		Returns:
			Dict[int,int]: 
		"""
		pass

	@overload
	def IBaseLinksInput(self, ids: List[int]) -> Dict[int,int]:
		"""No Description

		Args:
			ids(List[int]): ids

		Returns:
			Dict[int,int]: 
		"""
		pass

class IBaseLinksResults(IElementsResults):

	def __init__(self) -> None:
		"""Creating a new Instance of this class is not allowed


		Raises:
			Exception: if this class is instanciated
		"""
		raise Exception("Creating a new Instance of this class is not allowed")
		pass

class IBaseLinkResults(IElementResults):

	def __init__(self) -> None:
		"""Creating a new Instance of this class is not allowed


		Raises:
			Exception: if this class is instanciated
		"""
		raise Exception("Creating a new Instance of this class is not allowed")
		pass

class IBaseLinkUnits(IGeometryUnits):

	def __init__(self) -> None:
		"""Creating a new Instance of this class is not allowed


		Raises:
			Exception: if this class is instanciated
		"""
		raise Exception("Creating a new Instance of this class is not allowed")
		pass

	@property
	def LengthUnit(self) -> IUnit:
		"""No Description

		Returns:
			IBaseLinkUnits: 
		"""
		pass

class IBasePolygonInput(IActiveElementInput):

	def __init__(self) -> None:
		"""Creating a new Instance of this class is not allowed


		Raises:
			Exception: if this class is instanciated
		"""
		raise Exception("Creating a new Instance of this class is not allowed")
		pass

	def GetRings(self) -> array():
		"""Gets the rings of the polygon.

		Returns:
			array(): 
		"""
		pass

	def SetRings(self, rings: array()) -> None:
		"""Sets the rings of the polygon.

		Args:
			rings(array()): rings

		Returns:
			None: 
		"""
		pass

class IBasePolygonsInput(IActiveElementsInput):

	def __init__(self) -> None:
		"""Creating a new Instance of this class is not allowed


		Raises:
			Exception: if this class is instanciated
		"""
		raise Exception("Creating a new Instance of this class is not allowed")
		pass

	@overload
	def IBasePolygonsInput(self) -> Dict[int,int]:
		"""Gets ring geometry for all polygons.

		Returns:
			Dict[int,int]: 
		"""
		pass

	@overload
	def IBasePolygonsInput(self, ids: List[int]) -> Dict[int,int]:
		"""No Description

		Args:
			ids(List[int]): ids

		Returns:
			Dict[int,int]: 
		"""
		pass

class IBasePolygonsResults(IElementsResults):

	def __init__(self) -> None:
		"""Creating a new Instance of this class is not allowed


		Raises:
			Exception: if this class is instanciated
		"""
		raise Exception("Creating a new Instance of this class is not allowed")
		pass

class IBasePolygonResults(IElementResults):

	def __init__(self) -> None:
		"""Creating a new Instance of this class is not allowed


		Raises:
			Exception: if this class is instanciated
		"""
		raise Exception("Creating a new Instance of this class is not allowed")
		pass

