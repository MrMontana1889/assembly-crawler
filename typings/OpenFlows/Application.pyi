from typing import overload
from System import IntPtr

class ApplicationManagerBase(IApplicationManager):

	def __init__(self) -> None:
		"""Creating a new Instance of this class is not allowed


		Raises
		--------
			Exception: if this class is instantiated
		"""
		raise Exception("Creating a new Instance of this class is not allowed")
		pass

	@staticmethod
	def SetApplicationManager(applicationManager: IApplicationManager) -> None:
		"""No Description

		Args
		--------
			applicationManager (``IApplicationManager``) :  applicationManager

		Returns
		--------
			``None`` : 
		"""
		pass

	def Start(self, openUI: bool = True) -> None:
		"""No Description

		Args
		--------
			openUI (``bool``) :  openUI

		Returns
		--------
			``None`` : 
		"""
		pass

	@overload
	def SetParentFormSurrogateDelegate(self, parentFormSurrogateDelegate: ParentFormSurrogateDelegate) -> None:
		"""No Description

		Args
		--------
			parentFormSurrogateDelegate (``ParentFormSurrogateDelegate``) :  parentFormSurrogateDelegate

		Returns
		--------
			``None`` : 
		"""
		pass

	def Stop(self) -> None:
		"""No Description

		Returns
		--------
			``None`` : 
		"""
		pass

	@overload
	def SetParentFormSurrogateDelegate(self, parentFormSurrgateDelegate: ParentFormSurrogateDelegate) -> None:
		"""No Description

		Args
		--------
			parentFormSurrgateDelegate (``ParentFormSurrogateDelegate``) :  parentFormSurrgateDelegate

		Returns
		--------
			``None`` : 
		"""
		pass

	@property
	def DomainApplicationModel(self) -> IDomainApplicationModel:
		"""No Description

		Returns
		--------
			``ApplicationManagerBase`` : 
		"""
		pass

	@property
	def ParentFormModel(self) -> HaestadParentFormModel:
		"""No Description

		Returns
		--------
			``ApplicationManagerBase`` : 
		"""
		pass

	@property
	def ParentFormUIModel(self) -> GraphicalParentFormUIModelBase:
		"""No Description

		Returns
		--------
			``ApplicationManagerBase`` : 
		"""
		pass

	@property
	def ParentFormSurrogate(self) -> IParentFormSurrogate:
		"""No Description

		Returns
		--------
			``ApplicationManagerBase`` : 
		"""
		pass

	@property
	def IsStarted(self) -> bool:
		"""No Description

		Returns
		--------
			``ApplicationManagerBase`` : 
		"""
		pass

	@IsStarted.setter
	def IsStarted(self, isstarted: bool) -> None:
		pass

	@property
	def ExitCode(self) -> int:
		"""No Description

		Returns
		--------
			``ApplicationManagerBase`` : 
		"""
		pass

	@ExitCode.setter
	def ExitCode(self, exitcode: int) -> None:
		pass

class IParentFormSurrogate(IWin32Window, IUserInterface):

	def __init__(self) -> None:
		"""Creating a new Instance of this class is not allowed


		Raises
		--------
			Exception: if this class is instantiated
		"""
		raise Exception("Creating a new Instance of this class is not allowed")
		pass

	def SetParentWindowHandle(self, handle: IntPtr) -> None:
		"""No Description

		Args
		--------
			handle (``IntPtr``) :  handle

		Returns
		--------
			``None`` : 
		"""
		pass

class IApplicationManager:

	def __init__(self) -> None:
		"""Creating a new Instance of this class is not allowed


		Raises
		--------
			Exception: if this class is instantiated
		"""
		raise Exception("Creating a new Instance of this class is not allowed")
		pass

	def Start(self, openUI: bool = True) -> None:
		"""No Description

		Args
		--------
			openUI (``bool``) :  openUI

		Returns
		--------
			``None`` : 
		"""
		pass

	def SetParentFormSurrogateDelegate(self, parentFormSurrgateDelegate: ParentFormSurrogateDelegate) -> None:
		"""No Description

		Args
		--------
			parentFormSurrgateDelegate (``ParentFormSurrogateDelegate``) :  parentFormSurrgateDelegate

		Returns
		--------
			``None`` : 
		"""
		pass

	def Stop(self) -> None:
		"""No Description

		Returns
		--------
			``None`` : 
		"""
		pass

	@property
	def DomainApplicationModel(self) -> IDomainApplicationModel:
		"""No Description

		Returns
		--------
			``IApplicationManager`` : 
		"""
		pass

	@property
	def ParentFormModel(self) -> HaestadParentFormModel:
		"""No Description

		Returns
		--------
			``IApplicationManager`` : 
		"""
		pass

	@property
	def ParentFormUIModel(self) -> GraphicalParentFormUIModelBase:
		"""No Description

		Returns
		--------
			``IApplicationManager`` : 
		"""
		pass

	@property
	def ParentFormSurrogate(self) -> IParentFormSurrogate:
		"""No Description

		Returns
		--------
			``IApplicationManager`` : 
		"""
		pass

	@property
	def IsStarted(self) -> bool:
		"""No Description

		Returns
		--------
			``IApplicationManager`` : 
		"""
		pass

	@property
	def ExitCode(self) -> int:
		"""No Description

		Returns
		--------
			``IApplicationManager`` : 
		"""
		pass

