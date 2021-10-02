from typing import TypeVar

TFieldType = TypeVar("TFieldType", )
TNetworkElementTypeEnum = TypeVar("TNetworkElementTypeEnum", Enum)
TNetworkElementType = TypeVar("TNetworkElementType", Enum)

class IFieldInfo(INamable, ILabeled):

	def __init__(self) -> None:
		"""Creating a new Instance of this class is not allowed


		Raises:
			Exception: if this class is instanciated
		"""
		raise Exception("Creating a new Instance of this class is not allowed")
		pass

	def GetValue(self, id: int) -> TValueType:
		"""Method Description

		Args:
			id(int): id

		Returns:
			TValueType: 
		"""
		pass

	def SetValue(self, id: int, value: TValueType) -> None:
		"""Method Description

		Args:
			id(int): id
			value(TValueType): value

		Returns:
			None: 
		"""
		pass

	@property
	def Field(self) -> IField:
		"""
		Returns:
			IField: No Description
		"""
		pass

	@property
	def FieldType(self) -> int:
		"""
		Returns:
			int: No Description
		"""
		pass

	@property
	def FieldDataType(self) -> int:
		"""
		Returns:
			int: No Description
		"""
		pass

	@property
	def StorageUnit(self) -> Unit:
		"""
		Returns:
			Unit: No Description
		"""
		pass

	@property
	def Unit(self) -> IUnit:
		"""
		Returns:
			IUnit: No Description
		"""
		pass

class INetworkFieldInfo(IFieldInfo, INamable, ILabeled):

	def __init__(self) -> None:
		"""Creating a new Instance of this class is not allowed


		Raises:
			Exception: if this class is instanciated
		"""
		raise Exception("Creating a new Instance of this class is not allowed")
		pass

	@property
	def AlternativeTypeName(self) -> str:
		"""
		Returns:
			str: No Description
		"""
		pass

	@property
	def DomainElementTypeName(self) -> str:
		"""
		Returns:
			str: No Description
		"""
		pass

class IUserNetworkfieldInfo(INetworkFieldInfo, IFieldInfo, INamable, ILabeled):

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

class IResultFieldInfo(IFieldInfo, INamable, ILabeled):

	def __init__(self) -> None:
		"""Creating a new Instance of this class is not allowed


		Raises:
			Exception: if this class is instanciated
		"""
		raise Exception("Creating a new Instance of this class is not allowed")
		pass

	@property
	def ResultRecordTypeName(self) -> str:
		"""
		Returns:
			str: No Description
		"""
		pass

	@property
	def NumericalEngineTypeName(self) -> str:
		"""
		Returns:
			str: No Description
		"""
		pass

class IComponentElementFieldInfo(IFieldInfo, INamable, ILabeled):

	def __init__(self) -> None:
		"""Creating a new Instance of this class is not allowed


		Raises:
			Exception: if this class is instanciated
		"""
		raise Exception("Creating a new Instance of this class is not allowed")
		pass

	@property
	def SupportElementTypeName(self) -> str:
		"""
		Returns:
			str: No Description
		"""
		pass

class IFieldManager:

	def __init__(self) -> None:
		"""Creating a new Instance of this class is not allowed


		Raises:
			Exception: if this class is instanciated
		"""
		raise Exception("Creating a new Instance of this class is not allowed")
		pass

	def FieldByName(self, name: str) -> IFieldInfo:
		"""Method Description

		Args:
			name(str): name

		Returns:
			IFieldInfo: 
		"""
		pass

	def FieldByLabel(self, label: str) -> IFieldInfo:
		"""Method Description

		Args:
			label(str): label

		Returns:
			IFieldInfo: 
		"""
		pass

	@property
	def FieldInfo(self) -> IReadOnlyCollection`1:
		"""
		Returns:
			IReadOnlyCollection`1: No Description
		"""
		pass

class IUserFieldOptions(Generic[TFieldType, TNetworkElementTypeEnum]):

	def __init__(self) -> None:
		"""Creating a new Instance of this class is not allowed


		Raises:
			Exception: if this class is instanciated
		"""
		raise Exception("Creating a new Instance of this class is not allowed")
		pass

	@property
	def FieldType(self) -> int:
		"""
		Returns:
			int: No Description
		"""
		pass

	@property
	def Name(self) -> str:
		"""
		Returns:
			str: No Description
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
	def ElementType(self) -> TNetworkElementTypeEnum:
		"""
		Returns:
			TNetworkElementTypeEnum: No Description
		"""
		pass

	@property
	def SharedWith(self) -> List[TNetworkElementTypeEnum]:
		"""
		Returns:
			List[TNetworkElementTypeEnum]: No Description
		"""
		pass

	@property
	def DefaultValue(self) -> TFieldType:
		"""
		Returns:
			TFieldType: No Description
		"""
		pass

	@property
	def Category(self) -> str:
		"""
		Returns:
			str: No Description
		"""
		pass

	@property
	def JustLikeField(self) -> IFieldInfo:
		"""
		Returns:
			IFieldInfo: No Description
		"""
		pass

	@Name.setter
	def Name(self, name: str) -> None:
		pass

	@Label.setter
	def Label(self, label: str) -> None:
		pass

	@ElementType.setter
	def ElementType(self, elementtype: TNetworkElementTypeEnum) -> None:
		pass

	@DefaultValue.setter
	def DefaultValue(self, defaultvalue: TFieldType) -> None:
		pass

	@Category.setter
	def Category(self, category: str) -> None:
		pass

	@JustLikeField.setter
	def JustLikeField(self, justlikefield: IFieldInfo) -> None:
		pass

class IUserFieldManager(Generic[TNetworkElementType]):

	def __init__(self) -> None:
		"""Creating a new Instance of this class is not allowed


		Raises:
			Exception: if this class is instanciated
		"""
		raise Exception("Creating a new Instance of this class is not allowed")
		pass

	def NewFieldOptions(self) -> IUserFieldOptions`2:
		"""Method Description

		Returns:
			IUserFieldOptions`2: 
		"""
		pass

	def CreateField(self, options: IUserFieldOptions`2) -> IUserNetworkfieldInfo:
		"""Method Description

		Args:
			options(IUserFieldOptions`2): options

		Returns:
			IUserNetworkfieldInfo: 
		"""
		pass

