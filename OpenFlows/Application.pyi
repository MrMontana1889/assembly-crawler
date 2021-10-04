from OpenFlows.Enumerations import *

class IParentFormSurrogate(IWin32Window, IUserInterface):

	def __init__(self) -> None:
		"""Creating a new Instance of this class is not allowed


		Raises:
			Exception: if this class is instanciated
		"""
		raise Exception("Creating a new Instance of this class is not allowed")
		pass

	def SetParentWindowHandle(self, handle: int) -> None:
		"""Method Description

		Args:
			handle(int): handle

		Returns:
			None: 
		"""
		pass

class IApplicationManager:

	def __init__(self) -> None:
		"""Creating a new Instance of this class is not allowed


		Raises:
			Exception: if this class is instanciated
		"""
		raise Exception("Creating a new Instance of this class is not allowed")
		pass

	def Start(self) -> None:
		"""Method Description

		Returns:
			None: 
		"""
		pass

	def SetParentFormSurrogateDelegate(self, parentFormSurrgateDelegate: ParentFormSurrogateDelegate) -> None:
		"""Method Description

		Args:
			parentFormSurrgateDelegate(ParentFormSurrogateDelegate): parentFormSurrgateDelegate

		Returns:
			None: 
		"""
		pass

	def Stop(self) -> None:
		"""Method Description

		Returns:
			None: 
		"""
		pass

	@property
	def DomainApplicationModel(self) -> IDomainApplicationModel:
		"""
		Returns:
			IDomainApplicationModel: No Description
		"""
		pass

	@property
	def ParentFormModel(self) -> HaestadParentFormModel:
		"""
		Returns:
			HaestadParentFormModel: No Description
		"""
		pass

	@property
	def ParentFormUIModel(self) -> GraphicalParentFormUIModelBase:
		"""
		Returns:
			GraphicalParentFormUIModelBase: No Description
		"""
		pass

	@property
	def ParentFormSurrogate(self) -> IParentFormSurrogate:
		"""
		Returns:
			IParentFormSurrogate: No Description
		"""
		pass

	@property
	def IsStarted(self) -> bool:
		"""
		Returns:
			bool: No Description
		"""
		pass

