from typing import overload

class ILicenseManager(IDisposable, ILicenseProvider):

	def __init__(self) -> None:
		"""Creating a new Instance of this class is not allowed


		Raises:
			Exception: if this class is instanciated
		"""
		raise Exception("Creating a new Instance of this class is not allowed")
		pass

	@overload
	def ILicenseManager(self, product: int, parentWindow: IntPtr) -> int:
		"""Method Description

		Args:
			product(int): product
			parentWindow(IntPtr): parentWindow

		Returns:
			int: 
		"""
		pass

	@overload
	def ILicenseManager(self, licensedFeatureSet: ILicensedFeatureSet) -> int:
		"""Method Description

		Args:
			licensedFeatureSet(ILicensedFeatureSet): licensedFeatureSet

		Returns:
			int: 
		"""
		pass

	def IsInitialized(self) -> bool:
		"""Method Description

		Returns:
			bool: 
		"""
		pass

	def CheckLicenseState(self) -> None:
		"""Method Description

		Returns:
			None: 
		"""
		pass

	def IsLicenseValid(self) -> bool:
		"""Method Description

		Returns:
			bool: 
		"""
		pass

	def GetLicenseStatus(self) -> int:
		"""Method Description

		Returns:
			int: 
		"""
		pass

	@property
	def LicenseRunStatus(self) -> int:
		"""
		Returns:
			int: No Description
		"""
		pass

