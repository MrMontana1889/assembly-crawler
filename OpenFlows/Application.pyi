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
		"""Sets the handle of the parent window.

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
		"""Starts the application

		Returns:
			None: 
		"""
		pass

	def SetParentFormSurrogateDelegate(self, parentFormSurrgateDelegate: ParentFormSurrogateDelegate) -> None:
		"""Provides a custom ParentFormSurrogate to use for the application
            instead of the default implementation.

		Args:
			parentFormSurrgateDelegate(ParentFormSurrogateDelegate): parentFormSurrgateDelegate

		Returns:
			None: 
		"""
		pass

	def Stop(self) -> None:
		"""Stops the application

		Returns:
			None: 
		"""
		pass

	@property
	def DomainApplicationModel(self) -> IDomainApplicationModel:
		"""No Description

		Returns:
			IApplicationManager: 
		"""
		pass

	@property
	def ParentFormModel(self) -> HaestadParentFormModel:
		"""No Description

		Returns:
			IApplicationManager: 
		"""
		pass

	@property
	def ParentFormUIModel(self) -> GraphicalParentFormUIModelBase:
		"""No Description

		Returns:
			IApplicationManager: 
		"""
		pass

	@property
	def ParentFormSurrogate(self) -> IParentFormSurrogate:
		"""No Description

		Returns:
			IApplicationManager: 
		"""
		pass

	@property
	def IsStarted(self) -> bool:
		"""No Description

		Returns:
			IApplicationManager: 
		"""
		pass

