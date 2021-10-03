from typing import Generic, TypeVar, List, overload, Dict
from OpenFlows.Domain.ModelingElements import IModelingElementBase, TElementManagerType, TElementType, TElementTypeEnum, IElementUnits, IElementInput, IElementResults, IElementsInput, IElementsResults, IModelingElementsBase, IElement, IGeometryUnits
from enum import Enum
from OpenFlows.Domain.ModelingElements.Support import IFieldManager
from OpenFlows.Units import IUnit

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
		"""
		Returns:
			str: No Description
		"""
		pass

	@property
	def Input(self) -> TElementInputType:
		"""
		Returns:
			TElementInputType: No Description
		"""
		pass

	@property
	def Results(self) -> TElementResultsType:
		"""
		Returns:
			TElementResultsType: No Description
		"""
		pass

	@property
	def Units(self) -> TUnitsType:
		"""
		Returns:
			TUnitsType: No Description
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
		"""Method Description

		Args:
			state(ElementStateType): state

		Returns:
			List[TElementType]: 
		"""
		pass

	@property
	def Results(self) -> TElementsResultsType:
		"""
		Returns:
			TElementsResultsType: No Description
		"""
		pass

	@property
	def Input(self) -> TElementsInputType:
		"""
		Returns:
			TElementsInputType: No Description
		"""
		pass

	@property
	def ResultFields(self) -> IFieldManager:
		"""
		Returns:
			IFieldManager: No Description
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
		"""
		Returns:
			bool: No Description
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
		"""Method Description

		Returns:
			Dict[int,int]: 
		"""
		pass

	@overload
	def IActiveElementsInput(self, ids: List[int]) -> Dict[int,int]:
		"""Method Description

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
		"""Method Description

		Returns:
			GeometryPoint: 
		"""
		pass

	def SetPoint(self, point: GeometryPoint) -> None:
		"""Method Description

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
	def IPointNodesInput(self) -> Dict[int,int]:
		"""Method Description

		Returns:
			Dict[int,int]: 
		"""
		pass

	@overload
	def IPointNodesInput(self, ids: List[int]) -> Dict[int,int]:
		"""Method Description

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
		"""Method Description

		Returns:
			List[GeometryPoint]: 
		"""
		pass

	def SetPoints(self, points: List[GeometryPoint]) -> None:
		"""Method Description

		Args:
			points(List[GeometryPoint]): points

		Returns:
			None: 
		"""
		pass

	@property
	def StartNode(self) -> IElement:
		"""
		Returns:
			IElement: No Description
		"""
		pass

	@property
	def StopNode(self) -> IElement:
		"""
		Returns:
			IElement: No Description
		"""
		pass

	@property
	def IsUserDefinedLength(self) -> bool:
		"""
		Returns:
			bool: No Description
		"""
		pass

	@property
	def Length(self) -> float:
		"""
		Returns:
			float: No Description
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
		"""Method Description

		Returns:
			Dict[int,int]: 
		"""
		pass

	@overload
	def IBaseLinksInput(self, ids: List[int]) -> Dict[int,int]:
		"""Method Description

		Args:
			ids(List[int]): ids

		Returns:
			Dict[int,int]: 
		"""
		pass

	@overload
	def IBaseLinksInput(self) -> Dict[int,int]:
		"""Method Description

		Returns:
			Dict[int,int]: 
		"""
		pass

	@overload
	def IBaseLinksInput(self, ids: List[int]) -> Dict[int,int]:
		"""Method Description

		Args:
			ids(List[int]): ids

		Returns:
			Dict[int,int]: 
		"""
		pass

	@overload
	def IBaseLinksInput(self) -> Dict[int,int]:
		"""Method Description

		Returns:
			Dict[int,int]: 
		"""
		pass

	@overload
	def IBaseLinksInput(self, ids: List[int]) -> Dict[int,int]:
		"""Method Description

		Args:
			ids(List[int]): ids

		Returns:
			Dict[int,int]: 
		"""
		pass

	@overload
	def IBaseLinksInput(self) -> Dict[int,int]:
		"""Method Description

		Returns:
			Dict[int,int]: 
		"""
		pass

	@overload
	def IBaseLinksInput(self, ids: List[int]) -> Dict[int,int]:
		"""Method Description

		Args:
			ids(List[int]): ids

		Returns:
			Dict[int,int]: 
		"""
		pass

	@overload
	def IBaseLinksInput(self) -> Dict[int,int]:
		"""Method Description

		Returns:
			Dict[int,int]: 
		"""
		pass

	@overload
	def IBaseLinksInput(self, ids: List[int]) -> Dict[int,int]:
		"""Method Description

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
		"""
		Returns:
			IUnit: No Description
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

	def GetRings(self) -> GeometryPoint[][]:
		"""Method Description

		Returns:
			GeometryPoint[][]: 
		"""
		pass

	def SetRings(self, rings: GeometryPoint[][]) -> None:
		"""Method Description

		Args:
			rings(GeometryPoint[][]): rings

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
		"""Method Description

		Returns:
			Dict[int,int]: 
		"""
		pass

	@overload
	def IBasePolygonsInput(self, ids: List[int]) -> Dict[int,int]:
		"""Method Description

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

