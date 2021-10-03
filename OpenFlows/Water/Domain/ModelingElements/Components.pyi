from OpenFlows.Domain.ModelingElements.Collections import ICollectionElements, ICollection, ICollectionElement
from OpenFlows.Domain.ModelingElements import IElementUnits, IElement, TElementManagerType, TElementType, TUnitsType
from OpenFlows.Units import IUnit
from datetime import datetime
from OpenFlows.Domain.ModelingElements.Components import IComponentElements, IComponentElement, IModelComponents
from typing import Generic
from OpenFlows.Water.Enumerations import *
from OpenFlows.Water.Domain.ModelingElements.NetworkElements import IWaterNetworkElement


class IAirFlowPressureCollection(ICollectionElements[IAirFlowPressures, IAirFlowPressure, IAirFlowPressureUnits]):

	def __init__(self) -> None:
		"""Creating a new Instance of this class is not allowed


		Raises:
			Exception: if this class is instanciated
		"""
		raise Exception("Creating a new Instance of this class is not allowed")
		pass

class IAirFlowPressures(ICollection[IAirFlowPressure]):

	def __init__(self) -> None:
		"""Creating a new Instance of this class is not allowed


		Raises:
			Exception: if this class is instanciated
		"""
		raise Exception("Creating a new Instance of this class is not allowed")
		pass

	def Add(self, flow: float, pressure: float) -> IAirFlowPressure:
		"""Method Description

		Args:
			flow(float): flow
			pressure(float): pressure

		Returns:
			IAirFlowPressure: 
		"""
		pass

class IAirFlowPressure(ICollectionElement):

	def __init__(self) -> None:
		"""Creating a new Instance of this class is not allowed


		Raises:
			Exception: if this class is instanciated
		"""
		raise Exception("Creating a new Instance of this class is not allowed")
		pass

	@property
	def Flow(self) -> float:
		"""
		Returns:
			float: No Description
		"""
		pass

	@property
	def Pressure(self) -> float:
		"""
		Returns:
			float: No Description
		"""
		pass

	@Flow.setter
	def Flow(self, flow: float) -> None:
		pass

	@Pressure.setter
	def Pressure(self, pressure: float) -> None:
		pass

class IAirFlowPressureUnits(IElementUnits):

	def __init__(self) -> None:
		"""Creating a new Instance of this class is not allowed


		Raises:
			Exception: if this class is instanciated
		"""
		raise Exception("Creating a new Instance of this class is not allowed")
		pass

	@property
	def FlowUnit(self) -> IUnit:
		"""
		Returns:
			IUnit: No Description
		"""
		pass

	@property
	def PressureUnit(self) -> IUnit:
		"""
		Returns:
			IUnit: No Description
		"""
		pass

class IAirFlowCurve(IWaterComponentBase[IAirFlowCurves, IAirFlowCurve, IAirFlowCurveUnits]):

	def __init__(self) -> None:
		"""Creating a new Instance of this class is not allowed


		Raises:
			Exception: if this class is instanciated
		"""
		raise Exception("Creating a new Instance of this class is not allowed")
		pass

	@property
	def AirFlowPressureCollection(self) -> IAirFlowPressureCollection:
		"""
		Returns:
			IAirFlowPressureCollection: No Description
		"""
		pass

class IAirFlowCurves(IWaterComponentsBase[IAirFlowCurves, IAirFlowCurve, IAirFlowCurveUnits]):

	def __init__(self) -> None:
		"""Creating a new Instance of this class is not allowed


		Raises:
			Exception: if this class is instanciated
		"""
		raise Exception("Creating a new Instance of this class is not allowed")
		pass

class IAirFlowCurveUnits(IElementUnits):

	def __init__(self) -> None:
		"""Creating a new Instance of this class is not allowed


		Raises:
			Exception: if this class is instanciated
		"""
		raise Exception("Creating a new Instance of this class is not allowed")
		pass

class IControl(IWaterComponentBase[IControls, IControl, IElementUnits], IWaterComponent):

	def __init__(self) -> None:
		"""Creating a new Instance of this class is not allowed


		Raises:
			Exception: if this class is instanciated
		"""
		raise Exception("Creating a new Instance of this class is not allowed")
		pass

	@property
	def ControlType(self) -> ControlTypeEnum:
		"""
		Returns:
			ControlTypeEnum: No Description
		"""
		pass

	@property
	def Condition(self) -> IControlCondition:
		"""
		Returns:
			IControlCondition: No Description
		"""
		pass

	@property
	def Action(self) -> IControlAction:
		"""
		Returns:
			IControlAction: No Description
		"""
		pass

	@property
	def LogicalControl(self) -> ILogicalControl:
		"""
		Returns:
			ILogicalControl: No Description
		"""
		pass

	@property
	def DefineDescription(self) -> bool:
		"""
		Returns:
			bool: No Description
		"""
		pass

	@property
	def Description(self) -> str:
		"""
		Returns:
			str: No Description
		"""
		pass

	@property
	def Summary(self) -> str:
		"""
		Returns:
			str: No Description
		"""
		pass

	@ControlType.setter
	def ControlType(self, controltype: ControlTypeEnum) -> None:
		pass

	@Condition.setter
	def Condition(self, condition: IControlCondition) -> None:
		pass

	@Action.setter
	def Action(self, action: IControlAction) -> None:
		pass

	@DefineDescription.setter
	def DefineDescription(self, definedescription: bool) -> None:
		pass

	@Description.setter
	def Description(self, description: str) -> None:
		pass

class ILogicalControl:

	def __init__(self) -> None:
		"""Creating a new Instance of this class is not allowed


		Raises:
			Exception: if this class is instanciated
		"""
		raise Exception("Creating a new Instance of this class is not allowed")
		pass

	@property
	def IsLogicalControl(self) -> bool:
		"""
		Returns:
			bool: No Description
		"""
		pass

	@property
	def HasPriority(self) -> bool:
		"""
		Returns:
			bool: No Description
		"""
		pass

	@property
	def Priority(self) -> ControlPriorityEnum:
		"""
		Returns:
			ControlPriorityEnum: No Description
		"""
		pass

	@property
	def HasElse(self) -> bool:
		"""
		Returns:
			bool: No Description
		"""
		pass

	@property
	def ElseAction(self) -> IControlAction:
		"""
		Returns:
			IControlAction: No Description
		"""
		pass

	@HasPriority.setter
	def HasPriority(self, haspriority: bool) -> None:
		pass

	@Priority.setter
	def Priority(self, priority: ControlPriorityEnum) -> None:
		pass

	@HasElse.setter
	def HasElse(self, haselse: bool) -> None:
		pass

	@ElseAction.setter
	def ElseAction(self, elseaction: IControlAction) -> None:
		pass

class IControls(IWaterComponentsBase[IControls, IControl, IElementUnits]):

	def __init__(self) -> None:
		"""Creating a new Instance of this class is not allowed


		Raises:
			Exception: if this class is instanciated
		"""
		raise Exception("Creating a new Instance of this class is not allowed")
		pass

class IControlCondition(IWaterComponentBase[IControlConditions, IControlCondition, IControlConditionUnits], IWaterComponent):

	def __init__(self) -> None:
		"""Creating a new Instance of this class is not allowed


		Raises:
			Exception: if this class is instanciated
		"""
		raise Exception("Creating a new Instance of this class is not allowed")
		pass

	@property
	def ConditionType(self) -> ConditionTypeEnum:
		"""
		Returns:
			ConditionTypeEnum: No Description
		"""
		pass

	@property
	def SimpleConditionType(self) -> SimpleConditionType:
		"""
		Returns:
			SimpleConditionType: No Description
		"""
		pass

	@property
	def ElementCondition(self) -> IElementControlConditionInput:
		"""
		Returns:
			IElementControlConditionInput: No Description
		"""
		pass

	@property
	def SystemDemandCondition(self) -> ISystemDemandConditionInput:
		"""
		Returns:
			ISystemDemandConditionInput: No Description
		"""
		pass

	@property
	def ClockTimeCondition(self) -> IClockTimeConditionInput:
		"""
		Returns:
			IClockTimeConditionInput: No Description
		"""
		pass

	@property
	def TimeFromStartCondition(self) -> ITimeFromStartConditionInput:
		"""
		Returns:
			ITimeFromStartConditionInput: No Description
		"""
		pass

	@property
	def CompositeConditionCollection(self) -> ICompositeConditionCollection:
		"""
		Returns:
			ICompositeConditionCollection: No Description
		"""
		pass

	@property
	def IsUserDefinedDescriptionFormat(self) -> bool:
		"""
		Returns:
			bool: No Description
		"""
		pass

	@property
	def Description(self) -> str:
		"""
		Returns:
			str: No Description
		"""
		pass

	@property
	def Summary(self) -> str:
		"""
		Returns:
			str: No Description
		"""
		pass

	@ConditionType.setter
	def ConditionType(self, conditiontype: ConditionTypeEnum) -> None:
		pass

	@SimpleConditionType.setter
	def SimpleConditionType(self, simpleconditiontype: SimpleConditionType) -> None:
		pass

	@IsUserDefinedDescriptionFormat.setter
	def IsUserDefinedDescriptionFormat(self, isuserdefineddescriptionformat: bool) -> None:
		pass

	@Description.setter
	def Description(self, description: str) -> None:
		pass

class IControlSimpleConditionInput:

	def __init__(self) -> None:
		"""Creating a new Instance of this class is not allowed


		Raises:
			Exception: if this class is instanciated
		"""
		raise Exception("Creating a new Instance of this class is not allowed")
		pass

	@property
	def SimpleConditionType(self) -> SimpleConditionType:
		"""
		Returns:
			SimpleConditionType: No Description
		"""
		pass

	@property
	def Comparison(self) -> ConditionComparisonOperator:
		"""
		Returns:
			ConditionComparisonOperator: No Description
		"""
		pass

	@Comparison.setter
	def Comparison(self, comparison: ConditionComparisonOperator) -> None:
		pass

class IElementControlConditionInput(IControlSimpleConditionInput):

	def __init__(self) -> None:
		"""Creating a new Instance of this class is not allowed


		Raises:
			Exception: if this class is instanciated
		"""
		raise Exception("Creating a new Instance of this class is not allowed")
		pass

	@property
	def IsElementCondition(self) -> bool:
		"""
		Returns:
			bool: No Description
		"""
		pass

	@property
	def Element(self) -> IWaterNetworkElement:
		"""
		Returns:
			IWaterNetworkElement: No Description
		"""
		pass

	@property
	def Node(self) -> INodeConditionInput:
		"""
		Returns:
			INodeConditionInput: No Description
		"""
		pass

	@property
	def Tank(self) -> ITankConditionInput:
		"""
		Returns:
			ITankConditionInput: No Description
		"""
		pass

	@property
	def Pump(self) -> IPumpConditionInput:
		"""
		Returns:
			IPumpConditionInput: No Description
		"""
		pass

	@property
	def Pipe(self) -> IPipeConditionInput:
		"""
		Returns:
			IPipeConditionInput: No Description
		"""
		pass

	@property
	def PressureValve(self) -> IPressureValveConditionInput:
		"""
		Returns:
			IPressureValveConditionInput: No Description
		"""
		pass

	@property
	def FCV(self) -> IFlowControLValveConditionInput:
		"""
		Returns:
			IFlowControLValveConditionInput: No Description
		"""
		pass

	@property
	def GPV(self) -> IGeneralPurposeValveConditionInput:
		"""
		Returns:
			IGeneralPurposeValveConditionInput: No Description
		"""
		pass

	@property
	def TCV(self) -> IThrottleControlValveConditionInput:
		"""
		Returns:
			IThrottleControlValveConditionInput: No Description
		"""
		pass

	@property
	def HydroTank(self) -> IHydroTankConditionInput:
		"""
		Returns:
			IHydroTankConditionInput: No Description
		"""
		pass

	@property
	def SurgeTank(self) -> ISurgeTankConditionInput:
		"""
		Returns:
			ISurgeTankConditionInput: No Description
		"""
		pass

	@Element.setter
	def Element(self, element: IWaterNetworkElement) -> None:
		pass

class IElementConditionInput:

	def __init__(self) -> None:
		"""Creating a new Instance of this class is not allowed


		Raises:
			Exception: if this class is instanciated
		"""
		raise Exception("Creating a new Instance of this class is not allowed")
		pass

	@property
	def Element(self) -> IWaterNetworkElement:
		"""
		Returns:
			IWaterNetworkElement: No Description
		"""
		pass

class INodeConditionInput(IElementConditionInput):

	def __init__(self) -> None:
		"""Creating a new Instance of this class is not allowed


		Raises:
			Exception: if this class is instanciated
		"""
		raise Exception("Creating a new Instance of this class is not allowed")
		pass

	@property
	def NodeAttribute(self) -> NodeAttributeEnum:
		"""
		Returns:
			NodeAttributeEnum: No Description
		"""
		pass

	@property
	def Demand(self) -> float:
		"""
		Returns:
			float: No Description
		"""
		pass

	@property
	def HydraulicGrade(self) -> float:
		"""
		Returns:
			float: No Description
		"""
		pass

	@property
	def Pressure(self) -> float:
		"""
		Returns:
			float: No Description
		"""
		pass

	@NodeAttribute.setter
	def NodeAttribute(self, nodeattribute: NodeAttributeEnum) -> None:
		pass

	@Demand.setter
	def Demand(self, demand: float) -> None:
		pass

	@HydraulicGrade.setter
	def HydraulicGrade(self, hydraulicgrade: float) -> None:
		pass

	@Pressure.setter
	def Pressure(self, pressure: float) -> None:
		pass

class ITankConditionInput:

	def __init__(self) -> None:
		"""Creating a new Instance of this class is not allowed


		Raises:
			Exception: if this class is instanciated
		"""
		raise Exception("Creating a new Instance of this class is not allowed")
		pass

	@property
	def TankAttribute(self) -> TankAttributeEnum:
		"""
		Returns:
			TankAttributeEnum: No Description
		"""
		pass

	@property
	def Demand(self) -> float:
		"""
		Returns:
			float: No Description
		"""
		pass

	@property
	def HydraulicGrade(self) -> float:
		"""
		Returns:
			float: No Description
		"""
		pass

	@property
	def Pressure(self) -> float:
		"""
		Returns:
			float: No Description
		"""
		pass

	@property
	def Level(self) -> float:
		"""
		Returns:
			float: No Description
		"""
		pass

	@property
	def TimeToDrain(self) -> float:
		"""
		Returns:
			float: No Description
		"""
		pass

	@property
	def TimeToFill(self) -> float:
		"""
		Returns:
			float: No Description
		"""
		pass

	@property
	def PercentFull(self) -> float:
		"""
		Returns:
			float: No Description
		"""
		pass

	@TankAttribute.setter
	def TankAttribute(self, tankattribute: TankAttributeEnum) -> None:
		pass

	@Demand.setter
	def Demand(self, demand: float) -> None:
		pass

	@HydraulicGrade.setter
	def HydraulicGrade(self, hydraulicgrade: float) -> None:
		pass

	@Pressure.setter
	def Pressure(self, pressure: float) -> None:
		pass

	@Level.setter
	def Level(self, level: float) -> None:
		pass

	@TimeToDrain.setter
	def TimeToDrain(self, timetodrain: float) -> None:
		pass

	@TimeToFill.setter
	def TimeToFill(self, timetofill: float) -> None:
		pass

	@PercentFull.setter
	def PercentFull(self, percentfull: float) -> None:
		pass

class IPumpConditionInput(IElementConditionInput):

	def __init__(self) -> None:
		"""Creating a new Instance of this class is not allowed


		Raises:
			Exception: if this class is instanciated
		"""
		raise Exception("Creating a new Instance of this class is not allowed")
		pass

	@property
	def PumpAttribute(self) -> ControlConditionPumpAttribute:
		"""
		Returns:
			ControlConditionPumpAttribute: No Description
		"""
		pass

	@property
	def Discharge(self) -> float:
		"""
		Returns:
			float: No Description
		"""
		pass

	@property
	def PumpSetting(self) -> float:
		"""
		Returns:
			float: No Description
		"""
		pass

	@property
	def PumpStatus(self) -> PumpStatus:
		"""
		Returns:
			PumpStatus: No Description
		"""
		pass

	@PumpAttribute.setter
	def PumpAttribute(self, pumpattribute: ControlConditionPumpAttribute) -> None:
		pass

	@Discharge.setter
	def Discharge(self, discharge: float) -> None:
		pass

	@PumpSetting.setter
	def PumpSetting(self, pumpsetting: float) -> None:
		pass

	@PumpStatus.setter
	def PumpStatus(self, pumpstatus: PumpStatus) -> None:
		pass

class IPipeConditionInput(IElementConditionInput):

	def __init__(self) -> None:
		"""Creating a new Instance of this class is not allowed


		Raises:
			Exception: if this class is instanciated
		"""
		raise Exception("Creating a new Instance of this class is not allowed")
		pass

	@property
	def PipeAttribute(self) -> ControlConditionPipeAttribute:
		"""
		Returns:
			ControlConditionPipeAttribute: No Description
		"""
		pass

	@property
	def Discharge(self) -> float:
		"""
		Returns:
			float: No Description
		"""
		pass

	@property
	def PipeStatus(self) -> PipeStatus:
		"""
		Returns:
			PipeStatus: No Description
		"""
		pass

	@PipeAttribute.setter
	def PipeAttribute(self, pipeattribute: ControlConditionPipeAttribute) -> None:
		pass

	@Discharge.setter
	def Discharge(self, discharge: float) -> None:
		pass

	@PipeStatus.setter
	def PipeStatus(self, pipestatus: PipeStatus) -> None:
		pass

class IPressureValveConditionInput(IElementConditionInput):

	def __init__(self) -> None:
		"""Creating a new Instance of this class is not allowed


		Raises:
			Exception: if this class is instanciated
		"""
		raise Exception("Creating a new Instance of this class is not allowed")
		pass

	@property
	def PressureValveAttribute(self) -> ControlConditionPressureValveAttributeEnum:
		"""
		Returns:
			ControlConditionPressureValveAttributeEnum: No Description
		"""
		pass

	@property
	def Discharge(self) -> float:
		"""
		Returns:
			float: No Description
		"""
		pass

	@property
	def HeadlossCoefficient(self) -> float:
		"""
		Returns:
			float: No Description
		"""
		pass

	@property
	def ValveStatus(self) -> ControlConditionValveStatus:
		"""
		Returns:
			ControlConditionValveStatus: No Description
		"""
		pass

	@PressureValveAttribute.setter
	def PressureValveAttribute(self, pressurevalveattribute: ControlConditionPressureValveAttributeEnum) -> None:
		pass

	@Discharge.setter
	def Discharge(self, discharge: float) -> None:
		pass

	@HeadlossCoefficient.setter
	def HeadlossCoefficient(self, headlosscoefficient: float) -> None:
		pass

	@ValveStatus.setter
	def ValveStatus(self, valvestatus: ControlConditionValveStatus) -> None:
		pass

class IFlowControLValveConditionInput(IElementConditionInput):

	def __init__(self) -> None:
		"""Creating a new Instance of this class is not allowed


		Raises:
			Exception: if this class is instanciated
		"""
		raise Exception("Creating a new Instance of this class is not allowed")
		pass

	@property
	def FCVAttribute(self) -> ControlConditionFCVAttributeEnum:
		"""
		Returns:
			ControlConditionFCVAttributeEnum: No Description
		"""
		pass

	@property
	def Discharge(self) -> float:
		"""
		Returns:
			float: No Description
		"""
		pass

	@property
	def HeadlossCoefficient(self) -> float:
		"""
		Returns:
			float: No Description
		"""
		pass

	@property
	def FCVStatus(self) -> FCVStatusEnum:
		"""
		Returns:
			FCVStatusEnum: No Description
		"""
		pass

	@FCVAttribute.setter
	def FCVAttribute(self, fcvattribute: ControlConditionFCVAttributeEnum) -> None:
		pass

	@Discharge.setter
	def Discharge(self, discharge: float) -> None:
		pass

	@HeadlossCoefficient.setter
	def HeadlossCoefficient(self, headlosscoefficient: float) -> None:
		pass

	@FCVStatus.setter
	def FCVStatus(self, fcvstatus: FCVStatusEnum) -> None:
		pass

class IGeneralPurposeValveConditionInput(IElementConditionInput):

	def __init__(self) -> None:
		"""Creating a new Instance of this class is not allowed


		Raises:
			Exception: if this class is instanciated
		"""
		raise Exception("Creating a new Instance of this class is not allowed")
		pass

	@property
	def GPVAttribute(self) -> ControlConditionGPVAttributeEnum:
		"""
		Returns:
			ControlConditionGPVAttributeEnum: No Description
		"""
		pass

	@property
	def Discharge(self) -> float:
		"""
		Returns:
			float: No Description
		"""
		pass

	@property
	def GPVStatus(self) -> ControlConditionGPVStatusEnum:
		"""
		Returns:
			ControlConditionGPVStatusEnum: No Description
		"""
		pass

	@GPVAttribute.setter
	def GPVAttribute(self, gpvattribute: ControlConditionGPVAttributeEnum) -> None:
		pass

	@Discharge.setter
	def Discharge(self, discharge: float) -> None:
		pass

	@GPVStatus.setter
	def GPVStatus(self, gpvstatus: ControlConditionGPVStatusEnum) -> None:
		pass

class IThrottleControlValveConditionInput(IElementConditionInput):

	def __init__(self) -> None:
		"""Creating a new Instance of this class is not allowed


		Raises:
			Exception: if this class is instanciated
		"""
		raise Exception("Creating a new Instance of this class is not allowed")
		pass

	@property
	def TCVAttribute(self) -> ControlConditionTCVAttributeEnum:
		"""
		Returns:
			ControlConditionTCVAttributeEnum: No Description
		"""
		pass

	@property
	def Discharge(self) -> float:
		"""
		Returns:
			float: No Description
		"""
		pass

	@property
	def HeadlossCoefficient(self) -> float:
		"""
		Returns:
			float: No Description
		"""
		pass

	@property
	def TCVStatus(self) -> TCVStatusEnum:
		"""
		Returns:
			TCVStatusEnum: No Description
		"""
		pass

	@TCVAttribute.setter
	def TCVAttribute(self, tcvattribute: ControlConditionTCVAttributeEnum) -> None:
		pass

	@Discharge.setter
	def Discharge(self, discharge: float) -> None:
		pass

	@HeadlossCoefficient.setter
	def HeadlossCoefficient(self, headlosscoefficient: float) -> None:
		pass

	@TCVStatus.setter
	def TCVStatus(self, tcvstatus: TCVStatusEnum) -> None:
		pass

class IHydroTankConditionInput(IElementConditionInput):

	def __init__(self) -> None:
		"""Creating a new Instance of this class is not allowed


		Raises:
			Exception: if this class is instanciated
		"""
		raise Exception("Creating a new Instance of this class is not allowed")
		pass

	@property
	def HydroTankAttribute(self) -> HydroTankAttributeEnum:
		"""
		Returns:
			HydroTankAttributeEnum: No Description
		"""
		pass

	@property
	def HydraulicGrade(self) -> float:
		"""
		Returns:
			float: No Description
		"""
		pass

	@property
	def Pressure(self) -> float:
		"""
		Returns:
			float: No Description
		"""
		pass

	@HydroTankAttribute.setter
	def HydroTankAttribute(self, hydrotankattribute: HydroTankAttributeEnum) -> None:
		pass

	@HydraulicGrade.setter
	def HydraulicGrade(self, hydraulicgrade: float) -> None:
		pass

	@Pressure.setter
	def Pressure(self, pressure: float) -> None:
		pass

class ISurgeTankConditionInput(IElementConditionInput):

	def __init__(self) -> None:
		"""Creating a new Instance of this class is not allowed


		Raises:
			Exception: if this class is instanciated
		"""
		raise Exception("Creating a new Instance of this class is not allowed")
		pass

	@property
	def SurgeTankAttribute(self) -> SurgeTankAttributeEnum:
		"""
		Returns:
			SurgeTankAttributeEnum: No Description
		"""
		pass

	@property
	def Demand(self) -> float:
		"""
		Returns:
			float: No Description
		"""
		pass

	@property
	def HydraulicGrade(self) -> float:
		"""
		Returns:
			float: No Description
		"""
		pass

	@property
	def Pressure(self) -> float:
		"""
		Returns:
			float: No Description
		"""
		pass

	@SurgeTankAttribute.setter
	def SurgeTankAttribute(self, surgetankattribute: SurgeTankAttributeEnum) -> None:
		pass

	@Demand.setter
	def Demand(self, demand: float) -> None:
		pass

	@HydraulicGrade.setter
	def HydraulicGrade(self, hydraulicgrade: float) -> None:
		pass

	@Pressure.setter
	def Pressure(self, pressure: float) -> None:
		pass

class ISystemDemandConditionInput(IControlSimpleConditionInput):

	def __init__(self) -> None:
		"""Creating a new Instance of this class is not allowed


		Raises:
			Exception: if this class is instanciated
		"""
		raise Exception("Creating a new Instance of this class is not allowed")
		pass

	@property
	def IsSystemDemandCondition(self) -> bool:
		"""
		Returns:
			bool: No Description
		"""
		pass

	@property
	def SystemDemand(self) -> float:
		"""
		Returns:
			float: No Description
		"""
		pass

	@SystemDemand.setter
	def SystemDemand(self, systemdemand: float) -> None:
		pass

class IClockTimeConditionInput(IControlSimpleConditionInput):

	def __init__(self) -> None:
		"""Creating a new Instance of this class is not allowed


		Raises:
			Exception: if this class is instanciated
		"""
		raise Exception("Creating a new Instance of this class is not allowed")
		pass

	@property
	def IsClockTimeCondition(self) -> bool:
		"""
		Returns:
			bool: No Description
		"""
		pass

	@property
	def ClockTime(self) -> datetime:
		"""
		Returns:
			datetime: No Description
		"""
		pass

	@ClockTime.setter
	def ClockTime(self, clocktime: datetime) -> None:
		pass

class ITimeFromStartConditionInput(IControlSimpleConditionInput):

	def __init__(self) -> None:
		"""Creating a new Instance of this class is not allowed


		Raises:
			Exception: if this class is instanciated
		"""
		raise Exception("Creating a new Instance of this class is not allowed")
		pass

	@property
	def IsTimeFromStartCondition(self) -> bool:
		"""
		Returns:
			bool: No Description
		"""
		pass

	@property
	def TimeFromStart(self) -> float:
		"""
		Returns:
			float: No Description
		"""
		pass

	@TimeFromStart.setter
	def TimeFromStart(self, timefromstart: float) -> None:
		pass

class IControlConditions(IWaterComponentsBase[IControlConditions, IControlCondition, IControlConditionUnits]):

	def __init__(self) -> None:
		"""Creating a new Instance of this class is not allowed


		Raises:
			Exception: if this class is instanciated
		"""
		raise Exception("Creating a new Instance of this class is not allowed")
		pass

class IControlConditionUnits(IElementUnits):

	def __init__(self) -> None:
		"""Creating a new Instance of this class is not allowed


		Raises:
			Exception: if this class is instanciated
		"""
		raise Exception("Creating a new Instance of this class is not allowed")
		pass

	@property
	def DemandUnit(self) -> IUnit:
		"""
		Returns:
			IUnit: No Description
		"""
		pass

	@property
	def HydraulicGradeUnit(self) -> IUnit:
		"""
		Returns:
			IUnit: No Description
		"""
		pass

	@property
	def PressureUnit(self) -> IUnit:
		"""
		Returns:
			IUnit: No Description
		"""
		pass

	@property
	def LevelUnit(self) -> IUnit:
		"""
		Returns:
			IUnit: No Description
		"""
		pass

	@property
	def TimeToFillUnit(self) -> IUnit:
		"""
		Returns:
			IUnit: No Description
		"""
		pass

	@property
	def TimeToDrainUnit(self) -> IUnit:
		"""
		Returns:
			IUnit: No Description
		"""
		pass

	@property
	def PercentFullUnit(self) -> IUnit:
		"""
		Returns:
			IUnit: No Description
		"""
		pass

	@property
	def DischargeUnit(self) -> IUnit:
		"""
		Returns:
			IUnit: No Description
		"""
		pass

	@property
	def HeadlossCoefficientUnit(self) -> IUnit:
		"""
		Returns:
			IUnit: No Description
		"""
		pass

	@property
	def TimeFromStartUnit(self) -> IUnit:
		"""
		Returns:
			IUnit: No Description
		"""
		pass

class ICompositeCondition(ICollectionElement):

	def __init__(self) -> None:
		"""Creating a new Instance of this class is not allowed


		Raises:
			Exception: if this class is instanciated
		"""
		raise Exception("Creating a new Instance of this class is not allowed")
		pass

	@property
	def LogicalOperator(self) -> LogicalOperatorEnum:
		"""
		Returns:
			LogicalOperatorEnum: No Description
		"""
		pass

	@property
	def Condition(self) -> IControlCondition:
		"""
		Returns:
			IControlCondition: No Description
		"""
		pass

	@LogicalOperator.setter
	def LogicalOperator(self, logicaloperator: LogicalOperatorEnum) -> None:
		pass

	@Condition.setter
	def Condition(self, condition: IControlCondition) -> None:
		pass

class ICompositeConditions(ICollection[ICompositeCondition]):

	def __init__(self) -> None:
		"""Creating a new Instance of this class is not allowed


		Raises:
			Exception: if this class is instanciated
		"""
		raise Exception("Creating a new Instance of this class is not allowed")
		pass

	def Add(self, logicalOperator: LogicalOperatorEnum, condition: IControlCondition) -> ICompositeCondition:
		"""Method Description

		Args:
			logicalOperator(LogicalOperatorEnum): logicalOperator
			condition(IControlCondition): condition

		Returns:
			ICompositeCondition: 
		"""
		pass

class ICompositeConditionCollection(ICollectionElements[ICompositeConditions, ICompositeCondition, IElementUnits]):

	def __init__(self) -> None:
		"""Creating a new Instance of this class is not allowed


		Raises:
			Exception: if this class is instanciated
		"""
		raise Exception("Creating a new Instance of this class is not allowed")
		pass

class IControlAction(IWaterComponentBase[IControlActions, IControlAction, IControlActionUnits], IWaterComponent):

	def __init__(self) -> None:
		"""Creating a new Instance of this class is not allowed


		Raises:
			Exception: if this class is instanciated
		"""
		raise Exception("Creating a new Instance of this class is not allowed")
		pass

	@property
	def ActionType(self) -> ControlActionTypeEnum:
		"""
		Returns:
			ControlActionTypeEnum: No Description
		"""
		pass

	@property
	def Element(self) -> IWaterNetworkElement:
		"""
		Returns:
			IWaterNetworkElement: No Description
		"""
		pass

	@property
	def Pipe(self) -> IPipeActionInput:
		"""
		Returns:
			IPipeActionInput: No Description
		"""
		pass

	@property
	def Pump(self) -> IPumpActionInput:
		"""
		Returns:
			IPumpActionInput: No Description
		"""
		pass

	@property
	def TCV(self) -> IThrottleControlValveActionInput:
		"""
		Returns:
			IThrottleControlValveActionInput: No Description
		"""
		pass

	@property
	def GPV(self) -> IGeneralPurposeValveActionInput:
		"""
		Returns:
			IGeneralPurposeValveActionInput: No Description
		"""
		pass

	@property
	def FCV(self) -> IFlowControlValveActionInput:
		"""
		Returns:
			IFlowControlValveActionInput: No Description
		"""
		pass

	@property
	def PressureValve(self) -> IPressureValveActionInput:
		"""
		Returns:
			IPressureValveActionInput: No Description
		"""
		pass

	@property
	def CompositeActionCollection(self) -> ICompositeActionCollection:
		"""
		Returns:
			ICompositeActionCollection: No Description
		"""
		pass

	@property
	def DefineDescription(self) -> bool:
		"""
		Returns:
			bool: No Description
		"""
		pass

	@property
	def Description(self) -> str:
		"""
		Returns:
			str: No Description
		"""
		pass

	@property
	def Summary(self) -> str:
		"""
		Returns:
			str: No Description
		"""
		pass

	@ActionType.setter
	def ActionType(self, actiontype: ControlActionTypeEnum) -> None:
		pass

	@Element.setter
	def Element(self, element: IWaterNetworkElement) -> None:
		pass

	@DefineDescription.setter
	def DefineDescription(self, definedescription: bool) -> None:
		pass

	@Description.setter
	def Description(self, description: str) -> None:
		pass

class IElementActionInput:

	def __init__(self) -> None:
		"""Creating a new Instance of this class is not allowed


		Raises:
			Exception: if this class is instanciated
		"""
		raise Exception("Creating a new Instance of this class is not allowed")
		pass

	@property
	def Element(self) -> IWaterNetworkElement:
		"""
		Returns:
			IWaterNetworkElement: No Description
		"""
		pass

class IPipeActionInput(IElementActionInput):

	def __init__(self) -> None:
		"""Creating a new Instance of this class is not allowed


		Raises:
			Exception: if this class is instanciated
		"""
		raise Exception("Creating a new Instance of this class is not allowed")
		pass

	@property
	def IsPipeAction(self) -> bool:
		"""
		Returns:
			bool: No Description
		"""
		pass

	@property
	def PipeAttribute(self) -> ControlActionPipeAttribute:
		"""
		Returns:
			ControlActionPipeAttribute: No Description
		"""
		pass

	@property
	def PipeStatus(self) -> ControlActionPipeStatus:
		"""
		Returns:
			ControlActionPipeStatus: No Description
		"""
		pass

	@PipeAttribute.setter
	def PipeAttribute(self, pipeattribute: ControlActionPipeAttribute) -> None:
		pass

	@PipeStatus.setter
	def PipeStatus(self, pipestatus: ControlActionPipeStatus) -> None:
		pass

class IPumpActionInput(IElementActionInput):

	def __init__(self) -> None:
		"""Creating a new Instance of this class is not allowed


		Raises:
			Exception: if this class is instanciated
		"""
		raise Exception("Creating a new Instance of this class is not allowed")
		pass

	@property
	def IsPumpAction(self) -> bool:
		"""
		Returns:
			bool: No Description
		"""
		pass

	@property
	def PumpAttribute(self) -> ControlActionPumpAttribute:
		"""
		Returns:
			ControlActionPumpAttribute: No Description
		"""
		pass

	@property
	def PumpStatus(self) -> ControlActionPumpStatus:
		"""
		Returns:
			ControlActionPumpStatus: No Description
		"""
		pass

	@property
	def RelativeSpeedFactor(self) -> float:
		"""
		Returns:
			float: No Description
		"""
		pass

	@property
	def TargetPressure(self) -> float:
		"""
		Returns:
			float: No Description
		"""
		pass

	@property
	def TargetHead(self) -> float:
		"""
		Returns:
			float: No Description
		"""
		pass

	@PumpAttribute.setter
	def PumpAttribute(self, pumpattribute: ControlActionPumpAttribute) -> None:
		pass

	@PumpStatus.setter
	def PumpStatus(self, pumpstatus: ControlActionPumpStatus) -> None:
		pass

	@RelativeSpeedFactor.setter
	def RelativeSpeedFactor(self, relativespeedfactor: float) -> None:
		pass

	@TargetPressure.setter
	def TargetPressure(self, targetpressure: float) -> None:
		pass

	@TargetHead.setter
	def TargetHead(self, targethead: float) -> None:
		pass

class IThrottleControlValveActionInput(IElementActionInput):

	def __init__(self) -> None:
		"""Creating a new Instance of this class is not allowed


		Raises:
			Exception: if this class is instanciated
		"""
		raise Exception("Creating a new Instance of this class is not allowed")
		pass

	@property
	def IsTCVAction(self) -> bool:
		"""
		Returns:
			bool: No Description
		"""
		pass

	@property
	def TCVAttribute(self) -> ControlActionTCVAttribute:
		"""
		Returns:
			ControlActionTCVAttribute: No Description
		"""
		pass

	@property
	def TCVStatus(self) -> ControlActionTCVStatus:
		"""
		Returns:
			ControlActionTCVStatus: No Description
		"""
		pass

	@property
	def HeadlossCoefficient(self) -> float:
		"""
		Returns:
			float: No Description
		"""
		pass

	@TCVAttribute.setter
	def TCVAttribute(self, tcvattribute: ControlActionTCVAttribute) -> None:
		pass

	@TCVStatus.setter
	def TCVStatus(self, tcvstatus: ControlActionTCVStatus) -> None:
		pass

	@HeadlossCoefficient.setter
	def HeadlossCoefficient(self, headlosscoefficient: float) -> None:
		pass

class IGeneralPurposeValveActionInput(IElementActionInput):

	def __init__(self) -> None:
		"""Creating a new Instance of this class is not allowed


		Raises:
			Exception: if this class is instanciated
		"""
		raise Exception("Creating a new Instance of this class is not allowed")
		pass

	@property
	def IsGPVAction(self) -> bool:
		"""
		Returns:
			bool: No Description
		"""
		pass

	@property
	def GPVAttribute(self) -> ControlActionGPVAttribute:
		"""
		Returns:
			ControlActionGPVAttribute: No Description
		"""
		pass

	@property
	def GPVStatus(self) -> ControlActionGPVStatus:
		"""
		Returns:
			ControlActionGPVStatus: No Description
		"""
		pass

	@GPVAttribute.setter
	def GPVAttribute(self, gpvattribute: ControlActionGPVAttribute) -> None:
		pass

	@GPVStatus.setter
	def GPVStatus(self, gpvstatus: ControlActionGPVStatus) -> None:
		pass

class IFlowControlValveActionInput(IElementActionInput):

	def __init__(self) -> None:
		"""Creating a new Instance of this class is not allowed


		Raises:
			Exception: if this class is instanciated
		"""
		raise Exception("Creating a new Instance of this class is not allowed")
		pass

	@property
	def IsFCVAction(self) -> bool:
		"""
		Returns:
			bool: No Description
		"""
		pass

	@property
	def FCVAttribute(self) -> ControlActionFCVAttribute:
		"""
		Returns:
			ControlActionFCVAttribute: No Description
		"""
		pass

	@property
	def Discharge(self) -> float:
		"""
		Returns:
			float: No Description
		"""
		pass

	@property
	def FCVStatus(self) -> ControlActionFCVStatus:
		"""
		Returns:
			ControlActionFCVStatus: No Description
		"""
		pass

	@FCVAttribute.setter
	def FCVAttribute(self, fcvattribute: ControlActionFCVAttribute) -> None:
		pass

	@Discharge.setter
	def Discharge(self, discharge: float) -> None:
		pass

	@FCVStatus.setter
	def FCVStatus(self, fcvstatus: ControlActionFCVStatus) -> None:
		pass

class IPressureValveActionInput(IElementActionInput):

	def __init__(self) -> None:
		"""Creating a new Instance of this class is not allowed


		Raises:
			Exception: if this class is instanciated
		"""
		raise Exception("Creating a new Instance of this class is not allowed")
		pass

	@property
	def IsPressureValveAction(self) -> bool:
		"""
		Returns:
			bool: No Description
		"""
		pass

	@property
	def PressureValveAttribute(self) -> ControlActionPressureValveAttribute:
		"""
		Returns:
			ControlActionPressureValveAttribute: No Description
		"""
		pass

	@property
	def HydraulicGrade(self) -> float:
		"""
		Returns:
			float: No Description
		"""
		pass

	@property
	def Pressure(self) -> float:
		"""
		Returns:
			float: No Description
		"""
		pass

	@property
	def PressureValveStatus(self) -> ControlActionPressureValveStatus:
		"""
		Returns:
			ControlActionPressureValveStatus: No Description
		"""
		pass

	@PressureValveAttribute.setter
	def PressureValveAttribute(self, pressurevalveattribute: ControlActionPressureValveAttribute) -> None:
		pass

	@HydraulicGrade.setter
	def HydraulicGrade(self, hydraulicgrade: float) -> None:
		pass

	@Pressure.setter
	def Pressure(self, pressure: float) -> None:
		pass

	@PressureValveStatus.setter
	def PressureValveStatus(self, pressurevalvestatus: ControlActionPressureValveStatus) -> None:
		pass

class IControlActions(IWaterComponentsBase[IControlActions, IControlAction, IControlActionUnits]):

	def __init__(self) -> None:
		"""Creating a new Instance of this class is not allowed


		Raises:
			Exception: if this class is instanciated
		"""
		raise Exception("Creating a new Instance of this class is not allowed")
		pass

class IControlActionUnits(IElementUnits):

	def __init__(self) -> None:
		"""Creating a new Instance of this class is not allowed


		Raises:
			Exception: if this class is instanciated
		"""
		raise Exception("Creating a new Instance of this class is not allowed")
		pass

	@property
	def RelativeSpeedFactorUnit(self) -> IUnit:
		"""
		Returns:
			IUnit: No Description
		"""
		pass

	@property
	def TargetPressureUnit(self) -> IUnit:
		"""
		Returns:
			IUnit: No Description
		"""
		pass

	@property
	def TargetHeadUnit(self) -> IUnit:
		"""
		Returns:
			IUnit: No Description
		"""
		pass

	@property
	def HeadlossCoefficientUnit(self) -> IUnit:
		"""
		Returns:
			IUnit: No Description
		"""
		pass

	@property
	def DischargeUnit(self) -> IUnit:
		"""
		Returns:
			IUnit: No Description
		"""
		pass

	@property
	def HydraulicGradeUnit(self) -> IUnit:
		"""
		Returns:
			IUnit: No Description
		"""
		pass

	@property
	def PressureUnit(self) -> IUnit:
		"""
		Returns:
			IUnit: No Description
		"""
		pass

class ICompositeAction(ICollectionElement):

	def __init__(self) -> None:
		"""Creating a new Instance of this class is not allowed


		Raises:
			Exception: if this class is instanciated
		"""
		raise Exception("Creating a new Instance of this class is not allowed")
		pass

	@property
	def Action(self) -> IControlAction:
		"""
		Returns:
			IControlAction: No Description
		"""
		pass

	@Action.setter
	def Action(self, action: IControlAction) -> None:
		pass

class ICompositeActions(ICollection[ICompositeAction]):

	def __init__(self) -> None:
		"""Creating a new Instance of this class is not allowed


		Raises:
			Exception: if this class is instanciated
		"""
		raise Exception("Creating a new Instance of this class is not allowed")
		pass

	def Add(self, action: IControlAction) -> ICompositeAction:
		"""Method Description

		Args:
			action(IControlAction): action

		Returns:
			ICompositeAction: 
		"""
		pass

class ICompositeActionCollection(ICollectionElements[ICompositeActions, ICompositeAction, IElementUnits]):

	def __init__(self) -> None:
		"""Creating a new Instance of this class is not allowed


		Raises:
			Exception: if this class is instanciated
		"""
		raise Exception("Creating a new Instance of this class is not allowed")
		pass

class IWaterComponent(IElement):

	def __init__(self) -> None:
		"""Creating a new Instance of this class is not allowed


		Raises:
			Exception: if this class is instanciated
		"""
		raise Exception("Creating a new Instance of this class is not allowed")
		pass

	@property
	def ElementType(self) -> WaterComponentType:
		"""
		Returns:
			WaterComponentType: No Description
		"""
		pass

class IWaterComponentsBase(Generic[TElementManagerType, TElementType, TUnitsType], IComponentElements[TElementManagerType, TElementType, TUnitsType, WaterComponentType]):

	def __init__(self) -> None:
		"""Creating a new Instance of this class is not allowed


		Raises:
			Exception: if this class is instanciated
		"""
		raise Exception("Creating a new Instance of this class is not allowed")
		pass

class IWaterComponentBase(Generic[TElementManagerType, TElementType, TUnitsType], IComponentElement[TElementManagerType, TElementType, TUnitsType, WaterComponentType]):

	def __init__(self) -> None:
		"""Creating a new Instance of this class is not allowed


		Raises:
			Exception: if this class is instanciated
		"""
		raise Exception("Creating a new Instance of this class is not allowed")
		pass

class IZones(IWaterComponentsBase[IZones, IZone, IElementUnits]):

	def __init__(self) -> None:
		"""Creating a new Instance of this class is not allowed


		Raises:
			Exception: if this class is instanciated
		"""
		raise Exception("Creating a new Instance of this class is not allowed")
		pass

class IZone(IWaterComponentBase[IZones, IZone, IElementUnits]):

	def __init__(self) -> None:
		"""Creating a new Instance of this class is not allowed


		Raises:
			Exception: if this class is instanciated
		"""
		raise Exception("Creating a new Instance of this class is not allowed")
		pass

class IPattern(IWaterComponentBase[IPatterns, IPattern, IPatternUnits]):

	def __init__(self) -> None:
		"""Creating a new Instance of this class is not allowed


		Raises:
			Exception: if this class is instanciated
		"""
		raise Exception("Creating a new Instance of this class is not allowed")
		pass

	@property
	def PatternCategory(self) -> PatternCategory:
		"""
		Returns:
			PatternCategory: No Description
		"""
		pass

	@property
	def PatternFormat(self) -> PatternFormat:
		"""
		Returns:
			PatternFormat: No Description
		"""
		pass

	@property
	def PatternStartTime(self) -> datetime:
		"""
		Returns:
			datetime: No Description
		"""
		pass

	@property
	def PatternStartingMultiplier(self) -> float:
		"""
		Returns:
			float: No Description
		"""
		pass

	@property
	def PatternCurve(self) -> IPatternCurveCollection:
		"""
		Returns:
			IPatternCurveCollection: No Description
		"""
		pass

	@property
	def DailyMultipliers(self) -> IDailyMultipliers:
		"""
		Returns:
			IDailyMultipliers: No Description
		"""
		pass

	@property
	def MonthlyMultipliers(self) -> IMonthlyMultipliers:
		"""
		Returns:
			IMonthlyMultipliers: No Description
		"""
		pass

	@PatternCategory.setter
	def PatternCategory(self, patterncategory: PatternCategory) -> None:
		pass

	@PatternFormat.setter
	def PatternFormat(self, patternformat: PatternFormat) -> None:
		pass

	@PatternStartTime.setter
	def PatternStartTime(self, patternstarttime: datetime) -> None:
		pass

	@PatternStartingMultiplier.setter
	def PatternStartingMultiplier(self, patternstartingmultiplier: float) -> None:
		pass

class IPatternUnits(IPatternMultiplierUnits):

	def __init__(self) -> None:
		"""Creating a new Instance of this class is not allowed


		Raises:
			Exception: if this class is instanciated
		"""
		raise Exception("Creating a new Instance of this class is not allowed")
		pass

	@property
	def TimeFromStartUnit(self) -> IUnit:
		"""
		Returns:
			IUnit: No Description
		"""
		pass

class IPatternMultiplierUnits(IElementUnits):

	def __init__(self) -> None:
		"""Creating a new Instance of this class is not allowed


		Raises:
			Exception: if this class is instanciated
		"""
		raise Exception("Creating a new Instance of this class is not allowed")
		pass

	@property
	def MultiplierUnit(self) -> IUnit:
		"""
		Returns:
			IUnit: No Description
		"""
		pass

class IPatterns(IWaterComponentsBase[IPatterns, IPattern, IPatternUnits]):

	def __init__(self) -> None:
		"""Creating a new Instance of this class is not allowed


		Raises:
			Exception: if this class is instanciated
		"""
		raise Exception("Creating a new Instance of this class is not allowed")
		pass

class IPatternCurveCollection(ICollectionElements[IPatternCurve, IPatternCurveElement, IPatternUnits]):

	def __init__(self) -> None:
		"""Creating a new Instance of this class is not allowed


		Raises:
			Exception: if this class is instanciated
		"""
		raise Exception("Creating a new Instance of this class is not allowed")
		pass

class IPatternCurve(ICollection[IPatternCurveElement]):

	def __init__(self) -> None:
		"""Creating a new Instance of this class is not allowed


		Raises:
			Exception: if this class is instanciated
		"""
		raise Exception("Creating a new Instance of this class is not allowed")
		pass

	def Add(self, timeFromStart: float, multiplier: float) -> IPatternCurveElement:
		"""Method Description

		Args:
			timeFromStart(float): timeFromStart
			multiplier(float): multiplier

		Returns:
			IPatternCurveElement: 
		"""
		pass

class IPatternCurveElement(ICollectionElement):

	def __init__(self) -> None:
		"""Creating a new Instance of this class is not allowed


		Raises:
			Exception: if this class is instanciated
		"""
		raise Exception("Creating a new Instance of this class is not allowed")
		pass

	@property
	def TimeFromStart(self) -> float:
		"""
		Returns:
			float: No Description
		"""
		pass

	@property
	def Multiplier(self) -> float:
		"""
		Returns:
			float: No Description
		"""
		pass

	@TimeFromStart.setter
	def TimeFromStart(self, timefromstart: float) -> None:
		pass

	@Multiplier.setter
	def Multiplier(self, multiplier: float) -> None:
		pass

class IDailyMultipliers:

	def __init__(self) -> None:
		"""Creating a new Instance of this class is not allowed


		Raises:
			Exception: if this class is instanciated
		"""
		raise Exception("Creating a new Instance of this class is not allowed")
		pass

	@property
	def Sunday(self) -> float:
		"""
		Returns:
			float: No Description
		"""
		pass

	@property
	def Monday(self) -> float:
		"""
		Returns:
			float: No Description
		"""
		pass

	@property
	def Tuesday(self) -> float:
		"""
		Returns:
			float: No Description
		"""
		pass

	@property
	def Wednesday(self) -> float:
		"""
		Returns:
			float: No Description
		"""
		pass

	@property
	def Thursday(self) -> float:
		"""
		Returns:
			float: No Description
		"""
		pass

	@property
	def Friday(self) -> float:
		"""
		Returns:
			float: No Description
		"""
		pass

	@property
	def Saturday(self) -> float:
		"""
		Returns:
			float: No Description
		"""
		pass

	@Sunday.setter
	def Sunday(self, sunday: float) -> None:
		pass

	@Monday.setter
	def Monday(self, monday: float) -> None:
		pass

	@Tuesday.setter
	def Tuesday(self, tuesday: float) -> None:
		pass

	@Wednesday.setter
	def Wednesday(self, wednesday: float) -> None:
		pass

	@Thursday.setter
	def Thursday(self, thursday: float) -> None:
		pass

	@Friday.setter
	def Friday(self, friday: float) -> None:
		pass

	@Saturday.setter
	def Saturday(self, saturday: float) -> None:
		pass

class IMonthlyMultipliers:

	def __init__(self) -> None:
		"""Creating a new Instance of this class is not allowed


		Raises:
			Exception: if this class is instanciated
		"""
		raise Exception("Creating a new Instance of this class is not allowed")
		pass

	@property
	def January(self) -> float:
		"""
		Returns:
			float: No Description
		"""
		pass

	@property
	def February(self) -> float:
		"""
		Returns:
			float: No Description
		"""
		pass

	@property
	def March(self) -> float:
		"""
		Returns:
			float: No Description
		"""
		pass

	@property
	def April(self) -> float:
		"""
		Returns:
			float: No Description
		"""
		pass

	@property
	def May(self) -> float:
		"""
		Returns:
			float: No Description
		"""
		pass

	@property
	def June(self) -> float:
		"""
		Returns:
			float: No Description
		"""
		pass

	@property
	def July(self) -> float:
		"""
		Returns:
			float: No Description
		"""
		pass

	@property
	def August(self) -> float:
		"""
		Returns:
			float: No Description
		"""
		pass

	@property
	def September(self) -> float:
		"""
		Returns:
			float: No Description
		"""
		pass

	@property
	def October(self) -> float:
		"""
		Returns:
			float: No Description
		"""
		pass

	@property
	def November(self) -> float:
		"""
		Returns:
			float: No Description
		"""
		pass

	@property
	def December(self) -> float:
		"""
		Returns:
			float: No Description
		"""
		pass

	@January.setter
	def January(self, january: float) -> None:
		pass

	@February.setter
	def February(self, february: float) -> None:
		pass

	@March.setter
	def March(self, march: float) -> None:
		pass

	@April.setter
	def April(self, april: float) -> None:
		pass

	@May.setter
	def May(self, may: float) -> None:
		pass

	@June.setter
	def June(self, june: float) -> None:
		pass

	@July.setter
	def July(self, july: float) -> None:
		pass

	@August.setter
	def August(self, august: float) -> None:
		pass

	@September.setter
	def September(self, september: float) -> None:
		pass

	@October.setter
	def October(self, october: float) -> None:
		pass

	@November.setter
	def November(self, november: float) -> None:
		pass

	@December.setter
	def December(self, december: float) -> None:
		pass

class IPumpDefinitions(IWaterComponentsBase[IPumpDefinitions, IPumpDefinition, IPumpDefinitionUnits]):

	def __init__(self) -> None:
		"""Creating a new Instance of this class is not allowed


		Raises:
			Exception: if this class is instanciated
		"""
		raise Exception("Creating a new Instance of this class is not allowed")
		pass

class IPumpDefinition(IWaterComponentBase[IPumpDefinitions, IPumpDefinition, IPumpDefinitionUnits]):

	def __init__(self) -> None:
		"""Creating a new Instance of this class is not allowed


		Raises:
			Exception: if this class is instanciated
		"""
		raise Exception("Creating a new Instance of this class is not allowed")
		pass

	@property
	def Head(self) -> IPumpDefinitionHead:
		"""
		Returns:
			IPumpDefinitionHead: No Description
		"""
		pass

	@property
	def Efficiency(self) -> IPumpDefinitionEfficiency:
		"""
		Returns:
			IPumpDefinitionEfficiency: No Description
		"""
		pass

	@property
	def NPSH(self) -> IPumpDefinitionNPSH:
		"""
		Returns:
			IPumpDefinitionNPSH: No Description
		"""
		pass

	@property
	def Motor(self) -> IPumpDefinitionMotor:
		"""
		Returns:
			IPumpDefinitionMotor: No Description
		"""
		pass

class IPumpDefinitionUnits(IElementUnits):

	def __init__(self) -> None:
		"""Creating a new Instance of this class is not allowed


		Raises:
			Exception: if this class is instanciated
		"""
		raise Exception("Creating a new Instance of this class is not allowed")
		pass

	@property
	def FlowUnit(self) -> IUnit:
		"""
		Returns:
			IUnit: No Description
		"""
		pass

	@property
	def HeadUnit(self) -> IUnit:
		"""
		Returns:
			IUnit: No Description
		"""
		pass

	@property
	def PowerUnit(self) -> IUnit:
		"""
		Returns:
			IUnit: No Description
		"""
		pass

	@property
	def EfficiencyUnit(self) -> IUnit:
		"""
		Returns:
			IUnit: No Description
		"""
		pass

	@property
	def SpeedUnit(self) -> IUnit:
		"""
		Returns:
			IUnit: No Description
		"""
		pass

class IPumpDefinitionHead:

	def __init__(self) -> None:
		"""Creating a new Instance of this class is not allowed


		Raises:
			Exception: if this class is instanciated
		"""
		raise Exception("Creating a new Instance of this class is not allowed")
		pass

	@property
	def PumpDefinitionType(self) -> PumpDefinitionType:
		"""
		Returns:
			PumpDefinitionType: No Description
		"""
		pass

	@property
	def ConstantPower(self) -> float:
		"""
		Returns:
			float: No Description
		"""
		pass

	@property
	def DesignFlow(self) -> float:
		"""
		Returns:
			float: No Description
		"""
		pass

	@property
	def DesignHead(self) -> float:
		"""
		Returns:
			float: No Description
		"""
		pass

	@property
	def ShutoffHead(self) -> float:
		"""
		Returns:
			float: No Description
		"""
		pass

	@property
	def MaxOperatingHead(self) -> float:
		"""
		Returns:
			float: No Description
		"""
		pass

	@property
	def MaxOperatingFlow(self) -> float:
		"""
		Returns:
			float: No Description
		"""
		pass

	@property
	def MaxExtendedFlow(self) -> float:
		"""
		Returns:
			float: No Description
		"""
		pass

	@property
	def PumpCurve(self) -> IPumpCurveCollection:
		"""
		Returns:
			IPumpCurveCollection: No Description
		"""
		pass

	@PumpDefinitionType.setter
	def PumpDefinitionType(self, pumpdefinitiontype: PumpDefinitionType) -> None:
		pass

	@ConstantPower.setter
	def ConstantPower(self, constantpower: float) -> None:
		pass

	@DesignFlow.setter
	def DesignFlow(self, designflow: float) -> None:
		pass

	@DesignHead.setter
	def DesignHead(self, designhead: float) -> None:
		pass

	@ShutoffHead.setter
	def ShutoffHead(self, shutoffhead: float) -> None:
		pass

	@MaxOperatingHead.setter
	def MaxOperatingHead(self, maxoperatinghead: float) -> None:
		pass

	@MaxOperatingFlow.setter
	def MaxOperatingFlow(self, maxoperatingflow: float) -> None:
		pass

	@MaxExtendedFlow.setter
	def MaxExtendedFlow(self, maxextendedflow: float) -> None:
		pass

class IPumpCurveCollection(ICollectionElements[IPumpCurve, IPumpCurveElement, IPumpCurveUnits]):

	def __init__(self) -> None:
		"""Creating a new Instance of this class is not allowed


		Raises:
			Exception: if this class is instanciated
		"""
		raise Exception("Creating a new Instance of this class is not allowed")
		pass

class IPumpCurve(ICollection[IPumpCurveElement]):

	def __init__(self) -> None:
		"""Creating a new Instance of this class is not allowed


		Raises:
			Exception: if this class is instanciated
		"""
		raise Exception("Creating a new Instance of this class is not allowed")
		pass

	def Add(self, flow: float, head: float) -> IPumpCurveElement:
		"""Method Description

		Args:
			flow(float): flow
			head(float): head

		Returns:
			IPumpCurveElement: 
		"""
		pass

class IPumpCurveElement(ICollectionElement):

	def __init__(self) -> None:
		"""Creating a new Instance of this class is not allowed


		Raises:
			Exception: if this class is instanciated
		"""
		raise Exception("Creating a new Instance of this class is not allowed")
		pass

	@property
	def Flow(self) -> float:
		"""
		Returns:
			float: No Description
		"""
		pass

	@property
	def Head(self) -> float:
		"""
		Returns:
			float: No Description
		"""
		pass

	@Flow.setter
	def Flow(self, flow: float) -> None:
		pass

	@Head.setter
	def Head(self, head: float) -> None:
		pass

class IPumpCurveUnits(IElementUnits):

	def __init__(self) -> None:
		"""Creating a new Instance of this class is not allowed


		Raises:
			Exception: if this class is instanciated
		"""
		raise Exception("Creating a new Instance of this class is not allowed")
		pass

	@property
	def FlowUnit(self) -> IUnit:
		"""
		Returns:
			IUnit: No Description
		"""
		pass

	@property
	def HeadUnit(self) -> IUnit:
		"""
		Returns:
			IUnit: No Description
		"""
		pass

class IPumpDefinitionEfficiency:

	def __init__(self) -> None:
		"""Creating a new Instance of this class is not allowed


		Raises:
			Exception: if this class is instanciated
		"""
		raise Exception("Creating a new Instance of this class is not allowed")
		pass

	@property
	def PumpEfficiencyType(self) -> PumpEfficiencyTypeEnum:
		"""
		Returns:
			PumpEfficiencyTypeEnum: No Description
		"""
		pass

	@property
	def BEPFlow(self) -> float:
		"""
		Returns:
			float: No Description
		"""
		pass

	@property
	def BEPEfficiency(self) -> float:
		"""
		Returns:
			float: No Description
		"""
		pass

	@property
	def DefineBEPMaximumFlow(self) -> bool:
		"""
		Returns:
			bool: No Description
		"""
		pass

	@property
	def UserDefinedBEPMaximumFlow(self) -> float:
		"""
		Returns:
			float: No Description
		"""
		pass

	@property
	def ConstantEfficiency(self) -> float:
		"""
		Returns:
			float: No Description
		"""
		pass

	@property
	def FlowEfficiencyCurve(self) -> IFlowEfficiencyCollection:
		"""
		Returns:
			IFlowEfficiencyCollection: No Description
		"""
		pass

	@PumpEfficiencyType.setter
	def PumpEfficiencyType(self, pumpefficiencytype: PumpEfficiencyTypeEnum) -> None:
		pass

	@BEPFlow.setter
	def BEPFlow(self, bepflow: float) -> None:
		pass

	@BEPEfficiency.setter
	def BEPEfficiency(self, bepefficiency: float) -> None:
		pass

	@DefineBEPMaximumFlow.setter
	def DefineBEPMaximumFlow(self, definebepmaximumflow: bool) -> None:
		pass

	@UserDefinedBEPMaximumFlow.setter
	def UserDefinedBEPMaximumFlow(self, userdefinedbepmaximumflow: float) -> None:
		pass

	@ConstantEfficiency.setter
	def ConstantEfficiency(self, constantefficiency: float) -> None:
		pass

class IFlowEfficiencyCurveElement(ICollectionElement):

	def __init__(self) -> None:
		"""Creating a new Instance of this class is not allowed


		Raises:
			Exception: if this class is instanciated
		"""
		raise Exception("Creating a new Instance of this class is not allowed")
		pass

	@property
	def Flow(self) -> float:
		"""
		Returns:
			float: No Description
		"""
		pass

	@property
	def Efficiency(self) -> float:
		"""
		Returns:
			float: No Description
		"""
		pass

	@Flow.setter
	def Flow(self, flow: float) -> None:
		pass

	@Efficiency.setter
	def Efficiency(self, efficiency: float) -> None:
		pass

class IFlowEfficiencyCurve(ICollection[IFlowEfficiencyCurveElement]):

	def __init__(self) -> None:
		"""Creating a new Instance of this class is not allowed


		Raises:
			Exception: if this class is instanciated
		"""
		raise Exception("Creating a new Instance of this class is not allowed")
		pass

	def Add(self, flow: float, efficiency: float) -> IFlowEfficiencyCurveElement:
		"""Method Description

		Args:
			flow(float): flow
			efficiency(float): efficiency

		Returns:
			IFlowEfficiencyCurveElement: 
		"""
		pass

class IFlowEfficiencyUnits(IElementUnits):

	def __init__(self) -> None:
		"""Creating a new Instance of this class is not allowed


		Raises:
			Exception: if this class is instanciated
		"""
		raise Exception("Creating a new Instance of this class is not allowed")
		pass

	@property
	def FlowUnit(self) -> IUnit:
		"""
		Returns:
			IUnit: No Description
		"""
		pass

	@property
	def EfficiencyUnit(self) -> IUnit:
		"""
		Returns:
			IUnit: No Description
		"""
		pass

class IFlowEfficiencyCollection(ICollectionElements[IFlowEfficiencyCurve, IFlowEfficiencyCurveElement, IFlowEfficiencyUnits]):

	def __init__(self) -> None:
		"""Creating a new Instance of this class is not allowed


		Raises:
			Exception: if this class is instanciated
		"""
		raise Exception("Creating a new Instance of this class is not allowed")
		pass

class IPumpDefinitionNPSH:

	def __init__(self) -> None:
		"""Creating a new Instance of this class is not allowed


		Raises:
			Exception: if this class is instanciated
		"""
		raise Exception("Creating a new Instance of this class is not allowed")
		pass

	@property
	def UseNPSHCurve(self) -> bool:
		"""
		Returns:
			bool: No Description
		"""
		pass

	@property
	def NPSHCurveSafetyFactor(self) -> float:
		"""
		Returns:
			float: No Description
		"""
		pass

	@property
	def NPSHCurve(self) -> INPSHCurveCollection:
		"""
		Returns:
			INPSHCurveCollection: No Description
		"""
		pass

	@UseNPSHCurve.setter
	def UseNPSHCurve(self, usenpshcurve: bool) -> None:
		pass

	@NPSHCurveSafetyFactor.setter
	def NPSHCurveSafetyFactor(self, npshcurvesafetyfactor: float) -> None:
		pass

class IFlowNPSHr(ICollectionElement):

	def __init__(self) -> None:
		"""Creating a new Instance of this class is not allowed


		Raises:
			Exception: if this class is instanciated
		"""
		raise Exception("Creating a new Instance of this class is not allowed")
		pass

	@property
	def Flow(self) -> float:
		"""
		Returns:
			float: No Description
		"""
		pass

	@property
	def NPSHr(self) -> float:
		"""
		Returns:
			float: No Description
		"""
		pass

	@Flow.setter
	def Flow(self, flow: float) -> None:
		pass

	@NPSHr.setter
	def NPSHr(self, npshr: float) -> None:
		pass

class IFlowNPSHrCurve(ICollection[IFlowNPSHr]):

	def __init__(self) -> None:
		"""Creating a new Instance of this class is not allowed


		Raises:
			Exception: if this class is instanciated
		"""
		raise Exception("Creating a new Instance of this class is not allowed")
		pass

	def Add(self, flow: float, NPSHr: float) -> IFlowNPSHr:
		"""Method Description

		Args:
			flow(float): flow
			NPSHr(float): NPSHr

		Returns:
			IFlowNPSHr: 
		"""
		pass

class INPSHCurveUnits(IElementUnits):

	def __init__(self) -> None:
		"""Creating a new Instance of this class is not allowed


		Raises:
			Exception: if this class is instanciated
		"""
		raise Exception("Creating a new Instance of this class is not allowed")
		pass

	@property
	def FlowUnit(self) -> IUnit:
		"""
		Returns:
			IUnit: No Description
		"""
		pass

	@property
	def NPSHUnit(self) -> IUnit:
		"""
		Returns:
			IUnit: No Description
		"""
		pass

class INPSHCurveCollection(ICollectionElements[IFlowNPSHrCurve, IFlowNPSHr, INPSHCurveUnits]):

	def __init__(self) -> None:
		"""Creating a new Instance of this class is not allowed


		Raises:
			Exception: if this class is instanciated
		"""
		raise Exception("Creating a new Instance of this class is not allowed")
		pass

class IPumpDefinitionMotor:

	def __init__(self) -> None:
		"""Creating a new Instance of this class is not allowed


		Raises:
			Exception: if this class is instanciated
		"""
		raise Exception("Creating a new Instance of this class is not allowed")
		pass

	@property
	def IsVariableSpeedDrive(self) -> bool:
		"""
		Returns:
			bool: No Description
		"""
		pass

	@property
	def MotorEfficiency(self) -> float:
		"""
		Returns:
			float: No Description
		"""
		pass

	@property
	def SpeedEfficiencyCurve(self) -> ISpeedEfficiencyCurveCollection:
		"""
		Returns:
			ISpeedEfficiencyCurveCollection: No Description
		"""
		pass

	@IsVariableSpeedDrive.setter
	def IsVariableSpeedDrive(self, isvariablespeeddrive: bool) -> None:
		pass

	@MotorEfficiency.setter
	def MotorEfficiency(self, motorefficiency: float) -> None:
		pass

class ISpeedEfficiency(ICollectionElement):

	def __init__(self) -> None:
		"""Creating a new Instance of this class is not allowed


		Raises:
			Exception: if this class is instanciated
		"""
		raise Exception("Creating a new Instance of this class is not allowed")
		pass

	@property
	def Speed(self) -> float:
		"""
		Returns:
			float: No Description
		"""
		pass

	@property
	def Efficiency(self) -> float:
		"""
		Returns:
			float: No Description
		"""
		pass

	@Speed.setter
	def Speed(self, speed: float) -> None:
		pass

	@Efficiency.setter
	def Efficiency(self, efficiency: float) -> None:
		pass

class ISpeedEfficiencyCurve(ICollection[ISpeedEfficiency]):

	def __init__(self) -> None:
		"""Creating a new Instance of this class is not allowed


		Raises:
			Exception: if this class is instanciated
		"""
		raise Exception("Creating a new Instance of this class is not allowed")
		pass

	def Add(self, speed: float, efficiency: float) -> ISpeedEfficiency:
		"""Method Description

		Args:
			speed(float): speed
			efficiency(float): efficiency

		Returns:
			ISpeedEfficiency: 
		"""
		pass

class ISpeedEfficiencyUnits(IElementUnits):

	def __init__(self) -> None:
		"""Creating a new Instance of this class is not allowed


		Raises:
			Exception: if this class is instanciated
		"""
		raise Exception("Creating a new Instance of this class is not allowed")
		pass

	@property
	def SpeedUnit(self) -> IUnit:
		"""
		Returns:
			IUnit: No Description
		"""
		pass

	@property
	def EfficiencyUnit(self) -> IUnit:
		"""
		Returns:
			IUnit: No Description
		"""
		pass

class ISpeedEfficiencyCurveCollection(ICollectionElements[ISpeedEfficiencyCurve, ISpeedEfficiency, ISpeedEfficiencyUnits]):

	def __init__(self) -> None:
		"""Creating a new Instance of this class is not allowed


		Raises:
			Exception: if this class is instanciated
		"""
		raise Exception("Creating a new Instance of this class is not allowed")
		pass

class IConstituent(IWaterComponentBase[IConstituents, IConstituent, IConstituentUnits]):

	def __init__(self) -> None:
		"""Creating a new Instance of this class is not allowed


		Raises:
			Exception: if this class is instanciated
		"""
		raise Exception("Creating a new Instance of this class is not allowed")
		pass

	@property
	def Diffusivity(self) -> float:
		"""
		Returns:
			float: No Description
		"""
		pass

	@property
	def HasUnlimitedConcentration(self) -> bool:
		"""
		Returns:
			bool: No Description
		"""
		pass

	@property
	def ConcentrationLimit(self) -> float:
		"""
		Returns:
			float: No Description
		"""
		pass

	@property
	def BulkReactionOrder(self) -> int:
		"""
		Returns:
			int: No Description
		"""
		pass

	@property
	def BulkReactionRate(self) -> float:
		"""
		Returns:
			float: No Description
		"""
		pass

	@property
	def IsRoughnessCorrelated(self) -> bool:
		"""
		Returns:
			bool: No Description
		"""
		pass

	@property
	def RoughnessCorrelationFactor(self) -> float:
		"""
		Returns:
			float: No Description
		"""
		pass

	@property
	def WallReactionOrder(self) -> WallReactionOrder:
		"""
		Returns:
			WallReactionOrder: No Description
		"""
		pass

	@property
	def ZeroOrderWallReactionRate(self) -> float:
		"""
		Returns:
			float: No Description
		"""
		pass

	@property
	def FirstOrderWallReactionRate(self) -> float:
		"""
		Returns:
			float: No Description
		"""
		pass

	@Diffusivity.setter
	def Diffusivity(self, diffusivity: float) -> None:
		pass

	@HasUnlimitedConcentration.setter
	def HasUnlimitedConcentration(self, hasunlimitedconcentration: bool) -> None:
		pass

	@ConcentrationLimit.setter
	def ConcentrationLimit(self, concentrationlimit: float) -> None:
		pass

	@BulkReactionOrder.setter
	def BulkReactionOrder(self, bulkreactionorder: int) -> None:
		pass

	@BulkReactionRate.setter
	def BulkReactionRate(self, bulkreactionrate: float) -> None:
		pass

	@IsRoughnessCorrelated.setter
	def IsRoughnessCorrelated(self, isroughnesscorrelated: bool) -> None:
		pass

	@RoughnessCorrelationFactor.setter
	def RoughnessCorrelationFactor(self, roughnesscorrelationfactor: float) -> None:
		pass

	@WallReactionOrder.setter
	def WallReactionOrder(self, wallreactionorder: WallReactionOrder) -> None:
		pass

	@ZeroOrderWallReactionRate.setter
	def ZeroOrderWallReactionRate(self, zeroorderwallreactionrate: float) -> None:
		pass

	@FirstOrderWallReactionRate.setter
	def FirstOrderWallReactionRate(self, firstorderwallreactionrate: float) -> None:
		pass

class IConstituents(IWaterComponentsBase[IConstituents, IConstituent, IConstituentUnits]):

	def __init__(self) -> None:
		"""Creating a new Instance of this class is not allowed


		Raises:
			Exception: if this class is instanciated
		"""
		raise Exception("Creating a new Instance of this class is not allowed")
		pass

class IConstituentUnits(IElementUnits):

	def __init__(self) -> None:
		"""Creating a new Instance of this class is not allowed


		Raises:
			Exception: if this class is instanciated
		"""
		raise Exception("Creating a new Instance of this class is not allowed")
		pass

class IUnitDemandLoad(IWaterComponentBase[IUnitDemandLoads, IUnitDemandLoad, IUnitDemandLoadUnits]):

	def __init__(self) -> None:
		"""Creating a new Instance of this class is not allowed


		Raises:
			Exception: if this class is instanciated
		"""
		raise Exception("Creating a new Instance of this class is not allowed")
		pass

	@property
	def UnitDemand(self) -> float:
		"""
		Returns:
			float: No Description
		"""
		pass

	@property
	def UnitDemandType(self) -> UnitDemandLoadTypeEnum:
		"""
		Returns:
			UnitDemandLoadTypeEnum: No Description
		"""
		pass

	@property
	def PopulationUnit(self) -> PopulationUnit:
		"""
		Returns:
			PopulationUnit: No Description
		"""
		pass

	@property
	def AreaUnit(self) -> AreaUnit:
		"""
		Returns:
			AreaUnit: No Description
		"""
		pass

	@property
	def CountUnit(self) -> str:
		"""
		Returns:
			str: No Description
		"""
		pass

	@property
	def ReportPopulationEquivalent(self) -> bool:
		"""
		Returns:
			bool: No Description
		"""
		pass

	@property
	def PopulationEquivalent(self) -> float:
		"""
		Returns:
			float: No Description
		"""
		pass

	@UnitDemand.setter
	def UnitDemand(self, unitdemand: float) -> None:
		pass

	@UnitDemandType.setter
	def UnitDemandType(self, unitdemandtype: UnitDemandLoadTypeEnum) -> None:
		pass

	@PopulationUnit.setter
	def PopulationUnit(self, populationunit: PopulationUnit) -> None:
		pass

	@AreaUnit.setter
	def AreaUnit(self, areaunit: AreaUnit) -> None:
		pass

	@CountUnit.setter
	def CountUnit(self, countunit: str) -> None:
		pass

	@ReportPopulationEquivalent.setter
	def ReportPopulationEquivalent(self, reportpopulationequivalent: bool) -> None:
		pass

	@PopulationEquivalent.setter
	def PopulationEquivalent(self, populationequivalent: float) -> None:
		pass

class IUnitDemandLoads(IWaterComponentsBase[IUnitDemandLoads, IUnitDemandLoad, IUnitDemandLoadUnits]):

	def __init__(self) -> None:
		"""Creating a new Instance of this class is not allowed


		Raises:
			Exception: if this class is instanciated
		"""
		raise Exception("Creating a new Instance of this class is not allowed")
		pass

class IUnitDemandLoadUnits(IElementUnits):

	def __init__(self) -> None:
		"""Creating a new Instance of this class is not allowed


		Raises:
			Exception: if this class is instanciated
		"""
		raise Exception("Creating a new Instance of this class is not allowed")
		pass

class ISCADASignal(IWaterComponentBase[ISCADASignals, ISCADASignal, IElementUnits]):

	def __init__(self) -> None:
		"""Creating a new Instance of this class is not allowed


		Raises:
			Exception: if this class is instanciated
		"""
		raise Exception("Creating a new Instance of this class is not allowed")
		pass

	@property
	def ScadaDatasourceID(self) -> int:
		"""
		Returns:
			int: No Description
		"""
		pass

	@property
	def SignalLabel(self) -> str:
		"""
		Returns:
			str: No Description
		"""
		pass

	@property
	def IsDerived(self) -> bool:
		"""
		Returns:
			bool: No Description
		"""
		pass

	@property
	def Formula(self) -> str:
		"""
		Returns:
			str: No Description
		"""
		pass

	@property
	def TransformMethod(self) -> SCADASignalTransformMethod:
		"""
		Returns:
			SCADASignalTransformMethod: No Description
		"""
		pass

	@SignalLabel.setter
	def SignalLabel(self, signallabel: str) -> None:
		pass

	@IsDerived.setter
	def IsDerived(self, isderived: bool) -> None:
		pass

	@Formula.setter
	def Formula(self, formula: str) -> None:
		pass

	@TransformMethod.setter
	def TransformMethod(self, transformmethod: SCADASignalTransformMethod) -> None:
		pass

class ISCADASignals(IWaterComponentsBase[ISCADASignals, ISCADASignal, IElementUnits]):

	def __init__(self) -> None:
		"""Creating a new Instance of this class is not allowed


		Raises:
			Exception: if this class is instanciated
		"""
		raise Exception("Creating a new Instance of this class is not allowed")
		pass

class IGPVHeadlossCurve(IWaterComponentBase[IGPVHeadlossCurves, IGPVHeadlossCurve, IGPVHeadlossUnits]):

	def __init__(self) -> None:
		"""Creating a new Instance of this class is not allowed


		Raises:
			Exception: if this class is instanciated
		"""
		raise Exception("Creating a new Instance of this class is not allowed")
		pass

	@property
	def GPVHeadlossFlowCurve(self) -> IGPVFlowHeadlossCurveCollection:
		"""
		Returns:
			IGPVFlowHeadlossCurveCollection: No Description
		"""
		pass

class IGPVHeadlossCurves(IWaterComponentsBase[IGPVHeadlossCurves, IGPVHeadlossCurve, IGPVHeadlossUnits]):

	def __init__(self) -> None:
		"""Creating a new Instance of this class is not allowed


		Raises:
			Exception: if this class is instanciated
		"""
		raise Exception("Creating a new Instance of this class is not allowed")
		pass

class IGPVHeadlossUnits(IElementUnits):

	def __init__(self) -> None:
		"""Creating a new Instance of this class is not allowed


		Raises:
			Exception: if this class is instanciated
		"""
		raise Exception("Creating a new Instance of this class is not allowed")
		pass

class IGPVFlowHeadloss(ICollectionElement):

	def __init__(self) -> None:
		"""Creating a new Instance of this class is not allowed


		Raises:
			Exception: if this class is instanciated
		"""
		raise Exception("Creating a new Instance of this class is not allowed")
		pass

	@property
	def Flow(self) -> float:
		"""
		Returns:
			float: No Description
		"""
		pass

	@property
	def Headloss(self) -> float:
		"""
		Returns:
			float: No Description
		"""
		pass

	@Flow.setter
	def Flow(self, flow: float) -> None:
		pass

	@Headloss.setter
	def Headloss(self, headloss: float) -> None:
		pass

class IGPVFlowHeadlossCurve(ICollection[IGPVFlowHeadloss]):

	def __init__(self) -> None:
		"""Creating a new Instance of this class is not allowed


		Raises:
			Exception: if this class is instanciated
		"""
		raise Exception("Creating a new Instance of this class is not allowed")
		pass

	def Add(self, flow: float, headloss: float) -> IGPVFlowHeadloss:
		"""Method Description

		Args:
			flow(float): flow
			headloss(float): headloss

		Returns:
			IGPVFlowHeadloss: 
		"""
		pass

class IGPVFlowHeadlossCurveCollection(ICollectionElements[IGPVFlowHeadlossCurve, IGPVFlowHeadloss, IGPVFlowHeadlossUnits]):

	def __init__(self) -> None:
		"""Creating a new Instance of this class is not allowed


		Raises:
			Exception: if this class is instanciated
		"""
		raise Exception("Creating a new Instance of this class is not allowed")
		pass

class IGPVFlowHeadlossUnits(IElementUnits):

	def __init__(self) -> None:
		"""Creating a new Instance of this class is not allowed


		Raises:
			Exception: if this class is instanciated
		"""
		raise Exception("Creating a new Instance of this class is not allowed")
		pass

	@property
	def Flow(self) -> IUnit:
		"""
		Returns:
			IUnit: No Description
		"""
		pass

	@property
	def Headloss(self) -> IUnit:
		"""
		Returns:
			IUnit: No Description
		"""
		pass

class IValveCharacteristic(IWaterComponentBase[IValveCharacteristics, IValveCharacteristic, IValveCharacteristicUnits]):

	def __init__(self) -> None:
		"""Creating a new Instance of this class is not allowed


		Raises:
			Exception: if this class is instanciated
		"""
		raise Exception("Creating a new Instance of this class is not allowed")
		pass

	@property
	def ValveCharacteristicsCurve(self) -> IValveCharacteristicsCurveCollection:
		"""
		Returns:
			IValveCharacteristicsCurveCollection: No Description
		"""
		pass

class IValveCharacteristics(IWaterComponentsBase[IValveCharacteristics, IValveCharacteristic, IValveCharacteristicUnits]):

	def __init__(self) -> None:
		"""Creating a new Instance of this class is not allowed


		Raises:
			Exception: if this class is instanciated
		"""
		raise Exception("Creating a new Instance of this class is not allowed")
		pass

class IValveCharacteristicUnits(IElementUnits):

	def __init__(self) -> None:
		"""Creating a new Instance of this class is not allowed


		Raises:
			Exception: if this class is instanciated
		"""
		raise Exception("Creating a new Instance of this class is not allowed")
		pass

class IRelativeClosureRelativeArea(ICollectionElement):

	def __init__(self) -> None:
		"""Creating a new Instance of this class is not allowed


		Raises:
			Exception: if this class is instanciated
		"""
		raise Exception("Creating a new Instance of this class is not allowed")
		pass

	@property
	def RelativeClosure(self) -> float:
		"""
		Returns:
			float: No Description
		"""
		pass

	@property
	def RelativeArea(self) -> float:
		"""
		Returns:
			float: No Description
		"""
		pass

	@RelativeClosure.setter
	def RelativeClosure(self, relativeclosure: float) -> None:
		pass

	@RelativeArea.setter
	def RelativeArea(self, relativearea: float) -> None:
		pass

class IRelativeClosureRelativeAreas(ICollection[IRelativeClosureRelativeArea]):

	def __init__(self) -> None:
		"""Creating a new Instance of this class is not allowed


		Raises:
			Exception: if this class is instanciated
		"""
		raise Exception("Creating a new Instance of this class is not allowed")
		pass

	def Add(self, relativeClosure: float, relativeArea: float) -> IRelativeClosureRelativeArea:
		"""Method Description

		Args:
			relativeClosure(float): relativeClosure
			relativeArea(float): relativeArea

		Returns:
			IRelativeClosureRelativeArea: 
		"""
		pass

class IValveCharacteristicsCurveCollection(ICollectionElements[IRelativeClosureRelativeAreas, IRelativeClosureRelativeArea, IRelativeClosureRelativeAreaUnits]):

	def __init__(self) -> None:
		"""Creating a new Instance of this class is not allowed


		Raises:
			Exception: if this class is instanciated
		"""
		raise Exception("Creating a new Instance of this class is not allowed")
		pass

class IRelativeClosureRelativeAreaUnits(IElementUnits):

	def __init__(self) -> None:
		"""Creating a new Instance of this class is not allowed


		Raises:
			Exception: if this class is instanciated
		"""
		raise Exception("Creating a new Instance of this class is not allowed")
		pass

	@property
	def ClosureUnit(self) -> IUnit:
		"""
		Returns:
			IUnit: No Description
		"""
		pass

	@property
	def AreaUnit(self) -> IUnit:
		"""
		Returns:
			IUnit: No Description
		"""
		pass

class IMinorLossCoefficients(IWaterComponentsBase[IMinorLossCoefficients, IMinorLossCoefficient, IMinorLossCoefficientUnits]):

	def __init__(self) -> None:
		"""Creating a new Instance of this class is not allowed


		Raises:
			Exception: if this class is instanciated
		"""
		raise Exception("Creating a new Instance of this class is not allowed")
		pass

class IMinorLossCoefficient(IWaterComponentBase[IMinorLossCoefficients, IMinorLossCoefficient, IMinorLossCoefficientUnits]):

	def __init__(self) -> None:
		"""Creating a new Instance of this class is not allowed


		Raises:
			Exception: if this class is instanciated
		"""
		raise Exception("Creating a new Instance of this class is not allowed")
		pass

	@property
	def MinorLossType(self) -> MinorLossTypeEnum:
		"""
		Returns:
			MinorLossTypeEnum: No Description
		"""
		pass

	@property
	def MinorLoss(self) -> float:
		"""
		Returns:
			float: No Description
		"""
		pass

	@MinorLossType.setter
	def MinorLossType(self, minorlosstype: MinorLossTypeEnum) -> None:
		pass

	@MinorLoss.setter
	def MinorLoss(self, minorloss: float) -> None:
		pass

class IMinorLossCoefficientUnits(IElementUnits):

	def __init__(self) -> None:
		"""Creating a new Instance of this class is not allowed


		Raises:
			Exception: if this class is instanciated
		"""
		raise Exception("Creating a new Instance of this class is not allowed")
		pass

	@property
	def CoefficientUnit(self) -> IUnit:
		"""
		Returns:
			IUnit: No Description
		"""
		pass

class IWaterModelSupport(IModelComponents[IWaterComponent, WaterComponentType]):

	def __init__(self) -> None:
		"""Creating a new Instance of this class is not allowed


		Raises:
			Exception: if this class is instanciated
		"""
		raise Exception("Creating a new Instance of this class is not allowed")
		pass

	def SCADASignals(self, dataSourceID: int) -> ISCADASignals:
		"""Method Description

		Args:
			dataSourceID(int): dataSourceID

		Returns:
			ISCADASignals: 
		"""
		pass

	@property
	def Zones(self) -> IZones:
		"""
		Returns:
			IZones: No Description
		"""
		pass

	@property
	def Patterns(self) -> IPatterns:
		"""
		Returns:
			IPatterns: No Description
		"""
		pass

	@property
	def PumpDefinitions(self) -> IPumpDefinitions:
		"""
		Returns:
			IPumpDefinitions: No Description
		"""
		pass

	@property
	def Constituents(self) -> IConstituents:
		"""
		Returns:
			IConstituents: No Description
		"""
		pass

	@property
	def UnitDemandLoads(self) -> IUnitDemandLoads:
		"""
		Returns:
			IUnitDemandLoads: No Description
		"""
		pass

	@property
	def Controls(self) -> IControls:
		"""
		Returns:
			IControls: No Description
		"""
		pass

	@property
	def ControlConditions(self) -> IControlConditions:
		"""
		Returns:
			IControlConditions: No Description
		"""
		pass

	@property
	def ControlActions(self) -> IControlActions:
		"""
		Returns:
			IControlActions: No Description
		"""
		pass

	@property
	def AirFlowCurves(self) -> IAirFlowCurves:
		"""
		Returns:
			IAirFlowCurves: No Description
		"""
		pass

	@property
	def GPVHeadlossCurves(self) -> IGPVHeadlossCurves:
		"""
		Returns:
			IGPVHeadlossCurves: No Description
		"""
		pass

	@property
	def ValveCharacteristics(self) -> IValveCharacteristics:
		"""
		Returns:
			IValveCharacteristics: No Description
		"""
		pass

	@property
	def MinorLossCoefficients(self) -> IMinorLossCoefficients:
		"""
		Returns:
			IMinorLossCoefficients: No Description
		"""
		pass

