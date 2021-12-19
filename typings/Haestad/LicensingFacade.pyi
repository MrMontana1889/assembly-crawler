from enum import Enum
from System import TypeCode
from typing import overload, Dict
from datetime import datetime
from Haestad.LicensingFacade import LicenseRunStatusEnum

class LicenseRunStatusEnum(Enum):
	OK = 1001
	LIMITED = 1002
	SHUTDOWN = 1003
	UNKNOWN = -1

class LicenseStatus(Enum):
	OK = 101
	OFFLINE = 102
	PREACTIVATION = 104
	EXPIRED = 105
	ACCESSDENIED = 106
	DISABLEDBYLOGSEND = 107
	DISABLEDBYPOLICY = 108
	TRIAL = 109
	NOTENTITLED = 110
	UNKNOWN = -999
	ERROR = -1

class LicenseType(Enum):
	UNKNOWN = 0
	COMMERCIAL = 1
	ACADEMIC = 2
	HOMEUSE = 3
	NONCOMMERCIAL = 4
	TRIAL = 5
	FUTURETYPE2 = 6
	TEMPORARY = 99
	ERROR = -1

class LicenseEventType(Enum):
	LIVEUSAGEPOSTINGOCCURED = 0
	DEFERREDUSAGEPOSTINGOCCURED = 1
	USAGEPOSTINGERROROCCURED = 2
	SHUTDOWNPRODUCT = 3
	CCSTARTUP = 4
	CCSHUTDOWN = 5
	CCLOGIN = 6
	CCLOGOUT = 7

class ProductId(Enum):
	MICROSTATION = 1000
	BENTLEY_REDLINE = 1146
	BENTLEY_CIVILSTORM = 1207
	BENTLEY_CULVERTMASTER = 1210
	BENTLEY_CALIBRATOR = 1211
	BENTLEY_DESIGNER = 1212
	BENTLEY_FLOWMASTER = 1222
	BENTLEY_GISCONNECT = 1223
	BENTLEY_HEC_PACK = 1224
	BENTLEY_HAMMER = 1225
	BENTLEY_PONDPACK = 1233
	BENTLEY_SCADACONNECT = 1239
	BENTLEY_SEWERCAD = 1243
	BENTLEY_SEWERGEMS = 1244
	BENTLEY_SKELEBRATOR = 1245
	BENTLEY_STORMCAD = 1246
	BENTLEY_WATERCAD = 1248
	BENTLEY_WATERGEMS = 1249
	BENTLEY_WATERSAFE = 1250
	BENTLEY_SCHEDULER = 1860
	BENTLEY_GASANALYSIS = 1861
	BENTLEY_PIPEASSETPLANNER = 1895
	BENTLEY_SUE = 2335
	BENTLEY_OPENROADSDESIGNER = 2515
	BENTLEY_OPENRAILDESIGNER = 2641
	BENTLEY_CNCCBIMOPENROADS = 2697
	BENTLEY_OPENSITEDESIGNER = 2758
	BENTLEY_WATEROPS = 2922
	BENTLEY_SEWEROPS = 2923
	BENTLEY_OVERHEADLINEDESIGNER = 2963

class LicensePlatformType(Enum):
	UNKNOWN = 0
	MICROSTATION = 1
	AUTOCAD = 2
	ARCGIS = 3
	STANDALONE = 4
	NAVIGATOR = 5
	MX = 6
	GEOPAK = 7
	INROADS = 8
	OPENPLANTMODELER = 9
	OUTLOOKCONNECTOR = 10
	SHAREPOINTCONNECTOR = 11
	PROJECTWISE = 12

class ArchitectureType(Enum):
	X86 = 0
	X64 = 1

class ILicense:

	def __init__(self) -> None:
		"""Creating a new Instance of this class is not allowed


		Raises
		--------
			Exception: if this class is instantiated
		"""
		raise Exception("Creating a new Instance of this class is not allowed")
		pass

	def Initialize(self) -> bool:
		"""No Description

		Returns
		--------
			``bool`` : 
		"""
		pass

	def GetLicenseStatus(self) -> LicenseStatus:
		"""No Description

		Returns
		--------
			``LicenseStatus`` : 
		"""
		pass

	def StartDesktop(self) -> LicenseRunStatusEnum:
		"""No Description

		Returns
		--------
			``LicenseRunStatusEnum`` : 
		"""
		pass

	def StopDesktop(self) -> None:
		"""No Description

		Returns
		--------
			``None`` : 
		"""
		pass

	@overload
	def StartFeatureTracking(self, featureID: Guid, featureUserDataMap: Dict[str,str], instanceID: int) -> bool:
		"""No Description

		Args
		--------
			featureID (``Guid``) :  featureID
			featureUserDataMap (``Dict[str,str]``) :  featureUserDataMap
			instanceID (``int``) :  instanceID

		Returns
		--------
			``bool`` : 
		"""
		pass

	@overload
	def StartFeatureTracking(self, featureID: Guid, instanceID: int) -> bool:
		"""No Description

		Args
		--------
			featureID (``Guid``) :  featureID
			instanceID (``int``) :  instanceID

		Returns
		--------
			``bool`` : 
		"""
		pass

	def StopFeatureTracking(self, instanceID: int) -> bool:
		"""No Description

		Args
		--------
			instanceID (``int``) :  instanceID

		Returns
		--------
			``bool`` : 
		"""
		pass

	@overload
	def FeatureTrackingMark(self, featureID: Guid, featureUserDataKeyValMap: Dict[str,str]) -> bool:
		"""No Description

		Args
		--------
			featureID (``Guid``) :  featureID
			featureUserDataKeyValMap (``Dict[str,str]``) :  featureUserDataKeyValMap

		Returns
		--------
			``bool`` : 
		"""
		pass

	@overload
	def FeatureTrackingMark(self, featureID: Guid) -> bool:
		"""No Description

		Args
		--------
			featureID (``Guid``) :  featureID

		Returns
		--------
			``bool`` : 
		"""
		pass

	def StartDesktopProject(self, projectID: str) -> bool:
		"""No Description

		Args
		--------
			projectID (``str``) :  projectID

		Returns
		--------
			``bool`` : 
		"""
		pass

	def StopDesktopProject(self) -> bool:
		"""No Description

		Returns
		--------
			``bool`` : 
		"""
		pass

	def StartMLA(self, apProduct: ProductRelease, waitForExit: bool) -> None:
		"""No Description

		Args
		--------
			apProduct (``ProductRelease``) :  apProduct
			waitForExit (``bool``) :  waitForExit

		Returns
		--------
			``None`` : 
		"""
		pass

	def IsAnalysisEnabledMessage(self, showMessage: bool) -> bool:
		"""No Description

		Args
		--------
			showMessage (``bool``) :  showMessage

		Returns
		--------
			``bool`` : 
		"""
		pass

	def IsPrintingEnabledMessage(self, showMessage: bool) -> bool:
		"""No Description

		Args
		--------
			showMessage (``bool``) :  showMessage

		Returns
		--------
			``bool`` : 
		"""
		pass

	def GetProxyInformation(self, proxyName: str, proxyNeedsAuth: bool, proxyUserName: str, proxyPw: str, handshake: str) -> bool:
		"""No Description

		Args
		--------
			proxyName (``str``) :  proxyName
			proxyNeedsAuth (``bool``) :  proxyNeedsAuth
			proxyUserName (``str``) :  proxyUserName
			proxyPw (``str``) :  proxyPw
			handshake (``str``) :  handshake

		Returns
		--------
			``bool`` : 
		"""
		pass

	def GetComputerName(self) -> str:
		"""No Description

		Returns
		--------
			``str`` : 
		"""
		pass

	def GetDaysUntilDisabled(self) -> int:
		"""No Description

		Returns
		--------
			``int`` : 
		"""
		pass

	def GetOrganizationName(self) -> str:
		"""No Description

		Returns
		--------
			``str`` : 
		"""
		pass

	def GetUsername(self) -> str:
		"""No Description

		Returns
		--------
			``str`` : 
		"""
		pass

	def GetLicenseType(self) -> LicenseType:
		"""No Description

		Returns
		--------
			``LicenseType`` : 
		"""
		pass

	def GetExpirationDate(self) -> datetime:
		"""No Description

		Returns
		--------
			``datetime`` : 
		"""
		pass

	def ClearDefaultFeatureString(self) -> bool:
		"""No Description

		Returns
		--------
			``bool`` : 
		"""
		pass

	@property
	def IsTemporaryLicense(self) -> bool:
		"""No Description

		Returns
		--------
			``ILicense`` : 
		"""
		pass

	@property
	def RunStatus(self) -> LicenseRunStatusEnum:
		"""No Description

		Returns
		--------
			``ILicense`` : 
		"""
		pass

	@property
	def SizeEnabled(self) -> int:
		"""No Description

		Returns
		--------
			``ILicense`` : 
		"""
		pass

	@property
	def IsSUDAEnabled(self) -> bool:
		"""No Description

		Returns
		--------
			``ILicense`` : 
		"""
		pass

	@IsSUDAEnabled.setter
	def IsSUDAEnabled(self, issudaenabled: bool) -> None:
		pass

	@property
	def IsMicroStationEnabled(self) -> bool:
		"""No Description

		Returns
		--------
			``ILicense`` : 
		"""
		pass

	@property
	def IsArcGISEnabled(self) -> bool:
		"""No Description

		Returns
		--------
			``ILicense`` : 
		"""
		pass

	@property
	def IsAutoCADEnabled(self) -> bool:
		"""No Description

		Returns
		--------
			``ILicense`` : 
		"""
		pass

	@property
	def IsPrintingEnabled(self) -> bool:
		"""No Description

		Returns
		--------
			``ILicense`` : 
		"""
		pass

	@property
	def IsAnalysisEnabled(self) -> bool:
		"""No Description

		Returns
		--------
			``ILicense`` : 
		"""
		pass

	@property
	def IsDefaultFeatureSet(self) -> bool:
		"""No Description

		Returns
		--------
			``ILicense`` : 
		"""
		pass

	@property
	def ReadableType(self) -> str:
		"""No Description

		Returns
		--------
			``ILicense`` : 
		"""
		pass

	@property
	def ReadableFeatureStringType(self) -> str:
		"""No Description

		Returns
		--------
			``ILicense`` : 
		"""
		pass

	@property
	def FeatureString(self) -> str:
		"""No Description

		Returns
		--------
			``ILicense`` : 
		"""
		pass

	@property
	def Features(self) -> FeatureMap:
		"""No Description

		Returns
		--------
			``ILicense`` : 
		"""
		pass

	@property
	def DefaultFeatureString(self) -> str:
		"""No Description

		Returns
		--------
			``ILicense`` : 
		"""
		pass

	@DefaultFeatureString.setter
	def DefaultFeatureString(self, defaultfeaturestring: str) -> None:
		pass

	@property
	def IsCheckedOutLicense(self) -> bool:
		"""No Description

		Returns
		--------
			``ILicense`` : 
		"""
		pass

	@property
	def IsInitialized(self) -> bool:
		"""No Description

		Returns
		--------
			``ILicense`` : 
		"""
		pass

	@property
	def Product(self) -> ProductRelease:
		"""No Description

		Returns
		--------
			``ILicense`` : 
		"""
		pass

class ILicenseProvider:

	def __init__(self) -> None:
		"""Creating a new Instance of this class is not allowed


		Raises
		--------
			Exception: if this class is instantiated
		"""
		raise Exception("Creating a new Instance of this class is not allowed")
		pass

	def GetActiveLicense(self) -> License:
		"""No Description

		Returns
		--------
			``License`` : 
		"""
		pass

	def GetComputeTrackingID(self) -> Guid:
		"""No Description

		Returns
		--------
			``Guid`` : 
		"""
		pass

	def GetComputeSCADATrackingID(self) -> Guid:
		"""No Description

		Returns
		--------
			``Guid`` : 
		"""
		pass

	def AddFeatureUserData(self, userKey: str, userValue: str) -> None:
		"""No Description

		Args
		--------
			userKey (``str``) :  userKey
			userValue (``str``) :  userValue

		Returns
		--------
			``None`` : 
		"""
		pass

	@property
	def FeatureDataMap(self) -> Dict[str,str]:
		"""No Description

		Returns
		--------
			``ILicenseProvider`` : 
		"""
		pass

class IFeatureTrackingProvider(ILicenseProvider):

	def __init__(self) -> None:
		"""Creating a new Instance of this class is not allowed


		Raises
		--------
			Exception: if this class is instantiated
		"""
		raise Exception("Creating a new Instance of this class is not allowed")
		pass

	def IsFeatureTracked(self) -> bool:
		"""No Description

		Returns
		--------
			``bool`` : 
		"""
		pass

