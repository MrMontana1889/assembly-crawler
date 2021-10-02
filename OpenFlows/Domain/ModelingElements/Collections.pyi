from typing import TypeVar, List, Generic
from OpenFlows.Domain.ModelingElements import IElementUnits
from OpenFlows.Domain.ModelingElements.Support import IFieldManager

TCollectionType = TypeVar("TCollectionType", ICollection)
TElementType = TypeVar("TElementType", ICollectionElement)
TUnitsType = TypeVar("TUnitsType", IElementUnits)

class ICollectionElements(Generic[TCollectionType, TElementType, TUnitsType]):

	def __init__(self) -> None:
		"""Creating a new Instance of this class is not allowed


		Raises:
			Exception: if this class is instanciated
		"""
		raise Exception("Creating a new Instance of this class is not allowed")
		pass

	def Get(self) -> TCollectionType:
		"""Method Description

		Returns:
			TCollectionType: 
		"""
		pass

	def Set(self, collection: TCollectionType) -> None:
		"""Method Description

		Args:
			collection(TCollectionType): collection

		Returns:
			None: 
		"""
		pass

	def SelectElements(self, sorts: SortContextCollection, filters: FilterContextCollection) -> List[TElementType]:
		"""Method Description

		Args:
			sorts(SortContextCollection): sorts
			filters(FilterContextCollection): filters

		Returns:
			List[TElementType]: 
		"""
		pass

	@property
	def Count(self) -> int:
		"""
		Returns:
			int: No Description
		"""
		pass

	@property
	def Units(self) -> TUnitsType:
		"""
		Returns:
			TUnitsType: No Description
		"""
		pass

class ICollectionElement:

	def __init__(self) -> None:
		"""Creating a new Instance of this class is not allowed


		Raises:
			Exception: if this class is instanciated
		"""
		raise Exception("Creating a new Instance of this class is not allowed")
		pass

class ICollection(IEnumerable[TElementType], IEnumerable):

	def __init__(self) -> None:
		"""Creating a new Instance of this class is not allowed


		Raises:
			Exception: if this class is instanciated
		"""
		raise Exception("Creating a new Instance of this class is not allowed")
		pass

	def Add(self) -> TElementType:
		"""Method Description

		Returns:
			TElementType: 
		"""
		pass

	def RemoveAt(self, index: int) -> None:
		"""Method Description

		Args:
			index(int): index

		Returns:
			None: 
		"""
		pass

	def Remove(self, item: TElementType) -> bool:
		"""Method Description

		Args:
			item(TElementType): item

		Returns:
			bool: 
		"""
		pass

	def Clear(self) -> None:
		"""Method Description

		Returns:
			None: 
		"""
		pass

	@property
	def Item(self) -> TElementType:
		"""
		Returns:
			TElementType: No Description
		"""
		pass

	@property
	def Count(self) -> int:
		"""
		Returns:
			int: No Description
		"""
		pass

	@property
	def Fields(self) -> IFieldManager:
		"""
		Returns:
			IFieldManager: No Description
		"""
		pass

	@Item.setter
	def Item(self, item: int) -> None:
		pass

