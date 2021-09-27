from OpenFlows.ModelingElements import TScenarioOptionsType
from typing import Generic, List, TypeVar, overload
from ModelingElements import IElement, ElementStateType, TNetworkElementType, TNetworkElementTypeEnum, IScenario, IScenarios, TScenarioOptionsUnitsType, ISelectionSet, ISelectionSets
from Components import IModelComponents
from Units import INetworkUnits, IComponentUnits, IUnits
from enum import Enum
from OpenFlows.Domain import ModelingElementType

class IDisposable:
    def Dispose(self) -> None:
        pass

class INetwork(Generic[TNetworkElementType, TNetworkElementTypeEnum], IDisposable):
    def Elements(self, state: ElementStateType = ElementStateType.ALL) -> List[TNetworkElementType]:
        pass

    def ElementType(self, id: int) -> TNetworkElementTypeEnum:
        pass

TNetworkType = TypeVar("TNetworkType", INetwork)
TComponentElementType = TypeVar("TComponentElementType", IElement)
TComponentElementTypeEnum = TypeVar("TComponentElementTypeEnum", Enum)
TModelComponentsType = TypeVar("TModelComponentsType", IModelComponents)
TScenarioManagerType = TypeVar("TScenarioManagerType", IScenarios)
TScenarioType = TypeVar("TScenarioType", IScenario)
TSelectionSetsType = TypeVar("TSelectionSetsType", ISelectionSets)
TSelectionSetType = TypeVar("TSelectionSetType", ISelectionSet)
TSelectionSetNetworkElementType = TypeVar("TSelectionSetNetworkElementType", Enum)
TNetworkUnitsType = TypeVar("TNetworkUnitsType", INetworkUnits)
TComponentUnitsType = TypeVar("TComponentUnitsType", IComponentUnits)

class IModelElementManager:
    def Delete(self, id: int) -> None:
        pass
    def Element(self, id: int) -> IElement:
        pass
    def Exists(self, id: int) -> bool:
        pass
    def IsLink(self, id: int) -> bool:
        pass
    def IsNode(self, id: int) -> bool:
        pass
    def IsPolygon(self, id: int) -> bool:
        pass
    def ModelingElementType(self, id: int) -> ModelingElementType:
        pass
    def NetworkElements(self, label: str, wildCard: bool = False) -> List[IElement]:
        pass

class IModelIOOperations:
    def Close(self) -> None:
        pass
    def Save(self) -> None:
        pass
    def SaveAs(self, filename: str) -> None:
        pass

class IModelUnits(Generic[TNetworkUnitsType, TComponentUnitsType]):
    @property
    def Units(self) -> IUnits[TNetworkUnitsType, TComponentUnitsType]:
        pass

class IModelScenarioManagement(Generic[TScenarioManagerType, TScenarioType]):
    @property
    def Scenarios(self) -> TScenarioManagerType:
        pass

    @property
    def ActiveScenario(self) -> TScenarioType:
        pass

    def RunActiveScenario(self) -> None:
        pass
    @overload
    def SetActiveScenario(self, scenarioID: int) -> None:
        pass
    @overload
    def SetActiveScenario(self, scenario: TScenarioType) -> None:
        pass

class IDomainDataSet:
    pass

class IDomainModel:
    @property
    def DomainDataSet(self) -> IDomainDataSet:
        pass
    def IsQuerySelectionSet(self, id: int) -> bool:
        pass

class IModelSelectionSetManagement(Generic[TSelectionSetsType, TSelectionSetType, TSelectionSetNetworkElementType]):
    @property
    def SelectionSets(self) -> TSelectionSetsType:
        pass

class IModel(Generic[TNetworkType, TModelComponentsType, TScenarioManagerType, TScenarioType, 
    TScenarioOptionsType, TScenarioOptionsUnitsType, TSelectionSetsType, TSelectionSetType, 
    TSelectionSetNetworkElementType, TNetworkElementType, TNetworkElementTypeEnum, TComponentElementType, 
    TComponentElementTypeEnum, TNetworkUnitsType, TComponentUnitsType], IDisposable, IModelIOOperations, IModelElementManager,
    IModelUnits[TNetworkUnitsType, TComponentUnitsType], IModelScenarioManagement[TScenarioManagerType, TScenarioType],
    IDomainModel, IModelSelectionSetManagement[TSelectionSetsType, TSelectionSetType, TSelectionSetNetworkElementType]):
    
    @property
    def Network(self) -> TNetworkType:
        pass

    @property
    def Components(self) -> TModelComponentsType:
        pass

    # ModelInfo

    #UserFieldManager

    def NextNetworkElementLabel(self, t: TNetworkElementTypeEnum) -> str:
        pass