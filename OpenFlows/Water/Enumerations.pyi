from enum import Enum

class WaterNetworkElementType(Enum):
	SCADAElement = 23
	Lateral = 24
	Tap = 26
	Tank = 52
	Hydrant = 54
	Junction = 55
	Reservoir = 56
	FCV = 60
	TCV = 61
	GPV = 62
	PRV = 64
	PSV = 65
	PBV = 66
	Pump = 68
	Pipe = 69
	SpotElevation = 70
	IsolationValve = 71
	VSPB = 72
	CustomerMeter = 73
	Turbine = 300
	AirValve = 301
	HydropneumaticTank = 302
	SurgeValve = 303
	DischargeToAtmosphere = 305
	RuptureDisk = 306
	OrificeBetweenTwoPipes = 307
	SurgeTank = 308
	CheckValve = 309
	ValveWithLinearAreaChange = 310
	PeriodicHeadFlow = 321
	PumpStation = 700

class WaterComponentType(Enum):
	Pattern = 50
	PumpDefinition = 51
	Constituent = 52
	Zone = 53
	Control = 54
	ControlAction = 55
	ControlCondition = 56
	ControlSet = 59
	PDD = 60
	EnergyPrice = 61
	UnitDemandLoad = 62
	GPVHeadloss = 63
	ValveCharacteristic = 66
	AirFlowCurve = 68
	MinorLoss = 101
	UnitCarbonEmission = 202
	PowerMeter = 203
	MSXSetup = 220
	SCADASignal = 257

class ControlTypeEnum(Enum):
	LogicalType = 0
	SimpleType = 1

class ControlPriorityEnum(Enum):
	PriorityDefaultType = 0
	Priority1Type = 1
	Priority2Type = 2
	Priority3Type = 3
	Priority4Type = 4
	Priority5Type = 5

class ConditionTypeEnum(Enum):
	SimpleConditionType = 0
	CompositeConditionType = 1

class SimpleConditionType(Enum):
	Element = 0
	SystemDemand = 1
	ClockTime = 2
	TimeFromStart = 3

class ConditionComparisonOperator(Enum):
	Equals = 0
	GreaterThan = 1
	GreaterThanEqual = 2
	LessThan = 3
	LessThanEQual = 4
	NotEQual = 5

class NodeAttributeEnum(Enum):
	NodeDemandType = 0
	NodeHydraulicGradeType = 1
	NodePressureType = 2

class TankAttributeEnum(Enum):
	TankDemandType = 0
	TankHydraulicGradeType = 1
	TankPressureType = 2
	TankLevelType = 3
	TankTimeToDrainType = 4
	TankTimeToFillType = 5
	TankPercentFullType = 6

class ControlConditionPumpAttribute(Enum):
	PumpDischarge = 0
	ConditionPumpSetting = 1
	ConditionPumpStatus = 2

class PumpStatus(Enum):
	PumpOn = 0
	PumpOff = 1

class ControlConditionPipeAttribute(Enum):
	PipeDischarge = 0
	ConditionPipeStatus = 1

class PipeStatus(Enum):
	Open = 0
	Closed = 1

class ControlConditionPressureValveAttributeEnum(Enum):
	PressureValveDischargeType = 0
	PressureValveSettingType = 1
	PressureValveStatusType = 2

class ControlConditionValveStatus(Enum):
	Closed = 0
	Inactive = 1

class ControlConditionFCVAttributeEnum(Enum):
	FCVDischargeType = 0
	FCVSettingType = 1
	FCVStatusType = 2

class FCVStatusEnum(Enum):
	ClosedType = 0
	InactiveType = 1

class ControlConditionGPVAttributeEnum(Enum):
	GPVDischargeType = 0
	GPVStatusType = 1

class ControlConditionGPVStatusEnum(Enum):
	ClosedType = 0
	ActiveType = 1

class ControlConditionTCVAttributeEnum(Enum):
	TCVDischargeType = 0
	TCVSettingType = 1
	TCVStatusType = 2

class TCVStatusEnum(Enum):
	ClosedType = 0
	InactiveType = 1

class HydroTankAttributeEnum(Enum):
	HydroTankHydraulicGradeType = 1
	HydroTankPressureType = 2

class SurgeTankAttributeEnum(Enum):
	SurgeTankDemandType = 0
	SurgeTankHydraulicGradeType = 1
	SurgeTankPressureType = 2

class LogicalOperatorEnum(Enum):
	OperatorIfType = 0
	OperatorAndType = 1
	OperatorOrType = 2

class ControlActionTypeEnum(Enum):
	SimpleActionType = 0
	CompositeActionType = 1

class ControlActionPipeAttribute(Enum):
	PipeStatus = 0

class ControlActionPipeStatus(Enum):
	Open = 0
	Closed = 1

class ControlActionPumpAttribute(Enum):
	PumpStatus = 0
	PumpSetting = 1
	PumpPressureSetting = 2
	PumpHeadSetting = 3

class ControlActionPumpStatus(Enum):
	On = 0
	Off = 1

class ControlActionTCVAttribute(Enum):
	TCVStatus = 0
	TCVSetting = 1

class ControlActionTCVStatus(Enum):
	Closed = 0
	Inactive = 1

class ControlActionGPVAttribute(Enum):
	GPVStatus = 0

class ControlActionGPVStatus(Enum):
	Closed = 0
	Active = 1

class ControlActionFCVAttribute(Enum):
	FCVSetting = 0
	FCVStatus = 1

class ControlActionFCVStatus(Enum):
	Closed = 0
	Inactive = 1

class ControlActionPressureValveAttribute(Enum):
	PressureValveSettingHydraulicGrade = 0
	PressureValveStatus = 1
	PressureValveSettingPressure = 2

class ControlActionPressureValveStatus(Enum):
	Closed = 0
	Inactive = 1

class PatternCategory(Enum):
	PatternCategoryHydraulic = 0
	PatternCategoryConstituent = 1
	PatternCategoryReservoir = 2
	PatternCategoryPump = 3
	PatternCategoryOperationalValve = 4
	PatternCategoryOperationalPump = 5
	PatternCategoryOperationalTurbine = 6
	PatternCategoryValve = 7
	PatternCategoryValveRelativeClosure = 8
	PatternCategoryPowerUsage = 9

class PatternFormat(Enum):
	Stepwise = 0
	Continuous = 1

class PumpDefinitionType(Enum):
	ConstantPower = 0
	DesignPoint = 1
	Standard = 2
	StandardExtended = 3
	CustomExtended = 4
	MultiplePoint = 5
	VolumeFlow = 6
	DepthFlow = 7
	DepthFlowVariableSpeed = 8

class PumpEfficiencyTypeEnum(Enum):
	ConstantEfficiencyType = 0
	BestEfficiencyPointType = 1
	MultipleEfficiencyPointsType = 2

class WallReactionOrder(Enum):
	ZeroOrder = 0
	FirstOrder = 1

class UnitDemandLoadTypeEnum(Enum):
	PopulationBasedType = 0
	AreaBasedType = 1
	CountUnitType = 3

class PopulationUnit(Enum):
	Capita = 1
	ThousandCapita = 2
	HundredCapita = 3
	Customer = 4
	Employee = 5
	Passenger = 6
	Person = 7
	Guest = 8
	Resident = 9
	Student = 10

class AreaUnit(Enum):
	SquareMillimeters = 1
	SquareCentimeters = 2
	SquareMeters = 3
	Hectares = 4
	SquareKilometers = 5
	SquareInches = 6
	SquareFeet = 7
	ThousandSquareFeet = 8
	SquareYards = 9
	Acres = 10
	SquareMiles = 11

class SCADASignalTransformMethod(Enum):
	Threshold = 0
	Range = 1
	Formula = 2

class MinorLossTypeEnum(Enum):
	EntranceType = 0
	BendType = 1
	ContractionType = 2
	CrossType = 3
	ExitType = 4
	ExpansionType = 5
	TeeType = 6
	ValveType = 7
	WyeType = 8

class CheckValveFlowDirectionEnum(Enum):
	TowardsWye = 0
	AwayFromWye = 1

class TurbineOperatingCaseEnum(Enum):
	InstantLoadRejection = 0
	LoadRejection = 1
	LoadAcceptance = 2
	LoadVariation = 3

class TurbineStatusEnum(Enum):
	OpenType = 0
	ClosedType = 1

class PumpStatusEnum(Enum):
	PumpOnType = 0
	PumpOffType = 1
	PumpResultCannotDeliverHead = 2
	PumpResultCannotDeliverFlow = 3

class VSPBType(Enum):
	FixedHead = 1
	FixedFlow = 2

class VSPBFixedHeadType(Enum):
	HydraulicGrade = 0
	Pressure = 1

class ValveSettingType(Enum):
	Active = 0
	Inactive = 1
	Closed = 2

class HammerValveType(Enum):
	Butterfly = 0
	Needle = 1
	CircularGate = 2
	Globe = 3
	Ball = 4
	UserDefined = 5

class TCVCoefficientType(Enum):
	Headloss = 1
	Discharge = 2
	ValveCharacteristics = 3

class PressureValvesettingType(Enum):
	ValvePressure = 0
	ValveHGL = 1

class ConstituentSourceType(Enum):
	Concentration = 0
	FlowPacedBooster = 1
	SetpointBooster = 2
	MassBooster = 3

class PipeStatusType(Enum):
	Open = 0
	Closed = 1

class TankSectionType(Enum):
	Circular = 0
	NonCircular = 1
	VariableArea = 2

class SurgeTankTypeEnum(Enum):
	Simple = 0
	Differential = 1

class GasVesselLevelType(Enum):
	Fixed = 0
	Mean = 1
	Variable = 2

class HydroTankType(Enum):
	Sealed = 0
	Vented = 1
	DippingTube = 2

class OperatingRangeTypeEnum(Enum):
	OperatingRange_ElevationType = 0
	OperatingRange_LevelType = 1

class TankCalculationModel(Enum):
	ConstantAreaApproximation = 0
	GasLawModel = 1

class AirFlowCalculationMethod(Enum):
	OrificeDiameter = 0
	AirFlowCurve = 1

class TransientParameterType(Enum):
	Head = 0
	Flow = 1

class AirValveTypeEnum(Enum):
	SlowClosing = 0
	DoubleActing = 1
	TripleActing = 2
	VacuumBreaker = 3

class AirValveTransitionType(Enum):
	ByVolume = 0
	ByPressure = 1

class SAV_SRVTypeEnum(Enum):
	SAV = 0
	SRV = 1
	SAVAndSRV = 2

class SAVValveTypeEnum(Enum):
	Needle = 0
	CircularGate = 1
	Global = 2
	Ball = 3
	Butterfly = 4

class SavClosureTriggerEnum(Enum):
	Time = 0
	Pressure = 1

class SRVControlTypeEnum(Enum):
	SpringLoaded = 0
	TimeBased = 1

class SRVValveTypeEnum(Enum):
	Needle = 0
	CircularGate = 1
	Globe = 2
	Ball = 3
	Butterfly = 4

class DischargeToAtmosphereTypeEnum(Enum):
	Orifice = 0
	Valve = 1
	RatingCurve = 2

class ValveTypeInitialStatusEnum(Enum):
	Open = 1
	Closed = 2

class IsolationValveInitialSetting(Enum):
	IsolationValveOpen = 0
	IsolationValveClosed = 1

class SCADATargetAttribute(Enum):
	UnAssigned = 0
	RelativeClosure = -300
	ConstituentConcentration = -299
	PressureNodeDemand = -297
	ValveStatus = -58
	PumpStatus = -57
	PipeStatus = -56
	TankLevel = -55
	Pressure = -54
	HydraulicGrade = -53
	PumpSetting = -52
	PressureValveSetting = -51
	TCValveSetting = -50
	FCValveSetting = -49
	PressureOut = -48
	PressureIn = -47
	HydraulicGradeOut = -46
	HydraulicGradeIn = -45
	Discharge = -44
	WirePower = -43

class AdjustmentOperationType(Enum):
	Add = 0
	Subtrace = 1
	Multiply = 2
	Divide = 3
	Set = 4

class CalculationType(Enum):
	FireFlow = 0
	Flushing = 1
	Age = 2
	Constituent = 3
	Trace = 4
	HydraulicsOnly = 5
	MSX = 6
	SCADAConnectAnalysis = 7
	WaterQuality = 8

class EpaNetEngine_FrictionMethodEnum(Enum):
	DarcyWeisbachType = 0
	HazenWilliamsType = 1
	ManningsType = 2

class EpaNetEngine_TimeAnalysisTypeEnum(Enum):
	SteadyStateType = 0
	EpsType = 1

class DemandAdjustmentsType(Enum):
	None = 0
	Active = 1

class UnitDemandAdjustmentType(Enum):
	None = 0
	Active = 1

class RoughnessAdjustmentType(Enum):
	None = 0
	Active = 1

