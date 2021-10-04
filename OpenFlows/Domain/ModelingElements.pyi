from typing import List, Generic, overload, TypeVar
from enum import Enum
from OpenFlows.Units import IUnit
from datetime import datetime
from array import array
from OpenFlows.Enumerations import *
from OpenFlows.Domain.ModelingElements.Support import IFieldManager

TElementType = TypeVar("TElementType", IElement)
TElementManagerType = TypeVar("TElementManagerType", IModelingElementsBase)
TElementTypeEnum = TypeVar("TElementTypeEnum", Enum)
TUnitsType = TypeVar("TUnitsType", IElementUnits)
TScenarioOptionsType = TypeVar("TScenarioOptionsType", IScenarioOptions)
TScenarioOptionsUnitsType = TypeVar("TScenarioOptionsUnitsType", IElementUnits)
TNetworkElementType = TypeVar("TNetworkElementType", IElement)

class IElementManager:

	def __init__(self) -> None:
		"""Creating a new Instance of this class is not allowed


		Raises:
			Exception: if this class is instanciated
		"""
		raise Exception("Creating a new Instance of this class is not allowed")
		pass

	def ElementIDs(self) -> List[int]:
		"""Method Description

		Returns:
			List[int]: 
		"""
		pass

	def Exists(self, id: int) -> bool:
		"""Method Description

		Args:
			id(int): id

		Returns:
			bool: 
		"""
		pass

	@property
	def Count(self) -> int:
		"""
		Returns:
			int: No Description
		"""
		pass

class IElements(Generic[TElementType], IElementManager):

	def __init__(self) -> None:
		"""Creating a new Instance of this class is not allowed


		Raises:
			Exception: if this class is instanciated
		"""
		raise Exception("Creating a new Instance of this class is not allowed")
		pass

	def Elements(self) -> List[TElementType]:
		"""Method Description

		Returns:
			List[TElementType]: 
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

class IElement(IEditLabeled):

	def __init__(self) -> None:
		"""Creating a new Instance of this class is not allowed


		Raises:
			Exception: if this class is instanciated
		"""
		raise Exception("Creating a new Instance of this class is not allowed")
		pass

	@property
	def Id(self) -> int:
		"""
		Returns:
			int: No Description
		"""
		pass

	@property
	def Notes(self) -> str:
		"""
		Returns:
			str: No Description
		"""
		pass

	@property
	def ModelElementType(self) -> ModelElementType:
		"""
		Returns:
			ModelElementType: No Description
		"""
		pass

	@Notes.setter
	def Notes(self, notes: str) -> None:
		pass

class IElementUnits:

	def __init__(self) -> None:
		"""Creating a new Instance of this class is not allowed


		Raises:
			Exception: if this class is instanciated
		"""
		raise Exception("Creating a new Instance of this class is not allowed")
		pass

class IElementInput:

	def __init__(self) -> None:
		"""Creating a new Instance of this class is not allowed


		Raises:
			Exception: if this class is instanciated
		"""
		raise Exception("Creating a new Instance of this class is not allowed")
		pass

	@property
	def InputFields(self) -> IFieldManager:
		"""
		Returns:
			IFieldManager: No Description
		"""
		pass

class IElementsInput:

	def __init__(self) -> None:
		"""Creating a new Instance of this class is not allowed


		Raises:
			Exception: if this class is instanciated
		"""
		raise Exception("Creating a new Instance of this class is not allowed")
		pass

class IElementResults:

	def __init__(self) -> None:
		"""Creating a new Instance of this class is not allowed


		Raises:
			Exception: if this class is instanciated
		"""
		raise Exception("Creating a new Instance of this class is not allowed")
		pass

	@property
	def ResultFields(self) -> IFieldManager:
		"""
		Returns:
			IFieldManager: No Description
		"""
		pass

class IElementsResults:

	def __init__(self) -> None:
		"""Creating a new Instance of this class is not allowed


		Raises:
			Exception: if this class is instanciated
		"""
		raise Exception("Creating a new Instance of this class is not allowed")
		pass

class IModelingElementBase(Generic[TElementManagerType, TElementType, TElementTypeEnum], IElement):

	def __init__(self) -> None:
		"""Creating a new Instance of this class is not allowed


		Raises:
			Exception: if this class is instanciated
		"""
		raise Exception("Creating a new Instance of this class is not allowed")
		pass

	def Delete(self) -> None:
		"""Method Description

		Returns:
			None: 
		"""
		pass

	@property
	def Manager(self) -> TElementManagerType:
		"""
		Returns:
			TElementManagerType: No Description
		"""
		pass

	@property
	def ElementType(self) -> TElementTypeEnum:
		"""
		Returns:
			TElementTypeEnum: No Description
		"""
		pass

class IModelingElementsBase(Generic[TElementManagerType, TElementType, TElementTypeEnum], IElements[TElementType]):

	def __init__(self) -> None:
		"""Creating a new Instance of this class is not allowed


		Raises:
			Exception: if this class is instanciated
		"""
		raise Exception("Creating a new Instance of this class is not allowed")
		pass

	@overload
	def IModelingElementsBase(self, id: int) -> TElementType:
		"""Method Description

		Args:
			id(int): id

		Returns:
			TElementType: 
		"""
		pass

	@overload
	def IModelingElementsBase(self, label: str) -> TElementType:
		"""Method Description

		Args:
			label(str): label

		Returns:
			TElementType: 
		"""
		pass

	def Create(self) -> TElementType:
		"""Method Description

		Returns:
			TElementType: 
		"""
		pass

	def Elements(self, label: str) -> List[TElementType]:
		"""Method Description

		Args:
			label(str): label

		Returns:
			List[TElementType]: 
		"""
		pass

	@property
	def ElementType(self) -> TElementTypeEnum:
		"""
		Returns:
			TElementTypeEnum: No Description
		"""
		pass

	@property
	def InputFields(self) -> IFieldManager:
		"""
		Returns:
			IFieldManager: No Description
		"""
		pass

class IGeometryUnits(IElementUnits):

	def __init__(self) -> None:
		"""Creating a new Instance of this class is not allowed


		Raises:
			Exception: if this class is instanciated
		"""
		raise Exception("Creating a new Instance of this class is not allowed")
		pass

	@property
	def GeometryUnit(self) -> IUnit:
		"""
		Returns:
			IUnit: No Description
		"""
		pass

class IScenarioOptions(Generic[TUnitsType], IElement):

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

class IScenarios(Generic[TElementManagerType, TElementType, TScenarioOptionsType, TScenarioOptionsUnitsType], IModelingElementsBase[TElementManagerType, TElementType, ModelingElementTypes]):

	def __init__(self) -> None:
		"""Creating a new Instance of this class is not allowed


		Raises:
			Exception: if this class is instanciated
		"""
		raise Exception("Creating a new Instance of this class is not allowed")
		pass

	def Create(self, parentID: int) -> TElementType:
		"""Method Description

		Args:
			parentID(int): parentID

		Returns:
			TElementType: 
		"""
		pass

	def ChildrenOfElement(self, parentID: int) -> List[TElementType]:
		"""Method Description

		Args:
			parentID(int): parentID

		Returns:
			List[TElementType]: 
		"""
		pass

	def BaseElements(self) -> List[TElementType]:
		"""Method Description

		Returns:
			List[TElementType]: 
		"""
		pass

	@property
	def ActiveScenario(self) -> TElementType:
		"""
		Returns:
			TElementType: No Description
		"""
		pass

class IScenario(Generic[TElementManagerType, TElementType, TScenarioOptionsType, TScenarioOptionsUnitsType], IModelingElementBase[TElementManagerType, TElementType, ModelingElementTypes]):

	def __init__(self) -> None:
		"""Creating a new Instance of this class is not allowed


		Raises:
			Exception: if this class is instanciated
		"""
		raise Exception("Creating a new Instance of this class is not allowed")
		pass

	def TimeIndexToDateTime(self, timeStepIndex: int) -> datetime:
		"""Method Description

		Args:
			timeStepIndex(int): timeStepIndex

		Returns:
			datetime: 
		"""
		pass

	def TimeStepToDateTime(self, timeStepInSeconds: float) -> datetime:
		"""Method Description

		Args:
			timeStepInSeconds(float): timeStepInSeconds

		Returns:
			datetime: 
		"""
		pass

	def MakeCurrent(self) -> None:
		"""Method Description

		Returns:
			None: 
		"""
		pass

	def Run(self) -> None:
		"""Method Description

		Returns:
			None: 
		"""
		pass

	@property
	def Options(self) -> TScenarioOptionsType:
		"""
		Returns:
			TScenarioOptionsType: No Description
		"""
		pass

	@property
	def TimeStepsInSeconds(self) -> array(float):
		"""
		Returns:
			array(float): No Description
		"""
		pass

	@property
	def HasResults(self) -> bool:
		"""
		Returns:
			bool: No Description
		"""
		pass

	@property
	def ActiveTimeStep(self) -> int:
		"""
		Returns:
			int: No Description
		"""
		pass

	@property
	def ParentScenario(self) -> IScenario:
		"""
		Returns:
			IScenario: No Description
		"""
		pass

	@ActiveTimeStep.setter
	def ActiveTimeStep(self, activetimestep: int) -> None:
		pass

	@ParentScenario.setter
	def ParentScenario(self, parentscenario: IScenario) -> None:
		pass

class ISelectionSet(Generic[TElementManagerType, TElementType, TNetworkElementType], IModelingElementBase[TElementManagerType, TElementType, ModelingElementTypes]):

	def __init__(self) -> None:
		"""Creating a new Instance of this class is not allowed


		Raises:
			Exception: if this class is instanciated
		"""
		raise Exception("Creating a new Instance of this class is not allowed")
		pass

	@overload
	def ISelectionSet(self, ids: List[int]) -> None:
		"""Method Description

		Args:
			ids(List[int]): ids

		Returns:
			None: 
		"""
		pass

	@overload
	def ISelectionSet(self, elements: List[TNetworkElementType]) -> None:
		"""Method Description

		Args:
			elements(List[TNetworkElementType]): elements

		Returns:
			None: 
		"""
		pass

	def Get(self) -> List[int]:
		"""Method Description

		Returns:
			List[int]: 
		"""
		pass

	def Elements(self) -> List[TNetworkElementType]:
		"""Method Description

		Returns:
			List[TNetworkElementType]: 
		"""
		pass

	@property
	def Count(self) -> int:
		"""
		Returns:
			int: No Description
		"""
		pass

class ISelectionSets(Generic[TElementManagerType, TElementType, TNetworkElementType], IModelingElementsBase[TElementManagerType, TElementType, ModelingElementTypes]):

	def __init__(self) -> None:
		"""Creating a new Instance of this class is not allowed


		Raises:
			Exception: if this class is instanciated
		"""
		raise Exception("Creating a new Instance of this class is not allowed")
		pass

