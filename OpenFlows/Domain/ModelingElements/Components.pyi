from typing import TypeVar, List, Generic
from OpenFlows.Domain.ModelingElements import TElementManagerType, IElementManager, IElement

TElementType = TypeVar("TElementType", IElement)
TElementTypeEnum = TypeVar("TElementTypeEnum", Enum)

class IModelComponents(Generic[TElementType, TElementTypeEnum]):

	def __init__(self) -> None:
		"""Creating a new Instance of this class is not allowed


		Raises:
			Exception: if this class is instanciated
		"""
		raise Exception("Creating a new Instance of this class is not allowed")
		pass

	def ElementType(self, id: int) -> TElementTypeEnum:
		"""Method Description

		Args:
			id(int): id

		Returns:
			TElementTypeEnum: 
		"""
		pass

	def Elements(self) -> List[TElementType]:
		"""Method Description

		Returns:
			List[TElementType]: 
		"""
		pass

class IComponentElements(IModelingElementsBase[TElementManagerType, TElementType, TElementTypeEnum], IElements[TElementType], IElementManager):

	def __init__(self) -> None:
		"""Creating a new Instance of this class is not allowed


		Raises:
			Exception: if this class is instanciated
		"""
		raise Exception("Creating a new Instance of this class is not allowed")
		pass

class IComponentElement(IModelingElementBase[TElementManagerType, TElementType, TElementTypeEnum], IElement, IEditLabeled, ILabeled):

	def __init__(self) -> None:
		"""Creating a new Instance of this class is not allowed


		Raises:
			Exception: if this class is instanciated
		"""
		raise Exception("Creating a new Instance of this class is not allowed")
		pass

	@property
	def Units(self) -> TUnitsType:
		"""
		Returns:
			TUnitsType: No Description
		"""
		pass

