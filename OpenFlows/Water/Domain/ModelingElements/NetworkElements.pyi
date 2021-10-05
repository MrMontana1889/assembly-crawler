from OpenFlows.Domain.ModelingElements.Collections import ICollectionElement, ICollection, ICollectionElements
from OpenFlows.Water.Domain.ModelingElements.Components import IMinorLossCoefficient, IPattern, IPumpDefinition, IValveCharacteristic, IGPVHeadlossCurve, TElementManagerType, TElementType, TUnitsType, IZone, IUnitDemandLoad, IAirFlowCurve, ISCADASignal
from OpenFlows.Domain.ModelingElements import IElementUnits, IElementsResults, IElementResults, IElement, IGeometryUnits, TElementManagerType, TElementType, TUnitsType
from typing import overload, Dict, List, Union, Generic
from array import array
from OpenFlows.Units import IUnit
from OpenFlows.Domain.ModelingElements.NetworkElements import INetworkElements, TElementInputType, TElementResultsType, TElementsInputType, TElementsResultsType, IActiveElementInput, IActiveElementsInput, INetworkElement, IBaseLinksResults, IBaseLinkResults, IBaseLinkInput, IBaseLinksInput, IBaseLinkUnits, IPointNodeInput, IPointNodesInput, IBasePolygonsInput, IBasePolygonsResults, IBasePolygonResults, IBasePolygonInput
from OpenFlows.Domain.DataObjects import INetwork
from OpenFlows.Water.Enumerations import *


class IMinorLoss(ICollectionElement):

	def __init__(self) -> None:
		"""Creating a new Instance of this class is not allowed


		Raises:
			Exception: if this class is instanciated
		"""
		raise Exception("Creating a new Instance of this class is not allowed")
		pass

	@property
	def Quantity(self) -> int:
		"""No Description

		Returns:
			IMinorLoss: 
		"""
		pass

	@property
	def MinorLossCoefficient(self) -> IMinorLossCoefficient:
		"""No Description

		Returns:
			IMinorLoss: 
		"""
		pass

	@Quantity.setter
	def Quantity(self, quantity: int) -> None:
		pass

	@MinorLossCoefficient.setter
	def MinorLossCoefficient(self, minorlosscoefficient: IMinorLossCoefficient) -> None:
		pass

class IMinorLosses(ICollection[IMinorLoss]):

	def __init__(self) -> None:
		"""Creating a new Instance of this class is not allowed


		Raises:
			Exception: if this class is instanciated
		"""
		raise Exception("Creating a new Instance of this class is not allowed")
		pass

	def Add(self, quantity: int, minorLoss: IMinorLossCoefficient) -> IMinorLoss:
		"""Adds a new row to the collection given the data.

		Args:
			quantity(int): quantity
			minorLoss(IMinorLossCoefficient): minorLoss

		Returns:
			IMinorLoss: 
		"""
		pass

class IMinorLossCoefficientCollection(ICollectionElements[IMinorLosses, IMinorLoss, IMinorLossCollectionUnits]):

	def __init__(self) -> None:
		"""Creating a new Instance of this class is not allowed


		Raises:
			Exception: if this class is instanciated
		"""
		raise Exception("Creating a new Instance of this class is not allowed")
		pass

class IMinorLossCollectionUnits(IElementUnits):

	def __init__(self) -> None:
		"""Creating a new Instance of this class is not allowed


		Raises:
			Exception: if this class is instanciated
		"""
		raise Exception("Creating a new Instance of this class is not allowed")
		pass

class IBaseDirectedNodesResults(IElementsResults, IWaterQualityElementsResults):

	def __init__(self) -> None:
		"""Creating a new Instance of this class is not allowed


		Raises:
			Exception: if this class is instanciated
		"""
		raise Exception("Creating a new Instance of this class is not allowed")
		pass

	@overload
	def IBaseDirectedNodesResults(self) -> Dict[int,int]:
		"""Gets 'cannot deliver flow or head' for all directed nodes for the current time step.

		Returns:
			Dict[int,int]: 
		"""
		pass

	@overload
	def IBaseDirectedNodesResults(self, timeStepIndex: int) -> Dict[int,int]:
		"""Gets 'cannot deliver flow or head' for all directed nodes for the given time step.

		Args:
			timeStepIndex(int): timeStepIndex

		Returns:
			Dict[int,int]: 
		"""
		pass

	@overload
	def IBaseDirectedNodesResults(self, ids: List[int], timeStepIndex: int) -> Dict[int,int]:
		"""No Description

		Args:
			ids(List[int]): ids
			timeStepIndex(int): timeStepIndex

		Returns:
			Dict[int,int]: 
		"""
		pass

	@overload
	def IBaseDirectedNodesResults(self) -> Dict[int,int]:
		"""Set to true for all directed nodes if open during the current time step.

		Returns:
			Dict[int,int]: 
		"""
		pass

	@overload
	def IBaseDirectedNodesResults(self, timeStepIndex: int) -> Dict[int,int]:
		"""Set to true for all directed nodes if open during the given time step.

		Args:
			timeStepIndex(int): timeStepIndex

		Returns:
			Dict[int,int]: 
		"""
		pass

	@overload
	def IBaseDirectedNodesResults(self, ids: List[int], timeStepIndex: int) -> Dict[int,int]:
		"""No Description

		Args:
			ids(List[int]): ids
			timeStepIndex(int): timeStepIndex

		Returns:
			Dict[int,int]: 
		"""
		pass

class IBaseDirectedNodeResults(IElementResults, IWaterQualityResults):

	def __init__(self) -> None:
		"""Creating a new Instance of this class is not allowed


		Raises:
			Exception: if this class is instanciated
		"""
		raise Exception("Creating a new Instance of this class is not allowed")
		pass

	@overload
	def IBaseDirectedNodeResults(self) -> Union[bool, None]:
		"""If true then the cannot deliver head or cannot deliver flow warning was generated for the element for the current time step.

		Returns:
			Nullable: 
		"""
		pass

	@overload
	def IBaseDirectedNodeResults(self, timeStepIndex: int) -> Union[bool, None]:
		"""If true then the cannot deliver head or cannot deliver flow warning was generated for the element for the given time step.

		Args:
			timeStepIndex(int): timeStepIndex

		Returns:
			Nullable: 
		"""
		pass

	@overload
	def IBaseDirectedNodeResults(self) -> Union[bool, None]:
		"""Set to true if open during the current time step.

		Returns:
			Nullable: 
		"""
		pass

	@overload
	def IBaseDirectedNodeResults(self, timeStepIndex: int) -> Union[bool, None]:
		"""Set to true if open during the given time step.

		Args:
			timeStepIndex(int): timeStepIndex

		Returns:
			Nullable: 
		"""
		pass

	def CannotDeliverFlowsOrHeads(self) -> array(Union[bool, None]):
		"""If true then the pump cannot deliver head or cannot deliver flow warning was generated for the element across all time steps.

		Returns:
			array(): 
		"""
		pass

	def IsOpens(self) -> array(Union[bool, None]):
		"""Set to true if open during across all time steps.

		Returns:
			array(): 
		"""
		pass

class IBaseDirectedNodeInput(IPhysicalNodeElementInput, IWaterZoneableNetworkElementInput, IWaterQualityElementInput):

	def __init__(self) -> None:
		"""Creating a new Instance of this class is not allowed


		Raises:
			Exception: if this class is instanciated
		"""
		raise Exception("Creating a new Instance of this class is not allowed")
		pass

	@property
	def DownstreamLink(self) -> IElement:
		"""No Description

		Returns:
			IBaseDirectedNodeInput: 
		"""
		pass

	@property
	def InstallationYear(self) -> int:
		"""No Description

		Returns:
			IBaseDirectedNodeInput: 
		"""
		pass

	@DownstreamLink.setter
	def DownstreamLink(self, downstreamlink: IElement) -> None:
		pass

	@InstallationYear.setter
	def InstallationYear(self, installationyear: int) -> None:
		pass

class IBaseDirectedNodesInput(IWaterZoneableNetworkElementsInput, IWaterQualityElementsInput, IPhysicalNodeElementsInput):

	def __init__(self) -> None:
		"""Creating a new Instance of this class is not allowed


		Raises:
			Exception: if this class is instanciated
		"""
		raise Exception("Creating a new Instance of this class is not allowed")
		pass

	@overload
	def IBaseDirectedNodesInput(self) -> Dict[int,int]:
		"""Specify the install year of the element.  It does not affect the calculations.

		Returns:
			Dict[int,int]: 
		"""
		pass

	@overload
	def IBaseDirectedNodesInput(self, ids: List[int]) -> Dict[int,int]:
		"""No Description

		Args:
			ids(List[int]): ids

		Returns:
			Dict[int,int]: 
		"""
		pass

class IBaseDirectedNodeUnits(IElementResults, IWaterQualityResultsUnits, IGeometryUnits):

	def __init__(self) -> None:
		"""Creating a new Instance of this class is not allowed


		Raises:
			Exception: if this class is instanciated
		"""
		raise Exception("Creating a new Instance of this class is not allowed")
		pass

	@property
	def ElevationUnit(self) -> IUnit:
		"""No Description

		Returns:
			IBaseDirectedNodeUnits: 
		"""
		pass

class ICheckValveElementInput(IBaseDirectedNodeInput):

	def __init__(self) -> None:
		"""Creating a new Instance of this class is not allowed


		Raises:
			Exception: if this class is instanciated
		"""
		raise Exception("Creating a new Instance of this class is not allowed")
		pass

	@property
	def LocatedAtWye(self) -> bool:
		"""No Description

		Returns:
			ICheckValveElementInput: 
		"""
		pass

	@property
	def CheckValvePipeWithWye(self) -> IPipe:
		"""No Description

		Returns:
			ICheckValveElementInput: 
		"""
		pass

	@property
	def FlowDirection(self) -> CheckValveFlowDirectionEnum:
		"""No Description

		Returns:
			ICheckValveElementInput: 
		"""
		pass

	@property
	def InitialTypicalFlow(self) -> float:
		"""No Description

		Returns:
			ICheckValveElementInput: 
		"""
		pass

	@property
	def ThresholdPressure(self) -> float:
		"""No Description

		Returns:
			ICheckValveElementInput: 
		"""
		pass

	@property
	def ClosureTime(self) -> float:
		"""No Description

		Returns:
			ICheckValveElementInput: 
		"""
		pass

	@property
	def OpenTime(self) -> float:
		"""No Description

		Returns:
			ICheckValveElementInput: 
		"""
		pass

	@property
	def AllowDisruptionOfOperation(self) -> bool:
		"""No Description

		Returns:
			ICheckValveElementInput: 
		"""
		pass

	@LocatedAtWye.setter
	def LocatedAtWye(self, locatedatwye: bool) -> None:
		pass

	@CheckValvePipeWithWye.setter
	def CheckValvePipeWithWye(self, checkvalvepipewithwye: IPipe) -> None:
		pass

	@FlowDirection.setter
	def FlowDirection(self, flowdirection: CheckValveFlowDirectionEnum) -> None:
		pass

	@InitialTypicalFlow.setter
	def InitialTypicalFlow(self, initialtypicalflow: float) -> None:
		pass

	@ThresholdPressure.setter
	def ThresholdPressure(self, thresholdpressure: float) -> None:
		pass

	@ClosureTime.setter
	def ClosureTime(self, closuretime: float) -> None:
		pass

	@OpenTime.setter
	def OpenTime(self, opentime: float) -> None:
		pass

	@AllowDisruptionOfOperation.setter
	def AllowDisruptionOfOperation(self, allowdisruptionofoperation: bool) -> None:
		pass

class ICheckValveElementsInput(IBaseDirectedNodesInput):

	def __init__(self) -> None:
		"""Creating a new Instance of this class is not allowed


		Raises:
			Exception: if this class is instanciated
		"""
		raise Exception("Creating a new Instance of this class is not allowed")
		pass

	@overload
	def ICheckValveElementsInput(self) -> Dict[int,int]:
		"""Specifies whether the check valve is simulated as a simple check valve in a run of pipe, or if it is simulated as a wye connection.

		Returns:
			Dict[int,int]: 
		"""
		pass

	@overload
	def ICheckValveElementsInput(self, ids: List[int]) -> Dict[int,int]:
		"""No Description

		Args:
			ids(List[int]): ids

		Returns:
			Dict[int,int]: 
		"""
		pass

	@overload
	def ICheckValveElementsInput(self) -> Dict[int,int]:
		"""Denotes the allowable flow direction through the valve: - towards the wye branch, - away from the wye branch.

		Returns:
			Dict[int,int]: 
		"""
		pass

	@overload
	def ICheckValveElementsInput(self, ids: List[int]) -> Dict[int,int]:
		"""No Description

		Args:
			ids(List[int]): ids

		Returns:
			Dict[int,int]: 
		"""
		pass

	@overload
	def ICheckValveElementsInput(self) -> Dict[int,int]:
		"""This value is 0 should the valve be initially closed.

		Returns:
			Dict[int,int]: 
		"""
		pass

	@overload
	def ICheckValveElementsInput(self, ids: List[int]) -> Dict[int,int]:
		"""No Description

		Args:
			ids(List[int]): ids

		Returns:
			Dict[int,int]: 
		"""
		pass

	@overload
	def ICheckValveElementsInput(self) -> Dict[int,int]:
		"""The pressure difference between upstream and downstream side to (re)open the (closed) valve. If 0 is entered, 
            the valve (re)opens when the upstream pressure exceeds the downstream pressure.

		Returns:
			Dict[int,int]: 
		"""
		pass

	@overload
	def ICheckValveElementsInput(self, ids: List[int]) -> Dict[int,int]:
		"""No Description

		Args:
			ids(List[int]): ids

		Returns:
			Dict[int,int]: 
		"""
		pass

	@overload
	def ICheckValveElementsInput(self) -> Dict[int,int]:
		"""Time to close the valve, from the fully open position, after reverse flow is sensed. This establishes the rate of 
            closure in case the valve's opening is partial.

		Returns:
			Dict[int,int]: 
		"""
		pass

	@overload
	def ICheckValveElementsInput(self, ids: List[int]) -> Dict[int,int]:
		"""No Description

		Args:
			ids(List[int]): ids

		Returns:
			Dict[int,int]: 
		"""
		pass

	@overload
	def ICheckValveElementsInput(self) -> Dict[int,int]:
		"""Time to open the valve, from the fully closed position, after specified pressure difference is exceeded. This 
            establishes the rate of opening in case the valve's closure is partial.

		Returns:
			Dict[int,int]: 
		"""
		pass

	@overload
	def ICheckValveElementsInput(self, ids: List[int]) -> Dict[int,int]:
		"""No Description

		Args:
			ids(List[int]): ids

		Returns:
			Dict[int,int]: 
		"""
		pass

	@overload
	def ICheckValveElementsInput(self) -> Dict[int,int]:
		"""Determines whether an operation (opening or closing) can be terminated prematurely due to a signal to reverse.

		Returns:
			Dict[int,int]: 
		"""
		pass

	@overload
	def ICheckValveElementsInput(self, ids: List[int]) -> Dict[int,int]:
		"""No Description

		Args:
			ids(List[int]): ids

		Returns:
			Dict[int,int]: 
		"""
		pass

class ICheckValveElementResults(IBaseDirectedNodeResults):

	def __init__(self) -> None:
		"""Creating a new Instance of this class is not allowed


		Raises:
			Exception: if this class is instanciated
		"""
		raise Exception("Creating a new Instance of this class is not allowed")
		pass

	@overload
	def ICheckValveElementResults(self) -> Union[float, None]:
		"""Total flow through the check valve.

		Returns:
			Nullable: 
		"""
		pass

	@overload
	def ICheckValveElementResults(self, timeStepIndex: int) -> Union[float, None]:
		"""Total flow through the check valve.

		Args:
			timeStepIndex(int): timeStepIndex

		Returns:
			Nullable: 
		"""
		pass

	@overload
	def ICheckValveElementResults(self) -> Union[float, None]:
		"""Magnitude of flow through the selected check valve.

		Returns:
			Nullable: 
		"""
		pass

	@overload
	def ICheckValveElementResults(self, timeStepIndex: int) -> Union[float, None]:
		"""Magnitude of flow through the selected check valve.

		Args:
			timeStepIndex(int): timeStepIndex

		Returns:
			Nullable: 
		"""
		pass

	@overload
	def ICheckValveElementResults(self) -> Union[float, None]:
		"""Calculated pressure at the check valve.

		Returns:
			Nullable: 
		"""
		pass

	@overload
	def ICheckValveElementResults(self, timeStepIndex: int) -> Union[float, None]:
		"""Calculated pressure at the check valve.

		Args:
			timeStepIndex(int): timeStepIndex

		Returns:
			Nullable: 
		"""
		pass

	@overload
	def ICheckValveElementResults(self) -> Union[float, None]:
		"""Calculated hydraulic grade at the check valve.

		Returns:
			Nullable: 
		"""
		pass

	@overload
	def ICheckValveElementResults(self, timeStepIndex: int) -> Union[float, None]:
		"""Calculated hydraulic grade at the check valve.

		Args:
			timeStepIndex(int): timeStepIndex

		Returns:
			Nullable: 
		"""
		pass

	def Flows(self) -> array(Union[float, None]):
		"""Total flow through the check valve.

		Returns:
			array(): 
		"""
		pass

	def AbsoluteFlows(self) -> array(Union[float, None]):
		"""Magnitude of flow through the selected check valve.

		Returns:
			array(): 
		"""
		pass

	def Pressures(self) -> array(Union[float, None]):
		"""Calculated pressure at the check valve.

		Returns:
			array(): 
		"""
		pass

	def HydraulicGrades(self) -> array(Union[float, None]):
		"""Calculated hydraulic grade at the check valve.

		Returns:
			array(): 
		"""
		pass

class ICheckValveElementsResults(IBaseDirectedNodesResults):

	def __init__(self) -> None:
		"""Creating a new Instance of this class is not allowed


		Raises:
			Exception: if this class is instanciated
		"""
		raise Exception("Creating a new Instance of this class is not allowed")
		pass

	@overload
	def ICheckValveElementsResults(self) -> Dict[int,int]:
		"""Total flow through the check valve.

		Returns:
			Dict[int,int]: 
		"""
		pass

	@overload
	def ICheckValveElementsResults(self, timeStepIndex: int) -> Dict[int,int]:
		"""Total flow through the check valve.

		Args:
			timeStepIndex(int): timeStepIndex

		Returns:
			Dict[int,int]: 
		"""
		pass

	@overload
	def ICheckValveElementsResults(self, ids: List[int], timeStepIndex: int) -> Dict[int,int]:
		"""No Description

		Args:
			ids(List[int]): ids
			timeStepIndex(int): timeStepIndex

		Returns:
			Dict[int,int]: 
		"""
		pass

	@overload
	def ICheckValveElementsResults(self) -> Dict[int,int]:
		"""Magnitude of flow through the selected check valve.

		Returns:
			Dict[int,int]: 
		"""
		pass

	@overload
	def ICheckValveElementsResults(self, timeStepIndex: int) -> Dict[int,int]:
		"""Magnitude of flow through the selected check valve.

		Args:
			timeStepIndex(int): timeStepIndex

		Returns:
			Dict[int,int]: 
		"""
		pass

	@overload
	def ICheckValveElementsResults(self, ids: List[int], timeStepIndex: int) -> Dict[int,int]:
		"""No Description

		Args:
			ids(List[int]): ids
			timeStepIndex(int): timeStepIndex

		Returns:
			Dict[int,int]: 
		"""
		pass

	@overload
	def ICheckValveElementsResults(self) -> Dict[int,int]:
		"""Calculated pressure at the check valve.

		Returns:
			Dict[int,int]: 
		"""
		pass

	@overload
	def ICheckValveElementsResults(self, timeStepIndex: int) -> Dict[int,int]:
		"""Calculated pressure at the check valve.

		Args:
			timeStepIndex(int): timeStepIndex

		Returns:
			Dict[int,int]: 
		"""
		pass

	@overload
	def ICheckValveElementsResults(self, ids: List[int], timeSTepIndex: int) -> Dict[int,int]:
		"""No Description

		Args:
			ids(List[int]): ids
			timeSTepIndex(int): timeSTepIndex

		Returns:
			Dict[int,int]: 
		"""
		pass

	@overload
	def ICheckValveElementsResults(self) -> Dict[int,int]:
		"""Calculated hydraulic grade at the check valve.

		Returns:
			Dict[int,int]: 
		"""
		pass

	@overload
	def ICheckValveElementsResults(self, timeStepIndex: int) -> Dict[int,int]:
		"""Calculated hydraulic grade at the check valve.

		Args:
			timeStepIndex(int): timeStepIndex

		Returns:
			Dict[int,int]: 
		"""
		pass

	@overload
	def ICheckValveElementsResults(self, ids: List[int], timeStepIndex: int) -> Dict[int,int]:
		"""No Description

		Args:
			ids(List[int]): ids
			timeStepIndex(int): timeStepIndex

		Returns:
			Dict[int,int]: 
		"""
		pass

class ICheckValveUnits(IBaseDirectedNodeUnits):

	def __init__(self) -> None:
		"""Creating a new Instance of this class is not allowed


		Raises:
			Exception: if this class is instanciated
		"""
		raise Exception("Creating a new Instance of this class is not allowed")
		pass

	@property
	def FlowUnit(self) -> IUnit:
		"""No Description

		Returns:
			ICheckValveUnits: 
		"""
		pass

	@property
	def PressureUnit(self) -> IUnit:
		"""No Description

		Returns:
			ICheckValveUnits: 
		"""
		pass

	@property
	def HydraulicGradeUnit(self) -> IUnit:
		"""No Description

		Returns:
			ICheckValveUnits: 
		"""
		pass

class ICheckValves(IWaterNetworkElements[ICheckValves, ICheckValve, ICheckValveUnits, ICheckValveElementInput, ICheckValveElementResults, ICheckValveElementsInput, ICheckValveElementsResults]):

	def __init__(self) -> None:
		"""Creating a new Instance of this class is not allowed


		Raises:
			Exception: if this class is instanciated
		"""
		raise Exception("Creating a new Instance of this class is not allowed")
		pass

class ICheckValve(IWaterNetworkElement[ICheckValves, ICheckValve, ICheckValveUnits, ICheckValveElementInput, ICheckValveElementResults, ICheckValveElementsInput, ICheckValveElementsResults]):

	def __init__(self) -> None:
		"""Creating a new Instance of this class is not allowed


		Raises:
			Exception: if this class is instanciated
		"""
		raise Exception("Creating a new Instance of this class is not allowed")
		pass

class IOrificeBetweenTwoPipesInput(IBaseDirectedNodeInput):

	def __init__(self) -> None:
		"""Creating a new Instance of this class is not allowed


		Raises:
			Exception: if this class is instanciated
		"""
		raise Exception("Creating a new Instance of this class is not allowed")
		pass

	@property
	def TypicalPressureDrop(self) -> float:
		"""No Description

		Returns:
			IOrificeBetweenTwoPipesInput: 
		"""
		pass

	@property
	def TypicalFlow(self) -> float:
		"""No Description

		Returns:
			IOrificeBetweenTwoPipesInput: 
		"""
		pass

	@TypicalPressureDrop.setter
	def TypicalPressureDrop(self, typicalpressuredrop: float) -> None:
		pass

	@TypicalFlow.setter
	def TypicalFlow(self, typicalflow: float) -> None:
		pass

class IOrificesBetweenTwoPipesInput(IBaseDirectedNodesInput):

	def __init__(self) -> None:
		"""Creating a new Instance of this class is not allowed


		Raises:
			Exception: if this class is instanciated
		"""
		raise Exception("Creating a new Instance of this class is not allowed")
		pass

	def TypicalPressureDrops(self) -> Dict[int,int]:
		"""Pressure drop corresponding to the typical flow.

		Returns:
			Dict[int,int]: 
		"""
		pass

	def TypicalFlows(self) -> Dict[int,int]:
		"""This is a typical (positive) flow through the orifice or valve.

		Returns:
			Dict[int,int]: 
		"""
		pass

class IOrificeBetweenTwoPipesResults(IBaseDirectedNodeResults):

	def __init__(self) -> None:
		"""Creating a new Instance of this class is not allowed


		Raises:
			Exception: if this class is instanciated
		"""
		raise Exception("Creating a new Instance of this class is not allowed")
		pass

	@overload
	def IOrificeBetweenTwoPipesResults(self) -> Union[float, None]:
		"""Total flow through the orifice.

		Returns:
			Nullable: 
		"""
		pass

	@overload
	def IOrificeBetweenTwoPipesResults(self, timeStepIndex: int) -> Union[float, None]:
		"""Total flow through the orifice.

		Args:
			timeStepIndex(int): timeStepIndex

		Returns:
			Nullable: 
		"""
		pass

	@overload
	def IOrificeBetweenTwoPipesResults(self) -> Union[float, None]:
		"""Change in head across orifice.

		Returns:
			Nullable: 
		"""
		pass

	@overload
	def IOrificeBetweenTwoPipesResults(self, timeStepIndex: int) -> Union[float, None]:
		"""Change in head across orifice.

		Args:
			timeStepIndex(int): timeStepIndex

		Returns:
			Nullable: 
		"""
		pass

	@overload
	def IOrificeBetweenTwoPipesResults(self) -> Union[float, None]:
		"""Calculated hydraulic grade at the entrance of the orifice.

		Returns:
			Nullable: 
		"""
		pass

	@overload
	def IOrificeBetweenTwoPipesResults(self, timeStepIndex: int) -> Union[float, None]:
		"""Calculated hydraulic grade at the entrance of the orifice.

		Args:
			timeStepIndex(int): timeStepIndex

		Returns:
			Nullable: 
		"""
		pass

	@overload
	def IOrificeBetweenTwoPipesResults(self) -> Union[float, None]:
		"""Calculated hydraulic grade at the exit of the orifice.

		Returns:
			Nullable: 
		"""
		pass

	@overload
	def IOrificeBetweenTwoPipesResults(self, timeStepIndex: int) -> Union[float, None]:
		"""Calculated hydraulic grade at the exit of the orifice.

		Args:
			timeStepIndex(int): timeStepIndex

		Returns:
			Nullable: 
		"""
		pass

	@overload
	def IOrificeBetweenTwoPipesResults(self) -> Union[float, None]:
		"""Calculated pressure at the entrance of the orifice.

		Returns:
			Nullable: 
		"""
		pass

	@overload
	def IOrificeBetweenTwoPipesResults(self, timeStepIndex: int) -> Union[float, None]:
		"""Calculated pressure at the entrance of the orifice.

		Args:
			timeStepIndex(int): timeStepIndex

		Returns:
			Nullable: 
		"""
		pass

	@overload
	def IOrificeBetweenTwoPipesResults(self) -> Union[float, None]:
		"""Calculated pressure at the exit to the orifice.

		Returns:
			Nullable: 
		"""
		pass

	@overload
	def IOrificeBetweenTwoPipesResults(self, timeStepIndex: int) -> Union[float, None]:
		"""Calculated pressure at the exit to the orifice.

		Args:
			timeStepIndex(int): timeStepIndex

		Returns:
			Nullable: 
		"""
		pass

	@overload
	def IOrificeBetweenTwoPipesResults(self) -> Union[float, None]:
		"""Magnitude of flow through the selected orifice.

		Returns:
			Nullable: 
		"""
		pass

	@overload
	def IOrificeBetweenTwoPipesResults(self, timeStepIndex: int) -> Union[float, None]:
		"""Magnitude of flow through the selected orifice.

		Args:
			timeStepIndex(int): timeStepIndex

		Returns:
			Nullable: 
		"""
		pass

	def Flows(self) -> array(Union[float, None]):
		"""Total flow through the orifice.

		Returns:
			array(): 
		"""
		pass

	def Headlosses(self) -> array(Union[float, None]):
		"""Change in head across orifice.

		Returns:
			array(): 
		"""
		pass

	def FromHydraulicGrades(self) -> array(Union[float, None]):
		"""Calculated hydraulic grade at the entrance of the orifice.

		Returns:
			array(): 
		"""
		pass

	def ToHydraulicGrades(self) -> array(Union[float, None]):
		"""Calculated hydraulic grade at the exit of the orifice.

		Returns:
			array(): 
		"""
		pass

	def FromPressures(self) -> array(Union[float, None]):
		"""Calculated pressure at the entrance of the orifice.

		Returns:
			array(): 
		"""
		pass

	def ToPressures(self) -> array(Union[float, None]):
		"""Calculated pressure at the exit to the orifice.

		Returns:
			array(): 
		"""
		pass

	def AbsoluteFlows(self) -> array(Union[float, None]):
		"""Magnitude of flow through the selected orifice.

		Returns:
			array(): 
		"""
		pass

class IOrificesBetweenTwoPipesResults(IBaseDirectedNodesResults):

	def __init__(self) -> None:
		"""Creating a new Instance of this class is not allowed


		Raises:
			Exception: if this class is instanciated
		"""
		raise Exception("Creating a new Instance of this class is not allowed")
		pass

	@overload
	def IOrificesBetweenTwoPipesResults(self) -> Dict[int,int]:
		"""Total flow through the orifice.

		Returns:
			Dict[int,int]: 
		"""
		pass

	@overload
	def IOrificesBetweenTwoPipesResults(self, timeStepIndex: int) -> Dict[int,int]:
		"""Total flow through the orifice.

		Args:
			timeStepIndex(int): timeStepIndex

		Returns:
			Dict[int,int]: 
		"""
		pass

	@overload
	def IOrificesBetweenTwoPipesResults(self, ids: List[int], timeStepIndex: int) -> Dict[int,int]:
		"""No Description

		Args:
			ids(List[int]): ids
			timeStepIndex(int): timeStepIndex

		Returns:
			Dict[int,int]: 
		"""
		pass

	@overload
	def IOrificesBetweenTwoPipesResults(self) -> Dict[int,int]:
		"""Change in head across orifice.

		Returns:
			Dict[int,int]: 
		"""
		pass

	@overload
	def IOrificesBetweenTwoPipesResults(self, timeStepIndex: int) -> Dict[int,int]:
		"""Change in head across orifice.

		Args:
			timeStepIndex(int): timeStepIndex

		Returns:
			Dict[int,int]: 
		"""
		pass

	@overload
	def IOrificesBetweenTwoPipesResults(self, ids: List[int], timeStepIndex: int) -> Dict[int,int]:
		"""No Description

		Args:
			ids(List[int]): ids
			timeStepIndex(int): timeStepIndex

		Returns:
			Dict[int,int]: 
		"""
		pass

	@overload
	def IOrificesBetweenTwoPipesResults(self) -> Dict[int,int]:
		"""Calculated hydraulic grade at the entrance of the orifice.

		Returns:
			Dict[int,int]: 
		"""
		pass

	@overload
	def IOrificesBetweenTwoPipesResults(self, timeStepIndex: int) -> Dict[int,int]:
		"""Calculated hydraulic grade at the entrance of the orifice.

		Args:
			timeStepIndex(int): timeStepIndex

		Returns:
			Dict[int,int]: 
		"""
		pass

	@overload
	def IOrificesBetweenTwoPipesResults(self, ids: List[int], timeStepIndex: int) -> Dict[int,int]:
		"""No Description

		Args:
			ids(List[int]): ids
			timeStepIndex(int): timeStepIndex

		Returns:
			Dict[int,int]: 
		"""
		pass

	@overload
	def IOrificesBetweenTwoPipesResults(self) -> Dict[int,int]:
		"""Calculated hydraulic grade at the exit of the orifice.

		Returns:
			Dict[int,int]: 
		"""
		pass

	@overload
	def IOrificesBetweenTwoPipesResults(self, timeStepIndex: int) -> Dict[int,int]:
		"""Calculated hydraulic grade at the exit of the orifice.

		Args:
			timeStepIndex(int): timeStepIndex

		Returns:
			Dict[int,int]: 
		"""
		pass

	@overload
	def IOrificesBetweenTwoPipesResults(self, ids: List[int], timeStepIndex: int) -> Dict[int,int]:
		"""No Description

		Args:
			ids(List[int]): ids
			timeStepIndex(int): timeStepIndex

		Returns:
			Dict[int,int]: 
		"""
		pass

	@overload
	def IOrificesBetweenTwoPipesResults(self) -> Dict[int,int]:
		"""Calculated pressure at the entrance of the orifice.

		Returns:
			Dict[int,int]: 
		"""
		pass

	@overload
	def IOrificesBetweenTwoPipesResults(self, timeStepIndex: int) -> Dict[int,int]:
		"""Calculated pressure at the entrance of the orifice.

		Args:
			timeStepIndex(int): timeStepIndex

		Returns:
			Dict[int,int]: 
		"""
		pass

	@overload
	def IOrificesBetweenTwoPipesResults(self, ids: List[int], timeStepIndex: int) -> Dict[int,int]:
		"""No Description

		Args:
			ids(List[int]): ids
			timeStepIndex(int): timeStepIndex

		Returns:
			Dict[int,int]: 
		"""
		pass

	@overload
	def IOrificesBetweenTwoPipesResults(self) -> Dict[int,int]:
		"""Calculated pressure at the exit to the orifice.

		Returns:
			Dict[int,int]: 
		"""
		pass

	@overload
	def IOrificesBetweenTwoPipesResults(self, timeStepIndex: int) -> Dict[int,int]:
		"""Calculated pressure at the exit to the orifice.

		Args:
			timeStepIndex(int): timeStepIndex

		Returns:
			Dict[int,int]: 
		"""
		pass

	@overload
	def IOrificesBetweenTwoPipesResults(self, ids: List[int], timeStepIndex: int) -> Dict[int,int]:
		"""No Description

		Args:
			ids(List[int]): ids
			timeStepIndex(int): timeStepIndex

		Returns:
			Dict[int,int]: 
		"""
		pass

	@overload
	def IOrificesBetweenTwoPipesResults(self, timeStepIndex: int) -> Dict[int,int]:
		"""Magnitude of flow through the selected orifice.

		Args:
			timeStepIndex(int): timeStepIndex

		Returns:
			Dict[int,int]: 
		"""
		pass

	@overload
	def IOrificesBetweenTwoPipesResults(self, ids: List[int], timeStepIndex: int) -> Dict[int,int]:
		"""No Description

		Args:
			ids(List[int]): ids
			timeStepIndex(int): timeStepIndex

		Returns:
			Dict[int,int]: 
		"""
		pass

	def AbsolueFlow(self) -> Dict[int,int]:
		"""Magnitude of flow through the selected orifice.

		Returns:
			Dict[int,int]: 
		"""
		pass

class IOrificeBetweenTwoPipesUnits(IBaseDirectedNodeUnits):

	def __init__(self) -> None:
		"""Creating a new Instance of this class is not allowed


		Raises:
			Exception: if this class is instanciated
		"""
		raise Exception("Creating a new Instance of this class is not allowed")
		pass

	@property
	def FlowUnit(self) -> IUnit:
		"""No Description

		Returns:
			IOrificeBetweenTwoPipesUnits: 
		"""
		pass

	@property
	def HeadlossUnit(self) -> IUnit:
		"""No Description

		Returns:
			IOrificeBetweenTwoPipesUnits: 
		"""
		pass

	@property
	def HydraulicGradeUnit(self) -> IUnit:
		"""No Description

		Returns:
			IOrificeBetweenTwoPipesUnits: 
		"""
		pass

	@property
	def PressureUnit(self) -> IUnit:
		"""No Description

		Returns:
			IOrificeBetweenTwoPipesUnits: 
		"""
		pass

class IOrificeBetweenTwoPipes(IWaterNetworkElement[IOrificesBetweenTwoPipes, IOrificeBetweenTwoPipes, IOrificeBetweenTwoPipesUnits, IOrificeBetweenTwoPipesInput, IOrificeBetweenTwoPipesResults, IOrificesBetweenTwoPipesInput, IOrificesBetweenTwoPipesResults]):

	def __init__(self) -> None:
		"""Creating a new Instance of this class is not allowed


		Raises:
			Exception: if this class is instanciated
		"""
		raise Exception("Creating a new Instance of this class is not allowed")
		pass

class IOrificesBetweenTwoPipes(IWaterNetworkElements[IOrificesBetweenTwoPipes, IOrificeBetweenTwoPipes, IOrificeBetweenTwoPipesUnits, IOrificeBetweenTwoPipesInput, IOrificeBetweenTwoPipesResults, IOrificesBetweenTwoPipesInput, IOrificesBetweenTwoPipesResults]):

	def __init__(self) -> None:
		"""Creating a new Instance of this class is not allowed


		Raises:
			Exception: if this class is instanciated
		"""
		raise Exception("Creating a new Instance of this class is not allowed")
		pass

class ITurbineCurveCollection(ICollectionElements[ITurbineFlowHeads, ITurbineFlowHead, ITurbineCurveUnits]):

	def __init__(self) -> None:
		"""Creating a new Instance of this class is not allowed


		Raises:
			Exception: if this class is instanciated
		"""
		raise Exception("Creating a new Instance of this class is not allowed")
		pass

class ITurbineFlowHeads(ICollection[ITurbineFlowHead]):

	def __init__(self) -> None:
		"""Creating a new Instance of this class is not allowed


		Raises:
			Exception: if this class is instanciated
		"""
		raise Exception("Creating a new Instance of this class is not allowed")
		pass

	def Add(self, flow: float, head: float) -> ITurbineFlowHead:
		"""Adds a new row to the collection with the given data.

		Args:
			flow(float): flow
			head(float): head

		Returns:
			ITurbineFlowHead: 
		"""
		pass

class ITurbineFlowHead(ICollectionElement):

	def __init__(self) -> None:
		"""Creating a new Instance of this class is not allowed


		Raises:
			Exception: if this class is instanciated
		"""
		raise Exception("Creating a new Instance of this class is not allowed")
		pass

	@property
	def Flow(self) -> float:
		"""No Description

		Returns:
			ITurbineFlowHead: 
		"""
		pass

	@property
	def Head(self) -> float:
		"""No Description

		Returns:
			ITurbineFlowHead: 
		"""
		pass

	@Flow.setter
	def Flow(self, flow: float) -> None:
		pass

	@Head.setter
	def Head(self, head: float) -> None:
		pass

class ITurbineCurveUnits(IElementUnits):

	def __init__(self) -> None:
		"""Creating a new Instance of this class is not allowed


		Raises:
			Exception: if this class is instanciated
		"""
		raise Exception("Creating a new Instance of this class is not allowed")
		pass

	@property
	def FlowUnit(self) -> IUnit:
		"""No Description

		Returns:
			ITurbineCurveUnits: 
		"""
		pass

	@property
	def HeadUnit(self) -> IUnit:
		"""No Description

		Returns:
			ITurbineCurveUnits: 
		"""
		pass

class IElectricalTorqueCollection(ICollectionElements[IElectricalTorques, IElectricalTorque, IElectricalTorqueUnits]):

	def __init__(self) -> None:
		"""Creating a new Instance of this class is not allowed


		Raises:
			Exception: if this class is instanciated
		"""
		raise Exception("Creating a new Instance of this class is not allowed")
		pass

class IElectricalTorques(ICollection[IElectricalTorque]):

	def __init__(self) -> None:
		"""Creating a new Instance of this class is not allowed


		Raises:
			Exception: if this class is instanciated
		"""
		raise Exception("Creating a new Instance of this class is not allowed")
		pass

	def Add(self, time: float, torque: float) -> IElectricalTorque:
		"""Adds a new row with the given data.

		Args:
			time(float): time
			torque(float): torque

		Returns:
			IElectricalTorque: 
		"""
		pass

class IElectricalTorque(ICollectionElement):

	def __init__(self) -> None:
		"""Creating a new Instance of this class is not allowed


		Raises:
			Exception: if this class is instanciated
		"""
		raise Exception("Creating a new Instance of this class is not allowed")
		pass

	@property
	def Time(self) -> float:
		"""No Description

		Returns:
			IElectricalTorque: 
		"""
		pass

	@property
	def Torque(self) -> float:
		"""No Description

		Returns:
			IElectricalTorque: 
		"""
		pass

	@Time.setter
	def Time(self, time: float) -> None:
		pass

	@Torque.setter
	def Torque(self, torque: float) -> None:
		pass

class IElectricalTorqueUnits(IElementUnits):

	def __init__(self) -> None:
		"""Creating a new Instance of this class is not allowed


		Raises:
			Exception: if this class is instanciated
		"""
		raise Exception("Creating a new Instance of this class is not allowed")
		pass

	@property
	def TimeUnit(self) -> IUnit:
		"""No Description

		Returns:
			IElectricalTorqueUnits: 
		"""
		pass

	@property
	def TorqueUnit(self) -> IUnit:
		"""No Description

		Returns:
			IElectricalTorqueUnits: 
		"""
		pass

class ITurbineInput(IBaseDirectedNodeInput):

	def __init__(self) -> None:
		"""Creating a new Instance of this class is not allowed


		Raises:
			Exception: if this class is instanciated
		"""
		raise Exception("Creating a new Instance of this class is not allowed")
		pass

	@property
	def TimeDelayUntilValveOperates(self) -> float:
		"""No Description

		Returns:
			ITurbineInput: 
		"""
		pass

	@property
	def TimeForValveToOperate(self) -> float:
		"""No Description

		Returns:
			ITurbineInput: 
		"""
		pass

	@property
	def SphericalValveDiameter(self) -> float:
		"""No Description

		Returns:
			ITurbineInput: 
		"""
		pass

	@property
	def TurbineEfficiency(self) -> float:
		"""No Description

		Returns:
			ITurbineInput: 
		"""
		pass

	@property
	def MomentOfInertia(self) -> float:
		"""No Description

		Returns:
			ITurbineInput: 
		"""
		pass

	@property
	def RotationalSpeed(self) -> float:
		"""No Description

		Returns:
			ITurbineInput: 
		"""
		pass

	@property
	def GateOpeningPattern(self) -> IPattern:
		"""No Description

		Returns:
			ITurbineInput: 
		"""
		pass

	@property
	def SpecificSpeed(self) -> float:
		"""No Description

		Returns:
			ITurbineInput: 
		"""
		pass

	@property
	def TurbineInitialFlow(self) -> float:
		"""No Description

		Returns:
			ITurbineInput: 
		"""
		pass

	@property
	def TurbineInitialHead(self) -> float:
		"""No Description

		Returns:
			ITurbineInput: 
		"""
		pass

	@property
	def OperatingCase(self) -> TurbineOperatingCaseEnum:
		"""No Description

		Returns:
			ITurbineInput: 
		"""
		pass

	@property
	def ReportPeriod(self) -> int:
		"""No Description

		Returns:
			ITurbineInput: 
		"""
		pass

	@property
	def TurbineInitialStatus(self) -> TurbineStatusEnum:
		"""No Description

		Returns:
			ITurbineInput: 
		"""
		pass

	@property
	def TurbineCurveCollection(self) -> ITurbineCurveCollection:
		"""No Description

		Returns:
			ITurbineInput: 
		"""
		pass

	@property
	def ElectricalTorqueCollection(self) -> IElectricalTorqueCollection:
		"""No Description

		Returns:
			ITurbineInput: 
		"""
		pass

	@TimeDelayUntilValveOperates.setter
	def TimeDelayUntilValveOperates(self, timedelayuntilvalveoperates: float) -> None:
		pass

	@TimeForValveToOperate.setter
	def TimeForValveToOperate(self, timeforvalvetooperate: float) -> None:
		pass

	@SphericalValveDiameter.setter
	def SphericalValveDiameter(self, sphericalvalvediameter: float) -> None:
		pass

	@TurbineEfficiency.setter
	def TurbineEfficiency(self, turbineefficiency: float) -> None:
		pass

	@MomentOfInertia.setter
	def MomentOfInertia(self, momentofinertia: float) -> None:
		pass

	@RotationalSpeed.setter
	def RotationalSpeed(self, rotationalspeed: float) -> None:
		pass

	@GateOpeningPattern.setter
	def GateOpeningPattern(self, gateopeningpattern: IPattern) -> None:
		pass

	@SpecificSpeed.setter
	def SpecificSpeed(self, specificspeed: float) -> None:
		pass

	@TurbineInitialFlow.setter
	def TurbineInitialFlow(self, turbineinitialflow: float) -> None:
		pass

	@TurbineInitialHead.setter
	def TurbineInitialHead(self, turbineinitialhead: float) -> None:
		pass

	@OperatingCase.setter
	def OperatingCase(self, operatingcase: TurbineOperatingCaseEnum) -> None:
		pass

	@ReportPeriod.setter
	def ReportPeriod(self, reportperiod: int) -> None:
		pass

	@TurbineInitialStatus.setter
	def TurbineInitialStatus(self, turbineinitialstatus: TurbineStatusEnum) -> None:
		pass

class ITurbinesInput(IBaseDirectedNodesInput):

	def __init__(self) -> None:
		"""Creating a new Instance of this class is not allowed


		Raises:
			Exception: if this class is instanciated
		"""
		raise Exception("Creating a new Instance of this class is not allowed")
		pass

	def TimeDelayUntilValveOperates(self) -> Dict[int,int]:
		"""The time delay prior to operating the spherical valve.

		Returns:
			Dict[int,int]: 
		"""
		pass

	def TimeForValveToOperate(self) -> Dict[int,int]:
		"""Time required to operate the spherical valve. By default, it is set equal to one time step.

		Returns:
			Dict[int,int]: 
		"""
		pass

	def SphericalValveDiameter(self) -> Dict[int,int]:
		"""The diameter of the spherical valve.

		Returns:
			Dict[int,int]: 
		"""
		pass

	def TurbineEfficiency(self) -> Dict[int,int]:
		"""The overall efficiency of the turbine and the generator. A typical value is 80.

		Returns:
			Dict[int,int]: 
		"""
		pass

	def MomentOfInertia(self) -> Dict[int,int]:
		"""The (weight) moment of inertia accounts for the turbine, generator, and entrained water.

		Returns:
			Dict[int,int]: 
		"""
		pass

	def RotationalSpeed(self) -> Dict[int,int]:
		"""Also known as synchronous speed for a turbine. The power it generates depends on it.

		Returns:
			Dict[int,int]: 
		"""
		pass

	def GateOpeningPattern(self) -> Dict[int,int]:
		"""Operating Rule describes the percent wicket gate opening vs time.

		Returns:
			Dict[int,int]: 
		"""
		pass

	def SpecificSpeed(self) -> Dict[int,int]:
		"""This represents the type of turbine. HAMMER ships with 4-quadrant curves for: 30, 45, or 60 (US units), 115, 170, or 230 (metric units). You can add your own curves to this library.

		Returns:
			Dict[int,int]: 
		"""
		pass

	def TurbineInitialFlow(self) -> Dict[int,int]:
		"""Nominal or rated flow of the turbine.

		Returns:
			Dict[int,int]: 
		"""
		pass

	def TurbineInitialHead(self) -> Dict[int,int]:
		"""Nominal or rated head of the turbine.

		Returns:
			Dict[int,int]: 
		"""
		pass

	def OperatingCase(self) -> Dict[int,int]:
		"""Selects the type of transient event to be modeled.

		Returns:
			Dict[int,int]: 
		"""
		pass

	def ReportPeriod(self) -> Dict[int,int]:
		"""Number of time steps between successive printouts of operation. By default, this printout is suppressed.

		Returns:
			Dict[int,int]: 
		"""
		pass

	def TurbineInitialStatus(self) -> Dict[int,int]:
		"""Specify if the turbine is initially open or closed.

		Returns:
			Dict[int,int]: 
		"""
		pass

class ITurbineResults(IBaseDirectedNodeResults):

	def __init__(self) -> None:
		"""Creating a new Instance of this class is not allowed


		Raises:
			Exception: if this class is instanciated
		"""
		raise Exception("Creating a new Instance of this class is not allowed")
		pass

	@overload
	def ITurbineResults(self) -> Union[float, None]:
		"""Total flow through the turbine.

		Returns:
			Nullable: 
		"""
		pass

	@overload
	def ITurbineResults(self, timeStepIndex: int) -> Union[float, None]:
		"""Total flow through the turbine.

		Args:
			timeStepIndex(int): timeStepIndex

		Returns:
			Nullable: 
		"""
		pass

	@overload
	def ITurbineResults(self) -> Union[float, None]:
		"""Change in head across turbine.

		Returns:
			Nullable: 
		"""
		pass

	@overload
	def ITurbineResults(self, timeStepIndex: int) -> Union[float, None]:
		"""Change in head across turbine.

		Args:
			timeStepIndex(int): timeStepIndex

		Returns:
			Nullable: 
		"""
		pass

	@overload
	def ITurbineResults(self) -> Union[float, None]:
		"""Calculated hydraulic grade at the entrance of the turbine.

		Returns:
			Nullable: 
		"""
		pass

	@overload
	def ITurbineResults(self, timeStepIndex: int) -> Union[float, None]:
		"""Calculated hydraulic grade at the entrance of the turbine.

		Args:
			timeStepIndex(int): timeStepIndex

		Returns:
			Nullable: 
		"""
		pass

	@overload
	def ITurbineResults(self) -> Union[float, None]:
		"""Calculated hydraulic grade at the exit of the turbine.

		Returns:
			Nullable: 
		"""
		pass

	@overload
	def ITurbineResults(self, timeStepIndex: int) -> Union[float, None]:
		"""Calculated hydraulic grade at the exit of the turbine.

		Args:
			timeStepIndex(int): timeStepIndex

		Returns:
			Nullable: 
		"""
		pass

	@overload
	def ITurbineResults(self) -> Union[float, None]:
		"""Calculated pressure at the entrance of the turbine.

		Returns:
			Nullable: 
		"""
		pass

	@overload
	def ITurbineResults(self, timeStepIndex: int) -> Union[float, None]:
		"""Calculated pressure at the entrance of the turbine.

		Args:
			timeStepIndex(int): timeStepIndex

		Returns:
			Nullable: 
		"""
		pass

	@overload
	def ITurbineResults(self) -> Union[float, None]:
		"""Calculated pressure at the exit to the turbine.

		Returns:
			Nullable: 
		"""
		pass

	@overload
	def ITurbineResults(self, timeStepIndex: int) -> Union[float, None]:
		"""Calculated pressure at the exit to the turbine.

		Args:
			timeStepIndex(int): timeStepIndex

		Returns:
			Nullable: 
		"""
		pass

	@overload
	def ITurbineResults(self) -> Union[float, None]:
		"""Magnitude of flow through the selected turbine.

		Returns:
			Nullable: 
		"""
		pass

	@overload
	def ITurbineResults(self, timeStepIndex: int) -> Union[float, None]:
		"""Magnitude of flow through the selected turbine.

		Args:
			timeStepIndex(int): timeStepIndex

		Returns:
			Nullable: 
		"""
		pass

	def Flows(self) -> array(Union[float, None]):
		"""Total flow through the turbine.

		Returns:
			array(): 
		"""
		pass

	def Headlosses(self) -> array(Union[float, None]):
		"""Change in head across turbine.

		Returns:
			array(): 
		"""
		pass

	def FromHydraulicGrades(self) -> array(Union[float, None]):
		"""Calculated hydraulic grade at the entrance of the turbine.

		Returns:
			array(): 
		"""
		pass

	def ToHydraulicGrades(self) -> array(Union[float, None]):
		"""Calculated hydraulic grade at the exit of the turbine.

		Returns:
			array(): 
		"""
		pass

	def FromPressures(self) -> array(Union[float, None]):
		"""Calculated pressure at the entrance of the turbine.

		Returns:
			array(): 
		"""
		pass

	def ToPressures(self) -> array(Union[float, None]):
		"""Calculated pressure at the exit to the turbine.

		Returns:
			array(): 
		"""
		pass

	def AbsoluteFlows(self) -> array(Union[float, None]):
		"""Magnitude of flow through the selected turbine.

		Returns:
			array(): 
		"""
		pass

	def MaximumTransientSpeed(self) -> Union[float, None]:
		"""Maximum speed at turbine over the course of the transient simulation.

		Returns:
			Nullable: 
		"""
		pass

	def MinimumTransientSpeed(self) -> Union[float, None]:
		"""Minimum speed at turbine over the course of the transient simulation.

		Returns:
			Nullable: 
		"""
		pass

class ITurbinesResults(IBaseDirectedNodesResults):

	def __init__(self) -> None:
		"""Creating a new Instance of this class is not allowed


		Raises:
			Exception: if this class is instanciated
		"""
		raise Exception("Creating a new Instance of this class is not allowed")
		pass

	@overload
	def ITurbinesResults(self) -> Dict[int,int]:
		"""Total flow through the turbine.

		Returns:
			Dict[int,int]: 
		"""
		pass

	@overload
	def ITurbinesResults(self, timeStepIndex: int) -> Dict[int,int]:
		"""Total flow through the turbine.

		Args:
			timeStepIndex(int): timeStepIndex

		Returns:
			Dict[int,int]: 
		"""
		pass

	@overload
	def ITurbinesResults(self, ids: List[int], timeStepIndex: int) -> Dict[int,int]:
		"""No Description

		Args:
			ids(List[int]): ids
			timeStepIndex(int): timeStepIndex

		Returns:
			Dict[int,int]: 
		"""
		pass

	@overload
	def ITurbinesResults(self) -> Dict[int,int]:
		"""Change in head across turbine.

		Returns:
			Dict[int,int]: 
		"""
		pass

	@overload
	def ITurbinesResults(self, timeStepIndex: int) -> Dict[int,int]:
		"""Change in head across turbine.

		Args:
			timeStepIndex(int): timeStepIndex

		Returns:
			Dict[int,int]: 
		"""
		pass

	@overload
	def ITurbinesResults(self, ids: List[int], timeStepIndex: int) -> Dict[int,int]:
		"""No Description

		Args:
			ids(List[int]): ids
			timeStepIndex(int): timeStepIndex

		Returns:
			Dict[int,int]: 
		"""
		pass

	@overload
	def ITurbinesResults(self) -> Dict[int,int]:
		"""Calculated hydraulic grade at the entrance of the turbine.

		Returns:
			Dict[int,int]: 
		"""
		pass

	@overload
	def ITurbinesResults(self, timeStepIndex: int) -> Dict[int,int]:
		"""Calculated hydraulic grade at the entrance of the turbine.

		Args:
			timeStepIndex(int): timeStepIndex

		Returns:
			Dict[int,int]: 
		"""
		pass

	@overload
	def ITurbinesResults(self, ids: List[int], timeStepIndex: int) -> Dict[int,int]:
		"""No Description

		Args:
			ids(List[int]): ids
			timeStepIndex(int): timeStepIndex

		Returns:
			Dict[int,int]: 
		"""
		pass

	@overload
	def ITurbinesResults(self) -> Dict[int,int]:
		"""Calculated hydraulic grade at the exit of the turbine.

		Returns:
			Dict[int,int]: 
		"""
		pass

	@overload
	def ITurbinesResults(self, timeStepIndex: int) -> Dict[int,int]:
		"""Calculated hydraulic grade at the exit of the turbine.

		Args:
			timeStepIndex(int): timeStepIndex

		Returns:
			Dict[int,int]: 
		"""
		pass

	@overload
	def ITurbinesResults(self, ids: List[int], timeStepIndex: int) -> Dict[int,int]:
		"""No Description

		Args:
			ids(List[int]): ids
			timeStepIndex(int): timeStepIndex

		Returns:
			Dict[int,int]: 
		"""
		pass

	@overload
	def ITurbinesResults(self) -> Dict[int,int]:
		"""Calculated pressure at the entrance of the turbine.

		Returns:
			Dict[int,int]: 
		"""
		pass

	@overload
	def ITurbinesResults(self, timeStepIndex: int) -> Dict[int,int]:
		"""Calculated pressure at the entrance of the turbine.

		Args:
			timeStepIndex(int): timeStepIndex

		Returns:
			Dict[int,int]: 
		"""
		pass

	@overload
	def ITurbinesResults(self, ids: List[int], timeStepIndex: int) -> Dict[int,int]:
		"""No Description

		Args:
			ids(List[int]): ids
			timeStepIndex(int): timeStepIndex

		Returns:
			Dict[int,int]: 
		"""
		pass

	@overload
	def ITurbinesResults(self) -> Dict[int,int]:
		"""Calculated pressure at the exit to the turbine.

		Returns:
			Dict[int,int]: 
		"""
		pass

	@overload
	def ITurbinesResults(self, timeStepIndex: int) -> Dict[int,int]:
		"""Calculated pressure at the exit to the turbine.

		Args:
			timeStepIndex(int): timeStepIndex

		Returns:
			Dict[int,int]: 
		"""
		pass

	@overload
	def ITurbinesResults(self, ids: List[int], timeStepIndex: int) -> Dict[int,int]:
		"""No Description

		Args:
			ids(List[int]): ids
			timeStepIndex(int): timeStepIndex

		Returns:
			Dict[int,int]: 
		"""
		pass

	@overload
	def ITurbinesResults(self) -> Dict[int,int]:
		"""Magnitude of flow through the selected turbine.

		Returns:
			Dict[int,int]: 
		"""
		pass

	@overload
	def ITurbinesResults(self, timeStepIndex: int) -> Dict[int,int]:
		"""Magnitude of flow through the selected turbine.

		Args:
			timeStepIndex(int): timeStepIndex

		Returns:
			Dict[int,int]: 
		"""
		pass

	@overload
	def ITurbinesResults(self, ids: List[int], timeStepIndex: int) -> Dict[int,int]:
		"""No Description

		Args:
			ids(List[int]): ids
			timeStepIndex(int): timeStepIndex

		Returns:
			Dict[int,int]: 
		"""
		pass

	def MaximumTransientSpeeds(self) -> Dict[int,int]:
		"""Maximum speed at turbine over the course of the transient simulation.

		Returns:
			Dict[int,int]: 
		"""
		pass

	def MinimumTransientSpeeds(self) -> Dict[int,int]:
		"""Minimum speed at turbine over the course of the transient simulation.

		Returns:
			Dict[int,int]: 
		"""
		pass

class ITurbineUnits(IBaseDirectedNodeUnits):

	def __init__(self) -> None:
		"""Creating a new Instance of this class is not allowed


		Raises:
			Exception: if this class is instanciated
		"""
		raise Exception("Creating a new Instance of this class is not allowed")
		pass

	@property
	def TimeUnit(self) -> IUnit:
		"""No Description

		Returns:
			ITurbineUnits: 
		"""
		pass

	@property
	def DiameterUnit(self) -> IUnit:
		"""No Description

		Returns:
			ITurbineUnits: 
		"""
		pass

	@property
	def EfficiencyUnit(self) -> IUnit:
		"""No Description

		Returns:
			ITurbineUnits: 
		"""
		pass

	@property
	def InertiaUnit(self) -> IUnit:
		"""No Description

		Returns:
			ITurbineUnits: 
		"""
		pass

	@property
	def RotationUnit(self) -> IUnit:
		"""No Description

		Returns:
			ITurbineUnits: 
		"""
		pass

	@property
	def FlowUnit(self) -> IUnit:
		"""No Description

		Returns:
			ITurbineUnits: 
		"""
		pass

	@property
	def PressureUnit(self) -> IUnit:
		"""No Description

		Returns:
			ITurbineUnits: 
		"""
		pass

	@property
	def HeadlossUnit(self) -> IUnit:
		"""No Description

		Returns:
			ITurbineUnits: 
		"""
		pass

class ITurbine(IWaterNetworkElement[ITurbines, ITurbine, ITurbineUnits, ITurbineInput, ITurbineResults, ITurbinesInput, ITurbinesResults]):

	def __init__(self) -> None:
		"""Creating a new Instance of this class is not allowed


		Raises:
			Exception: if this class is instanciated
		"""
		raise Exception("Creating a new Instance of this class is not allowed")
		pass

class ITurbines(IWaterNetworkElements[ITurbines, ITurbine, ITurbineUnits, ITurbineInput, ITurbineResults, ITurbinesInput, ITurbinesResults]):

	def __init__(self) -> None:
		"""Creating a new Instance of this class is not allowed


		Raises:
			Exception: if this class is instanciated
		"""
		raise Exception("Creating a new Instance of this class is not allowed")
		pass

class IBasePumpsResults(IBaseDirectedNodesResults):

	def __init__(self) -> None:
		"""Creating a new Instance of this class is not allowed


		Raises:
			Exception: if this class is instanciated
		"""
		raise Exception("Creating a new Instance of this class is not allowed")
		pass

	@overload
	def IBasePumpsResults(self) -> Dict[int,int]:
		"""Current relative speed factor of pump at current time step for all pumps.

		Returns:
			Dict[int,int]: 
		"""
		pass

	@overload
	def IBasePumpsResults(self, timeStepIndex: int) -> Dict[int,int]:
		"""Current relative speed factor of pump at given time step for all pumps.

		Args:
			timeStepIndex(int): timeStepIndex

		Returns:
			Dict[int,int]: 
		"""
		pass

	@overload
	def IBasePumpsResults(self, ids: List[int], timeStepIndex: int) -> Dict[int,int]:
		"""No Description

		Args:
			ids(List[int]): ids
			timeStepIndex(int): timeStepIndex

		Returns:
			Dict[int,int]: 
		"""
		pass

	@overload
	def IBasePumpsResults(self) -> Dict[int,int]:
		"""Current hydraulic grade at suction side of the pump at current time step for all pumps.

		Returns:
			Dict[int,int]: 
		"""
		pass

	@overload
	def IBasePumpsResults(self, timeStepIndex: int) -> Dict[int,int]:
		"""Current hydraulic grade at suction side of the pump at given time step for all pumps.

		Args:
			timeStepIndex(int): timeStepIndex

		Returns:
			Dict[int,int]: 
		"""
		pass

	@overload
	def IBasePumpsResults(self, ids: List[int], timeStepIndex: int) -> Dict[int,int]:
		"""No Description

		Args:
			ids(List[int]): ids
			timeStepIndex(int): timeStepIndex

		Returns:
			Dict[int,int]: 
		"""
		pass

	@overload
	def IBasePumpsResults(self) -> Dict[int,int]:
		"""Current hydraulic grade at discharge side of the pump at current time step for all pumps.

		Returns:
			Dict[int,int]: 
		"""
		pass

	@overload
	def IBasePumpsResults(self, timeStepIndex: int) -> Dict[int,int]:
		"""Current hydraulic grade at discharge side of the pump at given time step for all pumps.

		Args:
			timeStepIndex(int): timeStepIndex

		Returns:
			Dict[int,int]: 
		"""
		pass

	@overload
	def IBasePumpsResults(self, ids: List[int], timeStepIndex: int) -> Dict[int,int]:
		"""No Description

		Args:
			ids(List[int]): ids
			timeStepIndex(int): timeStepIndex

		Returns:
			Dict[int,int]: 
		"""
		pass

	@overload
	def IBasePumpsResults(self) -> Dict[int,int]:
		"""Current pressure at suction side of the pump at current time step for all pumps.

		Returns:
			Dict[int,int]: 
		"""
		pass

	@overload
	def IBasePumpsResults(self, timeStepIndex: int) -> Dict[int,int]:
		"""Current pressure at suction side of the pump at given time step for all pumps.

		Args:
			timeStepIndex(int): timeStepIndex

		Returns:
			Dict[int,int]: 
		"""
		pass

	@overload
	def IBasePumpsResults(self, ids: List[int], timeStepIndex: int) -> Dict[int,int]:
		"""No Description

		Args:
			ids(List[int]): ids
			timeStepIndex(int): timeStepIndex

		Returns:
			Dict[int,int]: 
		"""
		pass

	@overload
	def IBasePumpsResults(self) -> Dict[int,int]:
		"""Current pressure at discharge side of the pump at current time step for all pumps.

		Returns:
			Dict[int,int]: 
		"""
		pass

	@overload
	def IBasePumpsResults(self, timeStepIndex: int) -> Dict[int,int]:
		"""Current pressure at discharge side of the pump at given time step for all pumps.

		Args:
			timeStepIndex(int): timeStepIndex

		Returns:
			Dict[int,int]: 
		"""
		pass

	@overload
	def IBasePumpsResults(self, ids: List[int], timeStepIndex: int) -> Dict[int,int]:
		"""No Description

		Args:
			ids(List[int]): ids
			timeStepIndex(int): timeStepIndex

		Returns:
			Dict[int,int]: 
		"""
		pass

	@overload
	def IBasePumpsResults(self) -> Dict[int,int]:
		"""Current flow pumped by standard pump or the pump battery at current time step for all pumps.

		Returns:
			Dict[int,int]: 
		"""
		pass

	@overload
	def IBasePumpsResults(self, timeStepIndex: int) -> Dict[int,int]:
		"""Current flow pumped by standard pump or the pump battery at given time step for all pumps.

		Args:
			timeStepIndex(int): timeStepIndex

		Returns:
			Dict[int,int]: 
		"""
		pass

	@overload
	def IBasePumpsResults(self, ids: List[int], timeStepIndex: int) -> Dict[int,int]:
		"""No Description

		Args:
			ids(List[int]): ids
			timeStepIndex(int): timeStepIndex

		Returns:
			Dict[int,int]: 
		"""
		pass

	@overload
	def IBasePumpsResults(self) -> Dict[int,int]:
		"""Current head gain between suction and discharge side of the pump at current time step for all pumps.

		Returns:
			Dict[int,int]: 
		"""
		pass

	@overload
	def IBasePumpsResults(self, timeStepIndex: int) -> Dict[int,int]:
		"""Current head gain between suction and discharge side of the pump at given time step for all pumps.

		Args:
			timeStepIndex(int): timeStepIndex

		Returns:
			Dict[int,int]: 
		"""
		pass

	@overload
	def IBasePumpsResults(self, ids: List[int], timeStepIndex: int) -> Dict[int,int]:
		"""No Description

		Args:
			ids(List[int]): ids
			timeStepIndex(int): timeStepIndex

		Returns:
			Dict[int,int]: 
		"""
		pass

	@overload
	def IBasePumpsResults(self) -> Dict[int,int]:
		"""Current margin of actual (available) pressure head over vapor pressure at the suction side of the pump (at the impeller) at current time step for all pumps.

		Returns:
			Dict[int,int]: 
		"""
		pass

	@overload
	def IBasePumpsResults(self, timeStepIndex: int) -> Dict[int,int]:
		"""Current margin of actual (available) pressure head over vapor pressure at the suction side of the pump (at the impeller) at given time step for all pumps.

		Args:
			timeStepIndex(int): timeStepIndex

		Returns:
			Dict[int,int]: 
		"""
		pass

	@overload
	def IBasePumpsResults(self, ids: List[int], timeStepIndex: int) -> Dict[int,int]:
		"""No Description

		Args:
			ids(List[int]): ids
			timeStepIndex(int): timeStepIndex

		Returns:
			Dict[int,int]: 
		"""
		pass

	@overload
	def IBasePumpsResults(self) -> Dict[int,int]:
		"""Current required (manufacturer specified) pressure head over vapor pressure at the suction side of the pump (at the impeller) that is required in order to avoid pump cavitation at current time step for all pumps.

		Returns:
			Dict[int,int]: 
		"""
		pass

	@overload
	def IBasePumpsResults(self, timeStepIndex: int) -> Dict[int,int]:
		"""Current required (manufacturer specified) pressure head over vapor pressure at the suction side of the pump (at the impeller) that is required in order to avoid pump cavitation at given time step for all pumps.

		Args:
			timeStepIndex(int): timeStepIndex

		Returns:
			Dict[int,int]: 
		"""
		pass

	@overload
	def IBasePumpsResults(self, ids: List[int], timeStepIndex: int) -> Dict[int,int]:
		"""No Description

		Args:
			ids(List[int]): ids
			timeStepIndex(int): timeStepIndex

		Returns:
			Dict[int,int]: 
		"""
		pass

	@overload
	def IBasePumpsResults(self) -> Dict[int,int]:
		"""Is true if the system demands on the pump exceeds its capabilities at current time step for all pumps.

		Returns:
			Dict[int,int]: 
		"""
		pass

	@overload
	def IBasePumpsResults(self, timeStepIndex: int) -> Dict[int,int]:
		"""Is true if the system demands on the pump exceeds its capabilities at given time step for all pumps.

		Args:
			timeStepIndex(int): timeStepIndex

		Returns:
			Dict[int,int]: 
		"""
		pass

	@overload
	def IBasePumpsResults(self, ids: List[int], timeStepIndex: int) -> Dict[int,int]:
		"""No Description

		Args:
			ids(List[int]): ids
			timeStepIndex(int): timeStepIndex

		Returns:
			Dict[int,int]: 
		"""
		pass

	@overload
	def IBasePumpsResults(self) -> Dict[int,int]:
		"""Displays whether the selected pump is 'On' or 'Off' during current time step at current time step for all pumps.

		Returns:
			Dict[int,int]: 
		"""
		pass

	@overload
	def IBasePumpsResults(self, timeStepIndex: int) -> Dict[int,int]:
		"""Displays whether the selected pump is 'On' or 'Off' during current time step at given time step for all pumps.

		Args:
			timeStepIndex(int): timeStepIndex

		Returns:
			Dict[int,int]: 
		"""
		pass

	@overload
	def IBasePumpsResults(self, ids: List[int], timeStepIndex: int) -> Dict[int,int]:
		"""No Description

		Args:
			ids(List[int]): ids
			timeStepIndex(int): timeStepIndex

		Returns:
			Dict[int,int]: 
		"""
		pass

	@overload
	def IBasePumpsResults(self) -> Dict[int,int]:
		"""The amount of energy delivered to the pump motor for all pumps at the current time step.

		Returns:
			Dict[int,int]: 
		"""
		pass

	@overload
	def IBasePumpsResults(self, timeStepIndex: int) -> Dict[int,int]:
		"""The amount of energy delivered to the pump motor for all pumps at the given time step.

		Args:
			timeStepIndex(int): timeStepIndex

		Returns:
			Dict[int,int]: 
		"""
		pass

	@overload
	def IBasePumpsResults(self, ids: List[int], timeStepIndex: int) -> Dict[int,int]:
		"""No Description

		Args:
			ids(List[int]): ids
			timeStepIndex(int): timeStepIndex

		Returns:
			Dict[int,int]: 
		"""
		pass

class IBasePumpResults(IBaseDirectedNodeResults):

	def __init__(self) -> None:
		"""Creating a new Instance of this class is not allowed


		Raises:
			Exception: if this class is instanciated
		"""
		raise Exception("Creating a new Instance of this class is not allowed")
		pass

	@overload
	def IBasePumpResults(self) -> Union[float, None]:
		"""Current relative speed factor of pump at current time step.

		Returns:
			Nullable: 
		"""
		pass

	@overload
	def IBasePumpResults(self, timeStepIndex: int) -> Union[float, None]:
		"""Current relative speed factor of pump at given time step.

		Args:
			timeStepIndex(int): timeStepIndex

		Returns:
			Nullable: 
		"""
		pass

	@overload
	def IBasePumpResults(self) -> Union[float, None]:
		"""Calculated hydraulic grade at suction side of the pump at current time step.

		Returns:
			Nullable: 
		"""
		pass

	@overload
	def IBasePumpResults(self, timeStepIndex: int) -> Union[float, None]:
		"""Calculated hydraulic grade at suction side of the pump at given time step.

		Args:
			timeStepIndex(int): timeStepIndex

		Returns:
			Nullable: 
		"""
		pass

	@overload
	def IBasePumpResults(self) -> Union[float, None]:
		"""Calculated hydraulic grade at discharge side of the pump at current time step.

		Returns:
			Nullable: 
		"""
		pass

	@overload
	def IBasePumpResults(self, timeStepIndex: int) -> Union[float, None]:
		"""Calculated hydraulic grade at discharge side of the pump at given time step.

		Args:
			timeStepIndex(int): timeStepIndex

		Returns:
			Nullable: 
		"""
		pass

	@overload
	def IBasePumpResults(self) -> Union[float, None]:
		"""Calculated pressure at suction side of the pump at current time step.

		Returns:
			Nullable: 
		"""
		pass

	@overload
	def IBasePumpResults(self, timeStepIndex: int) -> Union[float, None]:
		"""Calculated pressure at suction side of the pump at given time step.

		Args:
			timeStepIndex(int): timeStepIndex

		Returns:
			Nullable: 
		"""
		pass

	@overload
	def IBasePumpResults(self) -> Union[float, None]:
		"""Calculated pressure at discharge side of the pump at current time step.

		Returns:
			Nullable: 
		"""
		pass

	@overload
	def IBasePumpResults(self, timeStepIndex: int) -> Union[float, None]:
		"""Calculated pressure at discharge side of the pump at given time step.

		Args:
			timeStepIndex(int): timeStepIndex

		Returns:
			Nullable: 
		"""
		pass

	@overload
	def IBasePumpResults(self) -> Union[float, None]:
		"""Total flow pumped by standard pump or the pump battery at current time step.

		Returns:
			Nullable: 
		"""
		pass

	@overload
	def IBasePumpResults(self, timeStepIndex: int) -> Union[float, None]:
		"""Total flow pumped by standard pump or the pump battery at given time step.

		Args:
			timeStepIndex(int): timeStepIndex

		Returns:
			Nullable: 
		"""
		pass

	@overload
	def IBasePumpResults(self) -> Union[float, None]:
		"""Head gain between suction and discharge side of the pump at current time step.

		Returns:
			Nullable: 
		"""
		pass

	@overload
	def IBasePumpResults(self, timeStepIndex: int) -> Union[float, None]:
		"""Head gain between suction and discharge side of the pump at given time step.

		Args:
			timeStepIndex(int): timeStepIndex

		Returns:
			Nullable: 
		"""
		pass

	@overload
	def IBasePumpResults(self) -> Union[float, None]:
		"""The margin of actual (available) pressure head over vapor pressure at the suction side of the pump (at the impeller) at current time step.

		Returns:
			Nullable: 
		"""
		pass

	@overload
	def IBasePumpResults(self, timeStepIndex: int) -> Union[float, None]:
		"""The margin of actual (available) pressure head over vapor pressure at the suction side of the pump (at the impeller) at the given time step.

		Args:
			timeStepIndex(int): timeStepIndex

		Returns:
			Nullable: 
		"""
		pass

	@overload
	def IBasePumpResults(self) -> Union[float, None]:
		"""The required (manufacturer specified) pressure head over vapor pressure at the suction side of the pump (at the impeller) that is required in order to avoid pump cavitation at current time step.

		Returns:
			Nullable: 
		"""
		pass

	@overload
	def IBasePumpResults(self, timeStepIndex: int) -> Union[float, None]:
		"""The required (manufacturer specified) pressure head over vapor pressure at the suction side of the pump (at the impeller) that is required in order to avoid pump cavitation at given time step.

		Args:
			timeStepIndex(int): timeStepIndex

		Returns:
			Nullable: 
		"""
		pass

	@overload
	def IBasePumpResults(self) -> Union[bool, None]:
		"""Is true if the system demands on the pump exceeds its capabilities at current time step.

		Returns:
			Nullable: 
		"""
		pass

	@overload
	def IBasePumpResults(self, timeStepIndex: int) -> Union[bool, None]:
		"""Is true if the system demands on the pump exceeds its capabilities at given time step.

		Args:
			timeStepIndex(int): timeStepIndex

		Returns:
			Nullable: 
		"""
		pass

	@overload
	def IBasePumpResults(self) -> Union[PumpStatusEnum, None]:
		"""Displays whether the selected pump is 'On' or 'Off' during current time step at current time step.

		Returns:
			Nullable: 
		"""
		pass

	@overload
	def IBasePumpResults(self, timeStepIndex: int) -> Union[PumpStatusEnum, None]:
		"""Displays whether the selected pump is 'On' or 'Off' during current time step at given time step.

		Args:
			timeStepIndex(int): timeStepIndex

		Returns:
			Nullable: 
		"""
		pass

	@overload
	def IBasePumpResults(self) -> Union[float, None]:
		"""The amount of energy delivered to the pump motor at the current time step.

		Returns:
			Nullable: 
		"""
		pass

	@overload
	def IBasePumpResults(self, timeStepIndex: int) -> Union[float, None]:
		"""The amount of energy delivered to the pump motor at the given time step.

		Args:
			timeStepIndex(int): timeStepIndex

		Returns:
			Nullable: 
		"""
		pass

	def CalculatedRelativeSpeedFactors(self) -> array(Union[float, None]):
		"""Current relative speed factor of pump across all time steps.

		Returns:
			array(): 
		"""
		pass

	def SuctionHyraulicGrades(self) -> array(Union[float, None]):
		"""Calculated hydraulic grade at suction side of the pump across all time steps.

		Returns:
			array(): 
		"""
		pass

	def DischargeHydraulicGrades(self) -> array(Union[float, None]):
		"""Calculated hydraulic grade at discharge side of the pump across all time steps.

		Returns:
			array(): 
		"""
		pass

	def SuctionPressures(self) -> array(Union[float, None]):
		"""Calculated pressure at suction side of the pump across all time steps.

		Returns:
			array(): 
		"""
		pass

	def DischargePressures(self) -> array(Union[float, None]):
		"""Calculated pressure at discharge side of the pump across all time steps.

		Returns:
			array(): 
		"""
		pass

	def Flows(self) -> array(Union[float, None]):
		"""Total flow pumped by standard pump or the pump battery across all time steps.

		Returns:
			array(): 
		"""
		pass

	def PumpHeads(self) -> array(Union[float, None]):
		"""Head gain between suction and discharge side of the pump across all time steps.

		Returns:
			array(): 
		"""
		pass

	def AvailableNPSHs(self) -> array(Union[float, None]):
		"""The margin of actual (available) pressure head over vapor pressure at the suction side of the pump (at the impeller) across all time steps.

		Returns:
			array(): 
		"""
		pass

	def RequiredNPSHs(self) -> array(Union[float, None]):
		"""The required (manufacturer specified) pressure head over vapor pressure at the suction side of the pump (at the impeller) that is required in order to avoid pump cavitation across all time steps.

		Returns:
			array(): 
		"""
		pass

	def PumpExceedsOperatingRanges(self) -> array(Union[bool, None]):
		"""Is true if the system demands on the pump exceeds its capabilities across all time steps.

		Returns:
			array(): 
		"""
		pass

	def CalculatedPumpStatuses(self) -> array(Union[PumpStatusEnum, None]):
		"""Displays whether the selected pump is 'On' or 'Off' during current time step across all time steps.

		Returns:
			array(): 
		"""
		pass

	def WirePowers(self) -> array(Union[float, None]):
		"""The amount of energy delivered to the pump motor for all time steps.

		Returns:
			array(): 
		"""
		pass

class IBasePumpInput(IBaseDirectedNodeInput):

	def __init__(self) -> None:
		"""Creating a new Instance of this class is not allowed


		Raises:
			Exception: if this class is instanciated
		"""
		raise Exception("Creating a new Instance of this class is not allowed")
		pass

	@property
	def InitialRelativeSpeedFactor(self) -> float:
		"""No Description

		Returns:
			IBasePumpInput: 
		"""
		pass

	@property
	def InitialStatus(self) -> int:
		"""No Description

		Returns:
			IBasePumpInput: 
		"""
		pass

	@InitialRelativeSpeedFactor.setter
	def InitialRelativeSpeedFactor(self, initialrelativespeedfactor: float) -> None:
		pass

	@InitialStatus.setter
	def InitialStatus(self, initialstatus: int) -> None:
		pass

class IBasePumpsInput(IBaseDirectedNodesInput):

	def __init__(self) -> None:
		"""Creating a new Instance of this class is not allowed


		Raises:
			Exception: if this class is instanciated
		"""
		raise Exception("Creating a new Instance of this class is not allowed")
		pass

	@overload
	def IBasePumpsInput(self) -> Dict[int,int]:
		"""Determines the initial speed of the pump impeller relative to the speed at which the pump curve is defined.

		Returns:
			Dict[int,int]: 
		"""
		pass

	@overload
	def IBasePumpsInput(self, ids: List[int]) -> Dict[int,int]:
		"""No Description

		Args:
			ids(List[int]): ids

		Returns:
			Dict[int,int]: 
		"""
		pass

	@overload
	def IBasePumpsInput(self) -> Dict[int,int]:
		"""Sets the initial status of the pump to on or off.

		Returns:
			Dict[int,int]: 
		"""
		pass

	@overload
	def IBasePumpsInput(self, ids: List[int]) -> Dict[int,int]:
		"""No Description

		Args:
			ids(List[int]): ids

		Returns:
			Dict[int,int]: 
		"""
		pass

class IBasePumpUnits(IBaseDirectedNodeUnits):

	def __init__(self) -> None:
		"""Creating a new Instance of this class is not allowed


		Raises:
			Exception: if this class is instanciated
		"""
		raise Exception("Creating a new Instance of this class is not allowed")
		pass

	@property
	def RelativeSpeedFactorUnit(self) -> IUnit:
		"""No Description

		Returns:
			IBasePumpUnits: 
		"""
		pass

	@property
	def HydraulicGradeUnit(self) -> IUnit:
		"""No Description

		Returns:
			IBasePumpUnits: 
		"""
		pass

	@property
	def PressureUnit(self) -> IUnit:
		"""No Description

		Returns:
			IBasePumpUnits: 
		"""
		pass

	@property
	def FlowUnit(self) -> IUnit:
		"""No Description

		Returns:
			IBasePumpUnits: 
		"""
		pass

	@property
	def HeadUnit(self) -> IUnit:
		"""No Description

		Returns:
			IBasePumpUnits: 
		"""
		pass

	@property
	def NPSHUnit(self) -> IUnit:
		"""No Description

		Returns:
			IBasePumpUnits: 
		"""
		pass

	@property
	def PowerUnit(self) -> IUnit:
		"""No Description

		Returns:
			IBasePumpUnits: 
		"""
		pass

class IPumps(IWaterNetworkElements[IPumps, IPump, IPumpUnits, IPumpInput, IPumpResults, IPumpsInput, IPumpsResults]):

	def __init__(self) -> None:
		"""Creating a new Instance of this class is not allowed


		Raises:
			Exception: if this class is instanciated
		"""
		raise Exception("Creating a new Instance of this class is not allowed")
		pass

class IPump(IWaterNetworkElement[IPumps, IPump, IPumpUnits, IPumpInput, IPumpResults, IPumpsInput, IPumpsResults]):

	def __init__(self) -> None:
		"""Creating a new Instance of this class is not allowed


		Raises:
			Exception: if this class is instanciated
		"""
		raise Exception("Creating a new Instance of this class is not allowed")
		pass

class IPumpsInput(IBasePumpsInput):

	def __init__(self) -> None:
		"""Creating a new Instance of this class is not allowed


		Raises:
			Exception: if this class is instanciated
		"""
		raise Exception("Creating a new Instance of this class is not allowed")
		pass

class IPumpsResults(IBasePumpsResults):

	def __init__(self) -> None:
		"""Creating a new Instance of this class is not allowed


		Raises:
			Exception: if this class is instanciated
		"""
		raise Exception("Creating a new Instance of this class is not allowed")
		pass

class IPumpResults(IBasePumpResults):

	def __init__(self) -> None:
		"""Creating a new Instance of this class is not allowed


		Raises:
			Exception: if this class is instanciated
		"""
		raise Exception("Creating a new Instance of this class is not allowed")
		pass

class IPumpInput(IBasePumpInput):

	def __init__(self) -> None:
		"""Creating a new Instance of this class is not allowed


		Raises:
			Exception: if this class is instanciated
		"""
		raise Exception("Creating a new Instance of this class is not allowed")
		pass

	@property
	def PumpDefinition(self) -> IPumpDefinition:
		"""No Description

		Returns:
			IPumpInput: 
		"""
		pass

	@PumpDefinition.setter
	def PumpDefinition(self, pumpdefinition: IPumpDefinition) -> None:
		pass

class IPumpUnits(IBasePumpUnits):

	def __init__(self) -> None:
		"""Creating a new Instance of this class is not allowed


		Raises:
			Exception: if this class is instanciated
		"""
		raise Exception("Creating a new Instance of this class is not allowed")
		pass

class IVariableSpeedPumpBatterys(IWaterNetworkElements[IVariableSpeedPumpBatterys, IVariableSpeedPumpBattery, IVariableSpeedPumpBatteryUnits, IVSPBInput, IVSPBResults, IVSPBsInput, IVSPBsResults]):

	def __init__(self) -> None:
		"""Creating a new Instance of this class is not allowed


		Raises:
			Exception: if this class is instanciated
		"""
		raise Exception("Creating a new Instance of this class is not allowed")
		pass

class IVariableSpeedPumpBattery(IWaterNetworkElement[IVariableSpeedPumpBatterys, IVariableSpeedPumpBattery, IVariableSpeedPumpBatteryUnits, IVSPBInput, IVSPBResults, IVSPBsInput, IVSPBsResults]):

	def __init__(self) -> None:
		"""Creating a new Instance of this class is not allowed


		Raises:
			Exception: if this class is instanciated
		"""
		raise Exception("Creating a new Instance of this class is not allowed")
		pass

class IVSPBsInput(IBasePumpsInput):

	def __init__(self) -> None:
		"""Creating a new Instance of this class is not allowed


		Raises:
			Exception: if this class is instanciated
		"""
		raise Exception("Creating a new Instance of this class is not allowed")
		pass

	def PumpDefinitions(self) -> Dict[int,int]:
		"""Select pump definition for the lead and lag pumps in the battery.

		Returns:
			Dict[int,int]: 
		"""
		pass

	def ControlNodes(self) -> Dict[int,int]:
		"""The node that the battery checks to determine whether to increase, maintain, or decrease its relative speed factor.

		Returns:
			Dict[int,int]: 
		"""
		pass

	def TargetHydraulicGrades(self) -> Dict[int,int]:
		"""The Head that the battery will attempt to maintain for the Control Node.

		Returns:
			Dict[int,int]: 
		"""
		pass

	def MaximumRelativeSpeedFactors(self) -> Dict[int,int]:
		"""The highest relative speed factor that the pump can be set at to meet the target head at the control node. If the target head cannot be met when the pump is set at the maximum relative speed factor, the maximum will be used.

		Returns:
			Dict[int,int]: 
		"""
		pass

	def NumberOfLagPumps(self) -> Dict[int,int]:
		"""Number of lag pumps (identical to the lead pump) whose relative speed factor is adjusted to maintain the target head for a fixed head VSPB. (Lag pumps are not used for constant flow VSPBs).

		Returns:
			Dict[int,int]: 
		"""
		pass

	def ControlNodeOnSuctionSide(self) -> Dict[int,int]:
		"""Specifies if the VSPB has a suction side control node.

		Returns:
			Dict[int,int]: 
		"""
		pass

	def TargetFlows(self) -> Dict[int,int]:
		"""The relative speed of the lead pump will be adjusted to meet the Flow (Target). (Lag pumps are not used for constant flow VSPBs).

		Returns:
			Dict[int,int]: 
		"""
		pass

	def TargetPressures(self) -> Dict[int,int]:
		"""The Pressure that the battery will attempt to maintain for the Control Node.

		Returns:
			Dict[int,int]: 
		"""
		pass

	def VSPBTypes(self) -> Dict[int,int]:
		"""Specify how the variable speed pump battery is controlled.

		Returns:
			Dict[int,int]: 
		"""
		pass

	def VSPBFixedHeadTypes(self) -> Dict[int,int]:
		"""Establish if the battery should be regulated by pressure or hydraulic grade.

		Returns:
			Dict[int,int]: 
		"""
		pass

class IVSPBInput(IBasePumpInput):

	def __init__(self) -> None:
		"""Creating a new Instance of this class is not allowed


		Raises:
			Exception: if this class is instanciated
		"""
		raise Exception("Creating a new Instance of this class is not allowed")
		pass

	@property
	def PumpDefinition(self) -> IPumpDefinition:
		"""No Description

		Returns:
			IVSPBInput: 
		"""
		pass

	@property
	def ControlNode(self) -> IWaterElement:
		"""No Description

		Returns:
			IVSPBInput: 
		"""
		pass

	@property
	def TargetHydraulicGrade(self) -> float:
		"""No Description

		Returns:
			IVSPBInput: 
		"""
		pass

	@property
	def MaximumRelativeSpeedFactor(self) -> float:
		"""No Description

		Returns:
			IVSPBInput: 
		"""
		pass

	@property
	def NumberOfLagPumps(self) -> int:
		"""No Description

		Returns:
			IVSPBInput: 
		"""
		pass

	@property
	def ControlNodeOnSuctionSide(self) -> bool:
		"""No Description

		Returns:
			IVSPBInput: 
		"""
		pass

	@property
	def TargetFlow(self) -> float:
		"""No Description

		Returns:
			IVSPBInput: 
		"""
		pass

	@property
	def TargetPressure(self) -> float:
		"""No Description

		Returns:
			IVSPBInput: 
		"""
		pass

	@property
	def VSPBType(self) -> VSPBType:
		"""No Description

		Returns:
			IVSPBInput: 
		"""
		pass

	@property
	def VSPBFixedHeadType(self) -> VSPBFixedHeadType:
		"""No Description

		Returns:
			IVSPBInput: 
		"""
		pass

	@PumpDefinition.setter
	def PumpDefinition(self, pumpdefinition: IPumpDefinition) -> None:
		pass

	@ControlNode.setter
	def ControlNode(self, controlnode: IWaterElement) -> None:
		pass

	@TargetHydraulicGrade.setter
	def TargetHydraulicGrade(self, targethydraulicgrade: float) -> None:
		pass

	@MaximumRelativeSpeedFactor.setter
	def MaximumRelativeSpeedFactor(self, maximumrelativespeedfactor: float) -> None:
		pass

	@NumberOfLagPumps.setter
	def NumberOfLagPumps(self, numberoflagpumps: int) -> None:
		pass

	@ControlNodeOnSuctionSide.setter
	def ControlNodeOnSuctionSide(self, controlnodeonsuctionside: bool) -> None:
		pass

	@TargetFlow.setter
	def TargetFlow(self, targetflow: float) -> None:
		pass

	@TargetPressure.setter
	def TargetPressure(self, targetpressure: float) -> None:
		pass

	@VSPBType.setter
	def VSPBType(self, vspbtype: VSPBType) -> None:
		pass

	@VSPBFixedHeadType.setter
	def VSPBFixedHeadType(self, vspbfixedheadtype: VSPBFixedHeadType) -> None:
		pass

class IVSPBsResults(IBasePumpsResults):

	def __init__(self) -> None:
		"""Creating a new Instance of this class is not allowed


		Raises:
			Exception: if this class is instanciated
		"""
		raise Exception("Creating a new Instance of this class is not allowed")
		pass

	@overload
	def IVSPBsResults(self) -> Dict[int,int]:
		"""Flow contributed by the lead pump in the pump battery.

		Returns:
			Dict[int,int]: 
		"""
		pass

	@overload
	def IVSPBsResults(self, timeStepIndex: int) -> Dict[int,int]:
		"""Flow contributed by the lead pump in the pump battery.

		Args:
			timeStepIndex(int): timeStepIndex

		Returns:
			Dict[int,int]: 
		"""
		pass

	@overload
	def IVSPBsResults(self, ids: List[int], timeStepIndex: int) -> Dict[int,int]:
		"""No Description

		Args:
			ids(List[int]): ids
			timeStepIndex(int): timeStepIndex

		Returns:
			Dict[int,int]: 
		"""
		pass

	@overload
	def IVSPBsResults(self) -> Dict[int,int]:
		"""Number of pump battery lag pumps running duing the current time step.

		Returns:
			Dict[int,int]: 
		"""
		pass

	@overload
	def IVSPBsResults(self, timeStepIndex: int) -> Dict[int,int]:
		"""Number of pump battery lag pumps running duing the current time step.

		Args:
			timeStepIndex(int): timeStepIndex

		Returns:
			Dict[int,int]: 
		"""
		pass

	@overload
	def IVSPBsResults(self, ids: List[int], timeStepIndex: int) -> Dict[int,int]:
		"""No Description

		Args:
			ids(List[int]): ids
			timeStepIndex(int): timeStepIndex

		Returns:
			Dict[int,int]: 
		"""
		pass

class IVSPBResults(IBasePumpResults):

	def __init__(self) -> None:
		"""Creating a new Instance of this class is not allowed


		Raises:
			Exception: if this class is instanciated
		"""
		raise Exception("Creating a new Instance of this class is not allowed")
		pass

	@overload
	def IVSPBResults(self) -> Union[float, None]:
		"""Flow contributed by the lead pump in the pump battery.

		Returns:
			Nullable: 
		"""
		pass

	@overload
	def IVSPBResults(self, timeStepIndex: int) -> Union[float, None]:
		"""Flow contributed by the lead pump in the pump battery.

		Args:
			timeStepIndex(int): timeStepIndex

		Returns:
			Nullable: 
		"""
		pass

	@overload
	def IVSPBResults(self) -> Union[float, None]:
		"""Number of pump battery lag pumps running duing the current time step.

		Returns:
			Nullable: 
		"""
		pass

	@overload
	def IVSPBResults(self, timeStepIndex: int) -> Union[float, None]:
		"""Number of pump battery lag pumps running duing the current time step.

		Args:
			timeStepIndex(int): timeStepIndex

		Returns:
			Nullable: 
		"""
		pass

	def LoadPumpFlows(self) -> array(Union[float, None]):
		"""Flow contributed by the lead pump in the pump battery.

		Returns:
			array(): 
		"""
		pass

	def NumberRunningLagPumps(self) -> array(Union[float, None]):
		"""Number of pump battery lag pumps running duing the current time step.

		Returns:
			array(): 
		"""
		pass

class IVariableSpeedPumpBatteryUnits(IBasePumpUnits):

	def __init__(self) -> None:
		"""Creating a new Instance of this class is not allowed


		Raises:
			Exception: if this class is instanciated
		"""
		raise Exception("Creating a new Instance of this class is not allowed")
		pass

class IBaseValvesResults(IBaseDirectedNodesResults):

	def __init__(self) -> None:
		"""Creating a new Instance of this class is not allowed


		Raises:
			Exception: if this class is instanciated
		"""
		raise Exception("Creating a new Instance of this class is not allowed")
		pass

	@overload
	def IBaseValvesResults(self) -> Dict[int,int]:
		"""Total flow through at all valve at the current time step.

		Returns:
			Dict[int,int]: 
		"""
		pass

	@overload
	def IBaseValvesResults(self, timeStepIndex: int) -> Dict[int,int]:
		"""Total flow through at all valve at the given time step.

		Args:
			timeStepIndex(int): timeStepIndex

		Returns:
			Dict[int,int]: 
		"""
		pass

	@overload
	def IBaseValvesResults(self, ids: List[int], timeStepIndex: int) -> Dict[int,int]:
		"""No Description

		Args:
			ids(List[int]): ids
			timeStepIndex(int): timeStepIndex

		Returns:
			Dict[int,int]: 
		"""
		pass

	@overload
	def IBaseValvesResults(self) -> Dict[int,int]:
		"""Velocity of flow traveling through the valve at the current time step.

		Returns:
			Dict[int,int]: 
		"""
		pass

	@overload
	def IBaseValvesResults(self, timeStepIndex: int) -> Dict[int,int]:
		"""Velocity of flow traveling through the valves at the given time step.

		Args:
			timeStepIndex(int): timeStepIndex

		Returns:
			Dict[int,int]: 
		"""
		pass

	@overload
	def IBaseValvesResults(self, ids: List[int], timeStepIndex: int) -> Dict[int,int]:
		"""No Description

		Args:
			ids(List[int]): ids
			timeStepIndex(int): timeStepIndex

		Returns:
			Dict[int,int]: 
		"""
		pass

	@overload
	def IBaseValvesResults(self) -> Dict[int,int]:
		"""Change in head across all valves at the current time step.

		Returns:
			Dict[int,int]: 
		"""
		pass

	@overload
	def IBaseValvesResults(self, timeStepIndex: int) -> Dict[int,int]:
		"""Change in head across all valves at the given time step.

		Args:
			timeStepIndex(int): timeStepIndex

		Returns:
			Dict[int,int]: 
		"""
		pass

	@overload
	def IBaseValvesResults(self, ids: List[int], timeStepIndex: int) -> Dict[int,int]:
		"""No Description

		Args:
			ids(List[int]): ids
			timeStepIndex(int): timeStepIndex

		Returns:
			Dict[int,int]: 
		"""
		pass

	@overload
	def IBaseValvesResults(self) -> Dict[int,int]:
		"""Change in pressure across all valves at the current time step.

		Returns:
			Dict[int,int]: 
		"""
		pass

	@overload
	def IBaseValvesResults(self, timeStepIndex: int) -> Dict[int,int]:
		"""Change in pressure across all valves at the given time step.

		Args:
			timeStepIndex(int): timeStepIndex

		Returns:
			Dict[int,int]: 
		"""
		pass

	@overload
	def IBaseValvesResults(self, ids: List[int], timeStepIndex: int) -> Dict[int,int]:
		"""No Description

		Args:
			ids(List[int]): ids
			timeStepIndex(int): timeStepIndex

		Returns:
			Dict[int,int]: 
		"""
		pass

	@overload
	def IBaseValvesResults(self) -> Dict[int,int]:
		"""Calculated hydraulic grade at the entrance of all valves at the current time step.

		Returns:
			Dict[int,int]: 
		"""
		pass

	@overload
	def IBaseValvesResults(self, timeStepIndex: int) -> Dict[int,int]:
		"""Calculated hydraulic grade at the entrance of all valves at the given time step.

		Args:
			timeStepIndex(int): timeStepIndex

		Returns:
			Dict[int,int]: 
		"""
		pass

	@overload
	def IBaseValvesResults(self, ids: List[int], timeStepIndex: int) -> Dict[int,int]:
		"""No Description

		Args:
			ids(List[int]): ids
			timeStepIndex(int): timeStepIndex

		Returns:
			Dict[int,int]: 
		"""
		pass

	@overload
	def IBaseValvesResults(self) -> Dict[int,int]:
		"""Calculated hydraulic grade at the exit of all valves at the current time step.

		Returns:
			Dict[int,int]: 
		"""
		pass

	@overload
	def IBaseValvesResults(self, timeStepIndex: int) -> Dict[int,int]:
		"""Calculated hydraulic grade at the exit of all valves at the given time step.

		Args:
			timeStepIndex(int): timeStepIndex

		Returns:
			Dict[int,int]: 
		"""
		pass

	@overload
	def IBaseValvesResults(self, ids: List[int], timeStepIndex: int) -> Dict[int,int]:
		"""No Description

		Args:
			ids(List[int]): ids
			timeStepIndex(int): timeStepIndex

		Returns:
			Dict[int,int]: 
		"""
		pass

	@overload
	def IBaseValvesResults(self) -> Dict[int,int]:
		"""Calculated pressure at the entrance of all valves at the current time step.

		Returns:
			Dict[int,int]: 
		"""
		pass

	@overload
	def IBaseValvesResults(self, timeStepIndex: int) -> Dict[int,int]:
		"""Calculated pressure at the entrance of all valves at the given time step.

		Args:
			timeStepIndex(int): timeStepIndex

		Returns:
			Dict[int,int]: 
		"""
		pass

	@overload
	def IBaseValvesResults(self, ids: List[int], timeStepIndex: int) -> Dict[int,int]:
		"""No Description

		Args:
			ids(List[int]): ids
			timeStepIndex(int): timeStepIndex

		Returns:
			Dict[int,int]: 
		"""
		pass

	@overload
	def IBaseValvesResults(self) -> Dict[int,int]:
		"""Calculated pressure at the exit to all valves at the current time step.

		Returns:
			Dict[int,int]: 
		"""
		pass

	@overload
	def IBaseValvesResults(self, timeStepIndex: int) -> Dict[int,int]:
		"""Calculated pressure at the exit to all valves at the given time step.

		Args:
			timeStepIndex(int): timeStepIndex

		Returns:
			Dict[int,int]: 
		"""
		pass

	@overload
	def IBaseValvesResults(self, ids: List[int], timeStepIndex: int) -> Dict[int,int]:
		"""No Description

		Args:
			ids(List[int]): ids
			timeStepIndex(int): timeStepIndex

		Returns:
			Dict[int,int]: 
		"""
		pass

	@overload
	def IBaseValvesResults(self) -> Dict[int,int]:
		"""Displays the current calculated status (Open, Closed etc...) of all valves at the current time step.

		Returns:
			Dict[int,int]: 
		"""
		pass

	@overload
	def IBaseValvesResults(self, timeStepIndex: int) -> Dict[int,int]:
		"""Di plays the current calculated status (Open, Closed etc...) of all valves at the given time step.

		Args:
			timeStepIndex(int): timeStepIndex

		Returns:
			Dict[int,int]: 
		"""
		pass

	@overload
	def IBaseValvesResults(self, ids: List[int], timeStepIndex: int) -> Dict[int,int]:
		"""No Description

		Args:
			ids(List[int]): ids
			timeStepIndex(int): timeStepIndex

		Returns:
			Dict[int,int]: 
		"""
		pass

class IBaseValveResults(IBaseDirectedNodeResults):

	def __init__(self) -> None:
		"""Creating a new Instance of this class is not allowed


		Raises:
			Exception: if this class is instanciated
		"""
		raise Exception("Creating a new Instance of this class is not allowed")
		pass

	@overload
	def IBaseValveResults(self) -> Union[float, None]:
		"""Total flow through the valve at the current time step.

		Returns:
			Nullable: 
		"""
		pass

	@overload
	def IBaseValveResults(self, timeStepIndex: int) -> Union[float, None]:
		"""Total flow through the valve at the given time step.

		Args:
			timeStepIndex(int): timeStepIndex

		Returns:
			Nullable: 
		"""
		pass

	@overload
	def IBaseValveResults(self) -> Union[float, None]:
		"""Velocity of flow traveling through the valve at the current time step.

		Returns:
			Nullable: 
		"""
		pass

	@overload
	def IBaseValveResults(self, timeStepIndex: int) -> Union[float, None]:
		"""Velocity of flow traveling through the valve at the given time step.

		Args:
			timeStepIndex(int): timeStepIndex

		Returns:
			Nullable: 
		"""
		pass

	@overload
	def IBaseValveResults(self) -> Union[float, None]:
		"""Change in head across the valve at the current time step.

		Returns:
			Nullable: 
		"""
		pass

	@overload
	def IBaseValveResults(self, timeStepIndex: int) -> Union[float, None]:
		"""Change in head across the valve at the given time step.

		Args:
			timeStepIndex(int): timeStepIndex

		Returns:
			Nullable: 
		"""
		pass

	@overload
	def IBaseValveResults(self) -> Union[float, None]:
		"""Change in pressure across the valve at the current time step.

		Returns:
			Nullable: 
		"""
		pass

	@overload
	def IBaseValveResults(self, timeStepIndex: int) -> Union[float, None]:
		"""Change in pressure across the valve at the given time step.

		Args:
			timeStepIndex(int): timeStepIndex

		Returns:
			Nullable: 
		"""
		pass

	@overload
	def IBaseValveResults(self) -> Union[float, None]:
		"""Calculated hydraulic grade at the entrance of the valve at the current time step.

		Returns:
			Nullable: 
		"""
		pass

	@overload
	def IBaseValveResults(self, timeStepIndex: int) -> Union[float, None]:
		"""Calculated hydraulic grade at the entrance of the valve at the given time step.

		Args:
			timeStepIndex(int): timeStepIndex

		Returns:
			Nullable: 
		"""
		pass

	@overload
	def IBaseValveResults(self) -> Union[float, None]:
		"""Calculated hydraulic grade at the exit of the valve at the current time step.

		Returns:
			Nullable: 
		"""
		pass

	@overload
	def IBaseValveResults(self, timeStepIndex: int) -> Union[float, None]:
		"""Calculated hydraulic grade at the exit of the valve at the given time step.

		Args:
			timeStepIndex(int): timeStepIndex

		Returns:
			Nullable: 
		"""
		pass

	@overload
	def IBaseValveResults(self) -> Union[float, None]:
		"""Calculated pressure at the entrance of the valve at the current time step.

		Returns:
			Nullable: 
		"""
		pass

	@overload
	def IBaseValveResults(self, timeStepIndex: int) -> Union[float, None]:
		"""Calculated pressure at the entrance of the valve at the given time step.

		Args:
			timeStepIndex(int): timeStepIndex

		Returns:
			Nullable: 
		"""
		pass

	@overload
	def IBaseValveResults(self) -> Union[float, None]:
		"""Calculated pressure at the exit to the valve at the current time step.

		Returns:
			Nullable: 
		"""
		pass

	@overload
	def IBaseValveResults(self, timeStepIndex: int) -> Union[float, None]:
		"""Calculated pressure at the exit to the valve at the given time step.

		Args:
			timeStepIndex(int): timeStepIndex

		Returns:
			Nullable: 
		"""
		pass

	@overload
	def IBaseValveResults(self) -> Union[int, None]:
		"""Di plays the current calculated status (Open, Closed etc...) of the selected valve at the current time step.

		Returns:
			Nullable: 
		"""
		pass

	@overload
	def IBaseValveResults(self, timeStepIndex: int) -> Union[int, None]:
		"""Di plays the current calculated status (Open, Closed etc...) of the selected valve at the given time step.

		Args:
			timeStepIndex(int): timeStepIndex

		Returns:
			Nullable: 
		"""
		pass

	def Flows(self) -> array(Union[float, None]):
		"""Total flow through the valve across all time steps.

		Returns:
			array(): 
		"""
		pass

	def Velocities(self) -> array(Union[float, None]):
		"""Velocity of flow traveling through the valve across all time steps.

		Returns:
			array(): 
		"""
		pass

	def Headlosses(self) -> array(Union[float, None]):
		"""Change in head across the valve across all time steps.

		Returns:
			array(): 
		"""
		pass

	def PressureLosses(self) -> array(Union[float, None]):
		"""Change in pressure across the valve across all time steps.

		Returns:
			array(): 
		"""
		pass

	def FromHydraulicGrades(self) -> array(Union[float, None]):
		"""Calculated hydraulic grade at the entrance of the valve across all time steps.

		Returns:
			array(): 
		"""
		pass

	def ToHydraulicGrades(self) -> array(Union[float, None]):
		"""Calculated hydraulic grade at the exit of the valve across all time steps.

		Returns:
			array(): 
		"""
		pass

	def FromPressures(self) -> array(Union[float, None]):
		"""Calculated pressure at the entrance of the valve across all time steps.

		Returns:
			array(): 
		"""
		pass

	def ToPressures(self) -> array(Union[float, None]):
		"""Calculated pressure at the exit to the valve across all time steps.

		Returns:
			array(): 
		"""
		pass

	def CalculatedStatuses(self) -> array(Union[int, None]):
		"""Di plays the current calculated status (Open, Closed etc...) of the selected valve across all time steps.

		Returns:
			array(): 
		"""
		pass

class IBaseValveInput(IBaseDirectedNodeInput):

	def __init__(self) -> None:
		"""Creating a new Instance of this class is not allowed


		Raises:
			Exception: if this class is instanciated
		"""
		raise Exception("Creating a new Instance of this class is not allowed")
		pass

	@property
	def InitialStatus(self) -> ValveSettingType:
		"""No Description

		Returns:
			IBaseValveInput: 
		"""
		pass

	@property
	def ValveDiameter(self) -> float:
		"""No Description

		Returns:
			IBaseValveInput: 
		"""
		pass

	@property
	def MinorLossCoefficientCollection(self) -> IMinorLossCoefficientCollection:
		"""No Description

		Returns:
			IBaseValveInput: 
		"""
		pass

	@property
	def LocalMinorLossCoefficient(self) -> float:
		"""No Description

		Returns:
			IBaseValveInput: 
		"""
		pass

	@property
	def SpecifyLocalMinorLoss(self) -> bool:
		"""No Description

		Returns:
			IBaseValveInput: 
		"""
		pass

	@property
	def DerivedMinorLossCoefficient(self) -> float:
		"""No Description

		Returns:
			IBaseValveInput: 
		"""
		pass

	@InitialStatus.setter
	def InitialStatus(self, initialstatus: ValveSettingType) -> None:
		pass

	@ValveDiameter.setter
	def ValveDiameter(self, valvediameter: float) -> None:
		pass

	@LocalMinorLossCoefficient.setter
	def LocalMinorLossCoefficient(self, localminorlosscoefficient: float) -> None:
		pass

	@SpecifyLocalMinorLoss.setter
	def SpecifyLocalMinorLoss(self, specifylocalminorloss: bool) -> None:
		pass

class IBaseValvesInput(IBaseDirectedNodesInput):

	def __init__(self) -> None:
		"""Creating a new Instance of this class is not allowed


		Raises:
			Exception: if this class is instanciated
		"""
		raise Exception("Creating a new Instance of this class is not allowed")
		pass

	@overload
	def IBaseValvesInput(self) -> Dict[int,int]:
		"""Set the initial status for the valve.

		Returns:
			Dict[int,int]: 
		"""
		pass

	@overload
	def IBaseValvesInput(self, ids: List[int]) -> Dict[int,int]:
		"""No Description

		Args:
			ids(List[int]): ids

		Returns:
			Dict[int,int]: 
		"""
		pass

	@overload
	def IBaseValvesInput(self) -> Dict[int,int]:
		"""Inside diameter of the valve. Used to calculate the velocity through the valve and a corresponding minor loss when a minor loss coefficient is entered.

		Returns:
			Dict[int,int]: 
		"""
		pass

	@overload
	def IBaseValvesInput(self, ids: List[int]) -> Dict[int,int]:
		"""No Description

		Args:
			ids(List[int]): ids

		Returns:
			Dict[int,int]: 
		"""
		pass

	def LocalMinorLossCoefficient(self) -> Dict[int,int]:
		"""User input minor loss coefficent.  You can either type in the value directly or select the value from the Minor Loss Library. The minor loss is applied to the valve when it is fully open (inactive). Note that minor losses do not apply to the following valve types: General Purpose Valve and Valve With Linear Area Change. These two valve types do not support a (fully) open status and always apply the head/flow relationship defined by their headloss curve and discharge coefficient respectively.

		Returns:
			Dict[int,int]: 
		"""
		pass

	def SpecifyLocalMinorLoss(self) -> Dict[int,int]:
		"""If true then the minor coefficent for the element is manually set, otherwise the value is derived from the minor loss library.

		Returns:
			Dict[int,int]: 
		"""
		pass

	def DerivedMinorLossCoefficient(self) -> Dict[int,int]:
		"""Displays the composite value calculated from the data in the minor loss collection. The composite minor loss is applied to the valve when it is fully open (inactive). Note that minor losses do not apply to the following valve types: General Purpose Valve and Valve With Linear Area Change. These two valve types do not support a (fully) open status and always apply the head/flow relationship defined by their headloss curve and discharge coefficient respectively.

		Returns:
			Dict[int,int]: 
		"""
		pass

class IBaseValveUnits(IBaseDirectedNodeUnits):

	def __init__(self) -> None:
		"""Creating a new Instance of this class is not allowed


		Raises:
			Exception: if this class is instanciated
		"""
		raise Exception("Creating a new Instance of this class is not allowed")
		pass

	@property
	def ValveDiameterUnit(self) -> IUnit:
		"""No Description

		Returns:
			IBaseValveUnits: 
		"""
		pass

	@property
	def FlowUnit(self) -> IUnit:
		"""No Description

		Returns:
			IBaseValveUnits: 
		"""
		pass

	@property
	def VelocityUnit(self) -> IUnit:
		"""No Description

		Returns:
			IBaseValveUnits: 
		"""
		pass

	@property
	def HeadlossUnit(self) -> IUnit:
		"""No Description

		Returns:
			IBaseValveUnits: 
		"""
		pass

	@property
	def PressureLossUnit(self) -> IUnit:
		"""No Description

		Returns:
			IBaseValveUnits: 
		"""
		pass

	@property
	def HydraulicGradeUnit(self) -> IUnit:
		"""No Description

		Returns:
			IBaseValveUnits: 
		"""
		pass

	@property
	def PressureUnit(self) -> IUnit:
		"""No Description

		Returns:
			IBaseValveUnits: 
		"""
		pass

class IFlowControlValves(IWaterNetworkElements[IFlowControlValves, IFlowControlValve, IFlowControlValveUnits, IFlowControlValveInput, IFlowControlValveResults, IFlowControlValvesInput, IFlowControlValvesResults]):

	def __init__(self) -> None:
		"""Creating a new Instance of this class is not allowed


		Raises:
			Exception: if this class is instanciated
		"""
		raise Exception("Creating a new Instance of this class is not allowed")
		pass

class IFlowControlValve(IWaterNetworkElement[IFlowControlValves, IFlowControlValve, IFlowControlValveUnits, IFlowControlValveInput, IFlowControlValveResults, IFlowControlValvesInput, IFlowControlValvesResults]):

	def __init__(self) -> None:
		"""Creating a new Instance of this class is not allowed


		Raises:
			Exception: if this class is instanciated
		"""
		raise Exception("Creating a new Instance of this class is not allowed")
		pass

class IFlowControlValvesResults(IBaseValvesResults):

	def __init__(self) -> None:
		"""Creating a new Instance of this class is not allowed


		Raises:
			Exception: if this class is instanciated
		"""
		raise Exception("Creating a new Instance of this class is not allowed")
		pass

	@overload
	def IFlowControlValvesResults(self) -> Dict[int,int]:
		"""Flow setting for current time step at all FCVs.

		Returns:
			Dict[int,int]: 
		"""
		pass

	@overload
	def IFlowControlValvesResults(self, timeStepIndex: int) -> Dict[int,int]:
		"""Flow setting for given time step at all FCVs.

		Args:
			timeStepIndex(int): timeStepIndex

		Returns:
			Dict[int,int]: 
		"""
		pass

	@overload
	def IFlowControlValvesResults(self, ids: List[int], timeStepInde: int) -> Dict[int,int]:
		"""No Description

		Args:
			ids(List[int]): ids
			timeStepInde(int): timeStepInde

		Returns:
			Dict[int,int]: 
		"""
		pass

class IFlowControlValveResults(IBaseValveResults):

	def __init__(self) -> None:
		"""Creating a new Instance of this class is not allowed


		Raises:
			Exception: if this class is instanciated
		"""
		raise Exception("Creating a new Instance of this class is not allowed")
		pass

	@overload
	def IFlowControlValveResults(self) -> Union[float, None]:
		"""Flow setting at selected valve for current time step.

		Returns:
			Nullable: 
		"""
		pass

	@overload
	def IFlowControlValveResults(self, timeStepIndex: int) -> Union[float, None]:
		"""Flow setting at selected valve for given time step.

		Args:
			timeStepIndex(int): timeStepIndex

		Returns:
			Nullable: 
		"""
		pass

	def CalculatedFlowSettings(self) -> array(Union[float, None]):
		"""Flow setting at selected valve across all time steps.

		Returns:
			array(): 
		"""
		pass

class IFlowControlValvesInput(IBaseValvesInput):

	def __init__(self) -> None:
		"""Creating a new Instance of this class is not allowed


		Raises:
			Exception: if this class is instanciated
		"""
		raise Exception("Creating a new Instance of this class is not allowed")
		pass

	@overload
	def IFlowControlValvesInput(self) -> Dict[int,int]:
		"""Initial flow setting for all flow control valves.

		Returns:
			Dict[int,int]: 
		"""
		pass

	@overload
	def IFlowControlValvesInput(self, ids: List[int]) -> Dict[int,int]:
		"""No Description

		Args:
			ids(List[int]): ids

		Returns:
			Dict[int,int]: 
		"""
		pass

	def ValveCharacteristics(self) -> Dict[int,int]:
		"""Specifies the valve characteristics definition to be used for this valve. If the Valve Characteristic Curve is not defined then a default curve will be used. The default curve will have (Relative Closure, Relative Area) points of (0,1) and (1,0).

		Returns:
			Dict[int,int]: 
		"""
		pass

	def ValveTypes(self) -> Dict[int,int]:
		"""Specifies the type of valve. Choices are Butterfly, Needle, Circular Gate, Globe, Ball and User Defined.

		Returns:
			Dict[int,int]: 
		"""
		pass

class IFlowControlValveInput(IBaseValveInput):

	def __init__(self) -> None:
		"""Creating a new Instance of this class is not allowed


		Raises:
			Exception: if this class is instanciated
		"""
		raise Exception("Creating a new Instance of this class is not allowed")
		pass

	@property
	def InitialFlowSetting(self) -> float:
		"""No Description

		Returns:
			IFlowControlValveInput: 
		"""
		pass

	@property
	def ValveCharacteristics(self) -> IValveCharacteristic:
		"""No Description

		Returns:
			IFlowControlValveInput: 
		"""
		pass

	@property
	def ValveType(self) -> HammerValveType:
		"""No Description

		Returns:
			IFlowControlValveInput: 
		"""
		pass

	@InitialFlowSetting.setter
	def InitialFlowSetting(self, initialflowsetting: float) -> None:
		pass

	@ValveCharacteristics.setter
	def ValveCharacteristics(self, valvecharacteristics: IValveCharacteristic) -> None:
		pass

	@ValveType.setter
	def ValveType(self, valvetype: HammerValveType) -> None:
		pass

class IFlowControlValveUnits(IBaseValveUnits):

	def __init__(self) -> None:
		"""Creating a new Instance of this class is not allowed


		Raises:
			Exception: if this class is instanciated
		"""
		raise Exception("Creating a new Instance of this class is not allowed")
		pass

	@property
	def InitialFlowSettingUnit(self) -> IUnit:
		"""No Description

		Returns:
			IFlowControlValveUnits: 
		"""
		pass

class IThrottleControlValves(IWaterNetworkElements[IThrottleControlValves, IThrottleControlValve, IThrottleControlValveUnits, IThrottleControlValveInput, IThrottleControlValveResults, IThrottleControlValvesInput, IThrottleControlValvesResults]):

	def __init__(self) -> None:
		"""Creating a new Instance of this class is not allowed


		Raises:
			Exception: if this class is instanciated
		"""
		raise Exception("Creating a new Instance of this class is not allowed")
		pass

class IThrottleControlValve(IWaterNetworkElement[IThrottleControlValves, IThrottleControlValve, IThrottleControlValveUnits, IThrottleControlValveInput, IThrottleControlValveResults, IThrottleControlValvesInput, IThrottleControlValvesResults]):

	def __init__(self) -> None:
		"""Creating a new Instance of this class is not allowed


		Raises:
			Exception: if this class is instanciated
		"""
		raise Exception("Creating a new Instance of this class is not allowed")
		pass

class IThrottleControlValvesResults(IBaseValvesResults):

	def __init__(self) -> None:
		"""Creating a new Instance of this class is not allowed


		Raises:
			Exception: if this class is instanciated
		"""
		raise Exception("Creating a new Instance of this class is not allowed")
		pass

	@overload
	def IThrottleControlValvesResults(self) -> Dict[int,int]:
		"""Discharge Coefficient:  Discharge coefficient setting (Cv) at the current time step across all TCVs.

		Returns:
			Dict[int,int]: 
		"""
		pass

	@overload
	def IThrottleControlValvesResults(self, timeStepIndex: int) -> Dict[int,int]:
		"""Discharge Coefficient:  Discharge coefficient setting (Cv) at the given time step across all TCVs.

		Args:
			timeStepIndex(int): timeStepIndex

		Returns:
			Dict[int,int]: 
		"""
		pass

	@overload
	def IThrottleControlValvesResults(self, ids: List[int], timeStepIndex: int) -> Dict[int,int]:
		"""No Description

		Args:
			ids(List[int]): ids
			timeStepIndex(int): timeStepIndex

		Returns:
			Dict[int,int]: 
		"""
		pass

class IThrottleControlValveResults(IBaseValveResults):

	def __init__(self) -> None:
		"""Creating a new Instance of this class is not allowed


		Raises:
			Exception: if this class is instanciated
		"""
		raise Exception("Creating a new Instance of this class is not allowed")
		pass

	@overload
	def IThrottleControlValveResults(self) -> Union[float, None]:
		"""Discharge Coefficient:  TCV discharge coefficient setting (Cv) at the current time step.

		Returns:
			Nullable: 
		"""
		pass

	@overload
	def IThrottleControlValveResults(self, timeStepIndex: int) -> Union[float, None]:
		"""Discharge Coefficient:  TCV discharge coefficient setting (Cv) at the given time step.

		Args:
			timeStepIndex(int): timeStepIndex

		Returns:
			Nullable: 
		"""
		pass

	def CalculatedSettings(self) -> array(Union[float, None]):
		"""Discharge Coefficient:  TCV discharge coefficient setting (Cv) at all time steps.

		Returns:
			array(): 
		"""
		pass

class IThrottleControlValveInput(IBaseValveInput):

	def __init__(self) -> None:
		"""Creating a new Instance of this class is not allowed


		Raises:
			Exception: if this class is instanciated
		"""
		raise Exception("Creating a new Instance of this class is not allowed")
		pass

	@property
	def TCVCoefficientType(self) -> TCVCoefficientType:
		"""No Description

		Returns:
			IThrottleControlValveInput: 
		"""
		pass

	@property
	def InitialCoefficient(self) -> float:
		"""No Description

		Returns:
			IThrottleControlValveInput: 
		"""
		pass

	@property
	def ValveCharacteristics(self) -> IValveCharacteristic:
		"""No Description

		Returns:
			IThrottleControlValveInput: 
		"""
		pass

	@property
	def ValveType(self) -> HammerValveType:
		"""No Description

		Returns:
			IThrottleControlValveInput: 
		"""
		pass

	@TCVCoefficientType.setter
	def TCVCoefficientType(self, tcvcoefficienttype: TCVCoefficientType) -> None:
		pass

	@InitialCoefficient.setter
	def InitialCoefficient(self, initialcoefficient: float) -> None:
		pass

	@ValveCharacteristics.setter
	def ValveCharacteristics(self, valvecharacteristics: IValveCharacteristic) -> None:
		pass

	@ValveType.setter
	def ValveType(self, valvetype: HammerValveType) -> None:
		pass

class IThrottleControlValvesInput(IBaseValvesInput):

	def __init__(self) -> None:
		"""Creating a new Instance of this class is not allowed


		Raises:
			Exception: if this class is instanciated
		"""
		raise Exception("Creating a new Instance of this class is not allowed")
		pass

	@overload
	def IThrottleControlValvesInput(self) -> Dict[int,int]:
		"""Specifies which type of coefficient to enter for the TCV. If entering discharge coefficient, the value is internally converted into an equivalent headloss coefficient.

		Returns:
			Dict[int,int]: 
		"""
		pass

	@overload
	def IThrottleControlValvesInput(self, ids: List[int]) -> Dict[int,int]:
		"""No Description

		Args:
			ids(List[int]): ids

		Returns:
			Dict[int,int]: 
		"""
		pass

	@overload
	def IThrottleControlValvesInput(self) -> Dict[int,int]:
		"""(A relative closure of 0%% means the valve is 0%% closed, or 100%% open. Conversely, a relative closure of 100%% means the valve is 100%% closed, or 0%% open).

		Returns:
			Dict[int,int]: 
		"""
		pass

	@overload
	def IThrottleControlValvesInput(self, ids: List[int]) -> Dict[int,int]:
		"""No Description

		Args:
			ids(List[int]): ids

		Returns:
			Dict[int,int]: 
		"""
		pass

	def ValveCharacteristics(self) -> Dict[int,int]:
		"""Specifies the valve characteristics definition to be used for this valve. If the Valve Characteristic Curve is not defined then a default curve will be used. The default curve will have (Relative Closure, Relative Area) points of (0,1) and (1,0).

		Returns:
			Dict[int,int]: 
		"""
		pass

	def ValveTypes(self) -> Dict[int,int]:
		"""Specifies the type of valve. Choices are Butterfly, Needle, Circular Gate, Globe, Ball and User Defined.

		Returns:
			Dict[int,int]: 
		"""
		pass

class IThrottleControlValveUnits(IBaseValveUnits):

	def __init__(self) -> None:
		"""Creating a new Instance of this class is not allowed


		Raises:
			Exception: if this class is instanciated
		"""
		raise Exception("Creating a new Instance of this class is not allowed")
		pass

	@property
	def CoefficientUnit(self) -> IUnit:
		"""No Description

		Returns:
			IThrottleControlValveUnits: 
		"""
		pass

class IGeneralPurposeValves(IWaterNetworkElements[IGeneralPurposeValves, IGeneralPurposeValve, IGeneralPurposeValveUnits, IGeneralPurposeValveInput, IGeneralPurposeValveResults, IGeneralPurposeValvesInput, IGeneralPurposeValvesResults]):

	def __init__(self) -> None:
		"""Creating a new Instance of this class is not allowed


		Raises:
			Exception: if this class is instanciated
		"""
		raise Exception("Creating a new Instance of this class is not allowed")
		pass

class IGeneralPurposeValve(IWaterNetworkElement[IGeneralPurposeValves, IGeneralPurposeValve, IGeneralPurposeValveUnits, IGeneralPurposeValveInput, IGeneralPurposeValveResults, IGeneralPurposeValvesInput, IGeneralPurposeValvesResults]):

	def __init__(self) -> None:
		"""Creating a new Instance of this class is not allowed


		Raises:
			Exception: if this class is instanciated
		"""
		raise Exception("Creating a new Instance of this class is not allowed")
		pass

class IGeneralPurposeValvesInput(IBaseValvesInput):

	def __init__(self) -> None:
		"""Creating a new Instance of this class is not allowed


		Raises:
			Exception: if this class is instanciated
		"""
		raise Exception("Creating a new Instance of this class is not allowed")
		pass

	def GPVHeadlossCurves(self) -> Dict[int,int]:
		"""Select the GPV headloss curve to apply to the selected valve. The General Purpose Valve is a fictitious element allowing simulation of unique headloss/flow relationships, therefore, the headloss curve relationship is always applied. Minor losses are never applied for this valve type and as such the valve does not support a (fully) open status.

		Returns:
			Dict[int,int]: 
		"""
		pass

	def ValveCharacteristics(self) -> Dict[int,int]:
		"""Specifies the valve characteristics definition to be used for this valve. If the Valve Characteristic Curve is not defined then a default curve will be used. The default curve will have (Relative Closure, Relative Area) points of (0,1) and (1,0).

		Returns:
			Dict[int,int]: 
		"""
		pass

	def ValveTypes(self) -> Dict[int,int]:
		"""Specifies the type of valve. Choices are Butterfly, Needle, Circular Gate, Globe, Ball and User Defined.

		Returns:
			Dict[int,int]: 
		"""
		pass

class IGeneralPurposeValvesResults(IBaseValvesResults):

	def __init__(self) -> None:
		"""Creating a new Instance of this class is not allowed


		Raises:
			Exception: if this class is instanciated
		"""
		raise Exception("Creating a new Instance of this class is not allowed")
		pass

class IGeneralPurposeValveResults(IBaseValveResults):

	def __init__(self) -> None:
		"""Creating a new Instance of this class is not allowed


		Raises:
			Exception: if this class is instanciated
		"""
		raise Exception("Creating a new Instance of this class is not allowed")
		pass

class IGeneralPurposeValveInput(IBaseValveInput):

	def __init__(self) -> None:
		"""Creating a new Instance of this class is not allowed


		Raises:
			Exception: if this class is instanciated
		"""
		raise Exception("Creating a new Instance of this class is not allowed")
		pass

	@property
	def GPVHeadlossCurve(self) -> IGPVHeadlossCurve:
		"""No Description

		Returns:
			IGeneralPurposeValveInput: 
		"""
		pass

	@property
	def ValveCharacteristics(self) -> IValveCharacteristic:
		"""No Description

		Returns:
			IGeneralPurposeValveInput: 
		"""
		pass

	@property
	def ValveType(self) -> HammerValveType:
		"""No Description

		Returns:
			IGeneralPurposeValveInput: 
		"""
		pass

	@GPVHeadlossCurve.setter
	def GPVHeadlossCurve(self, gpvheadlosscurve: IGPVHeadlossCurve) -> None:
		pass

	@ValveCharacteristics.setter
	def ValveCharacteristics(self, valvecharacteristics: IValveCharacteristic) -> None:
		pass

	@ValveType.setter
	def ValveType(self, valvetype: HammerValveType) -> None:
		pass

class IGeneralPurposeValveUnits(IBaseValveUnits):

	def __init__(self) -> None:
		"""Creating a new Instance of this class is not allowed


		Raises:
			Exception: if this class is instanciated
		"""
		raise Exception("Creating a new Instance of this class is not allowed")
		pass

class IPressureValvesResults(IBaseValvesResults):

	def __init__(self) -> None:
		"""Creating a new Instance of this class is not allowed


		Raises:
			Exception: if this class is instanciated
		"""
		raise Exception("Creating a new Instance of this class is not allowed")
		pass

	@overload
	def IPressureValvesResults(self) -> Dict[int,int]:
		"""Pressure:  Pressure setting for all pressure valves at current time step.

		Returns:
			Dict[int,int]: 
		"""
		pass

	@overload
	def IPressureValvesResults(self, timeStepIndex: int) -> Dict[int,int]:
		"""Pressure:  Pressure setting for all pressure valves at given time step.

		Args:
			timeStepIndex(int): timeStepIndex

		Returns:
			Dict[int,int]: 
		"""
		pass

	@overload
	def IPressureValvesResults(self, ids: List[int], timeStepIndex: int) -> Dict[int,int]:
		"""No Description

		Args:
			ids(List[int]): ids
			timeStepIndex(int): timeStepIndex

		Returns:
			Dict[int,int]: 
		"""
		pass

class IPressureValveResults(IBaseValveResults):

	def __init__(self) -> None:
		"""Creating a new Instance of this class is not allowed


		Raises:
			Exception: if this class is instanciated
		"""
		raise Exception("Creating a new Instance of this class is not allowed")
		pass

	@overload
	def IPressureValveResults(self) -> Union[float, None]:
		"""Pressure:  Pressure setting for valve at current time step.

		Returns:
			Nullable: 
		"""
		pass

	@overload
	def IPressureValveResults(self, timeStepIndex: int) -> Union[float, None]:
		"""Pressure:  Pressure setting for valve at given time step.

		Args:
			timeStepIndex(int): timeStepIndex

		Returns:
			Nullable: 
		"""
		pass

	def CalculatedSettings(self) -> array(Union[float, None]):
		"""Pressure:  Pressure setting for valve across all time steps.

		Returns:
			array(): 
		"""
		pass

class IPressureValveInput(IBaseValveInput):

	def __init__(self) -> None:
		"""Creating a new Instance of this class is not allowed


		Raises:
			Exception: if this class is instanciated
		"""
		raise Exception("Creating a new Instance of this class is not allowed")
		pass

	@property
	def PressureValveSetting(self) -> PressureValvesettingType:
		"""No Description

		Returns:
			IPressureValveInput: 
		"""
		pass

	@property
	def InitialSetting(self) -> float:
		"""No Description

		Returns:
			IPressureValveInput: 
		"""
		pass

	@PressureValveSetting.setter
	def PressureValveSetting(self, pressurevalvesetting: PressureValvesettingType) -> None:
		pass

	@InitialSetting.setter
	def InitialSetting(self, initialsetting: float) -> None:
		pass

class IPressureValvesInput(IBaseValvesInput):

	def __init__(self) -> None:
		"""Creating a new Instance of this class is not allowed


		Raises:
			Exception: if this class is instanciated
		"""
		raise Exception("Creating a new Instance of this class is not allowed")
		pass

	@overload
	def IPressureValvesInput(self) -> Dict[int,int]:
		"""Establish if the valve should be regulated by pressure or hydraulic grade.

		Returns:
			Dict[int,int]: 
		"""
		pass

	@overload
	def IPressureValvesInput(self, ids: List[int]) -> Dict[int,int]:
		"""No Description

		Args:
			ids(List[int]): ids

		Returns:
			Dict[int,int]: 
		"""
		pass

	@overload
	def IPressureValvesInput(self) -> Dict[int,int]:
		"""Hydraulic Grade Setting (Initial) - Specify the initial hydraulic grade setting for the valve.

		Returns:
			Dict[int,int]: 
		"""
		pass

	@overload
	def IPressureValvesInput(self, ids: List[int]) -> Dict[int,int]:
		"""No Description

		Args:
			ids(List[int]): ids

		Returns:
			Dict[int,int]: 
		"""
		pass

class IPressureValveUnits(IBaseValveUnits):

	def __init__(self) -> None:
		"""Creating a new Instance of this class is not allowed


		Raises:
			Exception: if this class is instanciated
		"""
		raise Exception("Creating a new Instance of this class is not allowed")
		pass

	@property
	def SettingUnit(self) -> IUnit:
		"""No Description

		Returns:
			IPressureValveUnits: 
		"""
		pass

class IPressureBreakingValves(IWaterNetworkElements[IPressureBreakingValves, IPressureBreakingValve, IPressureBreakingValveUnits, IPressureBreakingValveInput, IPressureBreakingValveResults, IPressureBreakingValvesInput, IPressureBreakingValvesResults]):

	def __init__(self) -> None:
		"""Creating a new Instance of this class is not allowed


		Raises:
			Exception: if this class is instanciated
		"""
		raise Exception("Creating a new Instance of this class is not allowed")
		pass

class IPressureBreakingValve(IWaterNetworkElement[IPressureBreakingValves, IPressureBreakingValve, IPressureBreakingValveUnits, IPressureBreakingValveInput, IPressureBreakingValveResults, IPressureBreakingValvesInput, IPressureBreakingValvesResults]):

	def __init__(self) -> None:
		"""Creating a new Instance of this class is not allowed


		Raises:
			Exception: if this class is instanciated
		"""
		raise Exception("Creating a new Instance of this class is not allowed")
		pass

class IPressureBreakingValvesInput(IPressureValvesInput):

	def __init__(self) -> None:
		"""Creating a new Instance of this class is not allowed


		Raises:
			Exception: if this class is instanciated
		"""
		raise Exception("Creating a new Instance of this class is not allowed")
		pass

class IPressureBreakingValvesResults(IPressureValvesResults):

	def __init__(self) -> None:
		"""Creating a new Instance of this class is not allowed


		Raises:
			Exception: if this class is instanciated
		"""
		raise Exception("Creating a new Instance of this class is not allowed")
		pass

class IPressureBreakingValveResults(IPressureValveResults):

	def __init__(self) -> None:
		"""Creating a new Instance of this class is not allowed


		Raises:
			Exception: if this class is instanciated
		"""
		raise Exception("Creating a new Instance of this class is not allowed")
		pass

class IPressureBreakingValveInput(IPressureValveInput):

	def __init__(self) -> None:
		"""Creating a new Instance of this class is not allowed


		Raises:
			Exception: if this class is instanciated
		"""
		raise Exception("Creating a new Instance of this class is not allowed")
		pass

class IPressureBreakingValveUnits(IPressureValveUnits):

	def __init__(self) -> None:
		"""Creating a new Instance of this class is not allowed


		Raises:
			Exception: if this class is instanciated
		"""
		raise Exception("Creating a new Instance of this class is not allowed")
		pass

class IPressureSustainingValves(IWaterNetworkElements[IPressureSustainingValves, IPressureSustainingValve, IPressureSustainingValveUnits, IPressureSustainingValveInput, IPressureSustainingValveResults, IPressureSustainingValvesInput, IPressureSustainingValvesResults]):

	def __init__(self) -> None:
		"""Creating a new Instance of this class is not allowed


		Raises:
			Exception: if this class is instanciated
		"""
		raise Exception("Creating a new Instance of this class is not allowed")
		pass

class IPressureSustainingValve(IWaterNetworkElement[IPressureSustainingValves, IPressureSustainingValve, IPressureSustainingValveUnits, IPressureSustainingValveInput, IPressureSustainingValveResults, IPressureSustainingValvesInput, IPressureSustainingValvesResults]):

	def __init__(self) -> None:
		"""Creating a new Instance of this class is not allowed


		Raises:
			Exception: if this class is instanciated
		"""
		raise Exception("Creating a new Instance of this class is not allowed")
		pass

class IPressureSustainingValvesInput(IPressureValvesInput):

	def __init__(self) -> None:
		"""Creating a new Instance of this class is not allowed


		Raises:
			Exception: if this class is instanciated
		"""
		raise Exception("Creating a new Instance of this class is not allowed")
		pass

	def ValveCharacteristics(self) -> Dict[int,int]:
		"""Specifies the valve characteristics definition to be used for this valve. If the Valve Characteristic Curve is not defined then a default curve will be used. The default curve will have (Relative Closure, Relative Area) points of (0,1) and (1,0).

		Returns:
			Dict[int,int]: 
		"""
		pass

	def ValveTypes(self) -> Dict[int,int]:
		"""Specifies the type of valve. Choices are Butterfly, Needle, Circular Gate, Globe, Ball and User Defined.

		Returns:
			Dict[int,int]: 
		"""
		pass

class IPressureSustainingValvesResults(IPressureValvesResults):

	def __init__(self) -> None:
		"""Creating a new Instance of this class is not allowed


		Raises:
			Exception: if this class is instanciated
		"""
		raise Exception("Creating a new Instance of this class is not allowed")
		pass

class IPressureSustainingValveResults(IPressureValveResults):

	def __init__(self) -> None:
		"""Creating a new Instance of this class is not allowed


		Raises:
			Exception: if this class is instanciated
		"""
		raise Exception("Creating a new Instance of this class is not allowed")
		pass

class IPressureSustainingValveInput(IPressureValveInput):

	def __init__(self) -> None:
		"""Creating a new Instance of this class is not allowed


		Raises:
			Exception: if this class is instanciated
		"""
		raise Exception("Creating a new Instance of this class is not allowed")
		pass

	@property
	def ValveCharacteristics(self) -> IValveCharacteristic:
		"""No Description

		Returns:
			IPressureSustainingValveInput: 
		"""
		pass

	@property
	def ValveType(self) -> HammerValveType:
		"""No Description

		Returns:
			IPressureSustainingValveInput: 
		"""
		pass

	@ValveCharacteristics.setter
	def ValveCharacteristics(self, valvecharacteristics: IValveCharacteristic) -> None:
		pass

	@ValveType.setter
	def ValveType(self, valvetype: HammerValveType) -> None:
		pass

class IPressureSustainingValveUnits(IPressureValveUnits):

	def __init__(self) -> None:
		"""Creating a new Instance of this class is not allowed


		Raises:
			Exception: if this class is instanciated
		"""
		raise Exception("Creating a new Instance of this class is not allowed")
		pass

class IPressureReducingValves(IWaterNetworkElements[IPressureReducingValves, IPressureReducingValve, IPressureReducingValveUnits, IPressureReducingValveInput, IPressureReducingValveResults, IPressureReducingValvesInput, IPressureReducingValvesResults]):

	def __init__(self) -> None:
		"""Creating a new Instance of this class is not allowed


		Raises:
			Exception: if this class is instanciated
		"""
		raise Exception("Creating a new Instance of this class is not allowed")
		pass

class IPressureReducingValve(IWaterNetworkElement[IPressureReducingValves, IPressureReducingValve, IPressureReducingValveUnits, IPressureReducingValveInput, IPressureReducingValveResults, IPressureReducingValvesInput, IPressureReducingValvesResults]):

	def __init__(self) -> None:
		"""Creating a new Instance of this class is not allowed


		Raises:
			Exception: if this class is instanciated
		"""
		raise Exception("Creating a new Instance of this class is not allowed")
		pass

class IPressureReducingValvesInput(IPressureValvesInput):

	def __init__(self) -> None:
		"""Creating a new Instance of this class is not allowed


		Raises:
			Exception: if this class is instanciated
		"""
		raise Exception("Creating a new Instance of this class is not allowed")
		pass

	def ValveCharacteristics(self) -> Dict[int,int]:
		"""Specifies the valve characteristics definition to be used for this valve. If the Valve Characteristic Curve is not defined then a default curve will be used. The default curve will have (Relative Closure, Relative Area) points of (0,1) and (1,0).

		Returns:
			Dict[int,int]: 
		"""
		pass

	def ValveTypes(self) -> Dict[int,int]:
		"""Specifies the type of valve. Choices are Butterfly, Needle, Circular Gate, Globe, Ball and User Defined.

		Returns:
			Dict[int,int]: 
		"""
		pass

class IPressureReducingValvesResults(IPressureValvesResults):

	def __init__(self) -> None:
		"""Creating a new Instance of this class is not allowed


		Raises:
			Exception: if this class is instanciated
		"""
		raise Exception("Creating a new Instance of this class is not allowed")
		pass

class IPressureReducingValveResults(IPressureValveResults):

	def __init__(self) -> None:
		"""Creating a new Instance of this class is not allowed


		Raises:
			Exception: if this class is instanciated
		"""
		raise Exception("Creating a new Instance of this class is not allowed")
		pass

class IPressureReducingValveInput(IPressureValveInput):

	def __init__(self) -> None:
		"""Creating a new Instance of this class is not allowed


		Raises:
			Exception: if this class is instanciated
		"""
		raise Exception("Creating a new Instance of this class is not allowed")
		pass

	@property
	def ValveCharacteristics(self) -> IValveCharacteristic:
		"""No Description

		Returns:
			IPressureReducingValveInput: 
		"""
		pass

	@property
	def ValveType(self) -> HammerValveType:
		"""No Description

		Returns:
			IPressureReducingValveInput: 
		"""
		pass

	@ValveCharacteristics.setter
	def ValveCharacteristics(self, valvecharacteristics: IValveCharacteristic) -> None:
		pass

	@ValveType.setter
	def ValveType(self, valvetype: HammerValveType) -> None:
		pass

class IPressureReducingValveUnits(IPressureValveUnits):

	def __init__(self) -> None:
		"""Creating a new Instance of this class is not allowed


		Raises:
			Exception: if this class is instanciated
		"""
		raise Exception("Creating a new Instance of this class is not allowed")
		pass

class IValveLinearAreaChangeResults(IBaseValveResults):

	def __init__(self) -> None:
		"""Creating a new Instance of this class is not allowed


		Raises:
			Exception: if this class is instanciated
		"""
		raise Exception("Creating a new Instance of this class is not allowed")
		pass

class IValvesLinearAreaChangeResults(IBaseValvesResults):

	def __init__(self) -> None:
		"""Creating a new Instance of this class is not allowed


		Raises:
			Exception: if this class is instanciated
		"""
		raise Exception("Creating a new Instance of this class is not allowed")
		pass

class IValveLinearAreaChangeInput(IBaseValveInput):

	def __init__(self) -> None:
		"""Creating a new Instance of this class is not allowed


		Raises:
			Exception: if this class is instanciated
		"""
		raise Exception("Creating a new Instance of this class is not allowed")
		pass

	@property
	def TimeToClose(self) -> float:
		"""No Description

		Returns:
			IValveLinearAreaChangeInput: 
		"""
		pass

	@property
	def DischargeCoefficient(self) -> float:
		"""No Description

		Returns:
			IValveLinearAreaChangeInput: 
		"""
		pass

	@TimeToClose.setter
	def TimeToClose(self, timetoclose: float) -> None:
		pass

	@DischargeCoefficient.setter
	def DischargeCoefficient(self, dischargecoefficient: float) -> None:
		pass

class IValvesLinearAreaChangeInput(IBaseValvesInput):

	def __init__(self) -> None:
		"""Creating a new Instance of this class is not allowed


		Raises:
			Exception: if this class is instanciated
		"""
		raise Exception("Creating a new Instance of this class is not allowed")
		pass

	@overload
	def IValvesLinearAreaChangeInput(self) -> Dict[int,int]:
		"""For a slow-closing air valve, the valve starts to close linearly with respect to area once air begins to exit the pipe. If air subsequently re-enters, then the air valve opens fully again. For a valve with linear area change, the valve will close linearly over this time, starting at the beginning of the simulation if this value is greater than zero. If this value equals zero a valve with linear area change will close when reverse flow is first sensed and will remain closed for the remainder of the simulation. For an air valve, adiabatic compression (i.e., gas law exponent = 1.4) is assumed.

		Returns:
			Dict[int,int]: 
		"""
		pass

	@overload
	def IValvesLinearAreaChangeInput(self, ids: List[int]) -> Dict[int,int]:
		"""No Description

		Args:
			ids(List[int]): ids

		Returns:
			Dict[int,int]: 
		"""
		pass

	@overload
	def IValvesLinearAreaChangeInput(self) -> Dict[int,int]:
		"""The discharge coefficient for the valve. This is used to determine the flow/headloss relationship of the valve for the steady state / EPS analysis. Minor losses are never applied for this valve type and as such the valve does not support a (fully) open status.

		Returns:
			Dict[int,int]: 
		"""
		pass

	@overload
	def IValvesLinearAreaChangeInput(self, ids: List[int]) -> Dict[int,int]:
		"""No Description

		Args:
			ids(List[int]): ids

		Returns:
			Dict[int,int]: 
		"""
		pass

class IValveWithLinearAreaChange(IWaterNetworkElement[IValvesWithLinearAreaChange, IValveWithLinearAreaChange, IValveWithLinearAreaChangeUnits, IValveLinearAreaChangeInput, IValveLinearAreaChangeResults, IValvesLinearAreaChangeInput, IValvesLinearAreaChangeResults]):

	def __init__(self) -> None:
		"""Creating a new Instance of this class is not allowed


		Raises:
			Exception: if this class is instanciated
		"""
		raise Exception("Creating a new Instance of this class is not allowed")
		pass

class IValvesWithLinearAreaChange(IWaterNetworkElements[IValvesWithLinearAreaChange, IValveWithLinearAreaChange, IValveWithLinearAreaChangeUnits, IValveLinearAreaChangeInput, IValveLinearAreaChangeResults, IValvesLinearAreaChangeInput, IValvesLinearAreaChangeResults]):

	def __init__(self) -> None:
		"""Creating a new Instance of this class is not allowed


		Raises:
			Exception: if this class is instanciated
		"""
		raise Exception("Creating a new Instance of this class is not allowed")
		pass

class IValveWithLinearAreaChangeUnits(IBaseValveUnits):

	def __init__(self) -> None:
		"""Creating a new Instance of this class is not allowed


		Raises:
			Exception: if this class is instanciated
		"""
		raise Exception("Creating a new Instance of this class is not allowed")
		pass

	@property
	def DischargeCoefficientUnit(self) -> IUnit:
		"""No Description

		Returns:
			IValveWithLinearAreaChangeUnits: 
		"""
		pass

	@property
	def TimeToCloseUnit(self) -> IUnit:
		"""No Description

		Returns:
			IValveWithLinearAreaChangeUnits: 
		"""
		pass

class IWaterElement(IElement):

	def __init__(self) -> None:
		"""Creating a new Instance of this class is not allowed


		Raises:
			Exception: if this class is instanciated
		"""
		raise Exception("Creating a new Instance of this class is not allowed")
		pass

	@property
	def WaterElementType(self) -> WaterNetworkElementType:
		"""No Description

		Returns:
			IWaterElement: 
		"""
		pass

class IWaterNetworkElements(Generic[TElementManagerType, TElementType, TUnitsType, TElementInputType, TElementResultsType, TElementsInputType, TElementsResultsType], INetworkElements[TElementManagerType, TElementType, TUnitsType, WaterNetworkElementType, TElementInputType, TElementResultsType, TElementsInputType, TElementsResultsType]):

	def __init__(self) -> None:
		"""Creating a new Instance of this class is not allowed


		Raises:
			Exception: if this class is instanciated
		"""
		raise Exception("Creating a new Instance of this class is not allowed")
		pass

class IWaterNetworkElement(Generic[TElementManagerType, TElementType, TUnitsType, TElementInputType, TElementResultsType, TElementsInputType, TElementsResultsType], INetworkElement[TElementManagerType, TElementType, TUnitsType, WaterNetworkElementType, TElementInputType, TElementResultsType, TElementsInputType, TElementsResultsType], IWaterElement):

	def __init__(self) -> None:
		"""Creating a new Instance of this class is not allowed


		Raises:
			Exception: if this class is instanciated
		"""
		raise Exception("Creating a new Instance of this class is not allowed")
		pass

class IWaterZoneableNetworkElementInput(IActiveElementInput):

	def __init__(self) -> None:
		"""Creating a new Instance of this class is not allowed


		Raises:
			Exception: if this class is instanciated
		"""
		raise Exception("Creating a new Instance of this class is not allowed")
		pass

	@property
	def Zone(self) -> IZone:
		"""No Description

		Returns:
			IWaterZoneableNetworkElementInput: 
		"""
		pass

	@Zone.setter
	def Zone(self, zone: IZone) -> None:
		pass

class IWaterZoneableNetworkElementsInput(IActiveElementsInput):

	def __init__(self) -> None:
		"""Creating a new Instance of this class is not allowed


		Raises:
			Exception: if this class is instanciated
		"""
		raise Exception("Creating a new Instance of this class is not allowed")
		pass

	@overload
	def IWaterZoneableNetworkElementsInput(self) -> Dict[int,int]:
		"""Gets assigned zones across all elements of this type.

		Returns:
			Dict[int,int]: 
		"""
		pass

	@overload
	def IWaterZoneableNetworkElementsInput(self, ids: List[int]) -> Dict[int,int]:
		"""No Description

		Args:
			ids(List[int]): ids

		Returns:
			Dict[int,int]: 
		"""
		pass

class IWaterTraceableInput:

	def __init__(self) -> None:
		"""Creating a new Instance of this class is not allowed


		Raises:
			Exception: if this class is instanciated
		"""
		raise Exception("Creating a new Instance of this class is not allowed")
		pass

	def MakeActiveTraceElement(self) -> None:
		"""Makes the current element the trace element in the active scenario's trace alternative.

		Returns:
			None: 
		"""
		pass

class IWaterQualityResults:

	def __init__(self) -> None:
		"""Creating a new Instance of this class is not allowed


		Raises:
			Exception: if this class is instanciated
		"""
		raise Exception("Creating a new Instance of this class is not allowed")
		pass

	@overload
	def IWaterQualityResults(self) -> Union[float, None]:
		"""Age at selected element for current time step.

		Returns:
			Nullable: 
		"""
		pass

	@overload
	def IWaterQualityResults(self, timeStepIndex: int) -> Union[float, None]:
		"""Age at selected element for the time step.

		Args:
			timeStepIndex(int): The time step index to use to retrieve the result.

		Returns:
			Nullable: 
		"""
		pass

	@overload
	def IWaterQualityResults(self) -> Union[float, None]:
		"""Trace at selected element for current time step.

		Returns:
			Nullable: 
		"""
		pass

	@overload
	def IWaterQualityResults(self, timeStepIndex: int) -> Union[float, None]:
		"""Trace at selected element for the time step.

		Args:
			timeStepIndex(int): The time step index to use to retrieve the result.

		Returns:
			Nullable: 
		"""
		pass

	@overload
	def IWaterQualityResults(self) -> Union[float, None]:
		"""Concentration at selected element for current time step.

		Returns:
			Nullable: 
		"""
		pass

	@overload
	def IWaterQualityResults(self, timeStepIndex: int) -> Union[float, None]:
		"""Concentration at selected element for the time step.

		Args:
			timeStepIndex(int): The time step index to use to retrieve the result.

		Returns:
			Nullable: 
		"""
		pass

	def Ages(self) -> array(Union[float, None]):
		"""Age across all time steps for element.

		Returns:
			array(): 
		"""
		pass

	def Traces(self) -> array(Union[float, None]):
		"""Trace across all time steps for element.

		Returns:
			array(): 
		"""
		pass

	def Concentrations(self) -> array(Union[float, None]):
		"""Concentration across all time steps for element.

		Returns:
			array(): 
		"""
		pass

class IWaterQualityElementsInput:

	def __init__(self) -> None:
		"""Creating a new Instance of this class is not allowed


		Raises:
			Exception: if this class is instanciated
		"""
		raise Exception("Creating a new Instance of this class is not allowed")
		pass

	@overload
	def IWaterQualityElementsInput(self) -> Dict[int,int]:
		"""Gets the initial age for all elements of this type.

		Returns:
			Dict[int,int]: 
		"""
		pass

	@overload
	def IWaterQualityElementsInput(self, ids: List[int]) -> Dict[int,int]:
		"""No Description

		Args:
			ids(List[int]): ids

		Returns:
			Dict[int,int]: 
		"""
		pass

	@overload
	def IWaterQualityElementsInput(self) -> Dict[int,int]:
		"""Gets the initial trace for all elements of this type.

		Returns:
			Dict[int,int]: 
		"""
		pass

	@overload
	def IWaterQualityElementsInput(self, ids: List[int]) -> Dict[int,int]:
		"""No Description

		Args:
			ids(List[int]): ids

		Returns:
			Dict[int,int]: 
		"""
		pass

	@overload
	def IWaterQualityElementsInput(self) -> Dict[int,int]:
		"""Gets the initial concentration for all elements of this type.

		Returns:
			Dict[int,int]: 
		"""
		pass

	@overload
	def IWaterQualityElementsInput(self, ids: List[int]) -> Dict[int,int]:
		"""No Description

		Args:
			ids(List[int]): ids

		Returns:
			Dict[int,int]: 
		"""
		pass

class IWaterQualityElementInput:

	def __init__(self) -> None:
		"""Creating a new Instance of this class is not allowed


		Raises:
			Exception: if this class is instanciated
		"""
		raise Exception("Creating a new Instance of this class is not allowed")
		pass

	@property
	def InitialAge(self) -> float:
		"""No Description

		Returns:
			IWaterQualityElementInput: 
		"""
		pass

	@property
	def InitialConcentration(self) -> float:
		"""No Description

		Returns:
			IWaterQualityElementInput: 
		"""
		pass

	@property
	def InitialTrace(self) -> float:
		"""No Description

		Returns:
			IWaterQualityElementInput: 
		"""
		pass

	@InitialAge.setter
	def InitialAge(self, initialage: float) -> None:
		pass

	@InitialConcentration.setter
	def InitialConcentration(self, initialconcentration: float) -> None:
		pass

	@InitialTrace.setter
	def InitialTrace(self, initialtrace: float) -> None:
		pass

class IWaterQualityNodeInput:

	def __init__(self) -> None:
		"""Creating a new Instance of this class is not allowed


		Raises:
			Exception: if this class is instanciated
		"""
		raise Exception("Creating a new Instance of this class is not allowed")
		pass

	@property
	def IsConstituentSource(self) -> bool:
		"""No Description

		Returns:
			IWaterQualityNodeInput: 
		"""
		pass

	@property
	def ConstituentSourceType(self) -> ConstituentSourceType:
		"""No Description

		Returns:
			IWaterQualityNodeInput: 
		"""
		pass

	@property
	def BaseConstituent(self) -> float:
		"""No Description

		Returns:
			IWaterQualityNodeInput: 
		"""
		pass

	@IsConstituentSource.setter
	def IsConstituentSource(self, isconstituentsource: bool) -> None:
		pass

	@ConstituentSourceType.setter
	def ConstituentSourceType(self, constituentsourcetype: ConstituentSourceType) -> None:
		pass

	@BaseConstituent.setter
	def BaseConstituent(self, baseconstituent: float) -> None:
		pass

class IWaterQualityNodesInput:

	def __init__(self) -> None:
		"""Creating a new Instance of this class is not allowed


		Raises:
			Exception: if this class is instanciated
		"""
		raise Exception("Creating a new Instance of this class is not allowed")
		pass

class IWaterQualityElementsResults:

	def __init__(self) -> None:
		"""Creating a new Instance of this class is not allowed


		Raises:
			Exception: if this class is instanciated
		"""
		raise Exception("Creating a new Instance of this class is not allowed")
		pass

	@overload
	def IWaterQualityElementsResults(self) -> Dict[int,int]:
		"""Gets the calculated age results across all elements at the current time step.

		Returns:
			Dict[int,int]: 
		"""
		pass

	@overload
	def IWaterQualityElementsResults(self, timeStepIndex: int) -> Dict[int,int]:
		"""Gets the calculated age results across all elements at the given time step.

		Args:
			timeStepIndex(int): timeStepIndex

		Returns:
			Dict[int,int]: 
		"""
		pass

	@overload
	def IWaterQualityElementsResults(self, ids: List[int], timeStepIndex: int) -> Dict[int,int]:
		"""No Description

		Args:
			ids(List[int]): ids
			timeStepIndex(int): timeStepIndex

		Returns:
			Dict[int,int]: 
		"""
		pass

	@overload
	def IWaterQualityElementsResults(self) -> Dict[int,int]:
		"""Gets the calculated tract results across all elements at the current time step.

		Returns:
			Dict[int,int]: 
		"""
		pass

	@overload
	def IWaterQualityElementsResults(self, timeStepIndex: int) -> Dict[int,int]:
		"""Gets the calculated tract results across all elements at the given time step.

		Args:
			timeStepIndex(int): timeStepIndex

		Returns:
			Dict[int,int]: 
		"""
		pass

	@overload
	def IWaterQualityElementsResults(self, ids: List[int], timeStepIndex: int) -> Dict[int,int]:
		"""No Description

		Args:
			ids(List[int]): ids
			timeStepIndex(int): timeStepIndex

		Returns:
			Dict[int,int]: 
		"""
		pass

	@overload
	def IWaterQualityElementsResults(self) -> Dict[int,int]:
		"""Gets the calculated concentration results across all elements at the current time step.

		Returns:
			Dict[int,int]: 
		"""
		pass

	@overload
	def IWaterQualityElementsResults(self, timeStepIndex: int) -> Dict[int,int]:
		"""Gets the calculated concentration results across all elements at the given time step.

		Args:
			timeStepIndex(int): timeStepIndex

		Returns:
			Dict[int,int]: 
		"""
		pass

	@overload
	def IWaterQualityElementsResults(self, ids: List[int], timeStepIndex: int) -> Dict[int,int]:
		"""No Description

		Args:
			ids(List[int]): ids
			timeStepIndex(int): timeStepIndex

		Returns:
			Dict[int,int]: 
		"""
		pass

class IWaterQualityResultsUnits(IElementUnits):

	def __init__(self) -> None:
		"""Creating a new Instance of this class is not allowed


		Raises:
			Exception: if this class is instanciated
		"""
		raise Exception("Creating a new Instance of this class is not allowed")
		pass

	@property
	def AgeUnit(self) -> IUnit:
		"""No Description

		Returns:
			IWaterQualityResultsUnits: 
		"""
		pass

	@property
	def TraceUnit(self) -> IUnit:
		"""No Description

		Returns:
			IWaterQualityResultsUnits: 
		"""
		pass

	@property
	def ConcentrationUnit(self) -> IUnit:
		"""No Description

		Returns:
			IWaterQualityResultsUnits: 
		"""
		pass

class IWaterNetwork(INetwork[IWaterElement, WaterNetworkElementType]):

	def __init__(self) -> None:
		"""Creating a new Instance of this class is not allowed


		Raises:
			Exception: if this class is instanciated
		"""
		raise Exception("Creating a new Instance of this class is not allowed")
		pass

	@property
	def Pipes(self) -> IPipes:
		"""No Description

		Returns:
			IWaterNetwork: 
		"""
		pass

	@property
	def Laterals(self) -> ILaterals:
		"""No Description

		Returns:
			IWaterNetwork: 
		"""
		pass

	@property
	def Junctions(self) -> IJunctions:
		"""No Description

		Returns:
			IWaterNetwork: 
		"""
		pass

	@property
	def Hydrants(self) -> IHydrants:
		"""No Description

		Returns:
			IWaterNetwork: 
		"""
		pass

	@property
	def Tanks(self) -> ITanks:
		"""No Description

		Returns:
			IWaterNetwork: 
		"""
		pass

	@property
	def Reservoirs(self) -> IReservoirs:
		"""No Description

		Returns:
			IWaterNetwork: 
		"""
		pass

	@property
	def Taps(self) -> ITaps:
		"""No Description

		Returns:
			IWaterNetwork: 
		"""
		pass

	@property
	def CustomerMeters(self) -> ICustomerMeters:
		"""No Description

		Returns:
			IWaterNetwork: 
		"""
		pass

	@property
	def Pumps(self) -> IPumps:
		"""No Description

		Returns:
			IWaterNetwork: 
		"""
		pass

	@property
	def VSPBs(self) -> IVariableSpeedPumpBatterys:
		"""No Description

		Returns:
			IWaterNetwork: 
		"""
		pass

	@property
	def PumpStations(self) -> IPumpStations:
		"""No Description

		Returns:
			IWaterNetwork: 
		"""
		pass

	@property
	def SCADAElements(self) -> ISCADAElements:
		"""No Description

		Returns:
			IWaterNetwork: 
		"""
		pass

	@property
	def PRVs(self) -> IPressureReducingValves:
		"""No Description

		Returns:
			IWaterNetwork: 
		"""
		pass

	@property
	def PBVs(self) -> IPressureBreakingValves:
		"""No Description

		Returns:
			IWaterNetwork: 
		"""
		pass

	@property
	def PSVs(self) -> IPressureSustainingValves:
		"""No Description

		Returns:
			IWaterNetwork: 
		"""
		pass

	@property
	def TCVs(self) -> IThrottleControlValves:
		"""No Description

		Returns:
			IWaterNetwork: 
		"""
		pass

	@property
	def FCVs(self) -> IFlowControlValves:
		"""No Description

		Returns:
			IWaterNetwork: 
		"""
		pass

	@property
	def GPVs(self) -> IGeneralPurposeValves:
		"""No Description

		Returns:
			IWaterNetwork: 
		"""
		pass

	@property
	def IsolationValves(self) -> IIsolationValves:
		"""No Description

		Returns:
			IWaterNetwork: 
		"""
		pass

	@property
	def CheckValves(self) -> ICheckValves:
		"""No Description

		Returns:
			IWaterNetwork: 
		"""
		pass

	@property
	def SpotElevations(self) -> ISpotElevations:
		"""No Description

		Returns:
			IWaterNetwork: 
		"""
		pass

	@property
	def ValvesWithLinearAreaChange(self) -> IValvesWithLinearAreaChange:
		"""No Description

		Returns:
			IWaterNetwork: 
		"""
		pass

	@property
	def PeriodicHeadFlows(self) -> IPeriodicHeadFlows:
		"""No Description

		Returns:
			IWaterNetwork: 
		"""
		pass

	@property
	def AirValves(self) -> IAirValves:
		"""No Description

		Returns:
			IWaterNetwork: 
		"""
		pass

	@property
	def OrificesBetweenTwoPipes(self) -> IOrificesBetweenTwoPipes:
		"""No Description

		Returns:
			IWaterNetwork: 
		"""
		pass

	@property
	def SurgeValves(self) -> ISurgeValves:
		"""No Description

		Returns:
			IWaterNetwork: 
		"""
		pass

	@property
	def DischargeToAtmospheres(self) -> IDischargeToAtmospheres:
		"""No Description

		Returns:
			IWaterNetwork: 
		"""
		pass

	@property
	def RuptureDisks(self) -> IRuptureDisks:
		"""No Description

		Returns:
			IWaterNetwork: 
		"""
		pass

	@property
	def Turbines(self) -> ITurbines:
		"""No Description

		Returns:
			IWaterNetwork: 
		"""
		pass

	@property
	def SurgeTanks(self) -> ISurgeTanks:
		"""No Description

		Returns:
			IWaterNetwork: 
		"""
		pass

	@property
	def HydropneumaticTanks(self) -> IHydropneumaticTanks:
		"""No Description

		Returns:
			IWaterNetwork: 
		"""
		pass

class IPipes(IWaterNetworkElements[IPipes, IPipe, IPipeUnits, IPipeInput, IPipeResults, IPipesInput, IPipesResults]):

	def __init__(self) -> None:
		"""Creating a new Instance of this class is not allowed


		Raises:
			Exception: if this class is instanciated
		"""
		raise Exception("Creating a new Instance of this class is not allowed")
		pass

class IPipe(IWaterNetworkElement[IPipes, IPipe, IPipeUnits, IPipeInput, IPipeResults, IPipesInput, IPipesResults]):

	def __init__(self) -> None:
		"""Creating a new Instance of this class is not allowed


		Raises:
			Exception: if this class is instanciated
		"""
		raise Exception("Creating a new Instance of this class is not allowed")
		pass

class IHammerPipesResults:

	def __init__(self) -> None:
		"""Creating a new Instance of this class is not allowed


		Raises:
			Exception: if this class is instanciated
		"""
		raise Exception("Creating a new Instance of this class is not allowed")
		pass

	@overload
	def IHammerPipesResults(self) -> Dict[int,int]:
		"""Maximum head at any point along the pipe over the course of the transient simulation.

		Returns:
			Dict[int,int]: 
		"""
		pass

	@overload
	def IHammerPipesResults(self, ids: List[int]) -> Dict[int,int]:
		"""No Description

		Args:
			ids(List[int]): ids

		Returns:
			Dict[int,int]: 
		"""
		pass

class IPipesResults(IBaseLinksResults, IWaterQualityElementsResults, IHammerPipesResults):

	def __init__(self) -> None:
		"""Creating a new Instance of this class is not allowed


		Raises:
			Exception: if this class is instanciated
		"""
		raise Exception("Creating a new Instance of this class is not allowed")
		pass

	@overload
	def IPipesResults(self) -> Dict[int,int]:
		"""Gets flows for all pipes for the current time step.

		Returns:
			Dict[int,int]: 
		"""
		pass

	@overload
	def IPipesResults(self, timeStepIndex: int) -> Dict[int,int]:
		"""Gets flows for all pipes at the given time step.

		Args:
			timeStepIndex(int): timeStepIndex

		Returns:
			Dict[int,int]: 
		"""
		pass

	@overload
	def IPipesResults(self, ids: List[int], timeStepIndex: int) -> Dict[int,int]:
		"""No Description

		Args:
			ids(List[int]): ids
			timeStepIndex(int): timeStepIndex

		Returns:
			Dict[int,int]: 
		"""
		pass

	@overload
	def IPipesResults(self) -> Dict[int,int]:
		"""Gets the velocities for all pipes at the current time step.

		Returns:
			Dict[int,int]: 
		"""
		pass

	@overload
	def IPipesResults(self, timeStepIndex: int) -> Dict[int,int]:
		"""Gets the velocities for all pipes at the given time step.

		Args:
			timeStepIndex(int): timeStepIndex

		Returns:
			Dict[int,int]: 
		"""
		pass

	@overload
	def IPipesResults(self, ids: List[int], timeStepIndex: int) -> Dict[int,int]:
		"""No Description

		Args:
			ids(List[int]): ids
			timeStepIndex(int): timeStepIndex

		Returns:
			Dict[int,int]: 
		"""
		pass

	@overload
	def IPipesResults(self) -> Dict[int,int]:
		"""Gets the headlosses for all pipes at the current time step.

		Returns:
			Dict[int,int]: 
		"""
		pass

	@overload
	def IPipesResults(self, timeStepIndex: int) -> Dict[int,int]:
		"""Gets the headlosses for all pipes at the given time step.

		Args:
			timeStepIndex(int): timeStepIndex

		Returns:
			Dict[int,int]: 
		"""
		pass

	@overload
	def IPipesResults(self, ids: List[int], timeStepIndex: int) -> Dict[int,int]:
		"""No Description

		Args:
			ids(List[int]): ids
			timeStepIndex(int): timeStepIndex

		Returns:
			Dict[int,int]: 
		"""
		pass

	@overload
	def IPipesResults(self) -> Dict[int,int]:
		"""Gets the headloss gradients for all pipes at the current time step.

		Returns:
			Dict[int,int]: 
		"""
		pass

	@overload
	def IPipesResults(self, timeStepIndex: int) -> Dict[int,int]:
		"""Gets the headloss gradients for all pipes at the given time step.

		Args:
			timeStepIndex(int): timeStepIndex

		Returns:
			Dict[int,int]: 
		"""
		pass

	@overload
	def IPipesResults(self, ids: List[int], timeStepIndex: int) -> Dict[int,int]:
		"""No Description

		Args:
			ids(List[int]): ids
			timeStepIndex(int): timeStepIndex

		Returns:
			Dict[int,int]: 
		"""
		pass

	@overload
	def IPipesResults(self) -> Dict[int,int]:
		"""Gets the status for all pipes at the current time step.

		Returns:
			Dict[int,int]: 
		"""
		pass

	@overload
	def IPipesResults(self, timeStepIndex: int) -> Dict[int,int]:
		"""Gets the status for all pipes at the given time step.

		Args:
			timeStepIndex(int): timeStepIndex

		Returns:
			Dict[int,int]: 
		"""
		pass

	@overload
	def IPipesResults(self, ids: List[int], timeStepIndex: int) -> Dict[int,int]:
		"""No Description

		Args:
			ids(List[int]): ids
			timeStepIndex(int): timeStepIndex

		Returns:
			Dict[int,int]: 
		"""
		pass

class IHammerPipeResults:

	def __init__(self) -> None:
		"""Creating a new Instance of this class is not allowed


		Raises:
			Exception: if this class is instanciated
		"""
		raise Exception("Creating a new Instance of this class is not allowed")
		pass

	def MaximumHead(self) -> Union[float, None]:
		"""Maximum head at any point along the pipe over the course of the transient simulation.

		Returns:
			Nullable: 
		"""
		pass

class IPipeResults(IBaseLinkResults, IWaterQualityResults, IHammerPipeResults):

	def __init__(self) -> None:
		"""Creating a new Instance of this class is not allowed


		Raises:
			Exception: if this class is instanciated
		"""
		raise Exception("Creating a new Instance of this class is not allowed")
		pass

	@overload
	def IPipeResults(self) -> Union[float, None]:
		"""Total flow through the pipe.  If the value is negative the flow is traveling from the stop node to the start node, and vice versa if positive at current time step.

		Returns:
			Nullable: 
		"""
		pass

	@overload
	def IPipeResults(self, timeStepIndex: int) -> Union[float, None]:
		"""Total flow through the pipe.  If the value is negative the flow is traveling from the stop node to the start node, and vice versa if positive at given time step.

		Args:
			timeStepIndex(int): The time step index to use to retrieve the result.

		Returns:
			Nullable: 
		"""
		pass

	@overload
	def IPipeResults(self) -> Union[float, None]:
		"""Velocity of fluid through the pipe at current time step.

		Returns:
			Nullable: 
		"""
		pass

	@overload
	def IPipeResults(self, timeStepIndex: int) -> Union[float, None]:
		"""Velocity of fluid through the pipe at given time step.

		Args:
			timeStepIndex(int): The time step index to use to retrieve the result.

		Returns:
			Nullable: 
		"""
		pass

	@overload
	def IPipeResults(self) -> Union[float, None]:
		"""Total headloss occurring in the pipe, including both friction and minor headlosses and any minor losses from isolation valves at current time step.

		Returns:
			Nullable: 
		"""
		pass

	@overload
	def IPipeResults(self, timeStepIndex: int) -> Union[float, None]:
		"""Total headloss occurring in the pipe, including both friction and minor headlosses and any minor losses from isolation valves at given time step.

		Args:
			timeStepIndex(int): timeStepIndex

		Returns:
			Nullable: 
		"""
		pass

	@overload
	def IPipeResults(self) -> Union[float, None]:
		"""The headloss per unit length in the pipe at current time step.

		Returns:
			Nullable: 
		"""
		pass

	@overload
	def IPipeResults(self, timeStepIndex: int) -> Union[float, None]:
		"""The headloss per unit length in the pipe at given time step.

		Args:
			timeStepIndex(int): timeStepIndex

		Returns:
			Nullable: 
		"""
		pass

	@overload
	def IPipeResults(self) -> Union[int, None]:
		"""Whether or not the pipe is open or closed during current time step at current time step.

		Returns:
			Nullable: The status of the pipe.  Null if no results available.
		"""
		pass

	@overload
	def IPipeResults(self, timeStepIndex: int) -> Union[int, None]:
		"""Whether or not the pipe is open or closed during current time step at given time step.

		Args:
			timeStepIndex(int): timeStepIndex

		Returns:
			Nullable: 
		"""
		pass

	def Flows(self) -> array(Union[float, None]):
		"""Total flow through the pipe.  If the value is negative the flow is traveling from the stop node to the start node, and vice versa if positive across all time steps.

		Returns:
			array(): 
		"""
		pass

	def Velocities(self) -> array(Union[float, None]):
		"""Velocity of fluid through the pipe across all time steps.

		Returns:
			array(): 
		"""
		pass

	def Headlosses(self) -> array(Union[float, None]):
		"""Total headloss occurring in the pipe, including both friction and minor headlosses and any minor losses from isolation valves across all time steps.

		Returns:
			array(): A non-null double array in display units.  An empty array if no results available.
		"""
		pass

	def HeadlossGradients(self) -> array(Union[float, None]):
		"""The headloss per unit length in the pipe across all time steps.

		Returns:
			array(): A non-null double array in display units. An empty array if no results available.
		"""
		pass

	def CalculatedStatuses(self) -> array(Union[int, None]):
		"""Whether or not the pipe is open or closed during current time step across all time steps.

		Returns:
			array(): 
		"""
		pass

class IPipeInput(IBaseLinkInput, IWaterZoneableNetworkElementInput):

	def __init__(self) -> None:
		"""Creating a new Instance of this class is not allowed


		Raises:
			Exception: if this class is instanciated
		"""
		raise Exception("Creating a new Instance of this class is not allowed")
		pass

	@property
	def InstallationYear(self) -> int:
		"""No Description

		Returns:
			IPipeInput: 
		"""
		pass

	@property
	def InitialStatus(self) -> PipeStatusType:
		"""No Description

		Returns:
			IPipeInput: 
		"""
		pass

	@property
	def Diameter(self) -> float:
		"""No Description

		Returns:
			IPipeInput: 
		"""
		pass

	@property
	def Material(self) -> str:
		"""No Description

		Returns:
			IPipeInput: 
		"""
		pass

	@property
	def FrictionCoefficient(self) -> float:
		"""No Description

		Returns:
			IPipeInput: 
		"""
		pass

	@property
	def MinorLossCoefficientCollection(self) -> IMinorLossCoefficientCollection:
		"""No Description

		Returns:
			IPipeInput: 
		"""
		pass

	@property
	def LocalMinorLossCoefficient(self) -> float:
		"""No Description

		Returns:
			IPipeInput: 
		"""
		pass

	@property
	def SpecifyLocalMinorLoss(self) -> bool:
		"""No Description

		Returns:
			IPipeInput: 
		"""
		pass

	@property
	def DerivedMinorLossCoefficient(self) -> float:
		"""No Description

		Returns:
			IPipeInput: 
		"""
		pass

	@InstallationYear.setter
	def InstallationYear(self, installationyear: int) -> None:
		pass

	@InitialStatus.setter
	def InitialStatus(self, initialstatus: PipeStatusType) -> None:
		pass

	@Diameter.setter
	def Diameter(self, diameter: float) -> None:
		pass

	@Material.setter
	def Material(self, material: str) -> None:
		pass

	@FrictionCoefficient.setter
	def FrictionCoefficient(self, frictioncoefficient: float) -> None:
		pass

	@LocalMinorLossCoefficient.setter
	def LocalMinorLossCoefficient(self, localminorlosscoefficient: float) -> None:
		pass

	@SpecifyLocalMinorLoss.setter
	def SpecifyLocalMinorLoss(self, specifylocalminorloss: bool) -> None:
		pass

class IPipesInput(IBaseLinksInput, IWaterZoneableNetworkElementsInput):

	def __init__(self) -> None:
		"""Creating a new Instance of this class is not allowed


		Raises:
			Exception: if this class is instanciated
		"""
		raise Exception("Creating a new Instance of this class is not allowed")
		pass

	@overload
	def IPipesInput(self) -> Dict[int,int]:
		"""Specify the install year of the element.  It does not affect the calculations.

		Returns:
			Dict[int,int]: 
		"""
		pass

	@overload
	def IPipesInput(self, ids: List[int]) -> Dict[int,int]:
		"""No Description

		Args:
			ids(List[int]): ids

		Returns:
			Dict[int,int]: 
		"""
		pass

	@overload
	def IPipesInput(self) -> Dict[int,int]:
		"""Specify if the pipe is initially open or closed.

		Returns:
			Dict[int,int]: 
		"""
		pass

	@overload
	def IPipesInput(self, ids: List[int]) -> Dict[int,int]:
		"""No Description

		Args:
			ids(List[int]): ids

		Returns:
			Dict[int,int]: 
		"""
		pass

	@overload
	def IPipesInput(self) -> Dict[int,int]:
		"""Value represents the internal diameter of a circular pipe or four times the hydraulic radius for non-circular cross-sections.

		Returns:
			Dict[int,int]: 
		"""
		pass

	@overload
	def IPipesInput(self, ids: List[int]) -> Dict[int,int]:
		"""No Description

		Args:
			ids(List[int]): ids

		Returns:
			Dict[int,int]: 
		"""
		pass

	@overload
	def IPipesInput(self) -> Dict[int,int]:
		"""The pipe's material type.

		Returns:
			Dict[int,int]: 
		"""
		pass

	@overload
	def IPipesInput(self, ids: List[int]) -> Dict[int,int]:
		"""No Description

		Args:
			ids(List[int]): ids

		Returns:
			Dict[int,int]: 
		"""
		pass

	@overload
	def IPipesInput(self) -> Dict[int,int]:
		"""Manning's - Roughness coefficient used in Manning's formula.

		Returns:
			Dict[int,int]: 
		"""
		pass

	@overload
	def IPipesInput(self, ids: List[int]) -> Dict[int,int]:
		"""No Description

		Args:
			ids(List[int]): ids

		Returns:
			Dict[int,int]: 
		"""
		pass

	def LocalMinorLossCoefficient(self) -> Dict[int,int]:
		"""User input minor loss coefficent.  You can either type in the value directly or select the value from the Minor Loss Library. The minor loss is applied to the valve when it is fully open (inactive). Note that minor losses do not apply to the following valve types: General Purpose Valve and Valve With Linear Area Change. These two valve types do not support a (fully) open status and always apply the head/flow relationship defined by their headloss curve and discharge coefficient respectively.

		Returns:
			Dict[int,int]: 
		"""
		pass

	def SpecifyLocalMinorLoss(self) -> Dict[int,int]:
		"""If true then the minor coefficent for the element is manually set, otherwise the value is derived from the minor loss library.

		Returns:
			Dict[int,int]: 
		"""
		pass

	def DerivedMinorLossCoefficient(self) -> Dict[int,int]:
		"""Displays the composite value calculated from the data in the minor loss collection. The composite minor loss is applied to the valve when it is fully open (inactive). Note that minor losses do not apply to the following valve types: General Purpose Valve and Valve With Linear Area Change. These two valve types do not support a (fully) open status and always apply the head/flow relationship defined by their headloss curve and discharge coefficient respectively.

		Returns:
			Dict[int,int]: 
		"""
		pass

class IPipeUnits(IBaseLinkUnits, IWaterQualityResultsUnits):

	def __init__(self) -> None:
		"""Creating a new Instance of this class is not allowed


		Raises:
			Exception: if this class is instanciated
		"""
		raise Exception("Creating a new Instance of this class is not allowed")
		pass

	@property
	def DiameterUnit(self) -> IUnit:
		"""No Description

		Returns:
			IPipeUnits: 
		"""
		pass

	@property
	def FlowUnit(self) -> IUnit:
		"""No Description

		Returns:
			IPipeUnits: 
		"""
		pass

	@property
	def VelocityUnit(self) -> IUnit:
		"""No Description

		Returns:
			IPipeUnits: 
		"""
		pass

	@property
	def HeadlossUnit(self) -> IUnit:
		"""No Description

		Returns:
			IPipeUnits: 
		"""
		pass

	@property
	def HeadlossGradientUnit(self) -> IUnit:
		"""No Description

		Returns:
			IPipeUnits: 
		"""
		pass

class ILateral(IWaterNetworkElement[ILaterals, ILateral, IBaseLinkUnits, ILateralInput, IBaseLinkResults, ILateralsInput, IBaseLinksResults]):

	def __init__(self) -> None:
		"""Creating a new Instance of this class is not allowed


		Raises:
			Exception: if this class is instanciated
		"""
		raise Exception("Creating a new Instance of this class is not allowed")
		pass

class ILaterals(IWaterNetworkElements[ILaterals, ILateral, IBaseLinkUnits, ILateralInput, IBaseLinkResults, ILateralsInput, IBaseLinksResults]):

	def __init__(self) -> None:
		"""Creating a new Instance of this class is not allowed


		Raises:
			Exception: if this class is instanciated
		"""
		raise Exception("Creating a new Instance of this class is not allowed")
		pass

class ILateralInput(IBaseLinkInput):

	def __init__(self) -> None:
		"""Creating a new Instance of this class is not allowed


		Raises:
			Exception: if this class is instanciated
		"""
		raise Exception("Creating a new Instance of this class is not allowed")
		pass

class ILateralsInput(IBaseLinksInput):

	def __init__(self) -> None:
		"""Creating a new Instance of this class is not allowed


		Raises:
			Exception: if this class is instanciated
		"""
		raise Exception("Creating a new Instance of this class is not allowed")
		pass

class IFireFlowNodesResults(IDemandNodesResults):

	def __init__(self) -> None:
		"""Creating a new Instance of this class is not allowed


		Raises:
			Exception: if this class is instanciated
		"""
		raise Exception("Creating a new Instance of this class is not allowed")
		pass

	@overload
	def IFireFlowNodesResults(self) -> Dict[int,int]:
		"""Gets the total calculated demand for all fire flow nodes at the current time step.

		Returns:
			Dict[int,int]: 
		"""
		pass

	@overload
	def IFireFlowNodesResults(self, timeStepIndex: int) -> Dict[int,int]:
		"""Gets the total calculated demand for all fire flow nodes at the given time step.

		Args:
			timeStepIndex(int): timeStepIndex

		Returns:
			Dict[int,int]: 
		"""
		pass

	@overload
	def IFireFlowNodesResults(self, ids: List[int], timeStepIndex: int) -> Dict[int,int]:
		"""No Description

		Args:
			ids(List[int]): ids
			timeStepIndex(int): timeStepIndex

		Returns:
			Dict[int,int]: 
		"""
		pass

	@overload
	def IFireFlowNodesResults(self) -> Dict[int,int]:
		"""Gets the node pressure at all fire flow nodes at the current time step.

		Returns:
			Dict[int,int]: 
		"""
		pass

	@overload
	def IFireFlowNodesResults(self, timeStepIndex: int) -> Dict[int,int]:
		"""Gets the node pressure at all fire flow nodes at the given time step.

		Args:
			timeStepIndex(int): timeStepIndex

		Returns:
			Dict[int,int]: 
		"""
		pass

	@overload
	def IFireFlowNodesResults(self, ids: List[int], timeStepIndex: int) -> Dict[int,int]:
		"""No Description

		Args:
			ids(List[int]): ids
			timeStepIndex(int): timeStepIndex

		Returns:
			Dict[int,int]: 
		"""
		pass

class IFireFlowNodeResults(IDemandNodeResults):

	def __init__(self) -> None:
		"""Creating a new Instance of this class is not allowed


		Raises:
			Exception: if this class is instanciated
		"""
		raise Exception("Creating a new Instance of this class is not allowed")
		pass

	@overload
	def IFireFlowNodeResults(self) -> Union[float, None]:
		"""Total calculated demand at selected element at current time step.

		Returns:
			Nullable: 
		"""
		pass

	@overload
	def IFireFlowNodeResults(self, timeStepIndex: int) -> Union[float, None]:
		"""Total calculated demand at selected element at given time step.

		Args:
			timeStepIndex(int): timeStepIndex

		Returns:
			Nullable: 
		"""
		pass

	@overload
	def IFireFlowNodeResults(self) -> Union[float, None]:
		"""TCalculated pressure at node at current time step.

		Returns:
			Nullable: 
		"""
		pass

	@overload
	def IFireFlowNodeResults(self, timeStepIndex: int) -> Union[float, None]:
		"""Calculated pressure at node at given time step.

		Args:
			timeStepIndex(int): timeStepIndex

		Returns:
			Nullable: 
		"""
		pass

	def Demands(self) -> array(Union[float, None]):
		"""Total calculated demand at selected element across all time steps.

		Returns:
			array(): 
		"""
		pass

	def Pressures(self) -> array(Union[float, None]):
		"""Calculated pressure at node across all time steps.

		Returns:
			array(): 
		"""
		pass

class IFireFlowNodeInput(IDemandNodeInput, IWaterTraceableInput):

	def __init__(self) -> None:
		"""Creating a new Instance of this class is not allowed


		Raises:
			Exception: if this class is instanciated
		"""
		raise Exception("Creating a new Instance of this class is not allowed")
		pass

class IFireFlowNodesInput(IDemandNodesInput):

	def __init__(self) -> None:
		"""Creating a new Instance of this class is not allowed


		Raises:
			Exception: if this class is instanciated
		"""
		raise Exception("Creating a new Instance of this class is not allowed")
		pass

class IFireFlowNodeUnits(IDemandNodeUnits):

	def __init__(self) -> None:
		"""Creating a new Instance of this class is not allowed


		Raises:
			Exception: if this class is instanciated
		"""
		raise Exception("Creating a new Instance of this class is not allowed")
		pass

	@property
	def DemandUnit(self) -> IUnit:
		"""No Description

		Returns:
			IFireFlowNodeUnits: 
		"""
		pass

	@property
	def PressureUnit(self) -> IUnit:
		"""No Description

		Returns:
			IFireFlowNodeUnits: 
		"""
		pass

class IJunctions(IWaterNetworkElements[IJunctions, IJunction, IJunctionUnits, IJunctionInput, IJunctionResults, IJunctionsInput, IJunctionsResults]):

	def __init__(self) -> None:
		"""Creating a new Instance of this class is not allowed


		Raises:
			Exception: if this class is instanciated
		"""
		raise Exception("Creating a new Instance of this class is not allowed")
		pass

class IJunction(IWaterNetworkElement[IJunctions, IJunction, IJunctionUnits, IJunctionInput, IJunctionResults, IJunctionsInput, IJunctionsResults]):

	def __init__(self) -> None:
		"""Creating a new Instance of this class is not allowed


		Raises:
			Exception: if this class is instanciated
		"""
		raise Exception("Creating a new Instance of this class is not allowed")
		pass

class IJunctionsResults(IFireFlowNodesResults):

	def __init__(self) -> None:
		"""Creating a new Instance of this class is not allowed


		Raises:
			Exception: if this class is instanciated
		"""
		raise Exception("Creating a new Instance of this class is not allowed")
		pass

class IJunctionsInput(IFireFlowNodesInput):

	def __init__(self) -> None:
		"""Creating a new Instance of this class is not allowed


		Raises:
			Exception: if this class is instanciated
		"""
		raise Exception("Creating a new Instance of this class is not allowed")
		pass

class IJunctionInput(IFireFlowNodeInput):

	def __init__(self) -> None:
		"""Creating a new Instance of this class is not allowed


		Raises:
			Exception: if this class is instanciated
		"""
		raise Exception("Creating a new Instance of this class is not allowed")
		pass

class IJunctionResults(IFireFlowNodeResults):

	def __init__(self) -> None:
		"""Creating a new Instance of this class is not allowed


		Raises:
			Exception: if this class is instanciated
		"""
		raise Exception("Creating a new Instance of this class is not allowed")
		pass

class IJunctionUnits(IFireFlowNodeUnits):

	def __init__(self) -> None:
		"""Creating a new Instance of this class is not allowed


		Raises:
			Exception: if this class is instanciated
		"""
		raise Exception("Creating a new Instance of this class is not allowed")
		pass

class IHydrants(IWaterNetworkElements[IHydrants, IHydrant, IHydrantUnits, IHydrantInput, IHydrantResults, IHydrantsInput, IHydrantsResults]):

	def __init__(self) -> None:
		"""Creating a new Instance of this class is not allowed


		Raises:
			Exception: if this class is instanciated
		"""
		raise Exception("Creating a new Instance of this class is not allowed")
		pass

class IHydrant(IWaterNetworkElement[IHydrants, IHydrant, IHydrantUnits, IHydrantInput, IHydrantResults, IHydrantsInput, IHydrantsResults]):

	def __init__(self) -> None:
		"""Creating a new Instance of this class is not allowed


		Raises:
			Exception: if this class is instanciated
		"""
		raise Exception("Creating a new Instance of this class is not allowed")
		pass

class IHydrantsResults(IFireFlowNodesResults):

	def __init__(self) -> None:
		"""Creating a new Instance of this class is not allowed


		Raises:
			Exception: if this class is instanciated
		"""
		raise Exception("Creating a new Instance of this class is not allowed")
		pass

class IHydrantResults(IFireFlowNodeResults):

	def __init__(self) -> None:
		"""Creating a new Instance of this class is not allowed


		Raises:
			Exception: if this class is instanciated
		"""
		raise Exception("Creating a new Instance of this class is not allowed")
		pass

class IHydrantsInput(IFireFlowNodesInput):

	def __init__(self) -> None:
		"""Creating a new Instance of this class is not allowed


		Raises:
			Exception: if this class is instanciated
		"""
		raise Exception("Creating a new Instance of this class is not allowed")
		pass

class IHydrantInput(IFireFlowNodeInput):

	def __init__(self) -> None:
		"""Creating a new Instance of this class is not allowed


		Raises:
			Exception: if this class is instanciated
		"""
		raise Exception("Creating a new Instance of this class is not allowed")
		pass

class IHydrantUnits(IFireFlowNodeUnits):

	def __init__(self) -> None:
		"""Creating a new Instance of this class is not allowed


		Raises:
			Exception: if this class is instanciated
		"""
		raise Exception("Creating a new Instance of this class is not allowed")
		pass

class IDemandNodeInput(IBaseNodeInput):

	def __init__(self) -> None:
		"""Creating a new Instance of this class is not allowed


		Raises:
			Exception: if this class is instanciated
		"""
		raise Exception("Creating a new Instance of this class is not allowed")
		pass

	@property
	def DemandCollection(self) -> IDemandCollection:
		"""No Description

		Returns:
			IDemandNodeInput: 
		"""
		pass

	@property
	def UnitDemandLoadCollection(self) -> IUnitLoadDemandCollection:
		"""No Description

		Returns:
			IDemandNodeInput: 
		"""
		pass

class IDemandNodesInput(IBaseNodesInput):

	def __init__(self) -> None:
		"""Creating a new Instance of this class is not allowed


		Raises:
			Exception: if this class is instanciated
		"""
		raise Exception("Creating a new Instance of this class is not allowed")
		pass

class IDemandNodesResults(IBaseNodesResults):

	def __init__(self) -> None:
		"""Creating a new Instance of this class is not allowed


		Raises:
			Exception: if this class is instanciated
		"""
		raise Exception("Creating a new Instance of this class is not allowed")
		pass

class IDemandNodeResults(IBaseNodeResults):

	def __init__(self) -> None:
		"""Creating a new Instance of this class is not allowed


		Raises:
			Exception: if this class is instanciated
		"""
		raise Exception("Creating a new Instance of this class is not allowed")
		pass

class IDemandNodeUnits(IBaseNodeUnits):

	def __init__(self) -> None:
		"""Creating a new Instance of this class is not allowed


		Raises:
			Exception: if this class is instanciated
		"""
		raise Exception("Creating a new Instance of this class is not allowed")
		pass

class IDemandCollection(ICollectionElements[IDemands, IDemand, IDemandUnits]):

	def __init__(self) -> None:
		"""Creating a new Instance of this class is not allowed


		Raises:
			Exception: if this class is instanciated
		"""
		raise Exception("Creating a new Instance of this class is not allowed")
		pass

class IDemands(ICollection[IDemand]):

	def __init__(self) -> None:
		"""Creating a new Instance of this class is not allowed


		Raises:
			Exception: if this class is instanciated
		"""
		raise Exception("Creating a new Instance of this class is not allowed")
		pass

	def Add(self, flow: float, pattern: IPattern) -> IDemand:
		"""Adds a new row to the list of demands and assigns the provided values.

		Args:
			flow(float): The demand flow in display units
			pattern(IPattern): The pattern to apply.  If null, assumes fixed pattern.

		Returns:
			IDemand: 
		"""
		pass

class IDemand(ICollectionElement):

	def __init__(self) -> None:
		"""Creating a new Instance of this class is not allowed


		Raises:
			Exception: if this class is instanciated
		"""
		raise Exception("Creating a new Instance of this class is not allowed")
		pass

	@property
	def BaseFlow(self) -> float:
		"""No Description

		Returns:
			IDemand: 
		"""
		pass

	@property
	def DemandPattern(self) -> IPattern:
		"""No Description

		Returns:
			IDemand: 
		"""
		pass

	@BaseFlow.setter
	def BaseFlow(self, baseflow: float) -> None:
		pass

	@DemandPattern.setter
	def DemandPattern(self, demandpattern: IPattern) -> None:
		pass

class IDemandUnits(IElementUnits):

	def __init__(self) -> None:
		"""Creating a new Instance of this class is not allowed


		Raises:
			Exception: if this class is instanciated
		"""
		raise Exception("Creating a new Instance of this class is not allowed")
		pass

	@property
	def BaseFlowUnit(self) -> IUnit:
		"""No Description

		Returns:
			IDemandUnits: 
		"""
		pass

class IUnitLoadDemandCollection(ICollectionElements[IUnitLoadDemands, IUnitLoadDemand, IUnitLoadDemandUnits]):

	def __init__(self) -> None:
		"""Creating a new Instance of this class is not allowed


		Raises:
			Exception: if this class is instanciated
		"""
		raise Exception("Creating a new Instance of this class is not allowed")
		pass

class IUnitLoadDemands(ICollection[IUnitLoadDemand]):

	def __init__(self) -> None:
		"""Creating a new Instance of this class is not allowed


		Raises:
			Exception: if this class is instanciated
		"""
		raise Exception("Creating a new Instance of this class is not allowed")
		pass

	def Add(self, unitDemandLoad: IUnitDemandLoad, numberOfLoadingUnits: float, unitDemandBaseFlow: float, unitDemandPattern: IPattern) -> IUnitLoadDemand:
		"""Adds a new row to the unit demands and assigns the values.

		Args:
			unitDemandLoad(IUnitDemandLoad): The unit demand load to use.
			numberOfLoadingUnits(float): The number of loading units to use.
			unitDemandBaseFlow(float): The unit demand base flow in display units.
			unitDemandPattern(IPattern): The demand pattern to apply.  If null, assumes fixed pattern.

		Returns:
			IUnitLoadDemand: 
		"""
		pass

class IUnitLoadDemand(ICollectionElement):

	def __init__(self) -> None:
		"""Creating a new Instance of this class is not allowed


		Raises:
			Exception: if this class is instanciated
		"""
		raise Exception("Creating a new Instance of this class is not allowed")
		pass

	@property
	def UnitDemandLoad(self) -> IUnitDemandLoad:
		"""No Description

		Returns:
			IUnitLoadDemand: 
		"""
		pass

	@property
	def NumberOfLoadingUnits(self) -> float:
		"""No Description

		Returns:
			IUnitLoadDemand: 
		"""
		pass

	@property
	def UnitDemandBaseFlow(self) -> float:
		"""No Description

		Returns:
			IUnitLoadDemand: 
		"""
		pass

	@property
	def UnitDemandPattern(self) -> IPattern:
		"""No Description

		Returns:
			IUnitLoadDemand: 
		"""
		pass

	@UnitDemandLoad.setter
	def UnitDemandLoad(self, unitdemandload: IUnitDemandLoad) -> None:
		pass

	@NumberOfLoadingUnits.setter
	def NumberOfLoadingUnits(self, numberofloadingunits: float) -> None:
		pass

	@UnitDemandBaseFlow.setter
	def UnitDemandBaseFlow(self, unitdemandbaseflow: float) -> None:
		pass

	@UnitDemandPattern.setter
	def UnitDemandPattern(self, unitdemandpattern: IPattern) -> None:
		pass

class IUnitLoadDemandUnits(IElementUnits):

	def __init__(self) -> None:
		"""Creating a new Instance of this class is not allowed


		Raises:
			Exception: if this class is instanciated
		"""
		raise Exception("Creating a new Instance of this class is not allowed")
		pass

	@property
	def UnitDemandBaseFlowUnit(self) -> IUnit:
		"""No Description

		Returns:
			IUnitLoadDemandUnits: 
		"""
		pass

class IConventionalTanksResults(IBaseTanksResults):

	def __init__(self) -> None:
		"""Creating a new Instance of this class is not allowed


		Raises:
			Exception: if this class is instanciated
		"""
		raise Exception("Creating a new Instance of this class is not allowed")
		pass

	@overload
	def IConventionalTanksResults(self) -> Dict[int,int]:
		"""The difference between the calculated hydraulic grade and the base elevation of the tank at the current time step at all tanks.

		Returns:
			Dict[int,int]: 
		"""
		pass

	@overload
	def IConventionalTanksResults(self, timeStepIndex: int) -> Dict[int,int]:
		"""The difference between the calculated hydraulic grade and the base elevation of the tank at the given time step at all tanks.

		Args:
			timeStepIndex(int): timeStepIndex

		Returns:
			Dict[int,int]: 
		"""
		pass

	@overload
	def IConventionalTanksResults(self, ids: List[int], timeStepIndex: int) -> Dict[int,int]:
		"""No Description

		Args:
			ids(List[int]): ids
			timeStepIndex(int): timeStepIndex

		Returns:
			Dict[int,int]: 
		"""
		pass

	@overload
	def IConventionalTanksResults(self) -> Dict[int,int]:
		"""Total volume of fluid in tank including the inactive volume at the current time step.

		Returns:
			Dict[int,int]: 
		"""
		pass

	@overload
	def IConventionalTanksResults(self, timeStepIndex: int) -> Dict[int,int]:
		"""Total volume of fluid in tank including the inactive volume at the given time step.

		Args:
			timeStepIndex(int): timeStepIndex

		Returns:
			Dict[int,int]: 
		"""
		pass

	@overload
	def IConventionalTanksResults(self, ids: List[int], timeStepIndex: int) -> Dict[int,int]:
		"""No Description

		Args:
			ids(List[int]): ids
			timeStepIndex(int): timeStepIndex

		Returns:
			Dict[int,int]: 
		"""
		pass

	@overload
	def IConventionalTanksResults(self) -> Dict[int,int]:
		"""The ratio of tank active volume to the tank full active volume. Active volume is the tank volume within the operating range and is exclusive of inactive volume at the current time step.

		Returns:
			Dict[int,int]: 
		"""
		pass

	@overload
	def IConventionalTanksResults(self, timeStepIndex: int) -> Dict[int,int]:
		"""The ratio of tank active volume to the tank full active volume. Active volume is the tank volume within the operating range and is exclusive of inactive volume at the given time step.

		Args:
			timeStepIndex(int): timeStepIndex

		Returns:
			Dict[int,int]: 
		"""
		pass

	@overload
	def IConventionalTanksResults(self, ids: List[int], timeStepIndex: int) -> Dict[int,int]:
		"""No Description

		Args:
			ids(List[int]): ids
			timeStepIndex(int): timeStepIndex

		Returns:
			Dict[int,int]: 
		"""
		pass

	@overload
	def IConventionalTanksResults(self) -> Dict[int,int]:
		"""Whether a tank is empty, emptying, full, or filling at the current time step.

		Returns:
			Dict[int,int]: 
		"""
		pass

	@overload
	def IConventionalTanksResults(self, timeStepIndex: int) -> Dict[int,int]:
		"""Whether a tank is empty, emptying, full, or filling at the given time step.

		Args:
			timeStepIndex(int): timeStepIndex

		Returns:
			Dict[int,int]: 
		"""
		pass

	@overload
	def IConventionalTanksResults(self, ids: List[int], timeStepIndex: int) -> Dict[int,int]:
		"""No Description

		Args:
			ids(List[int]): ids
			timeStepIndex(int): timeStepIndex

		Returns:
			Dict[int,int]: 
		"""
		pass

	def VolumeFulls(self) -> Dict[int,int]:
		"""The full active volume of all tanks between the limits of the defined operating range, exclusive of any inactive volume at the current time step.

		Returns:
			Dict[int,int]: 
		"""
		pass

class IConventionalTankResults(IBaseTankResults):

	def __init__(self) -> None:
		"""Creating a new Instance of this class is not allowed


		Raises:
			Exception: if this class is instanciated
		"""
		raise Exception("Creating a new Instance of this class is not allowed")
		pass

	@overload
	def IConventionalTankResults(self) -> Union[float, None]:
		"""The difference between the calculated hydraulic grade and the base elevation of the tank at the current time step.

		Returns:
			Nullable: 
		"""
		pass

	@overload
	def IConventionalTankResults(self, timeStepIndex: int) -> Union[float, None]:
		"""The difference between the calculated hydraulic grade and the base elevation of the tank at the given time step.

		Args:
			timeStepIndex(int): timeStepIndex

		Returns:
			Nullable: 
		"""
		pass

	@overload
	def IConventionalTankResults(self) -> Union[float, None]:
		"""Total volume of fluid in tank including the inactive volume at the current time step.

		Returns:
			Nullable: 
		"""
		pass

	@overload
	def IConventionalTankResults(self, timeStepIndex: int) -> Union[float, None]:
		"""Total volume of fluid in tank including the inactive volume at the given time step.

		Args:
			timeStepIndex(int): timeStepIndex

		Returns:
			Nullable: 
		"""
		pass

	@overload
	def IConventionalTankResults(self) -> Union[float, None]:
		"""The ratio of tank active volume to the tank full active volume. Active volume is the tank volume within the operating range and is exclusive of inactive volume at the current time step.

		Returns:
			Nullable: 
		"""
		pass

	@overload
	def IConventionalTankResults(self, timeStepIndex: int) -> Union[float, None]:
		"""The ratio of tank active volume to the tank full active volume. Active volume is the tank volume within the operating range and is exclusive of inactive volume at the given time step.

		Args:
			timeStepIndex(int): timeStepIndex

		Returns:
			Nullable: 
		"""
		pass

	@overload
	def IConventionalTankResults(self) -> Union[int, None]:
		"""Whether a tank is empty, emptying, full, or filling at the current time step.

		Returns:
			Nullable: 
		"""
		pass

	@overload
	def IConventionalTankResults(self, timeStepIndex: int) -> Union[int, None]:
		"""Whether a tank is empty, emptying, full, or filling at the given time step.

		Args:
			timeStepIndex(int): timeStepIndex

		Returns:
			Nullable: 
		"""
		pass

	def VolumeFull(self) -> Union[float, None]:
		"""The full active volume of the tank between the limits of the defined operating range, exclusive of any inactive volume at the current time step.

		Returns:
			Nullable: 
		"""
		pass

	def Levels(self) -> array(Union[float, None]):
		"""The difference between the calculated hydraulic grade and the base elevation of the tank across all time steps.

		Returns:
			array(): 
		"""
		pass

	def Volumes(self) -> array(Union[float, None]):
		"""Total volume of fluid in tank including the inactive volume across all time steps.

		Returns:
			array(): 
		"""
		pass

	def PercentFulls(self) -> array(Union[float, None]):
		"""The ratio of tank active volume to the tank full active volume. Active volume is the tank volume within the operating range and is exclusive of inactive volume over all time steps.

		Returns:
			array(): 
		"""
		pass

	def TankStatuses(self) -> array(Union[int, None]):
		"""Whether a tank is empty, emptying, full, or filling across all time steps.

		Returns:
			array(): 
		"""
		pass

class IConventionalTanksInput(IBaseTanksInput):

	def __init__(self) -> None:
		"""Creating a new Instance of this class is not allowed


		Raises:
			Exception: if this class is instanciated
		"""
		raise Exception("Creating a new Instance of this class is not allowed")
		pass

	@overload
	def IConventionalTanksInput(self) -> Dict[int,int]:
		"""The type of section the tank is using.

		Returns:
			Dict[int,int]: 
		"""
		pass

	@overload
	def IConventionalTanksInput(self, ids: List[int]) -> Dict[int,int]:
		"""No Description

		Args:
			ids(List[int]): ids

		Returns:
			Dict[int,int]: 
		"""
		pass

	@overload
	def IConventionalTanksInput(self) -> Dict[int,int]:
		"""InvalidOperationException is thrown if the section type is not variable area.

		Returns:
			Dict[int,int]: 
		"""
		pass

	@overload
	def IConventionalTanksInput(self, ids: List[int]) -> Dict[int,int]:
		"""No Description

		Args:
			ids(List[int]): ids

		Returns:
			Dict[int,int]: 
		"""
		pass

	@overload
	def IConventionalTanksInput(self) -> Dict[int,int]:
		"""InvalidOperationException is thrown if the section type is not circular.

		Returns:
			Dict[int,int]: 
		"""
		pass

	@overload
	def IConventionalTanksInput(self, ids: List[int]) -> Dict[int,int]:
		"""No Description

		Args:
			ids(List[int]): ids

		Returns:
			Dict[int,int]: 
		"""
		pass

	@overload
	def IConventionalTanksInput(self) -> Dict[int,int]:
		"""InvalidOperationException is thrown if the section type is not non-circular.

		Returns:
			Dict[int,int]: 
		"""
		pass

	@overload
	def IConventionalTanksInput(self, ids: List[int]) -> Dict[int,int]:
		"""No Description

		Args:
			ids(List[int]): ids

		Returns:
			Dict[int,int]: 
		"""
		pass

	@overload
	def IConventionalTanksInput(self) -> Dict[int,int]:
		"""Always in display units.

		Returns:
			Dict[int,int]: 
		"""
		pass

	@overload
	def IConventionalTanksInput(self, ids: List[int]) -> Dict[int,int]:
		"""No Description

		Args:
			ids(List[int]): ids

		Returns:
			Dict[int,int]: 
		"""
		pass

	@overload
	def IConventionalTanksInput(self) -> Dict[int,int]:
		"""If the operational range is set to elevation, the minimum elevation is automatically calculated and set when this property is set.

		Returns:
			Dict[int,int]: 
		"""
		pass

	@overload
	def IConventionalTanksInput(self, ids: List[int]) -> Dict[int,int]:
		"""No Description

		Args:
			ids(List[int]): ids

		Returns:
			Dict[int,int]: 
		"""
		pass

	@overload
	def IConventionalTanksInput(self) -> Dict[int,int]:
		"""If the operational range is set to elevation, the initial elevation is automatically calculated and set when this property is set.

		Returns:
			Dict[int,int]: 
		"""
		pass

	@overload
	def IConventionalTanksInput(self, ids: List[int]) -> Dict[int,int]:
		"""No Description

		Args:
			ids(List[int]): ids

		Returns:
			Dict[int,int]: 
		"""
		pass

	@overload
	def IConventionalTanksInput(self) -> Dict[int,int]:
		"""If the operational range is et to elevation, the maximum elevation is automatically calculated and set when this property is set.

		Returns:
			Dict[int,int]: 
		"""
		pass

	@overload
	def IConventionalTanksInput(self, ids: List[int]) -> Dict[int,int]:
		"""No Description

		Args:
			ids(List[int]): ids

		Returns:
			Dict[int,int]: 
		"""
		pass

	@overload
	def IConventionalTanksInput(self) -> Dict[int,int]:
		"""Specifies whether or not to check high alarm levels during Steady State/EPS calculation and generate messages if the levels are violated.

		Returns:
			Dict[int,int]: 
		"""
		pass

	@overload
	def IConventionalTanksInput(self, ids: List[int]) -> Dict[int,int]:
		"""No Description

		Args:
			ids(List[int]): ids

		Returns:
			Dict[int,int]: 
		"""
		pass

	@overload
	def IConventionalTanksInput(self) -> Dict[int,int]:
		"""The level above which the high level alarm is generated. Calculation notifications are produced to advise you of any alarm level violations.

		Returns:
			Dict[int,int]: 
		"""
		pass

	@overload
	def IConventionalTanksInput(self, ids: List[int]) -> Dict[int,int]:
		"""No Description

		Args:
			ids(List[int]): ids

		Returns:
			Dict[int,int]: 
		"""
		pass

	@overload
	def IConventionalTanksInput(self) -> Dict[int,int]:
		"""Specifies whether or not to check low alarm levels during Steady State/EPS calculation and generate messages if the levels are violated.

		Returns:
			Dict[int,int]: 
		"""
		pass

	@overload
	def IConventionalTanksInput(self, ids: List[int]) -> Dict[int,int]:
		"""No Description

		Args:
			ids(List[int]): ids

		Returns:
			Dict[int,int]: 
		"""
		pass

	@overload
	def IConventionalTanksInput(self) -> Dict[int,int]:
		"""The level below which the low level alarm is generated. Calculation notifications are produced to advise you of any alarm level violations.

		Returns:
			Dict[int,int]: 
		"""
		pass

	@overload
	def IConventionalTanksInput(self, ids: List[int]) -> Dict[int,int]:
		"""No Description

		Args:
			ids(List[int]): ids

		Returns:
			Dict[int,int]: 
		"""
		pass

	@overload
	def IConventionalTanksInput(self) -> Dict[int,int]:
		"""The inactive volume of the tank. 
            This volume is the inaccessible volume of the tank that is below the tank active operating range and can become important in water quality simulations subject to the selected mixing model.

		Returns:
			Dict[int,int]: 
		"""
		pass

	@overload
	def IConventionalTanksInput(self, ids: List[int]) -> Dict[int,int]:
		"""No Description

		Args:
			ids(List[int]): ids

		Returns:
			Dict[int,int]: 
		"""
		pass

class IConventionalTankInput(IBaseTankInput):

	def __init__(self) -> None:
		"""Creating a new Instance of this class is not allowed


		Raises:
			Exception: if this class is instanciated
		"""
		raise Exception("Creating a new Instance of this class is not allowed")
		pass

	@property
	def TankSection(self) -> TankSectionType:
		"""No Description

		Returns:
			IConventionalTankInput: 
		"""
		pass

	@property
	def ActiveVolumeFull(self) -> float:
		"""No Description

		Returns:
			IConventionalTankInput: 
		"""
		pass

	@property
	def CrossSectionCurve(self) -> ICrossSectionCurveCollection:
		"""No Description

		Returns:
			IConventionalTankInput: 
		"""
		pass

	@property
	def Diameter(self) -> float:
		"""No Description

		Returns:
			IConventionalTankInput: 
		"""
		pass

	@property
	def AverageArea(self) -> float:
		"""No Description

		Returns:
			IConventionalTankInput: 
		"""
		pass

	@property
	def BaseElevation(self) -> float:
		"""No Description

		Returns:
			IConventionalTankInput: 
		"""
		pass

	@property
	def MinimumLevel(self) -> float:
		"""No Description

		Returns:
			IConventionalTankInput: 
		"""
		pass

	@property
	def InitialLevel(self) -> float:
		"""No Description

		Returns:
			IConventionalTankInput: 
		"""
		pass

	@property
	def MaximumLevel(self) -> float:
		"""No Description

		Returns:
			IConventionalTankInput: 
		"""
		pass

	@property
	def UseHighAlarm(self) -> bool:
		"""No Description

		Returns:
			IConventionalTankInput: 
		"""
		pass

	@property
	def HighAlarmLevel(self) -> float:
		"""No Description

		Returns:
			IConventionalTankInput: 
		"""
		pass

	@property
	def UseLowAlarm(self) -> bool:
		"""No Description

		Returns:
			IConventionalTankInput: 
		"""
		pass

	@property
	def LowAlarmLevel(self) -> float:
		"""No Description

		Returns:
			IConventionalTankInput: 
		"""
		pass

	@property
	def InactiveVolume(self) -> float:
		"""No Description

		Returns:
			IConventionalTankInput: 
		"""
		pass

	@TankSection.setter
	def TankSection(self, tanksection: TankSectionType) -> None:
		pass

	@ActiveVolumeFull.setter
	def ActiveVolumeFull(self, activevolumefull: float) -> None:
		pass

	@Diameter.setter
	def Diameter(self, diameter: float) -> None:
		pass

	@AverageArea.setter
	def AverageArea(self, averagearea: float) -> None:
		pass

	@BaseElevation.setter
	def BaseElevation(self, baseelevation: float) -> None:
		pass

	@MinimumLevel.setter
	def MinimumLevel(self, minimumlevel: float) -> None:
		pass

	@InitialLevel.setter
	def InitialLevel(self, initiallevel: float) -> None:
		pass

	@MaximumLevel.setter
	def MaximumLevel(self, maximumlevel: float) -> None:
		pass

	@UseHighAlarm.setter
	def UseHighAlarm(self, usehighalarm: bool) -> None:
		pass

	@HighAlarmLevel.setter
	def HighAlarmLevel(self, highalarmlevel: float) -> None:
		pass

	@UseLowAlarm.setter
	def UseLowAlarm(self, uselowalarm: bool) -> None:
		pass

	@LowAlarmLevel.setter
	def LowAlarmLevel(self, lowalarmlevel: float) -> None:
		pass

	@InactiveVolume.setter
	def InactiveVolume(self, inactivevolume: float) -> None:
		pass

class IConventionalTankUnits(IBaseTankUnits):

	def __init__(self) -> None:
		"""Creating a new Instance of this class is not allowed


		Raises:
			Exception: if this class is instanciated
		"""
		raise Exception("Creating a new Instance of this class is not allowed")
		pass

	@property
	def LevelUnit(self) -> IUnit:
		"""No Description

		Returns:
			IConventionalTankUnits: 
		"""
		pass

	@property
	def VolumeUnit(self) -> IUnit:
		"""No Description

		Returns:
			IConventionalTankUnits: 
		"""
		pass

	@property
	def PercentFullUnit(self) -> IUnit:
		"""No Description

		Returns:
			IConventionalTankUnits: 
		"""
		pass

class ICrossSectionCurveCollection(ICollectionElements[ICrossSectionCurve, ICrossSectionCurveElement, ICrossSectionCurveUnits]):

	def __init__(self) -> None:
		"""Creating a new Instance of this class is not allowed


		Raises:
			Exception: if this class is instanciated
		"""
		raise Exception("Creating a new Instance of this class is not allowed")
		pass

class ICrossSectionCurve(ICollection[ICrossSectionCurveElement]):

	def __init__(self) -> None:
		"""Creating a new Instance of this class is not allowed


		Raises:
			Exception: if this class is instanciated
		"""
		raise Exception("Creating a new Instance of this class is not allowed")
		pass

	def Add(self, depthRatio: float, volumeRatio: float) -> ICrossSectionCurveElement:
		"""Adds a row to the cross-section curve and assigns the values.

		Args:
			depthRatio(float): The depth ratio in display units.
			volumeRatio(float): The volume ratio in display units.

		Returns:
			ICrossSectionCurveElement: 
		"""
		pass

class ICrossSectionCurveElement(ICollectionElement):

	def __init__(self) -> None:
		"""Creating a new Instance of this class is not allowed


		Raises:
			Exception: if this class is instanciated
		"""
		raise Exception("Creating a new Instance of this class is not allowed")
		pass

	@property
	def DepthRatio(self) -> float:
		"""No Description

		Returns:
			ICrossSectionCurveElement: 
		"""
		pass

	@property
	def VolumeRatio(self) -> float:
		"""No Description

		Returns:
			ICrossSectionCurveElement: 
		"""
		pass

	@DepthRatio.setter
	def DepthRatio(self, depthratio: float) -> None:
		pass

	@VolumeRatio.setter
	def VolumeRatio(self, volumeratio: float) -> None:
		pass

class ICrossSectionCurveUnits(IElementUnits):

	def __init__(self) -> None:
		"""Creating a new Instance of this class is not allowed


		Raises:
			Exception: if this class is instanciated
		"""
		raise Exception("Creating a new Instance of this class is not allowed")
		pass

	@property
	def RatioUnit(self) -> IUnit:
		"""No Description

		Returns:
			ICrossSectionCurveUnits: 
		"""
		pass

class ITanks(IWaterNetworkElements[ITanks, ITank, ITankUnits, ITankInput, ITankResults, ITanksInput, ITanksResults]):

	def __init__(self) -> None:
		"""Creating a new Instance of this class is not allowed


		Raises:
			Exception: if this class is instanciated
		"""
		raise Exception("Creating a new Instance of this class is not allowed")
		pass

class ITank(IWaterNetworkElement[ITanks, ITank, ITankUnits, ITankInput, ITankResults, ITanksInput, ITanksResults]):

	def __init__(self) -> None:
		"""Creating a new Instance of this class is not allowed


		Raises:
			Exception: if this class is instanciated
		"""
		raise Exception("Creating a new Instance of this class is not allowed")
		pass

class ITanksResults(IConventionalTanksResults):

	def __init__(self) -> None:
		"""Creating a new Instance of this class is not allowed


		Raises:
			Exception: if this class is instanciated
		"""
		raise Exception("Creating a new Instance of this class is not allowed")
		pass

class ITankResults(IConventionalTankResults):

	def __init__(self) -> None:
		"""Creating a new Instance of this class is not allowed


		Raises:
			Exception: if this class is instanciated
		"""
		raise Exception("Creating a new Instance of this class is not allowed")
		pass

class ITanksInput(IConventionalTanksInput):

	def __init__(self) -> None:
		"""Creating a new Instance of this class is not allowed


		Raises:
			Exception: if this class is instanciated
		"""
		raise Exception("Creating a new Instance of this class is not allowed")
		pass

	def ValveCharacteristics(self) -> Dict[int,int]:
		"""Specifies the valve characteristics definition to be used for this valve. If the Valve Characteristic Curve is not defined then a default curve will be used. The default curve will have (Relative Closure, Relative Area) points of (0,1) and (1,0).

		Returns:
			Dict[int,int]: 
		"""
		pass

	def ValveTypes(self) -> Dict[int,int]:
		"""Specifies the type of valve. Choices are Butterfly, Needle, Circular Gate, Globe, Ball and User Defined.

		Returns:
			Dict[int,int]: 
		"""
		pass

class ITankInput(IConventionalTankInput, IWaterTraceableInput):

	def __init__(self) -> None:
		"""Creating a new Instance of this class is not allowed


		Raises:
			Exception: if this class is instanciated
		"""
		raise Exception("Creating a new Instance of this class is not allowed")
		pass

	@property
	def ValveCharacteristics(self) -> IValveCharacteristic:
		"""No Description

		Returns:
			ITankInput: 
		"""
		pass

	@property
	def ValveType(self) -> HammerValveType:
		"""No Description

		Returns:
			ITankInput: 
		"""
		pass

	@ValveCharacteristics.setter
	def ValveCharacteristics(self, valvecharacteristics: IValveCharacteristic) -> None:
		pass

	@ValveType.setter
	def ValveType(self, valvetype: HammerValveType) -> None:
		pass

class ITankUnits(IConventionalTankUnits):

	def __init__(self) -> None:
		"""Creating a new Instance of this class is not allowed


		Raises:
			Exception: if this class is instanciated
		"""
		raise Exception("Creating a new Instance of this class is not allowed")
		pass

class ISurgeTankInput(IConventionalTankInput):

	def __init__(self) -> None:
		"""Creating a new Instance of this class is not allowed


		Raises:
			Exception: if this class is instanciated
		"""
		raise Exception("Creating a new Instance of this class is not allowed")
		pass

	@property
	def TankOrificeDiameter(self) -> float:
		"""No Description

		Returns:
			ISurgeTankInput: 
		"""
		pass

	@property
	def RatioOfLosses(self) -> float:
		"""No Description

		Returns:
			ISurgeTankInput: 
		"""
		pass

	@property
	def HeadlossCoefficient(self) -> float:
		"""No Description

		Returns:
			ISurgeTankInput: 
		"""
		pass

	@property
	def SurgeTankType(self) -> SurgeTankTypeEnum:
		"""No Description

		Returns:
			ISurgeTankInput: 
		"""
		pass

	@property
	def HasCheckValve(self) -> bool:
		"""No Description

		Returns:
			ISurgeTankInput: 
		"""
		pass

	@property
	def WeirCoefficient(self) -> float:
		"""No Description

		Returns:
			ISurgeTankInput: 
		"""
		pass

	@property
	def WeirLength(self) -> float:
		"""No Description

		Returns:
			ISurgeTankInput: 
		"""
		pass

	@property
	def InternalRiserDiameter(self) -> float:
		"""No Description

		Returns:
			ISurgeTankInput: 
		"""
		pass

	@property
	def InternalRiserTopElevation(self) -> float:
		"""No Description

		Returns:
			ISurgeTankInput: 
		"""
		pass

	@property
	def JunctionElevation(self) -> float:
		"""No Description

		Returns:
			ISurgeTankInput: 
		"""
		pass

	@property
	def DiameterExternalRiser(self) -> float:
		"""No Description

		Returns:
			ISurgeTankInput: 
		"""
		pass

	@property
	def ElevationOrificeFromInternalRiserInTank(self) -> float:
		"""No Description

		Returns:
			ISurgeTankInput: 
		"""
		pass

	@property
	def ElevationTopOfTankBase(self) -> float:
		"""No Description

		Returns:
			ISurgeTankInput: 
		"""
		pass

	@TankOrificeDiameter.setter
	def TankOrificeDiameter(self, tankorificediameter: float) -> None:
		pass

	@RatioOfLosses.setter
	def RatioOfLosses(self, ratiooflosses: float) -> None:
		pass

	@HeadlossCoefficient.setter
	def HeadlossCoefficient(self, headlosscoefficient: float) -> None:
		pass

	@SurgeTankType.setter
	def SurgeTankType(self, surgetanktype: SurgeTankTypeEnum) -> None:
		pass

	@HasCheckValve.setter
	def HasCheckValve(self, hascheckvalve: bool) -> None:
		pass

	@WeirCoefficient.setter
	def WeirCoefficient(self, weircoefficient: float) -> None:
		pass

	@WeirLength.setter
	def WeirLength(self, weirlength: float) -> None:
		pass

	@InternalRiserDiameter.setter
	def InternalRiserDiameter(self, internalriserdiameter: float) -> None:
		pass

	@InternalRiserTopElevation.setter
	def InternalRiserTopElevation(self, internalrisertopelevation: float) -> None:
		pass

	@JunctionElevation.setter
	def JunctionElevation(self, junctionelevation: float) -> None:
		pass

	@DiameterExternalRiser.setter
	def DiameterExternalRiser(self, diameterexternalriser: float) -> None:
		pass

	@ElevationOrificeFromInternalRiserInTank.setter
	def ElevationOrificeFromInternalRiserInTank(self, elevationorificefrominternalriserintank: float) -> None:
		pass

	@ElevationTopOfTankBase.setter
	def ElevationTopOfTankBase(self, elevationtopoftankbase: float) -> None:
		pass

class ISurgeTanksInput(IConventionalTanksInput):

	def __init__(self) -> None:
		"""Creating a new Instance of this class is not allowed


		Raises:
			Exception: if this class is instanciated
		"""
		raise Exception("Creating a new Instance of this class is not allowed")
		pass

	def TankOrificeDiameter(self) -> Dict[int,int]:
		"""Specifies the diameter of the tank inlet orifice. Only used by the transient engine.

		Returns:
			Dict[int,int]: 
		"""
		pass

	def RatioOfLosses(self) -> Dict[int,int]:
		"""Ratio of the head losses for equal inflows to / outflows from the tank via the orifice. Default value is 2.5.

		Returns:
			Dict[int,int]: 
		"""
		pass

	def HeadlossCoefficient(self) -> Dict[int,int]:
		"""Applies to flow from the tank to the pipe/riser. This must be a positive number.

		Returns:
			Dict[int,int]: 
		"""
		pass

	def SurgeTankType(self) -> Dict[int,int]:
		"""Specifies the type of surge tank to simulate in the transient engine.

		Returns:
			Dict[int,int]: 
		"""
		pass

	def HasCheckValve(self) -> Dict[int,int]:
		"""Specify whether there is a check valve installed on the tank inlet/outlet. For the case of steady state and EPS simulations, a surge tank with a check valve is simulated as a pressure junction.

		Returns:
			Dict[int,int]: 
		"""
		pass

	def WeirCoefficient(self) -> Dict[int,int]:
		"""Coefficient k in the formula for weir flow over the top of the tank as follows: Q = k L H^1.5 ( H >= 0 ) where Q is the rate of overflow, L is the width of the weir, and H is the height above the top of the tank. The coefficient must be positive. By default, it is the large positive number 99999, say. For a broad-crested weir, in SI units k = 1.84 (refer to Streeter and Wylie, pg. 358).

		Returns:
			Dict[int,int]: 
		"""
		pass

	def WeirLength(self) -> Dict[int,int]:
		"""The width of the weir.

		Returns:
			Dict[int,int]: 
		"""
		pass

	def InternalRiserDiameter(self) -> Dict[int,int]:
		"""This is the upper riser.

		Returns:
			Dict[int,int]: 
		"""
		pass

	def InternalRiserTopElevation(self) -> Dict[int,int]:
		"""The top of the upper riser.

		Returns:
			Dict[int,int]: 
		"""
		pass

	def JunctionElevation(self) -> Dict[int,int]:
		"""Elevation at which the external and internal risers meet.

		Returns:
			Dict[int,int]: 
		"""
		pass

	def DiameterExternalRiser(self) -> Dict[int,int]:
		"""This is the lower riser.

		Returns:
			Dict[int,int]: 
		"""
		pass

	def ElevationOrificeFromInternalRiserInTank(self) -> Dict[int,int]:
		"""Elevation of the internal riser orifice.

		Returns:
			Dict[int,int]: 
		"""
		pass

	def ElevationTopOfTankBase(self) -> Dict[int,int]:
		"""The elevation of the top of the hemisherical base of the tank. For a cylindrical tank, this is equal to the pipe elevation.

		Returns:
			Dict[int,int]: 
		"""
		pass

class ISurgeTankResults(IConventionalTankResults):

	def __init__(self) -> None:
		"""Creating a new Instance of this class is not allowed


		Raises:
			Exception: if this class is instanciated
		"""
		raise Exception("Creating a new Instance of this class is not allowed")
		pass

class ISurgeTanksResults(IConventionalTanksResults):

	def __init__(self) -> None:
		"""Creating a new Instance of this class is not allowed


		Raises:
			Exception: if this class is instanciated
		"""
		raise Exception("Creating a new Instance of this class is not allowed")
		pass

class ISurgeTankUnits(IConventionalTankUnits):

	def __init__(self) -> None:
		"""Creating a new Instance of this class is not allowed


		Raises:
			Exception: if this class is instanciated
		"""
		raise Exception("Creating a new Instance of this class is not allowed")
		pass

	@property
	def DiameterUnit(self) -> IUnit:
		"""No Description

		Returns:
			ISurgeTankUnits: 
		"""
		pass

	@property
	def RatioUnit(self) -> IUnit:
		"""No Description

		Returns:
			ISurgeTankUnits: 
		"""
		pass

	@property
	def WeirCoefficientUnit(self) -> IUnit:
		"""No Description

		Returns:
			ISurgeTankUnits: 
		"""
		pass

	@property
	def LengthUnit(self) -> IUnit:
		"""No Description

		Returns:
			ISurgeTankUnits: 
		"""
		pass

class ISurgeTanks(IWaterNetworkElements[ISurgeTanks, ISurgeTank, ISurgeTankUnits, ISurgeTankInput, ISurgeTankResults, ISurgeTanksInput, ISurgeTanksResults]):

	def __init__(self) -> None:
		"""Creating a new Instance of this class is not allowed


		Raises:
			Exception: if this class is instanciated
		"""
		raise Exception("Creating a new Instance of this class is not allowed")
		pass

class ISurgeTank(IWaterNetworkElement[ISurgeTanks, ISurgeTank, ISurgeTankUnits, ISurgeTankInput, ISurgeTankResults, ISurgeTanksInput, ISurgeTanksResults]):

	def __init__(self) -> None:
		"""Creating a new Instance of this class is not allowed


		Raises:
			Exception: if this class is instanciated
		"""
		raise Exception("Creating a new Instance of this class is not allowed")
		pass

class IBaseTanksResults(IDemandNodesResults):

	def __init__(self) -> None:
		"""Creating a new Instance of this class is not allowed


		Raises:
			Exception: if this class is instanciated
		"""
		raise Exception("Creating a new Instance of this class is not allowed")
		pass

	@overload
	def IBaseTanksResults(self) -> Dict[int,int]:
		"""Net flow out of the element at current time step.

		Returns:
			Dict[int,int]: 
		"""
		pass

	@overload
	def IBaseTanksResults(self, timeStepIndex: int) -> Dict[int,int]:
		"""Net flow out of the element at given time step.

		Args:
			timeStepIndex(int): timeStepIndex

		Returns:
			Dict[int,int]: 
		"""
		pass

	@overload
	def IBaseTanksResults(self, ids: List[int], timeStepIndex: int) -> Dict[int,int]:
		"""No Description

		Args:
			ids(List[int]): ids
			timeStepIndex(int): timeStepIndex

		Returns:
			Dict[int,int]: 
		"""
		pass

class IBaseTankResults(IDemandNodeResults):

	def __init__(self) -> None:
		"""Creating a new Instance of this class is not allowed


		Raises:
			Exception: if this class is instanciated
		"""
		raise Exception("Creating a new Instance of this class is not allowed")
		pass

	@overload
	def IBaseTankResults(self) -> Union[float, None]:
		"""Net flow out of the element at current time step.

		Returns:
			Nullable: 
		"""
		pass

	@overload
	def IBaseTankResults(self, timeStepIndex: int) -> Union[float, None]:
		"""Net flow out of the element at given time step.

		Args:
			timeStepIndex(int): timeStepIndex

		Returns:
			Nullable: 
		"""
		pass

	def Flows(self) -> array(Union[float, None]):
		"""Net flow out of the element across all time steps.

		Returns:
			array(): 
		"""
		pass

class IBaseTankInput(IDemandNodeInput):

	def __init__(self) -> None:
		"""Creating a new Instance of this class is not allowed


		Raises:
			Exception: if this class is instanciated
		"""
		raise Exception("Creating a new Instance of this class is not allowed")
		pass

class IBaseTanksInput(IDemandNodesInput):

	def __init__(self) -> None:
		"""Creating a new Instance of this class is not allowed


		Raises:
			Exception: if this class is instanciated
		"""
		raise Exception("Creating a new Instance of this class is not allowed")
		pass

class IBaseTankUnits(IDemandNodeUnits):

	def __init__(self) -> None:
		"""Creating a new Instance of this class is not allowed


		Raises:
			Exception: if this class is instanciated
		"""
		raise Exception("Creating a new Instance of this class is not allowed")
		pass

	@property
	def FlowUnit(self) -> IUnit:
		"""No Description

		Returns:
			IBaseTankUnits: 
		"""
		pass

class IVariableLevelCurveCollection(ICollectionElements[ILevelDiameters, ILevelDiameter, IVariableLevelCurveUnits]):

	def __init__(self) -> None:
		"""Creating a new Instance of this class is not allowed


		Raises:
			Exception: if this class is instanciated
		"""
		raise Exception("Creating a new Instance of this class is not allowed")
		pass

class ILevelDiameters(ICollection[ILevelDiameter]):

	def __init__(self) -> None:
		"""Creating a new Instance of this class is not allowed


		Raises:
			Exception: if this class is instanciated
		"""
		raise Exception("Creating a new Instance of this class is not allowed")
		pass

	def Add(self, liquidLevel: float, diameter: float) -> ILevelDiameter:
		"""Adds a new row with the given data.

		Args:
			liquidLevel(float): liquidLevel
			diameter(float): diameter

		Returns:
			ILevelDiameter: 
		"""
		pass

class ILevelDiameter(ICollectionElement):

	def __init__(self) -> None:
		"""Creating a new Instance of this class is not allowed


		Raises:
			Exception: if this class is instanciated
		"""
		raise Exception("Creating a new Instance of this class is not allowed")
		pass

	@property
	def LiquidLevel(self) -> float:
		"""No Description

		Returns:
			ILevelDiameter: 
		"""
		pass

	@property
	def EquivalentDiameter(self) -> float:
		"""No Description

		Returns:
			ILevelDiameter: 
		"""
		pass

	@LiquidLevel.setter
	def LiquidLevel(self, liquidlevel: float) -> None:
		pass

	@EquivalentDiameter.setter
	def EquivalentDiameter(self, equivalentdiameter: float) -> None:
		pass

class IVariableLevelCurveUnits(IElementUnits):

	def __init__(self) -> None:
		"""Creating a new Instance of this class is not allowed


		Raises:
			Exception: if this class is instanciated
		"""
		raise Exception("Creating a new Instance of this class is not allowed")
		pass

	@property
	def LevelUnit(self) -> IUnit:
		"""No Description

		Returns:
			IVariableLevelCurveUnits: 
		"""
		pass

	@property
	def DiameterUnit(self) -> IUnit:
		"""No Description

		Returns:
			IVariableLevelCurveUnits: 
		"""
		pass

class IHydroTankInput(IBaseTankInput):

	def __init__(self) -> None:
		"""Creating a new Instance of this class is not allowed


		Raises:
			Exception: if this class is instanciated
		"""
		raise Exception("Creating a new Instance of this class is not allowed")
		pass

	@property
	def InitialVolumeOfGas(self) -> float:
		"""No Description

		Returns:
			IHydroTankInput: 
		"""
		pass

	@property
	def TankInletOrificeDiameter(self) -> float:
		"""No Description

		Returns:
			IHydroTankInput: 
		"""
		pass

	@property
	def RatioOfLosses(self) -> float:
		"""No Description

		Returns:
			IHydroTankInput: 
		"""
		pass

	@property
	def GasLawExponent(self) -> float:
		"""No Description

		Returns:
			IHydroTankInput: 
		"""
		pass

	@property
	def HasBladder(self) -> bool:
		"""No Description

		Returns:
			IHydroTankInput: 
		"""
		pass

	@property
	def GasPresetPressure(self) -> float:
		"""No Description

		Returns:
			IHydroTankInput: 
		"""
		pass

	@property
	def MeanLiquidElevation(self) -> float:
		"""No Description

		Returns:
			IHydroTankInput: 
		"""
		pass

	@property
	def AirInflowOrificeDiameter(self) -> float:
		"""No Description

		Returns:
			IHydroTankInput: 
		"""
		pass

	@property
	def AirOutflowOrificeDiameter(self) -> float:
		"""No Description

		Returns:
			IHydroTankInput: 
		"""
		pass

	@property
	def DippingTubeDiameter(self) -> float:
		"""No Description

		Returns:
			IHydroTankInput: 
		"""
		pass

	@property
	def CompressionChamberVolume(self) -> float:
		"""No Description

		Returns:
			IHydroTankInput: 
		"""
		pass

	@property
	def TopElevationDippingTube(self) -> float:
		"""No Description

		Returns:
			IHydroTankInput: 
		"""
		pass

	@property
	def BottomElevationDippingTube(self) -> float:
		"""No Description

		Returns:
			IHydroTankInput: 
		"""
		pass

	@property
	def LevelType(self) -> GasVesselLevelType:
		"""No Description

		Returns:
			IHydroTankInput: 
		"""
		pass

	@property
	def HydroTankType(self) -> HydroTankType:
		"""No Description

		Returns:
			IHydroTankInput: 
		"""
		pass

	@property
	def VariableLevelCurve(self) -> IVariableLevelCurveCollection:
		"""No Description

		Returns:
			IHydroTankInput: 
		"""
		pass

	@property
	def TankVolume(self) -> float:
		"""No Description

		Returns:
			IHydroTankInput: 
		"""
		pass

	@property
	def InflowMinorLossCoefficient(self) -> float:
		"""No Description

		Returns:
			IHydroTankInput: 
		"""
		pass

	@property
	def TankBaseElevation(self) -> float:
		"""No Description

		Returns:
			IHydroTankInput: 
		"""
		pass

	@property
	def TreatAsJunction(self) -> bool:
		"""No Description

		Returns:
			IHydroTankInput: 
		"""
		pass

	@property
	def OperatingRangeType(self) -> OperatingRangeTypeEnum:
		"""No Description

		Returns:
			IHydroTankInput: 
		"""
		pass

	@property
	def TankCalculationModel(self) -> TankCalculationModel:
		"""No Description

		Returns:
			IHydroTankInput: 
		"""
		pass

	@property
	def TankInitialElevation(self) -> float:
		"""No Description

		Returns:
			IHydroTankInput: 
		"""
		pass

	@property
	def TankInitialLevel(self) -> float:
		"""No Description

		Returns:
			IHydroTankInput: 
		"""
		pass

	@property
	def TankInitialLiquidVolume(self) -> float:
		"""No Description

		Returns:
			IHydroTankInput: 
		"""
		pass

	@property
	def AirInflowOrificeAirFlowCurve(self) -> IAirFlowCurve:
		"""No Description

		Returns:
			IHydroTankInput: 
		"""
		pass

	@property
	def AirOutflowOrificeAirFlowCurve(self) -> IAirFlowCurve:
		"""No Description

		Returns:
			IHydroTankInput: 
		"""
		pass

	@property
	def AirFlowCalculationMethod(self) -> AirFlowCalculationMethod:
		"""No Description

		Returns:
			IHydroTankInput: 
		"""
		pass

	@InitialVolumeOfGas.setter
	def InitialVolumeOfGas(self, initialvolumeofgas: float) -> None:
		pass

	@TankInletOrificeDiameter.setter
	def TankInletOrificeDiameter(self, tankinletorificediameter: float) -> None:
		pass

	@RatioOfLosses.setter
	def RatioOfLosses(self, ratiooflosses: float) -> None:
		pass

	@GasLawExponent.setter
	def GasLawExponent(self, gaslawexponent: float) -> None:
		pass

	@HasBladder.setter
	def HasBladder(self, hasbladder: bool) -> None:
		pass

	@GasPresetPressure.setter
	def GasPresetPressure(self, gaspresetpressure: float) -> None:
		pass

	@MeanLiquidElevation.setter
	def MeanLiquidElevation(self, meanliquidelevation: float) -> None:
		pass

	@AirInflowOrificeDiameter.setter
	def AirInflowOrificeDiameter(self, airinfloworificediameter: float) -> None:
		pass

	@AirOutflowOrificeDiameter.setter
	def AirOutflowOrificeDiameter(self, airoutfloworificediameter: float) -> None:
		pass

	@DippingTubeDiameter.setter
	def DippingTubeDiameter(self, dippingtubediameter: float) -> None:
		pass

	@CompressionChamberVolume.setter
	def CompressionChamberVolume(self, compressionchambervolume: float) -> None:
		pass

	@TopElevationDippingTube.setter
	def TopElevationDippingTube(self, topelevationdippingtube: float) -> None:
		pass

	@BottomElevationDippingTube.setter
	def BottomElevationDippingTube(self, bottomelevationdippingtube: float) -> None:
		pass

	@LevelType.setter
	def LevelType(self, leveltype: GasVesselLevelType) -> None:
		pass

	@HydroTankType.setter
	def HydroTankType(self, hydrotanktype: HydroTankType) -> None:
		pass

	@TankVolume.setter
	def TankVolume(self, tankvolume: float) -> None:
		pass

	@InflowMinorLossCoefficient.setter
	def InflowMinorLossCoefficient(self, inflowminorlosscoefficient: float) -> None:
		pass

	@TankBaseElevation.setter
	def TankBaseElevation(self, tankbaseelevation: float) -> None:
		pass

	@TreatAsJunction.setter
	def TreatAsJunction(self, treatasjunction: bool) -> None:
		pass

	@OperatingRangeType.setter
	def OperatingRangeType(self, operatingrangetype: OperatingRangeTypeEnum) -> None:
		pass

	@TankCalculationModel.setter
	def TankCalculationModel(self, tankcalculationmodel: TankCalculationModel) -> None:
		pass

	@TankInitialElevation.setter
	def TankInitialElevation(self, tankinitialelevation: float) -> None:
		pass

	@TankInitialLevel.setter
	def TankInitialLevel(self, tankinitiallevel: float) -> None:
		pass

	@TankInitialLiquidVolume.setter
	def TankInitialLiquidVolume(self, tankinitialliquidvolume: float) -> None:
		pass

	@AirInflowOrificeAirFlowCurve.setter
	def AirInflowOrificeAirFlowCurve(self, airinfloworificeairflowcurve: IAirFlowCurve) -> None:
		pass

	@AirOutflowOrificeAirFlowCurve.setter
	def AirOutflowOrificeAirFlowCurve(self, airoutfloworificeairflowcurve: IAirFlowCurve) -> None:
		pass

	@AirFlowCalculationMethod.setter
	def AirFlowCalculationMethod(self, airflowcalculationmethod: AirFlowCalculationMethod) -> None:
		pass

class IHydroTanksInput(IBaseTanksInput):

	def __init__(self) -> None:
		"""Creating a new Instance of this class is not allowed


		Raises:
			Exception: if this class is instanciated
		"""
		raise Exception("Creating a new Instance of this class is not allowed")
		pass

	def InitialVolumeOfGas(self) -> Dict[int,int]:
		"""The initial volume of gas in the pressure vessel at the start of the simulation. During the transient event, this gas volume expands or compresses, depending on the transient pressures in the system. Not used in steady state or EPS analyses.

		Returns:
			Dict[int,int]: 
		"""
		pass

	def TankInletOrificeDiameter(self) -> Dict[int,int]:
		"""This is the size of the opening between the gas vessel and the main pipe line. It is typically smaller than the main pipe size. It is used to compute the correct velocity through the tank inlet, so the correct headloss is computed based on the minor loss coefficient (the standard head loss equation is used: Hl = K*V2/2g.)

		Returns:
			Dict[int,int]: 
		"""
		pass

	def RatioOfLosses(self) -> Dict[int,int]:
		"""For same flow magnitude, ratio of inflow head loss to outflow loss. Default value is 2.5.

		Returns:
			Dict[int,int]: 
		"""
		pass

	def GasLawExponent(self) -> Dict[int,int]:
		"""Refers to the exponent to be used in the gas law equation. The usual range of this exponent is 1.0 to 1.4.

		Returns:
			Dict[int,int]: 
		"""
		pass

	def HasBladder(self) -> Dict[int,int]:
		"""Denotes whether the gas is contained within a bladder. If it is set to true, the transient analysis automatically assumes that the bladder occupied the full-tank volume at the preset pressure at some time and that the air volume was compressed to a smaller size by the steady-state pressure in the system. In this case the full-tank volume is specified by the Volume (Tank) field under ?Physical?.

		Returns:
			Dict[int,int]: 
		"""
		pass

	def GasPresetPressure(self) -> Dict[int,int]:
		"""If there is a bladder, this is the pressure of the gas prior to exposing the tank to pipeline pressure; otherwise, this should be omitted as it is ignored.

		Returns:
			Dict[int,int]: 
		"""
		pass

	def MeanLiquidElevation(self) -> Dict[int,int]:
		"""The mean elevation of the liquid at the gas-liquid interface. (Liquid level referenced from a datum of 0).

		Returns:
			Dict[int,int]: 
		"""
		pass

	def AirInflowOrificeDiameter(self) -> Dict[int,int]:
		"""This is the equivalent orifice size of the opening that allows air to enter the tank.

		Returns:
			Dict[int,int]: 
		"""
		pass

	def AirOutflowOrificeDiameter(self) -> Dict[int,int]:
		"""This is the equivalent orifice size of the opening that allows air to leave the tank.

		Returns:
			Dict[int,int]: 
		"""
		pass

	def DippingTubeDiameter(self) -> Dict[int,int]:
		"""The diameter of the dipping or ventilation tube within the hydropneumatic tank (only applicable for the Dipping Tube tank type)

		Returns:
			Dict[int,int]: 
		"""
		pass

	def CompressionChamberVolume(self) -> Dict[int,int]:
		"""The volume of the air around the dipping tube that is compressed once the water level elevation exceeds the bottom of the dipping tube.

		Returns:
			Dict[int,int]: 
		"""
		pass

	def TopElevationDippingTube(self) -> Dict[int,int]:
		"""The elevation of the top of the dipping tube and the dipping tube-type hydropneumatic tank.

		Returns:
			Dict[int,int]: 
		"""
		pass

	def BottomElevationDippingTube(self) -> Dict[int,int]:
		"""The elevation of the bottom of the dipping tube.

		Returns:
			Dict[int,int]: 
		"""
		pass

	def LevelType(self) -> Dict[int,int]:
		"""Specify the elevation type to be used for the transient analysis of the gas-liquid interface. The elevation in this instance is used to refer to the liquid level elevation (i.e., level referenced from a datum of zero.)

		Returns:
			Dict[int,int]: 
		"""
		pass

	def HydroTankType(self) -> Dict[int,int]:
		"""Specify the type of Hydropneumatic Tank that this model element represents. Sealed means the tank is a fully sealed pressure vessel. Vented means the tank has an air valve attached. Dipping tube means the tank has an internal dipping or ventilation tube.

		Returns:
			Dict[int,int]: 
		"""
		pass

	def TankVolume(self) -> Dict[int,int]:
		"""The total volume of the hydropneumatic tank. This value is used by steady state / EPS analysis for both the Constant Area Approximation and Gas Law calculation models. For a transient analysis, this value is only used if the "Has Bladder?" property under ?Transient (Physical)? is set to true.

		Returns:
			Dict[int,int]: 
		"""
		pass

	def InflowMinorLossCoefficient(self) -> Dict[int,int]:
		"""Dimensionless quantity, typical value = 2.5. This property is used only for transient analysis, to restrict the flow out of the hydropneumatic tank.

		Returns:
			Dict[int,int]: 
		"""
		pass

	def TankBaseElevation(self) -> Dict[int,int]:
		"""Elevation of the storage tank base used as a reference when entering water surface elevations in the tank in terms of levels.

		Returns:
			Dict[int,int]: 
		"""
		pass

	def TreatAsJunction(self) -> Dict[int,int]:
		"""Specifies whether or not to treat the hydropneumatic tank as a junction in steady state and EPS simulations. Note that if you wish to use the steady state / EPS results as input for a HAMMER transient analysis and you set this field to true, you will need to manually enter the initial gas volume of the tank for HAMMER.

		Returns:
			Dict[int,int]: 
		"""
		pass

	def OperatingRangeType(self) -> Dict[int,int]:
		"""Specify whether the vertical parameters of the tank are specified as levels measured from the base elevation or as elevations measured from the global datum.

		Returns:
			Dict[int,int]: 
		"""
		pass

	def TankCalculationModel(self) -> Dict[int,int]:
		"""Specifies which of the two models (constant area approximation and gas law model) should be used to simulate this hydropneumatic tank. Applies to steady state and EPS analyses only.

		Returns:
			Dict[int,int]: 
		"""
		pass

	def TankInitialElevation(self) -> Dict[int,int]:
		"""Starting water surface elevation/level in the tank. Used in steady state and EPS analyses.

		Returns:
			Dict[int,int]: 
		"""
		pass

	def TankInitialLevel(self) -> Dict[int,int]:
		"""Starting water surface elevation/level in the tank. Used in steady state and EPS analyses.

		Returns:
			Dict[int,int]: 
		"""
		pass

	def TankInitialLiquidVolume(self) -> Dict[int,int]:
		"""Starting liquid volume in the tank. For constant area approximation tanks, this volume includes the inactive volume of the tank that lies below the effective volume.

		Returns:
			Dict[int,int]: 
		"""
		pass

	def AirInflowOrificeAirFlowCurve(self) -> Dict[int,int]:
		"""The curve that defines the rate of air inflow (a ?free air? rate, measured at atmospheric pressure) into the tank versus the differential pressure across the air valve.

		Returns:
			Dict[int,int]: 
		"""
		pass

	def AirOutflowOrificeAirFlowCurve(self) -> Dict[int,int]:
		"""The curve that defines the rate of air outflow (a ?free air? rate, measured at atmospheric pressure) out of the tank versus the differential pressure across the air valve.

		Returns:
			Dict[int,int]: 
		"""
		pass

	def AirFlowCalculationMethod(self) -> Dict[int,int]:
		"""Specify whether the air valve air flow rate is determined by user-entered curves of pressure vs. air flow rate, or whether it is calculated based on a user-entered orifice diameter (not applicable for a sealed hydropneumatic tank).

		Returns:
			Dict[int,int]: 
		"""
		pass

class IHydroTankResults(IBaseTankResults):

	def __init__(self) -> None:
		"""Creating a new Instance of this class is not allowed


		Raises:
			Exception: if this class is instanciated
		"""
		raise Exception("Creating a new Instance of this class is not allowed")
		pass

	@overload
	def IHydroTankResults(self) -> Union[float, None]:
		"""The calculated volume of gas in the hydropneumatic tank. This result is based on the steady state Tank Calculation Model, however, if the tank is a Dipping Tube tank with a defined Variable Elevation Curve, this result is re-calculated to be representative of the dipping tube tank geometry. If the tank is simulated as a junction in steady state this result will be reported as N/A.

		Returns:
			Nullable: 
		"""
		pass

	@overload
	def IHydroTankResults(self, timeStepIndex: int) -> Union[float, None]:
		"""The calculated volume of gas in the hydropneumatic tank. This result is based on the steady state Tank Calculation Model, however, if the tank is a Dipping Tube tank with a defined Variable Elevation Curve, this result is re-calculated to be representative of the dipping tube tank geometry. If the tank is simulated as a junction in steady state this result will be reported as N/A.

		Args:
			timeStepIndex(int): timeStepIndex

		Returns:
			Nullable: 
		"""
		pass

	@overload
	def IHydroTankResults(self) -> Union[float, None]:
		"""The calculated pressure in the hydropenumatic tank. This result is based on the steady state Tank Calculation Model, however, if the tank is a Dipping Tube tank with a defined Variable Elevation Curve, this result is re-calculated to be representative of the dipping tube tank geometry. If the tank is simulated as a junction in steady state this result will be reported as N/A.

		Returns:
			Nullable: 
		"""
		pass

	@overload
	def IHydroTankResults(self, timeStepIndex: int) -> Union[float, None]:
		"""The calculated pressure in the hydropenumatic tank. This result is based on the steady state Tank Calculation Model, however, if the tank is a Dipping Tube tank with a defined Variable Elevation Curve, this result is re-calculated to be representative of the dipping tube tank geometry. If the tank is simulated as a junction in steady state this result will be reported as N/A.

		Args:
			timeStepIndex(int): timeStepIndex

		Returns:
			Nullable: 
		"""
		pass

	@overload
	def IHydroTankResults(self) -> Union[float, None]:
		"""The calculated liquid volume in the hydropneumatic tank. This result is based on the steady state Tank Calculation Model, however, if the tank is a Dipping Tube tank with a defined Variable Elevation Curve, this result is re-calculated to be representative of the dipping tube tank geometry. If the tank is simulated as a junction in steady state this result will be reported as N/A.

		Returns:
			Nullable: 
		"""
		pass

	@overload
	def IHydroTankResults(self, timeStepIndex: int) -> Union[float, None]:
		"""The calculated liquid volume in the hydropneumatic tank. This result is based on the steady state Tank Calculation Model, however, if the tank is a Dipping Tube tank with a defined Variable Elevation Curve, this result is re-calculated to be representative of the dipping tube tank geometry. If the tank is simulated as a junction in steady state this result will be reported as N/A.

		Args:
			timeStepIndex(int): timeStepIndex

		Returns:
			Nullable: 
		"""
		pass

	@overload
	def IHydroTankResults(self) -> Union[float, None]:
		"""The ratio of the fluid volume in the tank to the calculated full volume of the tank. This result is based on the steady state Tank Calculation Model, however, if the tank is a Dipping Tube tank with a defined Variable Elevation Curve, this result is re-calculated to be representative of the dipping tube tank geometry. If the tank is simulated as a junction in steady state this result will be reported as N/A.

		Returns:
			Nullable: 
		"""
		pass

	@overload
	def IHydroTankResults(self, timeStepIndex: int) -> Union[float, None]:
		"""The ratio of the fluid volume in the tank to the calculated full volume of the tank. This result is based on the steady state Tank Calculation Model, however, if the tank is a Dipping Tube tank with a defined Variable Elevation Curve, this result is re-calculated to be representative of the dipping tube tank geometry. If the tank is simulated as a junction in steady state this result will be reported as N/A.

		Args:
			timeStepIndex(int): timeStepIndex

		Returns:
			Nullable: 
		"""
		pass

	def CalculatedGasVolumes(self) -> array(Union[float, None]):
		"""The calculated volume of gas in the hydropneumatic tank. This result is based on the steady state Tank Calculation Model, however, if the tank is a Dipping Tube tank with a defined Variable Elevation Curve, this result is re-calculated to be representative of the dipping tube tank geometry. If the tank is simulated as a junction in steady state this result will be reported as N/A.

		Returns:
			array(): 
		"""
		pass

	def CalculatedPressures(self) -> array(Union[float, None]):
		"""The calculated pressure in the hydropenumatic tank. This result is based on the steady state Tank Calculation Model, however, if the tank is a Dipping Tube tank with a defined Variable Elevation Curve, this result is re-calculated to be representative of the dipping tube tank geometry. If the tank is simulated as a junction in steady state this result will be reported as N/A.

		Returns:
			array(): 
		"""
		pass

	def CalculatedLiquidVolumes(self) -> array(Union[float, None]):
		"""The calculated liquid volume in the hydropneumatic tank. This result is based on the steady state Tank Calculation Model, however, if the tank is a Dipping Tube tank with a defined Variable Elevation Curve, this result is re-calculated to be representative of the dipping tube tank geometry. If the tank is simulated as a junction in steady state this result will be reported as N/A.

		Returns:
			array(): 
		"""
		pass

	def CalculatedPercentFulls(self) -> array(Union[float, None]):
		"""The ratio of the fluid volume in the tank to the calculated full volume of the tank. This result is based on the steady state Tank Calculation Model, however, if the tank is a Dipping Tube tank with a defined Variable Elevation Curve, this result is re-calculated to be representative of the dipping tube tank geometry. If the tank is simulated as a junction in steady state this result will be reported as N/A.

		Returns:
			array(): 
		"""
		pass

	def MaximumTransientGasPressure(self) -> Union[float, None]:
		"""Maximum gas pressure at hydropneumatic tank over the course of the transient simulation.

		Returns:
			Nullable: 
		"""
		pass

	def MinimumTransientGasPressure(self) -> Union[float, None]:
		"""Minimum gas pressure at hydropneumatic tank over the course of the transient simulation.

		Returns:
			Nullable: 
		"""
		pass

	def MaximumTransientGasVolume(self) -> Union[float, None]:
		"""Maximum gas volume at hydropneumatic tank over the course of the transient simulation.

		Returns:
			Nullable: 
		"""
		pass

	def MinimumTransientGasVolume(self) -> Union[float, None]:
		"""Minimum gas volume at hydropneumatic tank over the course of the transient simulation.

		Returns:
			Nullable: 
		"""
		pass

	def MaximumTransientWaterLevel(self) -> Union[float, None]:
		"""Maximum water level at hydropneumatic tank over the course of the transient simulation.

		Returns:
			Nullable: 
		"""
		pass

	def MinimumTransientWaterLevel(self) -> Union[float, None]:
		"""Minimum water level at hydropneumatic tank over the course of the transient simulation.

		Returns:
			Nullable: 
		"""
		pass

class IHydroTanksResults(IBaseTanksResults):

	def __init__(self) -> None:
		"""Creating a new Instance of this class is not allowed


		Raises:
			Exception: if this class is instanciated
		"""
		raise Exception("Creating a new Instance of this class is not allowed")
		pass

	@overload
	def IHydroTanksResults(self) -> Dict[int,int]:
		"""The calculated volume of gas in the hydropneumatic tank. This result is based on the steady state Tank Calculation Model, however, if the tank is a Dipping Tube tank with a defined Variable Elevation Curve, this result is re-calculated to be representative of the dipping tube tank geometry. If the tank is simulated as a junction in steady state this result will be reported as N/A.

		Returns:
			Dict[int,int]: 
		"""
		pass

	@overload
	def IHydroTanksResults(self, timeStepIndex: int) -> Dict[int,int]:
		"""The calculated volume of gas in the hydropneumatic tank. This result is based on the steady state Tank Calculation Model, however, if the tank is a Dipping Tube tank with a defined Variable Elevation Curve, this result is re-calculated to be representative of the dipping tube tank geometry. If the tank is simulated as a junction in steady state this result will be reported as N/A.

		Args:
			timeStepIndex(int): timeStepIndex

		Returns:
			Dict[int,int]: 
		"""
		pass

	@overload
	def IHydroTanksResults(self, ids: List[int], timeStepIndex: int) -> Dict[int,int]:
		"""No Description

		Args:
			ids(List[int]): ids
			timeStepIndex(int): timeStepIndex

		Returns:
			Dict[int,int]: 
		"""
		pass

	@overload
	def IHydroTanksResults(self) -> Dict[int,int]:
		"""The calculated pressure in the hydropenumatic tank. This result is based on the steady state Tank Calculation Model, however, if the tank is a Dipping Tube tank with a defined Variable Elevation Curve, this result is re-calculated to be representative of the dipping tube tank geometry. If the tank is simulated as a junction in steady state this result will be reported as N/A.

		Returns:
			Dict[int,int]: 
		"""
		pass

	@overload
	def IHydroTanksResults(self, timeStepIndex: int) -> Dict[int,int]:
		"""The calculated pressure in the hydropenumatic tank. This result is based on the steady state Tank Calculation Model, however, if the tank is a Dipping Tube tank with a defined Variable Elevation Curve, this result is re-calculated to be representative of the dipping tube tank geometry. If the tank is simulated as a junction in steady state this result will be reported as N/A.

		Args:
			timeStepIndex(int): timeStepIndex

		Returns:
			Dict[int,int]: 
		"""
		pass

	@overload
	def IHydroTanksResults(self, ids: List[int], timeStepIndex: int) -> Dict[int,int]:
		"""No Description

		Args:
			ids(List[int]): ids
			timeStepIndex(int): timeStepIndex

		Returns:
			Dict[int,int]: 
		"""
		pass

	@overload
	def IHydroTanksResults(self) -> Dict[int,int]:
		"""The calculated liquid volume in the hydropneumatic tank. This result is based on the steady state Tank Calculation Model, however, if the tank is a Dipping Tube tank with a defined Variable Elevation Curve, this result is re-calculated to be representative of the dipping tube tank geometry. If the tank is simulated as a junction in steady state this result will be reported as N/A.

		Returns:
			Dict[int,int]: 
		"""
		pass

	@overload
	def IHydroTanksResults(self, timeStepIndex: int) -> Dict[int,int]:
		"""The calculated liquid volume in the hydropneumatic tank. This result is based on the steady state Tank Calculation Model, however, if the tank is a Dipping Tube tank with a defined Variable Elevation Curve, this result is re-calculated to be representative of the dipping tube tank geometry. If the tank is simulated as a junction in steady state this result will be reported as N/A.

		Args:
			timeStepIndex(int): timeStepIndex

		Returns:
			Dict[int,int]: 
		"""
		pass

	@overload
	def IHydroTanksResults(self, ids: List[int], timeStepIndex: int) -> Dict[int,int]:
		"""No Description

		Args:
			ids(List[int]): ids
			timeStepIndex(int): timeStepIndex

		Returns:
			Dict[int,int]: 
		"""
		pass

	@overload
	def IHydroTanksResults(self) -> Dict[int,int]:
		"""The ratio of the fluid volume in the tank to the calculated full volume of the tank. This result is based on the steady state Tank Calculation Model, however, if the tank is a Dipping Tube tank with a defined Variable Elevation Curve, this result is re-calculated to be representative of the dipping tube tank geometry. If the tank is simulated as a junction in steady state this result will be reported as N/A.

		Returns:
			Dict[int,int]: 
		"""
		pass

	@overload
	def IHydroTanksResults(self, timeStepIndex: int) -> Dict[int,int]:
		"""The ratio of the fluid volume in the tank to the calculated full volume of the tank. This result is based on the steady state Tank Calculation Model, however, if the tank is a Dipping Tube tank with a defined Variable Elevation Curve, this result is re-calculated to be representative of the dipping tube tank geometry. If the tank is simulated as a junction in steady state this result will be reported as N/A.

		Args:
			timeStepIndex(int): timeStepIndex

		Returns:
			Dict[int,int]: 
		"""
		pass

	@overload
	def IHydroTanksResults(self, ids: List[int], timeStepIndex: int) -> Dict[int,int]:
		"""No Description

		Args:
			ids(List[int]): ids
			timeStepIndex(int): timeStepIndex

		Returns:
			Dict[int,int]: 
		"""
		pass

	def MaximumTransientGasPressures(self) -> Dict[int,int]:
		"""Maximum gas pressure at hydropneumatic tank over the course of the transient simulation.

		Returns:
			Dict[int,int]: 
		"""
		pass

	def MinimumTransientGasPressures(self) -> Dict[int,int]:
		"""Minimum gas pressure at hydropneumatic tank over the course of the transient simulation.

		Returns:
			Dict[int,int]: 
		"""
		pass

	def MaximumTransientGasVolumes(self) -> Dict[int,int]:
		"""Maximum gas volume at hydropneumatic tank over the course of the transient simulation.

		Returns:
			Dict[int,int]: 
		"""
		pass

	def MinimumTransientGasVolumes(self) -> Dict[int,int]:
		"""Minimum gas volume at hydropneumatic tank over the course of the transient simulation.

		Returns:
			Dict[int,int]: 
		"""
		pass

	def MaximumTransientWaterLevels(self) -> Dict[int,int]:
		"""Maximum water level at hydropneumatic tank over the course of the transient simulation.

		Returns:
			Dict[int,int]: 
		"""
		pass

	def MinimumTransientWaterLevels(self) -> Dict[int,int]:
		"""Minimum water level at hydropneumatic tank over the course of the transient simulation.

		Returns:
			Dict[int,int]: 
		"""
		pass

class IHydropneumaticTankUnits(IBaseTankUnits):

	def __init__(self) -> None:
		"""Creating a new Instance of this class is not allowed


		Raises:
			Exception: if this class is instanciated
		"""
		raise Exception("Creating a new Instance of this class is not allowed")
		pass

	@property
	def VolumeUnit(self) -> IUnit:
		"""No Description

		Returns:
			IHydropneumaticTankUnits: 
		"""
		pass

	@property
	def DiameterUnit(self) -> IUnit:
		"""No Description

		Returns:
			IHydropneumaticTankUnits: 
		"""
		pass

	@property
	def GasExponentUnit(self) -> IUnit:
		"""No Description

		Returns:
			IHydropneumaticTankUnits: 
		"""
		pass

	@property
	def PressureUnit(self) -> IUnit:
		"""No Description

		Returns:
			IHydropneumaticTankUnits: 
		"""
		pass

	@property
	def LengthUnit(self) -> IUnit:
		"""No Description

		Returns:
			IHydropneumaticTankUnits: 
		"""
		pass

	@property
	def PercentUnit(self) -> IUnit:
		"""No Description

		Returns:
			IHydropneumaticTankUnits: 
		"""
		pass

class IHydropneumaticTank(IWaterNetworkElement[IHydropneumaticTanks, IHydropneumaticTank, IHydropneumaticTankUnits, IHydroTankInput, IHydroTankResults, IHydroTanksInput, IHydroTanksResults]):

	def __init__(self) -> None:
		"""Creating a new Instance of this class is not allowed


		Raises:
			Exception: if this class is instanciated
		"""
		raise Exception("Creating a new Instance of this class is not allowed")
		pass

class IHydropneumaticTanks(IWaterNetworkElements[IHydropneumaticTanks, IHydropneumaticTank, IHydropneumaticTankUnits, IHydroTankInput, IHydroTankResults, IHydroTanksInput, IHydroTanksResults]):

	def __init__(self) -> None:
		"""Creating a new Instance of this class is not allowed


		Raises:
			Exception: if this class is instanciated
		"""
		raise Exception("Creating a new Instance of this class is not allowed")
		pass

class IHammerNodeInput(IBaseNodeInput):

	def __init__(self) -> None:
		"""Creating a new Instance of this class is not allowed


		Raises:
			Exception: if this class is instanciated
		"""
		raise Exception("Creating a new Instance of this class is not allowed")
		pass

class IHammerNodesInput(IBaseNodesInput):

	def __init__(self) -> None:
		"""Creating a new Instance of this class is not allowed


		Raises:
			Exception: if this class is instanciated
		"""
		raise Exception("Creating a new Instance of this class is not allowed")
		pass

class IHammerNodeResults(IBaseNodeResults):

	def __init__(self) -> None:
		"""Creating a new Instance of this class is not allowed


		Raises:
			Exception: if this class is instanciated
		"""
		raise Exception("Creating a new Instance of this class is not allowed")
		pass

	@overload
	def IHammerNodeResults(self) -> Union[float, None]:
		"""Calculated pressure at node.

		Returns:
			Nullable: 
		"""
		pass

	@overload
	def IHammerNodeResults(self, timeStepIndex: int) -> Union[float, None]:
		"""Calculated pressure at node.

		Args:
			timeStepIndex(int): timeStepIndex

		Returns:
			Nullable: 
		"""
		pass

	@overload
	def IHammerNodeResults(self) -> Union[float, None]:
		"""Calculated pressure head at node.

		Returns:
			Nullable: 
		"""
		pass

	@overload
	def IHammerNodeResults(self, timeStepIndex: int) -> Union[float, None]:
		"""Calculated pressure head at node.

		Args:
			timeStepIndex(int): timeStepIndex

		Returns:
			Nullable: 
		"""
		pass

	def Pressures(self) -> array(Union[float, None]):
		"""Calculated pressure at node.

		Returns:
			array(): 
		"""
		pass

	def PressureHeads(self) -> array(Union[float, None]):
		"""Calculated pressure head at node.

		Returns:
			array(): 
		"""
		pass

class IHammerNodesResults(IBaseNodesResults):

	def __init__(self) -> None:
		"""Creating a new Instance of this class is not allowed


		Raises:
			Exception: if this class is instanciated
		"""
		raise Exception("Creating a new Instance of this class is not allowed")
		pass

	@overload
	def IHammerNodesResults(self) -> Dict[int,int]:
		"""Calculated pressure at node.

		Returns:
			Dict[int,int]: 
		"""
		pass

	@overload
	def IHammerNodesResults(self, timeStepIndex: int) -> Dict[int,int]:
		"""Calculated pressure at node.

		Args:
			timeStepIndex(int): timeStepIndex

		Returns:
			Dict[int,int]: 
		"""
		pass

	@overload
	def IHammerNodesResults(self, ids: List[int], timeStepIndex: int) -> Dict[int,int]:
		"""No Description

		Args:
			ids(List[int]): ids
			timeStepIndex(int): timeStepIndex

		Returns:
			Dict[int,int]: 
		"""
		pass

	@overload
	def IHammerNodesResults(self) -> Dict[int,int]:
		"""Calculated pressure head at node.

		Returns:
			Dict[int,int]: 
		"""
		pass

	@overload
	def IHammerNodesResults(self, timeStepIndex: int) -> Dict[int,int]:
		"""Calculated pressure head at node.

		Args:
			timeStepIndex(int): timeStepIndex

		Returns:
			Dict[int,int]: 
		"""
		pass

	@overload
	def IHammerNodesResults(self, ids: List[int], timeStepIndex: int) -> Dict[int,int]:
		"""No Description

		Args:
			ids(List[int]): ids
			timeStepIndex(int): timeStepIndex

		Returns:
			Dict[int,int]: 
		"""
		pass

class IHammerNodeUnits(IBaseNodeUnits):

	def __init__(self) -> None:
		"""Creating a new Instance of this class is not allowed


		Raises:
			Exception: if this class is instanciated
		"""
		raise Exception("Creating a new Instance of this class is not allowed")
		pass

	@property
	def PressureUnit(self) -> IUnit:
		"""No Description

		Returns:
			IHammerNodeUnits: 
		"""
		pass

	@property
	def PressureHeadUnit(self) -> IUnit:
		"""No Description

		Returns:
			IHammerNodeUnits: 
		"""
		pass

class IFlowPatternCollection(ICollectionElements[IFlowPatterns, IFlowPattern, IFlowPatternUnits]):

	def __init__(self) -> None:
		"""Creating a new Instance of this class is not allowed


		Raises:
			Exception: if this class is instanciated
		"""
		raise Exception("Creating a new Instance of this class is not allowed")
		pass

class IFlowPatterns(ICollection[IFlowPattern]):

	def __init__(self) -> None:
		"""Creating a new Instance of this class is not allowed


		Raises:
			Exception: if this class is instanciated
		"""
		raise Exception("Creating a new Instance of this class is not allowed")
		pass

	def Add(self, time: float, flow: float) -> IFlowPattern:
		"""Adds a new row to the collection (in-memory) with the provided time and flow values.

		Args:
			time(float): time
			flow(float): flow

		Returns:
			IFlowPattern: 
		"""
		pass

class IFlowPattern(ICollectionElement):

	def __init__(self) -> None:
		"""Creating a new Instance of this class is not allowed


		Raises:
			Exception: if this class is instanciated
		"""
		raise Exception("Creating a new Instance of this class is not allowed")
		pass

	@property
	def Time(self) -> float:
		"""No Description

		Returns:
			IFlowPattern: 
		"""
		pass

	@property
	def Flow(self) -> float:
		"""No Description

		Returns:
			IFlowPattern: 
		"""
		pass

	@Time.setter
	def Time(self, time: float) -> None:
		pass

	@Flow.setter
	def Flow(self, flow: float) -> None:
		pass

class IFlowPatternUnits(IElementUnits):

	def __init__(self) -> None:
		"""Creating a new Instance of this class is not allowed


		Raises:
			Exception: if this class is instanciated
		"""
		raise Exception("Creating a new Instance of this class is not allowed")
		pass

	@property
	def TimeUnit(self) -> IUnit:
		"""No Description

		Returns:
			IFlowPatternUnits: 
		"""
		pass

	@property
	def FlowUnit(self) -> IUnit:
		"""No Description

		Returns:
			IFlowPatternUnits: 
		"""
		pass

class IHeadPatternCollection(ICollectionElements[IHeadPatterns, IHeadPattern, IHeadPatternUnits]):

	def __init__(self) -> None:
		"""Creating a new Instance of this class is not allowed


		Raises:
			Exception: if this class is instanciated
		"""
		raise Exception("Creating a new Instance of this class is not allowed")
		pass

class IHeadPatterns(ICollection[IHeadPattern]):

	def __init__(self) -> None:
		"""Creating a new Instance of this class is not allowed


		Raises:
			Exception: if this class is instanciated
		"""
		raise Exception("Creating a new Instance of this class is not allowed")
		pass

	def Add(self, time: float, head: float) -> IHeadPattern:
		"""No Description

		Args:
			time(float): time
			head(float): head

		Returns:
			IHeadPattern: 
		"""
		pass

class IHeadPattern(ICollectionElement):

	def __init__(self) -> None:
		"""Creating a new Instance of this class is not allowed


		Raises:
			Exception: if this class is instanciated
		"""
		raise Exception("Creating a new Instance of this class is not allowed")
		pass

	@property
	def Time(self) -> float:
		"""No Description

		Returns:
			IHeadPattern: 
		"""
		pass

	@property
	def Head(self) -> float:
		"""No Description

		Returns:
			IHeadPattern: 
		"""
		pass

	@Time.setter
	def Time(self, time: float) -> None:
		pass

	@Head.setter
	def Head(self, head: float) -> None:
		pass

class IHeadPatternUnits(IElementUnits):

	def __init__(self) -> None:
		"""Creating a new Instance of this class is not allowed


		Raises:
			Exception: if this class is instanciated
		"""
		raise Exception("Creating a new Instance of this class is not allowed")
		pass

	@property
	def TimeUnit(self) -> IUnit:
		"""No Description

		Returns:
			IHeadPatternUnits: 
		"""
		pass

	@property
	def HeadUnit(self) -> IUnit:
		"""No Description

		Returns:
			IHeadPatternUnits: 
		"""
		pass

class IPeriodicHeadFlowInput(IHammerNodeInput):

	def __init__(self) -> None:
		"""Creating a new Instance of this class is not allowed


		Raises:
			Exception: if this class is instanciated
		"""
		raise Exception("Creating a new Instance of this class is not allowed")
		pass

	@property
	def Sinusoidal(self) -> bool:
		"""No Description

		Returns:
			IPeriodicHeadFlowInput: 
		"""
		pass

	@property
	def HeadMeanValue(self) -> float:
		"""No Description

		Returns:
			IPeriodicHeadFlowInput: 
		"""
		pass

	@property
	def HeadAmplitude(self) -> float:
		"""No Description

		Returns:
			IPeriodicHeadFlowInput: 
		"""
		pass

	@property
	def Phase(self) -> float:
		"""No Description

		Returns:
			IPeriodicHeadFlowInput: 
		"""
		pass

	@property
	def Period(self) -> float:
		"""No Description

		Returns:
			IPeriodicHeadFlowInput: 
		"""
		pass

	@property
	def FlowMeanValue(self) -> float:
		"""No Description

		Returns:
			IPeriodicHeadFlowInput: 
		"""
		pass

	@property
	def FlowAmplitude(self) -> float:
		"""No Description

		Returns:
			IPeriodicHeadFlowInput: 
		"""
		pass

	@property
	def TransientParameter(self) -> TransientParameterType:
		"""No Description

		Returns:
			IPeriodicHeadFlowInput: 
		"""
		pass

	@property
	def FlowPatternCollection(self) -> IFlowPatternCollection:
		"""No Description

		Returns:
			IPeriodicHeadFlowInput: 
		"""
		pass

	@property
	def HeadPatternCollection(self) -> IHeadPatternCollection:
		"""No Description

		Returns:
			IPeriodicHeadFlowInput: 
		"""
		pass

	@Sinusoidal.setter
	def Sinusoidal(self, sinusoidal: bool) -> None:
		pass

	@HeadMeanValue.setter
	def HeadMeanValue(self, headmeanvalue: float) -> None:
		pass

	@HeadAmplitude.setter
	def HeadAmplitude(self, headamplitude: float) -> None:
		pass

	@Phase.setter
	def Phase(self, phase: float) -> None:
		pass

	@Period.setter
	def Period(self, period: float) -> None:
		pass

	@FlowMeanValue.setter
	def FlowMeanValue(self, flowmeanvalue: float) -> None:
		pass

	@FlowAmplitude.setter
	def FlowAmplitude(self, flowamplitude: float) -> None:
		pass

	@TransientParameter.setter
	def TransientParameter(self, transientparameter: TransientParameterType) -> None:
		pass

class IPeriodicHeadFlowsInput(IHammerNodesInput):

	def __init__(self) -> None:
		"""Creating a new Instance of this class is not allowed


		Raises:
			Exception: if this class is instanciated
		"""
		raise Exception("Creating a new Instance of this class is not allowed")
		pass

	@overload
	def IPeriodicHeadFlowsInput(self) -> Dict[int,int]:
		"""If sinusoidal, then mean value, amplitude and phase are entered; otherwise, a table of values is required. A sinusoidal quantity X has the form: X = X0 + A sin( 2 * PI * t / T + Phase ).

		Returns:
			Dict[int,int]: 
		"""
		pass

	@overload
	def IPeriodicHeadFlowsInput(self, ids: List[int]) -> Dict[int,int]:
		"""No Description

		Args:
			ids(List[int]): ids

		Returns:
			Dict[int,int]: 
		"""
		pass

	@overload
	def IPeriodicHeadFlowsInput(self) -> Dict[int,int]:
		"""The mean head value. Required only if sinusoidal data specified.

		Returns:
			Dict[int,int]: 
		"""
		pass

	@overload
	def IPeriodicHeadFlowsInput(self, ids: List[int]) -> Dict[int,int]:
		"""No Description

		Args:
			ids(List[int]): ids

		Returns:
			Dict[int,int]: 
		"""
		pass

	@overload
	def IPeriodicHeadFlowsInput(self) -> Dict[int,int]:
		"""The amplitude of the sinusoidal head curve. Required only if sinusoidal data specified.

		Returns:
			Dict[int,int]: 
		"""
		pass

	@overload
	def IPeriodicHeadFlowsInput(self, ids: List[int]) -> Dict[int,int]:
		"""No Description

		Args:
			ids(List[int]): ids

		Returns:
			Dict[int,int]: 
		"""
		pass

	@overload
	def IPeriodicHeadFlowsInput(self) -> Dict[int,int]:
		"""Phase of the sinusoidal flow or head curve. Default option is 0 such that periodic component of head or flow is zero at time zero.

		Returns:
			Dict[int,int]: 
		"""
		pass

	@overload
	def IPeriodicHeadFlowsInput(self, ids: List[int]) -> Dict[int,int]:
		"""No Description

		Args:
			ids(List[int]): ids

		Returns:
			Dict[int,int]: 
		"""
		pass

	@overload
	def IPeriodicHeadFlowsInput(self) -> Dict[int,int]:
		"""Oscillation period of the sinusoidal flow or head curve (must be positive), or the period after which a tabular flow or head pattern repeats.

		Returns:
			Dict[int,int]: 
		"""
		pass

	@overload
	def IPeriodicHeadFlowsInput(self, ids: List[int]) -> Dict[int,int]:
		"""No Description

		Args:
			ids(List[int]): ids

		Returns:
			Dict[int,int]: 
		"""
		pass

	@overload
	def IPeriodicHeadFlowsInput(self) -> Dict[int,int]:
		"""The mean flow value. Required only if sinusoidal data specified.

		Returns:
			Dict[int,int]: 
		"""
		pass

	@overload
	def IPeriodicHeadFlowsInput(self, ids: List[int]) -> Dict[int,int]:
		"""No Description

		Args:
			ids(List[int]): ids

		Returns:
			Dict[int,int]: 
		"""
		pass

	@overload
	def IPeriodicHeadFlowsInput(self) -> Dict[int,int]:
		"""The amplitude of the sinusoidal flow curve. Required only if sinusoidal data specified.

		Returns:
			Dict[int,int]: 
		"""
		pass

	@overload
	def IPeriodicHeadFlowsInput(self, ids: List[int]) -> Dict[int,int]:
		"""No Description

		Args:
			ids(List[int]): ids

		Returns:
			Dict[int,int]: 
		"""
		pass

	@overload
	def IPeriodicHeadFlowsInput(self) -> Dict[int,int]:
		"""Specifies whether the periodic head/flow element is used to simulate a periodic head or periodic flow.

		Returns:
			Dict[int,int]: 
		"""
		pass

	@overload
	def IPeriodicHeadFlowsInput(self, ids: List[int]) -> Dict[int,int]:
		"""No Description

		Args:
			ids(List[int]): ids

		Returns:
			Dict[int,int]: 
		"""
		pass

class IPeriodicHeadFlowResults(IHammerNodeResults):

	def __init__(self) -> None:
		"""Creating a new Instance of this class is not allowed


		Raises:
			Exception: if this class is instanciated
		"""
		raise Exception("Creating a new Instance of this class is not allowed")
		pass

	@overload
	def IPeriodicHeadFlowResults(self) -> Union[float, None]:
		"""Calculated discharge from the node.

		Returns:
			Nullable: 
		"""
		pass

	@overload
	def IPeriodicHeadFlowResults(self, timeStepIndex: int) -> Union[float, None]:
		"""Calculated discharge from the node.

		Args:
			timeStepIndex(int): timeStepIndex

		Returns:
			Nullable: 
		"""
		pass

	def CalculatedDischarges(self) -> array(Union[float, None]):
		"""Calculated discharge from the node.

		Returns:
			array(): 
		"""
		pass

class IPeriodicHeadFlowsResults(IHammerNodesResults):

	def __init__(self) -> None:
		"""Creating a new Instance of this class is not allowed


		Raises:
			Exception: if this class is instanciated
		"""
		raise Exception("Creating a new Instance of this class is not allowed")
		pass

	@overload
	def IPeriodicHeadFlowsResults(self) -> Dict[int,int]:
		"""Calculated discharge from the node.

		Returns:
			Dict[int,int]: 
		"""
		pass

	@overload
	def IPeriodicHeadFlowsResults(self, timeStepIndex: int) -> Dict[int,int]:
		"""Calculated discharge from the node.

		Args:
			timeStepIndex(int): timeStepIndex

		Returns:
			Dict[int,int]: 
		"""
		pass

	@overload
	def IPeriodicHeadFlowsResults(self, ids: List[int], timeStepIndex: int) -> Dict[int,int]:
		"""No Description

		Args:
			ids(List[int]): ids
			timeStepIndex(int): timeStepIndex

		Returns:
			Dict[int,int]: 
		"""
		pass

class IPeriodicHeadFlowUnits(IHammerNodeUnits):

	def __init__(self) -> None:
		"""Creating a new Instance of this class is not allowed


		Raises:
			Exception: if this class is instanciated
		"""
		raise Exception("Creating a new Instance of this class is not allowed")
		pass

	@property
	def LengthUnit(self) -> IUnit:
		"""No Description

		Returns:
			IPeriodicHeadFlowUnits: 
		"""
		pass

	@property
	def AngleUnit(self) -> IUnit:
		"""No Description

		Returns:
			IPeriodicHeadFlowUnits: 
		"""
		pass

	@property
	def PeriodUnit(self) -> IUnit:
		"""No Description

		Returns:
			IPeriodicHeadFlowUnits: 
		"""
		pass

	@property
	def FlowUnit(self) -> IUnit:
		"""No Description

		Returns:
			IPeriodicHeadFlowUnits: 
		"""
		pass

class IPeriodicHeadFlows(IWaterNetworkElements[IPeriodicHeadFlows, IPeriodicHeadFlow, IPeriodicHeadFlowUnits, IPeriodicHeadFlowInput, IPeriodicHeadFlowResults, IPeriodicHeadFlowsInput, IPeriodicHeadFlowsResults]):

	def __init__(self) -> None:
		"""Creating a new Instance of this class is not allowed


		Raises:
			Exception: if this class is instanciated
		"""
		raise Exception("Creating a new Instance of this class is not allowed")
		pass

class IPeriodicHeadFlow(IWaterNetworkElement[IPeriodicHeadFlows, IPeriodicHeadFlow, IPeriodicHeadFlowUnits, IPeriodicHeadFlowInput, IPeriodicHeadFlowResults, IPeriodicHeadFlowsInput, IPeriodicHeadFlowsResults]):

	def __init__(self) -> None:
		"""Creating a new Instance of this class is not allowed


		Raises:
			Exception: if this class is instanciated
		"""
		raise Exception("Creating a new Instance of this class is not allowed")
		pass

class IAirValveInput(IHammerNodeInput):

	def __init__(self) -> None:
		"""Creating a new Instance of this class is not allowed


		Raises:
			Exception: if this class is instanciated
		"""
		raise Exception("Creating a new Instance of this class is not allowed")
		pass

	@property
	def InitialAirvolume(self) -> float:
		"""No Description

		Returns:
			IAirValveInput: 
		"""
		pass

	@property
	def SmallAirOutflowOrificeDiameter(self) -> float:
		"""No Description

		Returns:
			IAirValveInput: 
		"""
		pass

	@property
	def TransitionVolume(self) -> float:
		"""No Description

		Returns:
			IAirValveInput: 
		"""
		pass

	@property
	def LargeAirOutflowOrificeDiameter(self) -> float:
		"""No Description

		Returns:
			IAirValveInput: 
		"""
		pass

	@property
	def AirInflowOrificeDiameter(self) -> float:
		"""No Description

		Returns:
			IAirValveInput: 
		"""
		pass

	@property
	def AirOutflowOrificeDiameter(self) -> float:
		"""No Description

		Returns:
			IAirValveInput: 
		"""
		pass

	@property
	def TransitionPressure(self) -> float:
		"""No Description

		Returns:
			IAirValveInput: 
		"""
		pass

	@property
	def SmallAirFlowCurve(self) -> IAirFlowCurve:
		"""No Description

		Returns:
			IAirValveInput: 
		"""
		pass

	@property
	def LargeAirFlowCurve(self) -> IAirFlowCurve:
		"""No Description

		Returns:
			IAirValveInput: 
		"""
		pass

	@property
	def AirValveType(self) -> AirValveTypeEnum:
		"""No Description

		Returns:
			IAirValveInput: 
		"""
		pass

	@property
	def AirValveTransitionType(self) -> AirValveTransitionType:
		"""No Description

		Returns:
			IAirValveInput: 
		"""
		pass

	@property
	def TimeToClose(self) -> float:
		"""No Description

		Returns:
			IAirValveInput: 
		"""
		pass

	@property
	def ReportPeriod(self) -> int:
		"""No Description

		Returns:
			IAirValveInput: 
		"""
		pass

	@property
	def TreatAirValveAsJunction(self) -> bool:
		"""No Description

		Returns:
			IAirValveInput: 
		"""
		pass

	@property
	def InflowOrificeAirFlowCurve(self) -> IAirFlowCurve:
		"""No Description

		Returns:
			IAirValveInput: 
		"""
		pass

	@property
	def OutflowOrificeAirFlowCurve(self) -> IAirFlowCurve:
		"""No Description

		Returns:
			IAirValveInput: 
		"""
		pass

	@property
	def AirFlowCalculationMethod(self) -> AirFlowCalculationMethod:
		"""No Description

		Returns:
			IAirValveInput: 
		"""
		pass

	@InitialAirvolume.setter
	def InitialAirvolume(self, initialairvolume: float) -> None:
		pass

	@SmallAirOutflowOrificeDiameter.setter
	def SmallAirOutflowOrificeDiameter(self, smallairoutfloworificediameter: float) -> None:
		pass

	@TransitionVolume.setter
	def TransitionVolume(self, transitionvolume: float) -> None:
		pass

	@LargeAirOutflowOrificeDiameter.setter
	def LargeAirOutflowOrificeDiameter(self, largeairoutfloworificediameter: float) -> None:
		pass

	@AirInflowOrificeDiameter.setter
	def AirInflowOrificeDiameter(self, airinfloworificediameter: float) -> None:
		pass

	@AirOutflowOrificeDiameter.setter
	def AirOutflowOrificeDiameter(self, airoutfloworificediameter: float) -> None:
		pass

	@TransitionPressure.setter
	def TransitionPressure(self, transitionpressure: float) -> None:
		pass

	@SmallAirFlowCurve.setter
	def SmallAirFlowCurve(self, smallairflowcurve: IAirFlowCurve) -> None:
		pass

	@LargeAirFlowCurve.setter
	def LargeAirFlowCurve(self, largeairflowcurve: IAirFlowCurve) -> None:
		pass

	@AirValveType.setter
	def AirValveType(self, airvalvetype: AirValveTypeEnum) -> None:
		pass

	@AirValveTransitionType.setter
	def AirValveTransitionType(self, airvalvetransitiontype: AirValveTransitionType) -> None:
		pass

	@TimeToClose.setter
	def TimeToClose(self, timetoclose: float) -> None:
		pass

	@ReportPeriod.setter
	def ReportPeriod(self, reportperiod: int) -> None:
		pass

	@TreatAirValveAsJunction.setter
	def TreatAirValveAsJunction(self, treatairvalveasjunction: bool) -> None:
		pass

	@InflowOrificeAirFlowCurve.setter
	def InflowOrificeAirFlowCurve(self, infloworificeairflowcurve: IAirFlowCurve) -> None:
		pass

	@OutflowOrificeAirFlowCurve.setter
	def OutflowOrificeAirFlowCurve(self, outfloworificeairflowcurve: IAirFlowCurve) -> None:
		pass

	@AirFlowCalculationMethod.setter
	def AirFlowCalculationMethod(self, airflowcalculationmethod: AirFlowCalculationMethod) -> None:
		pass

class IAirValvesInput(IHammerNodesInput):

	def __init__(self) -> None:
		"""Creating a new Instance of this class is not allowed


		Raises:
			Exception: if this class is instanciated
		"""
		raise Exception("Creating a new Instance of this class is not allowed")
		pass

	def InitialAirVolumes(self) -> Dict[int,int]:
		"""Volume of air near the valve at initial time - default is zero. If volume is non-zero, then pressure must be zero.

		Returns:
			Dict[int,int]: 
		"""
		pass

	def SmallAirOutflowOrificeDiameters(self) -> Dict[int,int]:
		"""Refers to the discharge of air when the air volume is less than the transition volume (TV), or the air pressure is greater than the transition pressure (TP). This diameter is typically small enough for the injected air to be compressed.

		Returns:
			Dict[int,int]: 
		"""
		pass

	def TransitionVolumes(self) -> Dict[int,int]:
		"""This is the local volume of air at the air valve below which the transient solver switches from using the large air outflow orifice to the small air outflow orifice (in order to minimize transients). This volume often corresponds to the volume of the body of the air valve.

		Returns:
			Dict[int,int]: 
		"""
		pass

	def LargeAirOutflowOrificeDiameters(self) -> Dict[int,int]:
		"""Refers to the discharge of air when the air volume is greater than or equal to the transition volume (TV), or the air pressure is less than or equal to the transition pressure (TP). This diameter is typically larger than the diameter when the volume is less than the TV or greater than the TP.

		Returns:
			Dict[int,int]: 
		"""
		pass

	def AirInflowOrificeDiameters(self) -> Dict[int,int]:
		"""Diameter of orifice through which air is injected into the pipeline. This diameter should be large enough to allow free entry of air into the pipeline.

		Returns:
			Dict[int,int]: 
		"""
		pass

	def AirOutflowOrificeDiameters(self) -> Dict[int,int]:
		"""Diameter of the orifice through which air is expelled from the pipeline.

		Returns:
			Dict[int,int]: 
		"""
		pass

	def TransitionPressures(self) -> Dict[int,int]:
		"""This is the local internal system air pressure at the air valve above which the transient solver will switch from using the large air outflow orifice to the small air outflow orifice (in order to minimize transients).

		Returns:
			Dict[int,int]: 
		"""
		pass

	def SmallAirflowCurves(self) -> Dict[int,int]:
		"""Curve that defines discharge of air when the air volume is less than the transition volume (TV), or the air pressure is greater than the transition pressure (TP).

		Returns:
			Dict[int,int]: 
		"""
		pass

	def LargeAirFlowCurves(self) -> Dict[int,int]:
		"""Curve that defines discharge of air when the air volume is greater than or equal to the transition volume (TV), or the air pressure is less than or equal to the transition pressure (TP).

		Returns:
			Dict[int,int]: 
		"""
		pass

	def AirValveTypes(self) -> Dict[int,int]:
		"""Select the type of Air Valve to simulate. Choices are Slow Closing, Double Acting, Triple Acting and Vacuum Breaker. The choice you make will only affect the transient engine.

		Returns:
			Dict[int,int]: 
		"""
		pass

	def AirValveTransitionTypes(self) -> Dict[int,int]:
		"""Users can select whether the transient solver switches from the large air outflow orifice to the small air outflow orifice based on a Transition Volume or a Transition Pressure.

		Returns:
			Dict[int,int]: 
		"""
		pass

	def TimeToClose(self) -> Dict[int,int]:
		"""For a slow-closing air valve, the valve starts to close linearly with respect to area once air begins to exit the pipe. If air subsequently re-enters, then the air valve opens fully again. For a valve with linear area change, the valve will close linearly over this time, starting at the beginning of the simulation if this value is greater than zero. If this value equals zero a valve with linear area change will close when reverse flow is first sensed and will remain closed for the remainder of the simulation. For an air valve, adiabatic compression (i.e., gas law exponent = 1.4) is assumed.

		Returns:
			Dict[int,int]: 
		"""
		pass

	def ReportPeriods(self) -> Dict[int,int]:
		"""Number of time steps between successive printouts of operation. By default, this printout is suppressed.

		Returns:
			Dict[int,int]: 
		"""
		pass

	def TreatAirValvesAsJunctions(self) -> Dict[int,int]:
		"""Specifies whether or not to treat the air-valve as a junction element in steady state and EPS simulations. If false, the valve may allow part full flow subject to the prevailing hydraulic conditions.

		Returns:
			Dict[int,int]: 
		"""
		pass

	def InflowOrificeAirFlowCurves(self) -> Dict[int,int]:
		"""The curve that defines the rate of air inflow (a ?free air? rate, measured at atmospheric pressure) into the tank versus the differential pressure across the air valve.

		Returns:
			Dict[int,int]: 
		"""
		pass

	def OutflowOrificeAirFlowCurves(self) -> Dict[int,int]:
		"""The curve that defines the rate of air outflow (a ?free air? rate, measured at atmospheric pressure) out of the tank versus the differential pressure across the air valve.

		Returns:
			Dict[int,int]: 
		"""
		pass

	def AirFlowCalculationMethods(self) -> Dict[int,int]:
		"""Specify whether the air valve air flow rate is determined by user-entered curves of pressure vs. air flow rate, or whether it is calculated based on a user-entered orifice diameter (not applicable for a sealed hydropneumatic tank).

		Returns:
			Dict[int,int]: 
		"""
		pass

class IAirValveResults(IHammerNodeResults):

	def __init__(self) -> None:
		"""Creating a new Instance of this class is not allowed


		Raises:
			Exception: if this class is instanciated
		"""
		raise Exception("Creating a new Instance of this class is not allowed")
		pass

class IAirValvesResults(IHammerNodesResults):

	def __init__(self) -> None:
		"""Creating a new Instance of this class is not allowed


		Raises:
			Exception: if this class is instanciated
		"""
		raise Exception("Creating a new Instance of this class is not allowed")
		pass

class IAirValveUnits(IHammerNodeUnits):

	def __init__(self) -> None:
		"""Creating a new Instance of this class is not allowed


		Raises:
			Exception: if this class is instanciated
		"""
		raise Exception("Creating a new Instance of this class is not allowed")
		pass

	@property
	def VolumeUnit(self) -> IUnit:
		"""No Description

		Returns:
			IAirValveUnits: 
		"""
		pass

	@property
	def DiameterUnit(self) -> IUnit:
		"""No Description

		Returns:
			IAirValveUnits: 
		"""
		pass

	@property
	def TimeTocloseUnit(self) -> IUnit:
		"""No Description

		Returns:
			IAirValveUnits: 
		"""
		pass

class IAirValve(IWaterNetworkElement[IAirValves, IAirValve, IAirValveUnits, IAirValveInput, IAirValveResults, IAirValvesInput, IAirValvesResults]):

	def __init__(self) -> None:
		"""Creating a new Instance of this class is not allowed


		Raises:
			Exception: if this class is instanciated
		"""
		raise Exception("Creating a new Instance of this class is not allowed")
		pass

class IAirValves(IWaterNetworkElements[IAirValves, IAirValve, IAirValveUnits, IAirValveInput, IAirValveResults, IAirValvesInput, IAirValvesResults]):

	def __init__(self) -> None:
		"""Creating a new Instance of this class is not allowed


		Raises:
			Exception: if this class is instanciated
		"""
		raise Exception("Creating a new Instance of this class is not allowed")
		pass

class ISurgeValveInput(IHammerNodeInput):

	def __init__(self) -> None:
		"""Creating a new Instance of this class is not allowed


		Raises:
			Exception: if this class is instanciated
		"""
		raise Exception("Creating a new Instance of this class is not allowed")
		pass

	@property
	def SavDiameter(self) -> float:
		"""No Description

		Returns:
			ISurgeValveInput: 
		"""
		pass

	@property
	def SavThresholdPressure(self) -> float:
		"""No Description

		Returns:
			ISurgeValveInput: 
		"""
		pass

	@property
	def TimeForSAVToOpen(self) -> float:
		"""No Description

		Returns:
			ISurgeValveInput: 
		"""
		pass

	@property
	def TimeSAVStaysFullyOpen(self) -> float:
		"""No Description

		Returns:
			ISurgeValveInput: 
		"""
		pass

	@property
	def TimeForSAVToClose(self) -> float:
		"""No Description

		Returns:
			ISurgeValveInput: 
		"""
		pass

	@property
	def SavDischargeCoefficient(self) -> float:
		"""No Description

		Returns:
			ISurgeValveInput: 
		"""
		pass

	@property
	def SrvDiameter(self) -> float:
		"""No Description

		Returns:
			ISurgeValveInput: 
		"""
		pass

	@property
	def SrvThresholdPressure(self) -> float:
		"""No Description

		Returns:
			ISurgeValveInput: 
		"""
		pass

	@property
	def SrvSpringConstant(self) -> float:
		"""No Description

		Returns:
			ISurgeValveInput: 
		"""
		pass

	@property
	def TimeForSRVToOpen(self) -> float:
		"""No Description

		Returns:
			ISurgeValveInput: 
		"""
		pass

	@property
	def TimeForSRVToClose(self) -> float:
		"""No Description

		Returns:
			ISurgeValveInput: 
		"""
		pass

	@property
	def SrvDischargeCoefficient(self) -> float:
		"""No Description

		Returns:
			ISurgeValveInput: 
		"""
		pass

	@property
	def SavSrvType(self) -> SAV_SRVTypeEnum:
		"""No Description

		Returns:
			ISurgeValveInput: 
		"""
		pass

	@property
	def SavType(self) -> SAVValveTypeEnum:
		"""No Description

		Returns:
			ISurgeValveInput: 
		"""
		pass

	@property
	def SavClosureTriggerType(self) -> SavClosureTriggerEnum:
		"""No Description

		Returns:
			ISurgeValveInput: 
		"""
		pass

	@property
	def SrvControlType(self) -> SRVControlTypeEnum:
		"""No Description

		Returns:
			ISurgeValveInput: 
		"""
		pass

	@property
	def SrvValveType(self) -> SRVValveTypeEnum:
		"""No Description

		Returns:
			ISurgeValveInput: 
		"""
		pass

	@SavDiameter.setter
	def SavDiameter(self, savdiameter: float) -> None:
		pass

	@SavThresholdPressure.setter
	def SavThresholdPressure(self, savthresholdpressure: float) -> None:
		pass

	@TimeForSAVToOpen.setter
	def TimeForSAVToOpen(self, timeforsavtoopen: float) -> None:
		pass

	@TimeSAVStaysFullyOpen.setter
	def TimeSAVStaysFullyOpen(self, timesavstaysfullyopen: float) -> None:
		pass

	@TimeForSAVToClose.setter
	def TimeForSAVToClose(self, timeforsavtoclose: float) -> None:
		pass

	@SavDischargeCoefficient.setter
	def SavDischargeCoefficient(self, savdischargecoefficient: float) -> None:
		pass

	@SrvDiameter.setter
	def SrvDiameter(self, srvdiameter: float) -> None:
		pass

	@SrvThresholdPressure.setter
	def SrvThresholdPressure(self, srvthresholdpressure: float) -> None:
		pass

	@SrvSpringConstant.setter
	def SrvSpringConstant(self, srvspringconstant: float) -> None:
		pass

	@TimeForSRVToOpen.setter
	def TimeForSRVToOpen(self, timeforsrvtoopen: float) -> None:
		pass

	@TimeForSRVToClose.setter
	def TimeForSRVToClose(self, timeforsrvtoclose: float) -> None:
		pass

	@SrvDischargeCoefficient.setter
	def SrvDischargeCoefficient(self, srvdischargecoefficient: float) -> None:
		pass

	@SavSrvType.setter
	def SavSrvType(self, savsrvtype: SAV_SRVTypeEnum) -> None:
		pass

	@SavType.setter
	def SavType(self, savtype: SAVValveTypeEnum) -> None:
		pass

	@SavClosureTriggerType.setter
	def SavClosureTriggerType(self, savclosuretriggertype: SavClosureTriggerEnum) -> None:
		pass

	@SrvControlType.setter
	def SrvControlType(self, srvcontroltype: SRVControlTypeEnum) -> None:
		pass

	@SrvValveType.setter
	def SrvValveType(self, srvvalvetype: SRVValveTypeEnum) -> None:
		pass

class ISurgeValvesInput(IHammerNodesInput):

	def __init__(self) -> None:
		"""Creating a new Instance of this class is not allowed


		Raises:
			Exception: if this class is instanciated
		"""
		raise Exception("Creating a new Instance of this class is not allowed")
		pass

	def SavDiameter(self) -> Dict[int,int]:
		"""The valve's characteristics are determined by its Cv and type, so that the diameter is only used for descriptive purposes.

		Returns:
			Dict[int,int]: 
		"""
		pass

	def SavThresholdPressure(self) -> Dict[int,int]:
		"""Pressure below which the SAV opens.

		Returns:
			Dict[int,int]: 
		"""
		pass

	def TimeForSAVToOpen(self) -> Dict[int,int]:
		"""Time for the SAV to open fully after being triggered.

		Returns:
			Dict[int,int]: 
		"""
		pass

	def TimeSAVStaysFullyOpen(self) -> Dict[int,int]:
		"""Time that SAV remains fully open (i.e., time between the end of the opening phase and the start of the closing phase).

		Returns:
			Dict[int,int]: 
		"""
		pass

	def TimeForSAVToClose(self) -> Dict[int,int]:
		"""Time for the SAV to close fully, measured from the time that it was completely open.

		Returns:
			Dict[int,int]: 
		"""
		pass

	def SavDischargeCoefficient(self) -> Dict[int,int]:
		"""Discharge coefficient, Cv, is defined as: Flow / (Pressure Drop) ^ 0.5.

		Returns:
			Dict[int,int]: 
		"""
		pass

	def SrvDiameter(self) -> Dict[int,int]:
		"""The diameter of the SRV.

		Returns:
			Dict[int,int]: 
		"""
		pass

	def SrvThresholdPressure(self) -> Dict[int,int]:
		"""Pressure above which the SRV opens.

		Returns:
			Dict[int,int]: 
		"""
		pass

	def SrvSpringConstant(self) -> Dict[int,int]:
		"""Change in restoring force of the return spring per unit lift off seat. A possible value is 150 lb/in. (26.27 N/mm).

		Returns:
			Dict[int,int]: 
		"""
		pass

	def TimeForSRVToOpen(self) -> Dict[int,int]:
		"""Time for the SRV to open fully from fully closed position.

		Returns:
			Dict[int,int]: 
		"""
		pass

	def TimeForSRVToClose(self) -> Dict[int,int]:
		"""Time for SRV to close fully from fully open opsition.

		Returns:
			Dict[int,int]: 
		"""
		pass

	def SrvDischargeCoefficient(self) -> Dict[int,int]:
		"""Discharge coefficient of SRV at fully opening. it is defined as: Flow / (Pressure Drop) ^ 0.5.

		Returns:
			Dict[int,int]: 
		"""
		pass

	def SavSrvType(self) -> Dict[int,int]:
		"""The type of SAV/SRV valve to simulate in the transient engine.%n-SAV (surge aniticipator valve)%n-SRV (surge relief valve)%n-SAV + SRV (SAV and SRV)

		Returns:
			Dict[int,int]: 
		"""
		pass

	def SavType(self) -> Dict[int,int]:
		"""The type of SAV to simulate. Choices are Needle, Circular Gate, Globe, Ball and Butterfly. The choice you make will only affect the transient engine.

		Returns:
			Dict[int,int]: 
		"""
		pass

	def SavClosureTriggerType(self) -> Dict[int,int]:
		"""The closure of an open/opening SAV is initiated by either Time (SAV stays fully open) or the Threshold  Pressure (SAV), but not both. When based on Pressure, the SAV will begin to close when the pressure rises back above the Threshold Pressure (SAV), which may occur before the SAV has fully opened.

		Returns:
			Dict[int,int]: 
		"""
		pass

	def SrvControlType(self) -> Dict[int,int]:
		"""The opening and closure of SRV is control by spring constant or time.

		Returns:
			Dict[int,int]: 
		"""
		pass

	def SRVValveType(self) -> Dict[int,int]:
		"""The type of SRV to simulate. Choices are Needle, Circular Gate, Globe, Ball and Butterfly. The choice you make will only affect the transient engine.

		Returns:
			Dict[int,int]: 
		"""
		pass

class ISurgeValveResults(IHammerNodeResults):

	def __init__(self) -> None:
		"""Creating a new Instance of this class is not allowed


		Raises:
			Exception: if this class is instanciated
		"""
		raise Exception("Creating a new Instance of this class is not allowed")
		pass

class ISurgeValvesResults(IHammerNodesResults):

	def __init__(self) -> None:
		"""Creating a new Instance of this class is not allowed


		Raises:
			Exception: if this class is instanciated
		"""
		raise Exception("Creating a new Instance of this class is not allowed")
		pass

class ISurgeValveUnits(IHammerNodeUnits):

	def __init__(self) -> None:
		"""Creating a new Instance of this class is not allowed


		Raises:
			Exception: if this class is instanciated
		"""
		raise Exception("Creating a new Instance of this class is not allowed")
		pass

	@property
	def DiameterUnit(self) -> IUnit:
		"""No Description

		Returns:
			ISurgeValveUnits: 
		"""
		pass

	@property
	def TimeOpenUnit(self) -> IUnit:
		"""No Description

		Returns:
			ISurgeValveUnits: 
		"""
		pass

	@property
	def DischargeCoefficient(self) -> IUnit:
		"""No Description

		Returns:
			ISurgeValveUnits: 
		"""
		pass

	@property
	def SpringConstantUnit(self) -> IUnit:
		"""No Description

		Returns:
			ISurgeValveUnits: 
		"""
		pass

class ISurgeValve(IWaterNetworkElement[ISurgeValves, ISurgeValve, ISurgeValveUnits, ISurgeValveInput, ISurgeValveResults, ISurgeValvesInput, ISurgeValvesResults]):

	def __init__(self) -> None:
		"""Creating a new Instance of this class is not allowed


		Raises:
			Exception: if this class is instanciated
		"""
		raise Exception("Creating a new Instance of this class is not allowed")
		pass

class ISurgeValves(IWaterNetworkElements[ISurgeValves, ISurgeValve, ISurgeValveUnits, ISurgeValveInput, ISurgeValveResults, ISurgeValvesInput, ISurgeValvesResults]):

	def __init__(self) -> None:
		"""Creating a new Instance of this class is not allowed


		Raises:
			Exception: if this class is instanciated
		"""
		raise Exception("Creating a new Instance of this class is not allowed")
		pass

class IBaseOrificeNodeInput(IHammerNodeInput):

	def __init__(self) -> None:
		"""Creating a new Instance of this class is not allowed


		Raises:
			Exception: if this class is instanciated
		"""
		raise Exception("Creating a new Instance of this class is not allowed")
		pass

	@property
	def OrificePressureDrop(self) -> float:
		"""No Description

		Returns:
			IBaseOrificeNodeInput: 
		"""
		pass

	@property
	def OrificeFlow(self) -> float:
		"""No Description

		Returns:
			IBaseOrificeNodeInput: 
		"""
		pass

	@OrificePressureDrop.setter
	def OrificePressureDrop(self, orificepressuredrop: float) -> None:
		pass

	@OrificeFlow.setter
	def OrificeFlow(self, orificeflow: float) -> None:
		pass

class IBaseOrificeNodesInput(IHammerNodesInput):

	def __init__(self) -> None:
		"""Creating a new Instance of this class is not allowed


		Raises:
			Exception: if this class is instanciated
		"""
		raise Exception("Creating a new Instance of this class is not allowed")
		pass

	def OrificePressureDrop(self) -> Dict[int,int]:
		"""Pressure drop corresponding to the typical flow.

		Returns:
			Dict[int,int]: 
		"""
		pass

	def OrificeFlow(self) -> Dict[int,int]:
		"""This is a typical (positive) flow through the orifice or valve.

		Returns:
			Dict[int,int]: 
		"""
		pass

class IBaseOrificeNodeResults(IHammerNodeResults):

	def __init__(self) -> None:
		"""Creating a new Instance of this class is not allowed


		Raises:
			Exception: if this class is instanciated
		"""
		raise Exception("Creating a new Instance of this class is not allowed")
		pass

class IBaseOrificeNodesResults(IHammerNodesResults):

	def __init__(self) -> None:
		"""Creating a new Instance of this class is not allowed


		Raises:
			Exception: if this class is instanciated
		"""
		raise Exception("Creating a new Instance of this class is not allowed")
		pass

class IBaseOrificeNodeUnits(IHammerNodeUnits):

	def __init__(self) -> None:
		"""Creating a new Instance of this class is not allowed


		Raises:
			Exception: if this class is instanciated
		"""
		raise Exception("Creating a new Instance of this class is not allowed")
		pass

	@property
	def FlowUnit(self) -> IUnit:
		"""No Description

		Returns:
			IBaseOrificeNodeUnits: 
		"""
		pass

class IPressureHeadFlowCollection(ICollectionElements[IPressureHeadFlows, IPressureHeadFlow, IPressureHeadFlowUnits]):

	def __init__(self) -> None:
		"""Creating a new Instance of this class is not allowed


		Raises:
			Exception: if this class is instanciated
		"""
		raise Exception("Creating a new Instance of this class is not allowed")
		pass

class IPressureHeadFlows(ICollection[IPressureHeadFlow]):

	def __init__(self) -> None:
		"""Creating a new Instance of this class is not allowed


		Raises:
			Exception: if this class is instanciated
		"""
		raise Exception("Creating a new Instance of this class is not allowed")
		pass

	def Add(self, pressureHead: float, flow: float) -> IPressureHeadFlow:
		"""Adds a new row to the collection with the provided data.

		Args:
			pressureHead(float): pressureHead
			flow(float): flow

		Returns:
			IPressureHeadFlow: 
		"""
		pass

class IPressureHeadFlow(ICollectionElement):

	def __init__(self) -> None:
		"""Creating a new Instance of this class is not allowed


		Raises:
			Exception: if this class is instanciated
		"""
		raise Exception("Creating a new Instance of this class is not allowed")
		pass

	@property
	def PressureHead(self) -> float:
		"""No Description

		Returns:
			IPressureHeadFlow: 
		"""
		pass

	@property
	def Flow(self) -> float:
		"""No Description

		Returns:
			IPressureHeadFlow: 
		"""
		pass

	@PressureHead.setter
	def PressureHead(self, pressurehead: float) -> None:
		pass

	@Flow.setter
	def Flow(self, flow: float) -> None:
		pass

class IPressureHeadFlowUnits(IElementUnits):

	def __init__(self) -> None:
		"""Creating a new Instance of this class is not allowed


		Raises:
			Exception: if this class is instanciated
		"""
		raise Exception("Creating a new Instance of this class is not allowed")
		pass

	@property
	def PressureHeadUnit(self) -> IUnit:
		"""No Description

		Returns:
			IPressureHeadFlowUnits: 
		"""
		pass

	@property
	def FlowUnit(self) -> IUnit:
		"""No Description

		Returns:
			IPressureHeadFlowUnits: 
		"""
		pass

class IDischargeToAtmosphereNodeInput(IBaseOrificeNodeInput):

	def __init__(self) -> None:
		"""Creating a new Instance of this class is not allowed


		Raises:
			Exception: if this class is instanciated
		"""
		raise Exception("Creating a new Instance of this class is not allowed")
		pass

	@property
	def DischargeElementType(self) -> DischargeToAtmosphereTypeEnum:
		"""No Description

		Returns:
			IDischargeToAtmosphereNodeInput: 
		"""
		pass

	@property
	def InitialGaseVolume(self) -> float:
		"""No Description

		Returns:
			IDischargeToAtmosphereNodeInput: 
		"""
		pass

	@property
	def TimeToStartOperating(self) -> float:
		"""No Description

		Returns:
			IDischargeToAtmosphereNodeInput: 
		"""
		pass

	@property
	def TimeToFullyOpenOrClose(self) -> float:
		"""No Description

		Returns:
			IDischargeToAtmosphereNodeInput: 
		"""
		pass

	@property
	def PressureHeadFlowCollection(self) -> IPressureHeadFlowCollection:
		"""No Description

		Returns:
			IDischargeToAtmosphereNodeInput: 
		"""
		pass

	@property
	def InitialStatus(self) -> ValveTypeInitialStatusEnum:
		"""No Description

		Returns:
			IDischargeToAtmosphereNodeInput: 
		"""
		pass

	@property
	def ReportPeriod(self) -> int:
		"""No Description

		Returns:
			IDischargeToAtmosphereNodeInput: 
		"""
		pass

	@DischargeElementType.setter
	def DischargeElementType(self, dischargeelementtype: DischargeToAtmosphereTypeEnum) -> None:
		pass

	@InitialGaseVolume.setter
	def InitialGaseVolume(self, initialgasevolume: float) -> None:
		pass

	@TimeToStartOperating.setter
	def TimeToStartOperating(self, timetostartoperating: float) -> None:
		pass

	@TimeToFullyOpenOrClose.setter
	def TimeToFullyOpenOrClose(self, timetofullyopenorclose: float) -> None:
		pass

	@InitialStatus.setter
	def InitialStatus(self, initialstatus: ValveTypeInitialStatusEnum) -> None:
		pass

	@ReportPeriod.setter
	def ReportPeriod(self, reportperiod: int) -> None:
		pass

class IDischargeToAtmosphereNodesInput(IBaseOrificeNodesInput):

	def __init__(self) -> None:
		"""Creating a new Instance of this class is not allowed


		Raises:
			Exception: if this class is instanciated
		"""
		raise Exception("Creating a new Instance of this class is not allowed")
		pass

	def DischargeElementType(self) -> Dict[int,int]:
		"""The type of discharge element to simulate. Choices are Orifice, Valve or Rating Curve.

		Returns:
			Dict[int,int]: 
		"""
		pass

	def InitialGasVolume(self) -> Dict[int,int]:
		"""The accumulated air at the orifice at the beginning of the simulation.

		Returns:
			Dict[int,int]: 
		"""
		pass

	def TimeToStartOpening(self) -> Dict[int,int]:
		"""Valve starts to operate after this time.

		Returns:
			Dict[int,int]: 
		"""
		pass

	def TimeToFullyOpenOrClose(self) -> Dict[int,int]:
		"""Time to close (or open, if zero initial flow) the valve.

		Returns:
			Dict[int,int]: 
		"""
		pass

	def InitialStatus(self) -> Dict[int,int]:
		"""If the Discharge Element is a valve, then this field specifies whether the valve is initially open or closed.

		Returns:
			Dict[int,int]: 
		"""
		pass

	def ReportPeriod(self) -> Dict[int,int]:
		"""Number of time steps between successive printouts of operation. By default, this printout is suppressed.

		Returns:
			Dict[int,int]: 
		"""
		pass

class IDischargeToAtmosphereNodeResults(IBaseOrificeNodeResults):

	def __init__(self) -> None:
		"""Creating a new Instance of this class is not allowed


		Raises:
			Exception: if this class is instanciated
		"""
		raise Exception("Creating a new Instance of this class is not allowed")
		pass

	@overload
	def IDischargeToAtmosphereNodeResults(self) -> Union[float, None]:
		"""Calculated discharge from the node.

		Returns:
			Nullable: 
		"""
		pass

	@overload
	def IDischargeToAtmosphereNodeResults(self, timeStepIndex: int) -> Union[float, None]:
		"""Calculated discharge from the node.

		Args:
			timeStepIndex(int): timeStepIndex

		Returns:
			Nullable: 
		"""
		pass

	def CalculatedDischarges(self) -> array(Union[float, None]):
		"""Calculated discharge from the node.

		Returns:
			array(): 
		"""
		pass

class IDischargeToAtmosphereNodesResults(IBaseOrificeNodesResults):

	def __init__(self) -> None:
		"""Creating a new Instance of this class is not allowed


		Raises:
			Exception: if this class is instanciated
		"""
		raise Exception("Creating a new Instance of this class is not allowed")
		pass

	@overload
	def IDischargeToAtmosphereNodesResults(self) -> Dict[int,int]:
		"""Calculated discharge from the node.

		Returns:
			Dict[int,int]: 
		"""
		pass

	@overload
	def IDischargeToAtmosphereNodesResults(self, timeStepIndex: int) -> Dict[int,int]:
		"""Calculated discharge from the node.

		Args:
			timeStepIndex(int): timeStepIndex

		Returns:
			Dict[int,int]: 
		"""
		pass

	@overload
	def IDischargeToAtmosphereNodesResults(self, ids: List[int], timeStepIndex: int) -> Dict[int,int]:
		"""No Description

		Args:
			ids(List[int]): ids
			timeStepIndex(int): timeStepIndex

		Returns:
			Dict[int,int]: 
		"""
		pass

class IDischargeToAtmosphereUnits(IBaseOrificeNodeUnits):

	def __init__(self) -> None:
		"""Creating a new Instance of this class is not allowed


		Raises:
			Exception: if this class is instanciated
		"""
		raise Exception("Creating a new Instance of this class is not allowed")
		pass

	@property
	def VolumeUnit(self) -> IUnit:
		"""No Description

		Returns:
			IDischargeToAtmosphereUnits: 
		"""
		pass

	@property
	def TimeUnit(self) -> IUnit:
		"""No Description

		Returns:
			IDischargeToAtmosphereUnits: 
		"""
		pass

	@property
	def DischargeUnit(self) -> IUnit:
		"""No Description

		Returns:
			IDischargeToAtmosphereUnits: 
		"""
		pass

class IDischargeToAtmosphere(IWaterNetworkElement[IDischargeToAtmospheres, IDischargeToAtmosphere, IDischargeToAtmosphereUnits, IDischargeToAtmosphereNodeInput, IDischargeToAtmosphereNodeResults, IDischargeToAtmosphereNodesInput, IDischargeToAtmosphereNodesResults]):

	def __init__(self) -> None:
		"""Creating a new Instance of this class is not allowed


		Raises:
			Exception: if this class is instanciated
		"""
		raise Exception("Creating a new Instance of this class is not allowed")
		pass

class IDischargeToAtmospheres(IWaterNetworkElements[IDischargeToAtmospheres, IDischargeToAtmosphere, IDischargeToAtmosphereUnits, IDischargeToAtmosphereNodeInput, IDischargeToAtmosphereNodeResults, IDischargeToAtmosphereNodesInput, IDischargeToAtmosphereNodesResults]):

	def __init__(self) -> None:
		"""Creating a new Instance of this class is not allowed


		Raises:
			Exception: if this class is instanciated
		"""
		raise Exception("Creating a new Instance of this class is not allowed")
		pass

class IRuptureDiskInput(IBaseOrificeNodeInput):

	def __init__(self) -> None:
		"""Creating a new Instance of this class is not allowed


		Raises:
			Exception: if this class is instanciated
		"""
		raise Exception("Creating a new Instance of this class is not allowed")
		pass

	@property
	def PressureThreshold(self) -> float:
		"""No Description

		Returns:
			IRuptureDiskInput: 
		"""
		pass

	@PressureThreshold.setter
	def PressureThreshold(self, pressurethreshold: float) -> None:
		pass

class IRuptureDisksInput(IBaseOrificeNodesInput):

	def __init__(self) -> None:
		"""Creating a new Instance of this class is not allowed


		Raises:
			Exception: if this class is instanciated
		"""
		raise Exception("Creating a new Instance of this class is not allowed")
		pass

	def PressureThreshold(self) -> Dict[int,int]:
		"""The pressure above which the rupture disk breaks to vent the liquid to atmosphere.

		Returns:
			Dict[int,int]: 
		"""
		pass

class IRuptureDiskResults(IBaseOrificeNodeResults):

	def __init__(self) -> None:
		"""Creating a new Instance of this class is not allowed


		Raises:
			Exception: if this class is instanciated
		"""
		raise Exception("Creating a new Instance of this class is not allowed")
		pass

class IRuptureDisksResults(IBaseOrificeNodesResults):

	def __init__(self) -> None:
		"""Creating a new Instance of this class is not allowed


		Raises:
			Exception: if this class is instanciated
		"""
		raise Exception("Creating a new Instance of this class is not allowed")
		pass

class IRuptureDiskUnits(IBaseOrificeNodeUnits):

	def __init__(self) -> None:
		"""Creating a new Instance of this class is not allowed


		Raises:
			Exception: if this class is instanciated
		"""
		raise Exception("Creating a new Instance of this class is not allowed")
		pass

class IRuptureDisk(IWaterNetworkElement[IRuptureDisks, IRuptureDisk, IRuptureDiskUnits, IRuptureDiskInput, IRuptureDiskResults, IRuptureDisksInput, IRuptureDisksResults]):

	def __init__(self) -> None:
		"""Creating a new Instance of this class is not allowed


		Raises:
			Exception: if this class is instanciated
		"""
		raise Exception("Creating a new Instance of this class is not allowed")
		pass

class IRuptureDisks(IWaterNetworkElements[IRuptureDisks, IRuptureDisk, IRuptureDiskUnits, IRuptureDiskInput, IRuptureDiskResults, IRuptureDisksInput, IRuptureDisksResults]):

	def __init__(self) -> None:
		"""Creating a new Instance of this class is not allowed


		Raises:
			Exception: if this class is instanciated
		"""
		raise Exception("Creating a new Instance of this class is not allowed")
		pass

class IBaseNodesResults(IElementsResults, IWaterQualityElementsResults):

	def __init__(self) -> None:
		"""Creating a new Instance of this class is not allowed


		Raises:
			Exception: if this class is instanciated
		"""
		raise Exception("Creating a new Instance of this class is not allowed")
		pass

	@overload
	def IBaseNodesResults(self) -> Dict[int,int]:
		"""Gets the hydraulic grade for all nodes at the current time step.

		Returns:
			Dict[int,int]: 
		"""
		pass

	@overload
	def IBaseNodesResults(self, timeStepIndex: int) -> Dict[int,int]:
		"""Gets the hydraulic grade for all nodes at the given time step.

		Args:
			timeStepIndex(int): timeStepIndex

		Returns:
			Dict[int,int]: 
		"""
		pass

	@overload
	def IBaseNodesResults(self, ids: List[int], timeStepIndex: int) -> Dict[int,int]:
		"""No Description

		Args:
			ids(List[int]): ids
			timeStepIndex(int): timeStepIndex

		Returns:
			Dict[int,int]: 
		"""
		pass

class IPhysicalNodeElementInput(IPointNodeInput):

	def __init__(self) -> None:
		"""Creating a new Instance of this class is not allowed


		Raises:
			Exception: if this class is instanciated
		"""
		raise Exception("Creating a new Instance of this class is not allowed")
		pass

	@property
	def Elevation(self) -> float:
		"""No Description

		Returns:
			IPhysicalNodeElementInput: 
		"""
		pass

	@Elevation.setter
	def Elevation(self, elevation: float) -> None:
		pass

class IPhysicalNodeElementsInput(IPointNodesInput):

	def __init__(self) -> None:
		"""Creating a new Instance of this class is not allowed


		Raises:
			Exception: if this class is instanciated
		"""
		raise Exception("Creating a new Instance of this class is not allowed")
		pass

	@overload
	def IPhysicalNodeElementsInput(self) -> Dict[int,int]:
		"""Gets elevations for all base nodes.

		Returns:
			Dict[int,int]: 
		"""
		pass

	@overload
	def IPhysicalNodeElementsInput(self, ids: List[int]) -> Dict[int,int]:
		"""No Description

		Args:
			ids(List[int]): ids

		Returns:
			Dict[int,int]: 
		"""
		pass

class IBaseNodeInput(IPhysicalNodeElementInput, IWaterZoneableNetworkElementInput, IWaterQualityElementInput, IWaterQualityNodeInput):

	def __init__(self) -> None:
		"""Creating a new Instance of this class is not allowed


		Raises:
			Exception: if this class is instanciated
		"""
		raise Exception("Creating a new Instance of this class is not allowed")
		pass

class IBaseNodesInput(IWaterZoneableNetworkElementsInput, IWaterQualityElementsInput, IWaterQualityNodesInput, IPhysicalNodeElementsInput):

	def __init__(self) -> None:
		"""Creating a new Instance of this class is not allowed


		Raises:
			Exception: if this class is instanciated
		"""
		raise Exception("Creating a new Instance of this class is not allowed")
		pass

class IBaseNodeResults(IElementResults, IWaterQualityResults):

	def __init__(self) -> None:
		"""Creating a new Instance of this class is not allowed


		Raises:
			Exception: if this class is instanciated
		"""
		raise Exception("Creating a new Instance of this class is not allowed")
		pass

	@overload
	def IBaseNodeResults(self) -> Union[float, None]:
		"""Calculated hydraulic grade at node at current time step.

		Returns:
			Nullable: 
		"""
		pass

	@overload
	def IBaseNodeResults(self, timeStepIndex: int) -> Union[float, None]:
		"""Calculated hydraulic grade at node at given time step.

		Args:
			timeStepIndex(int): timeStepIndex

		Returns:
			Nullable: 
		"""
		pass

	def HydraulicGrades(self) -> array(Union[float, None]):
		"""Calculated hydraulic grade at node across all time steps.

		Returns:
			array(): 
		"""
		pass

class IBaseNodeUnits(IGeometryUnits, IWaterQualityResultsUnits):

	def __init__(self) -> None:
		"""Creating a new Instance of this class is not allowed


		Raises:
			Exception: if this class is instanciated
		"""
		raise Exception("Creating a new Instance of this class is not allowed")
		pass

	@property
	def ElevationUnit(self) -> IUnit:
		"""No Description

		Returns:
			IBaseNodeUnits: 
		"""
		pass

	@property
	def InitialAgeUnit(self) -> IUnit:
		"""No Description

		Returns:
			IBaseNodeUnits: 
		"""
		pass

	@property
	def InitialConcentrationUnit(self) -> IUnit:
		"""No Description

		Returns:
			IBaseNodeUnits: 
		"""
		pass

	@property
	def InitialTraceUnit(self) -> IUnit:
		"""No Description

		Returns:
			IBaseNodeUnits: 
		"""
		pass

	@property
	def BaseConcentrationUnit(self) -> IUnit:
		"""No Description

		Returns:
			IBaseNodeUnits: 
		"""
		pass

	@property
	def HydraulicGradeUnit(self) -> IUnit:
		"""No Description

		Returns:
			IBaseNodeUnits: 
		"""
		pass

class IReservoirs(IWaterNetworkElements[IReservoirs, IReservoir, IReservoirUnits, IReservoirInput, IReservoirResults, IReservoirsInput, IReservoirsResults]):

	def __init__(self) -> None:
		"""Creating a new Instance of this class is not allowed


		Raises:
			Exception: if this class is instanciated
		"""
		raise Exception("Creating a new Instance of this class is not allowed")
		pass

class IReservoir(IWaterNetworkElement[IReservoirs, IReservoir, IReservoirUnits, IReservoirInput, IReservoirResults, IReservoirsInput, IReservoirsResults]):

	def __init__(self) -> None:
		"""Creating a new Instance of this class is not allowed


		Raises:
			Exception: if this class is instanciated
		"""
		raise Exception("Creating a new Instance of this class is not allowed")
		pass

class IReservoirsResults(IBaseNodesResults):

	def __init__(self) -> None:
		"""Creating a new Instance of this class is not allowed


		Raises:
			Exception: if this class is instanciated
		"""
		raise Exception("Creating a new Instance of this class is not allowed")
		pass

	@overload
	def IReservoirsResults(self) -> Dict[int,int]:
		"""Net flow out at the current time step across all reservoirs.

		Returns:
			Dict[int,int]: 
		"""
		pass

	@overload
	def IReservoirsResults(self, timeStepIndex: int) -> Dict[int,int]:
		"""Net flow out at the given time step across all reservoirs.

		Args:
			timeStepIndex(int): timeStepIndex

		Returns:
			Dict[int,int]: 
		"""
		pass

	@overload
	def IReservoirsResults(self, ids: List[int], timeStepIndex: int) -> Dict[int,int]:
		"""No Description

		Args:
			ids(List[int]): ids
			timeStepIndex(int): timeStepIndex

		Returns:
			Dict[int,int]: 
		"""
		pass

class IReservoirResults(IBaseNodeResults):

	def __init__(self) -> None:
		"""Creating a new Instance of this class is not allowed


		Raises:
			Exception: if this class is instanciated
		"""
		raise Exception("Creating a new Instance of this class is not allowed")
		pass

	@overload
	def IReservoirResults(self) -> Union[float, None]:
		"""Net flow out of the element at the current time step.

		Returns:
			Nullable: 
		"""
		pass

	@overload
	def IReservoirResults(self, timeStepIndex: int) -> Union[float, None]:
		"""Net flow out of the element at the given time step.

		Args:
			timeStepIndex(int): timeStepIndex

		Returns:
			Nullable: 
		"""
		pass

	def Flows(self) -> array(Union[float, None]):
		"""Net flow out of the element across all time steps.

		Returns:
			array(): 
		"""
		pass

class IReservoirInput(IBaseNodeInput, IWaterTraceableInput):

	def __init__(self) -> None:
		"""Creating a new Instance of this class is not allowed


		Raises:
			Exception: if this class is instanciated
		"""
		raise Exception("Creating a new Instance of this class is not allowed")
		pass

class IReservoirsInput(IBaseNodesInput):

	def __init__(self) -> None:
		"""Creating a new Instance of this class is not allowed


		Raises:
			Exception: if this class is instanciated
		"""
		raise Exception("Creating a new Instance of this class is not allowed")
		pass

class IReservoirUnits(IBaseNodeUnits):

	def __init__(self) -> None:
		"""Creating a new Instance of this class is not allowed


		Raises:
			Exception: if this class is instanciated
		"""
		raise Exception("Creating a new Instance of this class is not allowed")
		pass

	@property
	def FlowUnit(self) -> IUnit:
		"""No Description

		Returns:
			IReservoirUnits: 
		"""
		pass

class ITapInput(IPointNodeInput):

	def __init__(self) -> None:
		"""Creating a new Instance of this class is not allowed


		Raises:
			Exception: if this class is instanciated
		"""
		raise Exception("Creating a new Instance of this class is not allowed")
		pass

	@property
	def AssociatedElement(self) -> IPipe:
		"""No Description

		Returns:
			ITapInput: 
		"""
		pass

	@AssociatedElement.setter
	def AssociatedElement(self, associatedelement: IPipe) -> None:
		pass

class ITapsInput(IPointNodesInput):

	def __init__(self) -> None:
		"""Creating a new Instance of this class is not allowed


		Raises:
			Exception: if this class is instanciated
		"""
		raise Exception("Creating a new Instance of this class is not allowed")
		pass

	@overload
	def ITapsInput(self) -> Dict[int,int]:
		"""Gets the geometry of all nodes of this type.

		Returns:
			Dict[int,int]: 
		"""
		pass

	@overload
	def ITapsInput(self, ids: List[int]) -> Dict[int,int]:
		"""No Description

		Args:
			ids(List[int]): ids

		Returns:
			Dict[int,int]: 
		"""
		pass

class ITap(IWaterNetworkElement[ITaps, ITap, IGeometryUnits, ITapInput, IElementResults, ITapsInput, IElementsResults]):

	def __init__(self) -> None:
		"""Creating a new Instance of this class is not allowed


		Raises:
			Exception: if this class is instanciated
		"""
		raise Exception("Creating a new Instance of this class is not allowed")
		pass

class ITaps(IWaterNetworkElements[ITaps, ITap, IGeometryUnits, ITapInput, IElementResults, ITapsInput, IElementsResults]):

	def __init__(self) -> None:
		"""Creating a new Instance of this class is not allowed


		Raises:
			Exception: if this class is instanciated
		"""
		raise Exception("Creating a new Instance of this class is not allowed")
		pass

class IIsolationValveElementInput(IPhysicalNodeElementInput):

	def __init__(self) -> None:
		"""Creating a new Instance of this class is not allowed


		Raises:
			Exception: if this class is instanciated
		"""
		raise Exception("Creating a new Instance of this class is not allowed")
		pass

	@property
	def ReferencedPipe(self) -> IPipe:
		"""No Description

		Returns:
			IIsolationValveElementInput: 
		"""
		pass

	@property
	def ValveDiameter(self) -> float:
		"""No Description

		Returns:
			IIsolationValveElementInput: 
		"""
		pass

	@property
	def MinorLossCoefficient(self) -> float:
		"""No Description

		Returns:
			IIsolationValveElementInput: 
		"""
		pass

	@property
	def IsOperable(self) -> bool:
		"""No Description

		Returns:
			IIsolationValveElementInput: 
		"""
		pass

	@property
	def InitialStatus(self) -> IsolationValveInitialSetting:
		"""No Description

		Returns:
			IIsolationValveElementInput: 
		"""
		pass

	@property
	def InstallationYear(self) -> int:
		"""No Description

		Returns:
			IIsolationValveElementInput: 
		"""
		pass

	@ReferencedPipe.setter
	def ReferencedPipe(self, referencedpipe: IPipe) -> None:
		pass

	@ValveDiameter.setter
	def ValveDiameter(self, valvediameter: float) -> None:
		pass

	@MinorLossCoefficient.setter
	def MinorLossCoefficient(self, minorlosscoefficient: float) -> None:
		pass

	@IsOperable.setter
	def IsOperable(self, isoperable: bool) -> None:
		pass

	@InitialStatus.setter
	def InitialStatus(self, initialstatus: IsolationValveInitialSetting) -> None:
		pass

	@InstallationYear.setter
	def InstallationYear(self, installationyear: int) -> None:
		pass

class IIsolationValveElementsInput(IPhysicalNodeElementsInput):

	def __init__(self) -> None:
		"""Creating a new Instance of this class is not allowed


		Raises:
			Exception: if this class is instanciated
		"""
		raise Exception("Creating a new Instance of this class is not allowed")
		pass

	@overload
	def IIsolationValveElementsInput(self) -> Dict[int,int]:
		"""The pipe the isolation valve references

		Returns:
			Dict[int,int]: 
		"""
		pass

	@overload
	def IIsolationValveElementsInput(self, ids: List[int]) -> Dict[int,int]:
		"""No Description

		Args:
			ids(List[int]): ids

		Returns:
			Dict[int,int]: 
		"""
		pass

	@overload
	def IIsolationValveElementsInput(self) -> Dict[int,int]:
		"""Inside diameter of the valve. Used to calculate the velocity through the valve and a corresponding minor loss when a minor loss coefficient is entered.

		Returns:
			Dict[int,int]: 
		"""
		pass

	@overload
	def IIsolationValveElementsInput(self, ids: List[int]) -> Dict[int,int]:
		"""No Description

		Args:
			ids(List[int]): ids

		Returns:
			Dict[int,int]: 
		"""
		pass

	@overload
	def IIsolationValveElementsInput(self) -> Dict[int,int]:
		"""K value in the minor headloss equation.

		Returns:
			Dict[int,int]: 
		"""
		pass

	@overload
	def IIsolationValveElementsInput(self, ids: List[int]) -> Dict[int,int]:
		"""No Description

		Args:
			ids(List[int]): ids

		Returns:
			Dict[int,int]: 
		"""
		pass

	@overload
	def IIsolationValveElementsInput(self) -> Dict[int,int]:
		"""If true, valve can be used in identifying segments.

		Returns:
			Dict[int,int]: 
		"""
		pass

	@overload
	def IIsolationValveElementsInput(self, ids: List[int]) -> Dict[int,int]:
		"""No Description

		Args:
			ids(List[int]): ids

		Returns:
			Dict[int,int]: 
		"""
		pass

	@overload
	def IIsolationValveElementsInput(self) -> Dict[int,int]:
		"""Set whether the valve is initially open or closed.

		Returns:
			Dict[int,int]: 
		"""
		pass

	@overload
	def IIsolationValveElementsInput(self, ids: List[int]) -> Dict[int,int]:
		"""No Description

		Args:
			ids(List[int]): ids

		Returns:
			Dict[int,int]: 
		"""
		pass

	@overload
	def IIsolationValveElementsInput(self) -> Dict[int,int]:
		"""Specify the install year of the element.  It does not affect the calculations.

		Returns:
			Dict[int,int]: 
		"""
		pass

	@overload
	def IIsolationValveElementsInput(self, ids: List[int]) -> Dict[int,int]:
		"""No Description

		Args:
			ids(List[int]): ids

		Returns:
			Dict[int,int]: 
		"""
		pass

class IIsolatioNValveElementResults(IElementResults):

	def __init__(self) -> None:
		"""Creating a new Instance of this class is not allowed


		Raises:
			Exception: if this class is instanciated
		"""
		raise Exception("Creating a new Instance of this class is not allowed")
		pass

	@overload
	def IIsolatioNValveElementResults(self) -> Union[float, None]:
		"""Hydraulic Grade at valve location on pipe.

		Returns:
			Nullable: 
		"""
		pass

	@overload
	def IIsolatioNValveElementResults(self, timeStepIndex: int) -> Union[float, None]:
		"""Hydraulic Grade at valve location on pipe.

		Args:
			timeStepIndex(int): timeStepIndex

		Returns:
			Nullable: 
		"""
		pass

	@overload
	def IIsolatioNValveElementResults(self) -> Union[float, None]:
		"""Pressure at valve location on pipe.

		Returns:
			Nullable: 
		"""
		pass

	@overload
	def IIsolatioNValveElementResults(self, timeStepIndex: int) -> Union[float, None]:
		"""Pressure at valve location on pipe.

		Args:
			timeStepIndex(int): timeStepIndex

		Returns:
			Nullable: 
		"""
		pass

	@overload
	def IIsolatioNValveElementResults(self) -> Union[float, None]:
		"""Magnitude of flow through isolation valve.

		Returns:
			Nullable: 
		"""
		pass

	@overload
	def IIsolatioNValveElementResults(self, timeStepIndex: int) -> Union[float, None]:
		"""Magnitude of flow through isolation valve.

		Args:
			timeStepIndex(int): timeStepIndex

		Returns:
			Nullable: 
		"""
		pass

	@overload
	def IIsolatioNValveElementResults(self) -> Union[float, None]:
		"""Velocity through the isolation valve.

		Returns:
			Nullable: 
		"""
		pass

	@overload
	def IIsolatioNValveElementResults(self, timeStepIndex: int) -> Union[float, None]:
		"""Velocity through the isolation valve.

		Args:
			timeStepIndex(int): timeStepIndex

		Returns:
			Nullable: 
		"""
		pass

	@overload
	def IIsolatioNValveElementResults(self) -> Union[bool, None]:
		"""True if current isolation valve is closed during the current time step.

		Returns:
			Nullable: 
		"""
		pass

	@overload
	def IIsolatioNValveElementResults(self, timeStepIndex: int) -> Union[bool, None]:
		"""True if current isolation valve is closed during the current time step.

		Args:
			timeStepIndex(int): timeStepIndex

		Returns:
			Nullable: 
		"""
		pass

	def HydraulicGrades(self) -> array(Union[float, None]):
		"""Hydraulic Grade at valve location on pipe.

		Returns:
			array(): 
		"""
		pass

	def Pressures(self) -> array(Union[float, None]):
		"""Pressure at valve location on pipe.

		Returns:
			array(): 
		"""
		pass

	def Flows(self) -> array(Union[float, None]):
		"""Magnitude of flow through isolation valve.

		Returns:
			array(): 
		"""
		pass

	def Velocities(self) -> array(Union[float, None]):
		"""Velocity through the isolation valve.

		Returns:
			array(): 
		"""
		pass

	def DistanceFromEndPoint(self) -> Union[float, None]:
		"""Presents the active Distance From End Point for the current isolation valve.

		Returns:
			Nullable: 
		"""
		pass

	def IsCloseds(self) -> array(Union[bool, None]):
		"""True if current isolation valve is closed during the current time step.

		Returns:
			array(): 
		"""
		pass

class IIsolationValveElementsResults(IElementsResults):

	def __init__(self) -> None:
		"""Creating a new Instance of this class is not allowed


		Raises:
			Exception: if this class is instanciated
		"""
		raise Exception("Creating a new Instance of this class is not allowed")
		pass

	@overload
	def IIsolationValveElementsResults(self) -> Dict[int,int]:
		"""Hydraulic Grade at valve location on pipe.

		Returns:
			Dict[int,int]: 
		"""
		pass

	@overload
	def IIsolationValveElementsResults(self, timeStepIndex: int) -> Dict[int,int]:
		"""Hydraulic Grade at valve location on pipe.

		Args:
			timeStepIndex(int): timeStepIndex

		Returns:
			Dict[int,int]: 
		"""
		pass

	@overload
	def IIsolationValveElementsResults(self, ids: List[int], timeStepIndex: int) -> Dict[int,int]:
		"""No Description

		Args:
			ids(List[int]): ids
			timeStepIndex(int): timeStepIndex

		Returns:
			Dict[int,int]: 
		"""
		pass

	@overload
	def IIsolationValveElementsResults(self) -> Dict[int,int]:
		"""Pressure at valve location on pipe.

		Returns:
			Dict[int,int]: 
		"""
		pass

	@overload
	def IIsolationValveElementsResults(self, timeStepIndex: int) -> Dict[int,int]:
		"""Pressure at valve location on pipe.

		Args:
			timeStepIndex(int): timeStepIndex

		Returns:
			Dict[int,int]: 
		"""
		pass

	@overload
	def IIsolationValveElementsResults(self, ids: List[int], timeStepIndex: int) -> Dict[int,int]:
		"""No Description

		Args:
			ids(List[int]): ids
			timeStepIndex(int): timeStepIndex

		Returns:
			Dict[int,int]: 
		"""
		pass

	@overload
	def IIsolationValveElementsResults(self) -> Dict[int,int]:
		"""Magnitude of flow through isolation valve.

		Returns:
			Dict[int,int]: 
		"""
		pass

	@overload
	def IIsolationValveElementsResults(self, timeStepIndex: int) -> Dict[int,int]:
		"""Magnitude of flow through isolation valve.

		Args:
			timeStepIndex(int): timeStepIndex

		Returns:
			Dict[int,int]: 
		"""
		pass

	@overload
	def IIsolationValveElementsResults(self, ids: List[int], timeStepIndex: int) -> Dict[int,int]:
		"""No Description

		Args:
			ids(List[int]): ids
			timeStepIndex(int): timeStepIndex

		Returns:
			Dict[int,int]: 
		"""
		pass

	@overload
	def IIsolationValveElementsResults(self) -> Dict[int,int]:
		"""Velocity through the isolation valve.

		Returns:
			Dict[int,int]: 
		"""
		pass

	@overload
	def IIsolationValveElementsResults(self, timeStepIndex: int) -> Dict[int,int]:
		"""Velocity through the isolation valve.

		Args:
			timeStepIndex(int): timeStepIndex

		Returns:
			Dict[int,int]: 
		"""
		pass

	@overload
	def IIsolationValveElementsResults(self, ids: List[int], timeStepIndex: int) -> Dict[int,int]:
		"""No Description

		Args:
			ids(List[int]): ids
			timeStepIndex(int): timeStepIndex

		Returns:
			Dict[int,int]: 
		"""
		pass

	@overload
	def IIsolationValveElementsResults(self) -> Dict[int,int]:
		"""Presents the active Distance From End Point for the current isolation valve.

		Returns:
			Dict[int,int]: 
		"""
		pass

	@overload
	def IIsolationValveElementsResults(self, ids: List[int]) -> Dict[int,int]:
		"""No Description

		Args:
			ids(List[int]): ids

		Returns:
			Dict[int,int]: 
		"""
		pass

	@overload
	def IIsolationValveElementsResults(self) -> Dict[int,int]:
		"""True if current isolation valve is closed during the current time step.

		Returns:
			Dict[int,int]: 
		"""
		pass

	@overload
	def IIsolationValveElementsResults(self, timeStepIndex: int) -> Dict[int,int]:
		"""True if current isolation valve is closed during the current time step.

		Args:
			timeStepIndex(int): timeStepIndex

		Returns:
			Dict[int,int]: 
		"""
		pass

	@overload
	def IIsolationValveElementsResults(self, ids: List[int], timeStepIndex: int) -> Dict[int,int]:
		"""No Description

		Args:
			ids(List[int]): ids
			timeStepIndex(int): timeStepIndex

		Returns:
			Dict[int,int]: 
		"""
		pass

class IIsolationValveUnits(IGeometryUnits):

	def __init__(self) -> None:
		"""Creating a new Instance of this class is not allowed


		Raises:
			Exception: if this class is instanciated
		"""
		raise Exception("Creating a new Instance of this class is not allowed")
		pass

	@property
	def DiameterUnit(self) -> IUnit:
		"""No Description

		Returns:
			IIsolationValveUnits: 
		"""
		pass

	@property
	def CoefficientUnit(self) -> IUnit:
		"""No Description

		Returns:
			IIsolationValveUnits: 
		"""
		pass

	@property
	def ElevationUnit(self) -> IUnit:
		"""No Description

		Returns:
			IIsolationValveUnits: 
		"""
		pass

	@property
	def PressureUnit(self) -> IUnit:
		"""No Description

		Returns:
			IIsolationValveUnits: 
		"""
		pass

	@property
	def FlowUnit(self) -> IUnit:
		"""No Description

		Returns:
			IIsolationValveUnits: 
		"""
		pass

	@property
	def VelocityUnit(self) -> IUnit:
		"""No Description

		Returns:
			IIsolationValveUnits: 
		"""
		pass

class IIsolationValves(IWaterNetworkElements[IIsolationValves, IIsolationValve, IIsolationValveUnits, IIsolationValveElementInput, IIsolatioNValveElementResults, IIsolationValveElementsInput, IIsolationValveElementsResults]):

	def __init__(self) -> None:
		"""Creating a new Instance of this class is not allowed


		Raises:
			Exception: if this class is instanciated
		"""
		raise Exception("Creating a new Instance of this class is not allowed")
		pass

class IIsolationValve(IWaterNetworkElement[IIsolationValves, IIsolationValve, IIsolationValveUnits, IIsolationValveElementInput, IIsolatioNValveElementResults, IIsolationValveElementsInput, IIsolationValveElementsResults]):

	def __init__(self) -> None:
		"""Creating a new Instance of this class is not allowed


		Raises:
			Exception: if this class is instanciated
		"""
		raise Exception("Creating a new Instance of this class is not allowed")
		pass

class ISpotElevationInput(IPointNodeInput):

	def __init__(self) -> None:
		"""Creating a new Instance of this class is not allowed


		Raises:
			Exception: if this class is instanciated
		"""
		raise Exception("Creating a new Instance of this class is not allowed")
		pass

	@property
	def Elevation(self) -> float:
		"""No Description

		Returns:
			ISpotElevationInput: 
		"""
		pass

	@Elevation.setter
	def Elevation(self, elevation: float) -> None:
		pass

class ISpotElevationsInput(IPointNodesInput):

	def __init__(self) -> None:
		"""Creating a new Instance of this class is not allowed


		Raises:
			Exception: if this class is instanciated
		"""
		raise Exception("Creating a new Instance of this class is not allowed")
		pass

	@overload
	def ISpotElevationsInput(self) -> Dict[int,int]:
		"""The spot elevations.

		Returns:
			Dict[int,int]: 
		"""
		pass

	@overload
	def ISpotElevationsInput(self, ids: List[int]) -> Dict[int,int]:
		"""No Description

		Args:
			ids(List[int]): ids

		Returns:
			Dict[int,int]: 
		"""
		pass

class ISpotElevationResults(IElementResults):

	def __init__(self) -> None:
		"""Creating a new Instance of this class is not allowed


		Raises:
			Exception: if this class is instanciated
		"""
		raise Exception("Creating a new Instance of this class is not allowed")
		pass

	@overload
	def ISpotElevationResults(self) -> Union[float, None]:
		"""Interpolated hydraulic grade at this location.

		Returns:
			Nullable: 
		"""
		pass

	@overload
	def ISpotElevationResults(self, timeStepIndex: int) -> Union[float, None]:
		"""Interpolated hydraulic grade at this location at the given time step

		Args:
			timeStepIndex(int): timeStepIndex

		Returns:
			Nullable: 
		"""
		pass

	@overload
	def ISpotElevationResults(self) -> Union[float, None]:
		"""Pressure based on the interpolated hydraulic grade.

		Returns:
			Nullable: 
		"""
		pass

	@overload
	def ISpotElevationResults(self, timeStepIndex: int) -> Union[float, None]:
		"""Pressure based on the interpolated hydraulic grade.

		Args:
			timeStepIndex(int): timeStepIndex

		Returns:
			Nullable: 
		"""
		pass

	def EnhancedHydraulicGrades(self) -> array(Union[float, None]):
		"""Interpolated hydraulic grade at this location across all time steps

		Returns:
			array(): 
		"""
		pass

	def EnhancedPressures(self) -> array(Union[float, None]):
		"""Pressure based on the interpolated hydraulic grade.

		Returns:
			array(): 
		"""
		pass

class ISpotElevationsResults(IElementsResults):

	def __init__(self) -> None:
		"""Creating a new Instance of this class is not allowed


		Raises:
			Exception: if this class is instanciated
		"""
		raise Exception("Creating a new Instance of this class is not allowed")
		pass

	@overload
	def ISpotElevationsResults(self) -> Dict[int,int]:
		"""Interpolated hydraulic grade at this location.

		Returns:
			Dict[int,int]: 
		"""
		pass

	@overload
	def ISpotElevationsResults(self, timeStepIndex: int) -> Dict[int,int]:
		"""Interpolated hydraulic grade at this location.

		Args:
			timeStepIndex(int): timeStepIndex

		Returns:
			Dict[int,int]: 
		"""
		pass

	@overload
	def ISpotElevationsResults(self, ids: List[int], timeStepIndex: int) -> Dict[int,int]:
		"""No Description

		Args:
			ids(List[int]): ids
			timeStepIndex(int): timeStepIndex

		Returns:
			Dict[int,int]: 
		"""
		pass

	@overload
	def ISpotElevationsResults(self) -> Dict[int,int]:
		"""Pressure based on the interpolated hydraulic grade.

		Returns:
			Dict[int,int]: 
		"""
		pass

	@overload
	def ISpotElevationsResults(self, timeStepIndex: int) -> Dict[int,int]:
		"""Pressure based on the interpolated hydraulic grade.

		Args:
			timeStepIndex(int): timeStepIndex

		Returns:
			Dict[int,int]: 
		"""
		pass

	@overload
	def ISpotElevationsResults(self, ids: List[int], timeStepIndex: int) -> Dict[int,int]:
		"""No Description

		Args:
			ids(List[int]): ids
			timeStepIndex(int): timeStepIndex

		Returns:
			Dict[int,int]: 
		"""
		pass

class ISpotElevationUnits(IGeometryUnits):

	def __init__(self) -> None:
		"""Creating a new Instance of this class is not allowed


		Raises:
			Exception: if this class is instanciated
		"""
		raise Exception("Creating a new Instance of this class is not allowed")
		pass

	@property
	def ElevationUnit(self) -> IUnit:
		"""No Description

		Returns:
			ISpotElevationUnits: 
		"""
		pass

	@property
	def HydraulicGradeUnit(self) -> IUnit:
		"""No Description

		Returns:
			ISpotElevationUnits: 
		"""
		pass

	@property
	def PressureUnit(self) -> IUnit:
		"""No Description

		Returns:
			ISpotElevationUnits: 
		"""
		pass

class ISpotElevation(IWaterNetworkElement[ISpotElevations, ISpotElevation, ISpotElevationUnits, ISpotElevationInput, ISpotElevationResults, ISpotElevationsInput, ISpotElevationsResults]):

	def __init__(self) -> None:
		"""Creating a new Instance of this class is not allowed


		Raises:
			Exception: if this class is instanciated
		"""
		raise Exception("Creating a new Instance of this class is not allowed")
		pass

class ISpotElevations(IWaterNetworkElements[ISpotElevations, ISpotElevation, ISpotElevationUnits, ISpotElevationInput, ISpotElevationResults, ISpotElevationsInput, ISpotElevationsResults]):

	def __init__(self) -> None:
		"""Creating a new Instance of this class is not allowed


		Raises:
			Exception: if this class is instanciated
		"""
		raise Exception("Creating a new Instance of this class is not allowed")
		pass

class ICustomerMeterInput(IPhysicalNodeElementInput):

	def __init__(self) -> None:
		"""Creating a new Instance of this class is not allowed


		Raises:
			Exception: if this class is instanciated
		"""
		raise Exception("Creating a new Instance of this class is not allowed")
		pass

	@property
	def DemandPattern(self) -> IPattern:
		"""No Description

		Returns:
			ICustomerMeterInput: 
		"""
		pass

	@property
	def BaseDemand(self) -> float:
		"""No Description

		Returns:
			ICustomerMeterInput: 
		"""
		pass

	@property
	def StartDemandDistribution(self) -> float:
		"""No Description

		Returns:
			ICustomerMeterInput: 
		"""
		pass

	@property
	def AssociatedElement(self) -> IWaterElement:
		"""No Description

		Returns:
			ICustomerMeterInput: 
		"""
		pass

	@property
	def UnitDemand(self) -> IUnitDemandLoad:
		"""No Description

		Returns:
			ICustomerMeterInput: 
		"""
		pass

	@property
	def UnitDemandPattern(self) -> IPattern:
		"""No Description

		Returns:
			ICustomerMeterInput: 
		"""
		pass

	@property
	def NumberOfUnitDemands(self) -> float:
		"""No Description

		Returns:
			ICustomerMeterInput: 
		"""
		pass

	@DemandPattern.setter
	def DemandPattern(self, demandpattern: IPattern) -> None:
		pass

	@BaseDemand.setter
	def BaseDemand(self, basedemand: float) -> None:
		pass

	@StartDemandDistribution.setter
	def StartDemandDistribution(self, startdemanddistribution: float) -> None:
		pass

	@AssociatedElement.setter
	def AssociatedElement(self, associatedelement: IWaterElement) -> None:
		pass

	@UnitDemand.setter
	def UnitDemand(self, unitdemand: IUnitDemandLoad) -> None:
		pass

	@UnitDemandPattern.setter
	def UnitDemandPattern(self, unitdemandpattern: IPattern) -> None:
		pass

	@NumberOfUnitDemands.setter
	def NumberOfUnitDemands(self, numberofunitdemands: float) -> None:
		pass

class ICustomerMetersInput(IPhysicalNodeElementsInput):

	def __init__(self) -> None:
		"""Creating a new Instance of this class is not allowed


		Raises:
			Exception: if this class is instanciated
		"""
		raise Exception("Creating a new Instance of this class is not allowed")
		pass

	@overload
	def ICustomerMetersInput(self) -> Dict[int,int]:
		"""Demand patterns for all customer meters.

		Returns:
			Dict[int,int]: 
		"""
		pass

	@overload
	def ICustomerMetersInput(self, ids: List[int]) -> Dict[int,int]:
		"""No Description

		Args:
			ids(List[int]): ids

		Returns:
			Dict[int,int]: 
		"""
		pass

	@overload
	def ICustomerMetersInput(self) -> Dict[int,int]:
		"""Base demand loads for all customer meters.

		Returns:
			Dict[int,int]: 
		"""
		pass

	@overload
	def ICustomerMetersInput(self, ids: List[int]) -> Dict[int,int]:
		"""No Description

		Args:
			ids(List[int]): ids

		Returns:
			Dict[int,int]: 
		"""
		pass

	@overload
	def ICustomerMetersInput(self) -> Dict[int,int]:
		"""Start demand distributions for all customer meters.

		Returns:
			Dict[int,int]: 
		"""
		pass

	@overload
	def ICustomerMetersInput(self, ids: List[int]) -> Dict[int,int]:
		"""No Description

		Args:
			ids(List[int]): ids

		Returns:
			Dict[int,int]: 
		"""
		pass

	@overload
	def ICustomerMetersInput(self) -> Dict[int,int]:
		"""Associated elements for all customer meters

		Returns:
			Dict[int,int]: 
		"""
		pass

	@overload
	def ICustomerMetersInput(self, ids: List[int]) -> Dict[int,int]:
		"""No Description

		Args:
			ids(List[int]): ids

		Returns:
			Dict[int,int]: 
		"""
		pass

	@overload
	def ICustomerMetersInput(self) -> Dict[int,int]:
		"""Unit demands for all customer meters.

		Returns:
			Dict[int,int]: 
		"""
		pass

	@overload
	def ICustomerMetersInput(self, ids: List[int]) -> Dict[int,int]:
		"""No Description

		Args:
			ids(List[int]): ids

		Returns:
			Dict[int,int]: 
		"""
		pass

	@overload
	def ICustomerMetersInput(self) -> Dict[int,int]:
		"""Unit demand patterns for all customer meters.

		Returns:
			Dict[int,int]: 
		"""
		pass

	@overload
	def ICustomerMetersInput(self, ids: List[int]) -> Dict[int,int]:
		"""No Description

		Args:
			ids(List[int]): ids

		Returns:
			Dict[int,int]: 
		"""
		pass

	@overload
	def ICustomerMetersInput(self) -> Dict[int,int]:
		"""Number of unit demands for all customer meters.

		Returns:
			Dict[int,int]: 
		"""
		pass

	@overload
	def ICustomerMetersInput(self, ids: List[int]) -> Dict[int,int]:
		"""No Description

		Args:
			ids(List[int]): ids

		Returns:
			Dict[int,int]: 
		"""
		pass

class ICustomerMeterResults(IElementResults):

	def __init__(self) -> None:
		"""Creating a new Instance of this class is not allowed


		Raises:
			Exception: if this class is instanciated
		"""
		raise Exception("Creating a new Instance of this class is not allowed")
		pass

	@overload
	def ICustomerMeterResults(self) -> Union[float, None]:
		"""Calculated hydraulic grade at node at current time step.

		Returns:
			Nullable: 
		"""
		pass

	@overload
	def ICustomerMeterResults(self, timeStepIndex: int) -> Union[float, None]:
		"""Calculated hydraulic grade at node at given time step.

		Args:
			timeStepIndex(int): timeStepIndex

		Returns:
			Nullable: 
		"""
		pass

	@overload
	def ICustomerMeterResults(self) -> Union[float, None]:
		"""Calculated pressure at customer meter for current time step. This result is only computed when the calculation option 'Calculate Customer Results?' is set to true.

		Returns:
			Nullable: 
		"""
		pass

	@overload
	def ICustomerMeterResults(self, timeStepIndex: int) -> Union[float, None]:
		"""Calculated pressure at customer meter at given time step. This result is only computed when the calculation option 'Calculate Customer Results?' is set to true.

		Args:
			timeStepIndex(int): timeStepIndex

		Returns:
			Nullable: 
		"""
		pass

	def HydraulicGrades(self) -> array(Union[float, None]):
		"""Calculated hydraulic grade at node across all time steps.

		Returns:
			array(): 
		"""
		pass

	def Pressures(self) -> array(Union[float, None]):
		"""Calculated pressure at customer meter across all time steps. This result is only computed when the calculation option 'Calculate Customer Results?' is set to true.

		Returns:
			array(): 
		"""
		pass

class ICustomerMetersResults(IElementsResults):

	def __init__(self) -> None:
		"""Creating a new Instance of this class is not allowed


		Raises:
			Exception: if this class is instanciated
		"""
		raise Exception("Creating a new Instance of this class is not allowed")
		pass

	@overload
	def ICustomerMetersResults(self) -> Dict[int,int]:
		"""Calculated hydraulic grade at node at current time step for all customer meters.

		Returns:
			Dict[int,int]: 
		"""
		pass

	@overload
	def ICustomerMetersResults(self, timeStepIndex: int) -> Dict[int,int]:
		"""Calculated hydraulic grade at node at given time step for all customer meters

		Args:
			timeStepIndex(int): timeStepIndex

		Returns:
			Dict[int,int]: 
		"""
		pass

	@overload
	def ICustomerMetersResults(self, ids: List[int], timeStepIndex: int) -> Dict[int,int]:
		"""No Description

		Args:
			ids(List[int]): ids
			timeStepIndex(int): timeStepIndex

		Returns:
			Dict[int,int]: 
		"""
		pass

	@overload
	def ICustomerMetersResults(self) -> Dict[int,int]:
		"""Calculated pressure at customer meter for current time step for all customer meters.

		Returns:
			Dict[int,int]: 
		"""
		pass

	@overload
	def ICustomerMetersResults(self, timeStepIndex: int) -> Dict[int,int]:
		"""Calculated pressure at customer meter for given time step for all customer meters

		Args:
			timeStepIndex(int): timeStepIndex

		Returns:
			Dict[int,int]: 
		"""
		pass

	@overload
	def ICustomerMetersResults(self, ids: List[int], timeStepIndex: int) -> Dict[int,int]:
		"""No Description

		Args:
			ids(List[int]): ids
			timeStepIndex(int): timeStepIndex

		Returns:
			Dict[int,int]: 
		"""
		pass

class ICustomerMeterUnits(IGeometryUnits):

	def __init__(self) -> None:
		"""Creating a new Instance of this class is not allowed


		Raises:
			Exception: if this class is instanciated
		"""
		raise Exception("Creating a new Instance of this class is not allowed")
		pass

	@property
	def ElevationUnit(self) -> IUnit:
		"""No Description

		Returns:
			ICustomerMeterUnits: 
		"""
		pass

	@property
	def HydraulicGradeUnit(self) -> IUnit:
		"""No Description

		Returns:
			ICustomerMeterUnits: 
		"""
		pass

	@property
	def PressureUnit(self) -> IUnit:
		"""No Description

		Returns:
			ICustomerMeterUnits: 
		"""
		pass

class ICustomerMeter(IWaterNetworkElement[ICustomerMeters, ICustomerMeter, ICustomerMeterUnits, ICustomerMeterInput, ICustomerMeterResults, ICustomerMetersInput, ICustomerMetersResults]):

	def __init__(self) -> None:
		"""Creating a new Instance of this class is not allowed


		Raises:
			Exception: if this class is instanciated
		"""
		raise Exception("Creating a new Instance of this class is not allowed")
		pass

class ICustomerMeters(IWaterNetworkElements[ICustomerMeters, ICustomerMeter, ICustomerMeterUnits, ICustomerMeterInput, ICustomerMeterResults, ICustomerMetersInput, ICustomerMetersResults]):

	def __init__(self) -> None:
		"""Creating a new Instance of this class is not allowed


		Raises:
			Exception: if this class is instanciated
		"""
		raise Exception("Creating a new Instance of this class is not allowed")
		pass

class ISCADAElementInput(IPointNodeInput):

	def __init__(self) -> None:
		"""Creating a new Instance of this class is not allowed


		Raises:
			Exception: if this class is instanciated
		"""
		raise Exception("Creating a new Instance of this class is not allowed")
		pass

	@property
	def TargetElement(self) -> IWaterElement:
		"""No Description

		Returns:
			ISCADAElementInput: 
		"""
		pass

	@property
	def RealtimeSignal(self) -> ISCADASignal:
		"""No Description

		Returns:
			ISCADAElementInput: 
		"""
		pass

	@property
	def HistoricalSignal(self) -> ISCADASignal:
		"""No Description

		Returns:
			ISCADAElementInput: 
		"""
		pass

	@property
	def TargetAttribute(self) -> SCADATargetAttribute:
		"""No Description

		Returns:
			ISCADAElementInput: 
		"""
		pass

	@TargetElement.setter
	def TargetElement(self, targetelement: IWaterElement) -> None:
		pass

	@RealtimeSignal.setter
	def RealtimeSignal(self, realtimesignal: ISCADASignal) -> None:
		pass

	@HistoricalSignal.setter
	def HistoricalSignal(self, historicalsignal: ISCADASignal) -> None:
		pass

	@TargetAttribute.setter
	def TargetAttribute(self, targetattribute: SCADATargetAttribute) -> None:
		pass

class ISCADAElementsInput(IPointNodesInput):

	def __init__(self) -> None:
		"""Creating a new Instance of this class is not allowed


		Raises:
			Exception: if this class is instanciated
		"""
		raise Exception("Creating a new Instance of this class is not allowed")
		pass

	@overload
	def ISCADAElementsInput(self) -> Dict[int,int]:
		"""The domain elements the SCADA elements target.

		Returns:
			Dict[int,int]: 
		"""
		pass

	@overload
	def ISCADAElementsInput(self, ids: List[int]) -> Dict[int,int]:
		"""No Description

		Args:
			ids(List[int]): ids

		Returns:
			Dict[int,int]: 
		"""
		pass

	@overload
	def ISCADAElementsInput(self) -> Dict[int,int]:
		"""The assigned real-time signals

		Returns:
			Dict[int,int]: 
		"""
		pass

	@overload
	def ISCADAElementsInput(self, ids: List[int]) -> Dict[int,int]:
		"""No Description

		Args:
			ids(List[int]): ids

		Returns:
			Dict[int,int]: 
		"""
		pass

	@overload
	def ISCADAElementsInput(self) -> Dict[int,int]:
		"""The assigned historical signals

		Returns:
			Dict[int,int]: 
		"""
		pass

	@overload
	def ISCADAElementsInput(self, ids: List[int]) -> Dict[int,int]:
		"""No Description

		Args:
			ids(List[int]): ids

		Returns:
			Dict[int,int]: 
		"""
		pass

class ISCADAElement(IWaterNetworkElement[ISCADAElements, ISCADAElement, IGeometryUnits, ISCADAElementInput, IElementResults, ISCADAElementsInput, IElementsResults]):

	def __init__(self) -> None:
		"""Creating a new Instance of this class is not allowed


		Raises:
			Exception: if this class is instanciated
		"""
		raise Exception("Creating a new Instance of this class is not allowed")
		pass

class ISCADAElements(IWaterNetworkElements[ISCADAElements, ISCADAElement, IGeometryUnits, ISCADAElementInput, IElementResults, ISCADAElementsInput, IElementsResults]):

	def __init__(self) -> None:
		"""Creating a new Instance of this class is not allowed


		Raises:
			Exception: if this class is instanciated
		"""
		raise Exception("Creating a new Instance of this class is not allowed")
		pass

class IPumpStations(IWaterNetworkElements[IPumpStations, IPumpStation, IPumpStationUnits, IPumpStationInput, IPumpStationResults, IPumpStationsInput, IPumpStationsResults]):

	def __init__(self) -> None:
		"""Creating a new Instance of this class is not allowed


		Raises:
			Exception: if this class is instanciated
		"""
		raise Exception("Creating a new Instance of this class is not allowed")
		pass

class IPumpStation(IWaterNetworkElement[IPumpStations, IPumpStation, IPumpStationUnits, IPumpStationInput, IPumpStationResults, IPumpStationsInput, IPumpStationsResults]):

	def __init__(self) -> None:
		"""Creating a new Instance of this class is not allowed


		Raises:
			Exception: if this class is instanciated
		"""
		raise Exception("Creating a new Instance of this class is not allowed")
		pass

class IPumpStationUnits(IGeometryUnits):

	def __init__(self) -> None:
		"""Creating a new Instance of this class is not allowed


		Raises:
			Exception: if this class is instanciated
		"""
		raise Exception("Creating a new Instance of this class is not allowed")
		pass

class IPumpStationsInput(IBasePolygonsInput):

	def __init__(self) -> None:
		"""Creating a new Instance of this class is not allowed


		Raises:
			Exception: if this class is instanciated
		"""
		raise Exception("Creating a new Instance of this class is not allowed")
		pass

class IPumpStationsResults(IBasePolygonsResults):

	def __init__(self) -> None:
		"""Creating a new Instance of this class is not allowed


		Raises:
			Exception: if this class is instanciated
		"""
		raise Exception("Creating a new Instance of this class is not allowed")
		pass

class IPumpStationResults(IBasePolygonResults):

	def __init__(self) -> None:
		"""Creating a new Instance of this class is not allowed


		Raises:
			Exception: if this class is instanciated
		"""
		raise Exception("Creating a new Instance of this class is not allowed")
		pass

class IPumpStationInput(IBasePolygonInput):

	def __init__(self) -> None:
		"""Creating a new Instance of this class is not allowed


		Raises:
			Exception: if this class is instanciated
		"""
		raise Exception("Creating a new Instance of this class is not allowed")
		pass

	@property
	def Pumps(self) -> IPumpStationPumpIDsCollection:
		"""No Description

		Returns:
			IPumpStationInput: 
		"""
		pass

class IPumpStationPumpIDsCollection(ICollectionElements[IPumpStationPumpIDs, IPumpStationPumpID, IElementUnits]):

	def __init__(self) -> None:
		"""Creating a new Instance of this class is not allowed


		Raises:
			Exception: if this class is instanciated
		"""
		raise Exception("Creating a new Instance of this class is not allowed")
		pass

class IPumpStationPumpIDs(ICollection[IPumpStationPumpID]):

	def __init__(self) -> None:
		"""Creating a new Instance of this class is not allowed


		Raises:
			Exception: if this class is instanciated
		"""
		raise Exception("Creating a new Instance of this class is not allowed")
		pass

	def Add(self, pump: IPump, pumpDefinition: IPumpDefinition) -> IPumpStationPumpID:
		"""Adds a pump to the pump station.

		Args:
			pump(IPump): The pump to associate with the pump station.
			pumpDefinition(IPumpDefinition): The pump definition to use with this pump.

		Returns:
			IPumpStationPumpID: 
		"""
		pass

class IPumpStationPumpID(ICollectionElement):

	def __init__(self) -> None:
		"""Creating a new Instance of this class is not allowed


		Raises:
			Exception: if this class is instanciated
		"""
		raise Exception("Creating a new Instance of this class is not allowed")
		pass

	@property
	def Pump(self) -> IElement:
		"""No Description

		Returns:
			IPumpStationPumpID: 
		"""
		pass

	@property
	def PumpDefinition(self) -> IPumpDefinition:
		"""No Description

		Returns:
			IPumpStationPumpID: 
		"""
		pass

	@Pump.setter
	def Pump(self, pump: IElement) -> None:
		pass

	@PumpDefinition.setter
	def PumpDefinition(self, pumpdefinition: IPumpDefinition) -> None:
		pass

