from enum import Enum
from System import TypeCode
from OpenFlows.Domain.DataObjects import IModel, IModelElementManager, IModelIOOperations, IModelScenarioManagement, IDomainModel, IModelSelectionSetManagement
from OpenFlows.Water.Units import INetworkElementUnits, IComponentElementUnits
from OpenFlows.Water.Domain.ModelingElements.NetworkElements import IWaterNetwork, IWaterElement
from OpenFlows.Water.Domain.ModelingElements.Components import IWaterModelSupport, IWaterComponent
from OpenFlows.Water.Domain.ModelingElements import IWaterScenarios, IWaterScenario, IWaterSelectionSets, IWaterSelectionSet
from OpenFlows.Water.Domain.ModelingElements.CalculationOptions import IWaterScenarioOptions, IWaterScenarioOptionsUnits
from OpenFlows.Units import IModelUnits
from OpenFlows.Water.Analysis import IAnalysisTools

class CalculationType(Enum):
	FIREFLOW = 0
	FLUSHING = 1
	AGE = 2
	CONSTITUENT = 3
	TRACE = 4
	HYDRAULICSONLY = 5
	MSX = 6
	SCADACONNECTANALYSIS = 7
	WATERQUALITY = 8

class DemandAdjustmentsType(Enum):
	NONE = 0
	ACTIVE = 1

class UnitDemandAdjustmentType(Enum):
	NONE = 0
	ACTIVE = 1

class RoughnessAdjustmentType(Enum):
	NONE = 0
	ACTIVE = 1

class AdjustmentOperationType(Enum):
	ADD = 0
	SUBTRACE = 1
	MULTIPLY = 2
	DIVIDE = 3
	SET = 4

class ConstituentSourceType(Enum):
	CONCENTRATION = 0
	FLOWPACEDBOOSTER = 1
	SETPOINTBOOSTER = 2
	MASSBOOSTER = 3

class PipeStatusType(Enum):
	OPEN = 0
	CLOSED = 1

class ValveSettingType(Enum):
	ACTIVE = 0
	INACTIVE = 1
	CLOSED = 2

class TCVCoefficientType(Enum):
	HEADLOSS = 1
	DISCHARGE = 2
	VALVECHARACTERISTICS = 3

class PressureValvesettingType(Enum):
	VALVEPRESSURE = 0
	VALVEHGL = 1

class TankSectionType(Enum):
	CIRCULAR = 0
	NONCIRCULAR = 1
	VARIABLEAREA = 2

class IWaterModel(IModel[IWaterNetwork, IWaterModelSupport, IWaterScenarios, IWaterScenario, IWaterScenarioOptions, IWaterScenarioOptionsUnits, IWaterSelectionSets, IWaterSelectionSet, IWaterElement, IWaterElement, WaterNetworkElementType, IWaterComponent, WaterComponentType, INetworkElementUnits, IComponentElementUnits]):

	def __init__(self) -> None:
		"""Creating a new Instance of this class is not allowed


		Raises
		--------
			Exception: if this class is instantiated
		"""
		raise Exception("Creating a new Instance of this class is not allowed")
		pass

	@property
	def AnalysisTools(self) -> IAnalysisTools:
		"""Analysis tools available in OpenFlows

		Returns
		--------
			``IWaterModel`` : 
		"""
		pass

