from typing import Generic
from OpenFlows.Domain.ModelingElements import IElementUnits, IElement
from OpenFlows.Domain.ModelingElements.Collections import ICollectionElement

class IActiveDemandAdjustmentsCollection(ICollectionElements[IActiveDemandAdjustments, IActiveDemandAdjustment, IElementUnits]):

	def __init__(self) -> None:
		"""Creating a new Instance of this class is not allowed


		Raises:
			Exception: if this class is instanciated
		"""
		raise Exception("Creating a new Instance of this class is not allowed")
		pass

class IActiveDemandAdjustments(ICollection[IActiveDemandAdjustment], IEnumerable[IActiveDemandAdjustment], IEnumerable):

	def __init__(self) -> None:
		"""Creating a new Instance of this class is not allowed


		Raises:
			Exception: if this class is instanciated
		"""
		raise Exception("Creating a new Instance of this class is not allowed")
		pass

	def Add(self, scope: IWaterSelectionSet, demandPattern: IPattern, operation: int, value: float) -> IActiveDemandAdjustment:
		"""Method Description

		Args:
			scope(IWaterSelectionSet): scope
			demandPattern(IPattern): demandPattern
			operation(int): operation
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
	def Operation(self) -> int:
		"""
		Returns:
			int: No Description
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
	def Operation(self, operation: int) -> None:
		pass

class IActiveRoughnessAdjustmentCollection(ICollectionElements[IActiveRoughnessAdjustments, IActiveRoughnessAdjustment, IElementUnits]):

	def __init__(self) -> None:
		"""Creating a new Instance of this class is not allowed


		Raises:
			Exception: if this class is instanciated
		"""
		raise Exception("Creating a new Instance of this class is not allowed")
		pass

class IActiveRoughnessAdjustments(ICollection[IActiveRoughnessAdjustment], IEnumerable[IActiveRoughnessAdjustment], IEnumerable):

	def __init__(self) -> None:
		"""Creating a new Instance of this class is not allowed


		Raises:
			Exception: if this class is instanciated
		"""
		raise Exception("Creating a new Instance of this class is not allowed")
		pass

	def Add(self, scope: IWaterSelectionSet, operation: int, value: float) -> IActiveRoughnessAdjustment:
		"""Method Description

		Args:
			scope(IWaterSelectionSet): scope
			operation(int): operation
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
	def Operation(self) -> int:
		"""
		Returns:
			int: No Description
		"""
		pass

	@Scope.setter
	def Scope(self, scope: IWaterSelectionSet) -> None:
		pass

	@Value.setter
	def Value(self, value: float) -> None:
		pass

	@Operation.setter
	def Operation(self, operation: int) -> None:
		pass

class IActiveUnitDemandAdjustmentCollection(ICollectionElements[IActiveUnitDemandAdjustments, IActiveUnitDemandAdjustment, IElementUnits]):

	def __init__(self) -> None:
		"""Creating a new Instance of this class is not allowed


		Raises:
			Exception: if this class is instanciated
		"""
		raise Exception("Creating a new Instance of this class is not allowed")
		pass

class IActiveUnitDemandAdjustments(ICollection[IActiveUnitDemandAdjustment], IEnumerable[IActiveUnitDemandAdjustment], IEnumerable):

	def __init__(self) -> None:
		"""Creating a new Instance of this class is not allowed


		Raises:
			Exception: if this class is instanciated
		"""
		raise Exception("Creating a new Instance of this class is not allowed")
		pass

	def Add(self, scope: IWaterSelectionSet, unitDemandLoad: IUnitDemandLoad, operation: int, value: float) -> IActiveUnitDemandAdjustment:
		"""Method Description

		Args:
			scope(IWaterSelectionSet): scope
			unitDemandLoad(IUnitDemandLoad): unitDemandLoad
			operation(int): operation
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
	def Operation(self) -> int:
		"""
		Returns:
			int: No Description
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
	def Operation(self, operation: int) -> None:
		pass

class IWaterScenarioOptions(IScenarioOptions[IWaterScenarioOptionsUnits], IElement, IEditLabeled, ILabeled):

	def __init__(self) -> None:
		"""Creating a new Instance of this class is not allowed


		Raises:
			Exception: if this class is instanciated
		"""
		raise Exception("Creating a new Instance of this class is not allowed")
		pass

	@property
	def CalculationType(self) -> int:
		"""
		Returns:
			int: No Description
		"""
		pass

	@property
	def FrictionMethod(self) -> int:
		"""
		Returns:
			int: No Description
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
	def TimeAnalysisType(self) -> int:
		"""
		Returns:
			int: No Description
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
	def DemandAdjustments(self) -> int:
		"""
		Returns:
			int: No Description
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
	def UnitDemandAdjustments(self) -> int:
		"""
		Returns:
			int: No Description
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
	def RoughnessAdjustments(self) -> int:
		"""
		Returns:
			int: No Description
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
	def CalculationType(self, calculationtype: int) -> None:
		pass

	@FrictionMethod.setter
	def FrictionMethod(self, frictionmethod: int) -> None:
		pass

	@SimulationStartDate.setter
	def SimulationStartDate(self, simulationstartdate: datetime) -> None:
		pass

	@TimeAnalysisType.setter
	def TimeAnalysisType(self, timeanalysistype: int) -> None:
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
	def DemandAdjustments(self, demandadjustments: int) -> None:
		pass

	@UnitDemandAdjustments.setter
	def UnitDemandAdjustments(self, unitdemandadjustments: int) -> None:
		pass

	@RoughnessAdjustments.setter
	def RoughnessAdjustments(self, roughnessadjustments: int) -> None:
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

