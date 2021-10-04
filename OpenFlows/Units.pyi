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
		"""No Description

		Returns:
			IModelUnits: 
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
		"""Formats the given value to the given unit's format.

		Args:
			value(float): The value to format
			unit(IUnit): The unit to use to format the value.

		Returns:
			str: 
		"""
		pass

	@overload
	def IUnits(self, value: float, unit: IUnit, format: FormatCode, signficantDigits: int) -> str:
		"""Formats the value using the unit, format and significant digits provided.

		Args:
			value(float): The value to format that is in the unit provided
			unit(IUnit): The unit the value is in.
			format(FormatCode): The format to use.
			signficantDigits(int): The number of digits to the right of the decimal.

		Returns:
			str: The format string of the provided value in the unit provided.
		"""
		pass

	def ConvertValue(self, value: float, fromUnit: Unit, toUnit: Unit) -> float:
		"""Convert a value from one unit to another.  The dimension of the toUnit and fromUnit mus be the same.

		Args:
			value(float): The value to convert.  Any value other than NaN
			fromUnit(Unit): The unit the value is currently in.
			toUnit(Unit): The unit to convert the value to.  Must be of the same dimension as fromUnit.

		Returns:
			float: The value in the toUnit specified.
		"""
		pass

	def Reset(self, unitSystem: UnitSystemType) -> None:
		"""Sets the units system to either SI or US Customary units

		Args:
			unitSystem(UnitSystemType): Resets all units to their default units of the given unit system.

		Returns:
			None: 
		"""
		pass

	@property
	def NetworkUnits(self) -> TNetworkUnitsType:
		"""No Description

		Returns:
			IUnits: 
		"""
		pass

	@property
	def ComponentUnits(self) -> TComponentUnitsType:
		"""No Description

		Returns:
			IUnits: 
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
		"""Format's the value into a string using the current unit's settings.

		Args:
			value(float): The value to format in the current unit

		Returns:
			str: A formatted string of the double value
		"""
		pass

	@overload
	def IUnit(self, value: float, format: FormatCode, significantDigits: int) -> str:
		"""Formats the value using the given format without overriding the settings of the Unit

		Args:
			value(float): The value to format in current unit
			format(FormatCode): Determines how the value is formatted
			significantDigits(int): The number of significant digits to the right of the decimal.

		Returns:
			str: A formatted string of the double value
		"""
		pass

	def SetUnit(self, unit: Unit) -> None:
		"""Sets the current unit.

		Args:
			unit(Unit): The unit to use and must be of the same dimension

		Returns:
			None: 
		"""
		pass

	def GetUnit(self) -> Unit:
		"""Gets the current assigned unit.

		Returns:
			Unit: The current unit
		"""
		pass

	def ConvertTo(self, value: float, unit: Unit) -> float:
		"""Converts a value from the current unit to the provided unit

		Args:
			value(float): The value to convert.  The value is assumed in the current unit
			unit(Unit): The value is converted to this unit.  The unit must be of the same dimension

		Returns:
			float: The converted value in the new unit
		"""
		pass

	@property
	def Dimension(self) -> Dimension:
		"""No Description

		Returns:
			IUnit: 
		"""
		pass

	@property
	def FormatCode(self) -> FormatCode:
		"""No Description

		Returns:
			IUnit: 
		"""
		pass

	@property
	def SignificantDigits(self) -> int:
		"""No Description

		Returns:
			IUnit: 
		"""
		pass

	@property
	def Label(self) -> str:
		"""No Description

		Returns:
			IUnit: 
		"""
		pass

	@property
	def ShortLabel(self) -> str:
		"""No Description

		Returns:
			IUnit: 
		"""
		pass

	@FormatCode.setter
	def FormatCode(self, formatcode: FormatCode) -> None:
		pass

	@SignificantDigits.setter
	def SignificantDigits(self, significantdigits: int) -> None:
		pass

