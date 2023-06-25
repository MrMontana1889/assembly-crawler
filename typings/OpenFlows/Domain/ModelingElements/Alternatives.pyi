from OpenFlows.Domain.ModelingElements import IModelingElementsBase, IElements, IElement, IElementUnits, IElementInput, IModelingElementBase, IElementManager
from typing import Generic, TypeVar
from enum import Enum
from Haestad.Support.Support import IEditLabeled, ILabeled

TAlternativeManagerType = TypeVar("TAlternativeManagerType")
TAlternativeElementType = TypeVar("TAlternativeElementType")
TAlternativeTypeEnum = TypeVar("TAlternativeTypeEnum")
TAlternativeUnitsType = TypeVar("TAlternativeUnitsType")
TSystemAlternativeType = TypeVar("TSystemAlternativeType")

class IAlternativeElements(Generic[TAlternativeManagerType, TAlternativeElementType, TAlternativeTypeEnum, TAlternativeUnitsType, TSystemAlternativeType], IModelingElementsBase[TAlternativeManagerType, TAlternativeElementType, TAlternativeTypeEnum]):

	def __init__(self) -> None:
		"""Creating a new Instance of this class is not allowed


		Raises
		--------
			Exception: if this class is instantiated
		"""
		raise Exception("Creating a new Instance of this class is not allowed")
		pass

class IAlternativeElement(Generic[TAlternativeManagerType, TAlternativeElementType, TAlternativeTypeEnum, TAlternativeUnitsType, TSystemAlternativeType], IModelingElementBase[TAlternativeManagerType, TAlternativeElementType, TAlternativeTypeEnum]):

	def __init__(self) -> None:
		"""Creating a new Instance of this class is not allowed


		Raises
		--------
			Exception: if this class is instantiated
		"""
		raise Exception("Creating a new Instance of this class is not allowed")
		pass

	@property
	def AlternativeType(self) -> TAlternativeTypeEnum:
		"""No Description

		Returns
		--------
			``IAlternativeElement`` : 
		"""
		pass

	@property
	def System(self) -> TSystemAlternativeType:
		"""No Description

		Returns
		--------
			``IAlternativeElement`` : 
		"""
		pass

	@property
	def Units(self) -> TAlternativeUnitsType:
		"""No Description

		Returns
		--------
			``IAlternativeElement`` : 
		"""
		pass

