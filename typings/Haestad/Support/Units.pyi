from Haestad.Support.Support import INamable, ILabeled
from typing import overload, List, Dict
from enum import Enum
from datetime import datetime
from array import array

class CurrencyBasedUnit(INamable):

	def __init__(self, astringName: str, adimension: Dimension, aunitsystem: UnitSystem, adouble: float, aintEnumValue: int, astringName: str, adimension: Dimension, aunitsystem: UnitSystem, adouble: float, aintEnumValue: int, bentleyName: str, astringName: str, adimension: Dimension, aunitsystem: UnitSystem, aiunitconverter: IUnitConverter, aintEnumValue: int, astringName: str, adimension: Dimension, aunitsystem: UnitSystem, aiunitconverter: IUnitConverter, aintEnumValue: int, bentleyName: str) -> None:
		"""No Description

		Args:
			astringName(str): astringName
			adimension(Dimension): adimension
			aunitsystem(UnitSystem): aunitsystem
			adouble(float): adouble
			aintEnumValue(int): aintEnumValue
			astringName(str): astringName
			adimension(Dimension): adimension
			aunitsystem(UnitSystem): aunitsystem
			adouble(float): adouble
			aintEnumValue(int): aintEnumValue
			bentleyName(str): bentleyName
			astringName(str): astringName
			adimension(Dimension): adimension
			aunitsystem(UnitSystem): aunitsystem
			aiunitconverter(IUnitConverter): aiunitconverter
			aintEnumValue(int): aintEnumValue
			astringName(str): astringName
			adimension(Dimension): adimension
			aunitsystem(UnitSystem): aunitsystem
			aiunitconverter(IUnitConverter): aiunitconverter
			aintEnumValue(int): aintEnumValue
			bentleyName(str): bentleyName
		"""
		pass

	def ConvertFrom(self, adouble: float, aunit: Unit) -> float:
		"""No Description

		Args:
			adouble(float): adouble
			aunit(Unit): aunit

		Returns:
			float: 
		"""
		pass

	def ConversionFactor(self, aunit: Unit) -> float:
		"""No Description

		Args:
			aunit(Unit): aunit

		Returns:
			float: 
		"""
		pass

	def ToSerializedString(self) -> str:
		"""No Description

		Returns:
			str: 
		"""
		pass

	@property
	def Dimension(self) -> Dimension:
		"""No Description

		Returns:
			CurrencyBasedUnit: 
		"""
		pass

	@property
	def EnumValue(self) -> int:
		"""No Description

		Returns:
			CurrencyBasedUnit: 
		"""
		pass

	@property
	def Label(self) -> str:
		"""No Description

		Returns:
			CurrencyBasedUnit: 
		"""
		pass

	@property
	def LabelKey(self) -> str:
		"""No Description

		Returns:
			CurrencyBasedUnit: 
		"""
		pass

	@property
	def Name(self) -> str:
		"""No Description

		Returns:
			CurrencyBasedUnit: 
		"""
		pass

	@property
	def BentleyName(self) -> str:
		"""No Description

		Returns:
			CurrencyBasedUnit: 
		"""
		pass

	@property
	def ShortLabel(self) -> str:
		"""No Description

		Returns:
			CurrencyBasedUnit: 
		"""
		pass

	@property
	def UnitSystem(self) -> UnitSystem:
		"""No Description

		Returns:
			CurrencyBasedUnit: 
		"""
		pass

class WeirCoefficientParameterized(INamable):

	def __init__(self, name: str, dimension: Dimension, aunitsystem: UnitSystem, converter: WeirCoefficientParameterizedUnitConverter, enumVal: int, name: str, dimension: Dimension, aunitsystem: UnitSystem, converter: WeirCoefficientParameterizedUnitConverter, enumVal: int, bentleyName: str) -> None:
		"""No Description

		Args:
			name(str): name
			dimension(Dimension): dimension
			aunitsystem(UnitSystem): aunitsystem
			converter(WeirCoefficientParameterizedUnitConverter): converter
			enumVal(int): enumVal
			name(str): name
			dimension(Dimension): dimension
			aunitsystem(UnitSystem): aunitsystem
			converter(WeirCoefficientParameterizedUnitConverter): converter
			enumVal(int): enumVal
			bentleyName(str): bentleyName
		"""
		pass

	def ConvertFrom(self, adouble: float, aunit: Unit) -> float:
		"""No Description

		Args:
			adouble(float): adouble
			aunit(Unit): aunit

		Returns:
			float: 
		"""
		pass

	def ConversionFactor(self, aunit: Unit) -> float:
		"""No Description

		Args:
			aunit(Unit): aunit

		Returns:
			float: 
		"""
		pass

	def ToSerializedString(self) -> str:
		"""No Description

		Returns:
			str: 
		"""
		pass

	@property
	def KExp(self) -> float:
		"""No Description

		Returns:
			WeirCoefficientParameterized: 
		"""
		pass

	@property
	def Dimension(self) -> Dimension:
		"""No Description

		Returns:
			WeirCoefficientParameterized: 
		"""
		pass

	@property
	def EnumValue(self) -> int:
		"""No Description

		Returns:
			WeirCoefficientParameterized: 
		"""
		pass

	@property
	def Label(self) -> str:
		"""No Description

		Returns:
			WeirCoefficientParameterized: 
		"""
		pass

	@property
	def LabelKey(self) -> str:
		"""No Description

		Returns:
			WeirCoefficientParameterized: 
		"""
		pass

	@property
	def Name(self) -> str:
		"""No Description

		Returns:
			WeirCoefficientParameterized: 
		"""
		pass

	@property
	def BentleyName(self) -> str:
		"""No Description

		Returns:
			WeirCoefficientParameterized: 
		"""
		pass

	@property
	def ShortLabel(self) -> str:
		"""No Description

		Returns:
			WeirCoefficientParameterized: 
		"""
		pass

	@property
	def UnitSystem(self) -> UnitSystem:
		"""No Description

		Returns:
			WeirCoefficientParameterized: 
		"""
		pass

	@KExp.setter
	def KExp(self, kexp: float) -> None:
		pass

class WeirCoefficientParameterizedUnitConverter(IUnitConverter):

	def __init__(self, unitSystem: UnitSystemIndex) -> None:
		"""No Description

		Args:
			unitSystem(UnitSystemIndex): unitSystem
		"""
		pass

	def FromBaseUnit(self, adouble: float) -> float:
		"""No Description

		Args:
			adouble(float): adouble

		Returns:
			float: 
		"""
		pass

	def ToBaseUnit(self, adouble: float) -> float:
		"""No Description

		Args:
			adouble(float): adouble

		Returns:
			float: 
		"""
		pass

	@property
	def KExp(self) -> float:
		"""No Description

		Returns:
			WeirCoefficientParameterizedUnitConverter: 
		"""
		pass

	@KExp.setter
	def KExp(self, kexp: float) -> None:
		pass

class InfiltrationPerUnitDepthUnit(INamable):

	def __init__(self, name: str, dimension: Dimension, aunitsystem: UnitSystem, converter: InfiltrationPerUnitDepthConverter, enumVal: int, name: str, dimension: Dimension, aunitsystem: UnitSystem, converter: InfiltrationPerUnitDepthConverter, enumVal: int, bentleyName: str) -> None:
		"""No Description

		Args:
			name(str): name
			dimension(Dimension): dimension
			aunitsystem(UnitSystem): aunitsystem
			converter(InfiltrationPerUnitDepthConverter): converter
			enumVal(int): enumVal
			name(str): name
			dimension(Dimension): dimension
			aunitsystem(UnitSystem): aunitsystem
			converter(InfiltrationPerUnitDepthConverter): converter
			enumVal(int): enumVal
			bentleyName(str): bentleyName
		"""
		pass

	def ConvertFrom(self, adouble: float, aunit: Unit) -> float:
		"""No Description

		Args:
			adouble(float): adouble
			aunit(Unit): aunit

		Returns:
			float: 
		"""
		pass

	def ConversionFactor(self, aunit: Unit) -> float:
		"""No Description

		Args:
			aunit(Unit): aunit

		Returns:
			float: 
		"""
		pass

	def ToSerializedString(self) -> str:
		"""No Description

		Returns:
			str: 
		"""
		pass

	@property
	def KExp(self) -> float:
		"""No Description

		Returns:
			InfiltrationPerUnitDepthUnit: 
		"""
		pass

	@property
	def Dimension(self) -> Dimension:
		"""No Description

		Returns:
			InfiltrationPerUnitDepthUnit: 
		"""
		pass

	@property
	def EnumValue(self) -> int:
		"""No Description

		Returns:
			InfiltrationPerUnitDepthUnit: 
		"""
		pass

	@property
	def Label(self) -> str:
		"""No Description

		Returns:
			InfiltrationPerUnitDepthUnit: 
		"""
		pass

	@property
	def LabelKey(self) -> str:
		"""No Description

		Returns:
			InfiltrationPerUnitDepthUnit: 
		"""
		pass

	@property
	def Name(self) -> str:
		"""No Description

		Returns:
			InfiltrationPerUnitDepthUnit: 
		"""
		pass

	@property
	def BentleyName(self) -> str:
		"""No Description

		Returns:
			InfiltrationPerUnitDepthUnit: 
		"""
		pass

	@property
	def ShortLabel(self) -> str:
		"""No Description

		Returns:
			InfiltrationPerUnitDepthUnit: 
		"""
		pass

	@property
	def UnitSystem(self) -> UnitSystem:
		"""No Description

		Returns:
			InfiltrationPerUnitDepthUnit: 
		"""
		pass

	@KExp.setter
	def KExp(self, kexp: float) -> None:
		pass

class InfiltrationPerUnitDepthConverter(IUnitConverter):

	def __init__(self, infiltrationUnit: UnitIndex, depthUnit: UnitIndex) -> None:
		"""No Description

		Args:
			infiltrationUnit(UnitIndex): infiltrationUnit
			depthUnit(UnitIndex): depthUnit
		"""
		pass

	def FromBaseUnit(self, adouble: float) -> float:
		"""No Description

		Args:
			adouble(float): adouble

		Returns:
			float: 
		"""
		pass

	def ToBaseUnit(self, adouble: float) -> float:
		"""No Description

		Args:
			adouble(float): adouble

		Returns:
			float: 
		"""
		pass

	@property
	def KExp(self) -> float:
		"""No Description

		Returns:
			InfiltrationPerUnitDepthConverter: 
		"""
		pass

	@property
	def BaseInfiltrationUnit(self) -> Unit:
		"""No Description

		Returns:
			InfiltrationPerUnitDepthConverter: 
		"""
		pass

	@property
	def BaseDepthUnit(self) -> Unit:
		"""No Description

		Returns:
			InfiltrationPerUnitDepthConverter: 
		"""
		pass

	@property
	def DepthUnit(self) -> Unit:
		"""No Description

		Returns:
			InfiltrationPerUnitDepthConverter: 
		"""
		pass

	@property
	def InfiltrationUnit(self) -> Unit:
		"""No Description

		Returns:
			InfiltrationPerUnitDepthConverter: 
		"""
		pass

	@KExp.setter
	def KExp(self, kexp: float) -> None:
		pass

class DrainageCoefficientUnit(INamable):

	def __init__(self, name: str, dimension: Dimension, aunitsystem: UnitSystem, converter: DrainageCoefficientUnitConverter, enumVal: int, name: str, dimension: Dimension, aunitsystem: UnitSystem, converter: DrainageCoefficientUnitConverter, enumVal: int, bentleyName: str) -> None:
		"""No Description

		Args:
			name(str): name
			dimension(Dimension): dimension
			aunitsystem(UnitSystem): aunitsystem
			converter(DrainageCoefficientUnitConverter): converter
			enumVal(int): enumVal
			name(str): name
			dimension(Dimension): dimension
			aunitsystem(UnitSystem): aunitsystem
			converter(DrainageCoefficientUnitConverter): converter
			enumVal(int): enumVal
			bentleyName(str): bentleyName
		"""
		pass

	def ConvertFrom(self, adouble: float, aunit: Unit) -> float:
		"""No Description

		Args:
			adouble(float): adouble
			aunit(Unit): aunit

		Returns:
			float: 
		"""
		pass

	def ConversionFactor(self, aunit: Unit) -> float:
		"""No Description

		Args:
			aunit(Unit): aunit

		Returns:
			float: 
		"""
		pass

	def ToSerializedString(self) -> str:
		"""No Description

		Returns:
			str: 
		"""
		pass

	@property
	def KExp(self) -> float:
		"""No Description

		Returns:
			DrainageCoefficientUnit: 
		"""
		pass

	@property
	def Dimension(self) -> Dimension:
		"""No Description

		Returns:
			DrainageCoefficientUnit: 
		"""
		pass

	@property
	def EnumValue(self) -> int:
		"""No Description

		Returns:
			DrainageCoefficientUnit: 
		"""
		pass

	@property
	def Label(self) -> str:
		"""No Description

		Returns:
			DrainageCoefficientUnit: 
		"""
		pass

	@property
	def LabelKey(self) -> str:
		"""No Description

		Returns:
			DrainageCoefficientUnit: 
		"""
		pass

	@property
	def Name(self) -> str:
		"""No Description

		Returns:
			DrainageCoefficientUnit: 
		"""
		pass

	@property
	def BentleyName(self) -> str:
		"""No Description

		Returns:
			DrainageCoefficientUnit: 
		"""
		pass

	@property
	def ShortLabel(self) -> str:
		"""No Description

		Returns:
			DrainageCoefficientUnit: 
		"""
		pass

	@property
	def UnitSystem(self) -> UnitSystem:
		"""No Description

		Returns:
			DrainageCoefficientUnit: 
		"""
		pass

	@KExp.setter
	def KExp(self, kexp: float) -> None:
		pass

class DrainageCoefficientUnitConverter(IUnitConverter):

	def __init__(self, infiltrationUnit: UnitIndex) -> None:
		"""No Description

		Args:
			infiltrationUnit(UnitIndex): infiltrationUnit
		"""
		pass

	def FromBaseUnit(self, adouble: float) -> float:
		"""No Description

		Args:
			adouble(float): adouble

		Returns:
			float: 
		"""
		pass

	def ToBaseUnit(self, adouble: float) -> float:
		"""No Description

		Args:
			adouble(float): adouble

		Returns:
			float: 
		"""
		pass

	@property
	def KExp(self) -> float:
		"""No Description

		Returns:
			DrainageCoefficientUnitConverter: 
		"""
		pass

	@property
	def BaseInfiltrationUnit(self) -> Unit:
		"""No Description

		Returns:
			DrainageCoefficientUnitConverter: 
		"""
		pass

	@property
	def InfiltrationUnit(self) -> Unit:
		"""No Description

		Returns:
			DrainageCoefficientUnitConverter: 
		"""
		pass

	@KExp.setter
	def KExp(self, kexp: float) -> None:
		pass

class Dimension(INamable):

	def __init__(self, astringName: str, aintEnumValue: int, astringName: str, aintEnumValue: int, bentleyName: str) -> None:
		"""No Description

		Args:
			astringName(str): astringName
			aintEnumValue(int): aintEnumValue
			astringName(str): astringName
			aintEnumValue(int): aintEnumValue
			bentleyName(str): bentleyName
		"""
		pass

	@staticmethod
	@overload
	def FromEnum(aint: int) -> Dimension:
		"""No Description

		Args:
			aint(int): aint

		Returns:
			Dimension: 
		"""
		pass

	@staticmethod
	@overload
	def FromEnum(dimension: DimensionType) -> Dimension:
		"""No Description

		Args:
			dimension(DimensionType): dimension

		Returns:
			Dimension: 
		"""
		pass

	@staticmethod
	@overload
	def Convert(adouble: float, dimensionType: DimensionType, aintFromUnit: int, aintToUnit: int) -> float:
		"""No Description

		Args:
			adouble(float): adouble
			dimensionType(DimensionType): dimensionType
			aintFromUnit(int): aintFromUnit
			aintToUnit(int): aintToUnit

		Returns:
			float: 
		"""
		pass

	@overload
	def Convert(self, adouble: float, aintFromUnit: int, aintToUnit: int) -> float:
		"""No Description

		Args:
			adouble(float): adouble
			aintFromUnit(int): aintFromUnit
			aintToUnit(int): aintToUnit

		Returns:
			float: 
		"""
		pass

	@staticmethod
	def FromIndex(aindex: DimensionIndex) -> Dimension:
		"""No Description

		Args:
			aindex(DimensionIndex): aindex

		Returns:
			Dimension: 
		"""
		pass

	@staticmethod
	def FromName(asNameDimension: str) -> Dimension:
		"""No Description

		Args:
			asNameDimension(str): asNameDimension

		Returns:
			Dimension: 
		"""
		pass

	def AvailableUnitsSortedEx(self, currentUnit: int) -> List:
		"""No Description

		Args:
			currentUnit(int): currentUnit

		Returns:
			List: 
		"""
		pass

	def UnitFromEnum(self, aiEnumValue: int) -> Unit:
		"""No Description

		Args:
			aiEnumValue(int): aiEnumValue

		Returns:
			Unit: 
		"""
		pass

	@property
	@staticmethod
	def Angle() -> Dimension:
		"""No Description

		Returns:
			Dimension: 
		"""
		pass

	@property
	@staticmethod
	def Area() -> Dimension:
		"""No Description

		Returns:
			Dimension: 
		"""
		pass

	@property
	@staticmethod
	def Concentration() -> Dimension:
		"""No Description

		Returns:
			Dimension: 
		"""
		pass

	@property
	@staticmethod
	def Currency() -> Dimension:
		"""No Description

		Returns:
			Dimension: 
		"""
		pass

	@property
	@staticmethod
	def CurrencyPerEnergy() -> Dimension:
		"""No Description

		Returns:
			Dimension: 
		"""
		pass

	@property
	@staticmethod
	def CurrencyPerLength() -> Dimension:
		"""No Description

		Returns:
			Dimension: 
		"""
		pass

	@property
	@staticmethod
	def Diffusivity() -> Dimension:
		"""No Description

		Returns:
			Dimension: 
		"""
		pass

	@property
	@staticmethod
	def ElectricalFrequency() -> Dimension:
		"""No Description

		Returns:
			Dimension: 
		"""
		pass

	@property
	@staticmethod
	def EmitterCoefficient() -> Dimension:
		"""No Description

		Returns:
			Dimension: 
		"""
		pass

	@property
	@staticmethod
	def Energy() -> Dimension:
		"""No Description

		Returns:
			Dimension: 
		"""
		pass

	@property
	@staticmethod
	def EnergyPerPower() -> Dimension:
		"""No Description

		Returns:
			Dimension: 
		"""
		pass

	@property
	@staticmethod
	def Flow() -> Dimension:
		"""No Description

		Returns:
			Dimension: 
		"""
		pass

	@property
	@staticmethod
	def FlowDensityPerArea() -> Dimension:
		"""No Description

		Returns:
			Dimension: 
		"""
		pass

	@property
	@staticmethod
	def FlowDensityPerCapita() -> Dimension:
		"""No Description

		Returns:
			Dimension: 
		"""
		pass

	@property
	@staticmethod
	def InfiltrationRate() -> Dimension:
		"""No Description

		Returns:
			Dimension: 
		"""
		pass

	@property
	@staticmethod
	def Length() -> Dimension:
		"""No Description

		Returns:
			Dimension: 
		"""
		pass

	@property
	@staticmethod
	def Mass() -> Dimension:
		"""No Description

		Returns:
			Dimension: 
		"""
		pass

	@property
	@staticmethod
	def MassPerEnergy() -> Dimension:
		"""No Description

		Returns:
			Dimension: 
		"""
		pass

	@property
	@staticmethod
	def MassRate() -> Dimension:
		"""No Description

		Returns:
			Dimension: 
		"""
		pass

	@property
	@staticmethod
	def None() -> Dimension:
		"""No Description

		Returns:
			Dimension: 
		"""
		pass

	@property
	@staticmethod
	def NthOrderBulkReactionRate() -> Dimension:
		"""No Description

		Returns:
			Dimension: 
		"""
		pass

	@property
	@staticmethod
	def Percent() -> Dimension:
		"""No Description

		Returns:
			Dimension: 
		"""
		pass

	@property
	@staticmethod
	def Population() -> Dimension:
		"""No Description

		Returns:
			Dimension: 
		"""
		pass

	@property
	@staticmethod
	def PopulationDensityPerArea() -> Dimension:
		"""No Description

		Returns:
			Dimension: 
		"""
		pass

	@property
	@staticmethod
	def Pressure() -> Dimension:
		"""No Description

		Returns:
			Dimension: 
		"""
		pass

	@property
	@staticmethod
	def Power() -> Dimension:
		"""No Description

		Returns:
			Dimension: 
		"""
		pass

	@property
	@staticmethod
	def RainfallIntensity() -> Dimension:
		"""No Description

		Returns:
			Dimension: 
		"""
		pass

	@property
	@staticmethod
	def ReactionRate() -> Dimension:
		"""No Description

		Returns:
			Dimension: 
		"""
		pass

	@property
	@staticmethod
	def RotationalFrequency() -> Dimension:
		"""No Description

		Returns:
			Dimension: 
		"""
		pass

	@property
	@staticmethod
	def Scale() -> Dimension:
		"""No Description

		Returns:
			Dimension: 
		"""
		pass

	@property
	@staticmethod
	def Slope() -> Dimension:
		"""No Description

		Returns:
			Dimension: 
		"""
		pass

	@property
	@staticmethod
	def SpecificWeight() -> Dimension:
		"""No Description

		Returns:
			Dimension: 
		"""
		pass

	@property
	@staticmethod
	def SurfaceReactionRate() -> Dimension:
		"""No Description

		Returns:
			Dimension: 
		"""
		pass

	@property
	@staticmethod
	def Temperature() -> Dimension:
		"""No Description

		Returns:
			Dimension: 
		"""
		pass

	@property
	@staticmethod
	def Time() -> Dimension:
		"""No Description

		Returns:
			Dimension: 
		"""
		pass

	@property
	@staticmethod
	def Unitless() -> Dimension:
		"""No Description

		Returns:
			Dimension: 
		"""
		pass

	@property
	@staticmethod
	def Velocity() -> Dimension:
		"""No Description

		Returns:
			Dimension: 
		"""
		pass

	@property
	@staticmethod
	def Volume() -> Dimension:
		"""No Description

		Returns:
			Dimension: 
		"""
		pass

	@property
	@staticmethod
	def WeirCoefficient() -> Dimension:
		"""No Description

		Returns:
			Dimension: 
		"""
		pass

	@property
	@staticmethod
	def ZeroOrderSurfaceReactionRate() -> Dimension:
		"""No Description

		Returns:
			Dimension: 
		"""
		pass

	@property
	@staticmethod
	def DiameterLength() -> Dimension:
		"""No Description

		Returns:
			Dimension: 
		"""
		pass

	@property
	@staticmethod
	def MassPerArea() -> Dimension:
		"""No Description

		Returns:
			Dimension: 
		"""
		pass

	@property
	@staticmethod
	def Inertia() -> Dimension:
		"""No Description

		Returns:
			Dimension: 
		"""
		pass

	@property
	@staticmethod
	def CurrencyPerPower() -> Dimension:
		"""No Description

		Returns:
			Dimension: 
		"""
		pass

	@property
	@staticmethod
	def CostPerUnitVolume() -> Dimension:
		"""No Description

		Returns:
			Dimension: 
		"""
		pass

	@property
	@staticmethod
	def EnergyPerUnitVolume() -> Dimension:
		"""No Description

		Returns:
			Dimension: 
		"""
		pass

	@property
	@staticmethod
	def Torque() -> Dimension:
		"""No Description

		Returns:
			Dimension: 
		"""
		pass

	@property
	@staticmethod
	def SpringConstant() -> Dimension:
		"""No Description

		Returns:
			Dimension: 
		"""
		pass

	@property
	@staticmethod
	def Force() -> Dimension:
		"""No Description

		Returns:
			Dimension: 
		"""
		pass

	@property
	@staticmethod
	def Density() -> Dimension:
		"""No Description

		Returns:
			Dimension: 
		"""
		pass

	@property
	@staticmethod
	def DischargePerPressureDrop() -> Dimension:
		"""No Description

		Returns:
			Dimension: 
		"""
		pass

	@property
	@staticmethod
	def VolumePerLength() -> Dimension:
		"""No Description

		Returns:
			Dimension: 
		"""
		pass

	@property
	@staticmethod
	def SideWeirCoefficient() -> Dimension:
		"""No Description

		Returns:
			Dimension: 
		"""
		pass

	@property
	@staticmethod
	def InfiltrationPerUnitDepth() -> Dimension:
		"""No Description

		Returns:
			Dimension: 
		"""
		pass

	@property
	@staticmethod
	def PressurePerLength() -> Dimension:
		"""No Description

		Returns:
			Dimension: 
		"""
		pass

	@property
	@staticmethod
	def MassPerLength() -> Dimension:
		"""No Description

		Returns:
			Dimension: 
		"""
		pass

	@property
	@staticmethod
	def PerLength() -> Dimension:
		"""No Description

		Returns:
			Dimension: 
		"""
		pass

	@property
	@staticmethod
	def PerPressure() -> Dimension:
		"""No Description

		Returns:
			Dimension: 
		"""
		pass

	@property
	@staticmethod
	def DynamicViscosity() -> Dimension:
		"""No Description

		Returns:
			Dimension: 
		"""
		pass

	@property
	@staticmethod
	def CalorificValue() -> Dimension:
		"""No Description

		Returns:
			Dimension: 
		"""
		pass

	@property
	@staticmethod
	def WeirCoefficientParameterized() -> Dimension:
		"""No Description

		Returns:
			Dimension: 
		"""
		pass

	@property
	@staticmethod
	def SnowMeltCoefficient() -> Dimension:
		"""No Description

		Returns:
			Dimension: 
		"""
		pass

	@property
	@staticmethod
	def BreakRate() -> Dimension:
		"""No Description

		Returns:
			Dimension: 
		"""
		pass

	@property
	@staticmethod
	def ValveOpenCloseRateCoefficient() -> Dimension:
		"""No Description

		Returns:
			Dimension: 
		"""
		pass

	@property
	@staticmethod
	def DrainCoefficientUnit() -> Dimension:
		"""No Description

		Returns:
			Dimension: 
		"""
		pass

	@property
	@staticmethod
	def NumberPerVolumeUnit() -> Dimension:
		"""No Description

		Returns:
			Dimension: 
		"""
		pass

	@property
	@staticmethod
	def NumberPerAreaUnit() -> Dimension:
		"""No Description

		Returns:
			Dimension: 
		"""
		pass

	@property
	@staticmethod
	def MolesPerVolumeUnit() -> Dimension:
		"""No Description

		Returns:
			Dimension: 
		"""
		pass

	@property
	@staticmethod
	def MolesPerAreaUnit() -> Dimension:
		"""No Description

		Returns:
			Dimension: 
		"""
		pass

	@property
	@staticmethod
	def ValveOpenCloseRateCoefficientPerFlow() -> Dimension:
		"""No Description

		Returns:
			Dimension: 
		"""
		pass

	@property
	@staticmethod
	def FlowPerUnitLength() -> Dimension:
		"""No Description

		Returns:
			Dimension: 
		"""
		pass

	@property
	@staticmethod
	def Acceleration() -> Dimension:
		"""No Description

		Returns:
			Dimension: 
		"""
		pass

	@property
	def AvailableUnitsSorted(self) -> List:
		"""No Description

		Returns:
			Dimension: 
		"""
		pass

	@property
	def EnumValue(self) -> int:
		"""No Description

		Returns:
			Dimension: 
		"""
		pass

	@property
	def Label(self) -> str:
		"""No Description

		Returns:
			Dimension: 
		"""
		pass

	@property
	def LabelKey(self) -> str:
		"""No Description

		Returns:
			Dimension: 
		"""
		pass

	@property
	def Name(self) -> str:
		"""No Description

		Returns:
			Dimension: 
		"""
		pass

	@property
	def BentleyName(self) -> str:
		"""No Description

		Returns:
			Dimension: 
		"""
		pass

	@property
	def ShortLabel(self) -> str:
		"""No Description

		Returns:
			Dimension: 
		"""
		pass

	@property
	def Units(self) -> ISet:
		"""No Description

		Returns:
			Dimension: 
		"""
		pass

class DimensionType(Enum):
	Dimensionless = 0
	Length = 1
	Area = 2
	Mass = 3
	Flow = 4
	Percentage = 5
	Time = 6
	ReactionRate = 7
	SurfaceReactionRate = 8
	Pressure = 9
	Concentration = 10
	Volume = 11
	Diffusivity = 12
	Temperature = 13
	Power = 14
	RainfallIntensity = 15
	Angle = 16
	InfiltrationRate = 17
	Velocity = 18
	Scale = 19
	NthOrderBulkReactionRate = 20
	ZeroOrderSurfaceReactionRate = 21
	CurrencyPerPower = 22
	CurrencyPerEnergy = 23
	Slope = 24
	FlowDensityPerArea = 25
	Currency = 26
	Population = 27
	Energy = 28
	MassRate = 29
	SpecificWeight = 30
	FlowPerCapita = 31
	PopulationDensityPerArea = 32
	EmitterCoeff = 33
	CurrencyPerLength = 34
	Unitless = 35
	ElectricalFrequency = 102
	RotationalFrequency = 103
	WeirCoefficient = 104
	DiameterLength = 105
	MassPerArea = 106
	Inertia = 108
	CostPerUnitVolume = 109
	EnergyPerUnitVolume = 110
	Torque = 111
	SpringConstant = 112
	Force = 113
	Density = 114
	DischargePerPressureDrop = 115
	VolumerPerLength = 116
	SideWeirCoefficient = 117
	InfiltrationPerUnitDepth = 118
	PressurePerLength = 119
	MassPerLength = 120
	PerLength = 121
	PerPressure = 122
	DynamicViscosity = 123
	CalorificValue = 124
	WeirCoefficientParameterized = 125
	SnowMeltCoefficient = 126
	BreakRate = 127
	MassPerEnergy = 128
	ValveOpenCloseRateCoefficient = 129
	EnergyPerPower = 130
	DrainCoefficient = 131
	NumberPerVolume = 132
	NumbersPerArea = 133
	MolesPerVolume = 134
	MolesPerArea = 135
	ValveOpenCloseRateCoefficientPerFlow = 136
	FlowPerUnitLength = 137
	Acceleration = 138

class EmitterCoefficientUnit(Enum):
	LitersPerDayPerMetersOfH2O = 1
	MegaLitersPerDayPerMetersOfH2O = 2
	LitersPerSecondPerMetersOfH2O = 3
	CubicMetersPerSecondPerMetersOfH2O = 4
	CubicMetersPerHourPerMetersOfH2O = 5
	CubicMetersPerDayPerMetersOfH2O = 6
	GallonsPerSecondPerPSI = 7
	GallonsPerDayPerPSI = 8
	ImperialGallonsPerSecondPerPSI = 9
	ImperialGallonsPerDayPerPSI = 10
	CubicFeetPerSecondPerPSI = 11
	CubicFeetPerDayPerPSI = 12
	LitersPerMinutePerMetersOfH2O = 13
	CubicMetersPerMinutePerMetersOfH2O = 14
	CFSPerPSI = 15
	CubicFeetPerMinutePerPSI = 16
	CFMPerPSI = 17
	GallonsPerMinutePerPSI = 18
	GPMPerPSI = 19
	ImperialGallonsPerMinutePerPSI = 20
	MGDPerPSI = 21
	MGDImperialPerPSI = 22

class LengthUnit(Enum):
	Meters = 1
	Kilometers = 2
	Centimeters = 3
	Millimeters = 4
	Feet = 5
	Mfeet = 6
	Millifeet = 7
	Inches = 8
	Yards = 9
	Miles = 10
	Decimeters = 11
	USSurveyFoot = 12

class AreaUnit(Enum):
	SquareMillimeters = 1
	SquareCentimeters = 2
	SquareMeters = 3
	Hectares = 4
	SquareKilometers = 5
	SquareInches = 6
	SquareFeet = 7
	ThousandSquareFeet = 8
	SquareYards = 9
	Acres = 10
	SquareMiles = 11

class MassUnit(Enum):
	Kilograms = 1
	Gram = 2
	Milligram = 3
	Pounds = 4
	Tons = 5

class FlowUnit(Enum):
	LitersPerDay = 1
	MegaLitersPerDay = 2
	LitersPerSecond = 3
	CubicMetersPerSecond = 4
	CubicMetersPerHour = 5
	CubicMetersPerDay = 6
	GallonsPerSecond = 7
	GallonsPerDay = 8
	ImperialGallonsPerSecond = 9
	ImperialGallonsPerDay = 10
	CubicFeetPerSecond = 11
	CubicFeetPerDay = 12
	AcreFeetPerMinute = 13
	LitersPerMinute = 14
	CubicMetersPerMinute = 15
	CFS = 16
	CubicFeetPerMinute = 17
	CFM = 18
	GallonsPerMinute = 19
	GPM = 20
	ImperialGallonsPerMinute = 21
	AcreInchPerMinute = 22
	AcreInchPerHour = 23
	AcreFeetPerHour = 24
	AcreFeetPerDay = 25
	MGD = 26
	MGDImperial = 27
	MillionLitersPerDay = 28
	GPD = 29
	LitersPerHour = 30

class PercentUnit(Enum):
	Percent = 1
	Unitless = 2

class TimeUnit(Enum):
	Seconds = 1
	Minutes = 2
	Hours = 3
	Days = 4
	Years = 5
	Milliseconds = 6

class ReactionRateUnit(Enum):
	PerSecond = 1
	PerDay = 2
	PerMinute = 3
	PerHour = 4

class SurfaceReactionRateUnit(Enum):
	MetersPerSecond = 1
	MetersPerDay = 2
	FeetPerDay = 3

class PressureUnit(Enum):
	NewtonsPerSquareMeter = 1
	MillimetersOfH2O = 2
	KiloPascals = 3
	MetersOfH2O = 4
	KilogramsPerSquareCentimeter = 5
	Bars = 6
	PoundsPerSquareFoot = 7
	FeetOfH2O = 8
	PoundsPerSquareInch = 9
	PSI = 10
	Atmospheres = 11
	KilogramsPerSquareMeter = 12
	Pascals = 13
	HektoPascals = 14
	MegaPascals = 15
	MilliBars = 16

class ConcentrationUnit(Enum):
	MicrogramsPerLiter = 1
	PartsPerBillion = 2
	MilliGramsPerLiter = 3
	PartsPerMillion = 4
	PoundsPerCubicFoot = 5
	PoundsPerMillionGallons = 6

class VolumeUnit(Enum):
	CubicCentimeters = 1
	Liters = 2
	CubicMeters = 3
	CubicInches = 4
	Gallons = 5
	ImpGallons = 6
	CubicFeet = 7
	CubicYards = 8
	AcreInches = 9
	AcreFeet = 10
	MillionGallons = 11
	ThousandGallons = 12
	ThousandLiters = 13
	MillionLiters = 14

class DollarsPerVolumeUnit(Enum):
	DollarsPerCubicCentimeters = 1
	DollarsPerLiters = 2
	DollarsPerCubicMeters = 3
	DollarsPerCubicInches = 4
	DollarsPerGallons = 5
	DollarsPerImpGallons = 6
	DollarsPerCubicFeet = 7
	DollarsPerCubicYards = 8
	DollarsPerAcreInches = 9
	DollarsPerAcreFeet = 10
	DollarsPerMillionGallons = 11
	DollarsPerThousandGallons = 12
	DollarsPerThousandLiters = 13
	DollarsPerMillionLiters = 14

class DiffusivityUnit(Enum):
	SquareMetersPerSecond = 1
	SquareFeetPerSecond = 2
	Stokes = 3
	Centistokes = 4

class TemperatureUnit(Enum):
	Celsius = 1
	Fahrenheit = 2
	Kelvin = 3

class PowerUnit(Enum):
	Watts = 1
	Kilowatts = 2
	HorsePower = 3
	MegaWatts = 4
	GigaWatts = 5

class EnergyUnit(Enum):
	Joules = 1
	KiloJoules = 2
	KiloWattHours = 3
	FootPoundals = 4
	MegaJoules = 5
	GigaJoules = 6
	WattSeconds = 7
	MegaWattHours = 8
	GigaWattHours = 9

class RainfallIntensityUnit(Enum):
	MillimetersPerMinute = 1
	CentimetersPerMinute = 2
	InchesPerDay = 3
	InchesPerHour = 4
	InchesPerMinute = 5
	MillimetersPerDay = 6
	CentimetersPerDay = 7
	MillimetersPerHour = 8
	CentimetersPerHour = 9
	MicrometersPerSecond = 10

class AngleUnit(Enum):
	Radians = 1
	Degrees = 2
	AngleMinutes = 3
	AngleSeconds = 4
	Quadrants = 5
	Revolutions = 6

class InfiltrationRateUnit(Enum):
	MillimetersPerMinute = 1
	CentimetersPerMinute = 2
	InchesPerDay = 3
	InchesPerHour = 4
	InchesPerMinute = 5
	MillimetersPerDay = 6
	CentimetersPerDay = 7
	MillimetersPerHour = 8
	CentimetersPerHour = 9

class VelocityUnit(Enum):
	CentimetersPerHour = 1
	CentimetersPerMinute = 2
	CentimetersPerSecond = 3
	MetersPerHour = 4
	MetersPerMinute = 5
	KilometersPerHour = 6
	MetersPerSecond = 7
	InchesPerHour = 8
	FeetPerHour = 9
	InchesPerMinute = 10
	FeetPerMinute = 11
	InchesPerSecond = 12
	FeetPerSecond = 13
	MilePerHour = 14
	KnotInternational = 15
	Knot = 16

class ScaleUnit(Enum):
	MetersPerCm = 1
	FeetPerInch = 2

class NthOrderBulkReactionRateUnit(Enum):
	MicrogramsPerLiterNPerSecond = 1
	MicrogramsPerLiterNPerDay = 2
	PartsPerBillionNPerSecond = 3
	PartsPerBillionNPerDay = 4
	MilliGramsPerLiterNPerSecond = 5
	MilliGramsPerLiterNPerDay = 6
	PartsPerMillionNPerSecond = 7
	PartsPerMillionNPerDay = 8
	PoundsPerCubicFootNPerSecond = 9
	PoundsPerCubicFootNPerDay = 10
	PoundsPerMillionGallonsNPerSecond = 11
	PoundsPerMillionGallonsNPerDay = 12

class ZeroOrderSurfaceReactionRateUnit(Enum):
	MicrogramsPerSquareMeterPerSecond = 1
	MicrogramsPerSquareMeterPerDay = 2
	MicrogramsPerSquareFeetPerDay = 3
	MilliGramsPerSquareMeterPerSecond = 4
	MilliGramsPerSquareMeterPerDay = 5
	MilliGramsPerSquareFeetPerDay = 6

class CurrencyPerEnergyUnit(Enum):
	DollarsPerKiloWattHour = 1

class CurrencyPerPowerUnit(Enum):
	DollarsPerKiloWatt = 1
	DollarsPerHorsePower = 2

class SlopeUnit(Enum):
	PercentSlope = 1
	OneOverS = 2
	CentimeterPerMeter = 3
	FeetPer1000Feet = 4
	FootPerFoot = 5
	FootPerFootVtoH = 6
	FootPerFootHtoV = 7
	FeetPerMile = 8
	HorizontalToVertical = 9
	VerticalToHorizontal = 10
	InchPerFoot = 11
	MeterPerKilometer = 12
	MeterPerMeter = 13
	MeterPerMeterVtoH = 14
	MeterPerMeterHtoV = 15
	MilliMeterPerMeter = 16
	MillimeterVerticalPerMeterHorizontal = 17
	MilliMeterPerMeterHtoV = 18

class FlowDensityPerAreaUnit(Enum):
	CFSPerSquareFeet = 1
	CFSPerAcres = 2
	CFSPerSquareMiles = 3
	GPMPerSquareFeet = 4
	GPMPerAcres = 5
	GPMPerSquareMile = 6
	GPDPerSquareFeet = 7
	GPDPerAcres = 8
	GPDPerSquareMile = 9
	LitersPerSquareMeterPerDay = 10
	LitersPerSquareKilometerPerDay = 11
	LitersPerHectaresPerDay = 12
	CubicMetersPerSquareMeterPerDay = 13
	CubicMetersPerSquareKilometerPerDay = 14
	CubicMetersPerHectaresPerDay = 15
	LitersPerHectaresPerSecond = 16

class PopulationDensityPerAreaUnit(Enum):
	PersonsPerSquareFeet = 1
	PersonsPerAcre = 2
	PersonsPerSquareMile = 3
	PersonsPerSquareMeter = 4
	PersonsPerSquareKilometer = 5
	PersonsPerHectares = 6

class FlowPerCapitaUnit(Enum):
	GPDPerCapita = 1
	LitersPerCapitaPerDay = 2

class CurrencyUnit(Enum):
	BaseCurrency = 1
	KiloCurrency = 2
	MegaCurrency = 3
	GigaCurrency = 4

class PopulationUnit(Enum):
	Capita = 1
	ThousandCapita = 2
	HundredCapita = 3
	Customer = 4
	Employee = 5
	Passenger = 6
	Person = 7
	Guest = 8
	Resident = 9
	Student = 10

class MassRateUnit(Enum):
	MicrogramsPerSecond = 1
	MilliGramsPerSecond = 2
	GramsPerSecond = 3
	KilogramsPerSecond = 4
	PoundsPerSecond = 5
	MicrogramsPerMinute = 6
	MilliGramsPerMinute = 7
	GramsPerMinute = 8
	KilogramsPerMinute = 9
	PoundsPerMinute = 10
	MicrogramsPerHour = 11
	MilliGramsPerHour = 12
	GramsPerHour = 13
	KilogramsPerHour = 14
	PoundsPerHour = 15
	MicrogramsPerDay = 16
	MilliGramsPerDay = 17
	GramsPerDay = 18
	KilogramsPerDay = 19
	PoundsPerDay = 20

class SpecificWeightUnit(Enum):
	NewtonsPerCubicMeter = 1
	KiloNewtonsPerCubicMeter = 2
	PoundsForcePerCubicFoot = 3

class ElectricalFrequencyUnit(Enum):
	Hertz = 1

class RotationalFrequencyUnit(Enum):
	RPM = 1

class WeirCoefficientUnit(Enum):
	SI = 1
	US = 2

class SideWeirCoefficientUnit(Enum):
	SI = 1
	US = 2

class DiameterLengthUnit(Enum):
	InchMiles = 1
	InchFeet = 2
	FootMiles = 3
	FootFeet = 4
	MillimeterMeters = 5
	MillimeterKilometers = 6
	MeterMeters = 7
	MeterKilometer = 8
	InchMeters = 9
	MillimeterMiles = 10

class MassPerAreaUnit(Enum):
	PoundsPerAcre = 1
	KilogramsPerHectare = 2
	MilligramsPerSquareFeet = 3
	MicrogramsPerSquareFeet = 4
	MilligramsPerSquareMeter = 5
	MicrogramsPerSquareMeter = 6
	MilligramsPerSquareCentimeter = 7
	MicrogramsPerSquareCentimeter = 8

class NumberPerVolumeUnit(Enum):
	NumbersPerLiter = 1
	ThousandNumbersPerLiter = 2
	MillionNumbersPerLiter = 3

class NumbersPerAreaUnit(Enum):
	NumbersPerSquareMeter = 1
	ThousandNumbersPerSquareMeter = 2
	MillionNumbersPerSquareMeter = 3
	NumbersPerSquareFeet = 4
	ThousandNumbersPerSquareFeet = 5
	MillionNumbersPerSquareFeet = 6
	NumbersPerSquareCentimeter = 7
	ThousandNumbersPerSquareCentimeter = 8
	MillionNumbersPerSquareCentimeter = 9

class MolesPerVolumeUnit(Enum):
	MolePerLiter = 1
	MilliMolePerLiter = 2

class MolesPerAreaUnit(Enum):
	MolePerSquareMeter = 1
	MilliMolePerSquareMeter = 2
	MolePerSquareFeet = 3
	MilliMolePerSquareFeet = 4
	MolePerSquareCentimeter = 5
	MilliMolePerSquareCentimeter = 6

class InertiaUnit(Enum):
	PoundSquareFeet = 1
	NewtonSquareMeters = 2
	KilogramSquareMeters = 3

class EnergyPerUnitVolume(Enum):
	KiloWattHourPerMillionGallons = 1
	KiloWattHourPerMillionLiters = 2
	KiloWattHourPerCubicMeters = 3
	KiloWattHourPerCubicFeet = 4

class TorqueUnit(Enum):
	NewtonMeters = 1
	PoundFeet = 2

class SpringConstantUnit(Enum):
	PoundPerInch = 1
	NewtonPerMillimeter = 2

class ForceUnit(Enum):
	PoundForce = 1
	KiloPoundForce = 2
	Newton = 3
	KiloNewton = 4

class DensityUnit(Enum):
	SlugPerCubicFoot = 1
	PoundPerCubicFoot = 2
	KilogramPerCubicMeter = 3

class DischargePerPressureDropUnit(Enum):
	CfsPerSquareRootFooH20 = 1
	CmsPerSquareRootMeterH20 = 2
	LPerSecPerSquareRootKpa = 3
	GpmPerSquareRootPsi = 4

class VolumerPerLength(Enum):
	CubicFeetPerFoot = 1
	CubicMetersPerMeter = 2

class InfiltrationPerUnitDepth(Enum):
	InchesPerHourPerFeetToKexp = 1
	CentimeterPerHourPerMeterToKexp = 2

class PressurePerLengthUnit(Enum):
	PascalsPerMeter = 1
	BarsPerKiloMeter = 2
	PSIPerFoot = 3
	PSIPerInch = 4

class MassPerLengthUnit(Enum):
	KilogramsPerMeter = 1
	PoundsPerFoot = 2

class PerLengthUnit(Enum):
	PerMeter = 1
	PerMillimeter = 2

class PerPressureUnit(Enum):
	PerPascals = 1
	PerBars = 2
	PerPSI = 3

class DynamicViscosityUnit(Enum):
	KilogramsPerMeterPerSecond = 1
	PoundSecondPerSquareFoot = 2

class CalorificValueUnit(Enum):
	JoulesPerCubicMeters = 1
	KiloJoulesPerCubicMeters = 2
	MegaJoulesPerCubicMeters = 3
	KiloWattHoursPerCubicMeters = 4

class DateTimeFormats(Enum):
	ElapsedTimeShort = 0
	ElapsedTimeLong = 1
	ShortTime = 2
	LongTime = 3
	ShortDate = 4
	LongDate = 5
	ShortDateAndShortTime = 6
	ShortDateAndLongTime = 7
	LongDateAndShortTime = 8
	LongDateAndLongTime = 9
	SortableDateTime = 10
	UniversalSortableDateTime = 11
	UniversalFullDateAndTime = 12

class WeirCoefficientParameterizedUnit(Enum):
	SI = 1
	US = 2

class SnowMeltCoefficientUnit(Enum):
	MillimetersPerHourPerDegreeCelsius = 1
	InchesPerHourPerDegreeFahrenheit = 2

class BreakRateUnit(Enum):
	BreaksPerYrPerKm = 1
	BreaksPerYrPerMi = 2
	BreaksPerYrPer1000Ft = 3
	BreaksPerYrPer100Mi = 4

class ValveOpenCloseRateCoefficientUnit(Enum):
	percentPerSecondPerMeterH2O = 1
	percentPerSecondPerFtH2O = 2
	percentPerSecondPerKiloPascal = 3
	percentPerSecondPerPSI = 4

class AccelerationUnit(Enum):
	MetersPerSquareSecond = 1
	FeetPerSquareSecond = 2

class DrainCoefficientUnit(Enum):
	DrainCoeffInchesPerHour = 1
	DrainCoeffMMPerHour = 2

class ValveOpenCloseRateCoefficientUnitPerFlow(Enum):
	PercentPerSecondPerCubicFeetPerSecond = 1
	PercentPerSecondPerCubicFeetPerMinute = 2
	PercentPerSecondPerCubicMeterPerSecond = 3
	PercentPerSecondPerCubicMeterPerMinute = 4
	PercentPerSecondPerLiterPerSecond = 5
	PercentPerSecondPerLiterPerMinute = 6
	PercentPerSecondPerGalPerSecond = 7
	PercentPerSecondPerGalPerMinute = 8

class FlowPerUnitLengthUnit(Enum):
	CubicFeetPerMilePerSecond = 0
	LitersPerKilometerPerSecond = 1
	QuadFeetPerSecond = 2
	GallonsPerFootPerMinute = 3
	GallonsPerMilePerMinute = 4
	QuadMeterPerSecond = 5
	CubicMetersPerKilometerPerSecond = 6
	LitersPerMeterPerSecond = 7

class IUnitConverter:

	def __init__(self) -> None:
		"""Creating a new Instance of this class is not allowed


		Raises:
			Exception: if this class is instanciated
		"""
		raise Exception("Creating a new Instance of this class is not allowed")
		pass

	def FromBaseUnit(self, adouble: float) -> float:
		"""No Description

		Args:
			adouble(float): adouble

		Returns:
			float: 
		"""
		pass

	def ToBaseUnit(self, adouble: float) -> float:
		"""No Description

		Args:
			adouble(float): adouble

		Returns:
			float: 
		"""
		pass

class NumericConversionHandler:

	def __init__(self, aunitStorage: Unit, anf: NumericFormatter) -> None:
		"""No Description

		Args:
			aunitStorage(Unit): aunitStorage
			anf(NumericFormatter): anf
		"""
		pass

	def DependsOn(self, anf: NumericFormatter) -> bool:
		"""No Description

		Args:
			anf(NumericFormatter): anf

		Returns:
			bool: 
		"""
		pass

	def StorageDoubleFromViewDouble(self, adouble: float) -> float:
		"""No Description

		Args:
			adouble(float): adouble

		Returns:
			float: 
		"""
		pass

	def StorageDoubleFromViewString(self, astring: str) -> float:
		"""No Description

		Args:
			astring(str): astring

		Returns:
			float: 
		"""
		pass

	def StorageToViewFactor(self) -> float:
		"""No Description

		Returns:
			float: 
		"""
		pass

	def ViewDoubleFromStorageDouble(self, adouble: float) -> float:
		"""No Description

		Args:
			adouble(float): adouble

		Returns:
			float: 
		"""
		pass

	def ViewStringFromStorageDouble(self, adouble: float) -> str:
		"""No Description

		Args:
			adouble(float): adouble

		Returns:
			str: 
		"""
		pass

	@property
	def Formatter(self) -> NumericFormatter:
		"""No Description

		Returns:
			NumericConversionHandler: 
		"""
		pass

	@property
	def StorageUnit(self) -> Unit:
		"""No Description

		Returns:
			NumericConversionHandler: 
		"""
		pass

class BaseDateTimeDelegate(ICloneable, ISerializable):

	def __init__(self, object: object, method: IntPtr) -> None:
		"""No Description

		Args:
			object(object): object
			method(IntPtr): method
		"""
		pass

	def Invoke(self) -> datetime:
		"""No Description

		Returns:
			datetime: 
		"""
		pass

	def BeginInvoke(self, callback: AsyncCallback, object: object) -> IAsyncResult:
		"""No Description

		Args:
			callback(AsyncCallback): callback
			object(object): object

		Returns:
			IAsyncResult: 
		"""
		pass

	def EndInvoke(self, result: IAsyncResult) -> datetime:
		"""No Description

		Args:
			result(IAsyncResult): result

		Returns:
			datetime: 
		"""
		pass

	def GetObjectData(self, info: SerializationInfo, context: StreamingContext) -> None:
		"""No Description

		Args:
			info(SerializationInfo): info
			context(StreamingContext): context

		Returns:
			None: 
		"""
		pass

	def GetInvocationList(self) -> array(Delegate):
		"""No Description

		Returns:
			array(Delegate): 
		"""
		pass

	def DynamicInvoke(self, args: array(object)) -> object:
		"""No Description

		Args:
			args(array(object)): args

		Returns:
			object: 
		"""
		pass

	def Clone(self) -> object:
		"""No Description

		Returns:
			object: 
		"""
		pass

	@property
	def Method(self) -> MethodInfo:
		"""No Description

		Returns:
			BaseDateTimeDelegate: 
		"""
		pass

	@property
	def Target(self) -> object:
		"""No Description

		Returns:
			BaseDateTimeDelegate: 
		"""
		pass

class NumberFormatInfoLibrary:

	def __init__(self) -> None:
		"""No Description
		"""
		pass

	@property
	def CurrentNumberFormatInfo(self) -> NumberFormatInfo:
		"""No Description

		Returns:
			NumberFormatInfoLibrary: 
		"""
		pass

	@property
	def CurrentCultureInfo(self) -> CultureInfo:
		"""No Description

		Returns:
			NumberFormatInfoLibrary: 
		"""
		pass

	@property
	@staticmethod
	def Current() -> NumberFormatInfoLibrary:
		"""No Description

		Returns:
			NumberFormatInfoLibrary: 
		"""
		pass

class NumericFormatter(INamable, IMementoable, ILabeled):

	def __init__(self, aintId: int, asName: str, aunit: Unit, asFormatCode: str, aintDecimalDigits: int, aintId: int, asName: str, aunit: Unit, asFormatCode: str, aintDecimalDigits: int, aboolIsStandardFormatter: bool, astringLabel: str, aintId: int, asName: str, asFormatCode: str, aintDecimalDigits: int, aunitDisplayDefaultSi: Unit, aunitDisplayDefaultUs: Unit, aintId: int, asName: str, asFormatCode: str, aintDecimalDigits: int, aunitDisplayDefaultSi: Unit, aunitDisplayDefaultUs: Unit, aboolIsStandardFormatter: bool, astringLabel: str, aintId: int, asName: str, aunit: Unit, asFormatCode: str, aintDecimalDigits: int, aunitDisplayDefaultSi: Unit, aunitDisplayDefaultUs: Unit, aintId: int, asName: str, aunit: Unit, asFormatCode: str, aintDecimalDigits: int, aunitDisplayDefaultSi: Unit, aunitDisplayDefaultUs: Unit, aboolIsStandardFormatter: bool, astringLabel: str) -> None:
		"""No Description

		Args:
			aintId(int): aintId
			asName(str): asName
			aunit(Unit): aunit
			asFormatCode(str): asFormatCode
			aintDecimalDigits(int): aintDecimalDigits
			aintId(int): aintId
			asName(str): asName
			aunit(Unit): aunit
			asFormatCode(str): asFormatCode
			aintDecimalDigits(int): aintDecimalDigits
			aboolIsStandardFormatter(bool): aboolIsStandardFormatter
			astringLabel(str): astringLabel
			aintId(int): aintId
			asName(str): asName
			asFormatCode(str): asFormatCode
			aintDecimalDigits(int): aintDecimalDigits
			aunitDisplayDefaultSi(Unit): aunitDisplayDefaultSi
			aunitDisplayDefaultUs(Unit): aunitDisplayDefaultUs
			aintId(int): aintId
			asName(str): asName
			asFormatCode(str): asFormatCode
			aintDecimalDigits(int): aintDecimalDigits
			aunitDisplayDefaultSi(Unit): aunitDisplayDefaultSi
			aunitDisplayDefaultUs(Unit): aunitDisplayDefaultUs
			aboolIsStandardFormatter(bool): aboolIsStandardFormatter
			astringLabel(str): astringLabel
			aintId(int): aintId
			asName(str): asName
			aunit(Unit): aunit
			asFormatCode(str): asFormatCode
			aintDecimalDigits(int): aintDecimalDigits
			aunitDisplayDefaultSi(Unit): aunitDisplayDefaultSi
			aunitDisplayDefaultUs(Unit): aunitDisplayDefaultUs
			aintId(int): aintId
			asName(str): asName
			aunit(Unit): aunit
			asFormatCode(str): asFormatCode
			aintDecimalDigits(int): aintDecimalDigits
			aunitDisplayDefaultSi(Unit): aunitDisplayDefaultSi
			aunitDisplayDefaultUs(Unit): aunitDisplayDefaultUs
			aboolIsStandardFormatter(bool): aboolIsStandardFormatter
			astringLabel(str): astringLabel
		"""
		pass

	def add_DecimalDigitsChanged(self, value: EventHandler) -> None:
		"""No Description

		Args:
			value(EventHandler): value

		Returns:
			None: 
		"""
		pass

	def remove_DecimalDigitsChanged(self, value: EventHandler) -> None:
		"""No Description

		Args:
			value(EventHandler): value

		Returns:
			None: 
		"""
		pass

	def add_DisplayUnitChanged(self, value: EventHandler) -> None:
		"""No Description

		Args:
			value(EventHandler): value

		Returns:
			None: 
		"""
		pass

	def remove_DisplayUnitChanged(self, value: EventHandler) -> None:
		"""No Description

		Args:
			value(EventHandler): value

		Returns:
			None: 
		"""
		pass

	def add_FormatCodeChanged(self, value: EventHandler) -> None:
		"""No Description

		Args:
			value(EventHandler): value

		Returns:
			None: 
		"""
		pass

	def remove_FormatCodeChanged(self, value: EventHandler) -> None:
		"""No Description

		Args:
			value(EventHandler): value

		Returns:
			None: 
		"""
		pass

	def CreateMemento(self) -> IMemento:
		"""No Description

		Returns:
			IMemento: 
		"""
		pass

	def DoubleFromDoubleUnit(self, adouble: float, aunit: Unit) -> float:
		"""No Description

		Args:
			adouble(float): adouble
			aunit(Unit): aunit

		Returns:
			float: 
		"""
		pass

	def DoubleUnitFromDouble(self, aunit: Unit, adouble: float) -> float:
		"""No Description

		Args:
			aunit(Unit): aunit
			adouble(float): adouble

		Returns:
			float: 
		"""
		pass

	def DoubleUnitFromString(self, aunit: Unit, astring: str) -> float:
		"""No Description

		Args:
			aunit(Unit): aunit
			astring(str): astring

		Returns:
			float: 
		"""
		pass

	def InitializeDefaultsFrom(self, anf: NumericFormatter) -> None:
		"""No Description

		Args:
			anf(NumericFormatter): anf

		Returns:
			None: 
		"""
		pass

	def InitializeFrom(self, anf: NumericFormatter) -> None:
		"""No Description

		Args:
			anf(NumericFormatter): anf

		Returns:
			None: 
		"""
		pass

	def ResetDefault(self, aunitsystem: UnitSystem) -> None:
		"""No Description

		Args:
			aunitsystem(UnitSystem): aunitsystem

		Returns:
			None: 
		"""
		pass

	def SetMemento(self, aimemento: IMemento) -> bool:
		"""No Description

		Args:
			aimemento(IMemento): aimemento

		Returns:
			bool: 
		"""
		pass

	def StringFromDoubleUnit(self, adouble: float, aunit: Unit) -> str:
		"""No Description

		Args:
			adouble(float): adouble
			aunit(Unit): aunit

		Returns:
			str: 
		"""
		pass

	@property
	def DecimalDigits(self) -> int:
		"""No Description

		Returns:
			NumericFormatter: 
		"""
		pass

	@property
	def Dimension(self) -> Dimension:
		"""No Description

		Returns:
			NumericFormatter: 
		"""
		pass

	@property
	def DisplayUnit(self) -> Unit:
		"""No Description

		Returns:
			NumericFormatter: 
		"""
		pass

	@property
	def DisplayUnitLabel(self) -> str:
		"""No Description

		Returns:
			NumericFormatter: 
		"""
		pass

	@property
	def FormatCode(self) -> str:
		"""No Description

		Returns:
			NumericFormatter: 
		"""
		pass

	@property
	def Label(self) -> str:
		"""No Description

		Returns:
			NumericFormatter: 
		"""
		pass

	@property
	def LabelKey(self) -> str:
		"""No Description

		Returns:
			NumericFormatter: 
		"""
		pass

	@property
	def Name(self) -> str:
		"""No Description

		Returns:
			NumericFormatter: 
		"""
		pass

	@property
	def NumericFormatterId(self) -> int:
		"""No Description

		Returns:
			NumericFormatter: 
		"""
		pass

	@property
	def IsStandardFormatter(self) -> bool:
		"""No Description

		Returns:
			NumericFormatter: 
		"""
		pass

	@property
	def Places(self) -> int:
		"""No Description

		Returns:
			NumericFormatter: 
		"""
		pass

	@property
	def DateTimeFormatForBinding(self) -> int:
		"""No Description

		Returns:
			NumericFormatter: 
		"""
		pass

	@property
	def ShortLabel(self) -> str:
		"""No Description

		Returns:
			NumericFormatter: 
		"""
		pass

	@property
	def XmlDisplayUnit(self) -> str:
		"""No Description

		Returns:
			NumericFormatter: 
		"""
		pass

	@DecimalDigits.setter
	def DecimalDigits(self, decimaldigits: int) -> None:
		pass

	@DisplayUnit.setter
	def DisplayUnit(self, displayunit: Unit) -> None:
		pass

	@FormatCode.setter
	def FormatCode(self, formatcode: str) -> None:
		pass

	@Name.setter
	def Name(self, name: str) -> None:
		pass

	@NumericFormatterId.setter
	def NumericFormatterId(self, numericformatterid: int) -> None:
		pass

	@Places.setter
	def Places(self, places: int) -> None:
		pass

	@DateTimeFormatForBinding.setter
	def DateTimeFormatForBinding(self, datetimeformatforbinding: int) -> None:
		pass

	@XmlDisplayUnit.setter
	def XmlDisplayUnit(self, xmldisplayunit: str) -> None:
		pass

class StationFormatter(INamable, IMementoable, ILabeled):

	def __init__(self, aintId: int, asName: str, aunit: Unit, asFormatCode: str, aintDecimalDigits: int, aintId: int, asName: str, asFormatCode: str, aintDecimalDigits: int, aunitDisplayDefaultSi: Unit, aunitDisplayDefaultUs: Unit, aintId: int, asName: str, aunit: Unit, asFormatCode: str, aintDecimalDigits: int, aunitDisplayDefaultSi: Unit, aunitDisplayDefaultUs: Unit) -> None:
		"""No Description

		Args:
			aintId(int): aintId
			asName(str): asName
			aunit(Unit): aunit
			asFormatCode(str): asFormatCode
			aintDecimalDigits(int): aintDecimalDigits
			aintId(int): aintId
			asName(str): asName
			asFormatCode(str): asFormatCode
			aintDecimalDigits(int): aintDecimalDigits
			aunitDisplayDefaultSi(Unit): aunitDisplayDefaultSi
			aunitDisplayDefaultUs(Unit): aunitDisplayDefaultUs
			aintId(int): aintId
			asName(str): asName
			aunit(Unit): aunit
			asFormatCode(str): asFormatCode
			aintDecimalDigits(int): aintDecimalDigits
			aunitDisplayDefaultSi(Unit): aunitDisplayDefaultSi
			aunitDisplayDefaultUs(Unit): aunitDisplayDefaultUs
		"""
		pass

	def DoubleUnitFromString(self, aunit: Unit, astring: str) -> float:
		"""No Description

		Args:
			aunit(Unit): aunit
			astring(str): astring

		Returns:
			float: 
		"""
		pass

	def InitializeFrom(self, anf: NumericFormatter) -> None:
		"""No Description

		Args:
			anf(NumericFormatter): anf

		Returns:
			None: 
		"""
		pass

	def StringFromDoubleUnit(self, adouble: float, aunit: Unit) -> str:
		"""No Description

		Args:
			adouble(float): adouble
			aunit(Unit): aunit

		Returns:
			str: 
		"""
		pass

	def add_DecimalDigitsChanged(self, value: EventHandler) -> None:
		"""No Description

		Args:
			value(EventHandler): value

		Returns:
			None: 
		"""
		pass

	def remove_DecimalDigitsChanged(self, value: EventHandler) -> None:
		"""No Description

		Args:
			value(EventHandler): value

		Returns:
			None: 
		"""
		pass

	def add_DisplayUnitChanged(self, value: EventHandler) -> None:
		"""No Description

		Args:
			value(EventHandler): value

		Returns:
			None: 
		"""
		pass

	def remove_DisplayUnitChanged(self, value: EventHandler) -> None:
		"""No Description

		Args:
			value(EventHandler): value

		Returns:
			None: 
		"""
		pass

	def add_FormatCodeChanged(self, value: EventHandler) -> None:
		"""No Description

		Args:
			value(EventHandler): value

		Returns:
			None: 
		"""
		pass

	def remove_FormatCodeChanged(self, value: EventHandler) -> None:
		"""No Description

		Args:
			value(EventHandler): value

		Returns:
			None: 
		"""
		pass

	def CreateMemento(self) -> IMemento:
		"""No Description

		Returns:
			IMemento: 
		"""
		pass

	def DoubleFromDoubleUnit(self, adouble: float, aunit: Unit) -> float:
		"""No Description

		Args:
			adouble(float): adouble
			aunit(Unit): aunit

		Returns:
			float: 
		"""
		pass

	def DoubleUnitFromDouble(self, aunit: Unit, adouble: float) -> float:
		"""No Description

		Args:
			aunit(Unit): aunit
			adouble(float): adouble

		Returns:
			float: 
		"""
		pass

	def InitializeDefaultsFrom(self, anf: NumericFormatter) -> None:
		"""No Description

		Args:
			anf(NumericFormatter): anf

		Returns:
			None: 
		"""
		pass

	def ResetDefault(self, aunitsystem: UnitSystem) -> None:
		"""No Description

		Args:
			aunitsystem(UnitSystem): aunitsystem

		Returns:
			None: 
		"""
		pass

	def SetMemento(self, aimemento: IMemento) -> bool:
		"""No Description

		Args:
			aimemento(IMemento): aimemento

		Returns:
			bool: 
		"""
		pass

	@property
	def Places(self) -> int:
		"""No Description

		Returns:
			StationFormatter: 
		"""
		pass

	@property
	def DecimalDigits(self) -> int:
		"""No Description

		Returns:
			StationFormatter: 
		"""
		pass

	@property
	def Dimension(self) -> Dimension:
		"""No Description

		Returns:
			StationFormatter: 
		"""
		pass

	@property
	def DisplayUnit(self) -> Unit:
		"""No Description

		Returns:
			StationFormatter: 
		"""
		pass

	@property
	def DisplayUnitLabel(self) -> str:
		"""No Description

		Returns:
			StationFormatter: 
		"""
		pass

	@property
	def FormatCode(self) -> str:
		"""No Description

		Returns:
			StationFormatter: 
		"""
		pass

	@property
	def Label(self) -> str:
		"""No Description

		Returns:
			StationFormatter: 
		"""
		pass

	@property
	def LabelKey(self) -> str:
		"""No Description

		Returns:
			StationFormatter: 
		"""
		pass

	@property
	def Name(self) -> str:
		"""No Description

		Returns:
			StationFormatter: 
		"""
		pass

	@property
	def NumericFormatterId(self) -> int:
		"""No Description

		Returns:
			StationFormatter: 
		"""
		pass

	@property
	def IsStandardFormatter(self) -> bool:
		"""No Description

		Returns:
			StationFormatter: 
		"""
		pass

	@property
	def DateTimeFormatForBinding(self) -> int:
		"""No Description

		Returns:
			StationFormatter: 
		"""
		pass

	@property
	def ShortLabel(self) -> str:
		"""No Description

		Returns:
			StationFormatter: 
		"""
		pass

	@property
	def XmlDisplayUnit(self) -> str:
		"""No Description

		Returns:
			StationFormatter: 
		"""
		pass

	@Places.setter
	def Places(self, places: int) -> None:
		pass

	@DecimalDigits.setter
	def DecimalDigits(self, decimaldigits: int) -> None:
		pass

	@DisplayUnit.setter
	def DisplayUnit(self, displayunit: Unit) -> None:
		pass

	@FormatCode.setter
	def FormatCode(self, formatcode: str) -> None:
		pass

	@Name.setter
	def Name(self, name: str) -> None:
		pass

	@NumericFormatterId.setter
	def NumericFormatterId(self, numericformatterid: int) -> None:
		pass

	@DateTimeFormatForBinding.setter
	def DateTimeFormatForBinding(self, datetimeformatforbinding: int) -> None:
		pass

	@XmlDisplayUnit.setter
	def XmlDisplayUnit(self, xmldisplayunit: str) -> None:
		pass

class DateTimeFormatter(INamable, IMementoable, ILabeled):

	def __init__(self, aintId: int, asName: str, aunit: Unit, asFormatCode: str, aintDecimalDigits: int, baseDateTimeDelegate: BaseDateTimeDelegate, aintId: int, asName: str, asFormatCode: str, aintDecimalDigits: int, aunitDisplayDefaultSi: Unit, aunitDisplayDefaultUs: Unit, baseDateTimeDelegate: BaseDateTimeDelegate, aintId: int, asName: str, aunit: Unit, asFormatCode: str, aintDecimalDigits: int, aunitDisplayDefaultSi: Unit, aunitDisplayDefaultUs: Unit, baseDateTimeDelegate: BaseDateTimeDelegate) -> None:
		"""No Description

		Args:
			aintId(int): aintId
			asName(str): asName
			aunit(Unit): aunit
			asFormatCode(str): asFormatCode
			aintDecimalDigits(int): aintDecimalDigits
			baseDateTimeDelegate(BaseDateTimeDelegate): baseDateTimeDelegate
			aintId(int): aintId
			asName(str): asName
			asFormatCode(str): asFormatCode
			aintDecimalDigits(int): aintDecimalDigits
			aunitDisplayDefaultSi(Unit): aunitDisplayDefaultSi
			aunitDisplayDefaultUs(Unit): aunitDisplayDefaultUs
			baseDateTimeDelegate(BaseDateTimeDelegate): baseDateTimeDelegate
			aintId(int): aintId
			asName(str): asName
			aunit(Unit): aunit
			asFormatCode(str): asFormatCode
			aintDecimalDigits(int): aintDecimalDigits
			aunitDisplayDefaultSi(Unit): aunitDisplayDefaultSi
			aunitDisplayDefaultUs(Unit): aunitDisplayDefaultUs
			baseDateTimeDelegate(BaseDateTimeDelegate): baseDateTimeDelegate
		"""
		pass

	def DoubleUnitFromString(self, aunit: Unit, astring: str) -> float:
		"""No Description

		Args:
			aunit(Unit): aunit
			astring(str): astring

		Returns:
			float: 
		"""
		pass

	def InitializeFrom(self, anf: NumericFormatter) -> None:
		"""No Description

		Args:
			anf(NumericFormatter): anf

		Returns:
			None: 
		"""
		pass

	def StringFromDoubleUnit(self, adouble: float, aunit: Unit) -> str:
		"""No Description

		Args:
			adouble(float): adouble
			aunit(Unit): aunit

		Returns:
			str: 
		"""
		pass

	def SetDateTimeFormat(self, dateTimeFormat: DateTimeFormats) -> None:
		"""No Description

		Args:
			dateTimeFormat(DateTimeFormats): dateTimeFormat

		Returns:
			None: 
		"""
		pass

	def SetDateTimeFormatString(self, formatString: str, formatIncludesDate: bool, formatIncludesTime: bool) -> None:
		"""No Description

		Args:
			formatString(str): formatString
			formatIncludesDate(bool): formatIncludesDate
			formatIncludesTime(bool): formatIncludesTime

		Returns:
			None: 
		"""
		pass

	def add_DecimalDigitsChanged(self, value: EventHandler) -> None:
		"""No Description

		Args:
			value(EventHandler): value

		Returns:
			None: 
		"""
		pass

	def remove_DecimalDigitsChanged(self, value: EventHandler) -> None:
		"""No Description

		Args:
			value(EventHandler): value

		Returns:
			None: 
		"""
		pass

	def add_DisplayUnitChanged(self, value: EventHandler) -> None:
		"""No Description

		Args:
			value(EventHandler): value

		Returns:
			None: 
		"""
		pass

	def remove_DisplayUnitChanged(self, value: EventHandler) -> None:
		"""No Description

		Args:
			value(EventHandler): value

		Returns:
			None: 
		"""
		pass

	def add_FormatCodeChanged(self, value: EventHandler) -> None:
		"""No Description

		Args:
			value(EventHandler): value

		Returns:
			None: 
		"""
		pass

	def remove_FormatCodeChanged(self, value: EventHandler) -> None:
		"""No Description

		Args:
			value(EventHandler): value

		Returns:
			None: 
		"""
		pass

	def CreateMemento(self) -> IMemento:
		"""No Description

		Returns:
			IMemento: 
		"""
		pass

	def DoubleFromDoubleUnit(self, adouble: float, aunit: Unit) -> float:
		"""No Description

		Args:
			adouble(float): adouble
			aunit(Unit): aunit

		Returns:
			float: 
		"""
		pass

	def DoubleUnitFromDouble(self, aunit: Unit, adouble: float) -> float:
		"""No Description

		Args:
			aunit(Unit): aunit
			adouble(float): adouble

		Returns:
			float: 
		"""
		pass

	def InitializeDefaultsFrom(self, anf: NumericFormatter) -> None:
		"""No Description

		Args:
			anf(NumericFormatter): anf

		Returns:
			None: 
		"""
		pass

	def ResetDefault(self, aunitsystem: UnitSystem) -> None:
		"""No Description

		Args:
			aunitsystem(UnitSystem): aunitsystem

		Returns:
			None: 
		"""
		pass

	def SetMemento(self, aimemento: IMemento) -> bool:
		"""No Description

		Args:
			aimemento(IMemento): aimemento

		Returns:
			bool: 
		"""
		pass

	@property
	def DateTimeFormatString(self) -> str:
		"""No Description

		Returns:
			DateTimeFormatter: 
		"""
		pass

	@property
	def FullDateTimeFormatString(self) -> str:
		"""No Description

		Returns:
			DateTimeFormatter: 
		"""
		pass

	@property
	def DateTimeFormatForBinding(self) -> int:
		"""No Description

		Returns:
			DateTimeFormatter: 
		"""
		pass

	@property
	def DateTimeFormat(self) -> DateTimeFormats:
		"""No Description

		Returns:
			DateTimeFormatter: 
		"""
		pass

	@property
	def HasUnitToDisplay(self) -> bool:
		"""No Description

		Returns:
			DateTimeFormatter: 
		"""
		pass

	@property
	def FormatCode(self) -> str:
		"""No Description

		Returns:
			DateTimeFormatter: 
		"""
		pass

	@property
	def DecimalDigits(self) -> int:
		"""No Description

		Returns:
			DateTimeFormatter: 
		"""
		pass

	@property
	def Dimension(self) -> Dimension:
		"""No Description

		Returns:
			DateTimeFormatter: 
		"""
		pass

	@property
	def DisplayUnit(self) -> Unit:
		"""No Description

		Returns:
			DateTimeFormatter: 
		"""
		pass

	@property
	def DisplayUnitLabel(self) -> str:
		"""No Description

		Returns:
			DateTimeFormatter: 
		"""
		pass

	@property
	def Label(self) -> str:
		"""No Description

		Returns:
			DateTimeFormatter: 
		"""
		pass

	@property
	def LabelKey(self) -> str:
		"""No Description

		Returns:
			DateTimeFormatter: 
		"""
		pass

	@property
	def Name(self) -> str:
		"""No Description

		Returns:
			DateTimeFormatter: 
		"""
		pass

	@property
	def NumericFormatterId(self) -> int:
		"""No Description

		Returns:
			DateTimeFormatter: 
		"""
		pass

	@property
	def IsStandardFormatter(self) -> bool:
		"""No Description

		Returns:
			DateTimeFormatter: 
		"""
		pass

	@property
	def Places(self) -> int:
		"""No Description

		Returns:
			DateTimeFormatter: 
		"""
		pass

	@property
	def ShortLabel(self) -> str:
		"""No Description

		Returns:
			DateTimeFormatter: 
		"""
		pass

	@property
	def XmlDisplayUnit(self) -> str:
		"""No Description

		Returns:
			DateTimeFormatter: 
		"""
		pass

	@DateTimeFormatForBinding.setter
	def DateTimeFormatForBinding(self, datetimeformatforbinding: int) -> None:
		pass

	@DateTimeFormat.setter
	def DateTimeFormat(self, datetimeformat: DateTimeFormats) -> None:
		pass

	@FormatCode.setter
	def FormatCode(self, formatcode: str) -> None:
		pass

	@DecimalDigits.setter
	def DecimalDigits(self, decimaldigits: int) -> None:
		pass

	@DisplayUnit.setter
	def DisplayUnit(self, displayunit: Unit) -> None:
		pass

	@Name.setter
	def Name(self, name: str) -> None:
		pass

	@NumericFormatterId.setter
	def NumericFormatterId(self, numericformatterid: int) -> None:
		pass

	@Places.setter
	def Places(self, places: int) -> None:
		pass

	@XmlDisplayUnit.setter
	def XmlDisplayUnit(self, xmldisplayunit: str) -> None:
		pass

class Unit(INamable):

	def __init__(self, astringName: str, adimension: Dimension, aunitsystem: UnitSystem, adouble: float, aintEnumValue: int, astringName: str, adimension: Dimension, aunitsystem: UnitSystem, adouble: float, aintEnumValue: int, bentleyName: str, astringName: str, adimension: Dimension, aunitsystem: UnitSystem, aiunitconverter: IUnitConverter, aintEnumValue: int, astringName: str, adimension: Dimension, aunitsystem: UnitSystem, aiunitconverter: IUnitConverter, aintEnumValue: int, bentleyName: str) -> None:
		"""No Description

		Args:
			astringName(str): astringName
			adimension(Dimension): adimension
			aunitsystem(UnitSystem): aunitsystem
			adouble(float): adouble
			aintEnumValue(int): aintEnumValue
			astringName(str): astringName
			adimension(Dimension): adimension
			aunitsystem(UnitSystem): aunitsystem
			adouble(float): adouble
			aintEnumValue(int): aintEnumValue
			bentleyName(str): bentleyName
			astringName(str): astringName
			adimension(Dimension): adimension
			aunitsystem(UnitSystem): aunitsystem
			aiunitconverter(IUnitConverter): aiunitconverter
			aintEnumValue(int): aintEnumValue
			astringName(str): astringName
			adimension(Dimension): adimension
			aunitsystem(UnitSystem): aunitsystem
			aiunitconverter(IUnitConverter): aiunitconverter
			aintEnumValue(int): aintEnumValue
			bentleyName(str): bentleyName
		"""
		pass

	@staticmethod
	def FromDimensionEnum(adimension: Dimension, aint: int) -> Unit:
		"""No Description

		Args:
			adimension(Dimension): adimension
			aint(int): aint

		Returns:
			Unit: 
		"""
		pass

	@staticmethod
	def FromDimensionName(adimension: Dimension, asNameUnit: str) -> Unit:
		"""No Description

		Args:
			adimension(Dimension): adimension
			asNameUnit(str): asNameUnit

		Returns:
			Unit: 
		"""
		pass

	@staticmethod
	def FromLabel(adimension: Dimension, aUnitLabel: str) -> Unit:
		"""No Description

		Args:
			adimension(Dimension): adimension
			aUnitLabel(str): aUnitLabel

		Returns:
			Unit: 
		"""
		pass

	@staticmethod
	def FromIndex(aindex: UnitIndex) -> Unit:
		"""No Description

		Args:
			aindex(UnitIndex): aindex

		Returns:
			Unit: 
		"""
		pass

	@staticmethod
	def FromSerializedString(astring: str) -> Unit:
		"""No Description

		Args:
			astring(str): astring

		Returns:
			Unit: 
		"""
		pass

	def ConvertFrom(self, adouble: float, aunit: Unit) -> float:
		"""No Description

		Args:
			adouble(float): adouble
			aunit(Unit): aunit

		Returns:
			float: 
		"""
		pass

	def ConversionFactor(self, aunit: Unit) -> float:
		"""No Description

		Args:
			aunit(Unit): aunit

		Returns:
			float: 
		"""
		pass

	def ToSerializedString(self) -> str:
		"""No Description

		Returns:
			str: 
		"""
		pass

	@property
	@staticmethod
	def PercentPerSecondPerKiloPascal() -> Unit:
		"""No Description

		Returns:
			Unit: 
		"""
		pass

	@property
	@staticmethod
	def PercentPerSecondPerPSI() -> Unit:
		"""No Description

		Returns:
			Unit: 
		"""
		pass

	@property
	@staticmethod
	def PercentPerSecondPerCubicFeetPerSecond() -> Unit:
		"""No Description

		Returns:
			Unit: 
		"""
		pass

	@property
	@staticmethod
	def PercentPerSecondPerCubicFeetPerMinute() -> Unit:
		"""No Description

		Returns:
			Unit: 
		"""
		pass

	@property
	@staticmethod
	def PercentPerSecondPerCubicMeterPerSecond() -> Unit:
		"""No Description

		Returns:
			Unit: 
		"""
		pass

	@property
	@staticmethod
	def PercentPerSecondPerCubicMeterPerMinute() -> Unit:
		"""No Description

		Returns:
			Unit: 
		"""
		pass

	@property
	@staticmethod
	def PercentPerSecondPerLiterPerSecond() -> Unit:
		"""No Description

		Returns:
			Unit: 
		"""
		pass

	@property
	@staticmethod
	def PercentPerSecondPerLiterPerMinute() -> Unit:
		"""No Description

		Returns:
			Unit: 
		"""
		pass

	@property
	@staticmethod
	def PercentPerSecondPerGalPerSecond() -> Unit:
		"""No Description

		Returns:
			Unit: 
		"""
		pass

	@property
	@staticmethod
	def PercentPerSecondPerGalPerMinute() -> Unit:
		"""No Description

		Returns:
			Unit: 
		"""
		pass

	@property
	@staticmethod
	def MetersPerSquareSecond() -> Unit:
		"""No Description

		Returns:
			Unit: 
		"""
		pass

	@property
	@staticmethod
	def FeetPerSquareSecond() -> Unit:
		"""No Description

		Returns:
			Unit: 
		"""
		pass

	@property
	@staticmethod
	def DrainCoeffInchesPerHour() -> Unit:
		"""No Description

		Returns:
			Unit: 
		"""
		pass

	@property
	@staticmethod
	def DrainCoeffMMPerHour() -> Unit:
		"""No Description

		Returns:
			Unit: 
		"""
		pass

	@property
	@staticmethod
	def MilligramsPerSquareCentimeter() -> Unit:
		"""No Description

		Returns:
			Unit: 
		"""
		pass

	@property
	@staticmethod
	def MilligramsPerSquareFeet() -> Unit:
		"""No Description

		Returns:
			Unit: 
		"""
		pass

	@property
	@staticmethod
	def MilligramsPerSquareMeter() -> Unit:
		"""No Description

		Returns:
			Unit: 
		"""
		pass

	@property
	@staticmethod
	def MicrogramsPerSquareCentimeter() -> Unit:
		"""No Description

		Returns:
			Unit: 
		"""
		pass

	@property
	@staticmethod
	def MicrogramsPerSquareFeet() -> Unit:
		"""No Description

		Returns:
			Unit: 
		"""
		pass

	@property
	@staticmethod
	def MicrogramsPerSquareMeter() -> Unit:
		"""No Description

		Returns:
			Unit: 
		"""
		pass

	@property
	@staticmethod
	def MolesPerLiter() -> Unit:
		"""No Description

		Returns:
			Unit: 
		"""
		pass

	@property
	@staticmethod
	def MilliMolesPerLiter() -> Unit:
		"""No Description

		Returns:
			Unit: 
		"""
		pass

	@property
	@staticmethod
	def NumbersPerLiter() -> Unit:
		"""No Description

		Returns:
			Unit: 
		"""
		pass

	@property
	@staticmethod
	def ThousandNumbersPerLiter() -> Unit:
		"""No Description

		Returns:
			Unit: 
		"""
		pass

	@property
	@staticmethod
	def MillionNumbersPerLiter() -> Unit:
		"""No Description

		Returns:
			Unit: 
		"""
		pass

	@property
	@staticmethod
	def MolesPerSquareMeter() -> Unit:
		"""No Description

		Returns:
			Unit: 
		"""
		pass

	@property
	@staticmethod
	def MolesPerSquareCentimeter() -> Unit:
		"""No Description

		Returns:
			Unit: 
		"""
		pass

	@property
	@staticmethod
	def MolesPerSquareFeet() -> Unit:
		"""No Description

		Returns:
			Unit: 
		"""
		pass

	@property
	@staticmethod
	def MilliMolesPerSquareMeter() -> Unit:
		"""No Description

		Returns:
			Unit: 
		"""
		pass

	@property
	@staticmethod
	def MilliMolesPerSquareCentimeter() -> Unit:
		"""No Description

		Returns:
			Unit: 
		"""
		pass

	@property
	@staticmethod
	def MilliMolesPerSquareFeet() -> Unit:
		"""No Description

		Returns:
			Unit: 
		"""
		pass

	@property
	@staticmethod
	def NumbersPerSquareMeter() -> Unit:
		"""No Description

		Returns:
			Unit: 
		"""
		pass

	@property
	@staticmethod
	def NumbersPerSquareCentimeter() -> Unit:
		"""No Description

		Returns:
			Unit: 
		"""
		pass

	@property
	@staticmethod
	def NumbersPerSquareFeet() -> Unit:
		"""No Description

		Returns:
			Unit: 
		"""
		pass

	@property
	@staticmethod
	def ThousandNumbersPerSquareMeter() -> Unit:
		"""No Description

		Returns:
			Unit: 
		"""
		pass

	@property
	@staticmethod
	def ThousandNumbersPerSquareCentimeter() -> Unit:
		"""No Description

		Returns:
			Unit: 
		"""
		pass

	@property
	@staticmethod
	def ThousandNumbersPerSquareFeet() -> Unit:
		"""No Description

		Returns:
			Unit: 
		"""
		pass

	@property
	@staticmethod
	def MillionNumbersPerSquareMeter() -> Unit:
		"""No Description

		Returns:
			Unit: 
		"""
		pass

	@property
	@staticmethod
	def MillionNumbersPerSquareCentimeter() -> Unit:
		"""No Description

		Returns:
			Unit: 
		"""
		pass

	@property
	@staticmethod
	def MillionNumbersPerSquareFeet() -> Unit:
		"""No Description

		Returns:
			Unit: 
		"""
		pass

	@property
	@staticmethod
	def CubicFeetPerMilePerSecond() -> Unit:
		"""No Description

		Returns:
			Unit: 
		"""
		pass

	@property
	@staticmethod
	def LitersPerKilometerPerSecond() -> Unit:
		"""No Description

		Returns:
			Unit: 
		"""
		pass

	@property
	@staticmethod
	def QuadFootPerSecond() -> Unit:
		"""No Description

		Returns:
			Unit: 
		"""
		pass

	@property
	@staticmethod
	def GallonsPerFootPerMinute() -> Unit:
		"""No Description

		Returns:
			Unit: 
		"""
		pass

	@property
	@staticmethod
	def GallonsPerMilePerMinute() -> Unit:
		"""No Description

		Returns:
			Unit: 
		"""
		pass

	@property
	@staticmethod
	def QuadMetersPerSecond() -> Unit:
		"""No Description

		Returns:
			Unit: 
		"""
		pass

	@property
	@staticmethod
	def CubicMetersPerKilometerPerSecond() -> Unit:
		"""No Description

		Returns:
			Unit: 
		"""
		pass

	@property
	@staticmethod
	def LitersPerMetersPerSecond() -> Unit:
		"""No Description

		Returns:
			Unit: 
		"""
		pass

	@property
	def Dimension(self) -> Dimension:
		"""No Description

		Returns:
			Unit: 
		"""
		pass

	@property
	def EnumValue(self) -> int:
		"""No Description

		Returns:
			Unit: 
		"""
		pass

	@property
	def Label(self) -> str:
		"""No Description

		Returns:
			Unit: 
		"""
		pass

	@property
	def LabelKey(self) -> str:
		"""No Description

		Returns:
			Unit: 
		"""
		pass

	@property
	def Name(self) -> str:
		"""No Description

		Returns:
			Unit: 
		"""
		pass

	@property
	def BentleyName(self) -> str:
		"""No Description

		Returns:
			Unit: 
		"""
		pass

	@property
	def ShortLabel(self) -> str:
		"""No Description

		Returns:
			Unit: 
		"""
		pass

	@property
	def UnitSystem(self) -> UnitSystem:
		"""No Description

		Returns:
			Unit: 
		"""
		pass

	@property
	@staticmethod
	def ThousandGallons() -> Unit:
		"""No Description

		Returns:
			Unit: 
		"""
		pass

	@property
	@staticmethod
	def ThousandLiters() -> Unit:
		"""No Description

		Returns:
			Unit: 
		"""
		pass

	@property
	@staticmethod
	def ThousandSquareFeet() -> Unit:
		"""No Description

		Returns:
			Unit: 
		"""
		pass

	@property
	@staticmethod
	def TonnesPerMegaJoule() -> Unit:
		"""No Description

		Returns:
			Unit: 
		"""
		pass

	@property
	@staticmethod
	def TonnesPerYear() -> Unit:
		"""No Description

		Returns:
			Unit: 
		"""
		pass

	@property
	@staticmethod
	def UnitlessPercent() -> Unit:
		"""No Description

		Returns:
			Unit: 
		"""
		pass

	@property
	@staticmethod
	def UnitlessUnit() -> Unit:
		"""No Description

		Returns:
			Unit: 
		"""
		pass

	@property
	@staticmethod
	def USSurveyFoot() -> Unit:
		"""No Description

		Returns:
			Unit: 
		"""
		pass

	@property
	@staticmethod
	def VelocityCentimetersPerHour() -> Unit:
		"""No Description

		Returns:
			Unit: 
		"""
		pass

	@property
	@staticmethod
	def VelocityCentimetersPerMinute() -> Unit:
		"""No Description

		Returns:
			Unit: 
		"""
		pass

	@property
	@staticmethod
	def VelocityCentimetersPerSecond() -> Unit:
		"""No Description

		Returns:
			Unit: 
		"""
		pass

	@property
	@staticmethod
	def VelocityFeetPerHour() -> Unit:
		"""No Description

		Returns:
			Unit: 
		"""
		pass

	@property
	@staticmethod
	def VelocityFeetPerMinute() -> Unit:
		"""No Description

		Returns:
			Unit: 
		"""
		pass

	@property
	@staticmethod
	def VelocityFeetPerSecond() -> Unit:
		"""No Description

		Returns:
			Unit: 
		"""
		pass

	@property
	@staticmethod
	def VelocityInchesPerHour() -> Unit:
		"""No Description

		Returns:
			Unit: 
		"""
		pass

	@property
	@staticmethod
	def VelocityInchesPerMinute() -> Unit:
		"""No Description

		Returns:
			Unit: 
		"""
		pass

	@property
	@staticmethod
	def VelocityInchesPerSecond() -> Unit:
		"""No Description

		Returns:
			Unit: 
		"""
		pass

	@property
	@staticmethod
	def VelocityKilometersPerHour() -> Unit:
		"""No Description

		Returns:
			Unit: 
		"""
		pass

	@property
	@staticmethod
	def VelocityKnot() -> Unit:
		"""No Description

		Returns:
			Unit: 
		"""
		pass

	@property
	@staticmethod
	def VelocityKnotInternational() -> Unit:
		"""No Description

		Returns:
			Unit: 
		"""
		pass

	@property
	@staticmethod
	def VelocityMetersPerHour() -> Unit:
		"""No Description

		Returns:
			Unit: 
		"""
		pass

	@property
	@staticmethod
	def VelocityMetersPerMinute() -> Unit:
		"""No Description

		Returns:
			Unit: 
		"""
		pass

	@property
	@staticmethod
	def VelocityMetersPerSecond() -> Unit:
		"""No Description

		Returns:
			Unit: 
		"""
		pass

	@property
	@staticmethod
	def VelocityMilePerHour() -> Unit:
		"""No Description

		Returns:
			Unit: 
		"""
		pass

	@property
	@staticmethod
	def VerticalPerHorizontal() -> Unit:
		"""No Description

		Returns:
			Unit: 
		"""
		pass

	@property
	@staticmethod
	def Watts() -> Unit:
		"""No Description

		Returns:
			Unit: 
		"""
		pass

	@property
	@staticmethod
	def WeirCoefficientSi() -> Unit:
		"""No Description

		Returns:
			Unit: 
		"""
		pass

	@property
	@staticmethod
	def WeirCoefficientUs() -> Unit:
		"""No Description

		Returns:
			Unit: 
		"""
		pass

	@property
	@staticmethod
	def Yards() -> Unit:
		"""No Description

		Returns:
			Unit: 
		"""
		pass

	@property
	@staticmethod
	def Years() -> Unit:
		"""No Description

		Returns:
			Unit: 
		"""
		pass

	@property
	@staticmethod
	def InchMiles() -> Unit:
		"""No Description

		Returns:
			Unit: 
		"""
		pass

	@property
	@staticmethod
	def InchFeet() -> Unit:
		"""No Description

		Returns:
			Unit: 
		"""
		pass

	@property
	@staticmethod
	def FootMiles() -> Unit:
		"""No Description

		Returns:
			Unit: 
		"""
		pass

	@property
	@staticmethod
	def FootFeet() -> Unit:
		"""No Description

		Returns:
			Unit: 
		"""
		pass

	@property
	@staticmethod
	def MillimeterMeters() -> Unit:
		"""No Description

		Returns:
			Unit: 
		"""
		pass

	@property
	@staticmethod
	def MillimeterKilometers() -> Unit:
		"""No Description

		Returns:
			Unit: 
		"""
		pass

	@property
	@staticmethod
	def MeterMeters() -> Unit:
		"""No Description

		Returns:
			Unit: 
		"""
		pass

	@property
	@staticmethod
	def MeterKilometers() -> Unit:
		"""No Description

		Returns:
			Unit: 
		"""
		pass

	@property
	@staticmethod
	def InchMeters() -> Unit:
		"""No Description

		Returns:
			Unit: 
		"""
		pass

	@property
	@staticmethod
	def MillimeterMiles() -> Unit:
		"""No Description

		Returns:
			Unit: 
		"""
		pass

	@property
	@staticmethod
	def PoundsPerAcre() -> Unit:
		"""No Description

		Returns:
			Unit: 
		"""
		pass

	@property
	@staticmethod
	def KilogramsPerHectare() -> Unit:
		"""No Description

		Returns:
			Unit: 
		"""
		pass

	@property
	@staticmethod
	def DollarsPerKiloWatt() -> Unit:
		"""No Description

		Returns:
			Unit: 
		"""
		pass

	@property
	@staticmethod
	def DollarsPerHorsepower() -> Unit:
		"""No Description

		Returns:
			Unit: 
		"""
		pass

	@property
	@staticmethod
	def DollarsPerCubicCentimeters() -> Unit:
		"""No Description

		Returns:
			Unit: 
		"""
		pass

	@property
	@staticmethod
	def DollarsPerLiters() -> Unit:
		"""No Description

		Returns:
			Unit: 
		"""
		pass

	@property
	@staticmethod
	def DollarsPerCubicMeters() -> Unit:
		"""No Description

		Returns:
			Unit: 
		"""
		pass

	@property
	@staticmethod
	def DollarsPerCubicInches() -> Unit:
		"""No Description

		Returns:
			Unit: 
		"""
		pass

	@property
	@staticmethod
	def DollarsPerGallons() -> Unit:
		"""No Description

		Returns:
			Unit: 
		"""
		pass

	@property
	@staticmethod
	def DollarsPerImpGallons() -> Unit:
		"""No Description

		Returns:
			Unit: 
		"""
		pass

	@property
	@staticmethod
	def DollarsPerCubicFeet() -> Unit:
		"""No Description

		Returns:
			Unit: 
		"""
		pass

	@property
	@staticmethod
	def DollarsPerCubicYards() -> Unit:
		"""No Description

		Returns:
			Unit: 
		"""
		pass

	@property
	@staticmethod
	def DollarsPerAcreInches() -> Unit:
		"""No Description

		Returns:
			Unit: 
		"""
		pass

	@property
	@staticmethod
	def DollarsPerAcreFeet() -> Unit:
		"""No Description

		Returns:
			Unit: 
		"""
		pass

	@property
	@staticmethod
	def DollarsPerMillionGallons() -> Unit:
		"""No Description

		Returns:
			Unit: 
		"""
		pass

	@property
	@staticmethod
	def DollarsPerThousandGallons() -> Unit:
		"""No Description

		Returns:
			Unit: 
		"""
		pass

	@property
	@staticmethod
	def DollarsPerThousandLiters() -> Unit:
		"""No Description

		Returns:
			Unit: 
		"""
		pass

	@property
	@staticmethod
	def DollarsPerMillionLiters() -> Unit:
		"""No Description

		Returns:
			Unit: 
		"""
		pass

	@property
	@staticmethod
	def PoundSquareFeet() -> Unit:
		"""No Description

		Returns:
			Unit: 
		"""
		pass

	@property
	@staticmethod
	def NewtonSquareMeters() -> Unit:
		"""No Description

		Returns:
			Unit: 
		"""
		pass

	@property
	@staticmethod
	def KilogramSquareMeters() -> Unit:
		"""No Description

		Returns:
			Unit: 
		"""
		pass

	@property
	@staticmethod
	def KiloWattHourPerMillionGallons() -> Unit:
		"""No Description

		Returns:
			Unit: 
		"""
		pass

	@property
	@staticmethod
	def KiloWattHourPerMillionLiters() -> Unit:
		"""No Description

		Returns:
			Unit: 
		"""
		pass

	@property
	@staticmethod
	def KiloWattHourPerCubicMeters() -> Unit:
		"""No Description

		Returns:
			Unit: 
		"""
		pass

	@property
	@staticmethod
	def KiloWattHourPerCubicFeet() -> Unit:
		"""No Description

		Returns:
			Unit: 
		"""
		pass

	@property
	@staticmethod
	def PerHour() -> Unit:
		"""No Description

		Returns:
			Unit: 
		"""
		pass

	@property
	@staticmethod
	def NewtonMeters() -> Unit:
		"""No Description

		Returns:
			Unit: 
		"""
		pass

	@property
	@staticmethod
	def PoundFeet() -> Unit:
		"""No Description

		Returns:
			Unit: 
		"""
		pass

	@property
	@staticmethod
	def PoundPerInch() -> Unit:
		"""No Description

		Returns:
			Unit: 
		"""
		pass

	@property
	@staticmethod
	def NewtonPerMillimeter() -> Unit:
		"""No Description

		Returns:
			Unit: 
		"""
		pass

	@property
	@staticmethod
	def PoundForce() -> Unit:
		"""No Description

		Returns:
			Unit: 
		"""
		pass

	@property
	@staticmethod
	def KiloPoundForce() -> Unit:
		"""No Description

		Returns:
			Unit: 
		"""
		pass

	@property
	@staticmethod
	def Newton() -> Unit:
		"""No Description

		Returns:
			Unit: 
		"""
		pass

	@property
	@staticmethod
	def KiloNewton() -> Unit:
		"""No Description

		Returns:
			Unit: 
		"""
		pass

	@property
	@staticmethod
	def SlugPerCubicFoot() -> Unit:
		"""No Description

		Returns:
			Unit: 
		"""
		pass

	@property
	@staticmethod
	def PoundPerCubicFoot() -> Unit:
		"""No Description

		Returns:
			Unit: 
		"""
		pass

	@property
	@staticmethod
	def KilogramPerCubicMeter() -> Unit:
		"""No Description

		Returns:
			Unit: 
		"""
		pass

	@property
	@staticmethod
	def CfsPerSquareRootFooH20() -> Unit:
		"""No Description

		Returns:
			Unit: 
		"""
		pass

	@property
	@staticmethod
	def CmsPerSquareRootMeterH20() -> Unit:
		"""No Description

		Returns:
			Unit: 
		"""
		pass

	@property
	@staticmethod
	def LPerSecPerSquareRootKpa() -> Unit:
		"""No Description

		Returns:
			Unit: 
		"""
		pass

	@property
	@staticmethod
	def GpmPerSquareRootPsi() -> Unit:
		"""No Description

		Returns:
			Unit: 
		"""
		pass

	@property
	@staticmethod
	def Pascals() -> Unit:
		"""No Description

		Returns:
			Unit: 
		"""
		pass

	@property
	@staticmethod
	def HektoPascals() -> Unit:
		"""No Description

		Returns:
			Unit: 
		"""
		pass

	@property
	@staticmethod
	def MegaPascals() -> Unit:
		"""No Description

		Returns:
			Unit: 
		"""
		pass

	@property
	@staticmethod
	def MilliBars() -> Unit:
		"""No Description

		Returns:
			Unit: 
		"""
		pass

	@property
	@staticmethod
	def SideWeirCoefficientSi() -> Unit:
		"""No Description

		Returns:
			Unit: 
		"""
		pass

	@property
	@staticmethod
	def SideWeirCoefficientUs() -> Unit:
		"""No Description

		Returns:
			Unit: 
		"""
		pass

	@property
	@staticmethod
	def CubicFeetPerFoot() -> Unit:
		"""No Description

		Returns:
			Unit: 
		"""
		pass

	@property
	@staticmethod
	def CubicMetersPerMeter() -> Unit:
		"""No Description

		Returns:
			Unit: 
		"""
		pass

	@property
	@staticmethod
	def InchesPerHourPerFeetToKexp() -> Unit:
		"""No Description

		Returns:
			Unit: 
		"""
		pass

	@property
	@staticmethod
	def CentimeterPerHourPerMeterToKexp() -> Unit:
		"""No Description

		Returns:
			Unit: 
		"""
		pass

	@property
	@staticmethod
	def Kelvin() -> Unit:
		"""No Description

		Returns:
			Unit: 
		"""
		pass

	@property
	@staticmethod
	def LitersPerHour() -> Unit:
		"""No Description

		Returns:
			Unit: 
		"""
		pass

	@property
	@staticmethod
	def Tons() -> Unit:
		"""No Description

		Returns:
			Unit: 
		"""
		pass

	@property
	@staticmethod
	def MegaWatts() -> Unit:
		"""No Description

		Returns:
			Unit: 
		"""
		pass

	@property
	@staticmethod
	def GigaWatts() -> Unit:
		"""No Description

		Returns:
			Unit: 
		"""
		pass

	@property
	@staticmethod
	def MegaJoules() -> Unit:
		"""No Description

		Returns:
			Unit: 
		"""
		pass

	@property
	@staticmethod
	def GigaJoules() -> Unit:
		"""No Description

		Returns:
			Unit: 
		"""
		pass

	@property
	@staticmethod
	def WattSeconds() -> Unit:
		"""No Description

		Returns:
			Unit: 
		"""
		pass

	@property
	@staticmethod
	def MegaWattHours() -> Unit:
		"""No Description

		Returns:
			Unit: 
		"""
		pass

	@property
	@staticmethod
	def GigaWattHours() -> Unit:
		"""No Description

		Returns:
			Unit: 
		"""
		pass

	@property
	@staticmethod
	def PascalsPerMeter() -> Unit:
		"""No Description

		Returns:
			Unit: 
		"""
		pass

	@property
	@staticmethod
	def BarsPerKilometer() -> Unit:
		"""No Description

		Returns:
			Unit: 
		"""
		pass

	@property
	@staticmethod
	def PSIPerFoot() -> Unit:
		"""No Description

		Returns:
			Unit: 
		"""
		pass

	@property
	@staticmethod
	def PSIPerInch() -> Unit:
		"""No Description

		Returns:
			Unit: 
		"""
		pass

	@property
	@staticmethod
	def KilogramsPerMeter() -> Unit:
		"""No Description

		Returns:
			Unit: 
		"""
		pass

	@property
	@staticmethod
	def PoundsPerFoot() -> Unit:
		"""No Description

		Returns:
			Unit: 
		"""
		pass

	@property
	@staticmethod
	def PerMeter() -> Unit:
		"""No Description

		Returns:
			Unit: 
		"""
		pass

	@property
	@staticmethod
	def PerMillimeter() -> Unit:
		"""No Description

		Returns:
			Unit: 
		"""
		pass

	@property
	@staticmethod
	def PerPascals() -> Unit:
		"""No Description

		Returns:
			Unit: 
		"""
		pass

	@property
	@staticmethod
	def PerBars() -> Unit:
		"""No Description

		Returns:
			Unit: 
		"""
		pass

	@property
	@staticmethod
	def PerPSI() -> Unit:
		"""No Description

		Returns:
			Unit: 
		"""
		pass

	@property
	@staticmethod
	def KilogramsPerMeterPerSecond() -> Unit:
		"""No Description

		Returns:
			Unit: 
		"""
		pass

	@property
	@staticmethod
	def PoundSecondPerSquareFoot() -> Unit:
		"""No Description

		Returns:
			Unit: 
		"""
		pass

	@property
	@staticmethod
	def JoulesPerCubicMeters() -> Unit:
		"""No Description

		Returns:
			Unit: 
		"""
		pass

	@property
	@staticmethod
	def KiloJoulesPerCubicMeters() -> Unit:
		"""No Description

		Returns:
			Unit: 
		"""
		pass

	@property
	@staticmethod
	def MegaJoulesPerCubicMeters() -> Unit:
		"""No Description

		Returns:
			Unit: 
		"""
		pass

	@property
	@staticmethod
	def KiloWattHoursPerCubicMeters() -> Unit:
		"""No Description

		Returns:
			Unit: 
		"""
		pass

	@property
	@staticmethod
	def WeirCoefficientParameterizedSI() -> Unit:
		"""No Description

		Returns:
			Unit: 
		"""
		pass

	@property
	@staticmethod
	def WeirCoefficientParameterizedUS() -> Unit:
		"""No Description

		Returns:
			Unit: 
		"""
		pass

	@property
	@staticmethod
	def MillimetersPerHourPerDegreeCelsius() -> Unit:
		"""No Description

		Returns:
			Unit: 
		"""
		pass

	@property
	@staticmethod
	def InchesPerHourPerDegreeFahrenheit() -> Unit:
		"""No Description

		Returns:
			Unit: 
		"""
		pass

	@property
	@staticmethod
	def BreaksPerYrPerKm() -> Unit:
		"""No Description

		Returns:
			Unit: 
		"""
		pass

	@property
	@staticmethod
	def BreaksPerYrPerMi() -> Unit:
		"""No Description

		Returns:
			Unit: 
		"""
		pass

	@property
	@staticmethod
	def BreaksPerYrPer1000Ft() -> Unit:
		"""No Description

		Returns:
			Unit: 
		"""
		pass

	@property
	@staticmethod
	def BreaksPerYrPer100Mi() -> Unit:
		"""No Description

		Returns:
			Unit: 
		"""
		pass

	@property
	@staticmethod
	def PercentPerSecondPerMeterH2O() -> Unit:
		"""No Description

		Returns:
			Unit: 
		"""
		pass

	@property
	@staticmethod
	def PercentPerSecondPerFtH2O() -> Unit:
		"""No Description

		Returns:
			Unit: 
		"""
		pass

	@property
	@staticmethod
	def KilogramsPerSecond() -> Unit:
		"""No Description

		Returns:
			Unit: 
		"""
		pass

	@property
	@staticmethod
	def KilogramsPerSquareCentimeter() -> Unit:
		"""No Description

		Returns:
			Unit: 
		"""
		pass

	@property
	@staticmethod
	def KilogramsPerSquareMeter() -> Unit:
		"""No Description

		Returns:
			Unit: 
		"""
		pass

	@property
	@staticmethod
	def KiloJoules() -> Unit:
		"""No Description

		Returns:
			Unit: 
		"""
		pass

	@property
	@staticmethod
	def Kilometers() -> Unit:
		"""No Description

		Returns:
			Unit: 
		"""
		pass

	@property
	@staticmethod
	def KiloNewtonsPerCubicMeter() -> Unit:
		"""No Description

		Returns:
			Unit: 
		"""
		pass

	@property
	@staticmethod
	def KiloPascals() -> Unit:
		"""No Description

		Returns:
			Unit: 
		"""
		pass

	@property
	@staticmethod
	def KiloWattHours() -> Unit:
		"""No Description

		Returns:
			Unit: 
		"""
		pass

	@property
	@staticmethod
	def KilowattHoursPerKilowatt() -> Unit:
		"""No Description

		Returns:
			Unit: 
		"""
		pass

	@property
	@staticmethod
	def Kilowatts() -> Unit:
		"""No Description

		Returns:
			Unit: 
		"""
		pass

	@property
	@staticmethod
	def Liters() -> Unit:
		"""No Description

		Returns:
			Unit: 
		"""
		pass

	@property
	@staticmethod
	def LitersPerCapitaPerDay() -> Unit:
		"""No Description

		Returns:
			Unit: 
		"""
		pass

	@property
	@staticmethod
	def LitersPerDay() -> Unit:
		"""No Description

		Returns:
			Unit: 
		"""
		pass

	@property
	@staticmethod
	def LitersPerDayPerMetersOfH2O() -> Unit:
		"""No Description

		Returns:
			Unit: 
		"""
		pass

	@property
	@staticmethod
	def LitersPerMinute() -> Unit:
		"""No Description

		Returns:
			Unit: 
		"""
		pass

	@property
	@staticmethod
	def LitersPerMinutePerMetersOfH2O() -> Unit:
		"""No Description

		Returns:
			Unit: 
		"""
		pass

	@property
	@staticmethod
	def LitersPerSecond() -> Unit:
		"""No Description

		Returns:
			Unit: 
		"""
		pass

	@property
	@staticmethod
	def LitersPerSecondPerMetersOfH2O() -> Unit:
		"""No Description

		Returns:
			Unit: 
		"""
		pass

	@property
	@staticmethod
	def LitersPerHectaresPerDay() -> Unit:
		"""No Description

		Returns:
			Unit: 
		"""
		pass

	@property
	@staticmethod
	def LitersPerHectaresPerSecond() -> Unit:
		"""No Description

		Returns:
			Unit: 
		"""
		pass

	@property
	@staticmethod
	def LitersPerSquareKilometerPerDay() -> Unit:
		"""No Description

		Returns:
			Unit: 
		"""
		pass

	@property
	@staticmethod
	def LitersPerSquareMeterPerDay() -> Unit:
		"""No Description

		Returns:
			Unit: 
		"""
		pass

	@property
	@staticmethod
	def MegaLitersPerDay() -> Unit:
		"""No Description

		Returns:
			Unit: 
		"""
		pass

	@property
	@staticmethod
	def MegaLitersPerDayPerMetersOfH2O() -> Unit:
		"""No Description

		Returns:
			Unit: 
		"""
		pass

	@property
	@staticmethod
	def MeterHorizontalPerMeterVertical() -> Unit:
		"""No Description

		Returns:
			Unit: 
		"""
		pass

	@property
	@staticmethod
	def MeterPerKilometer() -> Unit:
		"""No Description

		Returns:
			Unit: 
		"""
		pass

	@property
	@staticmethod
	def MeterPerMeter() -> Unit:
		"""No Description

		Returns:
			Unit: 
		"""
		pass

	@property
	@staticmethod
	def Meters() -> Unit:
		"""No Description

		Returns:
			Unit: 
		"""
		pass

	@property
	@staticmethod
	def MetersOfH2O() -> Unit:
		"""No Description

		Returns:
			Unit: 
		"""
		pass

	@property
	@staticmethod
	def MetersPerCm() -> Unit:
		"""No Description

		Returns:
			Unit: 
		"""
		pass

	@property
	@staticmethod
	def MetersPerDay() -> Unit:
		"""No Description

		Returns:
			Unit: 
		"""
		pass

	@property
	@staticmethod
	def MetersPerSecond() -> Unit:
		"""No Description

		Returns:
			Unit: 
		"""
		pass

	@property
	@staticmethod
	def MeterVerticalPerMeterHorizontal() -> Unit:
		"""No Description

		Returns:
			Unit: 
		"""
		pass

	@property
	@staticmethod
	def Mfeet() -> Unit:
		"""No Description

		Returns:
			Unit: 
		"""
		pass

	@property
	@staticmethod
	def MGD() -> Unit:
		"""No Description

		Returns:
			Unit: 
		"""
		pass

	@property
	@staticmethod
	def MGDPerPSI() -> Unit:
		"""No Description

		Returns:
			Unit: 
		"""
		pass

	@property
	@staticmethod
	def MGDImperial() -> Unit:
		"""No Description

		Returns:
			Unit: 
		"""
		pass

	@property
	@staticmethod
	def MGDImperialPerPSI() -> Unit:
		"""No Description

		Returns:
			Unit: 
		"""
		pass

	@property
	@staticmethod
	def MicrogramsPerDay() -> Unit:
		"""No Description

		Returns:
			Unit: 
		"""
		pass

	@property
	@staticmethod
	def MicrogramsPerHour() -> Unit:
		"""No Description

		Returns:
			Unit: 
		"""
		pass

	@property
	@staticmethod
	def MicrogramsPerLiter() -> Unit:
		"""No Description

		Returns:
			Unit: 
		"""
		pass

	@property
	@staticmethod
	def MicrogramsPerLiterNPerDay() -> Unit:
		"""No Description

		Returns:
			Unit: 
		"""
		pass

	@property
	@staticmethod
	def MicrogramsPerLiterNPerSecond() -> Unit:
		"""No Description

		Returns:
			Unit: 
		"""
		pass

	@property
	@staticmethod
	def MicrogramsPerMinute() -> Unit:
		"""No Description

		Returns:
			Unit: 
		"""
		pass

	@property
	@staticmethod
	def MicrogramsPerSecond() -> Unit:
		"""No Description

		Returns:
			Unit: 
		"""
		pass

	@property
	@staticmethod
	def MicrogramsPerSquareFeetPerDay() -> Unit:
		"""No Description

		Returns:
			Unit: 
		"""
		pass

	@property
	@staticmethod
	def MicrogramsPerSquareMeterPerDay() -> Unit:
		"""No Description

		Returns:
			Unit: 
		"""
		pass

	@property
	@staticmethod
	def MicrogramsPerSquareMeterPerSecond() -> Unit:
		"""No Description

		Returns:
			Unit: 
		"""
		pass

	@property
	@staticmethod
	def Miles() -> Unit:
		"""No Description

		Returns:
			Unit: 
		"""
		pass

	@property
	@staticmethod
	def Millifeet() -> Unit:
		"""No Description

		Returns:
			Unit: 
		"""
		pass

	@property
	@staticmethod
	def Milligram() -> Unit:
		"""No Description

		Returns:
			Unit: 
		"""
		pass

	@property
	@staticmethod
	def MilliGramsPerDay() -> Unit:
		"""No Description

		Returns:
			Unit: 
		"""
		pass

	@property
	@staticmethod
	def MilliGramsPerHour() -> Unit:
		"""No Description

		Returns:
			Unit: 
		"""
		pass

	@property
	@staticmethod
	def MilligramsPerLiter() -> Unit:
		"""No Description

		Returns:
			Unit: 
		"""
		pass

	@property
	@staticmethod
	def MilligramsPerLiterNPerDay() -> Unit:
		"""No Description

		Returns:
			Unit: 
		"""
		pass

	@property
	@staticmethod
	def MilligramsPerLiterNPerSecond() -> Unit:
		"""No Description

		Returns:
			Unit: 
		"""
		pass

	@property
	@staticmethod
	def MilliGramsPerMinute() -> Unit:
		"""No Description

		Returns:
			Unit: 
		"""
		pass

	@property
	@staticmethod
	def MilliGramsPerSecond() -> Unit:
		"""No Description

		Returns:
			Unit: 
		"""
		pass

	@property
	@staticmethod
	def MilliGramsPerSquareFeetPerDay() -> Unit:
		"""No Description

		Returns:
			Unit: 
		"""
		pass

	@property
	@staticmethod
	def MilliGramsPerSquareMeterPerDay() -> Unit:
		"""No Description

		Returns:
			Unit: 
		"""
		pass

	@property
	@staticmethod
	def MilliGramsPerSquareMeterPerSecond() -> Unit:
		"""No Description

		Returns:
			Unit: 
		"""
		pass

	@property
	@staticmethod
	def MillimeterHorizontalPerMeterVertical() -> Unit:
		"""No Description

		Returns:
			Unit: 
		"""
		pass

	@property
	@staticmethod
	def MillimeterPerMeter() -> Unit:
		"""No Description

		Returns:
			Unit: 
		"""
		pass

	@property
	@staticmethod
	def Millimeters() -> Unit:
		"""No Description

		Returns:
			Unit: 
		"""
		pass

	@property
	@staticmethod
	def MillimetersOfH2O() -> Unit:
		"""No Description

		Returns:
			Unit: 
		"""
		pass

	@property
	@staticmethod
	def MilliMetersPerDay() -> Unit:
		"""No Description

		Returns:
			Unit: 
		"""
		pass

	@property
	@staticmethod
	def MilliMetersPerHour() -> Unit:
		"""No Description

		Returns:
			Unit: 
		"""
		pass

	@property
	@staticmethod
	def MillimetersPerMinute() -> Unit:
		"""No Description

		Returns:
			Unit: 
		"""
		pass

	@property
	@staticmethod
	def MillimeterVerticalPerMeterHorizontal() -> Unit:
		"""No Description

		Returns:
			Unit: 
		"""
		pass

	@property
	@staticmethod
	def MillionGallons() -> Unit:
		"""No Description

		Returns:
			Unit: 
		"""
		pass

	@property
	@staticmethod
	def MillionLiters() -> Unit:
		"""No Description

		Returns:
			Unit: 
		"""
		pass

	@property
	@staticmethod
	def MillionLitersPerDay() -> Unit:
		"""No Description

		Returns:
			Unit: 
		"""
		pass

	@property
	@staticmethod
	def Milliseconds() -> Unit:
		"""No Description

		Returns:
			Unit: 
		"""
		pass

	@property
	@staticmethod
	def Minutes() -> Unit:
		"""No Description

		Returns:
			Unit: 
		"""
		pass

	@property
	@staticmethod
	def NewtonsPerCubicMeter() -> Unit:
		"""No Description

		Returns:
			Unit: 
		"""
		pass

	@property
	@staticmethod
	def NewtonsPerSquareMeter() -> Unit:
		"""No Description

		Returns:
			Unit: 
		"""
		pass

	@property
	@staticmethod
	def OneOverSlope() -> Unit:
		"""No Description

		Returns:
			Unit: 
		"""
		pass

	@property
	@staticmethod
	def None() -> Unit:
		"""No Description

		Returns:
			Unit: 
		"""
		pass

	@property
	@staticmethod
	def PartsPerBillion() -> Unit:
		"""No Description

		Returns:
			Unit: 
		"""
		pass

	@property
	@staticmethod
	def PartsPerBillionNPerDay() -> Unit:
		"""No Description

		Returns:
			Unit: 
		"""
		pass

	@property
	@staticmethod
	def PartsPerBillionNPerSecond() -> Unit:
		"""No Description

		Returns:
			Unit: 
		"""
		pass

	@property
	@staticmethod
	def PartsPerMillion() -> Unit:
		"""No Description

		Returns:
			Unit: 
		"""
		pass

	@property
	@staticmethod
	def PartsPerMillionNPerDay() -> Unit:
		"""No Description

		Returns:
			Unit: 
		"""
		pass

	@property
	@staticmethod
	def PartsPerMillionNPerSecond() -> Unit:
		"""No Description

		Returns:
			Unit: 
		"""
		pass

	@property
	@staticmethod
	def Passenger() -> Unit:
		"""No Description

		Returns:
			Unit: 
		"""
		pass

	@property
	@staticmethod
	def PerDay() -> Unit:
		"""No Description

		Returns:
			Unit: 
		"""
		pass

	@property
	@staticmethod
	def PercentPercent() -> Unit:
		"""No Description

		Returns:
			Unit: 
		"""
		pass

	@property
	@staticmethod
	def PercentSlope() -> Unit:
		"""No Description

		Returns:
			Unit: 
		"""
		pass

	@property
	@staticmethod
	def PerSecond() -> Unit:
		"""No Description

		Returns:
			Unit: 
		"""
		pass

	@property
	@staticmethod
	def Person() -> Unit:
		"""No Description

		Returns:
			Unit: 
		"""
		pass

	@property
	@staticmethod
	def PersonsPerAcre() -> Unit:
		"""No Description

		Returns:
			Unit: 
		"""
		pass

	@property
	@staticmethod
	def PersonsPerSquareFeet() -> Unit:
		"""No Description

		Returns:
			Unit: 
		"""
		pass

	@property
	@staticmethod
	def PersonsPerSquareKilometer() -> Unit:
		"""No Description

		Returns:
			Unit: 
		"""
		pass

	@property
	@staticmethod
	def PersonsPerHectares() -> Unit:
		"""No Description

		Returns:
			Unit: 
		"""
		pass

	@property
	@staticmethod
	def PersonsPerSquareMeter() -> Unit:
		"""No Description

		Returns:
			Unit: 
		"""
		pass

	@property
	@staticmethod
	def PersonsPerSquareMile() -> Unit:
		"""No Description

		Returns:
			Unit: 
		"""
		pass

	@property
	@staticmethod
	def Pounds() -> Unit:
		"""No Description

		Returns:
			Unit: 
		"""
		pass

	@property
	@staticmethod
	def PoundsForcePerCubicFoot() -> Unit:
		"""No Description

		Returns:
			Unit: 
		"""
		pass

	@property
	@staticmethod
	def PoundsPerCubicFoot() -> Unit:
		"""No Description

		Returns:
			Unit: 
		"""
		pass

	@property
	@staticmethod
	def PoundsPerCubicFootNPerDay() -> Unit:
		"""No Description

		Returns:
			Unit: 
		"""
		pass

	@property
	@staticmethod
	def PoundsPerCubicFootNPerSecond() -> Unit:
		"""No Description

		Returns:
			Unit: 
		"""
		pass

	@property
	@staticmethod
	def PoundsPerDay() -> Unit:
		"""No Description

		Returns:
			Unit: 
		"""
		pass

	@property
	@staticmethod
	def PoundsPerHour() -> Unit:
		"""No Description

		Returns:
			Unit: 
		"""
		pass

	@property
	@staticmethod
	def PoundsPerKilowattHour() -> Unit:
		"""No Description

		Returns:
			Unit: 
		"""
		pass

	@property
	@staticmethod
	def PoundsPerMillionGallons() -> Unit:
		"""No Description

		Returns:
			Unit: 
		"""
		pass

	@property
	@staticmethod
	def PoundsPerMillionGallonsNPerDay() -> Unit:
		"""No Description

		Returns:
			Unit: 
		"""
		pass

	@property
	@staticmethod
	def PoundsPerMillionGallonsNPerSecond() -> Unit:
		"""No Description

		Returns:
			Unit: 
		"""
		pass

	@property
	@staticmethod
	def PoundsPerMinute() -> Unit:
		"""No Description

		Returns:
			Unit: 
		"""
		pass

	@property
	@staticmethod
	def PoundsPerSecond() -> Unit:
		"""No Description

		Returns:
			Unit: 
		"""
		pass

	@property
	@staticmethod
	def PoundsPerSquareFoot() -> Unit:
		"""No Description

		Returns:
			Unit: 
		"""
		pass

	@property
	@staticmethod
	def PoundsPerSquareInch() -> Unit:
		"""No Description

		Returns:
			Unit: 
		"""
		pass

	@property
	@staticmethod
	def PSI() -> Unit:
		"""No Description

		Returns:
			Unit: 
		"""
		pass

	@property
	@staticmethod
	def Resident() -> Unit:
		"""No Description

		Returns:
			Unit: 
		"""
		pass

	@property
	@staticmethod
	def RPM() -> Unit:
		"""No Description

		Returns:
			Unit: 
		"""
		pass

	@property
	@staticmethod
	def Seconds() -> Unit:
		"""No Description

		Returns:
			Unit: 
		"""
		pass

	@property
	@staticmethod
	def SquareCentimeters() -> Unit:
		"""No Description

		Returns:
			Unit: 
		"""
		pass

	@property
	@staticmethod
	def SquareFeet() -> Unit:
		"""No Description

		Returns:
			Unit: 
		"""
		pass

	@property
	@staticmethod
	def SquareFeetPerSecond() -> Unit:
		"""No Description

		Returns:
			Unit: 
		"""
		pass

	@property
	@staticmethod
	def SquareInches() -> Unit:
		"""No Description

		Returns:
			Unit: 
		"""
		pass

	@property
	@staticmethod
	def SquareKilometers() -> Unit:
		"""No Description

		Returns:
			Unit: 
		"""
		pass

	@property
	@staticmethod
	def SquareMeters() -> Unit:
		"""No Description

		Returns:
			Unit: 
		"""
		pass

	@property
	@staticmethod
	def SquareMetersPerSecond() -> Unit:
		"""No Description

		Returns:
			Unit: 
		"""
		pass

	@property
	@staticmethod
	def SquareMiles() -> Unit:
		"""No Description

		Returns:
			Unit: 
		"""
		pass

	@property
	@staticmethod
	def SquareMillimeters() -> Unit:
		"""No Description

		Returns:
			Unit: 
		"""
		pass

	@property
	@staticmethod
	def SquareYards() -> Unit:
		"""No Description

		Returns:
			Unit: 
		"""
		pass

	@property
	@staticmethod
	def Stokes() -> Unit:
		"""No Description

		Returns:
			Unit: 
		"""
		pass

	@property
	@staticmethod
	def Student() -> Unit:
		"""No Description

		Returns:
			Unit: 
		"""
		pass

	@property
	@staticmethod
	def ThousandCapita() -> Unit:
		"""No Description

		Returns:
			Unit: 
		"""
		pass

	@property
	@staticmethod
	def AcreFeet() -> Unit:
		"""No Description

		Returns:
			Unit: 
		"""
		pass

	@property
	@staticmethod
	def AcreFeetPerDay() -> Unit:
		"""No Description

		Returns:
			Unit: 
		"""
		pass

	@property
	@staticmethod
	def AcreFeetPerHour() -> Unit:
		"""No Description

		Returns:
			Unit: 
		"""
		pass

	@property
	@staticmethod
	def AcreFeetPerMinute() -> Unit:
		"""No Description

		Returns:
			Unit: 
		"""
		pass

	@property
	@staticmethod
	def AcreInches() -> Unit:
		"""No Description

		Returns:
			Unit: 
		"""
		pass

	@property
	@staticmethod
	def AcreInchPerHour() -> Unit:
		"""No Description

		Returns:
			Unit: 
		"""
		pass

	@property
	@staticmethod
	def AcreInchPerMinute() -> Unit:
		"""No Description

		Returns:
			Unit: 
		"""
		pass

	@property
	@staticmethod
	def Acres() -> Unit:
		"""No Description

		Returns:
			Unit: 
		"""
		pass

	@property
	@staticmethod
	def AngleDegrees() -> Unit:
		"""No Description

		Returns:
			Unit: 
		"""
		pass

	@property
	@staticmethod
	def AngleMinutes() -> Unit:
		"""No Description

		Returns:
			Unit: 
		"""
		pass

	@property
	@staticmethod
	def AngleQuadrants() -> Unit:
		"""No Description

		Returns:
			Unit: 
		"""
		pass

	@property
	@staticmethod
	def AngleRadians() -> Unit:
		"""No Description

		Returns:
			Unit: 
		"""
		pass

	@property
	@staticmethod
	def AngleRevolutions() -> Unit:
		"""No Description

		Returns:
			Unit: 
		"""
		pass

	@property
	@staticmethod
	def AngleSeconds() -> Unit:
		"""No Description

		Returns:
			Unit: 
		"""
		pass

	@property
	@staticmethod
	def Atmospheres() -> Unit:
		"""No Description

		Returns:
			Unit: 
		"""
		pass

	@property
	@staticmethod
	def Bars() -> Unit:
		"""No Description

		Returns:
			Unit: 
		"""
		pass

	@property
	@staticmethod
	def Capita() -> Unit:
		"""No Description

		Returns:
			Unit: 
		"""
		pass

	@property
	@staticmethod
	def Celsius() -> Unit:
		"""No Description

		Returns:
			Unit: 
		"""
		pass

	@property
	@staticmethod
	def CentimeterPerMeter() -> Unit:
		"""No Description

		Returns:
			Unit: 
		"""
		pass

	@property
	@staticmethod
	def Centimeters() -> Unit:
		"""No Description

		Returns:
			Unit: 
		"""
		pass

	@property
	@staticmethod
	def CentimetersPerDay() -> Unit:
		"""No Description

		Returns:
			Unit: 
		"""
		pass

	@property
	@staticmethod
	def CentimetersPerHour() -> Unit:
		"""No Description

		Returns:
			Unit: 
		"""
		pass

	@property
	@staticmethod
	def CentimetersPerMinute() -> Unit:
		"""No Description

		Returns:
			Unit: 
		"""
		pass

	@property
	@staticmethod
	def Centistokes() -> Unit:
		"""No Description

		Returns:
			Unit: 
		"""
		pass

	@property
	@staticmethod
	def CFM() -> Unit:
		"""No Description

		Returns:
			Unit: 
		"""
		pass

	@property
	@staticmethod
	def CFMPerPSI() -> Unit:
		"""No Description

		Returns:
			Unit: 
		"""
		pass

	@property
	@staticmethod
	def CFS() -> Unit:
		"""No Description

		Returns:
			Unit: 
		"""
		pass

	@property
	@staticmethod
	def CFSPerPSI() -> Unit:
		"""No Description

		Returns:
			Unit: 
		"""
		pass

	@property
	@staticmethod
	def CFSPerAcres() -> Unit:
		"""No Description

		Returns:
			Unit: 
		"""
		pass

	@property
	@staticmethod
	def CFSPerSquareFeet() -> Unit:
		"""No Description

		Returns:
			Unit: 
		"""
		pass

	@property
	@staticmethod
	def CFSPerSquareMiles() -> Unit:
		"""No Description

		Returns:
			Unit: 
		"""
		pass

	@property
	@staticmethod
	def CubicCentimeters() -> Unit:
		"""No Description

		Returns:
			Unit: 
		"""
		pass

	@property
	@staticmethod
	def CubicFeet() -> Unit:
		"""No Description

		Returns:
			Unit: 
		"""
		pass

	@property
	@staticmethod
	def CubicFeetPerDay() -> Unit:
		"""No Description

		Returns:
			Unit: 
		"""
		pass

	@property
	@staticmethod
	def CubicFeetPerDayPerPSI() -> Unit:
		"""No Description

		Returns:
			Unit: 
		"""
		pass

	@property
	@staticmethod
	def CubicFeetPerMinute() -> Unit:
		"""No Description

		Returns:
			Unit: 
		"""
		pass

	@property
	@staticmethod
	def CubicFeetPerMinutePerPSI() -> Unit:
		"""No Description

		Returns:
			Unit: 
		"""
		pass

	@property
	@staticmethod
	def CubicFeetPerSecond() -> Unit:
		"""No Description

		Returns:
			Unit: 
		"""
		pass

	@property
	@staticmethod
	def CubicFeetPerSecondPerPSI() -> Unit:
		"""No Description

		Returns:
			Unit: 
		"""
		pass

	@property
	@staticmethod
	def CubicInches() -> Unit:
		"""No Description

		Returns:
			Unit: 
		"""
		pass

	@property
	@staticmethod
	def CubicMeters() -> Unit:
		"""No Description

		Returns:
			Unit: 
		"""
		pass

	@property
	@staticmethod
	def CubicMetersPerDay() -> Unit:
		"""No Description

		Returns:
			Unit: 
		"""
		pass

	@property
	@staticmethod
	def CubicMetersPerDayPerMetersOfH2O() -> Unit:
		"""No Description

		Returns:
			Unit: 
		"""
		pass

	@property
	@staticmethod
	def CubicMetersPerHour() -> Unit:
		"""No Description

		Returns:
			Unit: 
		"""
		pass

	@property
	@staticmethod
	def CubicMetersPerHourPerMetersOfH2O() -> Unit:
		"""No Description

		Returns:
			Unit: 
		"""
		pass

	@property
	@staticmethod
	def CubicMetersPerMinute() -> Unit:
		"""No Description

		Returns:
			Unit: 
		"""
		pass

	@property
	@staticmethod
	def CubicMetersPerMinutePerMetersOfH2O() -> Unit:
		"""No Description

		Returns:
			Unit: 
		"""
		pass

	@property
	@staticmethod
	def CubicMetersPerSecond() -> Unit:
		"""No Description

		Returns:
			Unit: 
		"""
		pass

	@property
	@staticmethod
	def CubicMetersPerSecondPerMetersOfH2O() -> Unit:
		"""No Description

		Returns:
			Unit: 
		"""
		pass

	@property
	@staticmethod
	def CubicMetersPerHectaresPerDay() -> Unit:
		"""No Description

		Returns:
			Unit: 
		"""
		pass

	@property
	@staticmethod
	def CubicMetersPerSquareKilometerPerDay() -> Unit:
		"""No Description

		Returns:
			Unit: 
		"""
		pass

	@property
	@staticmethod
	def CubicMetersPerSquareMeterPerDay() -> Unit:
		"""No Description

		Returns:
			Unit: 
		"""
		pass

	@property
	@staticmethod
	def CubicYards() -> Unit:
		"""No Description

		Returns:
			Unit: 
		"""
		pass

	@property
	@staticmethod
	def Customer() -> Unit:
		"""No Description

		Returns:
			Unit: 
		"""
		pass

	@property
	@staticmethod
	def Days() -> Unit:
		"""No Description

		Returns:
			Unit: 
		"""
		pass

	@property
	@staticmethod
	def Decimeters() -> Unit:
		"""No Description

		Returns:
			Unit: 
		"""
		pass

	@property
	@staticmethod
	def Dollars() -> Unit:
		"""No Description

		Returns:
			Unit: 
		"""
		pass

	@property
	@staticmethod
	def DollarsPerFoot() -> Unit:
		"""No Description

		Returns:
			Unit: 
		"""
		pass

	@property
	@staticmethod
	def DollarsPerMeter() -> Unit:
		"""No Description

		Returns:
			Unit: 
		"""
		pass

	@property
	@staticmethod
	def DollarsPerKiloWattHour() -> Unit:
		"""No Description

		Returns:
			Unit: 
		"""
		pass

	@property
	@staticmethod
	def Employee() -> Unit:
		"""No Description

		Returns:
			Unit: 
		"""
		pass

	@property
	@staticmethod
	def Fahrenheit() -> Unit:
		"""No Description

		Returns:
			Unit: 
		"""
		pass

	@property
	@staticmethod
	def Feet() -> Unit:
		"""No Description

		Returns:
			Unit: 
		"""
		pass

	@property
	@staticmethod
	def FeetOfH2O() -> Unit:
		"""No Description

		Returns:
			Unit: 
		"""
		pass

	@property
	@staticmethod
	def FeetPerDay() -> Unit:
		"""No Description

		Returns:
			Unit: 
		"""
		pass

	@property
	@staticmethod
	def FeetPerInch() -> Unit:
		"""No Description

		Returns:
			Unit: 
		"""
		pass

	@property
	@staticmethod
	def FootHorizontalPerFootVertical() -> Unit:
		"""No Description

		Returns:
			Unit: 
		"""
		pass

	@property
	@staticmethod
	def FootPer1000Feet() -> Unit:
		"""No Description

		Returns:
			Unit: 
		"""
		pass

	@property
	@staticmethod
	def FootPerFoot() -> Unit:
		"""No Description

		Returns:
			Unit: 
		"""
		pass

	@property
	@staticmethod
	def FootPerMile() -> Unit:
		"""No Description

		Returns:
			Unit: 
		"""
		pass

	@property
	@staticmethod
	def FootPoundals() -> Unit:
		"""No Description

		Returns:
			Unit: 
		"""
		pass

	@property
	@staticmethod
	def FootVerticalPerFootHorizontal() -> Unit:
		"""No Description

		Returns:
			Unit: 
		"""
		pass

	@property
	@staticmethod
	def Gallons() -> Unit:
		"""No Description

		Returns:
			Unit: 
		"""
		pass

	@property
	@staticmethod
	def GallonsPerDay() -> Unit:
		"""No Description

		Returns:
			Unit: 
		"""
		pass

	@property
	@staticmethod
	def GallonsPerDayPerPSI() -> Unit:
		"""No Description

		Returns:
			Unit: 
		"""
		pass

	@property
	@staticmethod
	def GallonsPerMinute() -> Unit:
		"""No Description

		Returns:
			Unit: 
		"""
		pass

	@property
	@staticmethod
	def GallonsPerMinutePerPSI() -> Unit:
		"""No Description

		Returns:
			Unit: 
		"""
		pass

	@property
	@staticmethod
	def GallonsPerSecond() -> Unit:
		"""No Description

		Returns:
			Unit: 
		"""
		pass

	@property
	@staticmethod
	def GallonsPerSecondPerPSI() -> Unit:
		"""No Description

		Returns:
			Unit: 
		"""
		pass

	@property
	@staticmethod
	def GPD() -> Unit:
		"""No Description

		Returns:
			Unit: 
		"""
		pass

	@property
	@staticmethod
	def GPDPerAcres() -> Unit:
		"""No Description

		Returns:
			Unit: 
		"""
		pass

	@property
	@staticmethod
	def GPDPerCapita() -> Unit:
		"""No Description

		Returns:
			Unit: 
		"""
		pass

	@property
	@staticmethod
	def GPDPerSquareFeet() -> Unit:
		"""No Description

		Returns:
			Unit: 
		"""
		pass

	@property
	@staticmethod
	def GPDPerSquareMile() -> Unit:
		"""No Description

		Returns:
			Unit: 
		"""
		pass

	@property
	@staticmethod
	def GPM() -> Unit:
		"""No Description

		Returns:
			Unit: 
		"""
		pass

	@property
	@staticmethod
	def GPMPerAcres() -> Unit:
		"""No Description

		Returns:
			Unit: 
		"""
		pass

	@property
	@staticmethod
	def GPMPerPSI() -> Unit:
		"""No Description

		Returns:
			Unit: 
		"""
		pass

	@property
	@staticmethod
	def GPMPerSquareFeet() -> Unit:
		"""No Description

		Returns:
			Unit: 
		"""
		pass

	@property
	@staticmethod
	def GPMPerSquareMile() -> Unit:
		"""No Description

		Returns:
			Unit: 
		"""
		pass

	@property
	@staticmethod
	def Gram() -> Unit:
		"""No Description

		Returns:
			Unit: 
		"""
		pass

	@property
	@staticmethod
	def GramsPerDay() -> Unit:
		"""No Description

		Returns:
			Unit: 
		"""
		pass

	@property
	@staticmethod
	def GramsPerHour() -> Unit:
		"""No Description

		Returns:
			Unit: 
		"""
		pass

	@property
	@staticmethod
	def GramsPerMinute() -> Unit:
		"""No Description

		Returns:
			Unit: 
		"""
		pass

	@property
	@staticmethod
	def GramsPerSecond() -> Unit:
		"""No Description

		Returns:
			Unit: 
		"""
		pass

	@property
	@staticmethod
	def Guest() -> Unit:
		"""No Description

		Returns:
			Unit: 
		"""
		pass

	@property
	@staticmethod
	def Hectares() -> Unit:
		"""No Description

		Returns:
			Unit: 
		"""
		pass

	@property
	@staticmethod
	def Hertz() -> Unit:
		"""No Description

		Returns:
			Unit: 
		"""
		pass

	@property
	@staticmethod
	def HorizontalPerVertical() -> Unit:
		"""No Description

		Returns:
			Unit: 
		"""
		pass

	@property
	@staticmethod
	def Horsepower() -> Unit:
		"""No Description

		Returns:
			Unit: 
		"""
		pass

	@property
	@staticmethod
	def Hours() -> Unit:
		"""No Description

		Returns:
			Unit: 
		"""
		pass

	@property
	@staticmethod
	def HundredCapita() -> Unit:
		"""No Description

		Returns:
			Unit: 
		"""
		pass

	@property
	@staticmethod
	def ImperialGallonsPerDay() -> Unit:
		"""No Description

		Returns:
			Unit: 
		"""
		pass

	@property
	@staticmethod
	def ImperialGallonsPerMinute() -> Unit:
		"""No Description

		Returns:
			Unit: 
		"""
		pass

	@property
	@staticmethod
	def ImperialGallonsPerSecond() -> Unit:
		"""No Description

		Returns:
			Unit: 
		"""
		pass

	@property
	@staticmethod
	def ImpGallons() -> Unit:
		"""No Description

		Returns:
			Unit: 
		"""
		pass

	@property
	@staticmethod
	def ImperialGallonsPerDayPerPSI() -> Unit:
		"""No Description

		Returns:
			Unit: 
		"""
		pass

	@property
	@staticmethod
	def ImperialGallonsPerMinutePerPSI() -> Unit:
		"""No Description

		Returns:
			Unit: 
		"""
		pass

	@property
	@staticmethod
	def ImperialGallonsPerSecondPerPSI() -> Unit:
		"""No Description

		Returns:
			Unit: 
		"""
		pass

	@property
	@staticmethod
	def Inches() -> Unit:
		"""No Description

		Returns:
			Unit: 
		"""
		pass

	@property
	@staticmethod
	def InchesPerDay() -> Unit:
		"""No Description

		Returns:
			Unit: 
		"""
		pass

	@property
	@staticmethod
	def InchesPerHour() -> Unit:
		"""No Description

		Returns:
			Unit: 
		"""
		pass

	@property
	@staticmethod
	def InchesPerMinute() -> Unit:
		"""No Description

		Returns:
			Unit: 
		"""
		pass

	@property
	@staticmethod
	def InchPerFoot() -> Unit:
		"""No Description

		Returns:
			Unit: 
		"""
		pass

	@property
	@staticmethod
	def InfiltrationRateCentimetersPerDay() -> Unit:
		"""No Description

		Returns:
			Unit: 
		"""
		pass

	@property
	@staticmethod
	def InfiltrationRateCentimetersPerHour() -> Unit:
		"""No Description

		Returns:
			Unit: 
		"""
		pass

	@property
	@staticmethod
	def InfiltrationRateCentimetersPerMinute() -> Unit:
		"""No Description

		Returns:
			Unit: 
		"""
		pass

	@property
	@staticmethod
	def InfiltrationRateInchesPerDay() -> Unit:
		"""No Description

		Returns:
			Unit: 
		"""
		pass

	@property
	@staticmethod
	def InfiltrationRateInchesPerHour() -> Unit:
		"""No Description

		Returns:
			Unit: 
		"""
		pass

	@property
	@staticmethod
	def InfiltrationRateInchesPerMinute() -> Unit:
		"""No Description

		Returns:
			Unit: 
		"""
		pass

	@property
	@staticmethod
	def InfiltrationRateMillimetersPerDay() -> Unit:
		"""No Description

		Returns:
			Unit: 
		"""
		pass

	@property
	@staticmethod
	def InfiltrationRateMillimetersPerHour() -> Unit:
		"""No Description

		Returns:
			Unit: 
		"""
		pass

	@property
	@staticmethod
	def InfiltrationRateMillimetersPerMinute() -> Unit:
		"""No Description

		Returns:
			Unit: 
		"""
		pass

	@property
	@staticmethod
	def Joules() -> Unit:
		"""No Description

		Returns:
			Unit: 
		"""
		pass

	@property
	@staticmethod
	def Kilograms() -> Unit:
		"""No Description

		Returns:
			Unit: 
		"""
		pass

	@property
	@staticmethod
	def KilogramsPerDay() -> Unit:
		"""No Description

		Returns:
			Unit: 
		"""
		pass

	@property
	@staticmethod
	def KilogramsPerHour() -> Unit:
		"""No Description

		Returns:
			Unit: 
		"""
		pass

	@property
	@staticmethod
	def KilogramsPerKilowattHour() -> Unit:
		"""No Description

		Returns:
			Unit: 
		"""
		pass

	@property
	@staticmethod
	def KilogramsPerMinute() -> Unit:
		"""No Description

		Returns:
			Unit: 
		"""
		pass

class UnitConversionManager:

	def __init__(self) -> None:
		"""No Description
		"""
		pass

	def AvailableDimensions(self) -> List:
		"""No Description

		Returns:
			List: 
		"""
		pass

	def DimensionAt(self, adimensionindex: DimensionIndex) -> Dimension:
		"""No Description

		Args:
			adimensionindex(DimensionIndex): adimensionindex

		Returns:
			Dimension: 
		"""
		pass

	def UnitIndexFor(self, unit: Unit) -> UnitIndex:
		"""No Description

		Args:
			unit(Unit): unit

		Returns:
			UnitIndex: 
		"""
		pass

	def UnitAt(self, aunitindex: UnitIndex) -> Unit:
		"""No Description

		Args:
			aunitindex(UnitIndex): aunitindex

		Returns:
			Unit: 
		"""
		pass

	def UnitSystemAt(self, aunitsystemindex: UnitSystemIndex) -> UnitSystem:
		"""No Description

		Args:
			aunitsystemindex(UnitSystemIndex): aunitsystemindex

		Returns:
			UnitSystem: 
		"""
		pass

	@property
	@staticmethod
	def Current() -> UnitConversionManager:
		"""No Description

		Returns:
			UnitConversionManager: 
		"""
		pass

	@property
	@staticmethod
	def EmitterExponent() -> float:
		"""No Description

		Returns:
			UnitConversionManager: 
		"""
		pass

	@EmitterExponent.setter
	@staticmethod
	def EmitterExponent(self, emitterexponent: float) -> None:
		pass

class UnitSystem(INamable):

	def __init__(self, astringName: str) -> None:
		"""No Description

		Args:
			astringName(str): astringName
		"""
		pass

	@staticmethod
	def FromSerializedString(astring: str) -> UnitSystem:
		"""No Description

		Args:
			astring(str): astring

		Returns:
			UnitSystem: 
		"""
		pass

	def ToSerializedString(self) -> str:
		"""No Description

		Returns:
			str: 
		"""
		pass

	@property
	@staticmethod
	def None() -> UnitSystem:
		"""No Description

		Returns:
			UnitSystem: 
		"""
		pass

	@property
	@staticmethod
	def Si() -> UnitSystem:
		"""No Description

		Returns:
			UnitSystem: 
		"""
		pass

	@property
	@staticmethod
	def UsCustomary() -> UnitSystem:
		"""No Description

		Returns:
			UnitSystem: 
		"""
		pass

	@property
	@staticmethod
	def Both() -> UnitSystem:
		"""No Description

		Returns:
			UnitSystem: 
		"""
		pass

	@property
	def Label(self) -> str:
		"""No Description

		Returns:
			UnitSystem: 
		"""
		pass

	@property
	def LabelKey(self) -> str:
		"""No Description

		Returns:
			UnitSystem: 
		"""
		pass

	@property
	def Name(self) -> str:
		"""No Description

		Returns:
			UnitSystem: 
		"""
		pass

	@property
	def ShortLabel(self) -> str:
		"""No Description

		Returns:
			UnitSystem: 
		"""
		pass

class ConversionException(ISerializable, _Exception):

	def __init__(self, asMessage: str) -> None:
		"""No Description

		Args:
			asMessage(str): asMessage
		"""
		pass

	def GetBaseException(self) -> Exception:
		"""No Description

		Returns:
			Exception: 
		"""
		pass

	def GetObjectData(self, info: SerializationInfo, context: StreamingContext) -> None:
		"""No Description

		Args:
			info(SerializationInfo): info
			context(StreamingContext): context

		Returns:
			None: 
		"""
		pass

	@property
	def Data(self) -> Dict:
		"""No Description

		Returns:
			ConversionException: 
		"""
		pass

	@property
	def InnerException(self) -> Exception:
		"""No Description

		Returns:
			ConversionException: 
		"""
		pass

	@property
	def TargetSite(self) -> MethodBase:
		"""No Description

		Returns:
			ConversionException: 
		"""
		pass

	@property
	def StackTrace(self) -> str:
		"""No Description

		Returns:
			ConversionException: 
		"""
		pass

	@property
	def HelpLink(self) -> str:
		"""No Description

		Returns:
			ConversionException: 
		"""
		pass

	@property
	def Source(self) -> str:
		"""No Description

		Returns:
			ConversionException: 
		"""
		pass

	@property
	def HResult(self) -> int:
		"""No Description

		Returns:
			ConversionException: 
		"""
		pass

	@property
	def Message(self) -> str:
		"""No Description

		Returns:
			ConversionException: 
		"""
		pass

	@HelpLink.setter
	def HelpLink(self, helplink: str) -> None:
		pass

	@Source.setter
	def Source(self, source: str) -> None:
		pass

class FactorConverter(IUnitConverter):

	def __init__(self, adouble: float) -> None:
		"""No Description

		Args:
			adouble(float): adouble
		"""
		pass

	def FromBaseUnit(self, adouble: float) -> float:
		"""No Description

		Args:
			adouble(float): adouble

		Returns:
			float: 
		"""
		pass

	def ToBaseUnit(self, adouble: float) -> float:
		"""No Description

		Args:
			adouble(float): adouble

		Returns:
			float: 
		"""
		pass

class DimensionIndex(Enum):
	None = 0
	Angle = 1
	Area = 2
	Concentration = 3
	Currency = 4
	CurrencyPerEnergy = 5
	CurrencyPerLength = 6
	Diffusivity = 7
	ElectricalFrequency = 8
	EmitterCoefficient = 9
	Energy = 10
	Flow = 11
	FlowDensityPerArea = 12
	FlowDensityPerCapita = 13
	InfiltrationRate = 14
	Length = 15
	Mass = 16
	MassRate = 17
	NthOrderBulkReactionRate = 18
	Percent = 19
	Population = 20
	PopulationDensityPerArea = 21
	Power = 22
	Pressure = 23
	RainfallIntensity = 24
	ReactionRate = 25
	RotationalFrequency = 26
	Scale = 27
	Slope = 28
	SpecificWeight = 29
	SurfaceReactionRate = 30
	Temperature = 31
	Time = 32
	Unitless = 33
	Velocity = 34
	Volume = 35
	WeirCoefficient = 36
	ZeroOrderSurfaceReactionRate = 37
	DiameterLength = 38
	MassPerArea = 39
	Inertia = 40
	CurrencyPerPower = 41
	CostPerUnitVolume = 42
	EnergyPerUnitVolume = 43
	Torque = 44
	SpringConstant = 45
	Force = 46
	Density = 47
	DischargePerPressureDrop = 48
	VolumePerLength = 49
	SideWeirCoefficient = 50
	InfiltrationPerUnitDepth = 51
	PressurePerLength = 52
	MassPerLength = 53
	PerLength = 54
	PerPressure = 55
	DynamicViscosity = 56
	CalorificValue = 57
	WeirCoefficientParameterized = 58
	SnowMeltCoefficient = 59
	BreakRate = 60
	MassPerEnergy = 61
	ValveOpenCloseRateCoefficient = 62
	EnergyPerPower = 63
	DrainCoefficientUnit = 64
	NumberPerVolume = 65
	NumberPerArea = 66
	MolesPerVolume = 67
	MolesPerArea = 68
	ValveOpenCloseRateCoefficientPerFlow = 69
	FlowPerUnitLength = 70
	Acceleration = 71

class UnitIndex(Enum):
	None = 0
	AcreFeet = 1
	AcreFeetPerDay = 2
	AcreFeetPerHour = 3
	AcreFeetPerMinute = 4
	AcreInches = 5
	AcreInchPerHour = 6
	AcreInchPerMinute = 7
	Acres = 8
	AngleDegrees = 9
	AngleMinutes = 10
	AngleQuadrants = 11
	AngleRadians = 12
	AngleRevolutions = 13
	AngleSeconds = 14
	Atmospheres = 15
	Bars = 16
	Capita = 17
	Celsius = 18
	CentimeterPerMeter = 19
	Centimeters = 20
	CentimetersPerDay = 21
	CentimetersPerHour = 22
	CentimetersPerMinute = 23
	Centistokes = 24
	CFM = 25
	CFMPerPSI = 26
	CFS = 27
	CFSPerPSI = 28
	CFSPerAcres = 29
	CFSPerSquareFeet = 30
	CFSPerSquareMiles = 31
	CubicCentimeters = 32
	CubicFeet = 33
	CubicFeetPerDay = 34
	CubicFeetPerDayPerPSI = 35
	CubicFeetPerMinute = 36
	CubicFeetPerMinutePerPSI = 37
	CubicFeetPerSecond = 38
	CubicFeetPerSecondPerPSI = 39
	CubicInches = 40
	CubicMeters = 41
	CubicMetersPerDay = 42
	CubicMetersPerDayPerMetersOfH2O = 43
	CubicMetersPerHour = 44
	CubicMetersPerHourPerMetersOfH2O = 45
	CubicMetersPerMinute = 46
	CubicMetersPerMinutePerMetersOfH2O = 47
	CubicMetersPerSecond = 48
	CubicMetersPerSecondPerMetersOfH2O = 49
	CubicMetersPerHectaresPerDay = 50
	CubicMetersPerSquareKilometerPerDay = 51
	CubicMetersPerSquareMeterPerDay = 52
	CubicYards = 53
	Customer = 54
	Days = 55
	Decimeters = 56
	Dollars = 57
	DollarsPerFoot = 58
	DollarsPerMeter = 59
	DollarsPerKiloWattHour = 60
	Employee = 61
	Fahrenheit = 62
	Feet = 63
	FeetOfH2O = 64
	FeetPerDay = 65
	FeetPerInch = 66
	FootHorizontalPerFootVertical = 67
	FootPer1000Feet = 68
	FootPerFoot = 69
	FootPerMile = 70
	FootPoundals = 71
	FootVerticalPerFootHorizontal = 72
	Gallons = 73
	GallonsPerDay = 74
	GallonsPerDayPerPSI = 75
	GallonsPerMinute = 76
	GallonsPerMinutePerPSI = 77
	GallonsPerSecond = 78
	GallonsPerSecondPerPSI = 79
	GPDPerAcres = 80
	GPDPerCapita = 81
	GPDPerSquareFeet = 82
	GPDPerSquareMile = 83
	GPM = 84
	GPMPerAcres = 85
	GPMPerPSI = 86
	GPMPerSquareFeet = 87
	GPMPerSquareMile = 88
	Gram = 89
	GramsPerDay = 90
	GramsPerHour = 91
	GramsPerMinute = 92
	GramsPerSecond = 93
	Guest = 94
	Hectares = 95
	Hertz = 96
	HorizontalPerVertical = 97
	Horsepower = 98
	Hours = 99
	HundredCapita = 100
	ImperialGallonsPerDay = 101
	ImperialGallonsPerMinute = 102
	ImperialGallonsPerSecond = 103
	ImpGallons = 104
	ImperialGallonsPerDayPerPSI = 105
	ImperialGallonsPerMinutePerPSI = 106
	ImperialGallonsPerSecondPerPSI = 107
	Inches = 108
	InchesPerDay = 109
	InchesPerHour = 110
	InchesPerMinute = 111
	InchPerFoot = 112
	InfiltrationRateCentimetersPerDay = 113
	InfiltrationRateCentimetersPerHour = 114
	InfiltrationRateCentimetersPerMinute = 115
	InfiltrationRateInchesPerDay = 116
	InfiltrationRateInchesPerHour = 117
	InfiltrationRateInchesPerMinute = 118
	InfiltrationRateMillimetersPerDay = 119
	InfiltrationRateMillimetersPerHour = 120
	InfiltrationRateMillimetersPerMinute = 121
	Joules = 122
	Kilograms = 123
	KilogramsPerDay = 124
	KilogramsPerHour = 125
	KilogramsPerMinute = 126
	KilogramsPerSecond = 127
	KilogramsPerSquareCentimeter = 128
	KiloJoules = 129
	Kilometers = 130
	KiloNewtonsPerCubicMeter = 131
	KiloPascals = 132
	KiloWattHours = 133
	Kilowatts = 134
	Liters = 135
	LitersPerCapitaPerDay = 136
	LitersPerDay = 137
	LitersPerDayPerMetersOfH2O = 138
	LitersPerMinute = 139
	LitersPerMinutePerMetersOfH2O = 140
	LitersPerSecond = 141
	LitersPerSecondPerMetersOfH2O = 142
	LitersPerHectaresPerDay = 143
	LitersPerSquareKilometerPerDay = 144
	LitersPerSquareMeterPerDay = 145
	MegaLitersPerDay = 146
	MegaLitersPerDayPerMetersOfH2O = 147
	MeterHorizontalPerMeterVertical = 148
	MeterPerKilometer = 149
	MeterPerMeter = 150
	Meters = 151
	MetersOfH2O = 152
	MetersPerCm = 153
	MetersPerDay = 154
	MetersPerSecond = 155
	MeterVerticalPerMeterHorizontal = 156
	Mfeet = 157
	MGD = 158
	MGDPerPSI = 159
	MGDImperial = 160
	MGDImperialPerPSI = 161
	MicrogramsPerDay = 162
	MicrogramsPerHour = 163
	MicrogramsPerLiter = 164
	MicrogramsPerLiterNPerDay = 165
	MicrogramsPerLiterNPerSecond = 166
	MicrogramsPerMinute = 167
	MicrogramsPerSecond = 168
	MicrogramsPerSquareFeetPerDay = 169
	MicrogramsPerSquareMeterPerDay = 170
	MicrogramsPerSquareMeterPerSecond = 171
	Miles = 172
	Millifeet = 173
	Milligram = 174
	MilliGramsPerDay = 175
	MilliGramsPerHour = 176
	MilligramsPerLiter = 177
	MilligramsPerLiterNPerDay = 178
	MilligramsPerLiterNPerSecond = 179
	MilliGramsPerMinute = 180
	MilliGramsPerSecond = 181
	MilliGramsPerSquareFeetPerDay = 182
	MilliGramsPerSquareMeterPerDay = 183
	MilliGramsPerSquareMeterPerSecond = 184
	MillimeterHorizontalPerMeterVertical = 185
	MillimeterPerMeter = 186
	Millimeters = 187
	MillimetersOfH2O = 188
	MilliMetersPerDay = 189
	MilliMetersPerHour = 190
	MillimetersPerMinute = 191
	MillimeterVerticalPerMeterHorizontal = 192
	MillionGallons = 193
	MillionLiters = 194
	Minutes = 195
	NewtonsPerCubicMeter = 196
	NewtonsPerSquareMeter = 197
	OneOverSlope = 198
	PartsPerBillion = 199
	PartsPerBillionNPerDay = 200
	PartsPerBillionNPerSecond = 201
	PartsPerMillion = 202
	PartsPerMillionNPerDay = 203
	PartsPerMillionNPerSecond = 204
	Passenger = 205
	PerDay = 206
	PercentPercent = 207
	PercentSlope = 208
	PerSecond = 209
	Person = 210
	PersonsPerAcre = 211
	PersonsPerSquareFeet = 212
	PersonsPerSquareKilometer = 213
	PersonsPerHectares = 214
	PersonsPerSquareMeter = 215
	PersonsPerSquareMile = 216
	Pounds = 217
	PoundsForcePerCubicFoot = 218
	PoundsPerCubicFoot = 219
	PoundsPerCubicFootNPerDay = 220
	PoundsPerCubicFootNPerSecond = 221
	PoundsPerDay = 222
	PoundsPerHour = 223
	PoundsPerMillionGallons = 224
	PoundsPerMillionGallonsNPerDay = 225
	PoundsPerMillionGallonsNPerSecond = 226
	PoundsPerMinute = 227
	PoundsPerSecond = 228
	PoundsPerSquareFoot = 229
	PoundsPerSquareInch = 230
	PSI = 231
	Resident = 232
	RPM = 233
	Seconds = 234
	SquareCentimeters = 235
	SquareFeet = 236
	SquareFeetPerSecond = 237
	SquareInches = 238
	SquareKilometers = 239
	SquareMeters = 240
	SquareMetersPerSecond = 241
	SquareMiles = 242
	SquareMillimeters = 243
	SquareYards = 244
	Stokes = 245
	Student = 246
	ThousandCapita = 247
	ThousandGallons = 248
	ThousandLiters = 249
	ThousandSquareFeet = 250
	UnitlessPercent = 251
	UnitlessUnit = 252
	VelocityCentimetersPerHour = 253
	VelocityCentimetersPerMinute = 254
	VelocityCentimetersPerSecond = 255
	VelocityFeetPerHour = 256
	VelocityFeetPerMinute = 257
	VelocityFeetPerSecond = 258
	VelocityInchesPerHour = 259
	VelocityInchesPerMinute = 260
	VelocityInchesPerSecond = 261
	VelocityKilometersPerHour = 262
	VelocityKnot = 263
	VelocityKnotInternational = 264
	VelocityMetersPerHour = 265
	VelocityMetersPerMinute = 266
	VelocityMetersPerSecond = 267
	VelocityMilePerHour = 268
	VerticalPerHorizontal = 269
	Watts = 270
	WeirCoefficientSi = 271
	WeirCoefficientUs = 272
	Yards = 273
	Years = 274
	MillionLitersPerDay = 275
	PerMinute = 276
	InchMiles = 277
	InchFeet = 278
	FootMiles = 279
	FootFeet = 280
	MillimeterMeters = 281
	MillimeterKilometers = 282
	MeterMeters = 283
	MeterKilometers = 284
	InchMeters = 285
	MillimeterMiles = 286
	PoundsPerAcre = 287
	KilogramsPerHectare = 288
	DollarsPerKiloWatt = 289
	PoundSquareFeet = 290
	NewtonSquareMeters = 291
	DollarsPerHorsepower = 292
	DollarsPerCubicCentimeters = 293
	DollarsPerLiters = 294
	DollarsPerCubicMeters = 295
	DollarsPerCubicInches = 296
	DollarsPerGallons = 297
	DollarsPerImpGallons = 298
	DollarsPerCubicFeet = 299
	DollarsPerCubicYards = 300
	DollarsPerAcreInches = 301
	DollarsPerAcreFeet = 302
	DollarsPerMillionGallons = 303
	DollarsPerThousandGallons = 304
	DollarsPerThousandLiters = 305
	DollarsPerMillionLiters = 306
	KilogramsPerSquareMeter = 307
	KiloWattHourPerMillionGallons = 308
	KiloWattHourPerMillionLiters = 309
	KiloWattHourPerCubicMeters = 310
	KiloWattHourPerCubicFeet = 311
	PerHour = 312
	NewtonMeters = 313
	PoundFeet = 314
	PoundPerInch = 315
	NewtonPerMillimeter = 316
	PoundForce = 317
	KiloPoundForce = 318
	Newton = 319
	KiloNewton = 320
	SlugPerCubicFoot = 321
	PoundPerCubicFoot = 322
	KilogramPerCubicMeter = 323
	CfsPerSquareRootFooH20 = 324
	CmsPerSquareRootMeterH20 = 325
	LPerSecPerSquareRootKpa = 326
	GpmPerSquareRootPsi = 327
	Milliseconds = 328
	KilogramSquareMeters = 329
	Pascals = 330
	GPD = 331
	SideWeirCoefficientSi = 332
	SideWeirCoefficientUs = 333
	CubicFeetPerFoot = 334
	CubicMetersPerMeter = 335
	InchesPerHourPerFeetToKexp = 336
	CentimeterPerHourPerMeterToKexp = 337
	HektoPascals = 338
	MegaPascals = 339
	MilliBars = 340
	Kelvin = 341
	LitersPerHour = 342
	Tons = 343
	MegaWatts = 344
	GigaWatts = 345
	MegaJoules = 346
	GigaJoules = 347
	WattSeconds = 348
	MegaWattHours = 349
	GigaWattHours = 350
	KilogramsPerMeterPerSecond = 351
	PerPascals = 352
	PerBars = 353
	PerMeter = 354
	PerMillimeter = 355
	KilogramsPerMeter = 356
	PascalsPerMeter = 357
	BarsPerKilometer = 358
	JoulesPerCubicMeters = 359
	KiloJoulesPerCubicMeters = 360
	MegaJoulesPerCubicMeters = 361
	KiloWattHoursPerCubicMeters = 362
	WeirCoefficientParameterizedUS = 363
	WeirCoefficientParameterizedSI = 364
	MillimetersPerHourPerDegreeCelsius = 365
	InchesPerHourPerDegreeFahrenheit = 366
	BreaksPerYrPerKm = 367
	BreaksPerYrPerMi = 368
	BreaksPerYrPer1000Ft = 369
	USSurveyFoot = 370
	PoundSecondPerSquareFoot = 371
	PoundsPerFoot = 372
	PSIPerFoot = 373
	PSIPerInch = 374
	PerPSI = 375
	BreaksPerYrPer100Mi = 376
	PoundsPerKilowattHour = 377
	KilogramsPerKilowattHour = 378
	TonnesPerMegaJoule = 379
	TonnesPerYear = 380
	PercentPerSecondPerMeterH2O = 381
	PercentPerSecondPerFtH2O = 382
	PercentPerSecondPerKiloPascal = 383
	PercentPerSecondPerPsi = 384
	KilowattHoursPerKilowatt = 385
	DrainCoeffInchesPerHour = 386
	DrainCoeffMMPerHour = 387
	MilligramsPerSquareFeet = 388
	MicrogramsPerSquareFeet = 389
	MilligramsPerSquareMeter = 390
	MicrogramsPerSquareMeter = 391
	MilligramsPerSquareCentimeter = 392
	MicrogramsPerSquareCentimeter = 393
	NumbersPerLiter = 394
	ThousandNumbersPerLiter = 395
	MillionNumbersPerLiter = 396
	NumbersPerSquareMeter = 397
	ThousandNumbersPerSquareMeter = 398
	MillionNumbersPerSquareMeter = 399
	NumbersPerSquareFeet = 400
	ThousandNumbersPerSquareFeet = 401
	MillionNumbersPerSquareFeet = 402
	NumbersPerSquareCentimeter = 403
	ThousandNumbersPerSquareCentimeter = 404
	MillionNumbersPerSquareCentimeter = 405
	MolesPerLiter = 406
	MilliMolesPerLiter = 407
	MolesPerSquareMeter = 408
	MilliMolesPerSquareMeter = 409
	MolesPerSquareFeet = 410
	MilliMolesPerSquareFeet = 411
	MolesPerSquareCentimeter = 412
	MilliMolesPerSquareCentimeter = 413
	PercentPerSecondPerCubicFeetPerSecond = 414
	PercentPerSecondPerCubicFeetPerMinute = 415
	PercentPerSecondPerCubicMeterPerSecond = 416
	PercentPerSecondPerCubicMeterPerMinute = 417
	PercentPerSecondPerLiterPerSecond = 418
	PercentPerSecondPerLiterPerMinute = 419
	PercentPerSecondPerGalPerSecond = 420
	PercentPerSecondPerGalPerMinute = 421
	MicrometersPerSecond = 422
	CubicFeetPerMilePerSecond = 423
	LitersPerKiliometersPerSecond = 424
	QuadFootPerSecond = 425
	GallonsPerFootPerMinute = 426
	GallonsPerMilePerMinute = 427
	QuadMetersPerSecond = 428
	CubicMetersPerKiliometerPerSecond = 429
	LitersPerMeterPerSecond = 430
	LitersPerHectaresPerSecond = 431
	MetersPerSquareSecond = 432
	FeetPerSquareSecond = 433

class UnitSystemIndex(Enum):
	None = 0
	Si = 1
	UsCustomary = 2
	Both = 3

class BaseUnitConverter(IUnitConverter):

	def __init__(self) -> None:
		"""No Description
		"""
		pass

	def FromBaseUnit(self, adouble: float) -> float:
		"""No Description

		Args:
			adouble(float): adouble

		Returns:
			float: 
		"""
		pass

	def ToBaseUnit(self, adouble: float) -> float:
		"""No Description

		Args:
			adouble(float): adouble

		Returns:
			float: 
		"""
		pass

class DegreesFahrenheitConverter(IUnitConverter):

	def __init__(self) -> None:
		"""No Description
		"""
		pass

	def FromBaseUnit(self, adoubleCelsius: float) -> float:
		"""No Description

		Args:
			adoubleCelsius(float): adoubleCelsius

		Returns:
			float: 
		"""
		pass

	def ToBaseUnit(self, adoubleFahrenheit: float) -> float:
		"""No Description

		Args:
			adoubleFahrenheit(float): adoubleFahrenheit

		Returns:
			float: 
		"""
		pass

class KelvinConverter(IUnitConverter):

	def __init__(self) -> None:
		"""No Description
		"""
		pass

	def FromBaseUnit(self, adoubleCelsius: float) -> float:
		"""No Description

		Args:
			adoubleCelsius(float): adoubleCelsius

		Returns:
			float: 
		"""
		pass

	def ToBaseUnit(self, adoubleKelvin: float) -> float:
		"""No Description

		Args:
			adoubleKelvin(float): adoubleKelvin

		Returns:
			float: 
		"""
		pass

class SlopeConverter(IUnitConverter):

	def __init__(self) -> None:
		"""No Description
		"""
		pass

	def FromBaseUnit(self, adouble: float) -> float:
		"""No Description

		Args:
			adouble(float): adouble

		Returns:
			float: 
		"""
		pass

	def ToBaseUnit(self, adouble: float) -> float:
		"""No Description

		Args:
			adouble(float): adouble

		Returns:
			float: 
		"""
		pass

class EmitterCoefficientConverterUS(IUnitConverter):

	def __init__(self, aTargetUnitFlowFactor: float) -> None:
		"""No Description

		Args:
			aTargetUnitFlowFactor(float): aTargetUnitFlowFactor
		"""
		pass

	def FromBaseUnit(self, aDouble: float) -> float:
		"""No Description

		Args:
			aDouble(float): aDouble

		Returns:
			float: 
		"""
		pass

	def ToBaseUnit(self, aDouble: float) -> float:
		"""No Description

		Args:
			aDouble(float): aDouble

		Returns:
			float: 
		"""
		pass

class EmitterCoefficientConverterSI(IUnitConverter):

	def __init__(self, aTargetUnitFlowFactor: float) -> None:
		"""No Description

		Args:
			aTargetUnitFlowFactor(float): aTargetUnitFlowFactor
		"""
		pass

	def FromBaseUnit(self, aDouble: float) -> float:
		"""No Description

		Args:
			aDouble(float): aDouble

		Returns:
			float: 
		"""
		pass

	def ToBaseUnit(self, aDouble: float) -> float:
		"""No Description

		Args:
			aDouble(float): aDouble

		Returns:
			float: 
		"""
		pass

