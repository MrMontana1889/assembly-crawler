from enum import Enum
from OpenFlows.ModelingElements import INetworkElements, INetworkElement, IElement, TElementManagerType, TElementType, TUnitsType, IElementUnits
from OpenFlows.ModelingElements import IElementInput, IElementResults, IElementsInput, IElementsResults
from OpenFlows.ModelingElements import TElementInputType, TElementResultsType, TElementsInputType, TElementsResultsType

class WaterNetworkElementType(Enum):
    SCADAElement = 23
    Lateral = 24
    Tap = 26
    Tank = 52
    Hydrant = 54
    Junction = 55
    Reservoir = 56
    FCV = 60

class IWaterNetworkElement(IElement):
    @property
    def WaterElementType(self) -> WaterNetworkElementType:
        pass

class IWaterNetworkElements(INetworkElements[TElementManagerType, TElementType, TUnitsType, WaterNetworkElementType,
    TElementInputType, TElementResultsType, TElementsInputType, TElementsResultsType]):
    pass

class IWaterNetworkElement(INetworkElement[TElementManagerType, TElementType, TUnitsType, WaterNetworkElementType,
    TElementInputType, TElementResultsType, TElementsInputType, TElementsResultsType]):
    pass

class IPipeUnits(IElementUnits):
    pass

class IPipeInput(IElementInput):
    @property
    def InstallationYear(self) -> int:
        pass
    @InstallationYear.setter
    def InstallationYear(self, iy: int) -> None:
        pass

    @property
    def Diameter(self) -> float:
        pass
    @Diameter.setter
    def Diameter(self, d: float) -> None:
        pass

class IPipeResults(IElementResults):
    pass

class IPipesInput(IElementsInput):
    pass

class IPipesResults(IElementsResults):
    pass

class IPipe(IWaterNetworkElement[IPipes, IPipe, IPipeUnits, IPipeInput, IPipeResults, IPipesInput, IPipesResults]):
        pass

class IPipes(IWaterNetworkElements[IPipes, IPipe, IPipeUnits, IPipeInput, IPipeResults, IPipesInput, IPipesResults]):
    pass

class IWaterNetwork:
    @property
    def Pipes(self) -> IPipes:
        pass