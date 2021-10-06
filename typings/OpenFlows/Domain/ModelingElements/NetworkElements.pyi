from enum import Enum
from array import array
from OpenFlows.Domain.ModelingElements import IModelingElementBase, TElementManagerType, TElementType, TElementTypeEnum, IElementUnits, IElementInput, IElementResults, IElementsInput, IElementsResults, IModelingElementsBase, IElement, IGeometryUnits
from typing import Generic, List, overload, Dict, TypeVar
from OpenFlows.Domain.ModelingElements.Support import IFieldManager
from OpenFlows.Units import IUnit

TUnitsType = TypeVar("TUnitsType", IElementUnits)
TElementInputType = TypeVar("TElementInputType", IElementInput)
TElementResultsType = TypeVar("TElementResultsType", IElementResults)
TElementsInputType = TypeVar("TElementsInputType", IElementsInput)
TElementsResultsType = TypeVar("TElementsResultsType", IElementsResults)

class ElementStateType(Enum):
	All = 0
	Active = 1
	Inactive = 2

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

	def Elements(self, state: ElementStateType) -> List[TElementType]:
		"""No Description

		Args:
			state(ElementStateType): state

		Returns:
			List[TElementType]: 
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
	def IsActives(self) -> Dict[int,int]:
		"""No Description

		Returns:
			Dict[int,int]: 
		"""
		pass

	@overload
	def IsActives(self, ids: List[int]) -> Dict[int,int]:
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
		"""No Description

		Returns:
			GeometryPoint: 
		"""
		pass

	def SetPoint(self, point: GeometryPoint) -> None:
		"""No Description

		Args:
			point(GeometryPoint): point

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
	def Geometries(self) -> Dict[int,int]:
		"""No Description

		Returns:
			Dict[int,int]: 
		"""
		pass

	@overload
	def Geometries(self, ids: List[int]) -> Dict[int,int]:
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
		"""No Description

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
	def Geometries(self) -> Dict[int,int]:
		"""No Description

		Returns:
			Dict[int,int]: 
		"""
		pass

	@overload
	def Geometries(self, ids: List[int]) -> Dict[int,int]:
		"""No Description

		Args:
			ids(List[int]): ids

		Returns:
			Dict[int,int]: 
		"""
		pass

	@overload
	def StartNodes(self) -> Dict[int,int]:
		"""No Description

		Returns:
			Dict[int,int]: 
		"""
		pass

	@overload
	def StartNodes(self, ids: List[int]) -> Dict[int,int]:
		"""No Description

		Args:
			ids(List[int]): ids

		Returns:
			Dict[int,int]: 
		"""
		pass

	@overload
	def StopNodes(self) -> Dict[int,int]:
		"""No Description

		Returns:
			Dict[int,int]: 
		"""
		pass

	@overload
	def StopNodes(self, ids: List[int]) -> Dict[int,int]:
		"""No Description

		Args:
			ids(List[int]): ids

		Returns:
			Dict[int,int]: 
		"""
		pass

	@overload
	def IsUserDefinedLengths(self) -> Dict[int,int]:
		"""No Description

		Returns:
			Dict[int,int]: 
		"""
		pass

	@overload
	def IsUserDefinedLengths(self, ids: List[int]) -> Dict[int,int]:
		"""No Description

		Args:
			ids(List[int]): ids

		Returns:
			Dict[int,int]: 
		"""
		pass

	@overload
	def Lengths(self) -> Dict[int,int]:
		"""No Description

		Returns:
			Dict[int,int]: 
		"""
		pass

	@overload
	def Lengths(self, ids: List[int]) -> Dict[int,int]:
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
		"""No Description

		Returns:
			array(): 
		"""
		pass

	def SetRings(self, rings: array()) -> None:
		"""No Description

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
	def Geometries(self) -> Dict[int,int]:
		"""No Description

		Returns:
			Dict[int,int]: 
		"""
		pass

	@overload
	def Geometries(self, ids: List[int]) -> Dict[int,int]:
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

