from typing import Generic
from OpenFlows.Domain.ModelingElements.Collections import ICollectionElements, ICollection, ICollectionElement
from OpenFlows.Domain.ModelingElements import IElementUnits, IScenarioOptions
from OpenFlows.Water.Domain.ModelingElements import IWaterSelectionSet
from OpenFlows.Water.Domain.ModelingElements.Components import IPattern, IUnitDemandLoad
from datetime import datetime
from OpenFlows.Units import IUnit

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
		"""Method Description

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
		"""
		Returns:
			IWaterSelectionSet: No Description
		"""
		pass

	@property
	def DemandPattern(self) -> IPattern:
		"""
		Returns:
			IPattern: No Description
		"""
		pass

	@property
	def Value(self) -> float:
		"""
		Returns:
			float: No Description
		"""
		pass

	@property
	def Operation(self) -> AdjustmentOperationType:
		"""
		Returns:
			AdjustmentOperationType: No Description
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
		"""Method Description

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
		"""
		Returns:
			IWaterSelectionSet: No Description
		"""
		pass

	@property
	def Value(self) -> float:
		"""
		Returns:
			float: No Description
		"""
		pass

	@property
	def Operation(self) -> AdjustmentOperationType:
		"""
		Returns:
			AdjustmentOperationType: No Description
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
		"""Method Description

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
		"""
		Returns:
			IWaterSelectionSet: No Description
		"""
		pass

	@property
	def UnitLoadDemand(self) -> IUnitDemandLoad:
		"""
		Returns:
			IUnitDemandLoad: No Description
		"""
		pass

	@property
	def Value(self) -> float:
		"""
		Returns:
			float: No Description
		"""
		pass

	@property
	def Operation(self) -> AdjustmentOperationType:
		"""
		Returns:
			AdjustmentOperationType: No Description
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
		"""
		Returns:
			CalculationType: No Description
		"""
		pass

	@property
	def FrictionMethod(self) -> EpaNetEngine_FrictionMethodEnum:
		"""
		Returns:
			EpaNetEngine_FrictionMethodEnum: No Description
		"""
		pass

	@property
	def SimulationStartDate(self) -> datetime:
		"""
		Returns:
			datetime: No Description
		"""
		pass

	@property
	def TimeAnalysisType(self) -> EpaNetEngine_TimeAnalysisTypeEnum:
		"""
		Returns:
			EpaNetEngine_TimeAnalysisTypeEnum: No Description
		"""
		pass

	@property
	def StartTime(self) -> datetime:
		"""
		Returns:
			datetime: No Description
		"""
		pass

	@property
	def Duration(self) -> float:
		"""
		Returns:
			float: No Description
		"""
		pass

	@property
	def HydraulicTimeStep(self) -> float:
		"""
		Returns:
			float: No Description
		"""
		pass

	@property
	def DemandAdjustments(self) -> DemandAdjustmentsType:
		"""
		Returns:
			DemandAdjustmentsType: No Description
		"""
		pass

	@property
	def ActiveDemandAdjustments(self) -> IActiveDemandAdjustmentsCollection:
		"""
		Returns:
			IActiveDemandAdjustmentsCollection: No Description
		"""
		pass

	@property
	def UnitDemandAdjustments(self) -> UnitDemandAdjustmentType:
		"""
		Returns:
			UnitDemandAdjustmentType: No Description
		"""
		pass

	@property
	def ActiveUnitLoadDemandAdjustments(self) -> IActiveUnitDemandAdjustmentCollection:
		"""
		Returns:
			IActiveUnitDemandAdjustmentCollection: No Description
		"""
		pass

	@property
	def RoughnessAdjustments(self) -> RoughnessAdjustmentType:
		"""
		Returns:
			RoughnessAdjustmentType: No Description
		"""
		pass

	@property
	def ActiveRoughnessAdjustments(self) -> IActiveRoughnessAdjustmentCollection:
		"""
		Returns:
			IActiveRoughnessAdjustmentCollection: No Description
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
		"""
		Returns:
			IUnit: No Description
		"""
		pass

	@property
	def HydraulicTimeStepUnit(self) -> IUnit:
		"""
		Returns:
			IUnit: No Description
		"""
		pass

