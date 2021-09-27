from OpenFlows.Components import IModelComponents
from OpenFlows.ModelingElements import IElement
from enum import Enum

class WaterComponentType(Enum):
    Pattern = 50
    PumpDefinition = 51

class IWaterComponent(IElement):
    @property
    def ElementType(self) -> WaterComponentType:
        pass

class IZones:
    pass

class IZone:
    pass

class IWaterModelSupport(IModelComponents[IWaterComponent, WaterComponentType]):
    @property
    def Zones(self) -> IZones:
        pass