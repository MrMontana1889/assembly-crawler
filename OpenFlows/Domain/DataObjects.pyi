from datetime import datetime
from typing import TypeVar, Generic, overload, List
from OpenFlows.Domain.ModelingElements import IModelingElementsBase, IModelingElementBase, IElement, ISelectionSets, ISelectionSet, IScenarios, IScenario, IScenarioOptions, IElementUnits
from enum import Enum
from OpenFlows.Units import IModelUnits, TNetworkUnitsType, TComponentUnitsType, INetworkUnits, IComponentUnits
from OpenFlows.Domain.ModelingElements.Components import IModelComponents
from OpenFlows.Domain.ModelingElements.Support import IUserFieldManager

TScenarioManagerType = TypeVar("TScenarioManagerType", IModelingElementsBase)
TScenarioType = TypeVar("TScenarioType", IModelingElementBase)
TNetworkElementType = TypeVar("TNetworkElementType", IElement)
TNetworkElementTypeEnum = TypeVar("TNetworkElementTypeEnum", Enum)
TSelectionSetsType = TypeVar("TSelectionSetsType", ISelectionSets)
TSelectionSetElementType = TypeVar("TSelectionSetElementType", ISelectionSet)
TSelectionSetNetworkElementType = TypeVar("TSelectionSetNetworkElementType", IElement)
TNetworkType = TypeVar("TNetworkType", INetwork)
TModelComponentsType = TypeVar("TModelComponentsType", IModelComponents)
TScenarioOptionsType = TypeVar("TScenarioOptionsType", IScenarioOptions)
TScenarioOptionsUnitsType = TypeVar("TScenarioOptionsUnitsType", IElementUnits)
TComponentElementType = TypeVar("TComponentElementType", IElement)
TComponentElementTypeEnum = TypeVar("TComponentElementTypeEnum", Enum)
TModelType = TypeVar("TModelType", IModel)

class IDomainModel:

	def __init__(self) -> None:
		"""Creating a new Instance of this class is not allowed


		Raises:
			Exception: if this class is instanciated
		"""
		raise Exception("Creating a new Instance of this class is not allowed")
		pass

	def IsQuerySelectionSet(self, id: int) -> bool:
		"""Method Description

		Args:
			id(int): id

		Returns:
			bool: 
		"""
		pass

	@property
	def DomainDataSet(self) -> IDomainDataSet:
		"""
		Returns:
			IDomainDataSet: No Description
		"""
		pass

class IModelInfo:

	def __init__(self) -> None:
		"""Creating a new Instance of this class is not allowed


		Raises:
			Exception: if this class is instanciated
		"""
		raise Exception("Creating a new Instance of this class is not allowed")
		pass

	@property
	def Filename(self) -> str:
		"""
		Returns:
			str: No Description
		"""
		pass

	@property
	def Date(self) -> datetime:
		"""
		Returns:
			datetime: No Description
		"""
		pass

	@property
	def Title(self) -> str:
		"""
		Returns:
			str: No Description
		"""
		pass

	@property
	def Company(self) -> str:
		"""
		Returns:
			str: No Description
		"""
		pass

	@property
	def Engineer(self) -> str:
		"""
		Returns:
			str: No Description
		"""
		pass

	@property
	def Notes(self) -> str:
		"""
		Returns:
			str: No Description
		"""
		pass

class IModelIOOperations:

	def __init__(self) -> None:
		"""Creating a new Instance of this class is not allowed


		Raises:
			Exception: if this class is instanciated
		"""
		raise Exception("Creating a new Instance of this class is not allowed")
		pass

	def Save(self) -> None:
		"""Method Description

		Returns:
			None: 
		"""
		pass

	def SaveAs(self, filename: str) -> None:
		"""Method Description

		Args:
			filename(str): filename

		Returns:
			None: 
		"""
		pass

	def Close(self) -> None:
		"""Method Description

		Returns:
			None: 
		"""
		pass

class IModelScenarioManagement(Generic[TScenarioManagerType, TScenarioType]):

	def __init__(self) -> None:
		"""Creating a new Instance of this class is not allowed


		Raises:
			Exception: if this class is instanciated
		"""
		raise Exception("Creating a new Instance of this class is not allowed")
		pass

	@overload
	def IModelScenarioManagement(self, scenarioID: int) -> None:
		"""Method Description

		Args:
			scenarioID(int): scenarioID

		Returns:
			None: 
		"""
		pass

	@overload
	def IModelScenarioManagement(self, scenario: TScenarioType) -> None:
		"""Method Description

		Args:
			scenario(TScenarioType): scenario

		Returns:
			None: 
		"""
		pass

	def RunActiveScenario(self) -> None:
		"""Method Description

		Returns:
			None: 
		"""
		pass

	@property
	def Scenarios(self) -> TScenarioManagerType:
		"""
		Returns:
			TScenarioManagerType: No Description
		"""
		pass

	@property
	def ActiveScenario(self) -> TScenarioType:
		"""
		Returns:
			TScenarioType: No Description
		"""
		pass

class INetwork(Generic[TNetworkElementType, TNetworkElementTypeEnum]):

	def __init__(self) -> None:
		"""Creating a new Instance of this class is not allowed


		Raises:
			Exception: if this class is instanciated
		"""
		raise Exception("Creating a new Instance of this class is not allowed")
		pass

	def ElementType(self, id: int) -> TNetworkElementTypeEnum:
		"""Method Description

		Args:
			id(int): id

		Returns:
			TNetworkElementTypeEnum: 
		"""
		pass

	def Elements(self, state: ElementStateType) -> List[TNetworkElementType]:
		"""Method Description

		Args:
			state(ElementStateType): state

		Returns:
			List[TNetworkElementType]: 
		"""
		pass

class IModelElementManager:

	def __init__(self) -> None:
		"""Creating a new Instance of this class is not allowed


		Raises:
			Exception: if this class is instanciated
		"""
		raise Exception("Creating a new Instance of this class is not allowed")
		pass

	def Element(self, id: int) -> IElement:
		"""Method Description

		Args:
			id(int): id

		Returns:
			IElement: 
		"""
		pass

	def NetworkElements(self, label: str, useWildcard: bool) -> List[IElement]:
		"""Method Description

		Args:
			label(str): label
			useWildcard(bool): useWildcard

		Returns:
			List[IElement]: 
		"""
		pass

	def ModelElementType(self, id: int) -> ModelElementType:
		"""Method Description

		Args:
			id(int): id

		Returns:
			ModelElementType: 
		"""
		pass

	def Delete(self, id: int) -> bool:
		"""Method Description

		Args:
			id(int): id

		Returns:
			bool: 
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

	def IsLink(self, id: int) -> bool:
		"""Method Description

		Args:
			id(int): id

		Returns:
			bool: 
		"""
		pass

	def IsNode(self, id: int) -> bool:
		"""Method Description

		Args:
			id(int): id

		Returns:
			bool: 
		"""
		pass

	def IsPolygon(self, id: int) -> bool:
		"""Method Description

		Args:
			id(int): id

		Returns:
			bool: 
		"""
		pass

	def NextNetworkElementLabel(self, domainElementType: int) -> str:
		"""Method Description

		Args:
			domainElementType(int): domainElementType

		Returns:
			str: 
		"""
		pass

class IModelSelectionSetManagement(Generic[TSelectionSetsType, TSelectionSetElementType, TSelectionSetNetworkElementType]):

	def __init__(self) -> None:
		"""Creating a new Instance of this class is not allowed


		Raises:
			Exception: if this class is instanciated
		"""
		raise Exception("Creating a new Instance of this class is not allowed")
		pass

	@property
	def SelectionSets(self) -> TSelectionSetsType:
		"""
		Returns:
			TSelectionSetsType: No Description
		"""
		pass

class IModel(Generic[TNetworkType, TModelComponentsType, TScenarioManagerType, TScenarioType, TScenarioOptionsType, TScenarioOptionsUnitsType, TSelectionSetsType, TSelectionSetElementType, TSelectionSetNetworkElementType, TNetworkElementType, TNetworkElementTypeEnum, TComponentElementType, TComponentElementTypeEnum, TNetworkUnitsType, TComponentUnitsType], IModelElementManager, IModelIOOperations, IModelUnits[TNetworkUnitsType, TComponentUnitsType], IModelScenarioManagement[TScenarioManagerType, TScenarioType], IDomainModel, IModelSelectionSetManagement[TSelectionSetsType, TSelectionSetElementType, TSelectionSetNetworkElementType]):

	def __init__(self) -> None:
		"""Creating a new Instance of this class is not allowed


		Raises:
			Exception: if this class is instanciated
		"""
		raise Exception("Creating a new Instance of this class is not allowed")
		pass

	def NextNetworkElementLabel(self, domainElementType: TNetworkElementTypeEnum) -> str:
		"""Method Description

		Args:
			domainElementType(TNetworkElementTypeEnum): domainElementType

		Returns:
			str: 
		"""
		pass

	@property
	def Network(self) -> TNetworkType:
		"""
		Returns:
			TNetworkType: No Description
		"""
		pass

	@property
	def Components(self) -> TModelComponentsType:
		"""
		Returns:
			TModelComponentsType: No Description
		"""
		pass

	@property
	def ModelInfo(self) -> IModelInfo:
		"""
		Returns:
			IModelInfo: No Description
		"""
		pass

	@property
	def UserFieldManager(self) -> IUserFieldManager:
		"""
		Returns:
			IUserFieldManager: No Description
		"""
		pass

class IOpenFlows(Generic[TNetworkType, TModelType, TModelComponentsType, TScenarioManagerType, TScenarioType, TScenarioOptionsType, TScenarioOptionsUnitsType, TSelectionSetsType, TSelectionSetElementType, TSelectionSetNetworkElementType, TNetworkElementType, TNetworkElementTypeEnum, TComponentElementType, TComponentElementTypeEnum, TNetworkUnitsType, TComponentUnitsType]):

	def __init__(self) -> None:
		"""Creating a new Instance of this class is not allowed


		Raises:
			Exception: if this class is instanciated
		"""
		raise Exception("Creating a new Instance of this class is not allowed")
		pass

	@overload
	def IOpenFlows(self, filename: str, openInPlace: bool) -> TModelType:
		"""Method Description

		Args:
			filename(str): filename
			openInPlace(bool): openInPlace

		Returns:
			TModelType: 
		"""
		pass

	@overload
	def IOpenFlows(self, project: IProject) -> TModelType:
		"""Method Description

		Args:
			project(IProject): project

		Returns:
			TModelType: 
		"""
		pass

