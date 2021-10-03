from enum import Enum

class FormatCode(Enum):
	Fixed = 0
	General = 1
	ScientificNotation = 2
	Number = 3

class UnitSystemType(Enum):
	USCustomary = 0
	SI = 1

class LicenseRunStatusEnum(Enum):
	OK = 1001
	Limited = 1002
	Shutdown = 1003
	Unknown = -1

class ProductId(Enum):
	MicroStation = 1000
	Bentley_Redline = 1146
	Bentley_CivilStorm = 1207
	Bentley_CulvertMaster = 1210
	Bentley_Calibrator = 1211
	Bentley_Designer = 1212
	Bentley_FlowMaster = 1222
	Bentley_GISConnect = 1223
	Bentley_HEC_Pack = 1224
	Bentley_HAMMER = 1225
	Bentley_PondPack = 1233
	Bentley_SCADAConnect = 1239
	Bentley_SewerCAD = 1243
	Bentley_SewerGEMS = 1244
	Bentley_Skelebrator = 1245
	Bentley_StormCAD = 1246
	Bentley_WaterCAD = 1248
	Bentley_WaterGEMS = 1249
	Bentley_WaterSAFE = 1250
	Bentley_Scheduler = 1860
	Bentley_GasAnalysis = 1861
	Bentley_PipeAssetPlanner = 1895
	Bentley_SUE = 2335
	Bentley_OpenRoadsDesigner = 2515
	Bentley_OpenRailDesigner = 2641
	Bentley_CNCCBIMOpenRoads = 2697
	Bentley_OpenSiteDesigner = 2758
	Bentley_WaterOPS = 2922
	Bentley_SewerOPS = 2923
	Bentley_OverHeadLineDesigner = 2963
	Bentley_OpenRailChina = 3136
	Bentley_OpenRailUltimateChina = 3210
	Bentley_OpenRoadsUltimateChina = 3211
	Bentley_OpenRoadsChina = 3216

class LicenseStatus(Enum):
	OK = 101
	Offline = 102
	PreActivation = 104
	Expired = 105
	AccessDenied = 106
	DisabledByLogSend = 107
	DisabledByPolicy = 108
	Trial = 109
	NotEntitled = 110
	Unknown = -999
	Error = -1

class ModelElementType(Enum):
	All = 0
	Scenario = 2
	NetworkElement = 3
	ComponentElement = 4
	Options = 5
	SelectionSet = 6

class ModelingElementTypes(Enum):
	Scenario = 2
	SelectionSet = 7

class DomainFieldType(Enum):
	ModelingElementField = 1
	SupportElementField = 2
	DomainElementField = 3
	ResultField = 4
	AlternativeField = 5
	SystemRecordField = 6

class FieldDataType(Enum):
	Integer = 1
	Real = 2
	Text = 3
	LongText = 4
	DateTime = 5
	Boolean = 6
	LongBinary = 7
	Referenced = 8
	Collection = 9
	Enumerated = 10

class UserFieldDataType(Enum):
	Integer = 1
	Real = 2
	LongText = 4
	DateTime = 5
	Boolean = 6

class ElementStateType(Enum):
	All = 0
	Active = 1
	Inactive = 2

