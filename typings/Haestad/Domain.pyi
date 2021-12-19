from enum import Enum
from System import TypeCode, ICloneable
from typing import overload, List, Dict, Iterator, Generic
from Haestad.Support.Support import FieldDataType, HmIDCollection, FieldCollection, IEditLabeled, IField, SortContextCollection, FilterContextCollection, GeometryPoint, IEditField, ILabeled
from Haestad.Support.Units import UnitIndex, NumericFormatter, TimeUnit, Unit, UnitSystem
from array import array
from Haestad.LicensingFacade import ILicenseProvider
from datetime import datetime
from System.Collections.Generic import T
from Haestad.Domain import IFieldManager


class ModelingElementType(Enum):
	ALL = 0
	ALTERNATIVE = 1
	SCENARIO = 2
	DOMAINELEMENT = 3
	SUPPORTELEMENT = 4
	CALCULATIONOPTIONS = 5
	ENGINEERINGLIBRARY = 6
	SELECTIONSET = 7
	EMBEDDEDSTICKYOBJECT = 8
	PROTOTYPEDOMAINELEMENT = 9
	PROFILE = 10

class ReferencedElementType(Enum):
	NONE = 0
	DOMAINELEMENT = 1
	SUPPORTELEMENT = 2
	SCENARIO = 3
	ALTERNATIVE = 4
	SELECTIONSET = 5

class DomainElementType(Enum):
	MANHOLEELEMENTMANAGER = 1
	CATCHBASINELEMENTMANAGER = 2
	CONDUITELEMENTMANAGER = 3
	CHANNELELEMENTMANAGER = 4
	OUTFALLELEMENTMANAGER = 5
	CATCHMENTELEMENTMANAGER = 6
	PONDELEMENTMANAGER = 7
	PONDOUTLETSTRUCTUREELEMENTMANAGER = 8
	CROSSSECTIONNODEELEMENTMANAGER = 9
	GUTTERLINKELEMENTMANAGER = 10
	PUMPELEMENTMANAGER = 11
	WETWELLELEMENTMANAGER = 12
	PRESSUREJUNCTIONELEMENTMANAGER = 13
	PRESSUREPIPEELEMENTMANAGER = 14
	JUNCTIONCHAMBERELEMENTMANAGER = 15
	BASENODEELEMENTMANAGER = 20
	BASELINKELEMENTMANAGER = 21
	BASEPOLYGONELEMENTMANAGER = 22
	SCADAELEMENTMANAGER = 23
	LATERALLINKELEMENTMANAGER = 24
	TAPNODEELEMENTMANAGER = 26
	BASEIDAHONODEELEMENTMANAGER = 50
	IDAHODEMANDNODEELEMENTMANAGER = 51
	IDAHOTANKELEMENTMANAGER = 52
	IDAHOFIREFLOWNODEMANAGER = 53
	IDAHOHYDRANTELEMENTMANAGER = 54
	IDAHOJUNCTIONELEMENTMANAGER = 55
	IDAHORESERVOIRELEMENTMANAGER = 56
	BASEDIRECTEDNODEELEMENTMANAGER = 57
	BASEVALVEELEMENTMANAGER = 58
	BASEPUMP = 59
	FCVELEMENTMANAGER = 60
	TCVELEMENTMANAGER = 61
	GPVELEMENTMANAGER = 62
	PRESSUREVALVEELEMENTMANAGER = 63
	PRVELEMENTMANAGER = 64
	PSVELEMENTMANAGER = 65
	PBVELEMENTMANAGER = 66
	PUMPSTATIONELEMENTMANAGER = 67
	STANDARDPUMPELEMENTMANAGER = 68
	IDAHOPIPEELEMENTMANAGER = 69
	IDAHOSPOTELEVATIONELEMENTMANAGER = 70
	PRESSUREISOLATIONVALVEELEMENTMANAGER = 71
	VARIABLESPEEDPUMPBATTERYELEMENTMANAGER = 72
	CUSTOMERNODEELEMENTMANAGER = 73
	GRAVITYSURFACESTRUCTUREELEMENTMANAGER = 100
	GRAVITYLINKELEMENTMANAGER = 201
	GRAVITYSTRUCTUREELEMENTMANAGER = 203
	GRAVITYNODEELEMENTMANAGER = 204
	PHYSICALLINKELEMENTMANAGER = 240
	TURBINEELEMENTMANAGER = 300
	AIRVALVEELEMENTMANAGER = 301
	HYDROPNEUMATICTANKELEMENTMANAGER = 302
	SAVSRVELEMENTMANAGER = 303
	BASEORIFICE = 304
	DISCHARGETOATMOSPHERE = 305
	RUPTUREDISK = 306
	ORIFICEBETWEENTWOPIPES = 307
	SURGETANK = 308
	CHECKVALVE = 309
	VALVEWITHLINEARAREACHANGE = 310
	BASETANK = 311
	CONVENTIONALTANK = 312
	BASEHAMMERNODE = 313
	PERIODICHEADFLOW = 321
	PRESSURESYSTEMNODE = 400
	PONDROUTEELEMENTMANAGER = 500
	GASREGULATINGVALVE = 602
	GASPIPE = 603
	GASNODE = 605
	IDAHOPUMPSTATION = 700
	LIDELEMENTMANAGER = 701
	HEADWALL = 800
	PROPERTYCONNECTIONELEMENTMANAGER = 810
	CONFLICTNODE = 3000
	COMMUNICATIONNODE = 3001
	ELECTRICALNODE = 3002
	POLNODE = 3003
	THERMALNODE = 3004
	WASTEWATERNODE = 3005
	WATERNODE = 3006
	GENERICUTILITYNODE = 3007
	COMMUNICATIONSEGMENT = 3008
	ELECTRICALSEGMENT = 3009
	POLSEGMENT = 3010
	THERMALSEGMENT = 3011
	WASTEWATERSEGMENT = 3012
	WATERSEGMENT = 3013
	GASSEGMENT = 3014
	GENERICUTILITYSEGMENT = 3015
	STORMWATERNODE = 3016
	STORMWATERSEGMENT = 3017
	REFERENCEELEMENT = 3018

class AlternativeType(Enum):
	HMIDATASETGEOMETRYALTERNATIVE = 1
	HMIDATASETTOPOLOGYALTERNATIVE = 2
	HMIACTIVETOPOLOGYALTERNATIVE = 3
	PHYSICALALTERNATIVE = 4
	BOUNDARYCONDITIONALTERNATIVE = 5
	INITIALCONDITIONALTERNATIVE = 6
	HYDROLOGICALTERNATIVE = 7
	OUTPUTALTERNATIVE = 8
	DRYLOADALTERNATIVE = 9
	RAINFALLRUNOFFALTERNATIVE = 10
	WATERQUALITYALTERNATIVE = 11
	SANITARYLOADINGALTERNATIVE = 12
	INFILTRATIONANDINFLOWALTERNATIVE = 13
	SCADAALTERNATIVE = 14
	DEMANDALTERNATIVE = 20
	INITIALSETTINGSALTERNATIVE = 21
	OPERATIONALALTERNATIVE = 22
	AGEALTERNATIVE = 23
	CONSTITUENTALTERNATIVE = 24
	TRACEALTERNATIVE = 25
	FIREFLOWALTERNATIVE = 26
	ENERGYCOSTALTERNATIVE = 28
	PRESSUREDEPENDENTDEMANDALTERNATIVE = 29
	CRITICALITYALTERNATIVE = 30
	FLUSHINGALTERNATIVE = 31
	CAPITALCOSTALTERNATIVE = 36
	HEADLOSSALTERNATIVE = 40
	DESIGNALTERNATIVE = 41
	SYSTEMFLOWSALTERNATIVE = 45
	HAMMERALTERNATIVE = 50
	PIPEBREAKALTERNATIVE = 51
	HMIUSERDEFINEDEXTENSIONSALTERNATIVE = 100
	CONFLICTALTERNATIVE = 1000
	NETWORKDATAALTERNATIVE = 1001

class SupportElementType(Enum):
	CATALOGPIPEELEMENTMANAGER = 1
	COMPOSITEOUTLETSTRUCTUREELEMENTMANAGER = 2
	PROFILEELEMENTMANAGER = 3
	POLLUTANTELEMENTMANAGER = 4
	AQUIFERSELEMENTMANAGER = 5
	CONTROLSETELEMENTMANAGER = 6
	LANDUSEELEMENTMANAGER = 8
	CONTROLSTRUCTUREELEMENTELEMENTMANAGER = 9
	STORMEVENTELEMENTMANAGER = 10
	PATTERNELEMENTMANAGER = 11
	EXTREMEFLOWFACTORELEMENTMANAGER = 12
	UNITSANITARYLOADELEMENTMANAGER = 13
	EXTREMEFLOWSETUPELEMENTMANAGER = 14
	PATTERNSETUPELEMENTMANAGER = 15
	DIMENSIONLESSUNITHYDROGRAPHELEMENTMANAGER = 16
	RTKSETELEMENTMANAGER = 17
	PROTOTYPEMANAGER = 18
	POLLUTOGRAPHELEMENTMANAGER = 19
	CATALOGGUTTER = 20
	LIDCONTROL = 21
	TIMESERIESCONTROLDATAMANAGER = 22
	IDAHOPATTERNELEMENTMANAGER = 50
	IDAHOPUMPDEFINITIONELEMENTMANAGER = 51
	IDAHOCONSTITUENTELEMENTMANAGER = 52
	ZONEELEMENTMANAGER = 53
	IDAHOCONTROLELEMENTMANAGER = 54
	IDAHOCONTROLACTIONELEMENTMANAGER = 55
	IDAHOCONTROLCONDITIONELEMENTMANAGER = 56
	IDAHOLOGICALCONTROLSETELEMENTMANAGER = 59
	PRESSUREDEPENDENTDEMANDFUNCTIONELEMENTMANAGER = 60
	ENERGYPRICINGELEMENTMANAGER = 61
	UNITDEMANDLOADELEMENTMANAGER = 62
	GPVHEADLOSSCURVEELEMENTMANAGER = 63
	CRITICALITYSTUDYGROUPELEMENTMANAGER = 64
	CRITICALITYSTUDYELEMENTMANAGER = 65
	VALVECHARACTERISTICSELEMENTMANAGER = 66
	FLUSHINGEVENTELEMENTMANAGER = 67
	AIRFLOWCURVEMANAGER = 68
	CHECKVALVEDYNAMICCHARACTERISTICSCURVEMANAGER = 69
	MINORLOSSCOEFFICIENTELEMENTMANAGER = 101
	TIMESERIESELEMENTMANAGER = 102
	INLETELEMENTMANAGER = 103
	GENERICHEADLOSSELEMENTMANAGER = 104
	STORMEVENTGROUP = 105
	CATALOGCONDUITELEMENTMANAGER = 106
	SCSCNVOLUMEELEMENTMANAGER = 107
	TR55GRAPHICALPEAKSTORAGE = 108
	FIRSTFLUSHCALCULATOR = 109
	WEIRDEPTHCOEFFICIENTMANAGER = 111
	WEIRSUBMERGENCEMANAGER = 112
	HYDROGRAPHMANAGER = 113
	TR55TABULARHYDROGRAPH = 114
	MINDRAINTIME = 115
	PEAKFLOWESTIMATEDSTORAGE = 116
	EQTWTABLEELEMENTMANAGER = 117
	QQPTEMPLATEELEMENTMANAGER = 118
	OVERLAYHYDROGRAPH = 119
	RATIONALMETHODQPEAK = 120
	PONDMAKER = 121
	STORAGECHAMBER = 124
	VORTEXVALVE = 125
	GENERICUNITHYDROGRAPH = 126
	MAINSCOREASPECT = 150
	MAINSCORE = 151
	PIPEBREAKGROUP = 152
	PIPEBREAKANALYSIS = 153
	FLUSHINGSTUDY = 175
	FLUSHINGAREA = 176
	FLUSHINGREPORTVIEW = 177
	CULVERTINLETCOEFFICIENTS = 180
	PRESSUREZONESTUDYGROUPELEMENTMANAGER = 200
	PRESSUREZONESTUDYELEMENTMANAGER = 201
	UNITCARBONEMISSIONS = 202
	POWERMETER = 203
	ENERGYAGGREGATIONSTUDY = 204
	MSXSETUP = 220
	SNOWPACK = 250
	SWMMRTKUNITHYDROGRAPHSET = 251
	PUMPSTATION = 252
	SCADADATASOURCE = 256
	SCADASIGNAL = 257
	ALERTMESSAGE = 260
	SCADACONNECTSIMULATOR = 261
	OPCPUBLISHINGRESULT = 262
	PERFORMANCESTUDY = 263
	DISTRICTMETERAREA = 265
	GASPIPETYPE = 300
	GASCUSTOMER = 301

class DomainElementShapeType(Enum):
	POINT = 0
	POLYLINE = 1
	POLYGON = 2
	DIRECTEDNODE = 3
	REFERENCENODE = 4
	LATERAL = 5

class wkbByteOrder(Enum):
	WKBXDR = 0
	WKBNDR = 1

class wkbGeometryType(Enum):
	WKBPOINT = 1
	WKBLINESTRING = 2
	WKBPOLYGON = 3
	WKBMULTIPOINT = 4
	WKBMULTILINESTRING = 5
	WKBMULTIPOLYGON = 6
	WKBGEOMETRYCOLLECTION = 7

class StandardFieldType(Enum):
	LABEL = 0
	NOTES = 1

class ConnectionType(Enum):
	JET4PT0 = 1
	SQLITE = 2

class ConnectionProperty(Enum):
	FILENAME = 1
	CONNECTIONTYPE = 2
	DATABASEPASSWORD = 3
	JETWORKSPACEUSERNAME = 4
	JETWORKSPACEPASSWORD = 5
	ENABLESCHEMAUPDATE = 6
	SHOULDUPDATECOUNTERS = 7
	ENABLECORESCHEMAUPDATE = 8
	CHECKSUCCESSFULCLOSEFLAG = 9

class SelectionSetType(Enum):
	STANDARD = 1
	PROFILE = 2

class FlowDirection(Enum):
	NOFLOW = 0
	POSITIVE = 1
	NEGATIVE = -1

class DomainFieldType(Enum):
	MODELINGELEMENTFIELD = 1
	SUPPORTELEMENTFIELD = 2
	DOMAINELEMENTFIELD = 3
	RESULTFIELD = 4
	ALTERNATIVEFIELD = 5
	SYSTEMRECORDFIELD = 6

class ReferenceCardinality(Enum):
	ONETOMANY = 0
	ONETOONE = 1

class NumericalEngineType(Enum):
	EPANET = 1
	GVFENGINE = 2

class StatisticType(Enum):
	MINIMUM = 1
	MAXIMUM = 2
	MEAN = 3
	SUM = 4
	COUNT = 5
	STANDARDDEVIATION = 6
	AREAUNDERCURVE = 7

class BulkOperationType(Enum):
	NONE = 0
	INSERT = 1
	LOAD = 2

class StoredQueryType(Enum):
	VIEW = 0
	STOREDPROCEDURE = 1

class CompactOperationTask(Enum):
	ALL = 0
	PURGEDELETEDROWS = 1
	REFRESHBOUNDINGBOX = 2
	REFRESHCACHEDMANAGERCOUNTS = 3
	REFRESHCACHEDGEOMETRYPROPERTIES = 4
	REFRESHREFERENCENODECACHESONLY = 5
	REFRESHCACHEDCOLLECTIONCOUNTS = 6
	REFRESHCACHEDSMARTLABELS = 7
	VERIFYVISUALLINKCONNECTIVITY = 8
	PURGEDELETEDGISIDS = 9
	PURGEDATAROWSFROMGISIDSMARKEDASDELETED = 10
	VERIFYSELECTIONSETSTHOROUGHLY = 11
	REFRESHCACHEDALTERNATIVELEVELS = 12
	WATERREFRESHCACHEDUNITDEMANDBASEFLOW = 13
	WATERREFRESHCACHEDMINORLOSSES = 14

class ExpressionType(Enum):
	NONE = 0
	ECEXPRESSIONS = 1

class FieldUpdateTypeEnum(Enum):
	NOCHANGE = 0
	CHANGE = 1
	ELIMINATED = 2

class ExternalIDType(Enum):
	PERSISTENTELEMENTPATH = 1

class PressureZoneValveStatusEnum(Enum):
	ALWAYSUSE = 0
	USEWHENCLOSED = 1
	DONOTUSE = 2
	USEWHENACTIVE = 3
	USEWHENCLOSEDORACTIVE = 4

class PressureZonePipeStatusEnum(Enum):
	USEWHENCLOSEDCHECKVALVE = 0
	USEWHENCLOSED = 1
	DONOTUSE = 2

class PressureZonePumpStatusEnum(Enum):
	ALWAYSUSE = 0
	DONOTUSE = 1

class PressureZoneCheckValveStatusEnum(Enum):
	ALWAYSUSE = 0
	DONOTUSE = 2

class PressureZoneOrificeBetweenPipesStatusEnum(Enum):
	ALWAYSUSE = 0
	DONOTUSE = 1

class UseInPressureZoneTraceEnum(Enum):
	PZTRACEALWAYSUSETYPE = 0
	PZTRACEUSEWHENCLOSEDTYPE = 1
	PZTRACEUSEWHENCLOSEDCHECKVALVETYPE = 2
	PZTRACEDONOTUSETYPE = 3
	PZTRACEUSEWHENACTIVETYPE = 4
	PZTRACEUSEWHENCLOSEDORACTIVETYPE = 5

class Tag(Enum):
	DEFAULT = 0

class Tag(Enum):
	DEFAULT = 0

class Tag(Enum):
	DEFAULT = 0

class Tag(Enum):
	DEFAULT = 0

class Tag(Enum):
	DEFAULT = 0

class Tag(Enum):
	DEFAULT = 0

class Tag(Enum):
	DEFAULT = 0

class Tag(Enum):
	DEFAULT = 0

class Tag(Enum):
	DEFAULT = 0

class Tag(Enum):
	DEFAULT = 0

class IDataSource:

	def __init__(self) -> None:
		"""Creating a new Instance of this class is not allowed


		Raises
		--------
			Exception: if this class is instantiated
		"""
		raise Exception("Creating a new Instance of this class is not allowed")
		pass

	def AddDomainDataSetType(self, name: str) -> IDomainDataSetType:
		"""No Description

		Args
		--------
			name (``str``) :  name

		Returns
		--------
			``IDomainDataSetType`` : 
		"""
		pass

	@overload
	def DomainDataSetType(self, id: int) -> IDomainDataSetType:
		"""No Description

		Args
		--------
			id (``int``) :  id

		Returns
		--------
			``IDomainDataSetType`` : 
		"""
		pass

	@overload
	def DomainDataSetType(self, name: str) -> IDomainDataSetType:
		"""No Description

		Args
		--------
			name (``str``) :  name

		Returns
		--------
			``IDomainDataSetType`` : 
		"""
		pass

	def GetDomainDataSetTypeID(self, name: str) -> int:
		"""No Description

		Args
		--------
			name (``str``) :  name

		Returns
		--------
			``int`` : 
		"""
		pass

	def SupportedDataSetTypes(self) -> DomainDataSetTypeCollection:
		"""No Description

		Returns
		--------
			``DomainDataSetTypeCollection`` : 
		"""
		pass

	def GetCurrentlyHiddenDomainDataSetTypes(self) -> DomainDataSetTypeCollection:
		"""No Description

		Returns
		--------
			``DomainDataSetTypeCollection`` : 
		"""
		pass

	def AddSubDomainDataSetType(self, name: str, parentDomainDataSetTypeID: int) -> IDomainDataSetType:
		"""No Description

		Args
		--------
			name (``str``) :  name
			parentDomainDataSetTypeID (``int``) :  parentDomainDataSetTypeID

		Returns
		--------
			``IDomainDataSetType`` : 
		"""
		pass

	def SubDomainDataSetTypeExists(self, parentDomainDataSetTypeID: int, subDomainDataSetTypeName: str) -> bool:
		"""No Description

		Args
		--------
			parentDomainDataSetTypeID (``int``) :  parentDomainDataSetTypeID
			subDomainDataSetTypeName (``str``) :  subDomainDataSetTypeName

		Returns
		--------
			``bool`` : 
		"""
		pass

	def SupportedSubDataSetTypes(self, parentDomainDataSetTypeID: int) -> DomainDataSetTypeCollection:
		"""No Description

		Args
		--------
			parentDomainDataSetTypeID (``int``) :  parentDomainDataSetTypeID

		Returns
		--------
			``DomainDataSetTypeCollection`` : 
		"""
		pass

	@property
	def DomainDataSetManager(self) -> IDomainDataSetManager:
		"""No Description

		Returns
		--------
			``IDataSource`` : 
		"""
		pass

	@property
	def ActiveDataSetTypeID(self) -> int:
		"""No Description

		Returns
		--------
			``IDataSource`` : 
		"""
		pass

	@ActiveDataSetTypeID.setter
	def ActiveDataSetTypeID(self, activedatasettypeid: int) -> None:
		pass

class IDataSourceConnection:

	def __init__(self) -> None:
		"""Creating a new Instance of this class is not allowed


		Raises
		--------
			Exception: if this class is instantiated
		"""
		raise Exception("Creating a new Instance of this class is not allowed")
		pass

	def Open(self) -> None:
		"""No Description

		Returns
		--------
			``None`` : 
		"""
		pass

	def Close(self) -> None:
		"""No Description

		Returns
		--------
			``None`` : 
		"""
		pass

	def IsOpen(self) -> bool:
		"""No Description

		Returns
		--------
			``bool`` : 
		"""
		pass

	def IsDataSource(self) -> bool:
		"""No Description

		Returns
		--------
			``bool`` : 
		"""
		pass

	def BeginSchemaEdit(self) -> None:
		"""No Description

		Returns
		--------
			``None`` : 
		"""
		pass

	def LoadSchema(self) -> None:
		"""No Description

		Returns
		--------
			``None`` : 
		"""
		pass

	def EndSchemaEdit(self) -> None:
		"""No Description

		Returns
		--------
			``None`` : 
		"""
		pass

	def Compact(self, context: CompactOperationContext) -> None:
		"""No Description

		Args
		--------
			context (``CompactOperationContext``) :  context

		Returns
		--------
			``None`` : 
		"""
		pass

	def UpdateCaches(self, context: CompactOperationContext) -> None:
		"""No Description

		Args
		--------
			context (``CompactOperationContext``) :  context

		Returns
		--------
			``None`` : 
		"""
		pass

	def ComputeBoundingBox(self) -> None:
		"""No Description

		Returns
		--------
			``None`` : 
		"""
		pass

	def ExecuteSchemaUpdate(self, domainDataSetTypeID: int) -> None:
		"""No Description

		Args
		--------
			domainDataSetTypeID (``int``) :  domainDataSetTypeID

		Returns
		--------
			``None`` : 
		"""
		pass

	def Flush(self) -> None:
		"""No Description

		Returns
		--------
			``None`` : 
		"""
		pass

	def ClearConnectionCaches(self) -> None:
		"""No Description

		Returns
		--------
			``None`` : 
		"""
		pass

	def Deactivate(self) -> None:
		"""No Description

		Returns
		--------
			``None`` : 
		"""
		pass

	def CreateExtendedProperty(self, propertyName: str, type: FieldDataType, defaultValue: object) -> None:
		"""No Description

		Args
		--------
			propertyName (``str``) :  propertyName
			type (``FieldDataType``) :  type
			defaultValue (``object``) :  defaultValue

		Returns
		--------
			``None`` : 
		"""
		pass

	def GetExtendedPropertyValue(self, propertyName: str) -> object:
		"""No Description

		Args
		--------
			propertyName (``str``) :  propertyName

		Returns
		--------
			``object`` : 
		"""
		pass

	def SetExtendedPropertyValue(self, propertyName: str, propertyValue: object) -> None:
		"""No Description

		Args
		--------
			propertyName (``str``) :  propertyName
			propertyValue (``object``) :  propertyValue

		Returns
		--------
			``None`` : 
		"""
		pass

	def SetConnectionProperty(self, key: ConnectionProperty, val: object) -> None:
		"""No Description

		Args
		--------
			key (``ConnectionProperty``) :  key
			val (``object``) :  val

		Returns
		--------
			``None`` : 
		"""
		pass

	def GetConnectionProperty(self, key: ConnectionProperty) -> object:
		"""No Description

		Args
		--------
			key (``ConnectionProperty``) :  key

		Returns
		--------
			``object`` : 
		"""
		pass

	@property
	def IsSchemaEditing(self) -> bool:
		"""No Description

		Returns
		--------
			``IDataSourceConnection`` : 
		"""
		pass

class ITransactionalConnection:

	def __init__(self) -> None:
		"""Creating a new Instance of this class is not allowed


		Raises
		--------
			Exception: if this class is instantiated
		"""
		raise Exception("Creating a new Instance of this class is not allowed")
		pass

	def BeginTransaction(self) -> None:
		"""No Description

		Returns
		--------
			``None`` : 
		"""
		pass

	def CommitTransaction(self) -> None:
		"""No Description

		Returns
		--------
			``None`` : 
		"""
		pass

	def RollbackTransaction(self) -> None:
		"""No Description

		Returns
		--------
			``None`` : 
		"""
		pass

class IDataSourceMessaging:

	def __init__(self) -> None:
		"""Creating a new Instance of this class is not allowed


		Raises
		--------
			Exception: if this class is instantiated
		"""
		raise Exception("Creating a new Instance of this class is not allowed")
		pass

	def Initialize(self, questionHandler: IMessageQuestionHandler, progressIndicator: IProgressIndicator) -> None:
		"""No Description

		Args
		--------
			questionHandler (``IMessageQuestionHandler``) :  questionHandler
			progressIndicator (``IProgressIndicator``) :  progressIndicator

		Returns
		--------
			``None`` : 
		"""
		pass

class IDataSourceSchemaUpdateResults:

	def __init__(self) -> None:
		"""Creating a new Instance of this class is not allowed


		Raises
		--------
			Exception: if this class is instantiated
		"""
		raise Exception("Creating a new Instance of this class is not allowed")
		pass

	def GetNewElementIdForOldElementId(self, elementTypeId: int, oldElementId: int) -> int:
		"""No Description

		Args
		--------
			elementTypeId (``int``) :  elementTypeId
			oldElementId (``int``) :  oldElementId

		Returns
		--------
			``int`` : 
		"""
		pass

	def GetUpdatedDomainFieldInformation(self, elementTypeId: int, oldFieldName: str) -> IUpdatedFieldInformation:
		"""No Description

		Args
		--------
			elementTypeId (``int``) :  elementTypeId
			oldFieldName (``str``) :  oldFieldName

		Returns
		--------
			``IUpdatedFieldInformation`` : 
		"""
		pass

	def GetUpdatedSupportFieldInformation(self, elementTypeId: int, oldFieldName: str) -> IUpdatedFieldInformation:
		"""No Description

		Args
		--------
			elementTypeId (``int``) :  elementTypeId
			oldFieldName (``str``) :  oldFieldName

		Returns
		--------
			``IUpdatedFieldInformation`` : 
		"""
		pass

	def GetOldDomainFieldNamesThatHaveChanged(self, elementTypeId: int) -> List[str]:
		"""No Description

		Args
		--------
			elementTypeId (``int``) :  elementTypeId

		Returns
		--------
			``List[str]`` : 
		"""
		pass

	def CreateSchemaStringMap(self) -> None:
		"""No Description

		Returns
		--------
			``None`` : 
		"""
		pass

	@property
	def ElementIdsWereChanged(self) -> bool:
		"""No Description

		Returns
		--------
			``IDataSourceSchemaUpdateResults`` : 
		"""
		pass

	@property
	def HasFieldChanges(self) -> bool:
		"""No Description

		Returns
		--------
			``IDataSourceSchemaUpdateResults`` : 
		"""
		pass

class IElementType:

	def __init__(self) -> None:
		"""Creating a new Instance of this class is not allowed


		Raises
		--------
			Exception: if this class is instantiated
		"""
		raise Exception("Creating a new Instance of this class is not allowed")
		pass

	@property
	def Id(self) -> int:
		"""No Description

		Returns
		--------
			``IElementType`` : 
		"""
		pass

	@property
	def Name(self) -> str:
		"""No Description

		Returns
		--------
			``IElementType`` : 
		"""
		pass

	@property
	def Label(self) -> str:
		"""No Description

		Returns
		--------
			``IElementType`` : 
		"""
		pass

	@Label.setter
	def Label(self, label: str) -> None:
		pass

	@property
	def Notes(self) -> str:
		"""No Description

		Returns
		--------
			``IElementType`` : 
		"""
		pass

	@Notes.setter
	def Notes(self, notes: str) -> None:
		pass

	@property
	def IsStandardType(self) -> bool:
		"""No Description

		Returns
		--------
			``IElementType`` : 
		"""
		pass

class IElementTypeUpdatable:

	def __init__(self) -> None:
		"""Creating a new Instance of this class is not allowed


		Raises
		--------
			Exception: if this class is instantiated
		"""
		raise Exception("Creating a new Instance of this class is not allowed")
		pass

	def SetId(self, newId: int) -> None:
		"""No Description

		Args
		--------
			newId (``int``) :  newId

		Returns
		--------
			``None`` : 
		"""
		pass

	def SetName(self, newName: str) -> None:
		"""No Description

		Args
		--------
			newName (``str``) :  newName

		Returns
		--------
			``None`` : 
		"""
		pass

class IFieldType(IElementType):

	def __init__(self) -> None:
		"""Creating a new Instance of this class is not allowed


		Raises
		--------
			Exception: if this class is instantiated
		"""
		raise Exception("Creating a new Instance of this class is not allowed")
		pass

	@overload
	def FieldDataType(self) -> FieldDataType:
		"""No Description

		Returns
		--------
			``FieldDataType`` : 
		"""
		pass

	@overload
	def FieldDataType(self, type: FieldDataType) -> None:
		"""No Description

		Args
		--------
			type (``FieldDataType``) :  type

		Returns
		--------
			``None`` : 
		"""
		pass

	@overload
	def Type(self) -> Type:
		"""No Description

		Returns
		--------
			``Type`` : 
		"""
		pass

	@overload
	def Type(self, type: Type) -> None:
		"""No Description

		Args
		--------
			type (``Type``) :  type

		Returns
		--------
			``None`` : 
		"""
		pass

	@overload
	def StorageUnit(self) -> UnitIndex:
		"""No Description

		Returns
		--------
			``UnitIndex`` : 
		"""
		pass

	@overload
	def StorageUnit(self, unit: UnitIndex) -> None:
		"""No Description

		Args
		--------
			unit (``UnitIndex``) :  unit

		Returns
		--------
			``None`` : 
		"""
		pass

	@overload
	def TextLength(self) -> int:
		"""No Description

		Returns
		--------
			``int`` : 
		"""
		pass

	@overload
	def TextLength(self, length: int) -> None:
		"""No Description

		Args
		--------
			length (``int``) :  length

		Returns
		--------
			``None`` : 
		"""
		pass

	def GetReferenceElementType(self) -> IElementType:
		"""No Description

		Returns
		--------
			``IElementType`` : 
		"""
		pass

	def SetReferenceElementType(self, elementType: IElementType) -> None:
		"""No Description

		Args
		--------
			elementType (``IElementType``) :  elementType

		Returns
		--------
			``None`` : 
		"""
		pass

	def SetIsReadOnly(self, value: bool) -> None:
		"""No Description

		Args
		--------
			value (``bool``) :  value

		Returns
		--------
			``None`` : 
		"""
		pass

	def GetReferenceCardinality(self) -> ReferenceCardinality:
		"""No Description

		Returns
		--------
			``ReferenceCardinality`` : 
		"""
		pass

	def SetReferenceCardinality(self, cardinality: ReferenceCardinality) -> None:
		"""No Description

		Args
		--------
			cardinality (``ReferenceCardinality``) :  cardinality

		Returns
		--------
			``None`` : 
		"""
		pass

	@overload
	def DefaultValue(self) -> object:
		"""No Description

		Returns
		--------
			``object`` : 
		"""
		pass

	@overload
	def DefaultValue(self, value: object) -> None:
		"""No Description

		Args
		--------
			value (``object``) :  value

		Returns
		--------
			``None`` : 
		"""
		pass

	def AddCollectionFieldType(self, name: str, type: FieldDataType) -> IFieldType:
		"""No Description

		Args
		--------
			name (``str``) :  name
			type (``FieldDataType``) :  type

		Returns
		--------
			``IFieldType`` : 
		"""
		pass

	@overload
	def CollectionFieldType(self, fieldTypeId: int) -> IFieldType:
		"""No Description

		Args
		--------
			fieldTypeId (``int``) :  fieldTypeId

		Returns
		--------
			``IFieldType`` : 
		"""
		pass

	@overload
	def CollectionFieldType(self, name: str) -> IFieldType:
		"""No Description

		Args
		--------
			name (``str``) :  name

		Returns
		--------
			``IFieldType`` : 
		"""
		pass

	def CollectionFieldTypeExists(self, name: str) -> bool:
		"""No Description

		Args
		--------
			name (``str``) :  name

		Returns
		--------
			``bool`` : 
		"""
		pass

	def CollectionFieldTypes(self) -> FieldTypeCollection:
		"""No Description

		Returns
		--------
			``FieldTypeCollection`` : 
		"""
		pass

	def EnumeratedTypeMemberExists(self, value: int) -> bool:
		"""No Description

		Args
		--------
			value (``int``) :  value

		Returns
		--------
			``bool`` : 
		"""
		pass

	def GetEnumeratedTypeMembers(self) -> List[IEnumeratedTypeMember]:
		"""No Description

		Returns
		--------
			``List[IEnumeratedTypeMember]`` : 
		"""
		pass

	def SetEnumeratedTypeMembers(self, names: array[str], values: array[int]) -> List[IEnumeratedTypeMember]:
		"""No Description

		Args
		--------
			names (``array[str]``) :  names
			values (``array[int]``) :  values

		Returns
		--------
			``List[IEnumeratedTypeMember]`` : 
		"""
		pass

	def GetNumericalRange(self, minValue: float, maxValue: float) -> None:
		"""No Description

		Args
		--------
			minValue (``float``) :  minValue
			maxValue (``float``) :  maxValue

		Returns
		--------
			``None`` : 
		"""
		pass

	def SetNumericalRange(self, minValue: float, maxValue: float) -> None:
		"""No Description

		Args
		--------
			minValue (``float``) :  minValue
			maxValue (``float``) :  maxValue

		Returns
		--------
			``None`` : 
		"""
		pass

	def GetSharedEnumeratedMembers(self) -> List[IEnumeratedTypeMember]:
		"""No Description

		Returns
		--------
			``List[IEnumeratedTypeMember]`` : 
		"""
		pass

	def GetFilteringByProduct(self) -> List[str]:
		"""No Description

		Returns
		--------
			``List[str]`` : 
		"""
		pass

	def SetFilteringByProduct(self, products: List[str]) -> None:
		"""No Description

		Args
		--------
			products (``List[str]``) :  products

		Returns
		--------
			``None`` : 
		"""
		pass

	def GetUniqueId(self) -> Guid:
		"""No Description

		Returns
		--------
			``Guid`` : 
		"""
		pass

	def SetUniqueId(self, uuid: Guid) -> None:
		"""No Description

		Args
		--------
			uuid (``Guid``) :  uuid

		Returns
		--------
			``None`` : 
		"""
		pass

	def GetAssociatedAction(self, factoryClassName: str, methodName: str, parameters: Dict[str,str]) -> None:
		"""No Description

		Args
		--------
			factoryClassName (``str``) :  factoryClassName
			methodName (``str``) :  methodName
			parameters (``Dict[str,str]``) :  parameters

		Returns
		--------
			``None`` : 
		"""
		pass

	def SetAssociatedAction(self, factoryClassName: str, methodName: str, parameters: Dict[str,str]) -> None:
		"""No Description

		Args
		--------
			factoryClassName (``str``) :  factoryClassName
			methodName (``str``) :  methodName
			parameters (``Dict[str,str]``) :  parameters

		Returns
		--------
			``None`` : 
		"""
		pass

	@property
	def Category(self) -> str:
		"""No Description

		Returns
		--------
			``IFieldType`` : 
		"""
		pass

	@Category.setter
	def Category(self, category: str) -> None:
		pass

	@property
	def IsEnumeratedMemberField(self) -> bool:
		"""No Description

		Returns
		--------
			``IFieldType`` : 
		"""
		pass

	@property
	def IsSharedEnumeratedMemberField(self) -> bool:
		"""No Description

		Returns
		--------
			``IFieldType`` : 
		"""
		pass

	@property
	def ParentEnumeratedTypeMember(self) -> IEnumeratedTypeMember:
		"""No Description

		Returns
		--------
			``IFieldType`` : 
		"""
		pass

	@property
	def IsCollectionMemberField(self) -> bool:
		"""No Description

		Returns
		--------
			``IFieldType`` : 
		"""
		pass

	@property
	def ParentCollectionFieldType(self) -> IFieldType:
		"""No Description

		Returns
		--------
			``IFieldType`` : 
		"""
		pass

	@property
	def IsReadOnly(self) -> bool:
		"""No Description

		Returns
		--------
			``IFieldType`` : 
		"""
		pass

	@property
	def IsSerializedAsBinary(self) -> bool:
		"""No Description

		Returns
		--------
			``IFieldType`` : 
		"""
		pass

	@IsSerializedAsBinary.setter
	def IsSerializedAsBinary(self, isserializedasbinary: bool) -> None:
		pass

	@property
	def OrderIndex(self) -> int:
		"""No Description

		Returns
		--------
			``IFieldType`` : 
		"""
		pass

	@OrderIndex.setter
	def OrderIndex(self, orderindex: int) -> None:
		pass

	@property
	def NumericFormatterName(self) -> str:
		"""No Description

		Returns
		--------
			``IFieldType`` : 
		"""
		pass

	@NumericFormatterName.setter
	def NumericFormatterName(self, numericformattername: str) -> None:
		pass

class IFieldTypeEx:

	def __init__(self) -> None:
		"""Creating a new Instance of this class is not allowed


		Raises
		--------
			Exception: if this class is instantiated
		"""
		raise Exception("Creating a new Instance of this class is not allowed")
		pass

	def GetDomainDataSetType(self) -> IDomainDataSetType:
		"""No Description

		Returns
		--------
			``IDomainDataSetType`` : 
		"""
		pass

	def GetSharedEnumeratedMemberFieldTypes(self) -> FieldTypeCollection:
		"""No Description

		Returns
		--------
			``FieldTypeCollection`` : 
		"""
		pass

class IFieldTypeUI:

	def __init__(self) -> None:
		"""Creating a new Instance of this class is not allowed


		Raises
		--------
			Exception: if this class is instantiated
		"""
		raise Exception("Creating a new Instance of this class is not allowed")
		pass

	def GetBlankIfReadOnly(self) -> bool:
		"""No Description

		Returns
		--------
			``bool`` : 
		"""
		pass

	def SetBlankIfReadOnly(self, val: bool) -> None:
		"""No Description

		Args
		--------
			val (``bool``) :  val

		Returns
		--------
			``None`` : 
		"""
		pass

	def GetRefreshDependentsOnChange(self) -> bool:
		"""No Description

		Returns
		--------
			``bool`` : 
		"""
		pass

	def SetRefreshDependentsOnChange(self, val: bool) -> None:
		"""No Description

		Args
		--------
			val (``bool``) :  val

		Returns
		--------
			``None`` : 
		"""
		pass

	def GetAssociatedElementTypes(self) -> List[IElementType]:
		"""No Description

		Returns
		--------
			``List[IElementType]`` : 
		"""
		pass

	def SetAssociatedElementTypes(self, elementTypes: List[IElementType]) -> None:
		"""No Description

		Args
		--------
			elementTypes (``List[IElementType]``) :  elementTypes

		Returns
		--------
			``None`` : 
		"""
		pass

	def GetFilteringByNumericalEngineType(self) -> List[str]:
		"""No Description

		Returns
		--------
			``List[str]`` : 
		"""
		pass

	def SetFilteringByNumericalEngineType(self, numericalEngineTypes: List[str]) -> None:
		"""No Description

		Args
		--------
			numericalEngineTypes (``List[str]``) :  numericalEngineTypes

		Returns
		--------
			``None`` : 
		"""
		pass

	def GetHideInPrototypes(self) -> bool:
		"""No Description

		Returns
		--------
			``bool`` : 
		"""
		pass

	def SetHideInPrototypes(self, val: bool) -> None:
		"""No Description

		Args
		--------
			val (``bool``) :  val

		Returns
		--------
			``None`` : 
		"""
		pass

class IFieldTypeInternal:

	def __init__(self) -> None:
		"""Creating a new Instance of this class is not allowed


		Raises
		--------
			Exception: if this class is instantiated
		"""
		raise Exception("Creating a new Instance of this class is not allowed")
		pass

	def GetEnumeratedTypeMember(self, enumeratedTypeMemberID: int) -> IEnumeratedTypeMember:
		"""No Description

		Args
		--------
			enumeratedTypeMemberID (``int``) :  enumeratedTypeMemberID

		Returns
		--------
			``IEnumeratedTypeMember`` : 
		"""
		pass

class IEnumeratedTypeMember(IElementType):

	def __init__(self) -> None:
		"""Creating a new Instance of this class is not allowed


		Raises
		--------
			Exception: if this class is instantiated
		"""
		raise Exception("Creating a new Instance of this class is not allowed")
		pass

	def AddFieldType(self, name: str, type: FieldDataType) -> IFieldType:
		"""No Description

		Args
		--------
			name (``str``) :  name
			type (``FieldDataType``) :  type

		Returns
		--------
			``IFieldType`` : 
		"""
		pass

	def AddCollectionFieldType(self, name: str, serializeAsBinary: bool) -> IFieldType:
		"""No Description

		Args
		--------
			name (``str``) :  name
			serializeAsBinary (``bool``) :  serializeAsBinary

		Returns
		--------
			``IFieldType`` : 
		"""
		pass

	def GetFieldTypeNamed(self, name: str) -> IFieldType:
		"""No Description

		Args
		--------
			name (``str``) :  name

		Returns
		--------
			``IFieldType`` : 
		"""
		pass

	def FieldTypes(self) -> FieldTypeCollection:
		"""No Description

		Returns
		--------
			``FieldTypeCollection`` : 
		"""
		pass

	def DeleteFieldType(self, attributeTypeID: int) -> None:
		"""No Description

		Args
		--------
			attributeTypeID (``int``) :  attributeTypeID

		Returns
		--------
			``None`` : 
		"""
		pass

	def GetFilteringByProduct(self) -> List[str]:
		"""No Description

		Returns
		--------
			``List[str]`` : 
		"""
		pass

	def SetFilteringByProduct(self, products: List[str]) -> None:
		"""No Description

		Args
		--------
			products (``List[str]``) :  products

		Returns
		--------
			``None`` : 
		"""
		pass

	def GetFilteringByNumericalEngineType(self) -> List[str]:
		"""No Description

		Returns
		--------
			``List[str]`` : 
		"""
		pass

	def SetFilteringByNumericalEngineType(self, numericalEngineTypeNames: List[str]) -> None:
		"""No Description

		Args
		--------
			numericalEngineTypeNames (``List[str]``) :  numericalEngineTypeNames

		Returns
		--------
			``None`` : 
		"""
		pass

	@property
	def ParentFieldType(self) -> IFieldType:
		"""No Description

		Returns
		--------
			``IEnumeratedTypeMember`` : 
		"""
		pass

	@property
	def EnumerationValue(self) -> int:
		"""No Description

		Returns
		--------
			``IEnumeratedTypeMember`` : 
		"""
		pass

class IEnumeratedTypeMemberUpdatable:

	def __init__(self) -> None:
		"""Creating a new Instance of this class is not allowed


		Raises
		--------
			Exception: if this class is instantiated
		"""
		raise Exception("Creating a new Instance of this class is not allowed")
		pass

	def RefactorSubEnumFieldTypeToNonEnumerated(self, name: str) -> None:
		"""No Description

		Args
		--------
			name (``str``) :  name

		Returns
		--------
			``None`` : 
		"""
		pass

class IModelingElementFieldType(IFieldType):

	def __init__(self) -> None:
		"""Creating a new Instance of this class is not allowed


		Raises
		--------
			Exception: if this class is instantiated
		"""
		raise Exception("Creating a new Instance of this class is not allowed")
		pass

	@property
	def ModelingElementType(self) -> ModelingElementType:
		"""No Description

		Returns
		--------
			``IModelingElementFieldType`` : 
		"""
		pass

	@property
	def ElementTypeID(self) -> int:
		"""No Description

		Returns
		--------
			``IModelingElementFieldType`` : 
		"""
		pass

class ISupportElementFieldType(IFieldType):

	def __init__(self) -> None:
		"""Creating a new Instance of this class is not allowed


		Raises
		--------
			Exception: if this class is instantiated
		"""
		raise Exception("Creating a new Instance of this class is not allowed")
		pass

	@property
	def SupportElementType(self) -> ISupportElementType:
		"""No Description

		Returns
		--------
			``ISupportElementFieldType`` : 
		"""
		pass

	@property
	def TableName(self) -> str:
		"""No Description

		Returns
		--------
			``ISupportElementFieldType`` : 
		"""
		pass

class ICalculationOptionsFieldType(IFieldType):

	def __init__(self) -> None:
		"""Creating a new Instance of this class is not allowed


		Raises
		--------
			Exception: if this class is instantiated
		"""
		raise Exception("Creating a new Instance of this class is not allowed")
		pass

	@property
	def NumericalEngineType(self) -> INumericalEngineType:
		"""No Description

		Returns
		--------
			``ICalculationOptionsFieldType`` : 
		"""
		pass

	@property
	def ShowInComputeCenter(self) -> bool:
		"""No Description

		Returns
		--------
			``ICalculationOptionsFieldType`` : 
		"""
		pass

	@ShowInComputeCenter.setter
	def ShowInComputeCenter(self, showincomputecenter: bool) -> None:
		pass

class IResultFieldType(IFieldType):

	def __init__(self) -> None:
		"""Creating a new Instance of this class is not allowed


		Raises
		--------
			Exception: if this class is instantiated
		"""
		raise Exception("Creating a new Instance of this class is not allowed")
		pass

	def SupportedDomainElementTypeIDs(self) -> HmIDCollection:
		"""No Description

		Returns
		--------
			``HmIDCollection`` : 
		"""
		pass

	@property
	def ResultRecordType(self) -> IResultRecordType:
		"""No Description

		Returns
		--------
			``IResultFieldType`` : 
		"""
		pass

	@property
	def IsTimeVariant(self) -> bool:
		"""No Description

		Returns
		--------
			``IResultFieldType`` : 
		"""
		pass

	@IsTimeVariant.setter
	def IsTimeVariant(self, istimevariant: bool) -> None:
		pass

	@property
	def Expression(self) -> str:
		"""No Description

		Returns
		--------
			``IResultFieldType`` : 
		"""
		pass

	@Expression.setter
	def Expression(self, expression: str) -> None:
		pass

	@property
	def ExpressionType(self) -> ExpressionType:
		"""No Description

		Returns
		--------
			``IResultFieldType`` : 
		"""
		pass

	@ExpressionType.setter
	def ExpressionType(self, expressiontype: ExpressionType) -> None:
		pass

class IDomainElementFieldType(IFieldType):

	def __init__(self) -> None:
		"""Creating a new Instance of this class is not allowed


		Raises
		--------
			Exception: if this class is instantiated
		"""
		raise Exception("Creating a new Instance of this class is not allowed")
		pass

	def TableName(self, domainElementTypeID: int) -> str:
		"""No Description

		Args
		--------
			domainElementTypeID (``int``) :  domainElementTypeID

		Returns
		--------
			``str`` : 
		"""
		pass

	def SupportedDomainElementTypeIDs(self) -> HmIDCollection:
		"""No Description

		Returns
		--------
			``HmIDCollection`` : 
		"""
		pass

	@property
	def AlternativeType(self) -> IAlternativeType:
		"""No Description

		Returns
		--------
			``IDomainElementFieldType`` : 
		"""
		pass

class ISystemRecordFieldType(IFieldType):

	def __init__(self) -> None:
		"""Creating a new Instance of this class is not allowed


		Raises
		--------
			Exception: if this class is instantiated
		"""
		raise Exception("Creating a new Instance of this class is not allowed")
		pass

	@property
	def AlternativeType(self) -> IAlternativeType:
		"""No Description

		Returns
		--------
			``ISystemRecordFieldType`` : 
		"""
		pass

class ISupportElementType(IModelingElementType):

	def __init__(self) -> None:
		"""Creating a new Instance of this class is not allowed


		Raises
		--------
			Exception: if this class is instantiated
		"""
		raise Exception("Creating a new Instance of this class is not allowed")
		pass

	@overload
	def AddFieldType(self, name: str, type: FieldDataType) -> ISupportElementFieldType:
		"""No Description

		Args
		--------
			name (``str``) :  name
			type (``FieldDataType``) :  type

		Returns
		--------
			``ISupportElementFieldType`` : 
		"""
		pass

	def AddCollectionFieldType(self, name: str, serializeAsBinary: bool) -> ISupportElementFieldType:
		"""No Description

		Args
		--------
			name (``str``) :  name
			serializeAsBinary (``bool``) :  serializeAsBinary

		Returns
		--------
			``ISupportElementFieldType`` : 
		"""
		pass

	@overload
	def AddFieldType(self, name: str, type: FieldDataType, enumFieldTypeID: int, sharedEnumMembers: array[str]) -> ISupportElementFieldType:
		"""No Description

		Args
		--------
			name (``str``) :  name
			type (``FieldDataType``) :  type
			enumFieldTypeID (``int``) :  enumFieldTypeID
			sharedEnumMembers (``array[str]``) :  sharedEnumMembers

		Returns
		--------
			``ISupportElementFieldType`` : 
		"""
		pass

	def DeleteFieldType(self, supportElementFieldTypeID: int) -> None:
		"""No Description

		Args
		--------
			supportElementFieldTypeID (``int``) :  supportElementFieldTypeID

		Returns
		--------
			``None`` : 
		"""
		pass

	@overload
	def FieldType(self, fieldTypeId: int) -> ISupportElementFieldType:
		"""No Description

		Args
		--------
			fieldTypeId (``int``) :  fieldTypeId

		Returns
		--------
			``ISupportElementFieldType`` : 
		"""
		pass

	@overload
	def FieldType(self, name: str) -> ISupportElementFieldType:
		"""No Description

		Args
		--------
			name (``str``) :  name

		Returns
		--------
			``ISupportElementFieldType`` : 
		"""
		pass

	def GetAssociatedAction(self, factoryClassName: str, methodName: str, parameters: Dict[str,str]) -> None:
		"""No Description

		Args
		--------
			factoryClassName (``str``) :  factoryClassName
			methodName (``str``) :  methodName
			parameters (``Dict[str,str]``) :  parameters

		Returns
		--------
			``None`` : 
		"""
		pass

	def SetAssociatedAction(self, factoryClassName: str, methodName: str, parameters: Dict[str,str]) -> None:
		"""No Description

		Args
		--------
			factoryClassName (``str``) :  factoryClassName
			methodName (``str``) :  methodName
			parameters (``Dict[str,str]``) :  parameters

		Returns
		--------
			``None`` : 
		"""
		pass

class ITreeElementType(IElementType):

	def __init__(self) -> None:
		"""Creating a new Instance of this class is not allowed


		Raises
		--------
			Exception: if this class is instantiated
		"""
		raise Exception("Creating a new Instance of this class is not allowed")
		pass

	def SubElementTypes(self) -> HmIDCollection:
		"""No Description

		Returns
		--------
			``HmIDCollection`` : 
		"""
		pass

	@property
	def ParentID(self) -> int:
		"""No Description

		Returns
		--------
			``ITreeElementType`` : 
		"""
		pass

class ITreeElementTypeUpdatable:

	def __init__(self) -> None:
		"""Creating a new Instance of this class is not allowed


		Raises
		--------
			Exception: if this class is instantiated
		"""
		raise Exception("Creating a new Instance of this class is not allowed")
		pass

	def SetParentID(self, newParentID: int) -> None:
		"""No Description

		Args
		--------
			newParentID (``int``) :  newParentID

		Returns
		--------
			``None`` : 
		"""
		pass

class IAlternativeType(IModelingElementType):

	def __init__(self) -> None:
		"""Creating a new Instance of this class is not allowed


		Raises
		--------
			Exception: if this class is instantiated
		"""
		raise Exception("Creating a new Instance of this class is not allowed")
		pass

	@overload
	def AddFieldType(self, name: str, type: FieldDataType) -> IDomainElementFieldType:
		"""No Description

		Args
		--------
			name (``str``) :  name
			type (``FieldDataType``) :  type

		Returns
		--------
			``IDomainElementFieldType`` : 
		"""
		pass

	def AddCollectionFieldType(self, name: str, serializeAsBinary: bool) -> IDomainElementFieldType:
		"""No Description

		Args
		--------
			name (``str``) :  name
			serializeAsBinary (``bool``) :  serializeAsBinary

		Returns
		--------
			``IDomainElementFieldType`` : 
		"""
		pass

	@overload
	def AddFieldType(self, name: str, type: FieldDataType, enumFieldTypeID: int, sharedEnumMembers: array[str]) -> IDomainElementFieldType:
		"""No Description

		Args
		--------
			name (``str``) :  name
			type (``FieldDataType``) :  type
			enumFieldTypeID (``int``) :  enumFieldTypeID
			sharedEnumMembers (``array[str]``) :  sharedEnumMembers

		Returns
		--------
			``IDomainElementFieldType`` : 
		"""
		pass

	def AddSystemRecordFieldType(self, name: str, type: FieldDataType) -> ISystemRecordFieldType:
		"""No Description

		Args
		--------
			name (``str``) :  name
			type (``FieldDataType``) :  type

		Returns
		--------
			``ISystemRecordFieldType`` : 
		"""
		pass

	def AddSystemRecordCollectionFieldType(self, name: str, serializeAsBinary: bool) -> ISystemRecordFieldType:
		"""No Description

		Args
		--------
			name (``str``) :  name
			serializeAsBinary (``bool``) :  serializeAsBinary

		Returns
		--------
			``ISystemRecordFieldType`` : 
		"""
		pass

	def SystemRecordFieldTypeExists(self, name: str) -> bool:
		"""No Description

		Args
		--------
			name (``str``) :  name

		Returns
		--------
			``bool`` : 
		"""
		pass

	def DeleteSystemRecordFieldType(self, systemRecordFieldTypeID: int) -> None:
		"""No Description

		Args
		--------
			systemRecordFieldTypeID (``int``) :  systemRecordFieldTypeID

		Returns
		--------
			``None`` : 
		"""
		pass

	@overload
	def FieldType(self, name: str) -> IDomainElementFieldType:
		"""No Description

		Args
		--------
			name (``str``) :  name

		Returns
		--------
			``IDomainElementFieldType`` : 
		"""
		pass

	@overload
	def FieldType(self, attributeTypeId: int) -> IDomainElementFieldType:
		"""No Description

		Args
		--------
			attributeTypeId (``int``) :  attributeTypeId

		Returns
		--------
			``IDomainElementFieldType`` : 
		"""
		pass

	@overload
	def SystemRecordFieldType(self, fieldTypeId: int) -> ISystemRecordFieldType:
		"""No Description

		Args
		--------
			fieldTypeId (``int``) :  fieldTypeId

		Returns
		--------
			``ISystemRecordFieldType`` : 
		"""
		pass

	@overload
	def SystemRecordFieldType(self, name: str) -> ISystemRecordFieldType:
		"""No Description

		Args
		--------
			name (``str``) :  name

		Returns
		--------
			``ISystemRecordFieldType`` : 
		"""
		pass

	def SystemRecordFieldTypes(self) -> FieldTypeCollection:
		"""No Description

		Returns
		--------
			``FieldTypeCollection`` : 
		"""
		pass

	@overload
	def FieldTypes(self, domainElementTypeID: int) -> FieldTypeCollection:
		"""No Description

		Args
		--------
			domainElementTypeID (``int``) :  domainElementTypeID

		Returns
		--------
			``FieldTypeCollection`` : 
		"""
		pass

	@overload
	def FieldTypes(self, domainElementTypeID: int, excludeInherited: bool) -> FieldTypeCollection:
		"""No Description

		Args
		--------
			domainElementTypeID (``int``) :  domainElementTypeID
			excludeInherited (``bool``) :  excludeInherited

		Returns
		--------
			``FieldTypeCollection`` : 
		"""
		pass

	def DeleteFieldType(self, domainElementFieldTypeID: int) -> None:
		"""No Description

		Args
		--------
			domainElementFieldTypeID (``int``) :  domainElementFieldTypeID

		Returns
		--------
			``None`` : 
		"""
		pass

	def SupportedDomainElementTypeIDs(self) -> HmIDCollection:
		"""No Description

		Returns
		--------
			``HmIDCollection`` : 
		"""
		pass

	def DropObsoleteObjects(self) -> None:
		"""No Description

		Returns
		--------
			``None`` : 
		"""
		pass

	@overload
	def FieldTypes(self) -> FieldTypeCollection:
		"""No Description

		Returns
		--------
			``FieldTypeCollection`` : 
		"""
		pass

class IAlternativeTypeUI:

	def __init__(self) -> None:
		"""Creating a new Instance of this class is not allowed


		Raises
		--------
			Exception: if this class is instantiated
		"""
		raise Exception("Creating a new Instance of this class is not allowed")
		pass

	def GetHideInUI(self) -> bool:
		"""No Description

		Returns
		--------
			``bool`` : 
		"""
		pass

	def SetHideInUI(self, value: bool) -> None:
		"""No Description

		Args
		--------
			value (``bool``) :  value

		Returns
		--------
			``None`` : 
		"""
		pass

class IDomainElementType(ITreeElementType, IModelingElementType):

	def __init__(self) -> None:
		"""Creating a new Instance of this class is not allowed


		Raises
		--------
			Exception: if this class is instantiated
		"""
		raise Exception("Creating a new Instance of this class is not allowed")
		pass

	def DomainElementShapeType(self) -> DomainElementShapeType:
		"""No Description

		Returns
		--------
			``DomainElementShapeType`` : 
		"""
		pass

	@overload
	def AddFieldType(self, domainElementFieldTypeID: int) -> None:
		"""No Description

		Args
		--------
			domainElementFieldTypeID (``int``) :  domainElementFieldTypeID

		Returns
		--------
			``None`` : 
		"""
		pass

	@overload
	def AddFieldType(self, name: str, dataType: FieldDataType) -> IFieldType:
		"""No Description

		Args
		--------
			name (``str``) :  name
			dataType (``FieldDataType``) :  dataType

		Returns
		--------
			``IFieldType`` : 
		"""
		pass

	@overload
	def SupportsFieldType(self, domainElementFieldTypeID: int) -> bool:
		"""No Description

		Args
		--------
			domainElementFieldTypeID (``int``) :  domainElementFieldTypeID

		Returns
		--------
			``bool`` : 
		"""
		pass

	@overload
	def SupportsFieldType(self, domainElementFieldTypeID: int, includeParentTypes: bool) -> bool:
		"""No Description

		Args
		--------
			domainElementFieldTypeID (``int``) :  domainElementFieldTypeID
			includeParentTypes (``bool``) :  includeParentTypes

		Returns
		--------
			``bool`` : 
		"""
		pass

	@overload
	def SupportsResultFieldType(self, resultFieldTypeID: int) -> bool:
		"""No Description

		Args
		--------
			resultFieldTypeID (``int``) :  resultFieldTypeID

		Returns
		--------
			``bool`` : 
		"""
		pass

	@overload
	def SupportsResultFieldType(self, resultFieldTypeID: int, includeParentTypes: bool) -> bool:
		"""No Description

		Args
		--------
			resultFieldTypeID (``int``) :  resultFieldTypeID
			includeParentTypes (``bool``) :  includeParentTypes

		Returns
		--------
			``bool`` : 
		"""
		pass

	def DropFieldType(self, domainElementFieldTypeID: int) -> None:
		"""No Description

		Args
		--------
			domainElementFieldTypeID (``int``) :  domainElementFieldTypeID

		Returns
		--------
			``None`` : 
		"""
		pass

	def RefactorFieldTypeUp(self, domainElementFieldTypeID: int, parentElementTypeID: int) -> None:
		"""No Description

		Args
		--------
			domainElementFieldTypeID (``int``) :  domainElementFieldTypeID
			parentElementTypeID (``int``) :  parentElementTypeID

		Returns
		--------
			``None`` : 
		"""
		pass

	def RefactorFieldTypeDown(self, domainElementFieldTypeID: int, parentElementTypeID: int) -> None:
		"""No Description

		Args
		--------
			domainElementFieldTypeID (``int``) :  domainElementFieldTypeID
			parentElementTypeID (``int``) :  parentElementTypeID

		Returns
		--------
			``None`` : 
		"""
		pass

	def AddResultFieldType(self, resultFieldTypeID: int) -> None:
		"""No Description

		Args
		--------
			resultFieldTypeID (``int``) :  resultFieldTypeID

		Returns
		--------
			``None`` : 
		"""
		pass

	def DropResultFieldType(self, resultFieldTypeID: int) -> None:
		"""No Description

		Args
		--------
			resultFieldTypeID (``int``) :  resultFieldTypeID

		Returns
		--------
			``None`` : 
		"""
		pass

	@overload
	def FieldTypes(self, nonAlternativeFieldTypesOnly: bool) -> FieldTypeCollection:
		"""No Description

		Args
		--------
			nonAlternativeFieldTypesOnly (``bool``) :  nonAlternativeFieldTypesOnly

		Returns
		--------
			``FieldTypeCollection`` : 
		"""
		pass

	@overload
	def FieldTypes(self, alternativeTypeID: int) -> FieldTypeCollection:
		"""No Description

		Args
		--------
			alternativeTypeID (``int``) :  alternativeTypeID

		Returns
		--------
			``FieldTypeCollection`` : 
		"""
		pass

	@overload
	def FieldTypes(self, alternativeTypeID: int, includeParentTypes: bool) -> FieldTypeCollection:
		"""No Description

		Args
		--------
			alternativeTypeID (``int``) :  alternativeTypeID
			includeParentTypes (``bool``) :  includeParentTypes

		Returns
		--------
			``FieldTypeCollection`` : 
		"""
		pass

	def SupportedAlternativeTypeIDs(self) -> HmIDCollection:
		"""No Description

		Returns
		--------
			``HmIDCollection`` : 
		"""
		pass

	def SupportsAlternativeType(self, alternativeTypeID: int, includeParentTypes: bool) -> bool:
		"""No Description

		Args
		--------
			alternativeTypeID (``int``) :  alternativeTypeID
			includeParentTypes (``bool``) :  includeParentTypes

		Returns
		--------
			``bool`` : 
		"""
		pass

	def DeleteFieldType(self, fieldTypeId: int) -> None:
		"""No Description

		Args
		--------
			fieldTypeId (``int``) :  fieldTypeId

		Returns
		--------
			``None`` : 
		"""
		pass

	def SupportedResultRecordTypeNames(self) -> StringCollection:
		"""No Description

		Returns
		--------
			``StringCollection`` : 
		"""
		pass

	@overload
	def FieldTypes(self) -> FieldTypeCollection:
		"""No Description

		Returns
		--------
			``FieldTypeCollection`` : 
		"""
		pass

class IDomainElementTypeEx:

	def __init__(self) -> None:
		"""Creating a new Instance of this class is not allowed


		Raises
		--------
			Exception: if this class is instantiated
		"""
		raise Exception("Creating a new Instance of this class is not allowed")
		pass

	def FieldTypeExists(self, name: str, includeHierarchy: bool) -> bool:
		"""No Description

		Args
		--------
			name (``str``) :  name
			includeHierarchy (``bool``) :  includeHierarchy

		Returns
		--------
			``bool`` : 
		"""
		pass

class IModelingElementTypeUI:

	def __init__(self) -> None:
		"""Creating a new Instance of this class is not allowed


		Raises
		--------
			Exception: if this class is instantiated
		"""
		raise Exception("Creating a new Instance of this class is not allowed")
		pass

	@property
	def OrderIndex(self) -> int:
		"""No Description

		Returns
		--------
			``IModelingElementTypeUI`` : 
		"""
		pass

	@OrderIndex.setter
	def OrderIndex(self, orderindex: int) -> None:
		pass

class IDomainDataSetType(IElementType):

	def __init__(self) -> None:
		"""Creating a new Instance of this class is not allowed


		Raises
		--------
			Exception: if this class is instantiated
		"""
		raise Exception("Creating a new Instance of this class is not allowed")
		pass

	def AddFieldType(self, name: str, type: FieldDataType) -> IFieldType:
		"""No Description

		Args
		--------
			name (``str``) :  name
			type (``FieldDataType``) :  type

		Returns
		--------
			``IFieldType`` : 
		"""
		pass

	def DeleteFieldType(self, name: str) -> None:
		"""No Description

		Args
		--------
			name (``str``) :  name

		Returns
		--------
			``None`` : 
		"""
		pass

	def FieldTypeExists(self, name: str) -> bool:
		"""No Description

		Args
		--------
			name (``str``) :  name

		Returns
		--------
			``bool`` : 
		"""
		pass

	def FieldType(self, name: str) -> IFieldType:
		"""No Description

		Args
		--------
			name (``str``) :  name

		Returns
		--------
			``IFieldType`` : 
		"""
		pass

	def FieldTypes(self) -> FieldTypeCollection:
		"""No Description

		Returns
		--------
			``FieldTypeCollection`` : 
		"""
		pass

	def ModelingElementType(self, type: ModelingElementType) -> IStandardModelingElementType:
		"""No Description

		Args
		--------
			type (``ModelingElementType``) :  type

		Returns
		--------
			``IStandardModelingElementType`` : 
		"""
		pass

	def AddAlternativeType(self, name: str) -> IAlternativeType:
		"""No Description

		Args
		--------
			name (``str``) :  name

		Returns
		--------
			``IAlternativeType`` : 
		"""
		pass

	def AddStandardAlternativeType(self, standardAlternativeTypeName: str) -> IAlternativeType:
		"""No Description

		Args
		--------
			standardAlternativeTypeName (``str``) :  standardAlternativeTypeName

		Returns
		--------
			``IAlternativeType`` : 
		"""
		pass

	@overload
	def AlternativeTypeExists(self, alternativeTypeName: str) -> bool:
		"""No Description

		Args
		--------
			alternativeTypeName (``str``) :  alternativeTypeName

		Returns
		--------
			``bool`` : 
		"""
		pass

	@overload
	def AlternativeTypeExists(self, alternativeTypeID: int) -> bool:
		"""No Description

		Args
		--------
			alternativeTypeID (``int``) :  alternativeTypeID

		Returns
		--------
			``bool`` : 
		"""
		pass

	@overload
	def AlternativeType(self, alternativeTypeID: int) -> IAlternativeType:
		"""No Description

		Args
		--------
			alternativeTypeID (``int``) :  alternativeTypeID

		Returns
		--------
			``IAlternativeType`` : 
		"""
		pass

	@overload
	def AlternativeType(self, alternativeTypeName: str) -> IAlternativeType:
		"""No Description

		Args
		--------
			alternativeTypeName (``str``) :  alternativeTypeName

		Returns
		--------
			``IAlternativeType`` : 
		"""
		pass

	def DeleteAlternativeType(self, alternativeTypeID: int) -> None:
		"""No Description

		Args
		--------
			alternativeTypeID (``int``) :  alternativeTypeID

		Returns
		--------
			``None`` : 
		"""
		pass

	def AlternativeTypes(self) -> AlternativeTypeCollection:
		"""No Description

		Returns
		--------
			``AlternativeTypeCollection`` : 
		"""
		pass

	@overload
	def AddDomainElementType(self, name: str, shapeType: DomainElementShapeType) -> IDomainElementType:
		"""No Description

		Args
		--------
			name (``str``) :  name
			shapeType (``DomainElementShapeType``) :  shapeType

		Returns
		--------
			``IDomainElementType`` : 
		"""
		pass

	@overload
	def AddDomainElementType(self, name: str, shapeType: DomainElementShapeType, standardAlternativeTypesToSupport: StringCollection) -> IDomainElementType:
		"""No Description

		Args
		--------
			name (``str``) :  name
			shapeType (``DomainElementShapeType``) :  shapeType
			standardAlternativeTypesToSupport (``StringCollection``) :  standardAlternativeTypesToSupport

		Returns
		--------
			``IDomainElementType`` : 
		"""
		pass

	@overload
	def AddDomainElementType(self, name: str, shapeType: DomainElementShapeType, parentDomainElementTypeID: int) -> IDomainElementType:
		"""No Description

		Args
		--------
			name (``str``) :  name
			shapeType (``DomainElementShapeType``) :  shapeType
			parentDomainElementTypeID (``int``) :  parentDomainElementTypeID

		Returns
		--------
			``IDomainElementType`` : 
		"""
		pass

	@overload
	def DomainElementType(self, domainElementTypeID: int) -> IDomainElementType:
		"""No Description

		Args
		--------
			domainElementTypeID (``int``) :  domainElementTypeID

		Returns
		--------
			``IDomainElementType`` : 
		"""
		pass

	@overload
	def DomainElementType(self, domainElementTypeName: str) -> IDomainElementType:
		"""No Description

		Args
		--------
			domainElementTypeName (``str``) :  domainElementTypeName

		Returns
		--------
			``IDomainElementType`` : 
		"""
		pass

	@overload
	def DomainElementTypeExists(self, domainElementTypeID: int) -> bool:
		"""No Description

		Args
		--------
			domainElementTypeID (``int``) :  domainElementTypeID

		Returns
		--------
			``bool`` : 
		"""
		pass

	@overload
	def DomainElementTypeExists(self, domainElementTypeName: str) -> bool:
		"""No Description

		Args
		--------
			domainElementTypeName (``str``) :  domainElementTypeName

		Returns
		--------
			``bool`` : 
		"""
		pass

	def DeleteDomainElementType(self, domainElementTypeID: int) -> None:
		"""No Description

		Args
		--------
			domainElementTypeID (``int``) :  domainElementTypeID

		Returns
		--------
			``None`` : 
		"""
		pass

	@overload
	def DomainElementTypes(self) -> DomainElementTypeCollection:
		"""No Description

		Returns
		--------
			``DomainElementTypeCollection`` : 
		"""
		pass

	@overload
	def DomainElementTypes(self, includeBaseTypes: bool) -> DomainElementTypeCollection:
		"""No Description

		Args
		--------
			includeBaseTypes (``bool``) :  includeBaseTypes

		Returns
		--------
			``DomainElementTypeCollection`` : 
		"""
		pass

	def AddSupportElementType(self, name: str) -> ISupportElementType:
		"""No Description

		Args
		--------
			name (``str``) :  name

		Returns
		--------
			``ISupportElementType`` : 
		"""
		pass

	@overload
	def SupportElementType(self, supportElementTypeID: int) -> ISupportElementType:
		"""No Description

		Args
		--------
			supportElementTypeID (``int``) :  supportElementTypeID

		Returns
		--------
			``ISupportElementType`` : 
		"""
		pass

	@overload
	def SupportElementType(self, supportElementTypeName: str) -> ISupportElementType:
		"""No Description

		Args
		--------
			supportElementTypeName (``str``) :  supportElementTypeName

		Returns
		--------
			``ISupportElementType`` : 
		"""
		pass

	@overload
	def SupportElementTypeExists(self, supportElementTypeName: str) -> bool:
		"""No Description

		Args
		--------
			supportElementTypeName (``str``) :  supportElementTypeName

		Returns
		--------
			``bool`` : 
		"""
		pass

	@overload
	def SupportElementTypeExists(self, supportElementTypeID: int) -> bool:
		"""No Description

		Args
		--------
			supportElementTypeID (``int``) :  supportElementTypeID

		Returns
		--------
			``bool`` : 
		"""
		pass

	def DeleteSupportElementType(self, supportElementTypeID: int) -> None:
		"""No Description

		Args
		--------
			supportElementTypeID (``int``) :  supportElementTypeID

		Returns
		--------
			``None`` : 
		"""
		pass

	def SupportElementTypes(self) -> SupportElementTypeCollection:
		"""No Description

		Returns
		--------
			``SupportElementTypeCollection`` : 
		"""
		pass

	def AddNumericalEngineType(self, name: str) -> INumericalEngineType:
		"""No Description

		Args
		--------
			name (``str``) :  name

		Returns
		--------
			``INumericalEngineType`` : 
		"""
		pass

	@overload
	def NumericalEngineType(self, name: str) -> INumericalEngineType:
		"""No Description

		Args
		--------
			name (``str``) :  name

		Returns
		--------
			``INumericalEngineType`` : 
		"""
		pass

	@overload
	def NumericalEngineType(self, numericalEngineTypeID: int) -> INumericalEngineType:
		"""No Description

		Args
		--------
			numericalEngineTypeID (``int``) :  numericalEngineTypeID

		Returns
		--------
			``INumericalEngineType`` : 
		"""
		pass

	@overload
	def NumericalEngineTypeExists(self, name: str) -> bool:
		"""No Description

		Args
		--------
			name (``str``) :  name

		Returns
		--------
			``bool`` : 
		"""
		pass

	@overload
	def NumericalEngineTypeExists(self, numericalEngineTypeID: int) -> bool:
		"""No Description

		Args
		--------
			numericalEngineTypeID (``int``) :  numericalEngineTypeID

		Returns
		--------
			``bool`` : 
		"""
		pass

	def DeleteNumericalEngineType(self, name: str) -> None:
		"""No Description

		Args
		--------
			name (``str``) :  name

		Returns
		--------
			``None`` : 
		"""
		pass

	def NumericalEngineTypes(self) -> NumericalEngineTypeCollection:
		"""No Description

		Returns
		--------
			``NumericalEngineTypeCollection`` : 
		"""
		pass

	def GetMainNumericalEngineTypeName(self) -> str:
		"""No Description

		Returns
		--------
			``str`` : 
		"""
		pass

	def SetMainNumericalEngineTypeName(self, name: str) -> None:
		"""No Description

		Args
		--------
			name (``str``) :  name

		Returns
		--------
			``None`` : 
		"""
		pass

	def AddResultRecordType(self, name: str) -> IResultRecordType:
		"""No Description

		Args
		--------
			name (``str``) :  name

		Returns
		--------
			``IResultRecordType`` : 
		"""
		pass

	def ResultRecordType(self, resultRecordTypeName: str) -> IResultRecordType:
		"""No Description

		Args
		--------
			resultRecordTypeName (``str``) :  resultRecordTypeName

		Returns
		--------
			``IResultRecordType`` : 
		"""
		pass

	def ResultRecordTypeExists(self, resultRecordTypeName: str) -> bool:
		"""No Description

		Args
		--------
			resultRecordTypeName (``str``) :  resultRecordTypeName

		Returns
		--------
			``bool`` : 
		"""
		pass

	def ResultRecordTypes(self) -> ResultRecordTypeCollection:
		"""No Description

		Returns
		--------
			``ResultRecordTypeCollection`` : 
		"""
		pass

	def AddNumericFormatter(self, name: str) -> NumericFormatter:
		"""No Description

		Args
		--------
			name (``str``) :  name

		Returns
		--------
			``NumericFormatter`` : 
		"""
		pass

	def NumericFormatter(self, name: str) -> NumericFormatter:
		"""No Description

		Args
		--------
			name (``str``) :  name

		Returns
		--------
			``NumericFormatter`` : 
		"""
		pass

	def NumericFormatters(self) -> StringCollection:
		"""No Description

		Returns
		--------
			``StringCollection`` : 
		"""
		pass

	def AddStoredQuery(self, name: str, type: StoredQueryType, queryText: str) -> IStoredQuery:
		"""No Description

		Args
		--------
			name (``str``) :  name
			type (``StoredQueryType``) :  type
			queryText (``str``) :  queryText

		Returns
		--------
			``IStoredQuery`` : 
		"""
		pass

	def DeleteStoredQuery(self, name: str) -> None:
		"""No Description

		Args
		--------
			name (``str``) :  name

		Returns
		--------
			``None`` : 
		"""
		pass

	def StoredQuery(self, name: str) -> IStoredQuery:
		"""No Description

		Args
		--------
			name (``str``) :  name

		Returns
		--------
			``IStoredQuery`` : 
		"""
		pass

	def StoredQueryExists(self, name: str) -> bool:
		"""No Description

		Args
		--------
			name (``str``) :  name

		Returns
		--------
			``bool`` : 
		"""
		pass

	def StoredQueryNames(self) -> StringCollection:
		"""No Description

		Returns
		--------
			``StringCollection`` : 
		"""
		pass

	def GetSchemaVersion(self) -> Version:
		"""No Description

		Returns
		--------
			``Version`` : 
		"""
		pass

	def SetSchemaVersion(self, version: Version) -> None:
		"""No Description

		Args
		--------
			version (``Version``) :  version

		Returns
		--------
			``None`` : 
		"""
		pass

	def AddProduct(self, name: str) -> None:
		"""No Description

		Args
		--------
			name (``str``) :  name

		Returns
		--------
			``None`` : 
		"""
		pass

	def ProductExists(self, productName: str) -> bool:
		"""No Description

		Args
		--------
			productName (``str``) :  productName

		Returns
		--------
			``bool`` : 
		"""
		pass

	def Products(self) -> List[str]:
		"""No Description

		Returns
		--------
			``List[str]`` : 
		"""
		pass

	def DeleteProduct(self, productName: str) -> None:
		"""No Description

		Args
		--------
			productName (``str``) :  productName

		Returns
		--------
			``None`` : 
		"""
		pass

	def GetMainTextResourceAssemblyName(self) -> str:
		"""No Description

		Returns
		--------
			``str`` : 
		"""
		pass

	def SetMainTextResourceAssemblyName(self, assemblyName: str) -> None:
		"""No Description

		Args
		--------
			assemblyName (``str``) :  assemblyName

		Returns
		--------
			``None`` : 
		"""
		pass

	@property
	def DataSource(self) -> IDataSource:
		"""No Description

		Returns
		--------
			``IDomainDataSetType`` : 
		"""
		pass

	@property
	def ParentDomainDataSetTypeID(self) -> int:
		"""No Description

		Returns
		--------
			``IDomainDataSetType`` : 
		"""
		pass

	@property
	def CanBeHidden(self) -> bool:
		"""No Description

		Returns
		--------
			``IDomainDataSetType`` : 
		"""
		pass

	@CanBeHidden.setter
	def CanBeHidden(self, canbehidden: bool) -> None:
		pass

	@property
	def ActiveProductFilter(self) -> str:
		"""No Description

		Returns
		--------
			``IDomainDataSetType`` : 
		"""
		pass

	@ActiveProductFilter.setter
	def ActiveProductFilter(self, activeproductfilter: str) -> None:
		pass

class IDomainDataSetTypeRefactoring:

	def __init__(self) -> None:
		"""Creating a new Instance of this class is not allowed


		Raises
		--------
			Exception: if this class is instantiated
		"""
		raise Exception("Creating a new Instance of this class is not allowed")
		pass

	def MoveFieldTypesBetweenAlternativeTypes(self, fieldTypes: FieldTypeCollection, targetAlternativeType: IAlternativeType) -> None:
		"""No Description

		Args
		--------
			fieldTypes (``FieldTypeCollection``) :  fieldTypes
			targetAlternativeType (``IAlternativeType``) :  targetAlternativeType

		Returns
		--------
			``None`` : 
		"""
		pass

class IStoredQuery(IElementType):

	def __init__(self) -> None:
		"""Creating a new Instance of this class is not allowed


		Raises
		--------
			Exception: if this class is instantiated
		"""
		raise Exception("Creating a new Instance of this class is not allowed")
		pass

	@property
	def QueryText(self) -> str:
		"""No Description

		Returns
		--------
			``IStoredQuery`` : 
		"""
		pass

	@QueryText.setter
	def QueryText(self, querytext: str) -> None:
		pass

	@property
	def QueryType(self) -> StoredQueryType:
		"""No Description

		Returns
		--------
			``IStoredQuery`` : 
		"""
		pass

class IModelingElementType(IElementType):

	def __init__(self) -> None:
		"""Creating a new Instance of this class is not allowed


		Raises
		--------
			Exception: if this class is instantiated
		"""
		raise Exception("Creating a new Instance of this class is not allowed")
		pass

	@overload
	def FieldType(self, fieldTypeId: int) -> IFieldType:
		"""No Description

		Args
		--------
			fieldTypeId (``int``) :  fieldTypeId

		Returns
		--------
			``IFieldType`` : 
		"""
		pass

	@overload
	def FieldType(self, name: str) -> IFieldType:
		"""No Description

		Args
		--------
			name (``str``) :  name

		Returns
		--------
			``IFieldType`` : 
		"""
		pass

	def FieldTypeExists(self, name: str) -> bool:
		"""No Description

		Args
		--------
			name (``str``) :  name

		Returns
		--------
			``bool`` : 
		"""
		pass

	def FieldTypes(self) -> FieldTypeCollection:
		"""No Description

		Returns
		--------
			``FieldTypeCollection`` : 
		"""
		pass

	@property
	def DomainDataSetType(self) -> IDomainDataSetType:
		"""No Description

		Returns
		--------
			``IModelingElementType`` : 
		"""
		pass

class IStandardModelingElementType(IModelingElementType):

	def __init__(self) -> None:
		"""Creating a new Instance of this class is not allowed


		Raises
		--------
			Exception: if this class is instantiated
		"""
		raise Exception("Creating a new Instance of this class is not allowed")
		pass

	def AddModelingElementFieldType(self, fieldName: str, type: FieldDataType) -> IFieldType:
		"""No Description

		Args
		--------
			fieldName (``str``) :  fieldName
			type (``FieldDataType``) :  type

		Returns
		--------
			``IFieldType`` : 
		"""
		pass

	def AddModelingElementCollectionFieldType(self, fieldName: str, serializeAsBinary: bool) -> IFieldType:
		"""No Description

		Args
		--------
			fieldName (``str``) :  fieldName
			serializeAsBinary (``bool``) :  serializeAsBinary

		Returns
		--------
			``IFieldType`` : 
		"""
		pass

	def ModelingElementFieldTypeExists(self, fieldName: str, elementTypeID: int) -> bool:
		"""No Description

		Args
		--------
			fieldName (``str``) :  fieldName
			elementTypeID (``int``) :  elementTypeID

		Returns
		--------
			``bool`` : 
		"""
		pass

	def ModelingElementFieldType(self, fieldName: str) -> IFieldType:
		"""No Description

		Args
		--------
			fieldName (``str``) :  fieldName

		Returns
		--------
			``IFieldType`` : 
		"""
		pass

	def ModelingElementFieldTypes(self, elementTypeID: int) -> FieldTypeCollection:
		"""No Description

		Args
		--------
			elementTypeID (``int``) :  elementTypeID

		Returns
		--------
			``FieldTypeCollection`` : 
		"""
		pass

	@property
	def ModelingElementType(self) -> ModelingElementType:
		"""No Description

		Returns
		--------
			``IStandardModelingElementType`` : 
		"""
		pass

class INumericalEngineType(IModelingElementType):

	def __init__(self) -> None:
		"""Creating a new Instance of this class is not allowed


		Raises
		--------
			Exception: if this class is instantiated
		"""
		raise Exception("Creating a new Instance of this class is not allowed")
		pass

	def AddResultFieldType(self, resultFieldTypeID: int) -> None:
		"""No Description

		Args
		--------
			resultFieldTypeID (``int``) :  resultFieldTypeID

		Returns
		--------
			``None`` : 
		"""
		pass

	def SupportedResultRecordTypeNames(self) -> StringCollection:
		"""No Description

		Returns
		--------
			``StringCollection`` : 
		"""
		pass

	def ResultFieldType(self, name: str, resultRecordTypeName: str) -> IResultFieldType:
		"""No Description

		Args
		--------
			name (``str``) :  name
			resultRecordTypeName (``str``) :  resultRecordTypeName

		Returns
		--------
			``IResultFieldType`` : 
		"""
		pass

	def ResultFieldTypes(self, resultRecordTypeName: str, domainElementTypeID: int) -> FieldTypeCollection:
		"""No Description

		Args
		--------
			resultRecordTypeName (``str``) :  resultRecordTypeName
			domainElementTypeID (``int``) :  domainElementTypeID

		Returns
		--------
			``FieldTypeCollection`` : 
		"""
		pass

	def ScenarioResultFieldTypes(self) -> FieldTypeCollection:
		"""No Description

		Returns
		--------
			``FieldTypeCollection`` : 
		"""
		pass

	def DropResultFieldType(self, resultFieldTypeID: int) -> None:
		"""No Description

		Args
		--------
			resultFieldTypeID (``int``) :  resultFieldTypeID

		Returns
		--------
			``None`` : 
		"""
		pass

	@overload
	def AddCalculationOptionsFieldType(self, name: str, type: FieldDataType) -> IFieldType:
		"""No Description

		Args
		--------
			name (``str``) :  name
			type (``FieldDataType``) :  type

		Returns
		--------
			``IFieldType`` : 
		"""
		pass

	@overload
	def AddCalculationOptionsFieldType(self, name: str, type: FieldDataType, enumFieldTypeID: int, sharedEnumMembers: array[str]) -> IFieldType:
		"""No Description

		Args
		--------
			name (``str``) :  name
			type (``FieldDataType``) :  type
			enumFieldTypeID (``int``) :  enumFieldTypeID
			sharedEnumMembers (``array[str]``) :  sharedEnumMembers

		Returns
		--------
			``IFieldType`` : 
		"""
		pass

	def AddCalculationOptionsCollectionFieldType(self, name: str, serializeAsBinary: bool) -> IFieldType:
		"""No Description

		Args
		--------
			name (``str``) :  name
			serializeAsBinary (``bool``) :  serializeAsBinary

		Returns
		--------
			``IFieldType`` : 
		"""
		pass

	def CalculationOptionsFieldType(self, name: str) -> IFieldType:
		"""No Description

		Args
		--------
			name (``str``) :  name

		Returns
		--------
			``IFieldType`` : 
		"""
		pass

	def CalculationOptionsFieldTypeExists(self, name: str) -> bool:
		"""No Description

		Args
		--------
			name (``str``) :  name

		Returns
		--------
			``bool`` : 
		"""
		pass

	def CalculationOptionsFieldTypes(self) -> FieldTypeCollection:
		"""No Description

		Returns
		--------
			``FieldTypeCollection`` : 
		"""
		pass

	def DeleteCalculationOptionsFieldType(self, name: str) -> None:
		"""No Description

		Args
		--------
			name (``str``) :  name

		Returns
		--------
			``None`` : 
		"""
		pass

	def SupportsFieldType(self, fieldTypeID: int) -> bool:
		"""No Description

		Args
		--------
			fieldTypeID (``int``) :  fieldTypeID

		Returns
		--------
			``bool`` : 
		"""
		pass

	def MakeComposite(self, subNumericalEngineTypes: List[INumericalEngineType], defaultActiveNumericalEngineType: INumericalEngineType) -> None:
		"""No Description

		Args
		--------
			subNumericalEngineTypes (``List[INumericalEngineType]``) :  subNumericalEngineTypes
			defaultActiveNumericalEngineType (``INumericalEngineType``) :  defaultActiveNumericalEngineType

		Returns
		--------
			``None`` : 
		"""
		pass

	def GetFilteringByProduct(self) -> List[str]:
		"""No Description

		Returns
		--------
			``List[str]`` : 
		"""
		pass

	def SetFilteringByProduct(self, products: List[str]) -> None:
		"""No Description

		Args
		--------
			products (``List[str]``) :  products

		Returns
		--------
			``None`` : 
		"""
		pass

	@property
	def CalculationAssemblyName(self) -> str:
		"""No Description

		Returns
		--------
			``INumericalEngineType`` : 
		"""
		pass

	@CalculationAssemblyName.setter
	def CalculationAssemblyName(self, calculationassemblyname: str) -> None:
		pass

	@property
	def CalculationClassName(self) -> str:
		"""No Description

		Returns
		--------
			``INumericalEngineType`` : 
		"""
		pass

	@CalculationClassName.setter
	def CalculationClassName(self, calculationclassname: str) -> None:
		pass

	@property
	def IsComposite(self) -> bool:
		"""No Description

		Returns
		--------
			``INumericalEngineType`` : 
		"""
		pass

class IResultRecordType(IElementType):

	def __init__(self) -> None:
		"""Creating a new Instance of this class is not allowed


		Raises
		--------
			Exception: if this class is instantiated
		"""
		raise Exception("Creating a new Instance of this class is not allowed")
		pass

	def AddFieldType(self, name: str, type: FieldDataType) -> IFieldType:
		"""No Description

		Args
		--------
			name (``str``) :  name
			type (``FieldDataType``) :  type

		Returns
		--------
			``IFieldType`` : 
		"""
		pass

	def DeleteFieldType(self, resultFieldTypeId: int) -> None:
		"""No Description

		Args
		--------
			resultFieldTypeId (``int``) :  resultFieldTypeId

		Returns
		--------
			``None`` : 
		"""
		pass

	@overload
	def FieldType(self, name: str) -> IFieldType:
		"""No Description

		Args
		--------
			name (``str``) :  name

		Returns
		--------
			``IFieldType`` : 
		"""
		pass

	@overload
	def FieldType(self, fieldTypeId: int) -> IFieldType:
		"""No Description

		Args
		--------
			fieldTypeId (``int``) :  fieldTypeId

		Returns
		--------
			``IFieldType`` : 
		"""
		pass

	def FieldTypeExists(self, name: str) -> bool:
		"""No Description

		Args
		--------
			name (``str``) :  name

		Returns
		--------
			``bool`` : 
		"""
		pass

	def FieldTypes(self) -> FieldTypeCollection:
		"""No Description

		Returns
		--------
			``FieldTypeCollection`` : 
		"""
		pass

	@property
	def DomainDataSetType(self) -> IDomainDataSetType:
		"""No Description

		Returns
		--------
			``IResultRecordType`` : 
		"""
		pass

class IDomainDatabaseContext:

	def __init__(self) -> None:
		"""Creating a new Instance of this class is not allowed


		Raises
		--------
			Exception: if this class is instantiated
		"""
		raise Exception("Creating a new Instance of this class is not allowed")
		pass

	def CurrentDomainDataSet(self) -> IDomainDataSet:
		"""No Description

		Returns
		--------
			``IDomainDataSet`` : 
		"""
		pass

	def CurrentDbConnection(self) -> DbConnection:
		"""No Description

		Returns
		--------
			``DbConnection`` : 
		"""
		pass

	def Flush(self) -> None:
		"""No Description

		Returns
		--------
			``None`` : 
		"""
		pass

class IDomainDataSetManager:

	def __init__(self) -> None:
		"""Creating a new Instance of this class is not allowed


		Raises
		--------
			Exception: if this class is instantiated
		"""
		raise Exception("Creating a new Instance of this class is not allowed")
		pass

	def AddDomainDataSet(self, domainDataSetTypeID: int, name: str) -> IDomainDataSet:
		"""No Description

		Args
		--------
			domainDataSetTypeID (``int``) :  domainDataSetTypeID
			name (``str``) :  name

		Returns
		--------
			``IDomainDataSet`` : 
		"""
		pass

	def DomainDataSet(self, domainDataSetID: int) -> IDomainDataSet:
		"""No Description

		Args
		--------
			domainDataSetID (``int``) :  domainDataSetID

		Returns
		--------
			``IDomainDataSet`` : 
		"""
		pass

	def DomainDataSets(self, domainDataSetTypeID: int) -> DomainDataSetCollection:
		"""No Description

		Args
		--------
			domainDataSetTypeID (``int``) :  domainDataSetTypeID

		Returns
		--------
			``DomainDataSetCollection`` : 
		"""
		pass

	def DeleteDomainDataSet(self, domainDataSetID: int) -> None:
		"""No Description

		Args
		--------
			domainDataSetID (``int``) :  domainDataSetID

		Returns
		--------
			``None`` : 
		"""
		pass

	@property
	def DataSource(self) -> IDataSource:
		"""No Description

		Returns
		--------
			``IDomainDataSetManager`` : 
		"""
		pass

class IDomainDataSet:

	def __init__(self) -> None:
		"""Creating a new Instance of this class is not allowed


		Raises
		--------
			Exception: if this class is instantiated
		"""
		raise Exception("Creating a new Instance of this class is not allowed")
		pass

	def Exists(self, modelingElementID: int) -> bool:
		"""No Description

		Args
		--------
			modelingElementID (``int``) :  modelingElementID

		Returns
		--------
			``bool`` : 
		"""
		pass

	def AlternativeTypeID(self, alternativeID: int) -> int:
		"""No Description

		Args
		--------
			alternativeID (``int``) :  alternativeID

		Returns
		--------
			``int`` : 
		"""
		pass

	def DomainElementTypeID(self, domainElementID: int) -> int:
		"""No Description

		Args
		--------
			domainElementID (``int``) :  domainElementID

		Returns
		--------
			``int`` : 
		"""
		pass

	def NumericalEngineTypeName(self, calculationOptionsID: int) -> str:
		"""No Description

		Args
		--------
			calculationOptionsID (``int``) :  calculationOptionsID

		Returns
		--------
			``str`` : 
		"""
		pass

	def DomainElementTypeIDs(self) -> IHmIDToObjectDictionary:
		"""No Description

		Returns
		--------
			``IHmIDToObjectDictionary`` : 
		"""
		pass

	def SupportElementTypeID(self, supportElementID: int) -> int:
		"""No Description

		Args
		--------
			supportElementID (``int``) :  supportElementID

		Returns
		--------
			``int`` : 
		"""
		pass

	def ModelingElementType(self, elementID: int) -> ModelingElementType:
		"""No Description

		Args
		--------
			elementID (``int``) :  elementID

		Returns
		--------
			``ModelingElementType`` : 
		"""
		pass

	def NumericalEngine(self, numericalEngineType: str) -> INumericalEngine:
		"""No Description

		Args
		--------
			numericalEngineType (``str``) :  numericalEngineType

		Returns
		--------
			``INumericalEngine`` : 
		"""
		pass

	def DomainDataSetType(self) -> IDomainDataSetType:
		"""No Description

		Returns
		--------
			``IDomainDataSetType`` : 
		"""
		pass

	def GeometryAlternativeManager(self) -> IAlternativeManager:
		"""No Description

		Returns
		--------
			``IAlternativeManager`` : 
		"""
		pass

	@overload
	def AlternativeManager(self, alternativeTypeID: int) -> IAlternativeManager:
		"""No Description

		Args
		--------
			alternativeTypeID (``int``) :  alternativeTypeID

		Returns
		--------
			``IAlternativeManager`` : 
		"""
		pass

	@overload
	def AlternativeManager(self, alternativeTypeName: str) -> IAlternativeManager:
		"""No Description

		Args
		--------
			alternativeTypeName (``str``) :  alternativeTypeName

		Returns
		--------
			``IAlternativeManager`` : 
		"""
		pass

	@overload
	def DomainElementManager(self, domainElementTypeID: int) -> IDomainElementManager:
		"""No Description

		Args
		--------
			domainElementTypeID (``int``) :  domainElementTypeID

		Returns
		--------
			``IDomainElementManager`` : 
		"""
		pass

	@overload
	def DomainElementManager(self, domainElementTypeName: str) -> IDomainElementManager:
		"""No Description

		Args
		--------
			domainElementTypeName (``str``) :  domainElementTypeName

		Returns
		--------
			``IDomainElementManager`` : 
		"""
		pass

	@overload
	def SupportElementManager(self, supportElementTypeID: int) -> ISupportElementManager:
		"""No Description

		Args
		--------
			supportElementTypeID (``int``) :  supportElementTypeID

		Returns
		--------
			``ISupportElementManager`` : 
		"""
		pass

	@overload
	def SupportElementManager(self, supportElementTypeName: str) -> ISupportElementManager:
		"""No Description

		Args
		--------
			supportElementTypeName (``str``) :  supportElementTypeName

		Returns
		--------
			``ISupportElementManager`` : 
		"""
		pass

	def PrototypeSupportElementManager(self, supportElementTypeID: int) -> IPrototypeManager:
		"""No Description

		Args
		--------
			supportElementTypeID (``int``) :  supportElementTypeID

		Returns
		--------
			``IPrototypeManager`` : 
		"""
		pass

	def PrototypeDomainElementManager(self, domainElementTypeID: int) -> IPrototypeDomainElementManager:
		"""No Description

		Args
		--------
			domainElementTypeID (``int``) :  domainElementTypeID

		Returns
		--------
			``IPrototypeDomainElementManager`` : 
		"""
		pass

	@property
	def Id(self) -> int:
		"""No Description

		Returns
		--------
			``IDomainDataSet`` : 
		"""
		pass

	@property
	def Guid(self) -> Guid:
		"""No Description

		Returns
		--------
			``IDomainDataSet`` : 
		"""
		pass

	@property
	def Label(self) -> str:
		"""No Description

		Returns
		--------
			``IDomainDataSet`` : 
		"""
		pass

	@Label.setter
	def Label(self, label: str) -> None:
		pass

	@property
	def Notes(self) -> str:
		"""No Description

		Returns
		--------
			``IDomainDataSet`` : 
		"""
		pass

	@Notes.setter
	def Notes(self, notes: str) -> None:
		pass

	@property
	def DomainDataSetManager(self) -> IDomainDataSetManager:
		"""No Description

		Returns
		--------
			``IDomainDataSet`` : 
		"""
		pass

	@property
	def FieldManager(self) -> IFieldManager:
		"""No Description

		Returns
		--------
			``IDomainDataSet`` : 
		"""
		pass

	@property
	def ScenarioManager(self) -> IScenarioManager:
		"""No Description

		Returns
		--------
			``IDomainDataSet`` : 
		"""
		pass

	@property
	def SelectionSetManager(self) -> ISelectionSetManager:
		"""No Description

		Returns
		--------
			``IDomainDataSet`` : 
		"""
		pass

	@property
	def ProfileManager(self) -> ISelectionSetManager:
		"""No Description

		Returns
		--------
			``IDomainDataSet`` : 
		"""
		pass

	@property
	def EmbeddedStickyObjectManager(self) -> IEmbeddedStickyObjectManager:
		"""No Description

		Returns
		--------
			``IDomainDataSet`` : 
		"""
		pass

	@property
	def ChangeTrackingEnabled(self) -> bool:
		"""No Description

		Returns
		--------
			``IDomainDataSet`` : 
		"""
		pass

	@ChangeTrackingEnabled.setter
	def ChangeTrackingEnabled(self, changetrackingenabled: bool) -> None:
		pass

	@property
	def ChangeTrackingLocked(self) -> bool:
		"""No Description

		Returns
		--------
			``IDomainDataSet`` : 
		"""
		pass

	@ChangeTrackingLocked.setter
	def ChangeTrackingLocked(self, changetrackinglocked: bool) -> None:
		pass

	@property
	def ChangeTrackingPassword(self) -> str:
		"""No Description

		Returns
		--------
			``IDomainDataSet`` : 
		"""
		pass

	@ChangeTrackingPassword.setter
	def ChangeTrackingPassword(self, changetrackingpassword: str) -> None:
		pass

	@property
	def ChangeTrackingPromptOnOpen(self) -> bool:
		"""No Description

		Returns
		--------
			``IDomainDataSet`` : 
		"""
		pass

	@ChangeTrackingPromptOnOpen.setter
	def ChangeTrackingPromptOnOpen(self, changetrackingpromptonopen: bool) -> None:
		pass

class IDomainDataSetUnitPresentation(IDomainDataSet):

	def __init__(self) -> None:
		"""Creating a new Instance of this class is not allowed


		Raises
		--------
			Exception: if this class is instantiated
		"""
		raise Exception("Creating a new Instance of this class is not allowed")
		pass

	@property
	def PresentationUnitManager(self) -> IPresentationUnitsManager:
		"""No Description

		Returns
		--------
			``IDomainDataSetUnitPresentation`` : 
		"""
		pass

class IDomainDataSet2DModeling:

	def __init__(self) -> None:
		"""Creating a new Instance of this class is not allowed


		Raises
		--------
			Exception: if this class is instantiated
		"""
		raise Exception("Creating a new Instance of this class is not allowed")
		pass

	@property
	def HasRainfallInflowToNode(self) -> bool:
		"""No Description

		Returns
		--------
			``IDomainDataSet2DModeling`` : 
		"""
		pass

	@HasRainfallInflowToNode.setter
	def HasRainfallInflowToNode(self, hasrainfallinflowtonode: bool) -> None:
		pass

	@property
	def MeshSize(self) -> float:
		"""No Description

		Returns
		--------
			``IDomainDataSet2DModeling`` : 
		"""
		pass

	@MeshSize.setter
	def MeshSize(self, meshsize: float) -> None:
		pass

class IDomainDataSetUpdatable:

	def __init__(self) -> None:
		"""Creating a new Instance of this class is not allowed


		Raises
		--------
			Exception: if this class is instantiated
		"""
		raise Exception("Creating a new Instance of this class is not allowed")
		pass

	def LocalizeExistingLabels(self) -> None:
		"""No Description

		Returns
		--------
			``None`` : 
		"""
		pass

	def SetGuid(self, guid: Guid) -> None:
		"""No Description

		Args
		--------
			guid (``Guid``) :  guid

		Returns
		--------
			``None`` : 
		"""
		pass

class IDomainDataSetSearch:

	def __init__(self) -> None:
		"""Creating a new Instance of this class is not allowed


		Raises
		--------
			Exception: if this class is instantiated
		"""
		raise Exception("Creating a new Instance of this class is not allowed")
		pass

	def GetElementIDsForLabel(self, label: str, type: ModelingElementType, elementTypeID: int, useWildcards: bool) -> HmIDCollection:
		"""No Description

		Args
		--------
			label (``str``) :  label
			type (``ModelingElementType``) :  type
			elementTypeID (``int``) :  elementTypeID
			useWildcards (``bool``) :  useWildcards

		Returns
		--------
			``HmIDCollection`` : 
		"""
		pass

	def GetDomainElementIDsForLabel(self, label: str, useWildcards: bool) -> HmIDCollection:
		"""No Description

		Args
		--------
			label (``str``) :  label
			useWildcards (``bool``) :  useWildcards

		Returns
		--------
			``HmIDCollection`` : 
		"""
		pass

	def GetLabel(self, elementID: int) -> str:
		"""No Description

		Args
		--------
			elementID (``int``) :  elementID

		Returns
		--------
			``str`` : 
		"""
		pass

	def GetLabelForDomainElementID(self, domainElementID: int) -> str:
		"""No Description

		Args
		--------
			domainElementID (``int``) :  domainElementID

		Returns
		--------
			``str`` : 
		"""
		pass

	@overload
	def GetIncomingLinkIDsToNode(self, domainElementID: int) -> HmIDCollection:
		"""No Description

		Args
		--------
			domainElementID (``int``) :  domainElementID

		Returns
		--------
			``HmIDCollection`` : 
		"""
		pass

	@overload
	def GetIncomingLinkIDsToNode(self, domainElementID: int, alternativeID: int, domainElementTypeIDs: HmIDCollection) -> HmIDCollection:
		"""No Description

		Args
		--------
			domainElementID (``int``) :  domainElementID
			alternativeID (``int``) :  alternativeID
			domainElementTypeIDs (``HmIDCollection``) :  domainElementTypeIDs

		Returns
		--------
			``HmIDCollection`` : 
		"""
		pass

	@overload
	def GetOutcomingLinkIDsFromNode(self, domainElementID: int) -> HmIDCollection:
		"""No Description

		Args
		--------
			domainElementID (``int``) :  domainElementID

		Returns
		--------
			``HmIDCollection`` : 
		"""
		pass

	@overload
	def GetOutcomingLinkIDsFromNode(self, domainElementID: int, alternativeID: int, domainElementTypeIDs: HmIDCollection) -> HmIDCollection:
		"""No Description

		Args
		--------
			domainElementID (``int``) :  domainElementID
			alternativeID (``int``) :  alternativeID
			domainElementTypeIDs (``HmIDCollection``) :  domainElementTypeIDs

		Returns
		--------
			``HmIDCollection`` : 
		"""
		pass

	def GetElementIDsWithDuplicateLabels(self, modelingElementType: ModelingElementType, elementTypeIDs: array[int], ignoreBlanks: bool) -> HmIDCollection:
		"""No Description

		Args
		--------
			modelingElementType (``ModelingElementType``) :  modelingElementType
			elementTypeIDs (``array[int]``) :  elementTypeIDs
			ignoreBlanks (``bool``) :  ignoreBlanks

		Returns
		--------
			``HmIDCollection`` : 
		"""
		pass

class IDomainDataSetLog:

	def __init__(self) -> None:
		"""Creating a new Instance of this class is not allowed


		Raises
		--------
			Exception: if this class is instantiated
		"""
		raise Exception("Creating a new Instance of this class is not allowed")
		pass

	@property
	def ChangeLogDatabase(self) -> IChangeLogDatabase:
		"""No Description

		Returns
		--------
			``IDomainDataSetLog`` : 
		"""
		pass

	@property
	def ChangeLog(self) -> IChangeLog:
		"""No Description

		Returns
		--------
			``IDomainDataSetLog`` : 
		"""
		pass

class IChangeLogDatabase:

	def __init__(self) -> None:
		"""Creating a new Instance of this class is not allowed


		Raises
		--------
			Exception: if this class is instantiated
		"""
		raise Exception("Creating a new Instance of this class is not allowed")
		pass

	def ArchiveChangeLog(self, process: IProcessInProgressEx, filteredIDs: HmIDCollection) -> None:
		"""No Description

		Args
		--------
			process (``IProcessInProgressEx``) :  process
			filteredIDs (``HmIDCollection``) :  filteredIDs

		Returns
		--------
			``None`` : 
		"""
		pass

	def GetChangeLogWriter(self) -> IChangeLogWriter:
		"""No Description

		Returns
		--------
			``IChangeLogWriter`` : 
		"""
		pass

	def GetEditsDataTable(self) -> DataTable:
		"""No Description

		Returns
		--------
			``DataTable`` : 
		"""
		pass

	def IsInitialized(self) -> bool:
		"""No Description

		Returns
		--------
			``bool`` : 
		"""
		pass

	@overload
	def ReadChangeLog(self, dataSet: DataSet, domainDataSet: IDomainDataSet, process: IProcessInProgress, dataRowLoader: IChangeLogDataRowLoader) -> DataSet:
		"""No Description

		Args
		--------
			dataSet (``DataSet``) :  dataSet
			domainDataSet (``IDomainDataSet``) :  domainDataSet
			process (``IProcessInProgress``) :  process
			dataRowLoader (``IChangeLogDataRowLoader``) :  dataRowLoader

		Returns
		--------
			``DataSet`` : 
		"""
		pass

	@overload
	def ReadChangeLog(self, domainDataSet: IDomainDataSet, process: IProcessInProgress, dataRowLoader: IChangeLogDataRowLoader) -> DataSet:
		"""No Description

		Args
		--------
			domainDataSet (``IDomainDataSet``) :  domainDataSet
			process (``IProcessInProgress``) :  process
			dataRowLoader (``IChangeLogDataRowLoader``) :  dataRowLoader

		Returns
		--------
			``DataSet`` : 
		"""
		pass

	@property
	def LogConnection(self) -> SQLiteConnection:
		"""No Description

		Returns
		--------
			``IChangeLogDatabase`` : 
		"""
		pass

class IChangeLogDataRowLoader:

	def __init__(self) -> None:
		"""Creating a new Instance of this class is not allowed


		Raises
		--------
			Exception: if this class is instantiated
		"""
		raise Exception("Creating a new Instance of this class is not allowed")
		pass

	def LoadDataRow(self, values: List[object]) -> None:
		"""No Description

		Args
		--------
			values (``List[object]``) :  values

		Returns
		--------
			``None`` : 
		"""
		pass

class IChangeLogWriter:

	def __init__(self) -> None:
		"""Creating a new Instance of this class is not allowed


		Raises
		--------
			Exception: if this class is instantiated
		"""
		raise Exception("Creating a new Instance of this class is not allowed")
		pass

	def CommitSQLTransaction(self) -> None:
		"""No Description

		Returns
		--------
			``None`` : 
		"""
		pass

	def WriteAlternativeAdd(self, alternativeID: int, parentAlternativeID: int, alternativeTypeID: int, isChildAlternative: bool) -> None:
		"""No Description

		Args
		--------
			alternativeID (``int``) :  alternativeID
			parentAlternativeID (``int``) :  parentAlternativeID
			alternativeTypeID (``int``) :  alternativeTypeID
			isChildAlternative (``bool``) :  isChildAlternative

		Returns
		--------
			``None`` : 
		"""
		pass

	def WriteAlternativeDelete(self, alternativeID: int, alternativeTypeID: int) -> None:
		"""No Description

		Args
		--------
			alternativeID (``int``) :  alternativeID
			alternativeTypeID (``int``) :  alternativeTypeID

		Returns
		--------
			``None`` : 
		"""
		pass

	def WriteAlternativeDuplicated(self, alternativeID: int, alternativeTypeID: int, parentID: int) -> None:
		"""No Description

		Args
		--------
			alternativeID (``int``) :  alternativeID
			alternativeTypeID (``int``) :  alternativeTypeID
			parentID (``int``) :  parentID

		Returns
		--------
			``None`` : 
		"""
		pass

	def WriteAlternativeMerge(self, alternativeID: int, alternativeTypeID: int, parentID: int) -> None:
		"""No Description

		Args
		--------
			alternativeID (``int``) :  alternativeID
			alternativeTypeID (``int``) :  alternativeTypeID
			parentID (``int``) :  parentID

		Returns
		--------
			``None`` : 
		"""
		pass

	def WriteAlternativeModified(self, alternativeID: int, alternativeTypeID: int, fieldTypeLabel: str, newValue: object) -> None:
		"""No Description

		Args
		--------
			alternativeID (``int``) :  alternativeID
			alternativeTypeID (``int``) :  alternativeTypeID
			fieldTypeLabel (``str``) :  fieldTypeLabel
			newValue (``object``) :  newValue

		Returns
		--------
			``None`` : 
		"""
		pass

	def WriteAlternativeParentIDChanged(self, alternativeID: int, alternativeTypeID: int, parentID: int) -> None:
		"""No Description

		Args
		--------
			alternativeID (``int``) :  alternativeID
			alternativeTypeID (``int``) :  alternativeTypeID
			parentID (``int``) :  parentID

		Returns
		--------
			``None`` : 
		"""
		pass

	def WriteAlternativeRestore(self, alternativeID: int, alternativeTypeID: int) -> None:
		"""No Description

		Args
		--------
			alternativeID (``int``) :  alternativeID
			alternativeTypeID (``int``) :  alternativeTypeID

		Returns
		--------
			``None`` : 
		"""
		pass

	def WriteChangeLogArchived(self) -> None:
		"""No Description

		Returns
		--------
			``None`` : 
		"""
		pass

	def WriteCollectionFieldGlobalEdit(self, alternativeID: int, alternativeTypeID: int, domainElementCollectionFieldType: IDomainElementFieldType, fieldType: str, elementIDs: List[int], value: object) -> None:
		"""No Description

		Args
		--------
			alternativeID (``int``) :  alternativeID
			alternativeTypeID (``int``) :  alternativeTypeID
			domainElementCollectionFieldType (``IDomainElementFieldType``) :  domainElementCollectionFieldType
			fieldType (``str``) :  fieldType
			elementIDs (``List[int]``) :  elementIDs
			value (``object``) :  value

		Returns
		--------
			``None`` : 
		"""
		pass

	def WriteCollectionValueAdd(self, domainElementID: int, alternativeID: int, alternativeTypeID: int, domainElementCollectionFieldType: IDomainElementFieldType) -> None:
		"""No Description

		Args
		--------
			domainElementID (``int``) :  domainElementID
			alternativeID (``int``) :  alternativeID
			alternativeTypeID (``int``) :  alternativeTypeID
			domainElementCollectionFieldType (``IDomainElementFieldType``) :  domainElementCollectionFieldType

		Returns
		--------
			``None`` : 
		"""
		pass

	def WriteCollectionValueDelete(self, domainElementID: int, alternativeID: int, alternativeTypeID: int, domainElementCollectionFieldType: IDomainElementFieldType) -> None:
		"""No Description

		Args
		--------
			domainElementID (``int``) :  domainElementID
			alternativeID (``int``) :  alternativeID
			alternativeTypeID (``int``) :  alternativeTypeID
			domainElementCollectionFieldType (``IDomainElementFieldType``) :  domainElementCollectionFieldType

		Returns
		--------
			``None`` : 
		"""
		pass

	def WriteDomainElementAdd(self, elementID: int, domainElementTypeID: int) -> None:
		"""No Description

		Args
		--------
			elementID (``int``) :  elementID
			domainElementTypeID (``int``) :  domainElementTypeID

		Returns
		--------
			``None`` : 
		"""
		pass

	def WriteDomainElementDelete(self, elementID: int, domainElementTypeID: int) -> None:
		"""No Description

		Args
		--------
			elementID (``int``) :  elementID
			domainElementTypeID (``int``) :  domainElementTypeID

		Returns
		--------
			``None`` : 
		"""
		pass

	def WriteDomainElementEdit(self, domainElementID: int, alternativeID: int, alternativeTypeID: int, fieldTypeLabel: str, newValue: object) -> None:
		"""No Description

		Args
		--------
			domainElementID (``int``) :  domainElementID
			alternativeID (``int``) :  alternativeID
			alternativeTypeID (``int``) :  alternativeTypeID
			fieldTypeLabel (``str``) :  fieldTypeLabel
			newValue (``object``) :  newValue

		Returns
		--------
			``None`` : 
		"""
		pass

	def WriteDomainElementEditCollection(self, domainElementID: int, alternativeID: int, alternativeTypeID: int, domainElementCollectionFieldType: IDomainElementFieldType, fieldTypeLabel: str) -> None:
		"""No Description

		Args
		--------
			domainElementID (``int``) :  domainElementID
			alternativeID (``int``) :  alternativeID
			alternativeTypeID (``int``) :  alternativeTypeID
			domainElementCollectionFieldType (``IDomainElementFieldType``) :  domainElementCollectionFieldType
			fieldTypeLabel (``str``) :  fieldTypeLabel

		Returns
		--------
			``None`` : 
		"""
		pass

	def WriteDomainElementEditNoAlternative(self, domainElementID: int, domainElementTypeID: Nullable[int], fieldTypeLabel: str, newValue: object) -> None:
		"""No Description

		Args
		--------
			domainElementID (``int``) :  domainElementID
			domainElementTypeID (``Nullable``) :  domainElementTypeID
			fieldTypeLabel (``str``) :  fieldTypeLabel
			newValue (``object``) :  newValue

		Returns
		--------
			``None`` : 
		"""
		pass

	def WriteDomainElementGlobalEdit(self, alternativeID: int, alternativeTypeID: int, fieldType: str, elementIDNewValueDictionary: Dict[int,int][int,object]) -> None:
		"""No Description

		Args
		--------
			alternativeID (``int``) :  alternativeID
			alternativeTypeID (``int``) :  alternativeTypeID
			fieldType (``str``) :  fieldType
			elementIDNewValueDictionary (``Dict[int,int]``) :  elementIDNewValueDictionary

		Returns
		--------
			``None`` : 
		"""
		pass

	@overload
	def WriteDomainElementRestore(self, elementIDs: HmIDCollection, domainElementTypeID: int) -> None:
		"""No Description

		Args
		--------
			elementIDs (``HmIDCollection``) :  elementIDs
			domainElementTypeID (``int``) :  domainElementTypeID

		Returns
		--------
			``None`` : 
		"""
		pass

	@overload
	def WriteDomainElementRestore(self, elementID: int, domainElementTypeID: int) -> None:
		"""No Description

		Args
		--------
			elementID (``int``) :  elementID
			domainElementTypeID (``int``) :  domainElementTypeID

		Returns
		--------
			``None`` : 
		"""
		pass

	def WriteDomainElementTypeLogContext(self, elementID: int, elementTypeID: int) -> None:
		"""No Description

		Args
		--------
			elementID (``int``) :  elementID
			elementTypeID (``int``) :  elementTypeID

		Returns
		--------
			``None`` : 
		"""
		pass

	def WriteTrackingTurnedOff(self) -> None:
		"""No Description

		Returns
		--------
			``None`` : 
		"""
		pass

	@property
	def CurrentContext(self) -> Nullable[Guid]:
		"""No Description

		Returns
		--------
			``IChangeLogWriter`` : 
		"""
		pass

	@CurrentContext.setter
	def CurrentContext(self, currentcontext: Nullable[Guid]) -> None:
		pass

	@property
	def Enabled(self) -> bool:
		"""No Description

		Returns
		--------
			``IChangeLogWriter`` : 
		"""
		pass

	@Enabled.setter
	def Enabled(self, enabled: bool) -> None:
		pass

class IChangeLog:

	def __init__(self) -> None:
		"""Creating a new Instance of this class is not allowed


		Raises
		--------
			Exception: if this class is instantiated
		"""
		raise Exception("Creating a new Instance of this class is not allowed")
		pass

	def Archive(self, process: IProcessInProgressEx, changeLogDataTable: DataTable, orderedIDs: array[int], filteredIDs: HmIDCollection, filename: str, whereClause: str, append: bool = False) -> None:
		"""No Description

		Args
		--------
			process (``IProcessInProgressEx``) :  process
			changeLogDataTable (``DataTable``) :  changeLogDataTable
			orderedIDs (``array[int]``) :  orderedIDs
			filteredIDs (``HmIDCollection``) :  filteredIDs
			filename (``str``) :  filename
			whereClause (``str``) :  whereClause
			append (``bool``) :  append

		Returns
		--------
			``None`` : 
		"""
		pass

	def CommitSQLTransaction(self) -> None:
		"""No Description

		Returns
		--------
			``None`` : 
		"""
		pass

	def WriteAlternativeAdd(self, alternativeID: int, parentAlternativeID: int, alternativeTypeID: int, isChildAlternative: bool) -> None:
		"""No Description

		Args
		--------
			alternativeID (``int``) :  alternativeID
			parentAlternativeID (``int``) :  parentAlternativeID
			alternativeTypeID (``int``) :  alternativeTypeID
			isChildAlternative (``bool``) :  isChildAlternative

		Returns
		--------
			``None`` : 
		"""
		pass

	def WriteAlternativeDelete(self, alternativeID: int, alternativeTypeID: int) -> None:
		"""No Description

		Args
		--------
			alternativeID (``int``) :  alternativeID
			alternativeTypeID (``int``) :  alternativeTypeID

		Returns
		--------
			``None`` : 
		"""
		pass

	def WriteAlternativeDuplicated(self, alternativeID: int, alternativeTypeID: int, parentID: int) -> None:
		"""No Description

		Args
		--------
			alternativeID (``int``) :  alternativeID
			alternativeTypeID (``int``) :  alternativeTypeID
			parentID (``int``) :  parentID

		Returns
		--------
			``None`` : 
		"""
		pass

	def WriteAlternativeMerge(self, alternativeID: int, alternativeTypeID: int, parentID: int) -> None:
		"""No Description

		Args
		--------
			alternativeID (``int``) :  alternativeID
			alternativeTypeID (``int``) :  alternativeTypeID
			parentID (``int``) :  parentID

		Returns
		--------
			``None`` : 
		"""
		pass

	def WriteAlternativeModified(self, alternativeID: int, alternativeTypeID: int, fieldTypeLabel: str, newValue: object) -> None:
		"""No Description

		Args
		--------
			alternativeID (``int``) :  alternativeID
			alternativeTypeID (``int``) :  alternativeTypeID
			fieldTypeLabel (``str``) :  fieldTypeLabel
			newValue (``object``) :  newValue

		Returns
		--------
			``None`` : 
		"""
		pass

	def WriteAlternativeParentChanged(self, alternativeID: int, alternativeTypeID: int, parentID: int) -> None:
		"""No Description

		Args
		--------
			alternativeID (``int``) :  alternativeID
			alternativeTypeID (``int``) :  alternativeTypeID
			parentID (``int``) :  parentID

		Returns
		--------
			``None`` : 
		"""
		pass

	def WriteAlternativeRestore(self, alternativeID: int, alternativeTypeID: int) -> None:
		"""No Description

		Args
		--------
			alternativeID (``int``) :  alternativeID
			alternativeTypeID (``int``) :  alternativeTypeID

		Returns
		--------
			``None`` : 
		"""
		pass

	def WriteChangeLogArchived(self) -> None:
		"""No Description

		Returns
		--------
			``None`` : 
		"""
		pass

	def WriteCollectionFieldGlobalEdit(self, alternativeID: int, alternativeTypeID: int, domainElementCollectionFieldType: IDomainElementFieldType, fieldType: str, elementIDs: List[int], value: object) -> None:
		"""No Description

		Args
		--------
			alternativeID (``int``) :  alternativeID
			alternativeTypeID (``int``) :  alternativeTypeID
			domainElementCollectionFieldType (``IDomainElementFieldType``) :  domainElementCollectionFieldType
			fieldType (``str``) :  fieldType
			elementIDs (``List[int]``) :  elementIDs
			value (``object``) :  value

		Returns
		--------
			``None`` : 
		"""
		pass

	def WriteCollectionValueAdd(self, domainElementID: int, alternativeID: int, alternativeTypeID: int, domainElementCollectionFieldType: IDomainElementFieldType) -> None:
		"""No Description

		Args
		--------
			domainElementID (``int``) :  domainElementID
			alternativeID (``int``) :  alternativeID
			alternativeTypeID (``int``) :  alternativeTypeID
			domainElementCollectionFieldType (``IDomainElementFieldType``) :  domainElementCollectionFieldType

		Returns
		--------
			``None`` : 
		"""
		pass

	def WriteCollectionValueDelete(self, domainElementID: int, alternativeID: int, alternativeTypeID: int, domainElementCollectionFieldType: IDomainElementFieldType) -> None:
		"""No Description

		Args
		--------
			domainElementID (``int``) :  domainElementID
			alternativeID (``int``) :  alternativeID
			alternativeTypeID (``int``) :  alternativeTypeID
			domainElementCollectionFieldType (``IDomainElementFieldType``) :  domainElementCollectionFieldType

		Returns
		--------
			``None`` : 
		"""
		pass

	def WriteDomainElementAdd(self, elementID: int, domainElementTypeID: int) -> None:
		"""No Description

		Args
		--------
			elementID (``int``) :  elementID
			domainElementTypeID (``int``) :  domainElementTypeID

		Returns
		--------
			``None`` : 
		"""
		pass

	def WriteDomainElementDelete(self, elementID: int, domainElementTypeID: int) -> None:
		"""No Description

		Args
		--------
			elementID (``int``) :  elementID
			domainElementTypeID (``int``) :  domainElementTypeID

		Returns
		--------
			``None`` : 
		"""
		pass

	def WriteDomainElementEdit(self, domainElementID: int, alternativeID: int, alternativeTypeID: int, fieldTypeLabel: str, newValue: object) -> None:
		"""No Description

		Args
		--------
			domainElementID (``int``) :  domainElementID
			alternativeID (``int``) :  alternativeID
			alternativeTypeID (``int``) :  alternativeTypeID
			fieldTypeLabel (``str``) :  fieldTypeLabel
			newValue (``object``) :  newValue

		Returns
		--------
			``None`` : 
		"""
		pass

	def WriteDomainElementEditCollection(self, domainElementID: int, alternativeID: int, alternativeTypeID: int, domainElementCollectionFieldType: IDomainElementFieldType, fieldTypeLabel: str) -> None:
		"""No Description

		Args
		--------
			domainElementID (``int``) :  domainElementID
			alternativeID (``int``) :  alternativeID
			alternativeTypeID (``int``) :  alternativeTypeID
			domainElementCollectionFieldType (``IDomainElementFieldType``) :  domainElementCollectionFieldType
			fieldTypeLabel (``str``) :  fieldTypeLabel

		Returns
		--------
			``None`` : 
		"""
		pass

	def WriteDomainElementEditNoAlternative(self, domainElementID: int, domainElementTypeID: Nullable[int], fieldTypeLabel: str, newValue: object) -> None:
		"""No Description

		Args
		--------
			domainElementID (``int``) :  domainElementID
			domainElementTypeID (``Nullable``) :  domainElementTypeID
			fieldTypeLabel (``str``) :  fieldTypeLabel
			newValue (``object``) :  newValue

		Returns
		--------
			``None`` : 
		"""
		pass

	def WriteDomainElementGlobalEdit(self, alternativeID: int, alternativeTypeID: int, fieldType: str, elementIDNewValueDictionary: Dict[int,int][int,object]) -> None:
		"""No Description

		Args
		--------
			alternativeID (``int``) :  alternativeID
			alternativeTypeID (``int``) :  alternativeTypeID
			fieldType (``str``) :  fieldType
			elementIDNewValueDictionary (``Dict[int,int]``) :  elementIDNewValueDictionary

		Returns
		--------
			``None`` : 
		"""
		pass

	@overload
	def WriteDomainElementRestore(self, elementIDs: HmIDCollection, domainElementTypeID: int) -> None:
		"""No Description

		Args
		--------
			elementIDs (``HmIDCollection``) :  elementIDs
			domainElementTypeID (``int``) :  domainElementTypeID

		Returns
		--------
			``None`` : 
		"""
		pass

	@overload
	def WriteDomainElementRestore(self, elementID: int, domainElementTypeID: int) -> None:
		"""No Description

		Args
		--------
			elementID (``int``) :  elementID
			domainElementTypeID (``int``) :  domainElementTypeID

		Returns
		--------
			``None`` : 
		"""
		pass

	def WriteDomainElementTypeLogContext(self, elementID: int, elementTypeID: int) -> None:
		"""No Description

		Args
		--------
			elementID (``int``) :  elementID
			elementTypeID (``int``) :  elementTypeID

		Returns
		--------
			``None`` : 
		"""
		pass

	def WriteTrackingTurnedOff(self) -> None:
		"""No Description

		Returns
		--------
			``None`` : 
		"""
		pass

	@property
	def Database(self) -> IChangeLogDatabase:
		"""No Description

		Returns
		--------
			``IChangeLog`` : 
		"""
		pass

	@property
	def Enabled(self) -> bool:
		"""No Description

		Returns
		--------
			``IChangeLog`` : 
		"""
		pass

	@Enabled.setter
	def Enabled(self, enabled: bool) -> None:
		pass

class IDomainDataSetGISIDLinks:

	def __init__(self) -> None:
		"""Creating a new Instance of this class is not allowed


		Raises
		--------
			Exception: if this class is instantiated
		"""
		raise Exception("Creating a new Instance of this class is not allowed")
		pass

	def DeleteAllGISIDs(self, elementID: int) -> None:
		"""No Description

		Args
		--------
			elementID (``int``) :  elementID

		Returns
		--------
			``None`` : 
		"""
		pass

	def GetGISIDsForElementID(self, elementID: int) -> StringCollection:
		"""No Description

		Args
		--------
			elementID (``int``) :  elementID

		Returns
		--------
			``StringCollection`` : 
		"""
		pass

	def GetElementIDsForGISID(self, gisID: str) -> HmIDCollection:
		"""No Description

		Args
		--------
			gisID (``str``) :  gisID

		Returns
		--------
			``HmIDCollection`` : 
		"""
		pass

	def GetDeletedElementIDsForGISID(self, gisID: str) -> HmIDCollection:
		"""No Description

		Args
		--------
			gisID (``str``) :  gisID

		Returns
		--------
			``HmIDCollection`` : 
		"""
		pass

	def GetDeletedGISIDToElementIDsMap(self) -> Dict:
		"""No Description

		Returns
		--------
			``Dict`` : 
		"""
		pass

	def GetUniqueGISIDsSet(self) -> Dict:
		"""No Description

		Returns
		--------
			``Dict`` : 
		"""
		pass

	def AddGISIDToElementID(self, elementID: int, gisID: str) -> None:
		"""No Description

		Args
		--------
			elementID (``int``) :  elementID
			gisID (``str``) :  gisID

		Returns
		--------
			``None`` : 
		"""
		pass

	def AddGISIDsToElementID(self, elementID: int, gisIDs: StringCollection) -> None:
		"""No Description

		Args
		--------
			elementID (``int``) :  elementID
			gisIDs (``StringCollection``) :  gisIDs

		Returns
		--------
			``None`` : 
		"""
		pass

	def IsElementAvailable(self, elementID: int) -> bool:
		"""No Description

		Args
		--------
			elementID (``int``) :  elementID

		Returns
		--------
			``bool`` : 
		"""
		pass

	def GetAllElementIdsWithGISIDs(self) -> Iterator[GenericPair]:
		"""No Description

		Returns
		--------
			``Iterator[GenericPair]`` : 
		"""
		pass

	def SetGISIDs(self, elementID: int, value: str) -> None:
		"""No Description

		Args
		--------
			elementID (``int``) :  elementID
			value (``str``) :  value

		Returns
		--------
			``None`` : 
		"""
		pass

class IDomainDataSetExternalIDLinks:

	def __init__(self) -> None:
		"""Creating a new Instance of this class is not allowed


		Raises
		--------
			Exception: if this class is instantiated
		"""
		raise Exception("Creating a new Instance of this class is not allowed")
		pass

	def GetElementIDForExternalID(self, idType: ExternalIDType, externalID: str) -> Union[int, None]:
		"""No Description

		Args
		--------
			idType (``ExternalIDType``) :  idType
			externalID (``str``) :  externalID

		Returns
		--------
			``Nullable`` : 
		"""
		pass

	def GetExternalIDs(self, elementID: int, idType: ExternalIDType) -> List[str]:
		"""No Description

		Args
		--------
			elementID (``int``) :  elementID
			idType (``ExternalIDType``) :  idType

		Returns
		--------
			``List[str]`` : 
		"""
		pass

	def AddExternalIDs(self, elementID: int, idType: ExternalIDType, externalIDs: List[str]) -> None:
		"""No Description

		Args
		--------
			elementID (``int``) :  elementID
			idType (``ExternalIDType``) :  idType
			externalIDs (``List[str]``) :  externalIDs

		Returns
		--------
			``None`` : 
		"""
		pass

	def ClearExternalIDs(self, elementID: int, idType: ExternalIDType) -> None:
		"""No Description

		Args
		--------
			elementID (``int``) :  elementID
			idType (``ExternalIDType``) :  idType

		Returns
		--------
			``None`` : 
		"""
		pass

	def ClearAllExternalIDs(self, idType: ExternalIDType) -> None:
		"""No Description

		Args
		--------
			idType (``ExternalIDType``) :  idType

		Returns
		--------
			``None`` : 
		"""
		pass

class IDomainDataSetBulkOperations:

	def __init__(self) -> None:
		"""Creating a new Instance of this class is not allowed


		Raises
		--------
			Exception: if this class is instantiated
		"""
		raise Exception("Creating a new Instance of this class is not allowed")
		pass

	def EnterBulkOperationState(self, type: BulkOperationType) -> None:
		"""No Description

		Args
		--------
			type (``BulkOperationType``) :  type

		Returns
		--------
			``None`` : 
		"""
		pass

	def ExitBulkOperationState(self) -> None:
		"""No Description

		Returns
		--------
			``None`` : 
		"""
		pass

	@property
	def CurrentBulkOperationState(self) -> BulkOperationType:
		"""No Description

		Returns
		--------
			``IDomainDataSetBulkOperations`` : 
		"""
		pass

class IModelingElement(IEditLabeled):

	def __init__(self) -> None:
		"""Creating a new Instance of this class is not allowed


		Raises
		--------
			Exception: if this class is instantiated
		"""
		raise Exception("Creating a new Instance of this class is not allowed")
		pass

	def SupportedFields(self) -> FieldCollection:
		"""No Description

		Returns
		--------
			``FieldCollection`` : 
		"""
		pass

	@property
	def Id(self) -> int:
		"""No Description

		Returns
		--------
			``IModelingElement`` : 
		"""
		pass

	@property
	def Notes(self) -> str:
		"""No Description

		Returns
		--------
			``IModelingElement`` : 
		"""
		pass

	@Notes.setter
	def Notes(self, notes: str) -> None:
		pass

	@property
	def ModelingElementType(self) -> ModelingElementType:
		"""No Description

		Returns
		--------
			``IModelingElement`` : 
		"""
		pass

	@property
	def Manager(self) -> IModelingElementManager:
		"""No Description

		Returns
		--------
			``IModelingElement`` : 
		"""
		pass

class IModelingElementManager(IListManager):

	def __init__(self) -> None:
		"""Creating a new Instance of this class is not allowed


		Raises
		--------
			Exception: if this class is instantiated
		"""
		raise Exception("Creating a new Instance of this class is not allowed")
		pass

	def Copy(self, id: int) -> int:
		"""No Description

		Args
		--------
			id (``int``) :  id

		Returns
		--------
			``int`` : 
		"""
		pass

	def Element(self, id: int) -> IModelingElement:
		"""No Description

		Args
		--------
			id (``int``) :  id

		Returns
		--------
			``IModelingElement`` : 
		"""
		pass

	def Exists(self, id: int) -> bool:
		"""No Description

		Args
		--------
			id (``int``) :  id

		Returns
		--------
			``bool`` : 
		"""
		pass

	def Restore(self, id: int) -> None:
		"""No Description

		Args
		--------
			id (``int``) :  id

		Returns
		--------
			``None`` : 
		"""
		pass

	def Elements(self) -> ModelingElementCollection:
		"""No Description

		Returns
		--------
			``ModelingElementCollection`` : 
		"""
		pass

	def ElementIDs(self) -> HmIDCollection:
		"""No Description

		Returns
		--------
			``HmIDCollection`` : 
		"""
		pass

	def ModelingElementField(self, fieldName: str) -> IField:
		"""No Description

		Args
		--------
			fieldName (``str``) :  fieldName

		Returns
		--------
			``IField`` : 
		"""
		pass

	@property
	def DomainDataSet(self) -> IDomainDataSet:
		"""No Description

		Returns
		--------
			``IModelingElementManager`` : 
		"""
		pass

class IModelingElementManagerBatch:

	def __init__(self) -> None:
		"""Creating a new Instance of this class is not allowed


		Raises
		--------
			Exception: if this class is instantiated
		"""
		raise Exception("Creating a new Instance of this class is not allowed")
		pass

	def Restore(self, ids: HmIDCollection) -> None:
		"""No Description

		Args
		--------
			ids (``HmIDCollection``) :  ids

		Returns
		--------
			``None`` : 
		"""
		pass

class ITreeElement(IModelingElement):

	def __init__(self) -> None:
		"""Creating a new Instance of this class is not allowed


		Raises
		--------
			Exception: if this class is instantiated
		"""
		raise Exception("Creating a new Instance of this class is not allowed")
		pass

	def Children(self) -> ModelingElementCollection:
		"""No Description

		Returns
		--------
			``ModelingElementCollection`` : 
		"""
		pass

	@property
	def ParentID(self) -> int:
		"""No Description

		Returns
		--------
			``ITreeElement`` : 
		"""
		pass

	@ParentID.setter
	def ParentID(self, parentid: int) -> None:
		pass

class ITreeElement2:

	def __init__(self) -> None:
		"""Creating a new Instance of this class is not allowed


		Raises
		--------
			Exception: if this class is instantiated
		"""
		raise Exception("Creating a new Instance of this class is not allowed")
		pass

	def GetLevelInHierarchy(self) -> int:
		"""No Description

		Returns
		--------
			``int`` : 
		"""
		pass

	def IsDescendantOf(self, treeElement: ITreeElement, numberOfLevels: int) -> bool:
		"""No Description

		Args
		--------
			treeElement (``ITreeElement``) :  treeElement
			numberOfLevels (``int``) :  numberOfLevels

		Returns
		--------
			``bool`` : 
		"""
		pass

class ITreeElementManager(IModelingElementManager):

	def __init__(self) -> None:
		"""Creating a new Instance of this class is not allowed


		Raises
		--------
			Exception: if this class is instantiated
		"""
		raise Exception("Creating a new Instance of this class is not allowed")
		pass

	def BaseElements(self) -> ModelingElementCollection:
		"""No Description

		Returns
		--------
			``ModelingElementCollection`` : 
		"""
		pass

	def ChildrenOfElement(self, parentID: int) -> ModelingElementCollection:
		"""No Description

		Args
		--------
			parentID (``int``) :  parentID

		Returns
		--------
			``ModelingElementCollection`` : 
		"""
		pass

class IDomainElement(IModelingElement):

	def __init__(self) -> None:
		"""Creating a new Instance of this class is not allowed


		Raises
		--------
			Exception: if this class is instantiated
		"""
		raise Exception("Creating a new Instance of this class is not allowed")
		pass

	def DomainElementType(self) -> IDomainElementType:
		"""No Description

		Returns
		--------
			``IDomainElementType`` : 
		"""
		pass

	@overload
	def DomainElementField(self, fieldName: str) -> IField:
		"""No Description

		Args
		--------
			fieldName (``str``) :  fieldName

		Returns
		--------
			``IField`` : 
		"""
		pass

	@overload
	def DomainElementField(self, fieldName: str, alternativeTypeName: str) -> IField:
		"""No Description

		Args
		--------
			fieldName (``str``) :  fieldName
			alternativeTypeName (``str``) :  alternativeTypeName

		Returns
		--------
			``IField`` : 
		"""
		pass

	@property
	def DomainElementTypeID(self) -> int:
		"""No Description

		Returns
		--------
			``IDomainElement`` : 
		"""
		pass

class IDomainElementManager(IModelingElementManager, ISelectableManager):

	def __init__(self) -> None:
		"""Creating a new Instance of this class is not allowed


		Raises
		--------
			Exception: if this class is instantiated
		"""
		raise Exception("Creating a new Instance of this class is not allowed")
		pass

	def DomainElementType(self) -> IDomainElementType:
		"""No Description

		Returns
		--------
			``IDomainElementType`` : 
		"""
		pass

	def DelayedElementIDs(self) -> IHmIDDelayedCollection:
		"""No Description

		Returns
		--------
			``IHmIDDelayedCollection`` : 
		"""
		pass

	@overload
	def DomainElementField(self, fieldName: str) -> IField:
		"""No Description

		Args
		--------
			fieldName (``str``) :  fieldName

		Returns
		--------
			``IField`` : 
		"""
		pass

	@overload
	def DomainElementField(self, fieldName: str, alternativeTypeName: str) -> IField:
		"""No Description

		Args
		--------
			fieldName (``str``) :  fieldName
			alternativeTypeName (``str``) :  alternativeTypeName

		Returns
		--------
			``IField`` : 
		"""
		pass

	@overload
	def ResultField(self, fieldName: str, resultRecordTypeName: str) -> IField:
		"""No Description

		Args
		--------
			fieldName (``str``) :  fieldName
			resultRecordTypeName (``str``) :  resultRecordTypeName

		Returns
		--------
			``IField`` : 
		"""
		pass

	@overload
	def ResultField(self, fieldName: str, numericalEngineTypeName: str, resultRecordTypeName: str) -> IField:
		"""No Description

		Args
		--------
			fieldName (``str``) :  fieldName
			numericalEngineTypeName (``str``) :  numericalEngineTypeName
			resultRecordTypeName (``str``) :  resultRecordTypeName

		Returns
		--------
			``IField`` : 
		"""
		pass

	@overload
	def SupportedResultFields(self) -> FieldCollection:
		"""No Description

		Returns
		--------
			``FieldCollection`` : 
		"""
		pass

	@overload
	def SupportedResultFields(self, numericalEngineTypeName: str) -> FieldCollection:
		"""No Description

		Args
		--------
			numericalEngineTypeName (``str``) :  numericalEngineTypeName

		Returns
		--------
			``FieldCollection`` : 
		"""
		pass

	def CrossElementFieldListManager(self, collectionFieldName: str, alternativeTypeName: str, alternativeID: int, sortContexts: SortContextCollection, filterContexts: FilterContextCollection) -> ICrossElementFieldListManager:
		"""No Description

		Args
		--------
			collectionFieldName (``str``) :  collectionFieldName
			alternativeTypeName (``str``) :  alternativeTypeName
			alternativeID (``int``) :  alternativeID
			sortContexts (``SortContextCollection``) :  sortContexts
			filterContexts (``FilterContextCollection``) :  filterContexts

		Returns
		--------
			``ICrossElementFieldListManager`` : 
		"""
		pass

class IAlternative(ITreeElement):

	def __init__(self) -> None:
		"""Creating a new Instance of this class is not allowed


		Raises
		--------
			Exception: if this class is instantiated
		"""
		raise Exception("Creating a new Instance of this class is not allowed")
		pass

	def AlternativeType(self) -> IAlternativeType:
		"""No Description

		Returns
		--------
			``IAlternativeType`` : 
		"""
		pass

	def AlternativeRecord(self, domainElementTypeID: int) -> IAlternativeRecord:
		"""No Description

		Args
		--------
			domainElementTypeID (``int``) :  domainElementTypeID

		Returns
		--------
			``IAlternativeRecord`` : 
		"""
		pass

	def AlternativeField(self, name: str, domainElementTypeID: int) -> IField:
		"""No Description

		Args
		--------
			name (``str``) :  name
			domainElementTypeID (``int``) :  domainElementTypeID

		Returns
		--------
			``IField`` : 
		"""
		pass

	def SystemRecordField(self, name: str) -> ISystemRecordField:
		"""No Description

		Args
		--------
			name (``str``) :  name

		Returns
		--------
			``ISystemRecordField`` : 
		"""
		pass

	def AlternativeFields(self, domainElementTypeID: int) -> FieldCollection:
		"""No Description

		Args
		--------
			domainElementTypeID (``int``) :  domainElementTypeID

		Returns
		--------
			``FieldCollection`` : 
		"""
		pass

	def ReferencedScenarios(self) -> HmIDCollection:
		"""No Description

		Returns
		--------
			``HmIDCollection`` : 
		"""
		pass

	@property
	def AlternativeTypeID(self) -> int:
		"""No Description

		Returns
		--------
			``IAlternative`` : 
		"""
		pass

class IAlternativeManager(ITreeElementManager):

	def __init__(self) -> None:
		"""Creating a new Instance of this class is not allowed


		Raises
		--------
			Exception: if this class is instantiated
		"""
		raise Exception("Creating a new Instance of this class is not allowed")
		pass

	def AlternativeType(self) -> IAlternativeType:
		"""No Description

		Returns
		--------
			``IAlternativeType`` : 
		"""
		pass

	def SystemAlternativeRecord(self) -> ISystemAlternativeRecord:
		"""No Description

		Returns
		--------
			``ISystemAlternativeRecord`` : 
		"""
		pass

	@overload
	def Add(self, alternativeParentId: int) -> int:
		"""No Description

		Args
		--------
			alternativeParentId (``int``) :  alternativeParentId

		Returns
		--------
			``int`` : 
		"""
		pass

	def SystemRecordField(self, name: str) -> ISystemRecordField:
		"""No Description

		Args
		--------
			name (``str``) :  name

		Returns
		--------
			``ISystemRecordField`` : 
		"""
		pass

	def AlternativeField(self, name: str, domainElementTypeID: int, initialAlternativeID: int) -> IField:
		"""No Description

		Args
		--------
			name (``str``) :  name
			domainElementTypeID (``int``) :  domainElementTypeID
			initialAlternativeID (``int``) :  initialAlternativeID

		Returns
		--------
			``IField`` : 
		"""
		pass

	def Merge(self, sourceAlternativeID: int) -> None:
		"""No Description

		Args
		--------
			sourceAlternativeID (``int``) :  sourceAlternativeID

		Returns
		--------
			``None`` : 
		"""
		pass

	@overload
	def Add(self) -> int:
		"""No Description

		Returns
		--------
			``int`` : 
		"""
		pass

class IAlternativeRecord:

	def __init__(self) -> None:
		"""Creating a new Instance of this class is not allowed


		Raises
		--------
			Exception: if this class is instantiated
		"""
		raise Exception("Creating a new Instance of this class is not allowed")
		pass

	def IsLocal(self, elementID: int) -> bool:
		"""No Description

		Args
		--------
			elementID (``int``) :  elementID

		Returns
		--------
			``bool`` : 
		"""
		pass

	def MakeLocal(self, elementID: int) -> None:
		"""No Description

		Args
		--------
			elementID (``int``) :  elementID

		Returns
		--------
			``None`` : 
		"""
		pass

	def MakeInherited(self, elementID: int) -> None:
		"""No Description

		Args
		--------
			elementID (``int``) :  elementID

		Returns
		--------
			``None`` : 
		"""
		pass

	@overload
	def GetValue(self, elementID: int, fieldTypeID: int, unit: UnitIndex) -> object:
		"""No Description

		Args
		--------
			elementID (``int``) :  elementID
			fieldTypeID (``int``) :  fieldTypeID
			unit (``UnitIndex``) :  unit

		Returns
		--------
			``object`` : 
		"""
		pass

	@overload
	def GetValue(self, elementID: int, fieldName: str, unit: UnitIndex) -> object:
		"""No Description

		Args
		--------
			elementID (``int``) :  elementID
			fieldName (``str``) :  fieldName
			unit (``UnitIndex``) :  unit

		Returns
		--------
			``object`` : 
		"""
		pass

	@overload
	def SetValue(self, elementID: int, fieldTypeID: int, unit: UnitIndex, newVal: object) -> None:
		"""No Description

		Args
		--------
			elementID (``int``) :  elementID
			fieldTypeID (``int``) :  fieldTypeID
			unit (``UnitIndex``) :  unit
			newVal (``object``) :  newVal

		Returns
		--------
			``None`` : 
		"""
		pass

	@overload
	def SetValue(self, elementID: int, fieldName: str, unit: UnitIndex, newVal: object) -> None:
		"""No Description

		Args
		--------
			elementID (``int``) :  elementID
			fieldName (``str``) :  fieldName
			unit (``UnitIndex``) :  unit
			newVal (``object``) :  newVal

		Returns
		--------
			``None`` : 
		"""
		pass

	@overload
	def GetValues(self, fieldTypeID: int, unit: UnitIndex) -> Dict:
		"""No Description

		Args
		--------
			fieldTypeID (``int``) :  fieldTypeID
			unit (``UnitIndex``) :  unit

		Returns
		--------
			``Dict`` : 
		"""
		pass

	@overload
	def GetValues(self, fieldName: str, unit: UnitIndex) -> Dict:
		"""No Description

		Args
		--------
			fieldName (``str``) :  fieldName
			unit (``UnitIndex``) :  unit

		Returns
		--------
			``Dict`` : 
		"""
		pass

	@overload
	def GetDataReader(self) -> IAlternativeRecordDataReader:
		"""No Description

		Returns
		--------
			``IAlternativeRecordDataReader`` : 
		"""
		pass

	@overload
	def GetDataReader(self, fieldTypeNames: array[str]) -> IAlternativeRecordDataReader:
		"""No Description

		Args
		--------
			fieldTypeNames (``array[str]``) :  fieldTypeNames

		Returns
		--------
			``IAlternativeRecordDataReader`` : 
		"""
		pass

	@property
	def Alternative(self) -> IAlternative:
		"""No Description

		Returns
		--------
			``IAlternativeRecord`` : 
		"""
		pass

class IFieldCollectionDataReader:

	def __init__(self) -> None:
		"""Creating a new Instance of this class is not allowed


		Raises
		--------
			Exception: if this class is instantiated
		"""
		raise Exception("Creating a new Instance of this class is not allowed")
		pass

	@overload
	def GetValues(self, fieldTypeName: str) -> Dict:
		"""No Description

		Args
		--------
			fieldTypeName (``str``) :  fieldTypeName

		Returns
		--------
			``Dict`` : 
		"""
		pass

	@overload
	def GetValues(self, fieldTypeName: str, unit: UnitIndex) -> Dict:
		"""No Description

		Args
		--------
			fieldTypeName (``str``) :  fieldTypeName
			unit (``UnitIndex``) :  unit

		Returns
		--------
			``Dict`` : 
		"""
		pass

	def Dispose(self, fieldTypeName: str) -> None:
		"""No Description

		Args
		--------
			fieldTypeName (``str``) :  fieldTypeName

		Returns
		--------
			``None`` : 
		"""
		pass

	def Refresh(self) -> None:
		"""No Description

		Returns
		--------
			``None`` : 
		"""
		pass

	def Close(self) -> None:
		"""No Description

		Returns
		--------
			``None`` : 
		"""
		pass

class IAlternativeRecordDataReader(IFieldCollectionDataReader):

	def __init__(self) -> None:
		"""Creating a new Instance of this class is not allowed


		Raises
		--------
			Exception: if this class is instantiated
		"""
		raise Exception("Creating a new Instance of this class is not allowed")
		pass

	@property
	def AlternativeRecord(self) -> IAlternativeRecord:
		"""No Description

		Returns
		--------
			``IAlternativeRecordDataReader`` : 
		"""
		pass

class ISystemAlternativeRecord:

	def __init__(self) -> None:
		"""Creating a new Instance of this class is not allowed


		Raises
		--------
			Exception: if this class is instantiated
		"""
		raise Exception("Creating a new Instance of this class is not allowed")
		pass

	def IsLocal(self, alternativeID: int) -> bool:
		"""No Description

		Args
		--------
			alternativeID (``int``) :  alternativeID

		Returns
		--------
			``bool`` : 
		"""
		pass

	def MakeLocal(self, alternativeID: int) -> None:
		"""No Description

		Args
		--------
			alternativeID (``int``) :  alternativeID

		Returns
		--------
			``None`` : 
		"""
		pass

	def MakeInherited(self, alternativeID: int) -> None:
		"""No Description

		Args
		--------
			alternativeID (``int``) :  alternativeID

		Returns
		--------
			``None`` : 
		"""
		pass

	def GetValue(self, alternativeID: int, fieldTypeID: int, unit: UnitIndex) -> object:
		"""No Description

		Args
		--------
			alternativeID (``int``) :  alternativeID
			fieldTypeID (``int``) :  fieldTypeID
			unit (``UnitIndex``) :  unit

		Returns
		--------
			``object`` : 
		"""
		pass

	def SetValue(self, alternativeID: int, fieldTypeID: int, unit: UnitIndex, newVal: object) -> None:
		"""No Description

		Args
		--------
			alternativeID (``int``) :  alternativeID
			fieldTypeID (``int``) :  fieldTypeID
			unit (``UnitIndex``) :  unit
			newVal (``object``) :  newVal

		Returns
		--------
			``None`` : 
		"""
		pass

	@property
	def AlternativeTypeID(self) -> int:
		"""No Description

		Returns
		--------
			``ISystemAlternativeRecord`` : 
		"""
		pass

class IGeometryPointAlternativeRecord(IAlternativeRecord):

	def __init__(self) -> None:
		"""Creating a new Instance of this class is not allowed


		Raises
		--------
			Exception: if this class is instantiated
		"""
		raise Exception("Creating a new Instance of this class is not allowed")
		pass

	def GetPoint(self, domainElementID: int) -> GeometryPoint:
		"""No Description

		Args
		--------
			domainElementID (``int``) :  domainElementID

		Returns
		--------
			``GeometryPoint`` : 
		"""
		pass

	def SetPoint(self, domainElementID: int, point: GeometryPoint) -> None:
		"""No Description

		Args
		--------
			domainElementID (``int``) :  domainElementID
			point (``GeometryPoint``) :  point

		Returns
		--------
			``None`` : 
		"""
		pass

class IGeometryPolylineAlternativeRecord(IAlternativeRecord):

	def __init__(self) -> None:
		"""Creating a new Instance of this class is not allowed


		Raises
		--------
			Exception: if this class is instantiated
		"""
		raise Exception("Creating a new Instance of this class is not allowed")
		pass

	def GetPoints(self, domainElementID: int) -> List[GeometryPoint]:
		"""No Description

		Args
		--------
			domainElementID (``int``) :  domainElementID

		Returns
		--------
			``List[GeometryPoint]`` : 
		"""
		pass

	def SetPoints(self, domainElementID: int, points: List[GeometryPoint]) -> None:
		"""No Description

		Args
		--------
			domainElementID (``int``) :  domainElementID
			points (``List[GeometryPoint]``) :  points

		Returns
		--------
			``None`` : 
		"""
		pass

class IGeometryPolygonAlternativeRecord(IAlternativeRecord):

	def __init__(self) -> None:
		"""Creating a new Instance of this class is not allowed


		Raises
		--------
			Exception: if this class is instantiated
		"""
		raise Exception("Creating a new Instance of this class is not allowed")
		pass

	def GetRings(self, domainElementID: int) -> List[List[GeometryPoint]]:
		"""No Description

		Args
		--------
			domainElementID (``int``) :  domainElementID

		Returns
		--------
			``List[List[GeometryPoint]]`` : 
		"""
		pass

	def SetRings(self, domainElementID: int, rings: List[List[GeometryPoint]]) -> None:
		"""No Description

		Args
		--------
			domainElementID (``int``) :  domainElementID
			rings (``List[List[GeometryPoint]]``) :  rings

		Returns
		--------
			``None`` : 
		"""
		pass

class IScenario(ITreeElement):

	def __init__(self) -> None:
		"""Creating a new Instance of this class is not allowed


		Raises
		--------
			Exception: if this class is instantiated
		"""
		raise Exception("Creating a new Instance of this class is not allowed")
		pass

	@overload
	def AlternativeID(self, alternativeTypeID: int) -> int:
		"""No Description

		Args
		--------
			alternativeTypeID (``int``) :  alternativeTypeID

		Returns
		--------
			``int`` : 
		"""
		pass

	@overload
	def AlternativeID(self, alternativeTypeName: str) -> int:
		"""No Description

		Args
		--------
			alternativeTypeName (``str``) :  alternativeTypeName

		Returns
		--------
			``int`` : 
		"""
		pass

	@overload
	def AlternativeID(self, alternativeTypeID: int, alternativeID: int) -> None:
		"""No Description

		Args
		--------
			alternativeTypeID (``int``) :  alternativeTypeID
			alternativeID (``int``) :  alternativeID

		Returns
		--------
			``None`` : 
		"""
		pass

	@overload
	def AlternativeID(self, alternativeTypeName: str, alternativeID: int) -> None:
		"""No Description

		Args
		--------
			alternativeTypeName (``str``) :  alternativeTypeName
			alternativeID (``int``) :  alternativeID

		Returns
		--------
			``None`` : 
		"""
		pass

	def IsAlternativeLocal(self, alternativeTypeID: int) -> bool:
		"""No Description

		Args
		--------
			alternativeTypeID (``int``) :  alternativeTypeID

		Returns
		--------
			``bool`` : 
		"""
		pass

	def MakeAlternativeLocal(self, alternativeTypeID: int) -> None:
		"""No Description

		Args
		--------
			alternativeTypeID (``int``) :  alternativeTypeID

		Returns
		--------
			``None`` : 
		"""
		pass

	def MakeAlternativeInherited(self, alternativeTypeID: int) -> None:
		"""No Description

		Args
		--------
			alternativeTypeID (``int``) :  alternativeTypeID

		Returns
		--------
			``None`` : 
		"""
		pass

	def IsCalculationOptionsLocal(self, numericalEngineTypeName: str) -> bool:
		"""No Description

		Args
		--------
			numericalEngineTypeName (``str``) :  numericalEngineTypeName

		Returns
		--------
			``bool`` : 
		"""
		pass

	def MakeCalculationOptionsLocal(self, numericalEngineTypeName: str) -> None:
		"""No Description

		Args
		--------
			numericalEngineTypeName (``str``) :  numericalEngineTypeName

		Returns
		--------
			``None`` : 
		"""
		pass

	def MakeCalculationOptionsInherited(self, numericalEngineTypeName: str) -> None:
		"""No Description

		Args
		--------
			numericalEngineTypeName (``str``) :  numericalEngineTypeName

		Returns
		--------
			``None`` : 
		"""
		pass

	@overload
	def CalculationOptionsID(self, numericalEngineTypeName: str) -> int:
		"""No Description

		Args
		--------
			numericalEngineTypeName (``str``) :  numericalEngineTypeName

		Returns
		--------
			``int`` : 
		"""
		pass

	@overload
	def CalculationOptionsID(self, numericalEngineTypeName: str, calculationOptionsID: int) -> None:
		"""No Description

		Args
		--------
			numericalEngineTypeName (``str``) :  numericalEngineTypeName
			calculationOptionsID (``int``) :  calculationOptionsID

		Returns
		--------
			``None`` : 
		"""
		pass

	def ResultManager(self, numericalEngineTypeName: str) -> IResultManager:
		"""No Description

		Args
		--------
			numericalEngineTypeName (``str``) :  numericalEngineTypeName

		Returns
		--------
			``IResultManager`` : 
		"""
		pass

	def GetActiveNumericalEngineTypeName(self, resultRecordTypeName: str) -> str:
		"""No Description

		Args
		--------
			resultRecordTypeName (``str``) :  resultRecordTypeName

		Returns
		--------
			``str`` : 
		"""
		pass

	def SetActiveNumericalEngineTypeName(self, numericalEngineTypeName: str) -> None:
		"""No Description

		Args
		--------
			numericalEngineTypeName (``str``) :  numericalEngineTypeName

		Returns
		--------
			``None`` : 
		"""
		pass

	@property
	def ActiveTimeStep(self) -> int:
		"""No Description

		Returns
		--------
			``IScenario`` : 
		"""
		pass

	@ActiveTimeStep.setter
	def ActiveTimeStep(self, activetimestep: int) -> None:
		pass

	@property
	def ActiveTimeIncrement(self) -> int:
		"""No Description

		Returns
		--------
			``IScenario`` : 
		"""
		pass

	@ActiveTimeIncrement.setter
	def ActiveTimeIncrement(self, activetimeincrement: int) -> None:
		pass

class IScenarioManager(ITreeElementManager):

	def __init__(self) -> None:
		"""Creating a new Instance of this class is not allowed


		Raises
		--------
			Exception: if this class is instantiated
		"""
		raise Exception("Creating a new Instance of this class is not allowed")
		pass

	def CalculationOptionsManager(self, numericalEngineTypeName: str) -> ICalculationOptionsManager:
		"""No Description

		Args
		--------
			numericalEngineTypeName (``str``) :  numericalEngineTypeName

		Returns
		--------
			``ICalculationOptionsManager`` : 
		"""
		pass

	@overload
	def ResultField(self, fieldName: str) -> IField:
		"""No Description

		Args
		--------
			fieldName (``str``) :  fieldName

		Returns
		--------
			``IField`` : 
		"""
		pass

	@overload
	def ResultField(self, fieldName: str, numericalEngineTypeName: str) -> IField:
		"""No Description

		Args
		--------
			fieldName (``str``) :  fieldName
			numericalEngineTypeName (``str``) :  numericalEngineTypeName

		Returns
		--------
			``IField`` : 
		"""
		pass

	@overload
	def SupportedResultFields(self) -> FieldCollection:
		"""No Description

		Returns
		--------
			``FieldCollection`` : 
		"""
		pass

	@overload
	def SupportedResultFields(self, numericalEngineTypeName: str) -> FieldCollection:
		"""No Description

		Args
		--------
			numericalEngineTypeName (``str``) :  numericalEngineTypeName

		Returns
		--------
			``FieldCollection`` : 
		"""
		pass

	@property
	def ActiveScenarioID(self) -> int:
		"""No Description

		Returns
		--------
			``IScenarioManager`` : 
		"""
		pass

	@ActiveScenarioID.setter
	def ActiveScenarioID(self, activescenarioid: int) -> None:
		pass

class ICalculationOptionsManager(IModelingElementManager):

	def __init__(self) -> None:
		"""Creating a new Instance of this class is not allowed


		Raises
		--------
			Exception: if this class is instantiated
		"""
		raise Exception("Creating a new Instance of this class is not allowed")
		pass

	def CalculationOptionsField(self, name: str) -> IField:
		"""No Description

		Args
		--------
			name (``str``) :  name

		Returns
		--------
			``IField`` : 
		"""
		pass

	@property
	def NumericalEngineTypeName(self) -> str:
		"""No Description

		Returns
		--------
			``ICalculationOptionsManager`` : 
		"""
		pass

class ICalculationOptions(IModelingElement):

	def __init__(self) -> None:
		"""Creating a new Instance of this class is not allowed


		Raises
		--------
			Exception: if this class is instantiated
		"""
		raise Exception("Creating a new Instance of this class is not allowed")
		pass

	def CalculationOptionsField(self, name: str) -> IField:
		"""No Description

		Args
		--------
			name (``str``) :  name

		Returns
		--------
			``IField`` : 
		"""
		pass

	@property
	def NumericalEngineTypeName(self) -> str:
		"""No Description

		Returns
		--------
			``ICalculationOptions`` : 
		"""
		pass

class ISelectionSetManager(IModelingElementManager):

	def __init__(self) -> None:
		"""Creating a new Instance of this class is not allowed


		Raises
		--------
			Exception: if this class is instantiated
		"""
		raise Exception("Creating a new Instance of this class is not allowed")
		pass

	def SelectionSetField(self, name: str) -> IField:
		"""No Description

		Args
		--------
			name (``str``) :  name

		Returns
		--------
			``IField`` : 
		"""
		pass

class ISelectionSet(IModelingElement):

	def __init__(self) -> None:
		"""Creating a new Instance of this class is not allowed


		Raises
		--------
			Exception: if this class is instantiated
		"""
		raise Exception("Creating a new Instance of this class is not allowed")
		pass

	def SelectionSetField(self, name: str) -> IField:
		"""No Description

		Args
		--------
			name (``str``) :  name

		Returns
		--------
			``IField`` : 
		"""
		pass

class IEmbeddedStickyObjectManager(IModelingElementManager):

	def __init__(self) -> None:
		"""Creating a new Instance of this class is not allowed


		Raises
		--------
			Exception: if this class is instantiated
		"""
		raise Exception("Creating a new Instance of this class is not allowed")
		pass

	def EmbeddedStickyObjectField(self, name: str) -> IField:
		"""No Description

		Args
		--------
			name (``str``) :  name

		Returns
		--------
			``IField`` : 
		"""
		pass

	@overload
	def ElementIDs(self, domainElementID: int) -> HmIDCollection:
		"""No Description

		Args
		--------
			domainElementID (``int``) :  domainElementID

		Returns
		--------
			``HmIDCollection`` : 
		"""
		pass

	def ElementIDsForDomainElementType(self, domainElementTypeID: int) -> HmIDCollection:
		"""No Description

		Args
		--------
			domainElementTypeID (``int``) :  domainElementTypeID

		Returns
		--------
			``HmIDCollection`` : 
		"""
		pass

	@overload
	def ElementIDs(self) -> HmIDCollection:
		"""No Description

		Returns
		--------
			``HmIDCollection`` : 
		"""
		pass

class IEmbeddedStickyObject(IModelingElement):

	def __init__(self) -> None:
		"""Creating a new Instance of this class is not allowed


		Raises
		--------
			Exception: if this class is instantiated
		"""
		raise Exception("Creating a new Instance of this class is not allowed")
		pass

	def EmbeddedStickyObjectField(self, name: str) -> IField:
		"""No Description

		Args
		--------
			name (``str``) :  name

		Returns
		--------
			``IField`` : 
		"""
		pass

class IResultManager:

	def __init__(self) -> None:
		"""Creating a new Instance of this class is not allowed


		Raises
		--------
			Exception: if this class is instantiated
		"""
		raise Exception("Creating a new Instance of this class is not allowed")
		pass

	def Open(self) -> None:
		"""No Description

		Returns
		--------
			``None`` : 
		"""
		pass

	def Close(self) -> None:
		"""No Description

		Returns
		--------
			``None`` : 
		"""
		pass

	def Deactivate(self) -> None:
		"""No Description

		Returns
		--------
			``None`` : 
		"""
		pass

	def TimeSteps(self, unit: TimeUnit) -> array[float]:
		"""No Description

		Args
		--------
			unit (``TimeUnit``) :  unit

		Returns
		--------
			``array[float]`` : 
		"""
		pass

	@overload
	def ResultRecord(self, resultRecordTypeID: int) -> IResultRecord:
		"""No Description

		Args
		--------
			resultRecordTypeID (``int``) :  resultRecordTypeID

		Returns
		--------
			``IResultRecord`` : 
		"""
		pass

	@overload
	def ResultRecord(self, resultRecordTypeName: str) -> IResultRecord:
		"""No Description

		Args
		--------
			resultRecordTypeName (``str``) :  resultRecordTypeName

		Returns
		--------
			``IResultRecord`` : 
		"""
		pass

	def ResultRecords(self, domainElementTypeID: int) -> ResultRecordCollection:
		"""No Description

		Args
		--------
			domainElementTypeID (``int``) :  domainElementTypeID

		Returns
		--------
			``ResultRecordCollection`` : 
		"""
		pass

	@property
	def IsActive(self) -> bool:
		"""No Description

		Returns
		--------
			``IResultManager`` : 
		"""
		pass

	@property
	def HasResults(self) -> bool:
		"""No Description

		Returns
		--------
			``IResultManager`` : 
		"""
		pass

	@property
	def NumericalEngineTypeName(self) -> str:
		"""No Description

		Returns
		--------
			``IResultManager`` : 
		"""
		pass

	@property
	def Scenario(self) -> IScenario:
		"""No Description

		Returns
		--------
			``IResultManager`` : 
		"""
		pass

class IResultRecord:

	def __init__(self) -> None:
		"""Creating a new Instance of this class is not allowed


		Raises
		--------
			Exception: if this class is instantiated
		"""
		raise Exception("Creating a new Instance of this class is not allowed")
		pass

	def GetValue(self, elementID: int, resultFieldTypeName: str, timeStep: int, unit: UnitIndex) -> object:
		"""No Description

		Args
		--------
			elementID (``int``) :  elementID
			resultFieldTypeName (``str``) :  resultFieldTypeName
			timeStep (``int``) :  timeStep
			unit (``UnitIndex``) :  unit

		Returns
		--------
			``object`` : 
		"""
		pass

	def GetValues(self, domainElementTypeIDs: HmIDCollection, resultFieldTypeName: str, timeStep: int, unit: UnitIndex) -> Dict:
		"""No Description

		Args
		--------
			domainElementTypeIDs (``HmIDCollection``) :  domainElementTypeIDs
			resultFieldTypeName (``str``) :  resultFieldTypeName
			timeStep (``int``) :  timeStep
			unit (``UnitIndex``) :  unit

		Returns
		--------
			``Dict`` : 
		"""
		pass

	def GetValuesOverTime(self, elementID: int, resultFieldTypeName: str, unit: UnitIndex) -> array:
		"""No Description

		Args
		--------
			elementID (``int``) :  elementID
			resultFieldTypeName (``str``) :  resultFieldTypeName
			unit (``UnitIndex``) :  unit

		Returns
		--------
			``array`` : 
		"""
		pass

class IResultField(IField):

	def __init__(self) -> None:
		"""Creating a new Instance of this class is not allowed


		Raises
		--------
			Exception: if this class is instantiated
		"""
		raise Exception("Creating a new Instance of this class is not allowed")
		pass

	def IsActive(self, scenarioId: int) -> bool:
		"""No Description

		Args
		--------
			scenarioId (``int``) :  scenarioId

		Returns
		--------
			``bool`` : 
		"""
		pass

	def HasResults(self, scenarioId: int) -> bool:
		"""No Description

		Args
		--------
			scenarioId (``int``) :  scenarioId

		Returns
		--------
			``bool`` : 
		"""
		pass

	def GetValuesForElementIDs(self, ids: HmIDCollection, scenarioID: int) -> Dict:
		"""No Description

		Args
		--------
			ids (``HmIDCollection``) :  ids
			scenarioID (``int``) :  scenarioID

		Returns
		--------
			``Dict`` : 
		"""
		pass

	@property
	def NumericalEngineType(self) -> INumericalEngineType:
		"""No Description

		Returns
		--------
			``IResultField`` : 
		"""
		pass

	@property
	def ResultRecordType(self) -> IResultRecordType:
		"""No Description

		Returns
		--------
			``IResultField`` : 
		"""
		pass

class IResultNonTimeVariantField(IResultField):

	def __init__(self) -> None:
		"""Creating a new Instance of this class is not allowed


		Raises
		--------
			Exception: if this class is instantiated
		"""
		raise Exception("Creating a new Instance of this class is not allowed")
		pass

	@overload
	def GetValue(self, elementID: int, scenarioID: int) -> object:
		"""No Description

		Args
		--------
			elementID (``int``) :  elementID
			scenarioID (``int``) :  scenarioID

		Returns
		--------
			``object`` : 
		"""
		pass

	@overload
	def GetValues(self, domainElementTypeIDs: HmIDCollection, scenarioID: int) -> Dict:
		"""No Description

		Args
		--------
			domainElementTypeIDs (``HmIDCollection``) :  domainElementTypeIDs
			scenarioID (``int``) :  scenarioID

		Returns
		--------
			``Dict`` : 
		"""
		pass

	@overload
	def GetUniqueValues(self, scenarioID: int) -> array:
		"""No Description

		Args
		--------
			scenarioID (``int``) :  scenarioID

		Returns
		--------
			``array`` : 
		"""
		pass

	@overload
	def GetUniqueValues(self, scenarioID: int, domainElementTypeIDs: HmIDCollection) -> array:
		"""No Description

		Args
		--------
			scenarioID (``int``) :  scenarioID
			domainElementTypeIDs (``HmIDCollection``) :  domainElementTypeIDs

		Returns
		--------
			``array`` : 
		"""
		pass

	@overload
	def GetValue(self, id: int) -> object:
		"""No Description

		Args
		--------
			id (``int``) :  id

		Returns
		--------
			``object`` : 
		"""
		pass

	@overload
	def GetValues(self) -> Dict:
		"""No Description

		Returns
		--------
			``Dict`` : 
		"""
		pass

	@overload
	def GetValues(self, ids: HmIDCollection) -> Dict:
		"""No Description

		Args
		--------
			ids (``HmIDCollection``) :  ids

		Returns
		--------
			``Dict`` : 
		"""
		pass

class IResultTimeVariantField(IResultField):

	def __init__(self) -> None:
		"""Creating a new Instance of this class is not allowed


		Raises
		--------
			Exception: if this class is instantiated
		"""
		raise Exception("Creating a new Instance of this class is not allowed")
		pass

	@overload
	def GetValue(self, elementID: int, scenarioID: int, timeStep: int) -> object:
		"""No Description

		Args
		--------
			elementID (``int``) :  elementID
			scenarioID (``int``) :  scenarioID
			timeStep (``int``) :  timeStep

		Returns
		--------
			``object`` : 
		"""
		pass

	def GetValuesOverTime(self, elementID: int, scenarioID: int) -> array:
		"""No Description

		Args
		--------
			elementID (``int``) :  elementID
			scenarioID (``int``) :  scenarioID

		Returns
		--------
			``array`` : 
		"""
		pass

	@overload
	def GetValues(self, domainElementTypeIDs: HmIDCollection, scenarioID: int, timeStep: int) -> Dict:
		"""No Description

		Args
		--------
			domainElementTypeIDs (``HmIDCollection``) :  domainElementTypeIDs
			scenarioID (``int``) :  scenarioID
			timeStep (``int``) :  timeStep

		Returns
		--------
			``Dict`` : 
		"""
		pass

	@overload
	def GetUniqueValues(self, scenarioID: int, timeStep: int) -> array:
		"""No Description

		Args
		--------
			scenarioID (``int``) :  scenarioID
			timeStep (``int``) :  timeStep

		Returns
		--------
			``array`` : 
		"""
		pass

	@overload
	def GetUniqueValues(self, scenarioID: int, timeStep: int, domainElementTypeIDs: HmIDCollection) -> array:
		"""No Description

		Args
		--------
			scenarioID (``int``) :  scenarioID
			timeStep (``int``) :  timeStep
			domainElementTypeIDs (``HmIDCollection``) :  domainElementTypeIDs

		Returns
		--------
			``array`` : 
		"""
		pass

	@overload
	def GetValuesForElementIDs(self, ids: HmIDCollection, scenarioID: int, timeStep: int) -> Dict:
		"""No Description

		Args
		--------
			ids (``HmIDCollection``) :  ids
			scenarioID (``int``) :  scenarioID
			timeStep (``int``) :  timeStep

		Returns
		--------
			``Dict`` : 
		"""
		pass

	@overload
	def GetValuesForElementIDs(self, ids: HmIDCollection, scenarioID: int) -> Dict:
		"""No Description

		Args
		--------
			ids (``HmIDCollection``) :  ids
			scenarioID (``int``) :  scenarioID

		Returns
		--------
			``Dict`` : 
		"""
		pass

	@overload
	def GetValue(self, id: int) -> object:
		"""No Description

		Args
		--------
			id (``int``) :  id

		Returns
		--------
			``object`` : 
		"""
		pass

	@overload
	def GetValues(self) -> Dict:
		"""No Description

		Returns
		--------
			``Dict`` : 
		"""
		pass

	@overload
	def GetValues(self, ids: HmIDCollection) -> Dict:
		"""No Description

		Args
		--------
			ids (``HmIDCollection``) :  ids

		Returns
		--------
			``Dict`` : 
		"""
		pass

class IFieldStatistics:

	def __init__(self) -> None:
		"""Creating a new Instance of this class is not allowed


		Raises
		--------
			Exception: if this class is instantiated
		"""
		raise Exception("Creating a new Instance of this class is not allowed")
		pass

	def GetStatistics(self, statTypes: List[StatisticType]) -> array[float]:
		"""No Description

		Args
		--------
			statTypes (``List[StatisticType]``) :  statTypes

		Returns
		--------
			``array[float]`` : 
		"""
		pass

class ISelectableFieldStatistics(IFieldStatistics):

	def __init__(self) -> None:
		"""Creating a new Instance of this class is not allowed


		Raises
		--------
			Exception: if this class is instantiated
		"""
		raise Exception("Creating a new Instance of this class is not allowed")
		pass

	@overload
	def GetStatistics(self, statTypes: List[StatisticType], filterContexts: FilterContextCollection) -> array[float]:
		"""No Description

		Args
		--------
			statTypes (``List[StatisticType]``) :  statTypes
			filterContexts (``FilterContextCollection``) :  filterContexts

		Returns
		--------
			``array[float]`` : 
		"""
		pass

	@overload
	def GetStatistics(self, statTypes: List[StatisticType]) -> array[float]:
		"""No Description

		Args
		--------
			statTypes (``List[StatisticType]``) :  statTypes

		Returns
		--------
			``array[float]`` : 
		"""
		pass

class IResultFieldStatistics(ISelectableFieldStatistics):

	def __init__(self) -> None:
		"""Creating a new Instance of this class is not allowed


		Raises
		--------
			Exception: if this class is instantiated
		"""
		raise Exception("Creating a new Instance of this class is not allowed")
		pass

	@overload
	def GetStatistics(self, scenarioID: int, domainElementTypeIDs: HmIDCollection, statTypes: List[StatisticType], filterContexts: FilterContextCollection) -> array[float]:
		"""No Description

		Args
		--------
			scenarioID (``int``) :  scenarioID
			domainElementTypeIDs (``HmIDCollection``) :  domainElementTypeIDs
			statTypes (``List[StatisticType]``) :  statTypes
			filterContexts (``FilterContextCollection``) :  filterContexts

		Returns
		--------
			``array[float]`` : 
		"""
		pass

	def GetStatisticsEstimate(self, scenarioID: int, domainElementTypeIDs: HmIDCollection, statTypes: List[StatisticType], filterContexts: FilterContextCollection) -> array[float]:
		"""No Description

		Args
		--------
			scenarioID (``int``) :  scenarioID
			domainElementTypeIDs (``HmIDCollection``) :  domainElementTypeIDs
			statTypes (``List[StatisticType]``) :  statTypes
			filterContexts (``FilterContextCollection``) :  filterContexts

		Returns
		--------
			``array[float]`` : 
		"""
		pass

	@overload
	def GetStatistics(self, statTypes: List[StatisticType], filterContexts: FilterContextCollection) -> array[float]:
		"""No Description

		Args
		--------
			statTypes (``List[StatisticType]``) :  statTypes
			filterContexts (``FilterContextCollection``) :  filterContexts

		Returns
		--------
			``array[float]`` : 
		"""
		pass

	@overload
	def GetStatistics(self, statTypes: List[StatisticType]) -> array[float]:
		"""No Description

		Args
		--------
			statTypes (``List[StatisticType]``) :  statTypes

		Returns
		--------
			``array[float]`` : 
		"""
		pass

class IResultTimeVariantFieldStatistics(IResultFieldStatistics):

	def __init__(self) -> None:
		"""Creating a new Instance of this class is not allowed


		Raises
		--------
			Exception: if this class is instantiated
		"""
		raise Exception("Creating a new Instance of this class is not allowed")
		pass

	@overload
	def GetStatistics(self, elementID: int, scenarioID: int, statTypes: List[StatisticType]) -> array[float]:
		"""No Description

		Args
		--------
			elementID (``int``) :  elementID
			scenarioID (``int``) :  scenarioID
			statTypes (``List[StatisticType]``) :  statTypes

		Returns
		--------
			``array[float]`` : 
		"""
		pass

	@overload
	def GetStatistics(self, scenarioID: int, domainElementTypeIDs: HmIDCollection, statTypes: List[StatisticType], timeStepIndex: int, filterContexts: FilterContextCollection) -> array[float]:
		"""No Description

		Args
		--------
			scenarioID (``int``) :  scenarioID
			domainElementTypeIDs (``HmIDCollection``) :  domainElementTypeIDs
			statTypes (``List[StatisticType]``) :  statTypes
			timeStepIndex (``int``) :  timeStepIndex
			filterContexts (``FilterContextCollection``) :  filterContexts

		Returns
		--------
			``array[float]`` : 
		"""
		pass

	@overload
	def GetStatistics(self, scenarioID: int, domainElementTypeIDs: HmIDCollection, statTypes: List[StatisticType], filterContexts: FilterContextCollection) -> array[float]:
		"""No Description

		Args
		--------
			scenarioID (``int``) :  scenarioID
			domainElementTypeIDs (``HmIDCollection``) :  domainElementTypeIDs
			statTypes (``List[StatisticType]``) :  statTypes
			filterContexts (``FilterContextCollection``) :  filterContexts

		Returns
		--------
			``array[float]`` : 
		"""
		pass

	@overload
	def GetStatistics(self, statTypes: List[StatisticType], filterContexts: FilterContextCollection) -> array[float]:
		"""No Description

		Args
		--------
			statTypes (``List[StatisticType]``) :  statTypes
			filterContexts (``FilterContextCollection``) :  filterContexts

		Returns
		--------
			``array[float]`` : 
		"""
		pass

	@overload
	def GetStatistics(self, statTypes: List[StatisticType]) -> array[float]:
		"""No Description

		Args
		--------
			statTypes (``List[StatisticType]``) :  statTypes

		Returns
		--------
			``array[float]`` : 
		"""
		pass

class INumericalEngine:

	def __init__(self) -> None:
		"""Creating a new Instance of this class is not allowed


		Raises
		--------
			Exception: if this class is instantiated
		"""
		raise Exception("Creating a new Instance of this class is not allowed")
		pass

	def Run(self, scenarios: ModelingElementCollection) -> None:
		"""No Description

		Args
		--------
			scenarios (``ModelingElementCollection``) :  scenarios

		Returns
		--------
			``None`` : 
		"""
		pass

	def IsRunning(self, scenarioID: int) -> bool:
		"""No Description

		Args
		--------
			scenarioID (``int``) :  scenarioID

		Returns
		--------
			``bool`` : 
		"""
		pass

	def add_ScenarioCalculationStarted(self, value: EventHandler) -> None:
		"""No Description

		Args
		--------
			value (``EventHandler``) :  value

		Returns
		--------
			``None`` : 
		"""
		pass

	def remove_ScenarioCalculationStarted(self, value: EventHandler) -> None:
		"""No Description

		Args
		--------
			value (``EventHandler``) :  value

		Returns
		--------
			``None`` : 
		"""
		pass

	def add_ScenarioCalculationFinished(self, value: EventHandler) -> None:
		"""No Description

		Args
		--------
			value (``EventHandler``) :  value

		Returns
		--------
			``None`` : 
		"""
		pass

	def remove_ScenarioCalculationFinished(self, value: EventHandler) -> None:
		"""No Description

		Args
		--------
			value (``EventHandler``) :  value

		Returns
		--------
			``None`` : 
		"""
		pass

	def add_CalculationStepStarted(self, value: EventHandler) -> None:
		"""No Description

		Args
		--------
			value (``EventHandler``) :  value

		Returns
		--------
			``None`` : 
		"""
		pass

	def remove_CalculationStepStarted(self, value: EventHandler) -> None:
		"""No Description

		Args
		--------
			value (``EventHandler``) :  value

		Returns
		--------
			``None`` : 
		"""
		pass

	def add_CalculationStepProgress(self, value: CalculationStepProgressEventHandler) -> None:
		"""No Description

		Args
		--------
			value (``CalculationStepProgressEventHandler``) :  value

		Returns
		--------
			``None`` : 
		"""
		pass

	def remove_CalculationStepProgress(self, value: CalculationStepProgressEventHandler) -> None:
		"""No Description

		Args
		--------
			value (``CalculationStepProgressEventHandler``) :  value

		Returns
		--------
			``None`` : 
		"""
		pass

	def add_CalculationStepFinished(self, value: EventHandler) -> None:
		"""No Description

		Args
		--------
			value (``EventHandler``) :  value

		Returns
		--------
			``None`` : 
		"""
		pass

	def remove_CalculationStepFinished(self, value: EventHandler) -> None:
		"""No Description

		Args
		--------
			value (``EventHandler``) :  value

		Returns
		--------
			``None`` : 
		"""
		pass

	def add_CalculationStarted(self, value: EventHandler) -> None:
		"""No Description

		Args
		--------
			value (``EventHandler``) :  value

		Returns
		--------
			``None`` : 
		"""
		pass

	def remove_CalculationStarted(self, value: EventHandler) -> None:
		"""No Description

		Args
		--------
			value (``EventHandler``) :  value

		Returns
		--------
			``None`` : 
		"""
		pass

	def add_CalculationFinished(self, value: EventHandler) -> None:
		"""No Description

		Args
		--------
			value (``EventHandler``) :  value

		Returns
		--------
			``None`` : 
		"""
		pass

	def remove_CalculationFinished(self, value: EventHandler) -> None:
		"""No Description

		Args
		--------
			value (``EventHandler``) :  value

		Returns
		--------
			``None`` : 
		"""
		pass

	@property
	def NumericalEngineTypeName(self) -> str:
		"""No Description

		Returns
		--------
			``INumericalEngine`` : 
		"""
		pass

	@property
	def NumericalEnginePath(self) -> str:
		"""No Description

		Returns
		--------
			``INumericalEngine`` : 
		"""
		pass

	@NumericalEnginePath.setter
	def NumericalEnginePath(self, numericalenginepath: str) -> None:
		pass

	@property
	def ResultDataConnection(self) -> IResultDataConnection:
		"""No Description

		Returns
		--------
			``INumericalEngine`` : 
		"""
		pass

class ICompositeNumericalEngine:

	def __init__(self) -> None:
		"""Creating a new Instance of this class is not allowed


		Raises
		--------
			Exception: if this class is instantiated
		"""
		raise Exception("Creating a new Instance of this class is not allowed")
		pass

	def GetActiveNumericalEngine(self, scenarioID: int) -> INumericalEngine:
		"""No Description

		Args
		--------
			scenarioID (``int``) :  scenarioID

		Returns
		--------
			``INumericalEngine`` : 
		"""
		pass

	def SupportsValidation(self, scenarioID: int) -> bool:
		"""No Description

		Args
		--------
			scenarioID (``int``) :  scenarioID

		Returns
		--------
			``bool`` : 
		"""
		pass

class ICompositeResultDataConnection:

	def __init__(self) -> None:
		"""Creating a new Instance of this class is not allowed


		Raises
		--------
			Exception: if this class is instantiated
		"""
		raise Exception("Creating a new Instance of this class is not allowed")
		pass

	def GetActiveResultDataConnection(self, scenarioID: int) -> IResultDataConnection:
		"""No Description

		Args
		--------
			scenarioID (``int``) :  scenarioID

		Returns
		--------
			``IResultDataConnection`` : 
		"""
		pass

class IResultDataConnectionFactory:

	def __init__(self) -> None:
		"""Creating a new Instance of this class is not allowed


		Raises
		--------
			Exception: if this class is instantiated
		"""
		raise Exception("Creating a new Instance of this class is not allowed")
		pass

	def NewResultDataConnection(self, domainDataSet: IDomainDataSet, numericalEngine: INumericalEngine) -> IResultDataConnection:
		"""No Description

		Args
		--------
			domainDataSet (``IDomainDataSet``) :  domainDataSet
			numericalEngine (``INumericalEngine``) :  numericalEngine

		Returns
		--------
			``IResultDataConnection`` : 
		"""
		pass

class IValidatingNumericalEngine(INumericalEngine):

	def __init__(self) -> None:
		"""Creating a new Instance of this class is not allowed


		Raises
		--------
			Exception: if this class is instantiated
		"""
		raise Exception("Creating a new Instance of this class is not allowed")
		pass

	def Validate(self, scenarios: ModelingElementCollection) -> None:
		"""No Description

		Args
		--------
			scenarios (``ModelingElementCollection``) :  scenarios

		Returns
		--------
			``None`` : 
		"""
		pass

class ILicensedNumericalEngine(INumericalEngine):

	def __init__(self) -> None:
		"""Creating a new Instance of this class is not allowed


		Raises
		--------
			Exception: if this class is instantiated
		"""
		raise Exception("Creating a new Instance of this class is not allowed")
		pass

	def SetLicensingInfo(self, license: License) -> None:
		"""No Description

		Args
		--------
			license (``License``) :  license

		Returns
		--------
			``None`` : 
		"""
		pass

class INumericalEngineWithResultDataConnectionFactory:

	def __init__(self) -> None:
		"""Creating a new Instance of this class is not allowed


		Raises
		--------
			Exception: if this class is instantiated
		"""
		raise Exception("Creating a new Instance of this class is not allowed")
		pass

	@ResultDataConnectionFactory.setter
	def ResultDataConnectionFactory(self, resultdataconnectionfactory: IResultDataConnectionFactory) -> None:
		pass

class ILicensedNumericalEngineEx(ILicensedNumericalEngine):

	def __init__(self) -> None:
		"""Creating a new Instance of this class is not allowed


		Raises
		--------
			Exception: if this class is instantiated
		"""
		raise Exception("Creating a new Instance of this class is not allowed")
		pass

	@overload
	def SetLicensingInfo(self, licenseProvider: ILicenseProvider) -> None:
		"""No Description

		Args
		--------
			licenseProvider (``ILicenseProvider``) :  licenseProvider

		Returns
		--------
			``None`` : 
		"""
		pass

	@overload
	def SetLicensingInfo(self, license: License) -> None:
		"""No Description

		Args
		--------
			license (``License``) :  license

		Returns
		--------
			``None`` : 
		"""
		pass

class IResultDataConnection:

	def __init__(self) -> None:
		"""Creating a new Instance of this class is not allowed


		Raises
		--------
			Exception: if this class is instantiated
		"""
		raise Exception("Creating a new Instance of this class is not allowed")
		pass

	def Open(self, scenarioID: int) -> None:
		"""No Description

		Args
		--------
			scenarioID (``int``) :  scenarioID

		Returns
		--------
			``None`` : 
		"""
		pass

	def Close(self, scenarioID: int) -> None:
		"""No Description

		Args
		--------
			scenarioID (``int``) :  scenarioID

		Returns
		--------
			``None`` : 
		"""
		pass

	def Deactivate(self, scenarioID: int) -> None:
		"""No Description

		Args
		--------
			scenarioID (``int``) :  scenarioID

		Returns
		--------
			``None`` : 
		"""
		pass

	def IsActive(self, scenarioID: int) -> bool:
		"""No Description

		Args
		--------
			scenarioID (``int``) :  scenarioID

		Returns
		--------
			``bool`` : 
		"""
		pass

	def HasResults(self, scenarioID: int) -> bool:
		"""No Description

		Args
		--------
			scenarioID (``int``) :  scenarioID

		Returns
		--------
			``bool`` : 
		"""
		pass

	def TimeStepsInSeconds(self, scenarioID: int) -> array[float]:
		"""No Description

		Args
		--------
			scenarioID (``int``) :  scenarioID

		Returns
		--------
			``array[float]`` : 
		"""
		pass

	def ResultRecordDataBroker(self, resultRecordTypeName: str) -> IResultRecordDataBroker:
		"""No Description

		Args
		--------
			resultRecordTypeName (``str``) :  resultRecordTypeName

		Returns
		--------
			``IResultRecordDataBroker`` : 
		"""
		pass

	def GetScenarioStartDateTime(self, scenarioID: int) -> datetime:
		"""No Description

		Args
		--------
			scenarioID (``int``) :  scenarioID

		Returns
		--------
			``datetime`` : 
		"""
		pass

	def GetRunUserNotificationsSummary(self, scenarioID: int) -> List[IUserNotification]:
		"""No Description

		Args
		--------
			scenarioID (``int``) :  scenarioID

		Returns
		--------
			``List[IUserNotification]`` : 
		"""
		pass

	def GetTimeStepUserNotificationsSummary(self, scenarioID: int, timeStepIndex: int) -> List[IUserNotification]:
		"""No Description

		Args
		--------
			scenarioID (``int``) :  scenarioID
			timeStepIndex (``int``) :  timeStepIndex

		Returns
		--------
			``List[IUserNotification]`` : 
		"""
		pass

	def GetUserNotifications(self, scenarioID: int, elementID: int, timeStepIndex: int) -> List[IUserNotification]:
		"""No Description

		Args
		--------
			scenarioID (``int``) :  scenarioID
			elementID (``int``) :  elementID
			timeStepIndex (``int``) :  timeStepIndex

		Returns
		--------
			``List[IUserNotification]`` : 
		"""
		pass

	def ResultConnectionIDs(self) -> HmIDCollection:
		"""No Description

		Returns
		--------
			``HmIDCollection`` : 
		"""
		pass

	def ResultPathAndFileNamesFor(self, databasePathAndFileName: str) -> array[str]:
		"""No Description

		Args
		--------
			databasePathAndFileName (``str``) :  databasePathAndFileName

		Returns
		--------
			``array[str]`` : 
		"""
		pass

	def NewResultPathAndFileNameFor(self, currentResultFileAndPathName: str, databasePathAndFileName: str) -> str:
		"""No Description

		Args
		--------
			currentResultFileAndPathName (``str``) :  currentResultFileAndPathName
			databasePathAndFileName (``str``) :  databasePathAndFileName

		Returns
		--------
			``str`` : 
		"""
		pass

	@property
	def DomainDataSet(self) -> IDomainDataSet:
		"""No Description

		Returns
		--------
			``IResultDataConnection`` : 
		"""
		pass

	@property
	def NumericalEngine(self) -> INumericalEngine:
		"""No Description

		Returns
		--------
			``IResultDataConnection`` : 
		"""
		pass

class IResultDataConnectionEX:

	def __init__(self) -> None:
		"""Creating a new Instance of this class is not allowed


		Raises
		--------
			Exception: if this class is instantiated
		"""
		raise Exception("Creating a new Instance of this class is not allowed")
		pass

	def HasHydraulicResults(self, elementId: int, scenarioID: int) -> bool:
		"""No Description

		Args
		--------
			elementId (``int``) :  elementId
			scenarioID (``int``) :  scenarioID

		Returns
		--------
			``bool`` : 
		"""
		pass

class ITranslatingTimeStepsResultDataConnection(IResultDataConnection):

	def __init__(self) -> None:
		"""Creating a new Instance of this class is not allowed


		Raises
		--------
			Exception: if this class is instantiated
		"""
		raise Exception("Creating a new Instance of this class is not allowed")
		pass

	def GetTranslatedTimeStepIndex(self, scenarioID: int, elementID: int, uberTimeStepIndex: int, isGravityResultField: bool) -> int:
		"""No Description

		Args
		--------
			scenarioID (``int``) :  scenarioID
			elementID (``int``) :  elementID
			uberTimeStepIndex (``int``) :  uberTimeStepIndex
			isGravityResultField (``bool``) :  isGravityResultField

		Returns
		--------
			``int`` : 
		"""
		pass

	def GetTimeStepsForSubnetworkID(self, scenarioID: int, subnetworkIndex: int) -> array[float]:
		"""No Description

		Args
		--------
			scenarioID (``int``) :  scenarioID
			subnetworkIndex (``int``) :  subnetworkIndex

		Returns
		--------
			``array[float]`` : 
		"""
		pass

	@overload
	def GetTimeStepUserNotificationsSummary(self, scenarioID: int, timeStepIndex: int, pressureSubnetworkID: int) -> List[IUserNotification]:
		"""No Description

		Args
		--------
			scenarioID (``int``) :  scenarioID
			timeStepIndex (``int``) :  timeStepIndex
			pressureSubnetworkID (``int``) :  pressureSubnetworkID

		Returns
		--------
			``List[IUserNotification]`` : 
		"""
		pass

	def PrepareResultDataConnectionForTimeStepsRequest(self, factor: int) -> None:
		"""No Description

		Args
		--------
			factor (``int``) :  factor

		Returns
		--------
			``None`` : 
		"""
		pass

	@overload
	def GetTimeStepUserNotificationsSummary(self, scenarioID: int, timeStepIndex: int) -> List[IUserNotification]:
		"""No Description

		Args
		--------
			scenarioID (``int``) :  scenarioID
			timeStepIndex (``int``) :  timeStepIndex

		Returns
		--------
			``List[IUserNotification]`` : 
		"""
		pass

	@property
	def UseHydrologicTimeSteps(self) -> bool:
		"""No Description

		Returns
		--------
			``ITranslatingTimeStepsResultDataConnection`` : 
		"""
		pass

	@UseHydrologicTimeSteps.setter
	def UseHydrologicTimeSteps(self, usehydrologictimesteps: bool) -> None:
		pass

	@property
	def UseReportingHydraulicTimeSteps(self) -> bool:
		"""No Description

		Returns
		--------
			``ITranslatingTimeStepsResultDataConnection`` : 
		"""
		pass

	@UseReportingHydraulicTimeSteps.setter
	def UseReportingHydraulicTimeSteps(self, usereportinghydraulictimesteps: bool) -> None:
		pass

	@property
	def ActiveSubnetworkID(self) -> int:
		"""No Description

		Returns
		--------
			``ITranslatingTimeStepsResultDataConnection`` : 
		"""
		pass

	@ActiveSubnetworkID.setter
	def ActiveSubnetworkID(self, activesubnetworkid: int) -> None:
		pass

class IResultRecordDataBroker:

	def __init__(self) -> None:
		"""Creating a new Instance of this class is not allowed


		Raises
		--------
			Exception: if this class is instantiated
		"""
		raise Exception("Creating a new Instance of this class is not allowed")
		pass

	def GetValue(self, elementID: int, scenarioID: int, fieldTypeName: str, timeStep: int) -> object:
		"""No Description

		Args
		--------
			elementID (``int``) :  elementID
			scenarioID (``int``) :  scenarioID
			fieldTypeName (``str``) :  fieldTypeName
			timeStep (``int``) :  timeStep

		Returns
		--------
			``object`` : 
		"""
		pass

	def GetValues(self, domainElementTypeIDs: HmIDCollection, scenarioID: int, fieldTypeName: str, timeStep: int) -> Dict:
		"""No Description

		Args
		--------
			domainElementTypeIDs (``HmIDCollection``) :  domainElementTypeIDs
			scenarioID (``int``) :  scenarioID
			fieldTypeName (``str``) :  fieldTypeName
			timeStep (``int``) :  timeStep

		Returns
		--------
			``Dict`` : 
		"""
		pass

	def GetValuesForElementIDs(self, elementIDs: HmIDCollection, scenarioID: int, fieldTypeName: str, timeStep: int) -> Dict:
		"""No Description

		Args
		--------
			elementIDs (``HmIDCollection``) :  elementIDs
			scenarioID (``int``) :  scenarioID
			fieldTypeName (``str``) :  fieldTypeName
			timeStep (``int``) :  timeStep

		Returns
		--------
			``Dict`` : 
		"""
		pass

	def GetValuesOverTime(self, elementID: int, scenarioID: int, fieldTypeName: str) -> array:
		"""No Description

		Args
		--------
			elementID (``int``) :  elementID
			scenarioID (``int``) :  scenarioID
			fieldTypeName (``str``) :  fieldTypeName

		Returns
		--------
			``array`` : 
		"""
		pass

	def GetStatisticValues(self, scenarioID: int, domainElementTypeIDs: HmIDCollection, fieldTypeName: str, statTypes: List[StatisticType], timeStepIndex: int, filterContexts: FilterContextCollection) -> array[float]:
		"""No Description

		Args
		--------
			scenarioID (``int``) :  scenarioID
			domainElementTypeIDs (``HmIDCollection``) :  domainElementTypeIDs
			fieldTypeName (``str``) :  fieldTypeName
			statTypes (``List[StatisticType]``) :  statTypes
			timeStepIndex (``int``) :  timeStepIndex
			filterContexts (``FilterContextCollection``) :  filterContexts

		Returns
		--------
			``array[float]`` : 
		"""
		pass

	def GetStatisticEstimateValues(self, scenarioID: int, domainElementTypeIDs: HmIDCollection, fieldTypeName: str, statTypes: List[StatisticType], timeStepIndex: int, filterContexts: FilterContextCollection) -> array[float]:
		"""No Description

		Args
		--------
			scenarioID (``int``) :  scenarioID
			domainElementTypeIDs (``HmIDCollection``) :  domainElementTypeIDs
			fieldTypeName (``str``) :  fieldTypeName
			statTypes (``List[StatisticType]``) :  statTypes
			timeStepIndex (``int``) :  timeStepIndex
			filterContexts (``FilterContextCollection``) :  filterContexts

		Returns
		--------
			``array[float]`` : 
		"""
		pass

	def GetStatisticValuesOverTime(self, elementID: int, scenarioID: int, fieldTypeName: str, statTypes: List[StatisticType]) -> array[float]:
		"""No Description

		Args
		--------
			elementID (``int``) :  elementID
			scenarioID (``int``) :  scenarioID
			fieldTypeName (``str``) :  fieldTypeName
			statTypes (``List[StatisticType]``) :  statTypes

		Returns
		--------
			``array[float]`` : 
		"""
		pass

	@property
	def ResultDataConnection(self) -> IResultDataConnection:
		"""No Description

		Returns
		--------
			``IResultRecordDataBroker`` : 
		"""
		pass

	@property
	def ResultRecordTypeName(self) -> str:
		"""No Description

		Returns
		--------
			``IResultRecordDataBroker`` : 
		"""
		pass

class ISupportElement(IModelingElement):

	def __init__(self) -> None:
		"""Creating a new Instance of this class is not allowed


		Raises
		--------
			Exception: if this class is instantiated
		"""
		raise Exception("Creating a new Instance of this class is not allowed")
		pass

	def SupportElementField(self, attributeName: str) -> IField:
		"""No Description

		Args
		--------
			attributeName (``str``) :  attributeName

		Returns
		--------
			``IField`` : 
		"""
		pass

	def SynchronizeFrom(self, engineeringReference: IEngineeringReference) -> None:
		"""No Description

		Args
		--------
			engineeringReference (``IEngineeringReference``) :  engineeringReference

		Returns
		--------
			``None`` : 
		"""
		pass

	def ConnectTo(self, engineeringReference: IEngineeringReference) -> None:
		"""No Description

		Args
		--------
			engineeringReference (``IEngineeringReference``) :  engineeringReference

		Returns
		--------
			``None`` : 
		"""
		pass

	@property
	def SupportElementTypeID(self) -> int:
		"""No Description

		Returns
		--------
			``ISupportElement`` : 
		"""
		pass

	@property
	def EngineeringReferenceGuid(self) -> Guid:
		"""No Description

		Returns
		--------
			``ISupportElement`` : 
		"""
		pass

	@property
	def EngineeringLibraryGuid(self) -> Guid:
		"""No Description

		Returns
		--------
			``ISupportElement`` : 
		"""
		pass

	@property
	def DateModified(self) -> datetime:
		"""No Description

		Returns
		--------
			``ISupportElement`` : 
		"""
		pass

class ISupportElement2:

	def __init__(self) -> None:
		"""Creating a new Instance of this class is not allowed


		Raises
		--------
			Exception: if this class is instantiated
		"""
		raise Exception("Creating a new Instance of this class is not allowed")
		pass

	def SetEngineeringReference(self, engineeringLibraryGuid: Guid, engineeringReferenceGuid: Guid) -> None:
		"""No Description

		Args
		--------
			engineeringLibraryGuid (``Guid``) :  engineeringLibraryGuid
			engineeringReferenceGuid (``Guid``) :  engineeringReferenceGuid

		Returns
		--------
			``None`` : 
		"""
		pass

class ISupportElementManager(IModelingElementManager, ISelectableManager):

	def __init__(self) -> None:
		"""Creating a new Instance of this class is not allowed


		Raises
		--------
			Exception: if this class is instantiated
		"""
		raise Exception("Creating a new Instance of this class is not allowed")
		pass

	def SupportElementField(self, attributeName: str) -> IField:
		"""No Description

		Args
		--------
			attributeName (``str``) :  attributeName

		Returns
		--------
			``IField`` : 
		"""
		pass

	@overload
	def Add(self, engineeringReference: IEngineeringReference) -> int:
		"""No Description

		Args
		--------
			engineeringReference (``IEngineeringReference``) :  engineeringReference

		Returns
		--------
			``int`` : 
		"""
		pass

	def CrossElementFieldListManager(self, collectionFieldName: str, sortContexts: SortContextCollection, filterContexts: FilterContextCollection) -> ICrossElementFieldListManager:
		"""No Description

		Args
		--------
			collectionFieldName (``str``) :  collectionFieldName
			sortContexts (``SortContextCollection``) :  sortContexts
			filterContexts (``FilterContextCollection``) :  filterContexts

		Returns
		--------
			``ICrossElementFieldListManager`` : 
		"""
		pass

	@overload
	def Add(self) -> int:
		"""No Description

		Returns
		--------
			``int`` : 
		"""
		pass

	@property
	def SupportElementTypeID(self) -> int:
		"""No Description

		Returns
		--------
			``ISupportElementManager`` : 
		"""
		pass

class IControlManager(ISupportElementManager):

	def __init__(self) -> None:
		"""Creating a new Instance of this class is not allowed


		Raises
		--------
			Exception: if this class is instantiated
		"""
		raise Exception("Creating a new Instance of this class is not allowed")
		pass

	def Flush(self) -> None:
		"""No Description

		Returns
		--------
			``None`` : 
		"""
		pass

	def ResetWorkingUnits(self) -> None:
		"""No Description

		Returns
		--------
			``None`` : 
		"""
		pass

class IPrototypeManager(IModelingElementManager):

	def __init__(self) -> None:
		"""Creating a new Instance of this class is not allowed


		Raises
		--------
			Exception: if this class is instantiated
		"""
		raise Exception("Creating a new Instance of this class is not allowed")
		pass

	@property
	def ActivePrototypeID(self) -> int:
		"""No Description

		Returns
		--------
			``IPrototypeManager`` : 
		"""
		pass

	@ActivePrototypeID.setter
	def ActivePrototypeID(self, activeprototypeid: int) -> None:
		pass

class IPrototypeDomainElementManager(IPrototypeManager):

	def __init__(self) -> None:
		"""Creating a new Instance of this class is not allowed


		Raises
		--------
			Exception: if this class is instantiated
		"""
		raise Exception("Creating a new Instance of this class is not allowed")
		pass

	@overload
	def PrototypeDomainElementField(self, fieldName: str) -> IField:
		"""No Description

		Args
		--------
			fieldName (``str``) :  fieldName

		Returns
		--------
			``IField`` : 
		"""
		pass

	@overload
	def PrototypeDomainElementField(self, fieldName: str, alternativeTypeName: str) -> IField:
		"""No Description

		Args
		--------
			fieldName (``str``) :  fieldName
			alternativeTypeName (``str``) :  alternativeTypeName

		Returns
		--------
			``IField`` : 
		"""
		pass

	@overload
	def Exists(self, prototypeGuid: Guid) -> bool:
		"""No Description

		Args
		--------
			prototypeGuid (``Guid``) :  prototypeGuid

		Returns
		--------
			``bool`` : 
		"""
		pass

	def ElementID(self, prototypeGuid: Guid) -> int:
		"""No Description

		Args
		--------
			prototypeGuid (``Guid``) :  prototypeGuid

		Returns
		--------
			``int`` : 
		"""
		pass

	@overload
	def Exists(self, id: int) -> bool:
		"""No Description

		Args
		--------
			id (``int``) :  id

		Returns
		--------
			``bool`` : 
		"""
		pass

	@property
	def DomainElementTypeID(self) -> int:
		"""No Description

		Returns
		--------
			``IPrototypeDomainElementManager`` : 
		"""
		pass

class IPrototypeDomainElement(IModelingElement):

	def __init__(self) -> None:
		"""Creating a new Instance of this class is not allowed


		Raises
		--------
			Exception: if this class is instantiated
		"""
		raise Exception("Creating a new Instance of this class is not allowed")
		pass

	@overload
	def PrototypeDomainElementField(self, fieldName: str) -> IField:
		"""No Description

		Args
		--------
			fieldName (``str``) :  fieldName

		Returns
		--------
			``IField`` : 
		"""
		pass

	@overload
	def PrototypeDomainElementField(self, fieldName: str, alternativeTypeName: str) -> IField:
		"""No Description

		Args
		--------
			fieldName (``str``) :  fieldName
			alternativeTypeName (``str``) :  alternativeTypeName

		Returns
		--------
			``IField`` : 
		"""
		pass

	def SetPrototypeGuid(self, prototypeGuid: Guid) -> None:
		"""No Description

		Args
		--------
			prototypeGuid (``Guid``) :  prototypeGuid

		Returns
		--------
			``None`` : 
		"""
		pass

	@property
	def DomainElementTypeID(self) -> int:
		"""No Description

		Returns
		--------
			``IPrototypeDomainElement`` : 
		"""
		pass

	@property
	def PrototypeGuid(self) -> Guid:
		"""No Description

		Returns
		--------
			``IPrototypeDomainElement`` : 
		"""
		pass

class IFieldManager:

	def __init__(self) -> None:
		"""Creating a new Instance of this class is not allowed


		Raises
		--------
			Exception: if this class is instantiated
		"""
		raise Exception("Creating a new Instance of this class is not allowed")
		pass

	def ModelingElementField(self, name: str, type: ModelingElementType, elementTypeID: int) -> IField:
		"""No Description

		Args
		--------
			name (``str``) :  name
			type (``ModelingElementType``) :  type
			elementTypeID (``int``) :  elementTypeID

		Returns
		--------
			``IField`` : 
		"""
		pass

	def ModelingElementFields(self, type: ModelingElementType, elementTypeID: int) -> FieldCollection:
		"""No Description

		Args
		--------
			type (``ModelingElementType``) :  type
			elementTypeID (``int``) :  elementTypeID

		Returns
		--------
			``FieldCollection`` : 
		"""
		pass

	def SupportElementFields(self, supportElementTypeID: int) -> FieldCollection:
		"""No Description

		Args
		--------
			supportElementTypeID (``int``) :  supportElementTypeID

		Returns
		--------
			``FieldCollection`` : 
		"""
		pass

	@overload
	def SupportElementField(self, name: str, supportElementTypeID: int) -> IField:
		"""No Description

		Args
		--------
			name (``str``) :  name
			supportElementTypeID (``int``) :  supportElementTypeID

		Returns
		--------
			``IField`` : 
		"""
		pass

	@overload
	def SupportElementField(self, name: str, supportElementTypeName: str) -> IField:
		"""No Description

		Args
		--------
			name (``str``) :  name
			supportElementTypeName (``str``) :  supportElementTypeName

		Returns
		--------
			``IField`` : 
		"""
		pass

	@overload
	def DomainElementField(self, name: str, domainElementTypeID: int) -> IField:
		"""No Description

		Args
		--------
			name (``str``) :  name
			domainElementTypeID (``int``) :  domainElementTypeID

		Returns
		--------
			``IField`` : 
		"""
		pass

	@overload
	def DomainElementField(self, name: str, domainElementTypeName: str) -> IField:
		"""No Description

		Args
		--------
			name (``str``) :  name
			domainElementTypeName (``str``) :  domainElementTypeName

		Returns
		--------
			``IField`` : 
		"""
		pass

	@overload
	def DomainElementField(self, name: str, alternativeTypeID: int, domainElementTypeID: int) -> IField:
		"""No Description

		Args
		--------
			name (``str``) :  name
			alternativeTypeID (``int``) :  alternativeTypeID
			domainElementTypeID (``int``) :  domainElementTypeID

		Returns
		--------
			``IField`` : 
		"""
		pass

	@overload
	def DomainElementField(self, name: str, alternativeTypeName: str, domainElementTypeName: str) -> IField:
		"""No Description

		Args
		--------
			name (``str``) :  name
			alternativeTypeName (``str``) :  alternativeTypeName
			domainElementTypeName (``str``) :  domainElementTypeName

		Returns
		--------
			``IField`` : 
		"""
		pass

	@overload
	def AlternativeField(self, name: str, alternativeTypeID: int, domainElementTypeID: int, alternativeID: int) -> IField:
		"""No Description

		Args
		--------
			name (``str``) :  name
			alternativeTypeID (``int``) :  alternativeTypeID
			domainElementTypeID (``int``) :  domainElementTypeID
			alternativeID (``int``) :  alternativeID

		Returns
		--------
			``IField`` : 
		"""
		pass

	@overload
	def AlternativeField(self, name: str, alternativeTypeName: str, domainElementTypeName: str, alternativeID: int) -> IField:
		"""No Description

		Args
		--------
			name (``str``) :  name
			alternativeTypeName (``str``) :  alternativeTypeName
			domainElementTypeName (``str``) :  domainElementTypeName
			alternativeID (``int``) :  alternativeID

		Returns
		--------
			``IField`` : 
		"""
		pass

	@overload
	def SystemRecordField(self, name: str, alternativeTypeID: int) -> IField:
		"""No Description

		Args
		--------
			name (``str``) :  name
			alternativeTypeID (``int``) :  alternativeTypeID

		Returns
		--------
			``IField`` : 
		"""
		pass

	@overload
	def SystemRecordField(self, name: str, alternativeTypeName: str) -> IField:
		"""No Description

		Args
		--------
			name (``str``) :  name
			alternativeTypeName (``str``) :  alternativeTypeName

		Returns
		--------
			``IField`` : 
		"""
		pass

	def SystemRecordFields(self, alternativeTypeID: int) -> FieldCollection:
		"""No Description

		Args
		--------
			alternativeTypeID (``int``) :  alternativeTypeID

		Returns
		--------
			``FieldCollection`` : 
		"""
		pass

	@overload
	def AlternativeFields(self, alternativeTypeID: int, domainElementTypeID: int, alternativeID: int) -> FieldCollection:
		"""No Description

		Args
		--------
			alternativeTypeID (``int``) :  alternativeTypeID
			domainElementTypeID (``int``) :  domainElementTypeID
			alternativeID (``int``) :  alternativeID

		Returns
		--------
			``FieldCollection`` : 
		"""
		pass

	@overload
	def AlternativeFields(self, domainElementTypeID: int, scenarioID: int) -> FieldCollection:
		"""No Description

		Args
		--------
			domainElementTypeID (``int``) :  domainElementTypeID
			scenarioID (``int``) :  scenarioID

		Returns
		--------
			``FieldCollection`` : 
		"""
		pass

	def ResultField(self, name: str, numericalEngineType: str, resultRecordTypeName: str) -> IField:
		"""No Description

		Args
		--------
			name (``str``) :  name
			numericalEngineType (``str``) :  numericalEngineType
			resultRecordTypeName (``str``) :  resultRecordTypeName

		Returns
		--------
			``IField`` : 
		"""
		pass

	@overload
	def DomainElementFields(self, alternativeTypeID: int, domainElementTypeID: int) -> FieldCollection:
		"""No Description

		Args
		--------
			alternativeTypeID (``int``) :  alternativeTypeID
			domainElementTypeID (``int``) :  domainElementTypeID

		Returns
		--------
			``FieldCollection`` : 
		"""
		pass

	@overload
	def DomainElementFields(self, domainElementTypeID: int) -> FieldCollection:
		"""No Description

		Args
		--------
			domainElementTypeID (``int``) :  domainElementTypeID

		Returns
		--------
			``FieldCollection`` : 
		"""
		pass

	def ResultFields(self, numericalEngineTypeName: str, resultRecordTypeName: str, domainElementTypeID: int) -> FieldCollection:
		"""No Description

		Args
		--------
			numericalEngineTypeName (``str``) :  numericalEngineTypeName
			resultRecordTypeName (``str``) :  resultRecordTypeName
			domainElementTypeID (``int``) :  domainElementTypeID

		Returns
		--------
			``FieldCollection`` : 
		"""
		pass

	def ScenarioResultFields(self, numericalEngineTypeName: str) -> FieldCollection:
		"""No Description

		Args
		--------
			numericalEngineTypeName (``str``) :  numericalEngineTypeName

		Returns
		--------
			``FieldCollection`` : 
		"""
		pass

	def DomainDataSetField(self, name: str) -> IField:
		"""No Description

		Args
		--------
			name (``str``) :  name

		Returns
		--------
			``IField`` : 
		"""
		pass

	@property
	def DomainDataSet(self) -> IDomainDataSet:
		"""No Description

		Returns
		--------
			``IFieldManager`` : 
		"""
		pass

class IControlFieldManager(IFieldManager):

	def __init__(self) -> None:
		"""Creating a new Instance of this class is not allowed


		Raises
		--------
			Exception: if this class is instantiated
		"""
		raise Exception("Creating a new Instance of this class is not allowed")
		pass

	@property
	def IsLoadingControls(self) -> bool:
		"""No Description

		Returns
		--------
			``IControlFieldManager`` : 
		"""
		pass

	@IsLoadingControls.setter
	def IsLoadingControls(self, isloadingcontrols: bool) -> None:
		pass

class IFieldManagerEx(IFieldManager):

	def __init__(self) -> None:
		"""Creating a new Instance of this class is not allowed


		Raises
		--------
			Exception: if this class is instantiated
		"""
		raise Exception("Creating a new Instance of this class is not allowed")
		pass

	def SupportedFlexTableFields(self, domainElementTyepID: int, isPipeTwoScenarioFlexTable: bool) -> FieldCollection:
		"""No Description

		Args
		--------
			domainElementTyepID (``int``) :  domainElementTyepID
			isPipeTwoScenarioFlexTable (``bool``) :  isPipeTwoScenarioFlexTable

		Returns
		--------
			``FieldCollection`` : 
		"""
		pass

	def FlexTableField(self, name: str) -> IField:
		"""No Description

		Args
		--------
			name (``str``) :  name

		Returns
		--------
			``IField`` : 
		"""
		pass

	def FlexTableFieldExists(self, elementTypeId: int, name: str) -> bool:
		"""No Description

		Args
		--------
			elementTypeId (``int``) :  elementTypeId
			name (``str``) :  name

		Returns
		--------
			``bool`` : 
		"""
		pass

class IDomainField(IField):

	def __init__(self) -> None:
		"""Creating a new Instance of this class is not allowed


		Raises
		--------
			Exception: if this class is instantiated
		"""
		raise Exception("Creating a new Instance of this class is not allowed")
		pass

	def GetUniqueValues(self) -> array:
		"""No Description

		Returns
		--------
			``array`` : 
		"""
		pass

	@property
	def FieldType(self) -> IFieldType:
		"""No Description

		Returns
		--------
			``IDomainField`` : 
		"""
		pass

class IEnumeratedField(IField):

	def __init__(self) -> None:
		"""Creating a new Instance of this class is not allowed


		Raises
		--------
			Exception: if this class is instantiated
		"""
		raise Exception("Creating a new Instance of this class is not allowed")
		pass

	def GetEnumeratedMembers(self) -> List[IEnumeratedMember]:
		"""No Description

		Returns
		--------
			``List[IEnumeratedMember]`` : 
		"""
		pass

class IEnumeratedMember:

	def __init__(self) -> None:
		"""Creating a new Instance of this class is not allowed


		Raises
		--------
			Exception: if this class is instantiated
		"""
		raise Exception("Creating a new Instance of this class is not allowed")
		pass

	def Field(self, name: str) -> IField:
		"""No Description

		Args
		--------
			name (``str``) :  name

		Returns
		--------
			``IField`` : 
		"""
		pass

	def SupportedFields(self) -> FieldCollection:
		"""No Description

		Returns
		--------
			``FieldCollection`` : 
		"""
		pass

	@property
	def Name(self) -> str:
		"""No Description

		Returns
		--------
			``IEnumeratedMember`` : 
		"""
		pass

	@property
	def Label(self) -> str:
		"""No Description

		Returns
		--------
			``IEnumeratedMember`` : 
		"""
		pass

	@Label.setter
	def Label(self, label: str) -> None:
		pass

	@property
	def ParentField(self) -> IField:
		"""No Description

		Returns
		--------
			``IEnumeratedMember`` : 
		"""
		pass

	@property
	def EnumerationValue(self) -> int:
		"""No Description

		Returns
		--------
			``IEnumeratedMember`` : 
		"""
		pass

class IDataField(IField):

	def __init__(self) -> None:
		"""Creating a new Instance of this class is not allowed


		Raises
		--------
			Exception: if this class is instantiated
		"""
		raise Exception("Creating a new Instance of this class is not allowed")
		pass

	@property
	def TableName(self) -> str:
		"""No Description

		Returns
		--------
			``IDataField`` : 
		"""
		pass

class ICollectionField(IField):

	def __init__(self) -> None:
		"""Creating a new Instance of this class is not allowed


		Raises
		--------
			Exception: if this class is instantiated
		"""
		raise Exception("Creating a new Instance of this class is not allowed")
		pass

	def GetEmptyCollectionFieldListManager(self) -> ICollectionFieldListManager:
		"""No Description

		Returns
		--------
			``ICollectionFieldListManager`` : 
		"""
		pass

class IUnitizedField(IField):

	def __init__(self) -> None:
		"""Creating a new Instance of this class is not allowed


		Raises
		--------
			Exception: if this class is instantiated
		"""
		raise Exception("Creating a new Instance of this class is not allowed")
		pass

	def GetDoubleValue(self, id: int) -> float:
		"""No Description

		Args
		--------
			id (``int``) :  id

		Returns
		--------
			``float`` : 
		"""
		pass

	@property
	def WorkingUnitIndex(self) -> UnitIndex:
		"""No Description

		Returns
		--------
			``IUnitizedField`` : 
		"""
		pass

	@WorkingUnitIndex.setter
	def WorkingUnitIndex(self, workingunitindex: UnitIndex) -> None:
		pass

	@property
	def StorageUnitIndex(self) -> UnitIndex:
		"""No Description

		Returns
		--------
			``IUnitizedField`` : 
		"""
		pass

class IPresentationUnitsManager:

	def __init__(self) -> None:
		"""Creating a new Instance of this class is not allowed


		Raises
		--------
			Exception: if this class is instantiated
		"""
		raise Exception("Creating a new Instance of this class is not allowed")
		pass

	def GetDisplayUnitFor(self, formatterName: str) -> Unit:
		"""No Description

		Args
		--------
			formatterName (``str``) :  formatterName

		Returns
		--------
			``Unit`` : 
		"""
		pass

	def StringFromDoubleUnit(self, value: float, formatterName: str, storageUnit: Unit) -> str:
		"""No Description

		Args
		--------
			value (``float``) :  value
			formatterName (``str``) :  formatterName
			storageUnit (``Unit``) :  storageUnit

		Returns
		--------
			``str`` : 
		"""
		pass

class IGeometryField(IField):

	def __init__(self) -> None:
		"""Creating a new Instance of this class is not allowed


		Raises
		--------
			Exception: if this class is instantiated
		"""
		raise Exception("Creating a new Instance of this class is not allowed")
		pass

	@property
	def ShouldUpdateBoundingBox(self) -> bool:
		"""No Description

		Returns
		--------
			``IGeometryField`` : 
		"""
		pass

	@ShouldUpdateBoundingBox.setter
	def ShouldUpdateBoundingBox(self, shouldupdateboundingbox: bool) -> None:
		pass

class IRealGeometryField(IField):

	def __init__(self) -> None:
		"""Creating a new Instance of this class is not allowed


		Raises
		--------
			Exception: if this class is instantiated
		"""
		raise Exception("Creating a new Instance of this class is not allowed")
		pass

	def GetGeometry(self, id: int) -> List[int]:
		"""No Description

		Args
		--------
			id (``int``) :  id

		Returns
		--------
			``List[int]`` : 
		"""
		pass

	def SetGeometry(self, id: int, bytes: List[int]) -> None:
		"""No Description

		Args
		--------
			id (``int``) :  id
			bytes (``List[int]``) :  bytes

		Returns
		--------
			``None`` : 
		"""
		pass

	@property
	def StorageUnitSystem(self) -> UnitSystem:
		"""No Description

		Returns
		--------
			``IRealGeometryField`` : 
		"""
		pass

	@property
	def WorkingUnitSystem(self) -> UnitSystem:
		"""No Description

		Returns
		--------
			``IRealGeometryField`` : 
		"""
		pass

	@WorkingUnitSystem.setter
	def WorkingUnitSystem(self, workingunitsystem: UnitSystem) -> None:
		pass

class IReferenceField(IField):

	def __init__(self) -> None:
		"""Creating a new Instance of this class is not allowed


		Raises
		--------
			Exception: if this class is instantiated
		"""
		raise Exception("Creating a new Instance of this class is not allowed")
		pass

	@property
	def ReferencedElementManager(self) -> IModelingElementManager:
		"""No Description

		Returns
		--------
			``IReferenceField`` : 
		"""
		pass

class IGeometryPointField(IUnitizedField):

	def __init__(self) -> None:
		"""Creating a new Instance of this class is not allowed


		Raises
		--------
			Exception: if this class is instantiated
		"""
		raise Exception("Creating a new Instance of this class is not allowed")
		pass

	def GetPoint(self, id: int) -> GeometryPoint:
		"""No Description

		Args
		--------
			id (``int``) :  id

		Returns
		--------
			``GeometryPoint`` : 
		"""
		pass

	def SetPoint(self, id: int, point: GeometryPoint) -> None:
		"""No Description

		Args
		--------
			id (``int``) :  id
			point (``GeometryPoint``) :  point

		Returns
		--------
			``None`` : 
		"""
		pass

class IGeometryReferenceNodeField:

	def __init__(self) -> None:
		"""Creating a new Instance of this class is not allowed


		Raises
		--------
			Exception: if this class is instantiated
		"""
		raise Exception("Creating a new Instance of this class is not allowed")
		pass

	def RefreshReferenceNode(self, elementID: int) -> None:
		"""No Description

		Args
		--------
			elementID (``int``) :  elementID

		Returns
		--------
			``None`` : 
		"""
		pass

	def RefreshReferenceNodes(self, valuesDic: IHmIDToObjectDictionary) -> None:
		"""No Description

		Args
		--------
			valuesDic (``IHmIDToObjectDictionary``) :  valuesDic

		Returns
		--------
			``None`` : 
		"""
		pass

class IGeometryPolylineField(IUnitizedField):

	def __init__(self) -> None:
		"""Creating a new Instance of this class is not allowed


		Raises
		--------
			Exception: if this class is instantiated
		"""
		raise Exception("Creating a new Instance of this class is not allowed")
		pass

	def GetPoints(self, id: int) -> List[GeometryPoint]:
		"""No Description

		Args
		--------
			id (``int``) :  id

		Returns
		--------
			``List[GeometryPoint]`` : 
		"""
		pass

	def SetPoints(self, id: int, points: List[GeometryPoint]) -> None:
		"""No Description

		Args
		--------
			id (``int``) :  id
			points (``List[GeometryPoint]``) :  points

		Returns
		--------
			``None`` : 
		"""
		pass

	def RefreshScaledLengths(self, valuesDic: IHmIDToObjectDictionary) -> None:
		"""No Description

		Args
		--------
			valuesDic (``IHmIDToObjectDictionary``) :  valuesDic

		Returns
		--------
			``None`` : 
		"""
		pass

class IGeometryLateralField:

	def __init__(self) -> None:
		"""Creating a new Instance of this class is not allowed


		Raises
		--------
			Exception: if this class is instantiated
		"""
		raise Exception("Creating a new Instance of this class is not allowed")
		pass

	def RefreshLateral(self, elementID: int) -> None:
		"""No Description

		Args
		--------
			elementID (``int``) :  elementID

		Returns
		--------
			``None`` : 
		"""
		pass

	def RefreshLaterals(self, valuesDic: IHmIDToObjectDictionary) -> None:
		"""No Description

		Args
		--------
			valuesDic (``IHmIDToObjectDictionary``) :  valuesDic

		Returns
		--------
			``None`` : 
		"""
		pass

class IGeometryPolygonField(IUnitizedField):

	def __init__(self) -> None:
		"""Creating a new Instance of this class is not allowed


		Raises
		--------
			Exception: if this class is instantiated
		"""
		raise Exception("Creating a new Instance of this class is not allowed")
		pass

	def GetRings(self, id: int) -> List[List[GeometryPoint]]:
		"""No Description

		Args
		--------
			id (``int``) :  id

		Returns
		--------
			``List[List[GeometryPoint]]`` : 
		"""
		pass

	def SetRings(self, id: int, rings: List[List[GeometryPoint]]) -> None:
		"""No Description

		Args
		--------
			id (``int``) :  id
			rings (``List[List[GeometryPoint]]``) :  rings

		Returns
		--------
			``None`` : 
		"""
		pass

	def RefreshScaledAreas(self, valuesDic: IHmIDToObjectDictionary) -> None:
		"""No Description

		Args
		--------
			valuesDic (``IHmIDToObjectDictionary``) :  valuesDic

		Returns
		--------
			``None`` : 
		"""
		pass

class IModelingElementField:

	def __init__(self) -> None:
		"""Creating a new Instance of this class is not allowed


		Raises
		--------
			Exception: if this class is instantiated
		"""
		raise Exception("Creating a new Instance of this class is not allowed")
		pass

	@property
	def SupportedModelingElementType(self) -> ModelingElementType:
		"""No Description

		Returns
		--------
			``IModelingElementField`` : 
		"""
		pass

	@property
	def ElementTypeID(self) -> int:
		"""No Description

		Returns
		--------
			``IModelingElementField`` : 
		"""
		pass

class ISupportElementField(IEditField):

	def __init__(self) -> None:
		"""Creating a new Instance of this class is not allowed


		Raises
		--------
			Exception: if this class is instantiated
		"""
		raise Exception("Creating a new Instance of this class is not allowed")
		pass

	@property
	def SupportElementType(self) -> ISupportElementType:
		"""No Description

		Returns
		--------
			``ISupportElementField`` : 
		"""
		pass

class IDomainElementField(IDataField):

	def __init__(self) -> None:
		"""Creating a new Instance of this class is not allowed


		Raises
		--------
			Exception: if this class is instantiated
		"""
		raise Exception("Creating a new Instance of this class is not allowed")
		pass

	def AlternativeRecord(self) -> IAlternativeRecord:
		"""No Description

		Returns
		--------
			``IAlternativeRecord`` : 
		"""
		pass

	@property
	def AlternativeType(self) -> IAlternativeType:
		"""No Description

		Returns
		--------
			``IDomainElementField`` : 
		"""
		pass

	@property
	def DomainElementType(self) -> IDomainElementType:
		"""No Description

		Returns
		--------
			``IDomainElementField`` : 
		"""
		pass

	@property
	def OwnerDomainElementType(self) -> IDomainElementType:
		"""No Description

		Returns
		--------
			``IDomainElementField`` : 
		"""
		pass

class IEditDomainElementField(IEditField):

	def __init__(self) -> None:
		"""Creating a new Instance of this class is not allowed


		Raises
		--------
			Exception: if this class is instantiated
		"""
		raise Exception("Creating a new Instance of this class is not allowed")
		pass

	@overload
	def SetValue(self, elementID: int, makeLocal: bool, newValue: object) -> None:
		"""No Description

		Args
		--------
			elementID (``int``) :  elementID
			makeLocal (``bool``) :  makeLocal
			newValue (``object``) :  newValue

		Returns
		--------
			``None`` : 
		"""
		pass

	@overload
	def SetValue(self, id: int, value: object) -> None:
		"""No Description

		Args
		--------
			id (``int``) :  id
			value (``object``) :  value

		Returns
		--------
			``None`` : 
		"""
		pass

class ISystemRecordField(IField):

	def __init__(self) -> None:
		"""Creating a new Instance of this class is not allowed


		Raises
		--------
			Exception: if this class is instantiated
		"""
		raise Exception("Creating a new Instance of this class is not allowed")
		pass

	@property
	def AlternativeType(self) -> IAlternativeType:
		"""No Description

		Returns
		--------
			``ISystemRecordField`` : 
		"""
		pass

class IAlternativeField(IDomainElementField):

	def __init__(self) -> None:
		"""Creating a new Instance of this class is not allowed


		Raises
		--------
			Exception: if this class is instantiated
		"""
		raise Exception("Creating a new Instance of this class is not allowed")
		pass

	@property
	def ActiveAlternativeID(self) -> int:
		"""No Description

		Returns
		--------
			``IAlternativeField`` : 
		"""
		pass

	@ActiveAlternativeID.setter
	def ActiveAlternativeID(self, activealternativeid: int) -> None:
		pass

class ICollectionFieldListManager(IOrderedListManager):

	def __init__(self) -> None:
		"""Creating a new Instance of this class is not allowed


		Raises
		--------
			Exception: if this class is instantiated
		"""
		raise Exception("Creating a new Instance of this class is not allowed")
		pass

	def Field(self, name: str) -> IField:
		"""No Description

		Args
		--------
			name (``str``) :  name

		Returns
		--------
			``IField`` : 
		"""
		pass

	def Clear(self) -> None:
		"""No Description

		Returns
		--------
			``None`` : 
		"""
		pass

class ICrossElementFieldListManager(ICollectionFieldListManager):

	def __init__(self) -> None:
		"""Creating a new Instance of this class is not allowed


		Raises
		--------
			Exception: if this class is instantiated
		"""
		raise Exception("Creating a new Instance of this class is not allowed")
		pass

	@overload
	def Delete(self, indices: HmIDCollection) -> None:
		"""No Description

		Args
		--------
			indices (``HmIDCollection``) :  indices

		Returns
		--------
			``None`` : 
		"""
		pass

	def Reload(self, sortContexts: SortContextCollection, filterContexts: FilterContextCollection) -> None:
		"""No Description

		Args
		--------
			sortContexts (``SortContextCollection``) :  sortContexts
			filterContexts (``FilterContextCollection``) :  filterContexts

		Returns
		--------
			``None`` : 
		"""
		pass

	@overload
	def Delete(self, id: int) -> None:
		"""No Description

		Args
		--------
			id (``int``) :  id

		Returns
		--------
			``None`` : 
		"""
		pass

	@property
	def ActiveElementID(self) -> int:
		"""No Description

		Returns
		--------
			``ICrossElementFieldListManager`` : 
		"""
		pass

	@ActiveElementID.setter
	def ActiveElementID(self, activeelementid: int) -> None:
		pass

	@property
	def ActiveSortContexts(self) -> SortContextCollection:
		"""No Description

		Returns
		--------
			``ICrossElementFieldListManager`` : 
		"""
		pass

	@property
	def ActiveFilterContexts(self) -> FilterContextCollection:
		"""No Description

		Returns
		--------
			``ICrossElementFieldListManager`` : 
		"""
		pass

class IAlternativeCrossElementFieldListManager(ICrossElementFieldListManager):

	def __init__(self) -> None:
		"""Creating a new Instance of this class is not allowed


		Raises
		--------
			Exception: if this class is instantiated
		"""
		raise Exception("Creating a new Instance of this class is not allowed")
		pass

	@overload
	def Reload(self, alternativeID: int, sortContexts: SortContextCollection, filterContexts: FilterContextCollection) -> None:
		"""No Description

		Args
		--------
			alternativeID (``int``) :  alternativeID
			sortContexts (``SortContextCollection``) :  sortContexts
			filterContexts (``FilterContextCollection``) :  filterContexts

		Returns
		--------
			``None`` : 
		"""
		pass

	@overload
	def Reload(self, sortContexts: SortContextCollection, filterContexts: FilterContextCollection) -> None:
		"""No Description

		Args
		--------
			sortContexts (``SortContextCollection``) :  sortContexts
			filterContexts (``FilterContextCollection``) :  filterContexts

		Returns
		--------
			``None`` : 
		"""
		pass

	@property
	def ActiveAlternativeID(self) -> int:
		"""No Description

		Returns
		--------
			``IAlternativeCrossElementFieldListManager`` : 
		"""
		pass

class ISelectableManager:

	def __init__(self) -> None:
		"""Creating a new Instance of this class is not allowed


		Raises
		--------
			Exception: if this class is instantiated
		"""
		raise Exception("Creating a new Instance of this class is not allowed")
		pass

	def SelectElementIDs(self, sortContextCollection: SortContextCollection, filterContextCollection: FilterContextCollection) -> IHmIDDelayedCollection:
		"""No Description

		Args
		--------
			sortContextCollection (``SortContextCollection``) :  sortContextCollection
			filterContextCollection (``FilterContextCollection``) :  filterContextCollection

		Returns
		--------
			``IHmIDDelayedCollection`` : 
		"""
		pass

	def Validate(self, filterContextCollection: FilterContextCollection) -> None:
		"""No Description

		Args
		--------
			filterContextCollection (``FilterContextCollection``) :  filterContextCollection

		Returns
		--------
			``None`` : 
		"""
		pass

	def GetDataReader(self, queryName: str, fields: FieldTypeCollection, parametersMap: Dict) -> IFieldCollectionDataReader:
		"""No Description

		Args
		--------
			queryName (``str``) :  queryName
			fields (``FieldTypeCollection``) :  fields
			parametersMap (``Dict``) :  parametersMap

		Returns
		--------
			``IFieldCollectionDataReader`` : 
		"""
		pass

class ISelectableManagerEx:

	def __init__(self) -> None:
		"""Creating a new Instance of this class is not allowed


		Raises
		--------
			Exception: if this class is instantiated
		"""
		raise Exception("Creating a new Instance of this class is not allowed")
		pass

	def GetDataReader(self, queryName: str, fields: FieldTypeCollection, parametersMap: Dict) -> IDisposableEnumerable:
		"""No Description

		Args
		--------
			queryName (``str``) :  queryName
			fields (``FieldTypeCollection``) :  fields
			parametersMap (``Dict``) :  parametersMap

		Returns
		--------
			``IDisposableEnumerable`` : 
		"""
		pass

class IEnumeratorDataAccessor:

	def __init__(self) -> None:
		"""Creating a new Instance of this class is not allowed


		Raises
		--------
			Exception: if this class is instantiated
		"""
		raise Exception("Creating a new Instance of this class is not allowed")
		pass

	def GetElementID(self) -> int:
		"""No Description

		Returns
		--------
			``int`` : 
		"""
		pass

	def GetNullableInt32(self, fieldIndex: int) -> Union[int, None]:
		"""No Description

		Args
		--------
			fieldIndex (``int``) :  fieldIndex

		Returns
		--------
			``Nullable`` : 
		"""
		pass

	def GetInt32(self, fieldIndex: int) -> int:
		"""No Description

		Args
		--------
			fieldIndex (``int``) :  fieldIndex

		Returns
		--------
			``int`` : 
		"""
		pass

	def GetDouble(self, fieldIndex: int, unitIndex: UnitIndex) -> float:
		"""No Description

		Args
		--------
			fieldIndex (``int``) :  fieldIndex
			unitIndex (``UnitIndex``) :  unitIndex

		Returns
		--------
			``float`` : 
		"""
		pass

	def GetBoolean(self, fieldIndex: int) -> bool:
		"""No Description

		Args
		--------
			fieldIndex (``int``) :  fieldIndex

		Returns
		--------
			``bool`` : 
		"""
		pass

	def GetDateTime(self, fieldIndex: int) -> datetime:
		"""No Description

		Args
		--------
			fieldIndex (``int``) :  fieldIndex

		Returns
		--------
			``datetime`` : 
		"""
		pass

	def GetString(self, fieldIndex: int) -> str:
		"""No Description

		Args
		--------
			fieldIndex (``int``) :  fieldIndex

		Returns
		--------
			``str`` : 
		"""
		pass

	def GetBlob(self, fieldIndex: int) -> List[int]:
		"""No Description

		Args
		--------
			fieldIndex (``int``) :  fieldIndex

		Returns
		--------
			``List[int]`` : 
		"""
		pass

	@property
	def FieldTypes(self) -> List[IFieldType]:
		"""No Description

		Returns
		--------
			``IEnumeratorDataAccessor`` : 
		"""
		pass

class IDisposableEnumerable(Generic[T], Iterator[T]):

	def __init__(self) -> None:
		"""Creating a new Instance of this class is not allowed


		Raises
		--------
			Exception: if this class is instantiated
		"""
		raise Exception("Creating a new Instance of this class is not allowed")
		pass

class IAlternativeRecordEx:

	def __init__(self) -> None:
		"""Creating a new Instance of this class is not allowed


		Raises
		--------
			Exception: if this class is instantiated
		"""
		raise Exception("Creating a new Instance of this class is not allowed")
		pass

	@overload
	def GetDataReader(self, fieldTypeNames: array[str], filterContexts: FilterContextCollection, sortContexts: SortContextCollection) -> IDisposableEnumerable:
		"""No Description

		Args
		--------
			fieldTypeNames (``array[str]``) :  fieldTypeNames
			filterContexts (``FilterContextCollection``) :  filterContexts
			sortContexts (``SortContextCollection``) :  sortContexts

		Returns
		--------
			``IDisposableEnumerable`` : 
		"""
		pass

	@overload
	def GetDataReader(self, fieldTypeNames: array[str], domainElementTypeID: int) -> IAlternativeRecordDataReader:
		"""No Description

		Args
		--------
			fieldTypeNames (``array[str]``) :  fieldTypeNames
			domainElementTypeID (``int``) :  domainElementTypeID

		Returns
		--------
			``IAlternativeRecordDataReader`` : 
		"""
		pass

class IHmIDDelayedCollection(ICloneable, List):

	def __init__(self) -> None:
		"""Creating a new Instance of this class is not allowed


		Raises
		--------
			Exception: if this class is instantiated
		"""
		raise Exception("Creating a new Instance of this class is not allowed")
		pass

	def Add(self, item: int) -> int:
		"""No Description

		Args
		--------
			item (``int``) :  item

		Returns
		--------
			``int`` : 
		"""
		pass

	def Contains(self, item: int) -> bool:
		"""No Description

		Args
		--------
			item (``int``) :  item

		Returns
		--------
			``bool`` : 
		"""
		pass

	def IndexOf(self, item: int) -> int:
		"""No Description

		Args
		--------
			item (``int``) :  item

		Returns
		--------
			``int`` : 
		"""
		pass

	def Sort(self) -> None:
		"""No Description

		Returns
		--------
			``None`` : 
		"""
		pass

	def Remove(self, item: int) -> None:
		"""No Description

		Args
		--------
			item (``int``) :  item

		Returns
		--------
			``None`` : 
		"""
		pass

	@property
	def Item(self) -> int:
		"""No Description

		Returns
		--------
			``IHmIDDelayedCollection`` : 
		"""
		pass

	@Item.setter
	def Item(self, item: int) -> None:
		pass

class IUpdatedFieldInformation:

	def __init__(self) -> None:
		"""Creating a new Instance of this class is not allowed


		Raises
		--------
			Exception: if this class is instantiated
		"""
		raise Exception("Creating a new Instance of this class is not allowed")
		pass

	@property
	def OldFieldName(self) -> str:
		"""No Description

		Returns
		--------
			``IUpdatedFieldInformation`` : 
		"""
		pass

	@property
	def NewFieldName(self) -> str:
		"""No Description

		Returns
		--------
			``IUpdatedFieldInformation`` : 
		"""
		pass

	@property
	def NewSource(self) -> str:
		"""No Description

		Returns
		--------
			``IUpdatedFieldInformation`` : 
		"""
		pass

	@property
	def FieldUpdateType(self) -> FieldUpdateTypeEnum:
		"""No Description

		Returns
		--------
			``IUpdatedFieldInformation`` : 
		"""
		pass

	@property
	def IsResultField(self) -> bool:
		"""No Description

		Returns
		--------
			``IUpdatedFieldInformation`` : 
		"""
		pass

class IEngineeringLibrary(IEditLabeled, ITreeElementManager):

	def __init__(self) -> None:
		"""Creating a new Instance of this class is not allowed


		Raises
		--------
			Exception: if this class is instantiated
		"""
		raise Exception("Creating a new Instance of this class is not allowed")
		pass

	@overload
	def Exists(self, guid: Guid) -> bool:
		"""No Description

		Args
		--------
			guid (``Guid``) :  guid

		Returns
		--------
			``bool`` : 
		"""
		pass

	def IsSourceAvailable(self) -> bool:
		"""No Description

		Returns
		--------
			``bool`` : 
		"""
		pass

	def EngineeringLibraryField(self, fieldName: str) -> IField:
		"""No Description

		Args
		--------
			fieldName (``str``) :  fieldName

		Returns
		--------
			``IField`` : 
		"""
		pass

	def GetEngineeringObject(self, aguid: Guid) -> IEngineeringReference:
		"""No Description

		Args
		--------
			aguid (``Guid``) :  aguid

		Returns
		--------
			``IEngineeringReference`` : 
		"""
		pass

	def AddFolder(self) -> int:
		"""No Description

		Returns
		--------
			``int`` : 
		"""
		pass

	def Commit(self) -> None:
		"""No Description

		Returns
		--------
			``None`` : 
		"""
		pass

	def Close(self, allowPrompts: bool) -> None:
		"""No Description

		Args
		--------
			allowPrompts (``bool``) :  allowPrompts

		Returns
		--------
			``None`` : 
		"""
		pass

	def ForceCheckIfAvailable(self) -> bool:
		"""No Description

		Returns
		--------
			``bool`` : 
		"""
		pass

	def GetSourceEngineeringLibraryTypeName(self) -> str:
		"""No Description

		Returns
		--------
			``str`` : 
		"""
		pass

	@overload
	def Exists(self, id: int) -> bool:
		"""No Description

		Args
		--------
			id (``int``) :  id

		Returns
		--------
			``bool`` : 
		"""
		pass

	@property
	def Guid(self) -> Guid:
		"""No Description

		Returns
		--------
			``IEngineeringLibrary`` : 
		"""
		pass

	@property
	def Source(self) -> str:
		"""No Description

		Returns
		--------
			``IEngineeringLibrary`` : 
		"""
		pass

	@Source.setter
	def Source(self, source: str) -> None:
		pass

	@property
	def Notes(self) -> str:
		"""No Description

		Returns
		--------
			``IEngineeringLibrary`` : 
		"""
		pass

	@Notes.setter
	def Notes(self, notes: str) -> None:
		pass

	@property
	def EngineeringLibraryTypeName(self) -> str:
		"""No Description

		Returns
		--------
			``IEngineeringLibrary`` : 
		"""
		pass

	@property
	def DateModified(self) -> datetime:
		"""No Description

		Returns
		--------
			``IEngineeringLibrary`` : 
		"""
		pass

	@property
	def IsEditable(self) -> bool:
		"""No Description

		Returns
		--------
			``IEngineeringLibrary`` : 
		"""
		pass

	@property
	def IsEnumerable(self) -> bool:
		"""No Description

		Returns
		--------
			``IEngineeringLibrary`` : 
		"""
		pass

	@property
	def IsInProjectWise(self) -> bool:
		"""No Description

		Returns
		--------
			``IEngineeringLibrary`` : 
		"""
		pass

class IEngineeringLibraryEx:

	def __init__(self) -> None:
		"""Creating a new Instance of this class is not allowed


		Raises
		--------
			Exception: if this class is instantiated
		"""
		raise Exception("Creating a new Instance of this class is not allowed")
		pass

	def GetPersistedGuid(self) -> Guid:
		"""No Description

		Returns
		--------
			``Guid`` : 
		"""
		pass

class IEngineeringReference(ITreeElement):

	def __init__(self) -> None:
		"""Creating a new Instance of this class is not allowed


		Raises
		--------
			Exception: if this class is instantiated
		"""
		raise Exception("Creating a new Instance of this class is not allowed")
		pass

	def EngineeringReferenceField(self, fieldName: str) -> IField:
		"""No Description

		Args
		--------
			fieldName (``str``) :  fieldName

		Returns
		--------
			``IField`` : 
		"""
		pass

	def SynchronizeFrom(self, supportElement: ISupportElement) -> None:
		"""No Description

		Args
		--------
			supportElement (``ISupportElement``) :  supportElement

		Returns
		--------
			``None`` : 
		"""
		pass

	@property
	def Guid(self) -> Guid:
		"""No Description

		Returns
		--------
			``IEngineeringReference`` : 
		"""
		pass

	@property
	def DateModified(self) -> datetime:
		"""No Description

		Returns
		--------
			``IEngineeringReference`` : 
		"""
		pass

	@property
	def EngineeringLibrary(self) -> IEngineeringLibrary:
		"""No Description

		Returns
		--------
			``IEngineeringReference`` : 
		"""
		pass

class IBlobable:

	def __init__(self) -> None:
		"""Creating a new Instance of this class is not allowed


		Raises
		--------
			Exception: if this class is instantiated
		"""
		raise Exception("Creating a new Instance of this class is not allowed")
		pass

	def GetBytes(self) -> List[int]:
		"""No Description

		Returns
		--------
			``List[int]`` : 
		"""
		pass

	def GetNumberOfBytes(self) -> int:
		"""No Description

		Returns
		--------
			``int`` : 
		"""
		pass

class IAlternativeTypeCollectionEnumerator:

	def __init__(self) -> None:
		"""Creating a new Instance of this class is not allowed


		Raises
		--------
			Exception: if this class is instantiated
		"""
		raise Exception("Creating a new Instance of this class is not allowed")
		pass

	def MoveNext(self) -> bool:
		"""No Description

		Returns
		--------
			``bool`` : 
		"""
		pass

	def Reset(self) -> None:
		"""No Description

		Returns
		--------
			``None`` : 
		"""
		pass

	@property
	def Current(self) -> IAlternativeType:
		"""No Description

		Returns
		--------
			``IAlternativeTypeCollectionEnumerator`` : 
		"""
		pass

class IFieldTypeCollectionEnumerator:

	def __init__(self) -> None:
		"""Creating a new Instance of this class is not allowed


		Raises
		--------
			Exception: if this class is instantiated
		"""
		raise Exception("Creating a new Instance of this class is not allowed")
		pass

	def MoveNext(self) -> bool:
		"""No Description

		Returns
		--------
			``bool`` : 
		"""
		pass

	def Reset(self) -> None:
		"""No Description

		Returns
		--------
			``None`` : 
		"""
		pass

	@property
	def Current(self) -> IFieldType:
		"""No Description

		Returns
		--------
			``IFieldTypeCollectionEnumerator`` : 
		"""
		pass

class IDomainDataSetCollectionEnumerator:

	def __init__(self) -> None:
		"""Creating a new Instance of this class is not allowed


		Raises
		--------
			Exception: if this class is instantiated
		"""
		raise Exception("Creating a new Instance of this class is not allowed")
		pass

	def MoveNext(self) -> bool:
		"""No Description

		Returns
		--------
			``bool`` : 
		"""
		pass

	def Reset(self) -> None:
		"""No Description

		Returns
		--------
			``None`` : 
		"""
		pass

	@property
	def Current(self) -> IDomainDataSet:
		"""No Description

		Returns
		--------
			``IDomainDataSetCollectionEnumerator`` : 
		"""
		pass

class IDomainDataSetTypeCollectionEnumerator:

	def __init__(self) -> None:
		"""Creating a new Instance of this class is not allowed


		Raises
		--------
			Exception: if this class is instantiated
		"""
		raise Exception("Creating a new Instance of this class is not allowed")
		pass

	def MoveNext(self) -> bool:
		"""No Description

		Returns
		--------
			``bool`` : 
		"""
		pass

	def Reset(self) -> None:
		"""No Description

		Returns
		--------
			``None`` : 
		"""
		pass

	@property
	def Current(self) -> IDomainDataSetType:
		"""No Description

		Returns
		--------
			``IDomainDataSetTypeCollectionEnumerator`` : 
		"""
		pass

class IDomainElementTypeCollectionEnumerator:

	def __init__(self) -> None:
		"""Creating a new Instance of this class is not allowed


		Raises
		--------
			Exception: if this class is instantiated
		"""
		raise Exception("Creating a new Instance of this class is not allowed")
		pass

	def MoveNext(self) -> bool:
		"""No Description

		Returns
		--------
			``bool`` : 
		"""
		pass

	def Reset(self) -> None:
		"""No Description

		Returns
		--------
			``None`` : 
		"""
		pass

	@property
	def Current(self) -> IDomainElementType:
		"""No Description

		Returns
		--------
			``IDomainElementTypeCollectionEnumerator`` : 
		"""
		pass

class IModelingElementCollectionEnumerator:

	def __init__(self) -> None:
		"""Creating a new Instance of this class is not allowed


		Raises
		--------
			Exception: if this class is instantiated
		"""
		raise Exception("Creating a new Instance of this class is not allowed")
		pass

	def MoveNext(self) -> bool:
		"""No Description

		Returns
		--------
			``bool`` : 
		"""
		pass

	def Reset(self) -> None:
		"""No Description

		Returns
		--------
			``None`` : 
		"""
		pass

	@property
	def Current(self) -> IModelingElement:
		"""No Description

		Returns
		--------
			``IModelingElementCollectionEnumerator`` : 
		"""
		pass

class INumericalEngineTypeCollectionEnumerator:

	def __init__(self) -> None:
		"""Creating a new Instance of this class is not allowed


		Raises
		--------
			Exception: if this class is instantiated
		"""
		raise Exception("Creating a new Instance of this class is not allowed")
		pass

	def MoveNext(self) -> bool:
		"""No Description

		Returns
		--------
			``bool`` : 
		"""
		pass

	def Reset(self) -> None:
		"""No Description

		Returns
		--------
			``None`` : 
		"""
		pass

	@property
	def Current(self) -> INumericalEngineType:
		"""No Description

		Returns
		--------
			``INumericalEngineTypeCollectionEnumerator`` : 
		"""
		pass

class IResultRecordCollectionEnumerator:

	def __init__(self) -> None:
		"""Creating a new Instance of this class is not allowed


		Raises
		--------
			Exception: if this class is instantiated
		"""
		raise Exception("Creating a new Instance of this class is not allowed")
		pass

	def MoveNext(self) -> bool:
		"""No Description

		Returns
		--------
			``bool`` : 
		"""
		pass

	def Reset(self) -> None:
		"""No Description

		Returns
		--------
			``None`` : 
		"""
		pass

	@property
	def Current(self) -> IResultRecord:
		"""No Description

		Returns
		--------
			``IResultRecordCollectionEnumerator`` : 
		"""
		pass

class IResultRecordTypeCollectionEnumerator:

	def __init__(self) -> None:
		"""Creating a new Instance of this class is not allowed


		Raises
		--------
			Exception: if this class is instantiated
		"""
		raise Exception("Creating a new Instance of this class is not allowed")
		pass

	def MoveNext(self) -> bool:
		"""No Description

		Returns
		--------
			``bool`` : 
		"""
		pass

	def Reset(self) -> None:
		"""No Description

		Returns
		--------
			``None`` : 
		"""
		pass

	@property
	def Current(self) -> IResultRecordType:
		"""No Description

		Returns
		--------
			``IResultRecordTypeCollectionEnumerator`` : 
		"""
		pass

class ISupportElementTypeCollectionEnumerator:

	def __init__(self) -> None:
		"""Creating a new Instance of this class is not allowed


		Raises
		--------
			Exception: if this class is instantiated
		"""
		raise Exception("Creating a new Instance of this class is not allowed")
		pass

	def MoveNext(self) -> bool:
		"""No Description

		Returns
		--------
			``bool`` : 
		"""
		pass

	def Reset(self) -> None:
		"""No Description

		Returns
		--------
			``None`` : 
		"""
		pass

	@property
	def Current(self) -> ISupportElementType:
		"""No Description

		Returns
		--------
			``ISupportElementTypeCollectionEnumerator`` : 
		"""
		pass

