from typing import Generic
from OpenFlows.Interfaces import TComponentUnitsType, TNetworkUnitsType
from enum import Enum

class Unit:
    pass

class FormatCode(Enum):
    Fixed = 0
    General = 1
    ScientificNotation = 2
    Number = 3

class IUnit(object):
    # Dimension
    
    @property
    def FormatCode(self) -> FormatCode:
        pass
    @FormatCode.setter
    def FormatCode(self, f: FormatCode) -> None:
        pass

    @property
    def SignificantDigits(self) -> int:
        pass
    @SignificantDigits.setter
    def SignificantDigits(self, s: int) -> None:
        pass

    @property
    def Label(self) -> str:
        pass

    @property
    def ShortLabel(self) -> str:
        pass

    def ConvertTo(self, v: float, u: Unit) -> float:
        pass

    def FormatValue(self, v: float) -> str:
        pass

    def FormatValue(self, v: float, f: FormatCode, s: int) -> str:
        pass

    def GetUnit(self) -> Unit:
        pass
    def SetUnit(self, u: Unit) -> None:
        pass

class INetworkUnits:
    pass

class IComponentUnits:
    pass

class UnitSystemType(Enum)
    UsCustomary = 0
    SI = 1

class IUnits(Generic[TNetworkUnitsType, TComponentUnitsType]):
    @property
    def NetworkUnits(self) -> TNetworkUnitsType:
        pass
    @property
    def ComponentUnits(self) -> TComponentUnitsType:
        pass

    def ConvertValue(self, v: float, fromUnit: Unit, toUnit: Unit) -> float:
        pass

    def FormatValue(self, v: float, unit: IUnit) -> str:
        pass

    def FormatValue(self, v: float, unit: IUnit, format: FormatCode, significantDigits: int) -> str:
        pass

    def Reset(self, unitSystem: UnitSystemType) -> None:
        pass