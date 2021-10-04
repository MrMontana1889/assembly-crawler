from typing import Generic, List, TypeVar
from OpenFlows.Domain.ModelingElements import IElement, IModelingElementsBase, TElementManagerType, IElementUnits, IModelingElementBase
from enum import Enum
from OpenFlows.Enumerations import *

TElementType = TypeVar("TElementType", IElement)
TElementTypeEnum = TypeVar("TElementTypeEnum", Enum)
TUnitsType = TypeVar("TUnitsType", IElementUnits)

class IModelComponents(Generic[TElementType, TElementTypeEnum]):

	def __init__(self) -> None:
		"""Creating a new Instance of this class is not allowed


		Raises:
			Exception: if this class is instanciated
		"""
		raise Exception("Creating a new Instance of this class is not allowed")
		pass

	def ElementType(self, id: int) -> TElementTypeEnum:
		"""Gets type of element for the given id.

		Args:
			id(int): id

		Returns:
			TElementTypeEnum: 
		"""
		pass

	def Elements(self) -> List[TElementType]:
		"""Returns a list of all support elements in the model.

		Returns:
			List[TElementType]: 
		"""
		pass

class IComponentElements(Generic[TElementManagerType, TElementType, TUnitsType, TElementTypeEnum], IModelingElementsBase[TElementManagerType, TElementType, TElementTypeEnum]):

	def __init__(self) -> None:
		"""Creating a new Instance of this class is not allowed


		Raises:
			Exception: if this class is instanciated
		"""
		raise Exception("Creating a new Instance of this class is not allowed")
		pass

class IComponentElement(Generic[TElementManagerType, TElementType, TUnitsType, TElementTypeEnum], IModelingElementBase[TElementManagerType, TElementType, TElementTypeEnum]):

	def __init__(self) -> None:
		"""Creating a new Instance of this class is not allowed


		Raises:
			Exception: if this class is instanciated
		"""
		raise Exception("Creating a new Instance of this class is not allowed")
		pass

	@property
	def Units(self) -> TUnitsType:
		"""No Description

		Returns:
			IComponentElement: 
		"""
		pass

