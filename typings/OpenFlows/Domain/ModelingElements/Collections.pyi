from OpenFlows.Domain.ModelingElements import TUnitsType, IElementUnits
from typing import List, Generic, Iterator, TypeVar
from Haestad.Support.Support import SortContextCollection, FilterContextCollection
from OpenFlows.Domain.ModelingElements.Support import IFieldManager

TCollectionType = TypeVar("TCollectionType")
TElementType = TypeVar("TElementType")

class ICollectionElements(Generic[TCollectionType, TElementType, TUnitsType]):

	def __init__(self) -> None:
		"""Creating a new Instance of this class is not allowed


		Raises
		--------
			Exception: if this class is instantiated
		"""
		raise Exception("Creating a new Instance of this class is not allowed")
		pass

	def Get(self) -> TCollectionType:
		"""No Description

		Returns
		--------
			``TCollectionType`` : 
		"""
		pass

	def Set(self, collection: TCollectionType) -> None:
		"""No Description

		Args
		--------
			collection (``TCollectionType``) :  collection

		Returns
		--------
			``None`` : 
		"""
		pass

	def SelectElements(self, sorts: SortContextCollection, filters: FilterContextCollection) -> List[TElementType]:
		"""No Description

		Args
		--------
			sorts (``SortContextCollection``) :  sorts
			filters (``FilterContextCollection``) :  filters

		Returns
		--------
			``List[TElementType]`` : 
		"""
		pass

	@property
	def Count(self) -> int:
		"""No Description

		Returns
		--------
			``ICollectionElements`` : 
		"""
		pass

	@property
	def Units(self) -> TUnitsType:
		"""No Description

		Returns
		--------
			``ICollectionElements`` : 
		"""
		pass

class IResultCollectionElements(Generic[TCollectionType, TElementType, TUnitsType]):

	def __init__(self) -> None:
		"""Creating a new Instance of this class is not allowed


		Raises
		--------
			Exception: if this class is instantiated
		"""
		raise Exception("Creating a new Instance of this class is not allowed")
		pass

	def Get(self) -> TCollectionType:
		"""No Description

		Returns
		--------
			``TCollectionType`` : 
		"""
		pass

	@property
	def Units(self) -> TUnitsType:
		"""No Description

		Returns
		--------
			``IResultCollectionElements`` : 
		"""
		pass

class ICollectionElement:

	def __init__(self) -> None:
		"""Creating a new Instance of this class is not allowed


		Raises
		--------
			Exception: if this class is instantiated
		"""
		raise Exception("Creating a new Instance of this class is not allowed")
		pass

class ICollection(Generic[TElementType], Iterator[TElementType]):

	def __init__(self) -> None:
		"""Creating a new Instance of this class is not allowed


		Raises
		--------
			Exception: if this class is instantiated
		"""
		raise Exception("Creating a new Instance of this class is not allowed")
		pass

	def Add(self) -> TElementType:
		"""No Description

		Returns
		--------
			``TElementType`` : 
		"""
		pass

	def RemoveAt(self, index: int) -> None:
		"""No Description

		Args
		--------
			index (``int``) :  index

		Returns
		--------
			``None`` : 
		"""
		pass

	def Remove(self, item: TElementType) -> bool:
		"""No Description

		Args
		--------
			item (``TElementType``) :  item

		Returns
		--------
			``bool`` : 
		"""
		pass

	def Clear(self) -> None:
		"""No Description

		Returns
		--------
			``None`` : 
		"""
		pass

	@property
	def Item(self) -> TElementType:
		"""No Description

		Returns
		--------
			``ICollection`` : 
		"""
		pass

	@Item.setter
	def Item(self, item: TElementType) -> None:
		pass

	@property
	def Count(self) -> int:
		"""No Description

		Returns
		--------
			``ICollection`` : 
		"""
		pass

	@property
	def Fields(self) -> IFieldManager:
		"""No Description

		Returns
		--------
			``ICollection`` : 
		"""
		pass

class IResultCollection(Generic[TElementType], Iterator[TElementType]):

	def __init__(self) -> None:
		"""Creating a new Instance of this class is not allowed


		Raises
		--------
			Exception: if this class is instantiated
		"""
		raise Exception("Creating a new Instance of this class is not allowed")
		pass

	def AsReadOnly(self) -> ReadOnlyCollection:
		"""No Description

		Returns
		--------
			``ReadOnlyCollection`` : 
		"""
		pass

	@property
	def Item(self) -> TElementType:
		"""No Description

		Returns
		--------
			``IResultCollection`` : 
		"""
		pass

	@property
	def Count(self) -> int:
		"""No Description

		Returns
		--------
			``IResultCollection`` : 
		"""
		pass

