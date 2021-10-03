from typing import overload

class ILicenseManager(ILicenseProvider):

	def __init__(self) -> None:
		"""Creating a new Instance of this class is not allowed


		Raises:
			Exception: if this class is instanciated
		"""
		raise Exception("Creating a new Instance of this class is not allowed")
		pass

	@overload
	def ILicenseManager(self, product: ProductId, parentWindow: IntPtr) -> LicenseRunStatusEnum:
		"""Method Description

		Args:
			product(ProductId): product
			parentWindow(IntPtr): parentWindow

		Returns:
			LicenseRunStatusEnum: 
		"""
		pass

	@overload
	def ILicenseManager(self, licensedFeatureSet: ILicensedFeatureSet) -> LicenseRunStatusEnum:
		"""Method Description

		Args:
			licensedFeatureSet(ILicensedFeatureSet): licensedFeatureSet

		Returns:
			LicenseRunStatusEnum: 
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

	def GetLicenseStatus(self) -> LicenseStatus:
		"""Method Description

		Returns:
			LicenseStatus: 
		"""
		pass

	@property
	def LicenseRunStatus(self) -> LicenseRunStatusEnum:
		"""
		Returns:
			LicenseRunStatusEnum: No Description
		"""
		pass

