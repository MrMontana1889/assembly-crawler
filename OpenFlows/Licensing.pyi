from typing import overload
from OpenFlows.Enumerations import *

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
		"""Initializes the license for a given product type.

		Args:
			product(ProductId): product
			parentWindow(IntPtr): parentWindow

		Returns:
			LicenseRunStatusEnum: 
		"""
		pass

	@overload
	def ILicenseManager(self, licensedFeatureSet: ILicensedFeatureSet) -> LicenseRunStatusEnum:
		"""Initializes the LicenseManager using the Framework-managed ILicensedFeatureSet

		Args:
			licensedFeatureSet(ILicensedFeatureSet): licensedFeatureSet

		Returns:
			LicenseRunStatusEnum: 
		"""
		pass

	def IsInitialized(self) -> bool:
		"""Checks to see if the license is initialized.

		Returns:
			bool: 
		"""
		pass

	def CheckLicenseState(self) -> None:
		"""Checks the state of the license.

		Returns:
			None: 
		"""
		pass

	def IsLicenseValid(self) -> bool:
		"""Checks to see if the license is valid.

		Returns:
			bool: 
		"""
		pass

	def GetLicenseStatus(self) -> LicenseStatus:
		"""Gets the current status of the license.

		Returns:
			LicenseStatus: 
		"""
		pass

	@property
	def LicenseRunStatus(self) -> LicenseRunStatusEnum:
		"""No Description

		Returns:
			ILicenseManager: 
		"""
		pass

