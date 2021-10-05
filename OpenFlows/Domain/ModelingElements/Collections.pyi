from typing import Generic, List, Iterator, TypeVar
from OpenFlows.Domain.ModelingElements import IElementUnits
from OpenFlows.Domain.ModelingElements.Support import IFieldManager
from OpenFlows.Enumerations import *

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
		"""Returns the collection data.

		Returns:
			TCollectionType: 
		"""
		pass

	def Set(self, collection: TCollectionType) -> None:
		"""No Description

		Args:
			collection(TCollectionType): collection

		Returns:
			None: 
		"""
		pass

	def SelectElements(self, sorts: SortContextCollection, filters: FilterContextCollection) -> List[TElementType]:
		"""Applies a sort and/or filter against the collection and returns the matching elements.

		Args:
			sorts(SortContextCollection): Sorts on a field in either ascending or descending order
			filters(FilterContextCollection): Filters the collection on one or more fields

		Returns:
			List[TElementType]:  containing matching elements for the provided criteria.
		"""
		pass

	@property
	def Count(self) -> int:
		"""No Description

		Returns:
			ICollectionElements: 
		"""
		pass

	@property
	def Units(self) -> TUnitsType:
		"""No Description

		Returns:
			ICollectionElements: 
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

class ICollection(Generic[TElementType], IEnumerable[TElementType]):

	def __init__(self) -> None:
		"""Creating a new Instance of this class is not allowed


		Raises:
			Exception: if this class is instanciated
		"""
		raise Exception("Creating a new Instance of this class is not allowed")
		pass

	def Add(self) -> TElementType:
		"""Creates a new item, adds it to the collection and returns the object.

		Returns:
			TElementType: 
		"""
		pass

	def RemoveAt(self, index: int) -> None:
		"""Removes the System.Collections.Generic.IList`1 item at the specified index.

		Args:
			index(int): The zero-based index of the item to remove.

		Returns:
			None: 
		"""
		pass

	def Remove(self, item: TElementType) -> bool:
		"""No Description

		Args:
			item(TElementType): item

		Returns:
			bool: 
		"""
		pass

	def Clear(self) -> None:
		"""Removes all items from the collection.

		Returns:
			None: 
		"""
		pass

	@property
	def Item(self) -> TElementType:
		"""No Description

		Returns:
			ICollection: 
		"""
		pass

	@property
	def Count(self) -> int:
		"""No Description

		Returns:
			ICollection: 
		"""
		pass

	@property
	def Fields(self) -> IFieldManager:
		"""No Description

		Returns:
			ICollection: 
		"""
		pass

	@Item.setter
	def Item(self, item: int) -> None:
		pass

