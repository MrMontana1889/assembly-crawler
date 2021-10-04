from typing import Generic, overload, TypeVar
from OpenFlows.Enumerations import *

TNetworkUnitsType = TypeVar("TNetworkUnitsType", INetworkUnits)
TComponentUnitsType = TypeVar("TComponentUnitsType", IComponentUnits)

class IModelUnits(Generic[TNetworkUnitsType, TComponentUnitsType]):

	def __init__(self) -> None:
		"""Creating a new Instance of this class is not allowed


		Raises:
			Exception: if this class is instanciated
		"""
		raise Exception("Creating a new Instance of this class is not allowed")
		pass

	@property
	def Units(self) -> IUnits:
		"""
		Returns:
			IUnits: No Description
		"""
		pass

class INetworkUnits:

	def __init__(self) -> None:
		"""Creating a new Instance of this class is not allowed


		Raises:
			Exception: if this class is instanciated
		"""
		raise Exception("Creating a new Instance of this class is not allowed")
		pass

class IComponentUnits:

	def __init__(self) -> None:
		"""Creating a new Instance of this class is not allowed


		Raises:
			Exception: if this class is instanciated
		"""
		raise Exception("Creating a new Instance of this class is not allowed")
		pass

class IUnits(Generic[TNetworkUnitsType, TComponentUnitsType]):

	def __init__(self) -> None:
		"""Creating a new Instance of this class is not allowed


		Raises:
			Exception: if this class is instanciated
		"""
		raise Exception("Creating a new Instance of this class is not allowed")
		pass

	@overload
	def IUnits(self, value: float, unit: IUnit) -> str:
		"""Method Description

		Args:
			value(float): value
			unit(IUnit): unit

		Returns:
			str: 
		"""
		pass

	@overload
	def IUnits(self, value: float, unit: IUnit, format: FormatCode, signficantDigits: int) -> str:
		"""Method Description

		Args:
			value(float): value
			unit(IUnit): unit
			format(FormatCode): format
			signficantDigits(int): signficantDigits

		Returns:
			str: 
		"""
		pass

	def ConvertValue(self, value: float, fromUnit: Unit, toUnit: Unit) -> float:
		"""Method Description

		Args:
			value(float): value
			fromUnit(Unit): fromUnit
			toUnit(Unit): toUnit

		Returns:
			float: 
		"""
		pass

	def Reset(self, unitSystem: UnitSystemType) -> None:
		"""Method Description

		Args:
			unitSystem(UnitSystemType): unitSystem

		Returns:
			None: 
		"""
		pass

	@property
	def NetworkUnits(self) -> TNetworkUnitsType:
		"""
		Returns:
			TNetworkUnitsType: No Description
		"""
		pass

	@property
	def ComponentUnits(self) -> TComponentUnitsType:
		"""
		Returns:
			TComponentUnitsType: No Description
		"""
		pass

class IUnit:

	def __init__(self) -> None:
		"""Creating a new Instance of this class is not allowed


		Raises:
			Exception: if this class is instanciated
		"""
		raise Exception("Creating a new Instance of this class is not allowed")
		pass

	@overload
	def IUnit(self, value: float) -> str:
		"""Method Description

		Args:
			value(float): value

		Returns:
			str: 
		"""
		pass

	@overload
	def IUnit(self, value: float, format: FormatCode, significantDigits: int) -> str:
		"""Method Description

		Args:
			value(float): value
			format(FormatCode): format
			significantDigits(int): significantDigits

		Returns:
			str: 
		"""
		pass

	def SetUnit(self, unit: Unit) -> None:
		"""Method Description

		Args:
			unit(Unit): unit

		Returns:
			None: 
		"""
		pass

	def GetUnit(self) -> Unit:
		"""Method Description

		Returns:
			Unit: 
		"""
		pass

	def ConvertTo(self, value: float, unit: Unit) -> float:
		"""Method Description

		Args:
			value(float): value
			unit(Unit): unit

		Returns:
			float: 
		"""
		pass

	@property
	def Dimension(self) -> Dimension:
		"""
		Returns:
			Dimension: No Description
		"""
		pass

	@property
	def FormatCode(self) -> FormatCode:
		"""
		Returns:
			FormatCode: No Description
		"""
		pass

	@property
	def SignificantDigits(self) -> int:
		"""
		Returns:
			int: No Description
		"""
		pass

	@property
	def Label(self) -> str:
		"""
		Returns:
			str: No Description
		"""
		pass

	@property
	def ShortLabel(self) -> str:
		"""
		Returns:
			str: No Description
		"""
		pass

	@FormatCode.setter
	def FormatCode(self, formatcode: FormatCode) -> None:
		pass

	@SignificantDigits.setter
	def SignificantDigits(self, significantdigits: int) -> None:
		pass

