from OpenFlows.Domain.ModelingElements.Collections import ICollectionElements, ICollection, ICollectionElement
from OpenFlows.Domain.ModelingElements import IElementUnits, IScenarioOptions
from OpenFlows.Water.Domain.ModelingElements import IWaterSelectionSet
from OpenFlows.Water.Domain.ModelingElements.Components import IPattern, IUnitDemandLoad
from datetime import datetime
from OpenFlows.Units import IUnit
from OpenFlows.Water.Enumerations import *

class IActiveDemandAdjustmentsCollection(ICollectionElements[IActiveDemandAdjustments, IActiveDemandAdjustment, IElementUnits]):

	def __init__(self) -> None:
		"""Creating a new Instance of this class is not allowed


		Raises:
			Exception: if this class is instanciated
		"""
		raise Exception("Creating a new Instance of this class is not allowed")
		pass

class IActiveDemandAdjustments(ICollection[IActiveDemandAdjustment]):

	def __init__(self) -> None:
		"""Creating a new Instance of this class is not allowed


		Raises:
			Exception: if this class is instanciated
		"""
		raise Exception("Creating a new Instance of this class is not allowed")
		pass

	def Add(self, scope: IWaterSelectionSet, demandPattern: IPattern, operation: AdjustmentOperationType, value: float) -> IActiveDemandAdjustment:
		"""Adds a new demand adjustment and assigns the values.

		Args:
			scope(IWaterSelectionSet): scope
			demandPattern(IPattern): demandPattern
			operation(AdjustmentOperationType): operation
			value(float): value

		Returns:
			IActiveDemandAdjustment: 
		"""
		pass

class IActiveDemandAdjustment(ICollectionElement):

	def __init__(self) -> None:
		"""Creating a new Instance of this class is not allowed


		Raises:
			Exception: if this class is instanciated
		"""
		raise Exception("Creating a new Instance of this class is not allowed")
		pass

	@property
	def Scope(self) -> IWaterSelectionSet:
		"""No Description

		Returns:
			IActiveDemandAdjustment: 
		"""
		pass

	@property
	def DemandPattern(self) -> IPattern:
		"""No Description

		Returns:
			IActiveDemandAdjustment: 
		"""
		pass

	@property
	def Value(self) -> float:
		"""No Description

		Returns:
			IActiveDemandAdjustment: 
		"""
		pass

	@property
	def Operation(self) -> AdjustmentOperationType:
		"""No Description

		Returns:
			IActiveDemandAdjustment: 
		"""
		pass

	@Scope.setter
	def Scope(self, scope: IWaterSelectionSet) -> None:
		pass

	@DemandPattern.setter
	def DemandPattern(self, demandpattern: IPattern) -> None:
		pass

	@Value.setter
	def Value(self, value: float) -> None:
		pass

	@Operation.setter
	def Operation(self, operation: AdjustmentOperationType) -> None:
		pass

class IActiveRoughnessAdjustmentCollection(ICollectionElements[IActiveRoughnessAdjustments, IActiveRoughnessAdjustment, IElementUnits]):

	def __init__(self) -> None:
		"""Creating a new Instance of this class is not allowed


		Raises:
			Exception: if this class is instanciated
		"""
		raise Exception("Creating a new Instance of this class is not allowed")
		pass

class IActiveRoughnessAdjustments(ICollection[IActiveRoughnessAdjustment]):

	def __init__(self) -> None:
		"""Creating a new Instance of this class is not allowed


		Raises:
			Exception: if this class is instanciated
		"""
		raise Exception("Creating a new Instance of this class is not allowed")
		pass

	def Add(self, scope: IWaterSelectionSet, operation: AdjustmentOperationType, value: float) -> IActiveRoughnessAdjustment:
		"""Adds a new roughness adjustment.

		Args:
			scope(IWaterSelectionSet): scope
			operation(AdjustmentOperationType): operation
			value(float): value

		Returns:
			IActiveRoughnessAdjustment: 
		"""
		pass

class IActiveRoughnessAdjustment(ICollectionElement):

	def __init__(self) -> None:
		"""Creating a new Instance of this class is not allowed


		Raises:
			Exception: if this class is instanciated
		"""
		raise Exception("Creating a new Instance of this class is not allowed")
		pass

	@property
	def Scope(self) -> IWaterSelectionSet:
		"""No Description

		Returns:
			IActiveRoughnessAdjustment: 
		"""
		pass

	@property
	def Value(self) -> float:
		"""No Description

		Returns:
			IActiveRoughnessAdjustment: 
		"""
		pass

	@property
	def Operation(self) -> AdjustmentOperationType:
		"""No Description

		Returns:
			IActiveRoughnessAdjustment: 
		"""
		pass

	@Scope.setter
	def Scope(self, scope: IWaterSelectionSet) -> None:
		pass

	@Value.setter
	def Value(self, value: float) -> None:
		pass

	@Operation.setter
	def Operation(self, operation: AdjustmentOperationType) -> None:
		pass

class IActiveUnitDemandAdjustmentCollection(ICollectionElements[IActiveUnitDemandAdjustments, IActiveUnitDemandAdjustment, IElementUnits]):

	def __init__(self) -> None:
		"""Creating a new Instance of this class is not allowed


		Raises:
			Exception: if this class is instanciated
		"""
		raise Exception("Creating a new Instance of this class is not allowed")
		pass

class IActiveUnitDemandAdjustments(ICollection[IActiveUnitDemandAdjustment]):

	def __init__(self) -> None:
		"""Creating a new Instance of this class is not allowed


		Raises:
			Exception: if this class is instanciated
		"""
		raise Exception("Creating a new Instance of this class is not allowed")
		pass

	def Add(self, scope: IWaterSelectionSet, unitDemandLoad: IUnitDemandLoad, operation: AdjustmentOperationType, value: float) -> IActiveUnitDemandAdjustment:
		"""Add a new unit demand adjustment.

		Args:
			scope(IWaterSelectionSet): scope
			unitDemandLoad(IUnitDemandLoad): unitDemandLoad
			operation(AdjustmentOperationType): operation
			value(float): value

		Returns:
			IActiveUnitDemandAdjustment: 
		"""
		pass

class IActiveUnitDemandAdjustment(ICollectionElement):

	def __init__(self) -> None:
		"""Creating a new Instance of this class is not allowed


		Raises:
			Exception: if this class is instanciated
		"""
		raise Exception("Creating a new Instance of this class is not allowed")
		pass

	@property
	def Scope(self) -> IWaterSelectionSet:
		"""No Description

		Returns:
			IActiveUnitDemandAdjustment: 
		"""
		pass

	@property
	def UnitLoadDemand(self) -> IUnitDemandLoad:
		"""No Description

		Returns:
			IActiveUnitDemandAdjustment: 
		"""
		pass

	@property
	def Value(self) -> float:
		"""No Description

		Returns:
			IActiveUnitDemandAdjustment: 
		"""
		pass

	@property
	def Operation(self) -> AdjustmentOperationType:
		"""No Description

		Returns:
			IActiveUnitDemandAdjustment: 
		"""
		pass

	@Scope.setter
	def Scope(self, scope: IWaterSelectionSet) -> None:
		pass

	@UnitLoadDemand.setter
	def UnitLoadDemand(self, unitloaddemand: IUnitDemandLoad) -> None:
		pass

	@Value.setter
	def Value(self, value: float) -> None:
		pass

	@Operation.setter
	def Operation(self, operation: AdjustmentOperationType) -> None:
		pass

class IWaterScenarioOptions(IScenarioOptions[IWaterScenarioOptionsUnits]):

	def __init__(self) -> None:
		"""Creating a new Instance of this class is not allowed


		Raises:
			Exception: if this class is instanciated
		"""
		raise Exception("Creating a new Instance of this class is not allowed")
		pass

	@property
	def CalculationType(self) -> CalculationType:
		"""No Description

		Returns:
			IWaterScenarioOptions: 
		"""
		pass

	@property
	def FrictionMethod(self) -> EpaNetEngine_FrictionMethodEnum:
		"""No Description

		Returns:
			IWaterScenarioOptions: 
		"""
		pass

	@property
	def SimulationStartDate(self) -> datetime:
		"""No Description

		Returns:
			IWaterScenarioOptions: 
		"""
		pass

	@property
	def TimeAnalysisType(self) -> EpaNetEngine_TimeAnalysisTypeEnum:
		"""No Description

		Returns:
			IWaterScenarioOptions: 
		"""
		pass

	@property
	def StartTime(self) -> datetime:
		"""No Description

		Returns:
			IWaterScenarioOptions: 
		"""
		pass

	@property
	def Duration(self) -> float:
		"""No Description

		Returns:
			IWaterScenarioOptions: 
		"""
		pass

	@property
	def HydraulicTimeStep(self) -> float:
		"""No Description

		Returns:
			IWaterScenarioOptions: 
		"""
		pass

	@property
	def DemandAdjustments(self) -> DemandAdjustmentsType:
		"""No Description

		Returns:
			IWaterScenarioOptions: 
		"""
		pass

	@property
	def ActiveDemandAdjustments(self) -> IActiveDemandAdjustmentsCollection:
		"""No Description

		Returns:
			IWaterScenarioOptions: 
		"""
		pass

	@property
	def UnitDemandAdjustments(self) -> UnitDemandAdjustmentType:
		"""No Description

		Returns:
			IWaterScenarioOptions: 
		"""
		pass

	@property
	def ActiveUnitLoadDemandAdjustments(self) -> IActiveUnitDemandAdjustmentCollection:
		"""No Description

		Returns:
			IWaterScenarioOptions: 
		"""
		pass

	@property
	def RoughnessAdjustments(self) -> RoughnessAdjustmentType:
		"""No Description

		Returns:
			IWaterScenarioOptions: 
		"""
		pass

	@property
	def ActiveRoughnessAdjustments(self) -> IActiveRoughnessAdjustmentCollection:
		"""No Description

		Returns:
			IWaterScenarioOptions: 
		"""
		pass

	@CalculationType.setter
	def CalculationType(self, calculationtype: CalculationType) -> None:
		pass

	@FrictionMethod.setter
	def FrictionMethod(self, frictionmethod: EpaNetEngine_FrictionMethodEnum) -> None:
		pass

	@SimulationStartDate.setter
	def SimulationStartDate(self, simulationstartdate: datetime) -> None:
		pass

	@TimeAnalysisType.setter
	def TimeAnalysisType(self, timeanalysistype: EpaNetEngine_TimeAnalysisTypeEnum) -> None:
		pass

	@StartTime.setter
	def StartTime(self, starttime: datetime) -> None:
		pass

	@Duration.setter
	def Duration(self, duration: float) -> None:
		pass

	@HydraulicTimeStep.setter
	def HydraulicTimeStep(self, hydraulictimestep: float) -> None:
		pass

	@DemandAdjustments.setter
	def DemandAdjustments(self, demandadjustments: DemandAdjustmentsType) -> None:
		pass

	@UnitDemandAdjustments.setter
	def UnitDemandAdjustments(self, unitdemandadjustments: UnitDemandAdjustmentType) -> None:
		pass

	@RoughnessAdjustments.setter
	def RoughnessAdjustments(self, roughnessadjustments: RoughnessAdjustmentType) -> None:
		pass

class IWaterScenarioOptionsUnits(IElementUnits):

	def __init__(self) -> None:
		"""Creating a new Instance of this class is not allowed


		Raises:
			Exception: if this class is instanciated
		"""
		raise Exception("Creating a new Instance of this class is not allowed")
		pass

	@property
	def DurationUnit(self) -> IUnit:
		"""No Description

		Returns:
			IWaterScenarioOptionsUnits: 
		"""
		pass

	@property
	def HydraulicTimeStepUnit(self) -> IUnit:
		"""No Description

		Returns:
			IWaterScenarioOptionsUnits: 
		"""
		pass

