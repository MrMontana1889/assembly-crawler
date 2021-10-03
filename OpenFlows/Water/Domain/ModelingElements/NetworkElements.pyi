from OpenFlows.Domain.ModelingElements.Collections import ICollectionElement, ICollection, ICollectionElements
from OpenFlows.Water.Domain.ModelingElements.Components import IMinorLossCoefficient, IPattern, IPumpDefinition, IValveCharacteristic, IGPVHeadlossCurve, IZone, IUnitDemandLoad, IAirFlowCurve, ISCADASignal
from typing import Generic, overload, Dict, List, Union, TypeVar
from OpenFlows.Domain.ModelingElements import IElementUnits, IElementsResults, IElementResults, IElement, IGeometryUnits, TElementManagerType, TElementType, TUnitsType
from array import array
from OpenFlows.Units import IUnit
from OpenFlows.Domain.ModelingElements.NetworkElements import INetworkElements, TElementInputType, TElementResultsType, TElementsInputType, TElementsResultsType, IActiveElementInput, IActiveElementsInput, INetworkElement, IBaseLinksResults, IBaseLinkResults, IBaseLinkInput, IBaseLinksInput, IBaseLinkUnits, IPointNodeInput, IPointNodesInput, IBasePolygonsInput, IBasePolygonsResults, IBasePolygonResults, IBasePolygonInput
from OpenFlows.Domain.DataObjects import INetwork


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
		"""
		Returns:
			int: No Description
		"""
		pass

	@property
	def MinorLossCoefficient(self) -> IMinorLossCoefficient:
		"""
		Returns:
			IMinorLossCoefficient: No Description
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
		"""Method Description

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
		"""Method Description

		Returns:
			Dict[int,int]: 
		"""
		pass

	@overload
	def IBaseDirectedNodesResults(self, timeStepIndex: int) -> Dict[int,int]:
		"""Method Description

		Args:
			timeStepIndex(int): timeStepIndex

		Returns:
			Dict[int,int]: 
		"""
		pass

	@overload
	def IBaseDirectedNodesResults(self, ids: List[int], timeStepIndex: int) -> Dict[int,int]:
		"""Method Description

		Args:
			ids(List[int]): ids
			timeStepIndex(int): timeStepIndex

		Returns:
			Dict[int,int]: 
		"""
		pass

	@overload
	def IBaseDirectedNodesResults(self) -> Dict[int,int]:
		"""Method Description

		Returns:
			Dict[int,int]: 
		"""
		pass

	@overload
	def IBaseDirectedNodesResults(self, timeStepIndex: int) -> Dict[int,int]:
		"""Method Description

		Args:
			timeStepIndex(int): timeStepIndex

		Returns:
			Dict[int,int]: 
		"""
		pass

	@overload
	def IBaseDirectedNodesResults(self, ids: List[int], timeStepIndex: int) -> Dict[int,int]:
		"""Method Description

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
		"""Method Description

		Returns:
			Nullable: 
		"""
		pass

	@overload
	def IBaseDirectedNodeResults(self, timeStepIndex: int) -> Union[bool, None]:
		"""Method Description

		Args:
			timeStepIndex(int): timeStepIndex

		Returns:
			Nullable: 
		"""
		pass

	@overload
	def IBaseDirectedNodeResults(self) -> Union[bool, None]:
		"""Method Description

		Returns:
			Nullable: 
		"""
		pass

	@overload
	def IBaseDirectedNodeResults(self, timeStepIndex: int) -> Union[bool, None]:
		"""Method Description

		Args:
			timeStepIndex(int): timeStepIndex

		Returns:
			Nullable: 
		"""
		pass

	def CannotDeliverFlowsOrHeads(self) -> array(Union[bool, None]):
		"""Method Description

		Returns:
			Nullable[]: 
		"""
		pass

	def IsOpens(self) -> array(Union[bool, None]):
		"""Method Description

		Returns:
			Nullable[]: 
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
		"""
		Returns:
			IElement: No Description
		"""
		pass

	@property
	def InstallationYear(self) -> int:
		"""
		Returns:
			int: No Description
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
		"""Method Description

		Returns:
			Dict[int,int]: 
		"""
		pass

	@overload
	def IBaseDirectedNodesInput(self, ids: List[int]) -> Dict[int,int]:
		"""Method Description

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
		"""
		Returns:
			IUnit: No Description
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
		"""
		Returns:
			bool: No Description
		"""
		pass

	@property
	def CheckValvePipeWithWye(self) -> IPipe:
		"""
		Returns:
			IPipe: No Description
		"""
		pass

	@property
	def FlowDirection(self) -> CheckValveFlowDirectionEnum:
		"""
		Returns:
			CheckValveFlowDirectionEnum: No Description
		"""
		pass

	@property
	def InitialTypicalFlow(self) -> float:
		"""
		Returns:
			float: No Description
		"""
		pass

	@property
	def ThresholdPressure(self) -> float:
		"""
		Returns:
			float: No Description
		"""
		pass

	@property
	def ClosureTime(self) -> float:
		"""
		Returns:
			float: No Description
		"""
		pass

	@property
	def OpenTime(self) -> float:
		"""
		Returns:
			float: No Description
		"""
		pass

	@property
	def AllowDisruptionOfOperation(self) -> bool:
		"""
		Returns:
			bool: No Description
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
		"""Method Description

		Returns:
			Dict[int,int]: 
		"""
		pass

	@overload
	def ICheckValveElementsInput(self, ids: List[int]) -> Dict[int,int]:
		"""Method Description

		Args:
			ids(List[int]): ids

		Returns:
			Dict[int,int]: 
		"""
		pass

	@overload
	def ICheckValveElementsInput(self) -> Dict[int,int]:
		"""Method Description

		Returns:
			Dict[int,int]: 
		"""
		pass

	@overload
	def ICheckValveElementsInput(self, ids: List[int]) -> Dict[int,int]:
		"""Method Description

		Args:
			ids(List[int]): ids

		Returns:
			Dict[int,int]: 
		"""
		pass

	@overload
	def ICheckValveElementsInput(self) -> Dict[int,int]:
		"""Method Description

		Returns:
			Dict[int,int]: 
		"""
		pass

	@overload
	def ICheckValveElementsInput(self, ids: List[int]) -> Dict[int,int]:
		"""Method Description

		Args:
			ids(List[int]): ids

		Returns:
			Dict[int,int]: 
		"""
		pass

	@overload
	def ICheckValveElementsInput(self) -> Dict[int,int]:
		"""Method Description

		Returns:
			Dict[int,int]: 
		"""
		pass

	@overload
	def ICheckValveElementsInput(self, ids: List[int]) -> Dict[int,int]:
		"""Method Description

		Args:
			ids(List[int]): ids

		Returns:
			Dict[int,int]: 
		"""
		pass

	@overload
	def ICheckValveElementsInput(self) -> Dict[int,int]:
		"""Method Description

		Returns:
			Dict[int,int]: 
		"""
		pass

	@overload
	def ICheckValveElementsInput(self, ids: List[int]) -> Dict[int,int]:
		"""Method Description

		Args:
			ids(List[int]): ids

		Returns:
			Dict[int,int]: 
		"""
		pass

	@overload
	def ICheckValveElementsInput(self) -> Dict[int,int]:
		"""Method Description

		Returns:
			Dict[int,int]: 
		"""
		pass

	@overload
	def ICheckValveElementsInput(self, ids: List[int]) -> Dict[int,int]:
		"""Method Description

		Args:
			ids(List[int]): ids

		Returns:
			Dict[int,int]: 
		"""
		pass

	@overload
	def ICheckValveElementsInput(self) -> Dict[int,int]:
		"""Method Description

		Returns:
			Dict[int,int]: 
		"""
		pass

	@overload
	def ICheckValveElementsInput(self, ids: List[int]) -> Dict[int,int]:
		"""Method Description

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
		"""Method Description

		Returns:
			Nullable: 
		"""
		pass

	@overload
	def ICheckValveElementResults(self, timeStepIndex: int) -> Union[float, None]:
		"""Method Description

		Args:
			timeStepIndex(int): timeStepIndex

		Returns:
			Nullable: 
		"""
		pass

	@overload
	def ICheckValveElementResults(self) -> Union[float, None]:
		"""Method Description

		Returns:
			Nullable: 
		"""
		pass

	@overload
	def ICheckValveElementResults(self, timeStepIndex: int) -> Union[float, None]:
		"""Method Description

		Args:
			timeStepIndex(int): timeStepIndex

		Returns:
			Nullable: 
		"""
		pass

	@overload
	def ICheckValveElementResults(self) -> Union[float, None]:
		"""Method Description

		Returns:
			Nullable: 
		"""
		pass

	@overload
	def ICheckValveElementResults(self, timeStepIndex: int) -> Union[float, None]:
		"""Method Description

		Args:
			timeStepIndex(int): timeStepIndex

		Returns:
			Nullable: 
		"""
		pass

	@overload
	def ICheckValveElementResults(self) -> Union[float, None]:
		"""Method Description

		Returns:
			Nullable: 
		"""
		pass

	@overload
	def ICheckValveElementResults(self, timeStepIndex: int) -> Union[float, None]:
		"""Method Description

		Args:
			timeStepIndex(int): timeStepIndex

		Returns:
			Nullable: 
		"""
		pass

	def Flows(self) -> array(Union[float, None]):
		"""Method Description

		Returns:
			Nullable[]: 
		"""
		pass

	def AbsoluteFlows(self) -> array(Union[float, None]):
		"""Method Description

		Returns:
			Nullable[]: 
		"""
		pass

	def Pressures(self) -> array(Union[float, None]):
		"""Method Description

		Returns:
			Nullable[]: 
		"""
		pass

	def HydraulicGrades(self) -> array(Union[float, None]):
		"""Method Description

		Returns:
			Nullable[]: 
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
		"""Method Description

		Returns:
			Dict[int,int]: 
		"""
		pass

	@overload
	def ICheckValveElementsResults(self, timeStepIndex: int) -> Dict[int,int]:
		"""Method Description

		Args:
			timeStepIndex(int): timeStepIndex

		Returns:
			Dict[int,int]: 
		"""
		pass

	@overload
	def ICheckValveElementsResults(self, ids: List[int], timeStepIndex: int) -> Dict[int,int]:
		"""Method Description

		Args:
			ids(List[int]): ids
			timeStepIndex(int): timeStepIndex

		Returns:
			Dict[int,int]: 
		"""
		pass

	@overload
	def ICheckValveElementsResults(self) -> Dict[int,int]:
		"""Method Description

		Returns:
			Dict[int,int]: 
		"""
		pass

	@overload
	def ICheckValveElementsResults(self, timeStepIndex: int) -> Dict[int,int]:
		"""Method Description

		Args:
			timeStepIndex(int): timeStepIndex

		Returns:
			Dict[int,int]: 
		"""
		pass

	@overload
	def ICheckValveElementsResults(self, ids: List[int], timeStepIndex: int) -> Dict[int,int]:
		"""Method Description

		Args:
			ids(List[int]): ids
			timeStepIndex(int): timeStepIndex

		Returns:
			Dict[int,int]: 
		"""
		pass

	@overload
	def ICheckValveElementsResults(self) -> Dict[int,int]:
		"""Method Description

		Returns:
			Dict[int,int]: 
		"""
		pass

	@overload
	def ICheckValveElementsResults(self, timeStepIndex: int) -> Dict[int,int]:
		"""Method Description

		Args:
			timeStepIndex(int): timeStepIndex

		Returns:
			Dict[int,int]: 
		"""
		pass

	@overload
	def ICheckValveElementsResults(self, ids: List[int], timeSTepIndex: int) -> Dict[int,int]:
		"""Method Description

		Args:
			ids(List[int]): ids
			timeSTepIndex(int): timeSTepIndex

		Returns:
			Dict[int,int]: 
		"""
		pass

	@overload
	def ICheckValveElementsResults(self) -> Dict[int,int]:
		"""Method Description

		Returns:
			Dict[int,int]: 
		"""
		pass

	@overload
	def ICheckValveElementsResults(self, timeStepIndex: int) -> Dict[int,int]:
		"""Method Description

		Args:
			timeStepIndex(int): timeStepIndex

		Returns:
			Dict[int,int]: 
		"""
		pass

	@overload
	def ICheckValveElementsResults(self, ids: List[int], timeStepIndex: int) -> Dict[int,int]:
		"""Method Description

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
	def HydraulicGradeUnit(self) -> IUnit:
		"""
		Returns:
			IUnit: No Description
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
		"""
		Returns:
			float: No Description
		"""
		pass

	@property
	def TypicalFlow(self) -> float:
		"""
		Returns:
			float: No Description
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
		"""Method Description

		Returns:
			Dict[int,int]: 
		"""
		pass

	def TypicalFlows(self) -> Dict[int,int]:
		"""Method Description

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
		"""Method Description

		Returns:
			Nullable: 
		"""
		pass

	@overload
	def IOrificeBetweenTwoPipesResults(self, timeStepIndex: int) -> Union[float, None]:
		"""Method Description

		Args:
			timeStepIndex(int): timeStepIndex

		Returns:
			Nullable: 
		"""
		pass

	@overload
	def IOrificeBetweenTwoPipesResults(self) -> Union[float, None]:
		"""Method Description

		Returns:
			Nullable: 
		"""
		pass

	@overload
	def IOrificeBetweenTwoPipesResults(self, timeStepIndex: int) -> Union[float, None]:
		"""Method Description

		Args:
			timeStepIndex(int): timeStepIndex

		Returns:
			Nullable: 
		"""
		pass

	@overload
	def IOrificeBetweenTwoPipesResults(self) -> Union[float, None]:
		"""Method Description

		Returns:
			Nullable: 
		"""
		pass

	@overload
	def IOrificeBetweenTwoPipesResults(self, timeStepIndex: int) -> Union[float, None]:
		"""Method Description

		Args:
			timeStepIndex(int): timeStepIndex

		Returns:
			Nullable: 
		"""
		pass

	@overload
	def IOrificeBetweenTwoPipesResults(self) -> Union[float, None]:
		"""Method Description

		Returns:
			Nullable: 
		"""
		pass

	@overload
	def IOrificeBetweenTwoPipesResults(self, timeStepIndex: int) -> Union[float, None]:
		"""Method Description

		Args:
			timeStepIndex(int): timeStepIndex

		Returns:
			Nullable: 
		"""
		pass

	@overload
	def IOrificeBetweenTwoPipesResults(self) -> Union[float, None]:
		"""Method Description

		Returns:
			Nullable: 
		"""
		pass

	@overload
	def IOrificeBetweenTwoPipesResults(self, timeStepIndex: int) -> Union[float, None]:
		"""Method Description

		Args:
			timeStepIndex(int): timeStepIndex

		Returns:
			Nullable: 
		"""
		pass

	@overload
	def IOrificeBetweenTwoPipesResults(self) -> Union[float, None]:
		"""Method Description

		Returns:
			Nullable: 
		"""
		pass

	@overload
	def IOrificeBetweenTwoPipesResults(self, timeStepIndex: int) -> Union[float, None]:
		"""Method Description

		Args:
			timeStepIndex(int): timeStepIndex

		Returns:
			Nullable: 
		"""
		pass

	@overload
	def IOrificeBetweenTwoPipesResults(self) -> Union[float, None]:
		"""Method Description

		Returns:
			Nullable: 
		"""
		pass

	@overload
	def IOrificeBetweenTwoPipesResults(self, timeStepIndex: int) -> Union[float, None]:
		"""Method Description

		Args:
			timeStepIndex(int): timeStepIndex

		Returns:
			Nullable: 
		"""
		pass

	def Flows(self) -> array(Union[float, None]):
		"""Method Description

		Returns:
			Nullable[]: 
		"""
		pass

	def Headlosses(self) -> array(Union[float, None]):
		"""Method Description

		Returns:
			Nullable[]: 
		"""
		pass

	def FromHydraulicGrades(self) -> array(Union[float, None]):
		"""Method Description

		Returns:
			Nullable[]: 
		"""
		pass

	def ToHydraulicGrades(self) -> array(Union[float, None]):
		"""Method Description

		Returns:
			Nullable[]: 
		"""
		pass

	def FromPressures(self) -> array(Union[float, None]):
		"""Method Description

		Returns:
			Nullable[]: 
		"""
		pass

	def ToPressures(self) -> array(Union[float, None]):
		"""Method Description

		Returns:
			Nullable[]: 
		"""
		pass

	def AbsoluteFlows(self) -> array(Union[float, None]):
		"""Method Description

		Returns:
			Nullable[]: 
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
		"""Method Description

		Returns:
			Dict[int,int]: 
		"""
		pass

	@overload
	def IOrificesBetweenTwoPipesResults(self, timeStepIndex: int) -> Dict[int,int]:
		"""Method Description

		Args:
			timeStepIndex(int): timeStepIndex

		Returns:
			Dict[int,int]: 
		"""
		pass

	@overload
	def IOrificesBetweenTwoPipesResults(self, ids: List[int], timeStepIndex: int) -> Dict[int,int]:
		"""Method Description

		Args:
			ids(List[int]): ids
			timeStepIndex(int): timeStepIndex

		Returns:
			Dict[int,int]: 
		"""
		pass

	@overload
	def IOrificesBetweenTwoPipesResults(self) -> Dict[int,int]:
		"""Method Description

		Returns:
			Dict[int,int]: 
		"""
		pass

	@overload
	def IOrificesBetweenTwoPipesResults(self, timeStepIndex: int) -> Dict[int,int]:
		"""Method Description

		Args:
			timeStepIndex(int): timeStepIndex

		Returns:
			Dict[int,int]: 
		"""
		pass

	@overload
	def IOrificesBetweenTwoPipesResults(self, ids: List[int], timeStepIndex: int) -> Dict[int,int]:
		"""Method Description

		Args:
			ids(List[int]): ids
			timeStepIndex(int): timeStepIndex

		Returns:
			Dict[int,int]: 
		"""
		pass

	@overload
	def IOrificesBetweenTwoPipesResults(self) -> Dict[int,int]:
		"""Method Description

		Returns:
			Dict[int,int]: 
		"""
		pass

	@overload
	def IOrificesBetweenTwoPipesResults(self, timeStepIndex: int) -> Dict[int,int]:
		"""Method Description

		Args:
			timeStepIndex(int): timeStepIndex

		Returns:
			Dict[int,int]: 
		"""
		pass

	@overload
	def IOrificesBetweenTwoPipesResults(self, ids: List[int], timeStepIndex: int) -> Dict[int,int]:
		"""Method Description

		Args:
			ids(List[int]): ids
			timeStepIndex(int): timeStepIndex

		Returns:
			Dict[int,int]: 
		"""
		pass

	@overload
	def IOrificesBetweenTwoPipesResults(self) -> Dict[int,int]:
		"""Method Description

		Returns:
			Dict[int,int]: 
		"""
		pass

	@overload
	def IOrificesBetweenTwoPipesResults(self, timeStepIndex: int) -> Dict[int,int]:
		"""Method Description

		Args:
			timeStepIndex(int): timeStepIndex

		Returns:
			Dict[int,int]: 
		"""
		pass

	@overload
	def IOrificesBetweenTwoPipesResults(self, ids: List[int], timeStepIndex: int) -> Dict[int,int]:
		"""Method Description

		Args:
			ids(List[int]): ids
			timeStepIndex(int): timeStepIndex

		Returns:
			Dict[int,int]: 
		"""
		pass

	@overload
	def IOrificesBetweenTwoPipesResults(self) -> Dict[int,int]:
		"""Method Description

		Returns:
			Dict[int,int]: 
		"""
		pass

	@overload
	def IOrificesBetweenTwoPipesResults(self, timeStepIndex: int) -> Dict[int,int]:
		"""Method Description

		Args:
			timeStepIndex(int): timeStepIndex

		Returns:
			Dict[int,int]: 
		"""
		pass

	@overload
	def IOrificesBetweenTwoPipesResults(self, ids: List[int], timeStepIndex: int) -> Dict[int,int]:
		"""Method Description

		Args:
			ids(List[int]): ids
			timeStepIndex(int): timeStepIndex

		Returns:
			Dict[int,int]: 
		"""
		pass

	@overload
	def IOrificesBetweenTwoPipesResults(self) -> Dict[int,int]:
		"""Method Description

		Returns:
			Dict[int,int]: 
		"""
		pass

	@overload
	def IOrificesBetweenTwoPipesResults(self, timeStepIndex: int) -> Dict[int,int]:
		"""Method Description

		Args:
			timeStepIndex(int): timeStepIndex

		Returns:
			Dict[int,int]: 
		"""
		pass

	@overload
	def IOrificesBetweenTwoPipesResults(self, ids: List[int], timeStepIndex: int) -> Dict[int,int]:
		"""Method Description

		Args:
			ids(List[int]): ids
			timeStepIndex(int): timeStepIndex

		Returns:
			Dict[int,int]: 
		"""
		pass

	@overload
	def IOrificesBetweenTwoPipesResults(self, timeStepIndex: int) -> Dict[int,int]:
		"""Method Description

		Args:
			timeStepIndex(int): timeStepIndex

		Returns:
			Dict[int,int]: 
		"""
		pass

	@overload
	def IOrificesBetweenTwoPipesResults(self, ids: List[int], timeStepIndex: int) -> Dict[int,int]:
		"""Method Description

		Args:
			ids(List[int]): ids
			timeStepIndex(int): timeStepIndex

		Returns:
			Dict[int,int]: 
		"""
		pass

	def AbsolueFlow(self) -> Dict[int,int]:
		"""Method Description

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
		"""
		Returns:
			IUnit: No Description
		"""
		pass

	@property
	def HeadlossUnit(self) -> IUnit:
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
		"""Method Description

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
		"""Method Description

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
		"""
		Returns:
			float: No Description
		"""
		pass

	@property
	def Torque(self) -> float:
		"""
		Returns:
			float: No Description
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
		"""
		Returns:
			IUnit: No Description
		"""
		pass

	@property
	def TorqueUnit(self) -> IUnit:
		"""
		Returns:
			IUnit: No Description
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
		"""
		Returns:
			float: No Description
		"""
		pass

	@property
	def TimeForValveToOperate(self) -> float:
		"""
		Returns:
			float: No Description
		"""
		pass

	@property
	def SphericalValveDiameter(self) -> float:
		"""
		Returns:
			float: No Description
		"""
		pass

	@property
	def TurbineEfficiency(self) -> float:
		"""
		Returns:
			float: No Description
		"""
		pass

	@property
	def MomentOfInertia(self) -> float:
		"""
		Returns:
			float: No Description
		"""
		pass

	@property
	def RotationalSpeed(self) -> float:
		"""
		Returns:
			float: No Description
		"""
		pass

	@property
	def GateOpeningPattern(self) -> IPattern:
		"""
		Returns:
			IPattern: No Description
		"""
		pass

	@property
	def SpecificSpeed(self) -> float:
		"""
		Returns:
			float: No Description
		"""
		pass

	@property
	def TurbineInitialFlow(self) -> float:
		"""
		Returns:
			float: No Description
		"""
		pass

	@property
	def TurbineInitialHead(self) -> float:
		"""
		Returns:
			float: No Description
		"""
		pass

	@property
	def OperatingCase(self) -> TurbineOperatingCaseEnum:
		"""
		Returns:
			TurbineOperatingCaseEnum: No Description
		"""
		pass

	@property
	def ReportPeriod(self) -> int:
		"""
		Returns:
			int: No Description
		"""
		pass

	@property
	def TurbineInitialStatus(self) -> TurbineStatusEnum:
		"""
		Returns:
			TurbineStatusEnum: No Description
		"""
		pass

	@property
	def TurbineCurveCollection(self) -> ITurbineCurveCollection:
		"""
		Returns:
			ITurbineCurveCollection: No Description
		"""
		pass

	@property
	def ElectricalTorqueCollection(self) -> IElectricalTorqueCollection:
		"""
		Returns:
			IElectricalTorqueCollection: No Description
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
		"""Method Description

		Returns:
			Dict[int,int]: 
		"""
		pass

	def TimeForValveToOperate(self) -> Dict[int,int]:
		"""Method Description

		Returns:
			Dict[int,int]: 
		"""
		pass

	def SphericalValveDiameter(self) -> Dict[int,int]:
		"""Method Description

		Returns:
			Dict[int,int]: 
		"""
		pass

	def TurbineEfficiency(self) -> Dict[int,int]:
		"""Method Description

		Returns:
			Dict[int,int]: 
		"""
		pass

	def MomentOfInertia(self) -> Dict[int,int]:
		"""Method Description

		Returns:
			Dict[int,int]: 
		"""
		pass

	def RotationalSpeed(self) -> Dict[int,int]:
		"""Method Description

		Returns:
			Dict[int,int]: 
		"""
		pass

	def GateOpeningPattern(self) -> Dict[int,int]:
		"""Method Description

		Returns:
			Dict[int,int]: 
		"""
		pass

	def SpecificSpeed(self) -> Dict[int,int]:
		"""Method Description

		Returns:
			Dict[int,int]: 
		"""
		pass

	def TurbineInitialFlow(self) -> Dict[int,int]:
		"""Method Description

		Returns:
			Dict[int,int]: 
		"""
		pass

	def TurbineInitialHead(self) -> Dict[int,int]:
		"""Method Description

		Returns:
			Dict[int,int]: 
		"""
		pass

	def OperatingCase(self) -> Dict[int,int]:
		"""Method Description

		Returns:
			Dict[int,int]: 
		"""
		pass

	def ReportPeriod(self) -> Dict[int,int]:
		"""Method Description

		Returns:
			Dict[int,int]: 
		"""
		pass

	def TurbineInitialStatus(self) -> Dict[int,int]:
		"""Method Description

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
		"""Method Description

		Returns:
			Nullable: 
		"""
		pass

	@overload
	def ITurbineResults(self, timeStepIndex: int) -> Union[float, None]:
		"""Method Description

		Args:
			timeStepIndex(int): timeStepIndex

		Returns:
			Nullable: 
		"""
		pass

	@overload
	def ITurbineResults(self) -> Union[float, None]:
		"""Method Description

		Returns:
			Nullable: 
		"""
		pass

	@overload
	def ITurbineResults(self, timeStepIndex: int) -> Union[float, None]:
		"""Method Description

		Args:
			timeStepIndex(int): timeStepIndex

		Returns:
			Nullable: 
		"""
		pass

	@overload
	def ITurbineResults(self) -> Union[float, None]:
		"""Method Description

		Returns:
			Nullable: 
		"""
		pass

	@overload
	def ITurbineResults(self, timeStepIndex: int) -> Union[float, None]:
		"""Method Description

		Args:
			timeStepIndex(int): timeStepIndex

		Returns:
			Nullable: 
		"""
		pass

	@overload
	def ITurbineResults(self) -> Union[float, None]:
		"""Method Description

		Returns:
			Nullable: 
		"""
		pass

	@overload
	def ITurbineResults(self, timeStepIndex: int) -> Union[float, None]:
		"""Method Description

		Args:
			timeStepIndex(int): timeStepIndex

		Returns:
			Nullable: 
		"""
		pass

	@overload
	def ITurbineResults(self) -> Union[float, None]:
		"""Method Description

		Returns:
			Nullable: 
		"""
		pass

	@overload
	def ITurbineResults(self, timeStepIndex: int) -> Union[float, None]:
		"""Method Description

		Args:
			timeStepIndex(int): timeStepIndex

		Returns:
			Nullable: 
		"""
		pass

	@overload
	def ITurbineResults(self) -> Union[float, None]:
		"""Method Description

		Returns:
			Nullable: 
		"""
		pass

	@overload
	def ITurbineResults(self, timeStepIndex: int) -> Union[float, None]:
		"""Method Description

		Args:
			timeStepIndex(int): timeStepIndex

		Returns:
			Nullable: 
		"""
		pass

	@overload
	def ITurbineResults(self) -> Union[float, None]:
		"""Method Description

		Returns:
			Nullable: 
		"""
		pass

	@overload
	def ITurbineResults(self, timeStepIndex: int) -> Union[float, None]:
		"""Method Description

		Args:
			timeStepIndex(int): timeStepIndex

		Returns:
			Nullable: 
		"""
		pass

	def Flows(self) -> array(Union[float, None]):
		"""Method Description

		Returns:
			Nullable[]: 
		"""
		pass

	def Headlosses(self) -> array(Union[float, None]):
		"""Method Description

		Returns:
			Nullable[]: 
		"""
		pass

	def FromHydraulicGrades(self) -> array(Union[float, None]):
		"""Method Description

		Returns:
			Nullable[]: 
		"""
		pass

	def ToHydraulicGrades(self) -> array(Union[float, None]):
		"""Method Description

		Returns:
			Nullable[]: 
		"""
		pass

	def FromPressures(self) -> array(Union[float, None]):
		"""Method Description

		Returns:
			Nullable[]: 
		"""
		pass

	def ToPressures(self) -> array(Union[float, None]):
		"""Method Description

		Returns:
			Nullable[]: 
		"""
		pass

	def AbsoluteFlows(self) -> array(Union[float, None]):
		"""Method Description

		Returns:
			Nullable[]: 
		"""
		pass

	def MaximumTransientSpeed(self) -> Union[float, None]:
		"""Method Description

		Returns:
			Nullable: 
		"""
		pass

	def MinimumTransientSpeed(self) -> Union[float, None]:
		"""Method Description

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
		"""Method Description

		Returns:
			Dict[int,int]: 
		"""
		pass

	@overload
	def ITurbinesResults(self, timeStepIndex: int) -> Dict[int,int]:
		"""Method Description

		Args:
			timeStepIndex(int): timeStepIndex

		Returns:
			Dict[int,int]: 
		"""
		pass

	@overload
	def ITurbinesResults(self, ids: List[int], timeStepIndex: int) -> Dict[int,int]:
		"""Method Description

		Args:
			ids(List[int]): ids
			timeStepIndex(int): timeStepIndex

		Returns:
			Dict[int,int]: 
		"""
		pass

	@overload
	def ITurbinesResults(self) -> Dict[int,int]:
		"""Method Description

		Returns:
			Dict[int,int]: 
		"""
		pass

	@overload
	def ITurbinesResults(self, timeStepIndex: int) -> Dict[int,int]:
		"""Method Description

		Args:
			timeStepIndex(int): timeStepIndex

		Returns:
			Dict[int,int]: 
		"""
		pass

	@overload
	def ITurbinesResults(self, ids: List[int], timeStepIndex: int) -> Dict[int,int]:
		"""Method Description

		Args:
			ids(List[int]): ids
			timeStepIndex(int): timeStepIndex

		Returns:
			Dict[int,int]: 
		"""
		pass

	@overload
	def ITurbinesResults(self) -> Dict[int,int]:
		"""Method Description

		Returns:
			Dict[int,int]: 
		"""
		pass

	@overload
	def ITurbinesResults(self, timeStepIndex: int) -> Dict[int,int]:
		"""Method Description

		Args:
			timeStepIndex(int): timeStepIndex

		Returns:
			Dict[int,int]: 
		"""
		pass

	@overload
	def ITurbinesResults(self, ids: List[int], timeStepIndex: int) -> Dict[int,int]:
		"""Method Description

		Args:
			ids(List[int]): ids
			timeStepIndex(int): timeStepIndex

		Returns:
			Dict[int,int]: 
		"""
		pass

	@overload
	def ITurbinesResults(self) -> Dict[int,int]:
		"""Method Description

		Returns:
			Dict[int,int]: 
		"""
		pass

	@overload
	def ITurbinesResults(self, timeStepIndex: int) -> Dict[int,int]:
		"""Method Description

		Args:
			timeStepIndex(int): timeStepIndex

		Returns:
			Dict[int,int]: 
		"""
		pass

	@overload
	def ITurbinesResults(self, ids: List[int], timeStepIndex: int) -> Dict[int,int]:
		"""Method Description

		Args:
			ids(List[int]): ids
			timeStepIndex(int): timeStepIndex

		Returns:
			Dict[int,int]: 
		"""
		pass

	@overload
	def ITurbinesResults(self) -> Dict[int,int]:
		"""Method Description

		Returns:
			Dict[int,int]: 
		"""
		pass

	@overload
	def ITurbinesResults(self, timeStepIndex: int) -> Dict[int,int]:
		"""Method Description

		Args:
			timeStepIndex(int): timeStepIndex

		Returns:
			Dict[int,int]: 
		"""
		pass

	@overload
	def ITurbinesResults(self, ids: List[int], timeStepIndex: int) -> Dict[int,int]:
		"""Method Description

		Args:
			ids(List[int]): ids
			timeStepIndex(int): timeStepIndex

		Returns:
			Dict[int,int]: 
		"""
		pass

	@overload
	def ITurbinesResults(self) -> Dict[int,int]:
		"""Method Description

		Returns:
			Dict[int,int]: 
		"""
		pass

	@overload
	def ITurbinesResults(self, timeStepIndex: int) -> Dict[int,int]:
		"""Method Description

		Args:
			timeStepIndex(int): timeStepIndex

		Returns:
			Dict[int,int]: 
		"""
		pass

	@overload
	def ITurbinesResults(self, ids: List[int], timeStepIndex: int) -> Dict[int,int]:
		"""Method Description

		Args:
			ids(List[int]): ids
			timeStepIndex(int): timeStepIndex

		Returns:
			Dict[int,int]: 
		"""
		pass

	@overload
	def ITurbinesResults(self) -> Dict[int,int]:
		"""Method Description

		Returns:
			Dict[int,int]: 
		"""
		pass

	@overload
	def ITurbinesResults(self, timeStepIndex: int) -> Dict[int,int]:
		"""Method Description

		Args:
			timeStepIndex(int): timeStepIndex

		Returns:
			Dict[int,int]: 
		"""
		pass

	@overload
	def ITurbinesResults(self, ids: List[int], timeStepIndex: int) -> Dict[int,int]:
		"""Method Description

		Args:
			ids(List[int]): ids
			timeStepIndex(int): timeStepIndex

		Returns:
			Dict[int,int]: 
		"""
		pass

	def MaximumTransientSpeeds(self) -> Dict[int,int]:
		"""Method Description

		Returns:
			Dict[int,int]: 
		"""
		pass

	def MinimumTransientSpeeds(self) -> Dict[int,int]:
		"""Method Description

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
		"""
		Returns:
			IUnit: No Description
		"""
		pass

	@property
	def DiameterUnit(self) -> IUnit:
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
	def InertiaUnit(self) -> IUnit:
		"""
		Returns:
			IUnit: No Description
		"""
		pass

	@property
	def RotationUnit(self) -> IUnit:
		"""
		Returns:
			IUnit: No Description
		"""
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

	@property
	def HeadlossUnit(self) -> IUnit:
		"""
		Returns:
			IUnit: No Description
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
		"""Method Description

		Returns:
			Dict[int,int]: 
		"""
		pass

	@overload
	def IBasePumpsResults(self, timeStepIndex: int) -> Dict[int,int]:
		"""Method Description

		Args:
			timeStepIndex(int): timeStepIndex

		Returns:
			Dict[int,int]: 
		"""
		pass

	@overload
	def IBasePumpsResults(self, ids: List[int], timeStepIndex: int) -> Dict[int,int]:
		"""Method Description

		Args:
			ids(List[int]): ids
			timeStepIndex(int): timeStepIndex

		Returns:
			Dict[int,int]: 
		"""
		pass

	@overload
	def IBasePumpsResults(self) -> Dict[int,int]:
		"""Method Description

		Returns:
			Dict[int,int]: 
		"""
		pass

	@overload
	def IBasePumpsResults(self, timeStepIndex: int) -> Dict[int,int]:
		"""Method Description

		Args:
			timeStepIndex(int): timeStepIndex

		Returns:
			Dict[int,int]: 
		"""
		pass

	@overload
	def IBasePumpsResults(self, ids: List[int], timeStepIndex: int) -> Dict[int,int]:
		"""Method Description

		Args:
			ids(List[int]): ids
			timeStepIndex(int): timeStepIndex

		Returns:
			Dict[int,int]: 
		"""
		pass

	@overload
	def IBasePumpsResults(self) -> Dict[int,int]:
		"""Method Description

		Returns:
			Dict[int,int]: 
		"""
		pass

	@overload
	def IBasePumpsResults(self, timeStepIndex: int) -> Dict[int,int]:
		"""Method Description

		Args:
			timeStepIndex(int): timeStepIndex

		Returns:
			Dict[int,int]: 
		"""
		pass

	@overload
	def IBasePumpsResults(self, ids: List[int], timeStepIndex: int) -> Dict[int,int]:
		"""Method Description

		Args:
			ids(List[int]): ids
			timeStepIndex(int): timeStepIndex

		Returns:
			Dict[int,int]: 
		"""
		pass

	@overload
	def IBasePumpsResults(self) -> Dict[int,int]:
		"""Method Description

		Returns:
			Dict[int,int]: 
		"""
		pass

	@overload
	def IBasePumpsResults(self, timeStepIndex: int) -> Dict[int,int]:
		"""Method Description

		Args:
			timeStepIndex(int): timeStepIndex

		Returns:
			Dict[int,int]: 
		"""
		pass

	@overload
	def IBasePumpsResults(self, ids: List[int], timeStepIndex: int) -> Dict[int,int]:
		"""Method Description

		Args:
			ids(List[int]): ids
			timeStepIndex(int): timeStepIndex

		Returns:
			Dict[int,int]: 
		"""
		pass

	@overload
	def IBasePumpsResults(self) -> Dict[int,int]:
		"""Method Description

		Returns:
			Dict[int,int]: 
		"""
		pass

	@overload
	def IBasePumpsResults(self, timeStepIndex: int) -> Dict[int,int]:
		"""Method Description

		Args:
			timeStepIndex(int): timeStepIndex

		Returns:
			Dict[int,int]: 
		"""
		pass

	@overload
	def IBasePumpsResults(self, ids: List[int], timeStepIndex: int) -> Dict[int,int]:
		"""Method Description

		Args:
			ids(List[int]): ids
			timeStepIndex(int): timeStepIndex

		Returns:
			Dict[int,int]: 
		"""
		pass

	@overload
	def IBasePumpsResults(self) -> Dict[int,int]:
		"""Method Description

		Returns:
			Dict[int,int]: 
		"""
		pass

	@overload
	def IBasePumpsResults(self, timeStepIndex: int) -> Dict[int,int]:
		"""Method Description

		Args:
			timeStepIndex(int): timeStepIndex

		Returns:
			Dict[int,int]: 
		"""
		pass

	@overload
	def IBasePumpsResults(self, ids: List[int], timeStepIndex: int) -> Dict[int,int]:
		"""Method Description

		Args:
			ids(List[int]): ids
			timeStepIndex(int): timeStepIndex

		Returns:
			Dict[int,int]: 
		"""
		pass

	@overload
	def IBasePumpsResults(self) -> Dict[int,int]:
		"""Method Description

		Returns:
			Dict[int,int]: 
		"""
		pass

	@overload
	def IBasePumpsResults(self, timeStepIndex: int) -> Dict[int,int]:
		"""Method Description

		Args:
			timeStepIndex(int): timeStepIndex

		Returns:
			Dict[int,int]: 
		"""
		pass

	@overload
	def IBasePumpsResults(self, ids: List[int], timeStepIndex: int) -> Dict[int,int]:
		"""Method Description

		Args:
			ids(List[int]): ids
			timeStepIndex(int): timeStepIndex

		Returns:
			Dict[int,int]: 
		"""
		pass

	@overload
	def IBasePumpsResults(self) -> Dict[int,int]:
		"""Method Description

		Returns:
			Dict[int,int]: 
		"""
		pass

	@overload
	def IBasePumpsResults(self, timeStepIndex: int) -> Dict[int,int]:
		"""Method Description

		Args:
			timeStepIndex(int): timeStepIndex

		Returns:
			Dict[int,int]: 
		"""
		pass

	@overload
	def IBasePumpsResults(self, ids: List[int], timeStepIndex: int) -> Dict[int,int]:
		"""Method Description

		Args:
			ids(List[int]): ids
			timeStepIndex(int): timeStepIndex

		Returns:
			Dict[int,int]: 
		"""
		pass

	@overload
	def IBasePumpsResults(self) -> Dict[int,int]:
		"""Method Description

		Returns:
			Dict[int,int]: 
		"""
		pass

	@overload
	def IBasePumpsResults(self, timeStepIndex: int) -> Dict[int,int]:
		"""Method Description

		Args:
			timeStepIndex(int): timeStepIndex

		Returns:
			Dict[int,int]: 
		"""
		pass

	@overload
	def IBasePumpsResults(self, ids: List[int], timeStepIndex: int) -> Dict[int,int]:
		"""Method Description

		Args:
			ids(List[int]): ids
			timeStepIndex(int): timeStepIndex

		Returns:
			Dict[int,int]: 
		"""
		pass

	@overload
	def IBasePumpsResults(self) -> Dict[int,int]:
		"""Method Description

		Returns:
			Dict[int,int]: 
		"""
		pass

	@overload
	def IBasePumpsResults(self, timeStepIndex: int) -> Dict[int,int]:
		"""Method Description

		Args:
			timeStepIndex(int): timeStepIndex

		Returns:
			Dict[int,int]: 
		"""
		pass

	@overload
	def IBasePumpsResults(self, ids: List[int], timeStepIndex: int) -> Dict[int,int]:
		"""Method Description

		Args:
			ids(List[int]): ids
			timeStepIndex(int): timeStepIndex

		Returns:
			Dict[int,int]: 
		"""
		pass

	@overload
	def IBasePumpsResults(self) -> Dict[int,int]:
		"""Method Description

		Returns:
			Dict[int,int]: 
		"""
		pass

	@overload
	def IBasePumpsResults(self, timeStepIndex: int) -> Dict[int,int]:
		"""Method Description

		Args:
			timeStepIndex(int): timeStepIndex

		Returns:
			Dict[int,int]: 
		"""
		pass

	@overload
	def IBasePumpsResults(self, ids: List[int], timeStepIndex: int) -> Dict[int,int]:
		"""Method Description

		Args:
			ids(List[int]): ids
			timeStepIndex(int): timeStepIndex

		Returns:
			Dict[int,int]: 
		"""
		pass

	@overload
	def IBasePumpsResults(self) -> Dict[int,int]:
		"""Method Description

		Returns:
			Dict[int,int]: 
		"""
		pass

	@overload
	def IBasePumpsResults(self, timeStepIndex: int) -> Dict[int,int]:
		"""Method Description

		Args:
			timeStepIndex(int): timeStepIndex

		Returns:
			Dict[int,int]: 
		"""
		pass

	@overload
	def IBasePumpsResults(self, ids: List[int], timeStepIndex: int) -> Dict[int,int]:
		"""Method Description

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
		"""Method Description

		Returns:
			Nullable: 
		"""
		pass

	@overload
	def IBasePumpResults(self, timeStepIndex: int) -> Union[float, None]:
		"""Method Description

		Args:
			timeStepIndex(int): timeStepIndex

		Returns:
			Nullable: 
		"""
		pass

	@overload
	def IBasePumpResults(self) -> Union[float, None]:
		"""Method Description

		Returns:
			Nullable: 
		"""
		pass

	@overload
	def IBasePumpResults(self, timeStepIndex: int) -> Union[float, None]:
		"""Method Description

		Args:
			timeStepIndex(int): timeStepIndex

		Returns:
			Nullable: 
		"""
		pass

	@overload
	def IBasePumpResults(self) -> Union[float, None]:
		"""Method Description

		Returns:
			Nullable: 
		"""
		pass

	@overload
	def IBasePumpResults(self, timeStepIndex: int) -> Union[float, None]:
		"""Method Description

		Args:
			timeStepIndex(int): timeStepIndex

		Returns:
			Nullable: 
		"""
		pass

	@overload
	def IBasePumpResults(self) -> Union[float, None]:
		"""Method Description

		Returns:
			Nullable: 
		"""
		pass

	@overload
	def IBasePumpResults(self, timeStepIndex: int) -> Union[float, None]:
		"""Method Description

		Args:
			timeStepIndex(int): timeStepIndex

		Returns:
			Nullable: 
		"""
		pass

	@overload
	def IBasePumpResults(self) -> Union[float, None]:
		"""Method Description

		Returns:
			Nullable: 
		"""
		pass

	@overload
	def IBasePumpResults(self, timeStepIndex: int) -> Union[float, None]:
		"""Method Description

		Args:
			timeStepIndex(int): timeStepIndex

		Returns:
			Nullable: 
		"""
		pass

	@overload
	def IBasePumpResults(self) -> Union[float, None]:
		"""Method Description

		Returns:
			Nullable: 
		"""
		pass

	@overload
	def IBasePumpResults(self, timeStepIndex: int) -> Union[float, None]:
		"""Method Description

		Args:
			timeStepIndex(int): timeStepIndex

		Returns:
			Nullable: 
		"""
		pass

	@overload
	def IBasePumpResults(self) -> Union[float, None]:
		"""Method Description

		Returns:
			Nullable: 
		"""
		pass

	@overload
	def IBasePumpResults(self, timeStepIndex: int) -> Union[float, None]:
		"""Method Description

		Args:
			timeStepIndex(int): timeStepIndex

		Returns:
			Nullable: 
		"""
		pass

	@overload
	def IBasePumpResults(self) -> Union[float, None]:
		"""Method Description

		Returns:
			Nullable: 
		"""
		pass

	@overload
	def IBasePumpResults(self, timeStepIndex: int) -> Union[float, None]:
		"""Method Description

		Args:
			timeStepIndex(int): timeStepIndex

		Returns:
			Nullable: 
		"""
		pass

	@overload
	def IBasePumpResults(self) -> Union[float, None]:
		"""Method Description

		Returns:
			Nullable: 
		"""
		pass

	@overload
	def IBasePumpResults(self, timeStepIndex: int) -> Union[float, None]:
		"""Method Description

		Args:
			timeStepIndex(int): timeStepIndex

		Returns:
			Nullable: 
		"""
		pass

	@overload
	def IBasePumpResults(self) -> Union[bool, None]:
		"""Method Description

		Returns:
			Nullable: 
		"""
		pass

	@overload
	def IBasePumpResults(self, timeStepIndex: int) -> Union[bool, None]:
		"""Method Description

		Args:
			timeStepIndex(int): timeStepIndex

		Returns:
			Nullable: 
		"""
		pass

	@overload
	def IBasePumpResults(self) -> Union[PumpStatusEnum, None]:
		"""Method Description

		Returns:
			Nullable: 
		"""
		pass

	@overload
	def IBasePumpResults(self, timeStepIndex: int) -> Union[PumpStatusEnum, None]:
		"""Method Description

		Args:
			timeStepIndex(int): timeStepIndex

		Returns:
			Nullable: 
		"""
		pass

	@overload
	def IBasePumpResults(self) -> Union[float, None]:
		"""Method Description

		Returns:
			Nullable: 
		"""
		pass

	@overload
	def IBasePumpResults(self, timeStepIndex: int) -> Union[float, None]:
		"""Method Description

		Args:
			timeStepIndex(int): timeStepIndex

		Returns:
			Nullable: 
		"""
		pass

	def CalculatedRelativeSpeedFactors(self) -> array(Union[float, None]):
		"""Method Description

		Returns:
			Nullable[]: 
		"""
		pass

	def SuctionHyraulicGrades(self) -> array(Union[float, None]):
		"""Method Description

		Returns:
			Nullable[]: 
		"""
		pass

	def DischargeHydraulicGrades(self) -> array(Union[float, None]):
		"""Method Description

		Returns:
			Nullable[]: 
		"""
		pass

	def SuctionPressures(self) -> array(Union[float, None]):
		"""Method Description

		Returns:
			Nullable[]: 
		"""
		pass

	def DischargePressures(self) -> array(Union[float, None]):
		"""Method Description

		Returns:
			Nullable[]: 
		"""
		pass

	def Flows(self) -> array(Union[float, None]):
		"""Method Description

		Returns:
			Nullable[]: 
		"""
		pass

	def PumpHeads(self) -> array(Union[float, None]):
		"""Method Description

		Returns:
			Nullable[]: 
		"""
		pass

	def AvailableNPSHs(self) -> array(Union[float, None]):
		"""Method Description

		Returns:
			Nullable[]: 
		"""
		pass

	def RequiredNPSHs(self) -> array(Union[float, None]):
		"""Method Description

		Returns:
			Nullable[]: 
		"""
		pass

	def PumpExceedsOperatingRanges(self) -> array(Union[bool, None]):
		"""Method Description

		Returns:
			Nullable[]: 
		"""
		pass

	def CalculatedPumpStatuses(self) -> array(Union[PumpStatusEnum, None]):
		"""Method Description

		Returns:
			Nullable[]: 
		"""
		pass

	def WirePowers(self) -> array(Union[float, None]):
		"""Method Description

		Returns:
			Nullable[]: 
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
		"""
		Returns:
			float: No Description
		"""
		pass

	@property
	def InitialStatus(self) -> int:
		"""
		Returns:
			int: No Description
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
		"""Method Description

		Returns:
			Dict[int,int]: 
		"""
		pass

	@overload
	def IBasePumpsInput(self, ids: List[int]) -> Dict[int,int]:
		"""Method Description

		Args:
			ids(List[int]): ids

		Returns:
			Dict[int,int]: 
		"""
		pass

	@overload
	def IBasePumpsInput(self) -> Dict[int,int]:
		"""Method Description

		Returns:
			Dict[int,int]: 
		"""
		pass

	@overload
	def IBasePumpsInput(self, ids: List[int]) -> Dict[int,int]:
		"""Method Description

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
	def NPSHUnit(self) -> IUnit:
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
		"""
		Returns:
			IPumpDefinition: No Description
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
		"""Method Description

		Returns:
			Dict[int,int]: 
		"""
		pass

	def ControlNodes(self) -> Dict[int,int]:
		"""Method Description

		Returns:
			Dict[int,int]: 
		"""
		pass

	def TargetHydraulicGrades(self) -> Dict[int,int]:
		"""Method Description

		Returns:
			Dict[int,int]: 
		"""
		pass

	def MaximumRelativeSpeedFactors(self) -> Dict[int,int]:
		"""Method Description

		Returns:
			Dict[int,int]: 
		"""
		pass

	def NumberOfLagPumps(self) -> Dict[int,int]:
		"""Method Description

		Returns:
			Dict[int,int]: 
		"""
		pass

	def ControlNodeOnSuctionSide(self) -> Dict[int,int]:
		"""Method Description

		Returns:
			Dict[int,int]: 
		"""
		pass

	def TargetFlows(self) -> Dict[int,int]:
		"""Method Description

		Returns:
			Dict[int,int]: 
		"""
		pass

	def TargetPressures(self) -> Dict[int,int]:
		"""Method Description

		Returns:
			Dict[int,int]: 
		"""
		pass

	def VSPBTypes(self) -> Dict[int,int]:
		"""Method Description

		Returns:
			Dict[int,int]: 
		"""
		pass

	def VSPBFixedHeadTypes(self) -> Dict[int,int]:
		"""Method Description

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
		"""
		Returns:
			IPumpDefinition: No Description
		"""
		pass

	@property
	def ControlNode(self) -> IWaterNetworkElement:
		"""
		Returns:
			IWaterNetworkElement: No Description
		"""
		pass

	@property
	def TargetHydraulicGrade(self) -> float:
		"""
		Returns:
			float: No Description
		"""
		pass

	@property
	def MaximumRelativeSpeedFactor(self) -> float:
		"""
		Returns:
			float: No Description
		"""
		pass

	@property
	def NumberOfLagPumps(self) -> int:
		"""
		Returns:
			int: No Description
		"""
		pass

	@property
	def ControlNodeOnSuctionSide(self) -> bool:
		"""
		Returns:
			bool: No Description
		"""
		pass

	@property
	def TargetFlow(self) -> float:
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
	def VSPBType(self) -> VSPBType:
		"""
		Returns:
			VSPBType: No Description
		"""
		pass

	@property
	def VSPBFixedHeadType(self) -> VSPBFixedHeadType:
		"""
		Returns:
			VSPBFixedHeadType: No Description
		"""
		pass

	@PumpDefinition.setter
	def PumpDefinition(self, pumpdefinition: IPumpDefinition) -> None:
		pass

	@ControlNode.setter
	def ControlNode(self, controlnode: IWaterNetworkElement) -> None:
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
		"""Method Description

		Returns:
			Dict[int,int]: 
		"""
		pass

	@overload
	def IVSPBsResults(self, timeStepIndex: int) -> Dict[int,int]:
		"""Method Description

		Args:
			timeStepIndex(int): timeStepIndex

		Returns:
			Dict[int,int]: 
		"""
		pass

	@overload
	def IVSPBsResults(self, ids: List[int], timeStepIndex: int) -> Dict[int,int]:
		"""Method Description

		Args:
			ids(List[int]): ids
			timeStepIndex(int): timeStepIndex

		Returns:
			Dict[int,int]: 
		"""
		pass

	@overload
	def IVSPBsResults(self) -> Dict[int,int]:
		"""Method Description

		Returns:
			Dict[int,int]: 
		"""
		pass

	@overload
	def IVSPBsResults(self, timeStepIndex: int) -> Dict[int,int]:
		"""Method Description

		Args:
			timeStepIndex(int): timeStepIndex

		Returns:
			Dict[int,int]: 
		"""
		pass

	@overload
	def IVSPBsResults(self, ids: List[int], timeStepIndex: int) -> Dict[int,int]:
		"""Method Description

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
		"""Method Description

		Returns:
			Nullable: 
		"""
		pass

	@overload
	def IVSPBResults(self, timeStepIndex: int) -> Union[float, None]:
		"""Method Description

		Args:
			timeStepIndex(int): timeStepIndex

		Returns:
			Nullable: 
		"""
		pass

	@overload
	def IVSPBResults(self) -> Union[float, None]:
		"""Method Description

		Returns:
			Nullable: 
		"""
		pass

	@overload
	def IVSPBResults(self, timeStepIndex: int) -> Union[float, None]:
		"""Method Description

		Args:
			timeStepIndex(int): timeStepIndex

		Returns:
			Nullable: 
		"""
		pass

	def LoadPumpFlows(self) -> array(Union[float, None]):
		"""Method Description

		Returns:
			Nullable[]: 
		"""
		pass

	def NumberRunningLagPumps(self) -> array(Union[float, None]):
		"""Method Description

		Returns:
			Nullable[]: 
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
		"""Method Description

		Returns:
			Dict[int,int]: 
		"""
		pass

	@overload
	def IBaseValvesResults(self, timeStepIndex: int) -> Dict[int,int]:
		"""Method Description

		Args:
			timeStepIndex(int): timeStepIndex

		Returns:
			Dict[int,int]: 
		"""
		pass

	@overload
	def IBaseValvesResults(self, ids: List[int], timeStepIndex: int) -> Dict[int,int]:
		"""Method Description

		Args:
			ids(List[int]): ids
			timeStepIndex(int): timeStepIndex

		Returns:
			Dict[int,int]: 
		"""
		pass

	@overload
	def IBaseValvesResults(self) -> Dict[int,int]:
		"""Method Description

		Returns:
			Dict[int,int]: 
		"""
		pass

	@overload
	def IBaseValvesResults(self, timeStepIndex: int) -> Dict[int,int]:
		"""Method Description

		Args:
			timeStepIndex(int): timeStepIndex

		Returns:
			Dict[int,int]: 
		"""
		pass

	@overload
	def IBaseValvesResults(self, ids: List[int], timeStepIndex: int) -> Dict[int,int]:
		"""Method Description

		Args:
			ids(List[int]): ids
			timeStepIndex(int): timeStepIndex

		Returns:
			Dict[int,int]: 
		"""
		pass

	@overload
	def IBaseValvesResults(self) -> Dict[int,int]:
		"""Method Description

		Returns:
			Dict[int,int]: 
		"""
		pass

	@overload
	def IBaseValvesResults(self, timeStepIndex: int) -> Dict[int,int]:
		"""Method Description

		Args:
			timeStepIndex(int): timeStepIndex

		Returns:
			Dict[int,int]: 
		"""
		pass

	@overload
	def IBaseValvesResults(self, ids: List[int], timeStepIndex: int) -> Dict[int,int]:
		"""Method Description

		Args:
			ids(List[int]): ids
			timeStepIndex(int): timeStepIndex

		Returns:
			Dict[int,int]: 
		"""
		pass

	@overload
	def IBaseValvesResults(self) -> Dict[int,int]:
		"""Method Description

		Returns:
			Dict[int,int]: 
		"""
		pass

	@overload
	def IBaseValvesResults(self, timeStepIndex: int) -> Dict[int,int]:
		"""Method Description

		Args:
			timeStepIndex(int): timeStepIndex

		Returns:
			Dict[int,int]: 
		"""
		pass

	@overload
	def IBaseValvesResults(self, ids: List[int], timeStepIndex: int) -> Dict[int,int]:
		"""Method Description

		Args:
			ids(List[int]): ids
			timeStepIndex(int): timeStepIndex

		Returns:
			Dict[int,int]: 
		"""
		pass

	@overload
	def IBaseValvesResults(self) -> Dict[int,int]:
		"""Method Description

		Returns:
			Dict[int,int]: 
		"""
		pass

	@overload
	def IBaseValvesResults(self, timeStepIndex: int) -> Dict[int,int]:
		"""Method Description

		Args:
			timeStepIndex(int): timeStepIndex

		Returns:
			Dict[int,int]: 
		"""
		pass

	@overload
	def IBaseValvesResults(self, ids: List[int], timeStepIndex: int) -> Dict[int,int]:
		"""Method Description

		Args:
			ids(List[int]): ids
			timeStepIndex(int): timeStepIndex

		Returns:
			Dict[int,int]: 
		"""
		pass

	@overload
	def IBaseValvesResults(self) -> Dict[int,int]:
		"""Method Description

		Returns:
			Dict[int,int]: 
		"""
		pass

	@overload
	def IBaseValvesResults(self, timeStepIndex: int) -> Dict[int,int]:
		"""Method Description

		Args:
			timeStepIndex(int): timeStepIndex

		Returns:
			Dict[int,int]: 
		"""
		pass

	@overload
	def IBaseValvesResults(self, ids: List[int], timeStepIndex: int) -> Dict[int,int]:
		"""Method Description

		Args:
			ids(List[int]): ids
			timeStepIndex(int): timeStepIndex

		Returns:
			Dict[int,int]: 
		"""
		pass

	@overload
	def IBaseValvesResults(self) -> Dict[int,int]:
		"""Method Description

		Returns:
			Dict[int,int]: 
		"""
		pass

	@overload
	def IBaseValvesResults(self, timeStepIndex: int) -> Dict[int,int]:
		"""Method Description

		Args:
			timeStepIndex(int): timeStepIndex

		Returns:
			Dict[int,int]: 
		"""
		pass

	@overload
	def IBaseValvesResults(self, ids: List[int], timeStepIndex: int) -> Dict[int,int]:
		"""Method Description

		Args:
			ids(List[int]): ids
			timeStepIndex(int): timeStepIndex

		Returns:
			Dict[int,int]: 
		"""
		pass

	@overload
	def IBaseValvesResults(self) -> Dict[int,int]:
		"""Method Description

		Returns:
			Dict[int,int]: 
		"""
		pass

	@overload
	def IBaseValvesResults(self, timeStepIndex: int) -> Dict[int,int]:
		"""Method Description

		Args:
			timeStepIndex(int): timeStepIndex

		Returns:
			Dict[int,int]: 
		"""
		pass

	@overload
	def IBaseValvesResults(self, ids: List[int], timeStepIndex: int) -> Dict[int,int]:
		"""Method Description

		Args:
			ids(List[int]): ids
			timeStepIndex(int): timeStepIndex

		Returns:
			Dict[int,int]: 
		"""
		pass

	@overload
	def IBaseValvesResults(self) -> Dict[int,int]:
		"""Method Description

		Returns:
			Dict[int,int]: 
		"""
		pass

	@overload
	def IBaseValvesResults(self, timeStepIndex: int) -> Dict[int,int]:
		"""Method Description

		Args:
			timeStepIndex(int): timeStepIndex

		Returns:
			Dict[int,int]: 
		"""
		pass

	@overload
	def IBaseValvesResults(self, ids: List[int], timeStepIndex: int) -> Dict[int,int]:
		"""Method Description

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
		"""Method Description

		Returns:
			Nullable: 
		"""
		pass

	@overload
	def IBaseValveResults(self, timeStepIndex: int) -> Union[float, None]:
		"""Method Description

		Args:
			timeStepIndex(int): timeStepIndex

		Returns:
			Nullable: 
		"""
		pass

	@overload
	def IBaseValveResults(self) -> Union[float, None]:
		"""Method Description

		Returns:
			Nullable: 
		"""
		pass

	@overload
	def IBaseValveResults(self, timeStepIndex: int) -> Union[float, None]:
		"""Method Description

		Args:
			timeStepIndex(int): timeStepIndex

		Returns:
			Nullable: 
		"""
		pass

	@overload
	def IBaseValveResults(self) -> Union[float, None]:
		"""Method Description

		Returns:
			Nullable: 
		"""
		pass

	@overload
	def IBaseValveResults(self, timeStepIndex: int) -> Union[float, None]:
		"""Method Description

		Args:
			timeStepIndex(int): timeStepIndex

		Returns:
			Nullable: 
		"""
		pass

	@overload
	def IBaseValveResults(self) -> Union[float, None]:
		"""Method Description

		Returns:
			Nullable: 
		"""
		pass

	@overload
	def IBaseValveResults(self, timeStepIndex: int) -> Union[float, None]:
		"""Method Description

		Args:
			timeStepIndex(int): timeStepIndex

		Returns:
			Nullable: 
		"""
		pass

	@overload
	def IBaseValveResults(self) -> Union[float, None]:
		"""Method Description

		Returns:
			Nullable: 
		"""
		pass

	@overload
	def IBaseValveResults(self, timeStepIndex: int) -> Union[float, None]:
		"""Method Description

		Args:
			timeStepIndex(int): timeStepIndex

		Returns:
			Nullable: 
		"""
		pass

	@overload
	def IBaseValveResults(self) -> Union[float, None]:
		"""Method Description

		Returns:
			Nullable: 
		"""
		pass

	@overload
	def IBaseValveResults(self, timeStepIndex: int) -> Union[float, None]:
		"""Method Description

		Args:
			timeStepIndex(int): timeStepIndex

		Returns:
			Nullable: 
		"""
		pass

	@overload
	def IBaseValveResults(self) -> Union[float, None]:
		"""Method Description

		Returns:
			Nullable: 
		"""
		pass

	@overload
	def IBaseValveResults(self, timeStepIndex: int) -> Union[float, None]:
		"""Method Description

		Args:
			timeStepIndex(int): timeStepIndex

		Returns:
			Nullable: 
		"""
		pass

	@overload
	def IBaseValveResults(self) -> Union[float, None]:
		"""Method Description

		Returns:
			Nullable: 
		"""
		pass

	@overload
	def IBaseValveResults(self, timeStepIndex: int) -> Union[float, None]:
		"""Method Description

		Args:
			timeStepIndex(int): timeStepIndex

		Returns:
			Nullable: 
		"""
		pass

	@overload
	def IBaseValveResults(self) -> Union[int, None]:
		"""Method Description

		Returns:
			Nullable: 
		"""
		pass

	@overload
	def IBaseValveResults(self, timeStepIndex: int) -> Union[int, None]:
		"""Method Description

		Args:
			timeStepIndex(int): timeStepIndex

		Returns:
			Nullable: 
		"""
		pass

	def Flows(self) -> array(Union[float, None]):
		"""Method Description

		Returns:
			Nullable[]: 
		"""
		pass

	def Velocities(self) -> array(Union[float, None]):
		"""Method Description

		Returns:
			Nullable[]: 
		"""
		pass

	def Headlosses(self) -> array(Union[float, None]):
		"""Method Description

		Returns:
			Nullable[]: 
		"""
		pass

	def PressureLosses(self) -> array(Union[float, None]):
		"""Method Description

		Returns:
			Nullable[]: 
		"""
		pass

	def FromHydraulicGrades(self) -> array(Union[float, None]):
		"""Method Description

		Returns:
			Nullable[]: 
		"""
		pass

	def ToHydraulicGrades(self) -> array(Union[float, None]):
		"""Method Description

		Returns:
			Nullable[]: 
		"""
		pass

	def FromPressures(self) -> array(Union[float, None]):
		"""Method Description

		Returns:
			Nullable[]: 
		"""
		pass

	def ToPressures(self) -> array(Union[float, None]):
		"""Method Description

		Returns:
			Nullable[]: 
		"""
		pass

	def CalculatedStatuses(self) -> array(Union[int, None]):
		"""Method Description

		Returns:
			Nullable[]: 
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
		"""
		Returns:
			ValveSettingType: No Description
		"""
		pass

	@property
	def ValveDiameter(self) -> float:
		"""
		Returns:
			float: No Description
		"""
		pass

	@property
	def MinorLossCoefficientCollection(self) -> IMinorLossCoefficientCollection:
		"""
		Returns:
			IMinorLossCoefficientCollection: No Description
		"""
		pass

	@property
	def LocalMinorLossCoefficient(self) -> float:
		"""
		Returns:
			float: No Description
		"""
		pass

	@property
	def SpecifyLocalMinorLoss(self) -> bool:
		"""
		Returns:
			bool: No Description
		"""
		pass

	@property
	def DerivedMinorLossCoefficient(self) -> float:
		"""
		Returns:
			float: No Description
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
		"""Method Description

		Returns:
			Dict[int,int]: 
		"""
		pass

	@overload
	def IBaseValvesInput(self, ids: List[int]) -> Dict[int,int]:
		"""Method Description

		Args:
			ids(List[int]): ids

		Returns:
			Dict[int,int]: 
		"""
		pass

	@overload
	def IBaseValvesInput(self) -> Dict[int,int]:
		"""Method Description

		Returns:
			Dict[int,int]: 
		"""
		pass

	@overload
	def IBaseValvesInput(self, ids: List[int]) -> Dict[int,int]:
		"""Method Description

		Args:
			ids(List[int]): ids

		Returns:
			Dict[int,int]: 
		"""
		pass

	def LocalMinorLossCoefficient(self) -> Dict[int,int]:
		"""Method Description

		Returns:
			Dict[int,int]: 
		"""
		pass

	def SpecifyLocalMinorLoss(self) -> Dict[int,int]:
		"""Method Description

		Returns:
			Dict[int,int]: 
		"""
		pass

	def DerivedMinorLossCoefficient(self) -> Dict[int,int]:
		"""Method Description

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
		"""
		Returns:
			IUnit: No Description
		"""
		pass

	@property
	def FlowUnit(self) -> IUnit:
		"""
		Returns:
			IUnit: No Description
		"""
		pass

	@property
	def VelocityUnit(self) -> IUnit:
		"""
		Returns:
			IUnit: No Description
		"""
		pass

	@property
	def HeadlossUnit(self) -> IUnit:
		"""
		Returns:
			IUnit: No Description
		"""
		pass

	@property
	def PressureLossUnit(self) -> IUnit:
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
		"""Method Description

		Returns:
			Dict[int,int]: 
		"""
		pass

	@overload
	def IFlowControlValvesResults(self, timeStepIndex: int) -> Dict[int,int]:
		"""Method Description

		Args:
			timeStepIndex(int): timeStepIndex

		Returns:
			Dict[int,int]: 
		"""
		pass

	@overload
	def IFlowControlValvesResults(self, ids: List[int], timeStepInde: int) -> Dict[int,int]:
		"""Method Description

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
		"""Method Description

		Returns:
			Nullable: 
		"""
		pass

	@overload
	def IFlowControlValveResults(self, timeStepIndex: int) -> Union[float, None]:
		"""Method Description

		Args:
			timeStepIndex(int): timeStepIndex

		Returns:
			Nullable: 
		"""
		pass

	def CalculatedFlowSettings(self) -> array(Union[float, None]):
		"""Method Description

		Returns:
			Nullable[]: 
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
		"""Method Description

		Returns:
			Dict[int,int]: 
		"""
		pass

	@overload
	def IFlowControlValvesInput(self, ids: List[int]) -> Dict[int,int]:
		"""Method Description

		Args:
			ids(List[int]): ids

		Returns:
			Dict[int,int]: 
		"""
		pass

	def ValveCharacteristics(self) -> Dict[int,int]:
		"""Method Description

		Returns:
			Dict[int,int]: 
		"""
		pass

	def ValveTypes(self) -> Dict[int,int]:
		"""Method Description

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
		"""
		Returns:
			float: No Description
		"""
		pass

	@property
	def ValveCharacteristics(self) -> IValveCharacteristic:
		"""
		Returns:
			IValveCharacteristic: No Description
		"""
		pass

	@property
	def ValveType(self) -> HammerValveType:
		"""
		Returns:
			HammerValveType: No Description
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
		"""
		Returns:
			IUnit: No Description
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
		"""Method Description

		Returns:
			Dict[int,int]: 
		"""
		pass

	@overload
	def IThrottleControlValvesResults(self, timeStepIndex: int) -> Dict[int,int]:
		"""Method Description

		Args:
			timeStepIndex(int): timeStepIndex

		Returns:
			Dict[int,int]: 
		"""
		pass

	@overload
	def IThrottleControlValvesResults(self, ids: List[int], timeStepIndex: int) -> Dict[int,int]:
		"""Method Description

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
		"""Method Description

		Returns:
			Nullable: 
		"""
		pass

	@overload
	def IThrottleControlValveResults(self, timeStepIndex: int) -> Union[float, None]:
		"""Method Description

		Args:
			timeStepIndex(int): timeStepIndex

		Returns:
			Nullable: 
		"""
		pass

	def CalculatedSettings(self) -> array(Union[float, None]):
		"""Method Description

		Returns:
			Nullable[]: 
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
		"""
		Returns:
			TCVCoefficientType: No Description
		"""
		pass

	@property
	def InitialCoefficient(self) -> float:
		"""
		Returns:
			float: No Description
		"""
		pass

	@property
	def ValveCharacteristics(self) -> IValveCharacteristic:
		"""
		Returns:
			IValveCharacteristic: No Description
		"""
		pass

	@property
	def ValveType(self) -> HammerValveType:
		"""
		Returns:
			HammerValveType: No Description
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
		"""Method Description

		Returns:
			Dict[int,int]: 
		"""
		pass

	@overload
	def IThrottleControlValvesInput(self, ids: List[int]) -> Dict[int,int]:
		"""Method Description

		Args:
			ids(List[int]): ids

		Returns:
			Dict[int,int]: 
		"""
		pass

	@overload
	def IThrottleControlValvesInput(self) -> Dict[int,int]:
		"""Method Description

		Returns:
			Dict[int,int]: 
		"""
		pass

	@overload
	def IThrottleControlValvesInput(self, ids: List[int]) -> Dict[int,int]:
		"""Method Description

		Args:
			ids(List[int]): ids

		Returns:
			Dict[int,int]: 
		"""
		pass

	def ValveCharacteristics(self) -> Dict[int,int]:
		"""Method Description

		Returns:
			Dict[int,int]: 
		"""
		pass

	def ValveTypes(self) -> Dict[int,int]:
		"""Method Description

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
		"""
		Returns:
			IUnit: No Description
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
		"""Method Description

		Returns:
			Dict[int,int]: 
		"""
		pass

	def ValveCharacteristics(self) -> Dict[int,int]:
		"""Method Description

		Returns:
			Dict[int,int]: 
		"""
		pass

	def ValveTypes(self) -> Dict[int,int]:
		"""Method Description

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
		"""
		Returns:
			IGPVHeadlossCurve: No Description
		"""
		pass

	@property
	def ValveCharacteristics(self) -> IValveCharacteristic:
		"""
		Returns:
			IValveCharacteristic: No Description
		"""
		pass

	@property
	def ValveType(self) -> HammerValveType:
		"""
		Returns:
			HammerValveType: No Description
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
		"""Method Description

		Returns:
			Dict[int,int]: 
		"""
		pass

	@overload
	def IPressureValvesResults(self, timeStepIndex: int) -> Dict[int,int]:
		"""Method Description

		Args:
			timeStepIndex(int): timeStepIndex

		Returns:
			Dict[int,int]: 
		"""
		pass

	@overload
	def IPressureValvesResults(self, ids: List[int], timeStepIndex: int) -> Dict[int,int]:
		"""Method Description

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
		"""Method Description

		Returns:
			Nullable: 
		"""
		pass

	@overload
	def IPressureValveResults(self, timeStepIndex: int) -> Union[float, None]:
		"""Method Description

		Args:
			timeStepIndex(int): timeStepIndex

		Returns:
			Nullable: 
		"""
		pass

	def CalculatedSettings(self) -> array(Union[float, None]):
		"""Method Description

		Returns:
			Nullable[]: 
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
		"""
		Returns:
			PressureValvesettingType: No Description
		"""
		pass

	@property
	def InitialSetting(self) -> float:
		"""
		Returns:
			float: No Description
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
		"""Method Description

		Returns:
			Dict[int,int]: 
		"""
		pass

	@overload
	def IPressureValvesInput(self, ids: List[int]) -> Dict[int,int]:
		"""Method Description

		Args:
			ids(List[int]): ids

		Returns:
			Dict[int,int]: 
		"""
		pass

	@overload
	def IPressureValvesInput(self) -> Dict[int,int]:
		"""Method Description

		Returns:
			Dict[int,int]: 
		"""
		pass

	@overload
	def IPressureValvesInput(self, ids: List[int]) -> Dict[int,int]:
		"""Method Description

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
		"""
		Returns:
			IUnit: No Description
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
		"""Method Description

		Returns:
			Dict[int,int]: 
		"""
		pass

	def ValveTypes(self) -> Dict[int,int]:
		"""Method Description

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
		"""
		Returns:
			IValveCharacteristic: No Description
		"""
		pass

	@property
	def ValveType(self) -> HammerValveType:
		"""
		Returns:
			HammerValveType: No Description
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
		"""Method Description

		Returns:
			Dict[int,int]: 
		"""
		pass

	def ValveTypes(self) -> Dict[int,int]:
		"""Method Description

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
		"""
		Returns:
			IValveCharacteristic: No Description
		"""
		pass

	@property
	def ValveType(self) -> HammerValveType:
		"""
		Returns:
			HammerValveType: No Description
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
		"""
		Returns:
			float: No Description
		"""
		pass

	@property
	def DischargeCoefficient(self) -> float:
		"""
		Returns:
			float: No Description
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
		"""Method Description

		Returns:
			Dict[int,int]: 
		"""
		pass

	@overload
	def IValvesLinearAreaChangeInput(self, ids: List[int]) -> Dict[int,int]:
		"""Method Description

		Args:
			ids(List[int]): ids

		Returns:
			Dict[int,int]: 
		"""
		pass

	@overload
	def IValvesLinearAreaChangeInput(self) -> Dict[int,int]:
		"""Method Description

		Returns:
			Dict[int,int]: 
		"""
		pass

	@overload
	def IValvesLinearAreaChangeInput(self, ids: List[int]) -> Dict[int,int]:
		"""Method Description

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
		"""
		Returns:
			IUnit: No Description
		"""
		pass

	@property
	def TimeToCloseUnit(self) -> IUnit:
		"""
		Returns:
			IUnit: No Description
		"""
		pass

class IWaterNetworkElement(IElement):

	def __init__(self) -> None:
		"""Creating a new Instance of this class is not allowed


		Raises:
			Exception: if this class is instanciated
		"""
		raise Exception("Creating a new Instance of this class is not allowed")
		pass

	@property
	def WaterElementType(self) -> WaterNetworkElementType:
		"""
		Returns:
			WaterNetworkElementType: No Description
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

class IWaterNetworkElement(Generic[TElementManagerType, TElementType, TUnitsType, TElementInputType, TElementResultsType, TElementsInputType, TElementsResultsType], INetworkElement[TElementManagerType, TElementType, TUnitsType, WaterNetworkElementType, TElementInputType, TElementResultsType, TElementsInputType, TElementsResultsType], IWaterNetworkElement):

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
		"""
		Returns:
			IZone: No Description
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
		"""Method Description

		Returns:
			Dict[int,int]: 
		"""
		pass

	@overload
	def IWaterZoneableNetworkElementsInput(self, ids: List[int]) -> Dict[int,int]:
		"""Method Description

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
		"""Method Description

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
		"""Method Description

		Returns:
			Nullable: 
		"""
		pass

	@overload
	def IWaterQualityResults(self, timeStepIndex: int) -> Union[float, None]:
		"""Method Description

		Args:
			timeStepIndex(int): timeStepIndex

		Returns:
			Nullable: 
		"""
		pass

	@overload
	def IWaterQualityResults(self) -> Union[float, None]:
		"""Method Description

		Returns:
			Nullable: 
		"""
		pass

	@overload
	def IWaterQualityResults(self, timeStepIndex: int) -> Union[float, None]:
		"""Method Description

		Args:
			timeStepIndex(int): timeStepIndex

		Returns:
			Nullable: 
		"""
		pass

	@overload
	def IWaterQualityResults(self) -> Union[float, None]:
		"""Method Description

		Returns:
			Nullable: 
		"""
		pass

	@overload
	def IWaterQualityResults(self, timeStepIndex: int) -> Union[float, None]:
		"""Method Description

		Args:
			timeStepIndex(int): timeStepIndex

		Returns:
			Nullable: 
		"""
		pass

	def Ages(self) -> array(Union[float, None]):
		"""Method Description

		Returns:
			Nullable[]: 
		"""
		pass

	def Traces(self) -> array(Union[float, None]):
		"""Method Description

		Returns:
			Nullable[]: 
		"""
		pass

	def Concentrations(self) -> array(Union[float, None]):
		"""Method Description

		Returns:
			Nullable[]: 
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
		"""Method Description

		Returns:
			Dict[int,int]: 
		"""
		pass

	@overload
	def IWaterQualityElementsInput(self, ids: List[int]) -> Dict[int,int]:
		"""Method Description

		Args:
			ids(List[int]): ids

		Returns:
			Dict[int,int]: 
		"""
		pass

	@overload
	def IWaterQualityElementsInput(self) -> Dict[int,int]:
		"""Method Description

		Returns:
			Dict[int,int]: 
		"""
		pass

	@overload
	def IWaterQualityElementsInput(self, ids: List[int]) -> Dict[int,int]:
		"""Method Description

		Args:
			ids(List[int]): ids

		Returns:
			Dict[int,int]: 
		"""
		pass

	@overload
	def IWaterQualityElementsInput(self) -> Dict[int,int]:
		"""Method Description

		Returns:
			Dict[int,int]: 
		"""
		pass

	@overload
	def IWaterQualityElementsInput(self, ids: List[int]) -> Dict[int,int]:
		"""Method Description

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
		"""
		Returns:
			float: No Description
		"""
		pass

	@property
	def InitialConcentration(self) -> float:
		"""
		Returns:
			float: No Description
		"""
		pass

	@property
	def InitialTrace(self) -> float:
		"""
		Returns:
			float: No Description
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
		"""
		Returns:
			bool: No Description
		"""
		pass

	@property
	def ConstituentSourceType(self) -> ConstituentSourceType:
		"""
		Returns:
			ConstituentSourceType: No Description
		"""
		pass

	@property
	def BaseConstituent(self) -> float:
		"""
		Returns:
			float: No Description
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
		"""Method Description

		Returns:
			Dict[int,int]: 
		"""
		pass

	@overload
	def IWaterQualityElementsResults(self, timeStepIndex: int) -> Dict[int,int]:
		"""Method Description

		Args:
			timeStepIndex(int): timeStepIndex

		Returns:
			Dict[int,int]: 
		"""
		pass

	@overload
	def IWaterQualityElementsResults(self, ids: List[int], timeStepIndex: int) -> Dict[int,int]:
		"""Method Description

		Args:
			ids(List[int]): ids
			timeStepIndex(int): timeStepIndex

		Returns:
			Dict[int,int]: 
		"""
		pass

	@overload
	def IWaterQualityElementsResults(self) -> Dict[int,int]:
		"""Method Description

		Returns:
			Dict[int,int]: 
		"""
		pass

	@overload
	def IWaterQualityElementsResults(self, timeStepIndex: int) -> Dict[int,int]:
		"""Method Description

		Args:
			timeStepIndex(int): timeStepIndex

		Returns:
			Dict[int,int]: 
		"""
		pass

	@overload
	def IWaterQualityElementsResults(self, ids: List[int], timeStepIndex: int) -> Dict[int,int]:
		"""Method Description

		Args:
			ids(List[int]): ids
			timeStepIndex(int): timeStepIndex

		Returns:
			Dict[int,int]: 
		"""
		pass

	@overload
	def IWaterQualityElementsResults(self) -> Dict[int,int]:
		"""Method Description

		Returns:
			Dict[int,int]: 
		"""
		pass

	@overload
	def IWaterQualityElementsResults(self, timeStepIndex: int) -> Dict[int,int]:
		"""Method Description

		Args:
			timeStepIndex(int): timeStepIndex

		Returns:
			Dict[int,int]: 
		"""
		pass

	@overload
	def IWaterQualityElementsResults(self, ids: List[int], timeStepIndex: int) -> Dict[int,int]:
		"""Method Description

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
		"""
		Returns:
			IUnit: No Description
		"""
		pass

	@property
	def TraceUnit(self) -> IUnit:
		"""
		Returns:
			IUnit: No Description
		"""
		pass

	@property
	def ConcentrationUnit(self) -> IUnit:
		"""
		Returns:
			IUnit: No Description
		"""
		pass

class IWaterNetwork(INetwork[IWaterNetworkElement, WaterNetworkElementType]):

	def __init__(self) -> None:
		"""Creating a new Instance of this class is not allowed


		Raises:
			Exception: if this class is instanciated
		"""
		raise Exception("Creating a new Instance of this class is not allowed")
		pass

	@property
	def Pipes(self) -> IPipes:
		"""
		Returns:
			IPipes: No Description
		"""
		pass

	@property
	def Laterals(self) -> ILaterals:
		"""
		Returns:
			ILaterals: No Description
		"""
		pass

	@property
	def Junctions(self) -> IJunctions:
		"""
		Returns:
			IJunctions: No Description
		"""
		pass

	@property
	def Hydrants(self) -> IHydrants:
		"""
		Returns:
			IHydrants: No Description
		"""
		pass

	@property
	def Tanks(self) -> ITanks:
		"""
		Returns:
			ITanks: No Description
		"""
		pass

	@property
	def Reservoirs(self) -> IReservoirs:
		"""
		Returns:
			IReservoirs: No Description
		"""
		pass

	@property
	def Taps(self) -> ITaps:
		"""
		Returns:
			ITaps: No Description
		"""
		pass

	@property
	def CustomerMeters(self) -> ICustomerMeters:
		"""
		Returns:
			ICustomerMeters: No Description
		"""
		pass

	@property
	def Pumps(self) -> IPumps:
		"""
		Returns:
			IPumps: No Description
		"""
		pass

	@property
	def VSPBs(self) -> IVariableSpeedPumpBatterys:
		"""
		Returns:
			IVariableSpeedPumpBatterys: No Description
		"""
		pass

	@property
	def PumpStations(self) -> IPumpStations:
		"""
		Returns:
			IPumpStations: No Description
		"""
		pass

	@property
	def SCADAElements(self) -> ISCADAElements:
		"""
		Returns:
			ISCADAElements: No Description
		"""
		pass

	@property
	def PRVs(self) -> IPressureReducingValves:
		"""
		Returns:
			IPressureReducingValves: No Description
		"""
		pass

	@property
	def PBVs(self) -> IPressureBreakingValves:
		"""
		Returns:
			IPressureBreakingValves: No Description
		"""
		pass

	@property
	def PSVs(self) -> IPressureSustainingValves:
		"""
		Returns:
			IPressureSustainingValves: No Description
		"""
		pass

	@property
	def TCVs(self) -> IThrottleControlValves:
		"""
		Returns:
			IThrottleControlValves: No Description
		"""
		pass

	@property
	def FCVs(self) -> IFlowControlValves:
		"""
		Returns:
			IFlowControlValves: No Description
		"""
		pass

	@property
	def GPVs(self) -> IGeneralPurposeValves:
		"""
		Returns:
			IGeneralPurposeValves: No Description
		"""
		pass

	@property
	def IsolationValves(self) -> IIsolationValves:
		"""
		Returns:
			IIsolationValves: No Description
		"""
		pass

	@property
	def CheckValves(self) -> ICheckValves:
		"""
		Returns:
			ICheckValves: No Description
		"""
		pass

	@property
	def SpotElevations(self) -> ISpotElevations:
		"""
		Returns:
			ISpotElevations: No Description
		"""
		pass

	@property
	def ValvesWithLinearAreaChange(self) -> IValvesWithLinearAreaChange:
		"""
		Returns:
			IValvesWithLinearAreaChange: No Description
		"""
		pass

	@property
	def PeriodicHeadFlows(self) -> IPeriodicHeadFlows:
		"""
		Returns:
			IPeriodicHeadFlows: No Description
		"""
		pass

	@property
	def AirValves(self) -> IAirValves:
		"""
		Returns:
			IAirValves: No Description
		"""
		pass

	@property
	def OrificesBetweenTwoPipes(self) -> IOrificesBetweenTwoPipes:
		"""
		Returns:
			IOrificesBetweenTwoPipes: No Description
		"""
		pass

	@property
	def SurgeValves(self) -> ISurgeValves:
		"""
		Returns:
			ISurgeValves: No Description
		"""
		pass

	@property
	def DischargeToAtmospheres(self) -> IDischargeToAtmospheres:
		"""
		Returns:
			IDischargeToAtmospheres: No Description
		"""
		pass

	@property
	def RuptureDisks(self) -> IRuptureDisks:
		"""
		Returns:
			IRuptureDisks: No Description
		"""
		pass

	@property
	def Turbines(self) -> ITurbines:
		"""
		Returns:
			ITurbines: No Description
		"""
		pass

	@property
	def SurgeTanks(self) -> ISurgeTanks:
		"""
		Returns:
			ISurgeTanks: No Description
		"""
		pass

	@property
	def HydropneumaticTanks(self) -> IHydropneumaticTanks:
		"""
		Returns:
			IHydropneumaticTanks: No Description
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
		"""Method Description

		Returns:
			Dict[int,int]: 
		"""
		pass

	@overload
	def IHammerPipesResults(self, ids: List[int]) -> Dict[int,int]:
		"""Method Description

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
		"""Method Description

		Returns:
			Dict[int,int]: 
		"""
		pass

	@overload
	def IPipesResults(self, timeStepIndex: int) -> Dict[int,int]:
		"""Method Description

		Args:
			timeStepIndex(int): timeStepIndex

		Returns:
			Dict[int,int]: 
		"""
		pass

	@overload
	def IPipesResults(self, ids: List[int], timeStepIndex: int) -> Dict[int,int]:
		"""Method Description

		Args:
			ids(List[int]): ids
			timeStepIndex(int): timeStepIndex

		Returns:
			Dict[int,int]: 
		"""
		pass

	@overload
	def IPipesResults(self) -> Dict[int,int]:
		"""Method Description

		Returns:
			Dict[int,int]: 
		"""
		pass

	@overload
	def IPipesResults(self, timeStepIndex: int) -> Dict[int,int]:
		"""Method Description

		Args:
			timeStepIndex(int): timeStepIndex

		Returns:
			Dict[int,int]: 
		"""
		pass

	@overload
	def IPipesResults(self, ids: List[int], timeStepIndex: int) -> Dict[int,int]:
		"""Method Description

		Args:
			ids(List[int]): ids
			timeStepIndex(int): timeStepIndex

		Returns:
			Dict[int,int]: 
		"""
		pass

	@overload
	def IPipesResults(self) -> Dict[int,int]:
		"""Method Description

		Returns:
			Dict[int,int]: 
		"""
		pass

	@overload
	def IPipesResults(self, timeStepIndex: int) -> Dict[int,int]:
		"""Method Description

		Args:
			timeStepIndex(int): timeStepIndex

		Returns:
			Dict[int,int]: 
		"""
		pass

	@overload
	def IPipesResults(self, ids: List[int], timeStepIndex: int) -> Dict[int,int]:
		"""Method Description

		Args:
			ids(List[int]): ids
			timeStepIndex(int): timeStepIndex

		Returns:
			Dict[int,int]: 
		"""
		pass

	@overload
	def IPipesResults(self) -> Dict[int,int]:
		"""Method Description

		Returns:
			Dict[int,int]: 
		"""
		pass

	@overload
	def IPipesResults(self, timeStepIndex: int) -> Dict[int,int]:
		"""Method Description

		Args:
			timeStepIndex(int): timeStepIndex

		Returns:
			Dict[int,int]: 
		"""
		pass

	@overload
	def IPipesResults(self, ids: List[int], timeStepIndex: int) -> Dict[int,int]:
		"""Method Description

		Args:
			ids(List[int]): ids
			timeStepIndex(int): timeStepIndex

		Returns:
			Dict[int,int]: 
		"""
		pass

	@overload
	def IPipesResults(self) -> Dict[int,int]:
		"""Method Description

		Returns:
			Dict[int,int]: 
		"""
		pass

	@overload
	def IPipesResults(self, timeStepIndex: int) -> Dict[int,int]:
		"""Method Description

		Args:
			timeStepIndex(int): timeStepIndex

		Returns:
			Dict[int,int]: 
		"""
		pass

	@overload
	def IPipesResults(self, ids: List[int], timeStepIndex: int) -> Dict[int,int]:
		"""Method Description

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
		"""Method Description

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
		"""Method Description

		Returns:
			Nullable: 
		"""
		pass

	@overload
	def IPipeResults(self, timeStepIndex: int) -> Union[float, None]:
		"""Method Description

		Args:
			timeStepIndex(int): timeStepIndex

		Returns:
			Nullable: 
		"""
		pass

	@overload
	def IPipeResults(self) -> Union[float, None]:
		"""Method Description

		Returns:
			Nullable: 
		"""
		pass

	@overload
	def IPipeResults(self, timeStepIndex: int) -> Union[float, None]:
		"""Method Description

		Args:
			timeStepIndex(int): timeStepIndex

		Returns:
			Nullable: 
		"""
		pass

	@overload
	def IPipeResults(self) -> Union[float, None]:
		"""Method Description

		Returns:
			Nullable: 
		"""
		pass

	@overload
	def IPipeResults(self, timeStepIndex: int) -> Union[float, None]:
		"""Method Description

		Args:
			timeStepIndex(int): timeStepIndex

		Returns:
			Nullable: 
		"""
		pass

	@overload
	def IPipeResults(self) -> Union[float, None]:
		"""Method Description

		Returns:
			Nullable: 
		"""
		pass

	@overload
	def IPipeResults(self, timeStepIndex: int) -> Union[float, None]:
		"""Method Description

		Args:
			timeStepIndex(int): timeStepIndex

		Returns:
			Nullable: 
		"""
		pass

	@overload
	def IPipeResults(self) -> Union[int, None]:
		"""Method Description

		Returns:
			Nullable: 
		"""
		pass

	@overload
	def IPipeResults(self, timeStepIndex: int) -> Union[int, None]:
		"""Method Description

		Args:
			timeStepIndex(int): timeStepIndex

		Returns:
			Nullable: 
		"""
		pass

	def Flows(self) -> array(Union[float, None]):
		"""Method Description

		Returns:
			Nullable[]: 
		"""
		pass

	def Velocities(self) -> array(Union[float, None]):
		"""Method Description

		Returns:
			Nullable[]: 
		"""
		pass

	def Headlosses(self) -> array(Union[float, None]):
		"""Method Description

		Returns:
			Nullable[]: 
		"""
		pass

	def HeadlossGradients(self) -> array(Union[float, None]):
		"""Method Description

		Returns:
			Nullable[]: 
		"""
		pass

	def CalculatedStatuses(self) -> array(Union[int, None]):
		"""Method Description

		Returns:
			Nullable[]: 
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
		"""
		Returns:
			int: No Description
		"""
		pass

	@property
	def InitialStatus(self) -> PipeStatusType:
		"""
		Returns:
			PipeStatusType: No Description
		"""
		pass

	@property
	def Diameter(self) -> float:
		"""
		Returns:
			float: No Description
		"""
		pass

	@property
	def Material(self) -> str:
		"""
		Returns:
			str: No Description
		"""
		pass

	@property
	def FrictionCoefficient(self) -> float:
		"""
		Returns:
			float: No Description
		"""
		pass

	@property
	def MinorLossCoefficientCollection(self) -> IMinorLossCoefficientCollection:
		"""
		Returns:
			IMinorLossCoefficientCollection: No Description
		"""
		pass

	@property
	def LocalMinorLossCoefficient(self) -> float:
		"""
		Returns:
			float: No Description
		"""
		pass

	@property
	def SpecifyLocalMinorLoss(self) -> bool:
		"""
		Returns:
			bool: No Description
		"""
		pass

	@property
	def DerivedMinorLossCoefficient(self) -> float:
		"""
		Returns:
			float: No Description
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
		"""Method Description

		Returns:
			Dict[int,int]: 
		"""
		pass

	@overload
	def IPipesInput(self, ids: List[int]) -> Dict[int,int]:
		"""Method Description

		Args:
			ids(List[int]): ids

		Returns:
			Dict[int,int]: 
		"""
		pass

	@overload
	def IPipesInput(self) -> Dict[int,int]:
		"""Method Description

		Returns:
			Dict[int,int]: 
		"""
		pass

	@overload
	def IPipesInput(self, ids: List[int]) -> Dict[int,int]:
		"""Method Description

		Args:
			ids(List[int]): ids

		Returns:
			Dict[int,int]: 
		"""
		pass

	@overload
	def IPipesInput(self) -> Dict[int,int]:
		"""Method Description

		Returns:
			Dict[int,int]: 
		"""
		pass

	@overload
	def IPipesInput(self, ids: List[int]) -> Dict[int,int]:
		"""Method Description

		Args:
			ids(List[int]): ids

		Returns:
			Dict[int,int]: 
		"""
		pass

	@overload
	def IPipesInput(self) -> Dict[int,int]:
		"""Method Description

		Returns:
			Dict[int,int]: 
		"""
		pass

	@overload
	def IPipesInput(self, ids: List[int]) -> Dict[int,int]:
		"""Method Description

		Args:
			ids(List[int]): ids

		Returns:
			Dict[int,int]: 
		"""
		pass

	@overload
	def IPipesInput(self) -> Dict[int,int]:
		"""Method Description

		Returns:
			Dict[int,int]: 
		"""
		pass

	@overload
	def IPipesInput(self, ids: List[int]) -> Dict[int,int]:
		"""Method Description

		Args:
			ids(List[int]): ids

		Returns:
			Dict[int,int]: 
		"""
		pass

	def LocalMinorLossCoefficient(self) -> Dict[int,int]:
		"""Method Description

		Returns:
			Dict[int,int]: 
		"""
		pass

	def SpecifyLocalMinorLoss(self) -> Dict[int,int]:
		"""Method Description

		Returns:
			Dict[int,int]: 
		"""
		pass

	def DerivedMinorLossCoefficient(self) -> Dict[int,int]:
		"""Method Description

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
		"""
		Returns:
			IUnit: No Description
		"""
		pass

	@property
	def FlowUnit(self) -> IUnit:
		"""
		Returns:
			IUnit: No Description
		"""
		pass

	@property
	def VelocityUnit(self) -> IUnit:
		"""
		Returns:
			IUnit: No Description
		"""
		pass

	@property
	def HeadlossUnit(self) -> IUnit:
		"""
		Returns:
			IUnit: No Description
		"""
		pass

	@property
	def HeadlossGradientUnit(self) -> IUnit:
		"""
		Returns:
			IUnit: No Description
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
		"""Method Description

		Returns:
			Dict[int,int]: 
		"""
		pass

	@overload
	def IFireFlowNodesResults(self, timeStepIndex: int) -> Dict[int,int]:
		"""Method Description

		Args:
			timeStepIndex(int): timeStepIndex

		Returns:
			Dict[int,int]: 
		"""
		pass

	@overload
	def IFireFlowNodesResults(self, ids: List[int], timeStepIndex: int) -> Dict[int,int]:
		"""Method Description

		Args:
			ids(List[int]): ids
			timeStepIndex(int): timeStepIndex

		Returns:
			Dict[int,int]: 
		"""
		pass

	@overload
	def IFireFlowNodesResults(self) -> Dict[int,int]:
		"""Method Description

		Returns:
			Dict[int,int]: 
		"""
		pass

	@overload
	def IFireFlowNodesResults(self, timeStepIndex: int) -> Dict[int,int]:
		"""Method Description

		Args:
			timeStepIndex(int): timeStepIndex

		Returns:
			Dict[int,int]: 
		"""
		pass

	@overload
	def IFireFlowNodesResults(self, ids: List[int], timeStepIndex: int) -> Dict[int,int]:
		"""Method Description

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
		"""Method Description

		Returns:
			Nullable: 
		"""
		pass

	@overload
	def IFireFlowNodeResults(self, timeStepIndex: int) -> Union[float, None]:
		"""Method Description

		Args:
			timeStepIndex(int): timeStepIndex

		Returns:
			Nullable: 
		"""
		pass

	@overload
	def IFireFlowNodeResults(self) -> Union[float, None]:
		"""Method Description

		Returns:
			Nullable: 
		"""
		pass

	@overload
	def IFireFlowNodeResults(self, timeStepIndex: int) -> Union[float, None]:
		"""Method Description

		Args:
			timeStepIndex(int): timeStepIndex

		Returns:
			Nullable: 
		"""
		pass

	def Demands(self) -> array(Union[float, None]):
		"""Method Description

		Returns:
			Nullable[]: 
		"""
		pass

	def Pressures(self) -> array(Union[float, None]):
		"""Method Description

		Returns:
			Nullable[]: 
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
		"""
		Returns:
			IDemandCollection: No Description
		"""
		pass

	@property
	def UnitDemandLoadCollection(self) -> IUnitLoadDemandCollection:
		"""
		Returns:
			IUnitLoadDemandCollection: No Description
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
		"""Method Description

		Args:
			flow(float): flow
			pattern(IPattern): pattern

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
		"""
		Returns:
			float: No Description
		"""
		pass

	@property
	def DemandPattern(self) -> IPattern:
		"""
		Returns:
			IPattern: No Description
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
		"""
		Returns:
			IUnit: No Description
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
		"""Method Description

		Args:
			unitDemandLoad(IUnitDemandLoad): unitDemandLoad
			numberOfLoadingUnits(float): numberOfLoadingUnits
			unitDemandBaseFlow(float): unitDemandBaseFlow
			unitDemandPattern(IPattern): unitDemandPattern

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
		"""
		Returns:
			IUnitDemandLoad: No Description
		"""
		pass

	@property
	def NumberOfLoadingUnits(self) -> float:
		"""
		Returns:
			float: No Description
		"""
		pass

	@property
	def UnitDemandBaseFlow(self) -> float:
		"""
		Returns:
			float: No Description
		"""
		pass

	@property
	def UnitDemandPattern(self) -> IPattern:
		"""
		Returns:
			IPattern: No Description
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
		"""
		Returns:
			IUnit: No Description
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
		"""Method Description

		Returns:
			Dict[int,int]: 
		"""
		pass

	@overload
	def IConventionalTanksResults(self, timeStepIndex: int) -> Dict[int,int]:
		"""Method Description

		Args:
			timeStepIndex(int): timeStepIndex

		Returns:
			Dict[int,int]: 
		"""
		pass

	@overload
	def IConventionalTanksResults(self, ids: List[int], timeStepIndex: int) -> Dict[int,int]:
		"""Method Description

		Args:
			ids(List[int]): ids
			timeStepIndex(int): timeStepIndex

		Returns:
			Dict[int,int]: 
		"""
		pass

	@overload
	def IConventionalTanksResults(self) -> Dict[int,int]:
		"""Method Description

		Returns:
			Dict[int,int]: 
		"""
		pass

	@overload
	def IConventionalTanksResults(self, timeStepIndex: int) -> Dict[int,int]:
		"""Method Description

		Args:
			timeStepIndex(int): timeStepIndex

		Returns:
			Dict[int,int]: 
		"""
		pass

	@overload
	def IConventionalTanksResults(self, ids: List[int], timeStepIndex: int) -> Dict[int,int]:
		"""Method Description

		Args:
			ids(List[int]): ids
			timeStepIndex(int): timeStepIndex

		Returns:
			Dict[int,int]: 
		"""
		pass

	@overload
	def IConventionalTanksResults(self) -> Dict[int,int]:
		"""Method Description

		Returns:
			Dict[int,int]: 
		"""
		pass

	@overload
	def IConventionalTanksResults(self, timeStepIndex: int) -> Dict[int,int]:
		"""Method Description

		Args:
			timeStepIndex(int): timeStepIndex

		Returns:
			Dict[int,int]: 
		"""
		pass

	@overload
	def IConventionalTanksResults(self, ids: List[int], timeStepIndex: int) -> Dict[int,int]:
		"""Method Description

		Args:
			ids(List[int]): ids
			timeStepIndex(int): timeStepIndex

		Returns:
			Dict[int,int]: 
		"""
		pass

	@overload
	def IConventionalTanksResults(self) -> Dict[int,int]:
		"""Method Description

		Returns:
			Dict[int,int]: 
		"""
		pass

	@overload
	def IConventionalTanksResults(self, timeStepIndex: int) -> Dict[int,int]:
		"""Method Description

		Args:
			timeStepIndex(int): timeStepIndex

		Returns:
			Dict[int,int]: 
		"""
		pass

	@overload
	def IConventionalTanksResults(self, ids: List[int], timeStepIndex: int) -> Dict[int,int]:
		"""Method Description

		Args:
			ids(List[int]): ids
			timeStepIndex(int): timeStepIndex

		Returns:
			Dict[int,int]: 
		"""
		pass

	def VolumeFulls(self) -> Dict[int,int]:
		"""Method Description

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
		"""Method Description

		Returns:
			Nullable: 
		"""
		pass

	@overload
	def IConventionalTankResults(self, timeStepIndex: int) -> Union[float, None]:
		"""Method Description

		Args:
			timeStepIndex(int): timeStepIndex

		Returns:
			Nullable: 
		"""
		pass

	@overload
	def IConventionalTankResults(self) -> Union[float, None]:
		"""Method Description

		Returns:
			Nullable: 
		"""
		pass

	@overload
	def IConventionalTankResults(self, timeStepIndex: int) -> Union[float, None]:
		"""Method Description

		Args:
			timeStepIndex(int): timeStepIndex

		Returns:
			Nullable: 
		"""
		pass

	@overload
	def IConventionalTankResults(self) -> Union[float, None]:
		"""Method Description

		Returns:
			Nullable: 
		"""
		pass

	@overload
	def IConventionalTankResults(self, timeStepIndex: int) -> Union[float, None]:
		"""Method Description

		Args:
			timeStepIndex(int): timeStepIndex

		Returns:
			Nullable: 
		"""
		pass

	@overload
	def IConventionalTankResults(self) -> Union[int, None]:
		"""Method Description

		Returns:
			Nullable: 
		"""
		pass

	@overload
	def IConventionalTankResults(self, timeStepIndex: int) -> Union[int, None]:
		"""Method Description

		Args:
			timeStepIndex(int): timeStepIndex

		Returns:
			Nullable: 
		"""
		pass

	def VolumeFull(self) -> Union[float, None]:
		"""Method Description

		Returns:
			Nullable: 
		"""
		pass

	def Levels(self) -> array(Union[float, None]):
		"""Method Description

		Returns:
			Nullable[]: 
		"""
		pass

	def Volumes(self) -> array(Union[float, None]):
		"""Method Description

		Returns:
			Nullable[]: 
		"""
		pass

	def PercentFulls(self) -> array(Union[float, None]):
		"""Method Description

		Returns:
			Nullable[]: 
		"""
		pass

	def TankStatuses(self) -> array(Union[int, None]):
		"""Method Description

		Returns:
			Nullable[]: 
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
		"""Method Description

		Returns:
			Dict[int,int]: 
		"""
		pass

	@overload
	def IConventionalTanksInput(self, ids: List[int]) -> Dict[int,int]:
		"""Method Description

		Args:
			ids(List[int]): ids

		Returns:
			Dict[int,int]: 
		"""
		pass

	@overload
	def IConventionalTanksInput(self) -> Dict[int,int]:
		"""Method Description

		Returns:
			Dict[int,int]: 
		"""
		pass

	@overload
	def IConventionalTanksInput(self, ids: List[int]) -> Dict[int,int]:
		"""Method Description

		Args:
			ids(List[int]): ids

		Returns:
			Dict[int,int]: 
		"""
		pass

	@overload
	def IConventionalTanksInput(self) -> Dict[int,int]:
		"""Method Description

		Returns:
			Dict[int,int]: 
		"""
		pass

	@overload
	def IConventionalTanksInput(self, ids: List[int]) -> Dict[int,int]:
		"""Method Description

		Args:
			ids(List[int]): ids

		Returns:
			Dict[int,int]: 
		"""
		pass

	@overload
	def IConventionalTanksInput(self) -> Dict[int,int]:
		"""Method Description

		Returns:
			Dict[int,int]: 
		"""
		pass

	@overload
	def IConventionalTanksInput(self, ids: List[int]) -> Dict[int,int]:
		"""Method Description

		Args:
			ids(List[int]): ids

		Returns:
			Dict[int,int]: 
		"""
		pass

	@overload
	def IConventionalTanksInput(self) -> Dict[int,int]:
		"""Method Description

		Returns:
			Dict[int,int]: 
		"""
		pass

	@overload
	def IConventionalTanksInput(self, ids: List[int]) -> Dict[int,int]:
		"""Method Description

		Args:
			ids(List[int]): ids

		Returns:
			Dict[int,int]: 
		"""
		pass

	@overload
	def IConventionalTanksInput(self) -> Dict[int,int]:
		"""Method Description

		Returns:
			Dict[int,int]: 
		"""
		pass

	@overload
	def IConventionalTanksInput(self, ids: List[int]) -> Dict[int,int]:
		"""Method Description

		Args:
			ids(List[int]): ids

		Returns:
			Dict[int,int]: 
		"""
		pass

	@overload
	def IConventionalTanksInput(self) -> Dict[int,int]:
		"""Method Description

		Returns:
			Dict[int,int]: 
		"""
		pass

	@overload
	def IConventionalTanksInput(self, ids: List[int]) -> Dict[int,int]:
		"""Method Description

		Args:
			ids(List[int]): ids

		Returns:
			Dict[int,int]: 
		"""
		pass

	@overload
	def IConventionalTanksInput(self) -> Dict[int,int]:
		"""Method Description

		Returns:
			Dict[int,int]: 
		"""
		pass

	@overload
	def IConventionalTanksInput(self, ids: List[int]) -> Dict[int,int]:
		"""Method Description

		Args:
			ids(List[int]): ids

		Returns:
			Dict[int,int]: 
		"""
		pass

	@overload
	def IConventionalTanksInput(self) -> Dict[int,int]:
		"""Method Description

		Returns:
			Dict[int,int]: 
		"""
		pass

	@overload
	def IConventionalTanksInput(self, ids: List[int]) -> Dict[int,int]:
		"""Method Description

		Args:
			ids(List[int]): ids

		Returns:
			Dict[int,int]: 
		"""
		pass

	@overload
	def IConventionalTanksInput(self) -> Dict[int,int]:
		"""Method Description

		Returns:
			Dict[int,int]: 
		"""
		pass

	@overload
	def IConventionalTanksInput(self, ids: List[int]) -> Dict[int,int]:
		"""Method Description

		Args:
			ids(List[int]): ids

		Returns:
			Dict[int,int]: 
		"""
		pass

	@overload
	def IConventionalTanksInput(self) -> Dict[int,int]:
		"""Method Description

		Returns:
			Dict[int,int]: 
		"""
		pass

	@overload
	def IConventionalTanksInput(self, ids: List[int]) -> Dict[int,int]:
		"""Method Description

		Args:
			ids(List[int]): ids

		Returns:
			Dict[int,int]: 
		"""
		pass

	@overload
	def IConventionalTanksInput(self) -> Dict[int,int]:
		"""Method Description

		Returns:
			Dict[int,int]: 
		"""
		pass

	@overload
	def IConventionalTanksInput(self, ids: List[int]) -> Dict[int,int]:
		"""Method Description

		Args:
			ids(List[int]): ids

		Returns:
			Dict[int,int]: 
		"""
		pass

	@overload
	def IConventionalTanksInput(self) -> Dict[int,int]:
		"""Method Description

		Returns:
			Dict[int,int]: 
		"""
		pass

	@overload
	def IConventionalTanksInput(self, ids: List[int]) -> Dict[int,int]:
		"""Method Description

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
		"""
		Returns:
			TankSectionType: No Description
		"""
		pass

	@property
	def ActiveVolumeFull(self) -> float:
		"""
		Returns:
			float: No Description
		"""
		pass

	@property
	def CrossSectionCurve(self) -> ICrossSectionCurveCollection:
		"""
		Returns:
			ICrossSectionCurveCollection: No Description
		"""
		pass

	@property
	def Diameter(self) -> float:
		"""
		Returns:
			float: No Description
		"""
		pass

	@property
	def AverageArea(self) -> float:
		"""
		Returns:
			float: No Description
		"""
		pass

	@property
	def BaseElevation(self) -> float:
		"""
		Returns:
			float: No Description
		"""
		pass

	@property
	def MinimumLevel(self) -> float:
		"""
		Returns:
			float: No Description
		"""
		pass

	@property
	def InitialLevel(self) -> float:
		"""
		Returns:
			float: No Description
		"""
		pass

	@property
	def MaximumLevel(self) -> float:
		"""
		Returns:
			float: No Description
		"""
		pass

	@property
	def UseHighAlarm(self) -> bool:
		"""
		Returns:
			bool: No Description
		"""
		pass

	@property
	def HighAlarmLevel(self) -> float:
		"""
		Returns:
			float: No Description
		"""
		pass

	@property
	def UseLowAlarm(self) -> bool:
		"""
		Returns:
			bool: No Description
		"""
		pass

	@property
	def LowAlarmLevel(self) -> float:
		"""
		Returns:
			float: No Description
		"""
		pass

	@property
	def InactiveVolume(self) -> float:
		"""
		Returns:
			float: No Description
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
		"""
		Returns:
			IUnit: No Description
		"""
		pass

	@property
	def VolumeUnit(self) -> IUnit:
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
		"""Method Description

		Args:
			depthRatio(float): depthRatio
			volumeRatio(float): volumeRatio

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
		"""
		Returns:
			float: No Description
		"""
		pass

	@property
	def VolumeRatio(self) -> float:
		"""
		Returns:
			float: No Description
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
		"""
		Returns:
			IUnit: No Description
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
		"""Method Description

		Returns:
			Dict[int,int]: 
		"""
		pass

	def ValveTypes(self) -> Dict[int,int]:
		"""Method Description

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
		"""
		Returns:
			IValveCharacteristic: No Description
		"""
		pass

	@property
	def ValveType(self) -> HammerValveType:
		"""
		Returns:
			HammerValveType: No Description
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
		"""
		Returns:
			float: No Description
		"""
		pass

	@property
	def RatioOfLosses(self) -> float:
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
	def SurgeTankType(self) -> SurgeTankTypeEnum:
		"""
		Returns:
			SurgeTankTypeEnum: No Description
		"""
		pass

	@property
	def HasCheckValve(self) -> bool:
		"""
		Returns:
			bool: No Description
		"""
		pass

	@property
	def WeirCoefficient(self) -> float:
		"""
		Returns:
			float: No Description
		"""
		pass

	@property
	def WeirLength(self) -> float:
		"""
		Returns:
			float: No Description
		"""
		pass

	@property
	def InternalRiserDiameter(self) -> float:
		"""
		Returns:
			float: No Description
		"""
		pass

	@property
	def InternalRiserTopElevation(self) -> float:
		"""
		Returns:
			float: No Description
		"""
		pass

	@property
	def JunctionElevation(self) -> float:
		"""
		Returns:
			float: No Description
		"""
		pass

	@property
	def DiameterExternalRiser(self) -> float:
		"""
		Returns:
			float: No Description
		"""
		pass

	@property
	def ElevationOrificeFromInternalRiserInTank(self) -> float:
		"""
		Returns:
			float: No Description
		"""
		pass

	@property
	def ElevationTopOfTankBase(self) -> float:
		"""
		Returns:
			float: No Description
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
		"""Method Description

		Returns:
			Dict[int,int]: 
		"""
		pass

	def RatioOfLosses(self) -> Dict[int,int]:
		"""Method Description

		Returns:
			Dict[int,int]: 
		"""
		pass

	def HeadlossCoefficient(self) -> Dict[int,int]:
		"""Method Description

		Returns:
			Dict[int,int]: 
		"""
		pass

	def SurgeTankType(self) -> Dict[int,int]:
		"""Method Description

		Returns:
			Dict[int,int]: 
		"""
		pass

	def HasCheckValve(self) -> Dict[int,int]:
		"""Method Description

		Returns:
			Dict[int,int]: 
		"""
		pass

	def WeirCoefficient(self) -> Dict[int,int]:
		"""Method Description

		Returns:
			Dict[int,int]: 
		"""
		pass

	def WeirLength(self) -> Dict[int,int]:
		"""Method Description

		Returns:
			Dict[int,int]: 
		"""
		pass

	def InternalRiserDiameter(self) -> Dict[int,int]:
		"""Method Description

		Returns:
			Dict[int,int]: 
		"""
		pass

	def InternalRiserTopElevation(self) -> Dict[int,int]:
		"""Method Description

		Returns:
			Dict[int,int]: 
		"""
		pass

	def JunctionElevation(self) -> Dict[int,int]:
		"""Method Description

		Returns:
			Dict[int,int]: 
		"""
		pass

	def DiameterExternalRiser(self) -> Dict[int,int]:
		"""Method Description

		Returns:
			Dict[int,int]: 
		"""
		pass

	def ElevationOrificeFromInternalRiserInTank(self) -> Dict[int,int]:
		"""Method Description

		Returns:
			Dict[int,int]: 
		"""
		pass

	def ElevationTopOfTankBase(self) -> Dict[int,int]:
		"""Method Description

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
		"""
		Returns:
			IUnit: No Description
		"""
		pass

	@property
	def RatioUnit(self) -> IUnit:
		"""
		Returns:
			IUnit: No Description
		"""
		pass

	@property
	def WeirCoefficientUnit(self) -> IUnit:
		"""
		Returns:
			IUnit: No Description
		"""
		pass

	@property
	def LengthUnit(self) -> IUnit:
		"""
		Returns:
			IUnit: No Description
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
		"""Method Description

		Returns:
			Dict[int,int]: 
		"""
		pass

	@overload
	def IBaseTanksResults(self, timeStepIndex: int) -> Dict[int,int]:
		"""Method Description

		Args:
			timeStepIndex(int): timeStepIndex

		Returns:
			Dict[int,int]: 
		"""
		pass

	@overload
	def IBaseTanksResults(self, ids: List[int], timeStepIndex: int) -> Dict[int,int]:
		"""Method Description

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
		"""Method Description

		Returns:
			Nullable: 
		"""
		pass

	@overload
	def IBaseTankResults(self, timeStepIndex: int) -> Union[float, None]:
		"""Method Description

		Args:
			timeStepIndex(int): timeStepIndex

		Returns:
			Nullable: 
		"""
		pass

	def Flows(self) -> array(Union[float, None]):
		"""Method Description

		Returns:
			Nullable[]: 
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
		"""
		Returns:
			IUnit: No Description
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
		"""Method Description

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
		"""
		Returns:
			float: No Description
		"""
		pass

	@property
	def EquivalentDiameter(self) -> float:
		"""
		Returns:
			float: No Description
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
		"""
		Returns:
			IUnit: No Description
		"""
		pass

	@property
	def DiameterUnit(self) -> IUnit:
		"""
		Returns:
			IUnit: No Description
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
		"""
		Returns:
			float: No Description
		"""
		pass

	@property
	def TankInletOrificeDiameter(self) -> float:
		"""
		Returns:
			float: No Description
		"""
		pass

	@property
	def RatioOfLosses(self) -> float:
		"""
		Returns:
			float: No Description
		"""
		pass

	@property
	def GasLawExponent(self) -> float:
		"""
		Returns:
			float: No Description
		"""
		pass

	@property
	def HasBladder(self) -> bool:
		"""
		Returns:
			bool: No Description
		"""
		pass

	@property
	def GasPresetPressure(self) -> float:
		"""
		Returns:
			float: No Description
		"""
		pass

	@property
	def MeanLiquidElevation(self) -> float:
		"""
		Returns:
			float: No Description
		"""
		pass

	@property
	def AirInflowOrificeDiameter(self) -> float:
		"""
		Returns:
			float: No Description
		"""
		pass

	@property
	def AirOutflowOrificeDiameter(self) -> float:
		"""
		Returns:
			float: No Description
		"""
		pass

	@property
	def DippingTubeDiameter(self) -> float:
		"""
		Returns:
			float: No Description
		"""
		pass

	@property
	def CompressionChamberVolume(self) -> float:
		"""
		Returns:
			float: No Description
		"""
		pass

	@property
	def TopElevationDippingTube(self) -> float:
		"""
		Returns:
			float: No Description
		"""
		pass

	@property
	def BottomElevationDippingTube(self) -> float:
		"""
		Returns:
			float: No Description
		"""
		pass

	@property
	def LevelType(self) -> GasVesselLevelType:
		"""
		Returns:
			GasVesselLevelType: No Description
		"""
		pass

	@property
	def HydroTankType(self) -> HydroTankType:
		"""
		Returns:
			HydroTankType: No Description
		"""
		pass

	@property
	def VariableLevelCurve(self) -> IVariableLevelCurveCollection:
		"""
		Returns:
			IVariableLevelCurveCollection: No Description
		"""
		pass

	@property
	def TankVolume(self) -> float:
		"""
		Returns:
			float: No Description
		"""
		pass

	@property
	def InflowMinorLossCoefficient(self) -> float:
		"""
		Returns:
			float: No Description
		"""
		pass

	@property
	def TankBaseElevation(self) -> float:
		"""
		Returns:
			float: No Description
		"""
		pass

	@property
	def TreatAsJunction(self) -> bool:
		"""
		Returns:
			bool: No Description
		"""
		pass

	@property
	def OperatingRangeType(self) -> OperatingRangeTypeEnum:
		"""
		Returns:
			OperatingRangeTypeEnum: No Description
		"""
		pass

	@property
	def TankCalculationModel(self) -> TankCalculationModel:
		"""
		Returns:
			TankCalculationModel: No Description
		"""
		pass

	@property
	def TankInitialElevation(self) -> float:
		"""
		Returns:
			float: No Description
		"""
		pass

	@property
	def TankInitialLevel(self) -> float:
		"""
		Returns:
			float: No Description
		"""
		pass

	@property
	def TankInitialLiquidVolume(self) -> float:
		"""
		Returns:
			float: No Description
		"""
		pass

	@property
	def AirInflowOrificeAirFlowCurve(self) -> IAirFlowCurve:
		"""
		Returns:
			IAirFlowCurve: No Description
		"""
		pass

	@property
	def AirOutflowOrificeAirFlowCurve(self) -> IAirFlowCurve:
		"""
		Returns:
			IAirFlowCurve: No Description
		"""
		pass

	@property
	def AirFlowCalculationMethod(self) -> AirFlowCalculationMethod:
		"""
		Returns:
			AirFlowCalculationMethod: No Description
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
		"""Method Description

		Returns:
			Dict[int,int]: 
		"""
		pass

	def TankInletOrificeDiameter(self) -> Dict[int,int]:
		"""Method Description

		Returns:
			Dict[int,int]: 
		"""
		pass

	def RatioOfLosses(self) -> Dict[int,int]:
		"""Method Description

		Returns:
			Dict[int,int]: 
		"""
		pass

	def GasLawExponent(self) -> Dict[int,int]:
		"""Method Description

		Returns:
			Dict[int,int]: 
		"""
		pass

	def HasBladder(self) -> Dict[int,int]:
		"""Method Description

		Returns:
			Dict[int,int]: 
		"""
		pass

	def GasPresetPressure(self) -> Dict[int,int]:
		"""Method Description

		Returns:
			Dict[int,int]: 
		"""
		pass

	def MeanLiquidElevation(self) -> Dict[int,int]:
		"""Method Description

		Returns:
			Dict[int,int]: 
		"""
		pass

	def AirInflowOrificeDiameter(self) -> Dict[int,int]:
		"""Method Description

		Returns:
			Dict[int,int]: 
		"""
		pass

	def AirOutflowOrificeDiameter(self) -> Dict[int,int]:
		"""Method Description

		Returns:
			Dict[int,int]: 
		"""
		pass

	def DippingTubeDiameter(self) -> Dict[int,int]:
		"""Method Description

		Returns:
			Dict[int,int]: 
		"""
		pass

	def CompressionChamberVolume(self) -> Dict[int,int]:
		"""Method Description

		Returns:
			Dict[int,int]: 
		"""
		pass

	def TopElevationDippingTube(self) -> Dict[int,int]:
		"""Method Description

		Returns:
			Dict[int,int]: 
		"""
		pass

	def BottomElevationDippingTube(self) -> Dict[int,int]:
		"""Method Description

		Returns:
			Dict[int,int]: 
		"""
		pass

	def LevelType(self) -> Dict[int,int]:
		"""Method Description

		Returns:
			Dict[int,int]: 
		"""
		pass

	def HydroTankType(self) -> Dict[int,int]:
		"""Method Description

		Returns:
			Dict[int,int]: 
		"""
		pass

	def TankVolume(self) -> Dict[int,int]:
		"""Method Description

		Returns:
			Dict[int,int]: 
		"""
		pass

	def InflowMinorLossCoefficient(self) -> Dict[int,int]:
		"""Method Description

		Returns:
			Dict[int,int]: 
		"""
		pass

	def TankBaseElevation(self) -> Dict[int,int]:
		"""Method Description

		Returns:
			Dict[int,int]: 
		"""
		pass

	def TreatAsJunction(self) -> Dict[int,int]:
		"""Method Description

		Returns:
			Dict[int,int]: 
		"""
		pass

	def OperatingRangeType(self) -> Dict[int,int]:
		"""Method Description

		Returns:
			Dict[int,int]: 
		"""
		pass

	def TankCalculationModel(self) -> Dict[int,int]:
		"""Method Description

		Returns:
			Dict[int,int]: 
		"""
		pass

	def TankInitialElevation(self) -> Dict[int,int]:
		"""Method Description

		Returns:
			Dict[int,int]: 
		"""
		pass

	def TankInitialLevel(self) -> Dict[int,int]:
		"""Method Description

		Returns:
			Dict[int,int]: 
		"""
		pass

	def TankInitialLiquidVolume(self) -> Dict[int,int]:
		"""Method Description

		Returns:
			Dict[int,int]: 
		"""
		pass

	def AirInflowOrificeAirFlowCurve(self) -> Dict[int,int]:
		"""Method Description

		Returns:
			Dict[int,int]: 
		"""
		pass

	def AirOutflowOrificeAirFlowCurve(self) -> Dict[int,int]:
		"""Method Description

		Returns:
			Dict[int,int]: 
		"""
		pass

	def AirFlowCalculationMethod(self) -> Dict[int,int]:
		"""Method Description

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
		"""Method Description

		Returns:
			Nullable: 
		"""
		pass

	@overload
	def IHydroTankResults(self, timeStepIndex: int) -> Union[float, None]:
		"""Method Description

		Args:
			timeStepIndex(int): timeStepIndex

		Returns:
			Nullable: 
		"""
		pass

	@overload
	def IHydroTankResults(self) -> Union[float, None]:
		"""Method Description

		Returns:
			Nullable: 
		"""
		pass

	@overload
	def IHydroTankResults(self, timeStepIndex: int) -> Union[float, None]:
		"""Method Description

		Args:
			timeStepIndex(int): timeStepIndex

		Returns:
			Nullable: 
		"""
		pass

	@overload
	def IHydroTankResults(self) -> Union[float, None]:
		"""Method Description

		Returns:
			Nullable: 
		"""
		pass

	@overload
	def IHydroTankResults(self, timeStepIndex: int) -> Union[float, None]:
		"""Method Description

		Args:
			timeStepIndex(int): timeStepIndex

		Returns:
			Nullable: 
		"""
		pass

	@overload
	def IHydroTankResults(self) -> Union[float, None]:
		"""Method Description

		Returns:
			Nullable: 
		"""
		pass

	@overload
	def IHydroTankResults(self, timeStepIndex: int) -> Union[float, None]:
		"""Method Description

		Args:
			timeStepIndex(int): timeStepIndex

		Returns:
			Nullable: 
		"""
		pass

	def CalculatedGasVolumes(self) -> array(Union[float, None]):
		"""Method Description

		Returns:
			Nullable[]: 
		"""
		pass

	def CalculatedPressures(self) -> array(Union[float, None]):
		"""Method Description

		Returns:
			Nullable[]: 
		"""
		pass

	def CalculatedLiquidVolumes(self) -> array(Union[float, None]):
		"""Method Description

		Returns:
			Nullable[]: 
		"""
		pass

	def CalculatedPercentFulls(self) -> array(Union[float, None]):
		"""Method Description

		Returns:
			Nullable[]: 
		"""
		pass

	def MaximumTransientGasPressure(self) -> Union[float, None]:
		"""Method Description

		Returns:
			Nullable: 
		"""
		pass

	def MinimumTransientGasPressure(self) -> Union[float, None]:
		"""Method Description

		Returns:
			Nullable: 
		"""
		pass

	def MaximumTransientGasVolume(self) -> Union[float, None]:
		"""Method Description

		Returns:
			Nullable: 
		"""
		pass

	def MinimumTransientGasVolume(self) -> Union[float, None]:
		"""Method Description

		Returns:
			Nullable: 
		"""
		pass

	def MaximumTransientWaterLevel(self) -> Union[float, None]:
		"""Method Description

		Returns:
			Nullable: 
		"""
		pass

	def MinimumTransientWaterLevel(self) -> Union[float, None]:
		"""Method Description

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
		"""Method Description

		Returns:
			Dict[int,int]: 
		"""
		pass

	@overload
	def IHydroTanksResults(self, timeStepIndex: int) -> Dict[int,int]:
		"""Method Description

		Args:
			timeStepIndex(int): timeStepIndex

		Returns:
			Dict[int,int]: 
		"""
		pass

	@overload
	def IHydroTanksResults(self, ids: List[int], timeStepIndex: int) -> Dict[int,int]:
		"""Method Description

		Args:
			ids(List[int]): ids
			timeStepIndex(int): timeStepIndex

		Returns:
			Dict[int,int]: 
		"""
		pass

	@overload
	def IHydroTanksResults(self) -> Dict[int,int]:
		"""Method Description

		Returns:
			Dict[int,int]: 
		"""
		pass

	@overload
	def IHydroTanksResults(self, timeStepIndex: int) -> Dict[int,int]:
		"""Method Description

		Args:
			timeStepIndex(int): timeStepIndex

		Returns:
			Dict[int,int]: 
		"""
		pass

	@overload
	def IHydroTanksResults(self, ids: List[int], timeStepIndex: int) -> Dict[int,int]:
		"""Method Description

		Args:
			ids(List[int]): ids
			timeStepIndex(int): timeStepIndex

		Returns:
			Dict[int,int]: 
		"""
		pass

	@overload
	def IHydroTanksResults(self) -> Dict[int,int]:
		"""Method Description

		Returns:
			Dict[int,int]: 
		"""
		pass

	@overload
	def IHydroTanksResults(self, timeStepIndex: int) -> Dict[int,int]:
		"""Method Description

		Args:
			timeStepIndex(int): timeStepIndex

		Returns:
			Dict[int,int]: 
		"""
		pass

	@overload
	def IHydroTanksResults(self, ids: List[int], timeStepIndex: int) -> Dict[int,int]:
		"""Method Description

		Args:
			ids(List[int]): ids
			timeStepIndex(int): timeStepIndex

		Returns:
			Dict[int,int]: 
		"""
		pass

	@overload
	def IHydroTanksResults(self) -> Dict[int,int]:
		"""Method Description

		Returns:
			Dict[int,int]: 
		"""
		pass

	@overload
	def IHydroTanksResults(self, timeStepIndex: int) -> Dict[int,int]:
		"""Method Description

		Args:
			timeStepIndex(int): timeStepIndex

		Returns:
			Dict[int,int]: 
		"""
		pass

	@overload
	def IHydroTanksResults(self, ids: List[int], timeStepIndex: int) -> Dict[int,int]:
		"""Method Description

		Args:
			ids(List[int]): ids
			timeStepIndex(int): timeStepIndex

		Returns:
			Dict[int,int]: 
		"""
		pass

	def MaximumTransientGasPressures(self) -> Dict[int,int]:
		"""Method Description

		Returns:
			Dict[int,int]: 
		"""
		pass

	def MinimumTransientGasPressures(self) -> Dict[int,int]:
		"""Method Description

		Returns:
			Dict[int,int]: 
		"""
		pass

	def MaximumTransientGasVolumes(self) -> Dict[int,int]:
		"""Method Description

		Returns:
			Dict[int,int]: 
		"""
		pass

	def MinimumTransientGasVolumes(self) -> Dict[int,int]:
		"""Method Description

		Returns:
			Dict[int,int]: 
		"""
		pass

	def MaximumTransientWaterLevels(self) -> Dict[int,int]:
		"""Method Description

		Returns:
			Dict[int,int]: 
		"""
		pass

	def MinimumTransientWaterLevels(self) -> Dict[int,int]:
		"""Method Description

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
		"""
		Returns:
			IUnit: No Description
		"""
		pass

	@property
	def DiameterUnit(self) -> IUnit:
		"""
		Returns:
			IUnit: No Description
		"""
		pass

	@property
	def GasExponentUnit(self) -> IUnit:
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
	def LengthUnit(self) -> IUnit:
		"""
		Returns:
			IUnit: No Description
		"""
		pass

	@property
	def PercentUnit(self) -> IUnit:
		"""
		Returns:
			IUnit: No Description
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
		"""Method Description

		Returns:
			Nullable: 
		"""
		pass

	@overload
	def IHammerNodeResults(self, timeStepIndex: int) -> Union[float, None]:
		"""Method Description

		Args:
			timeStepIndex(int): timeStepIndex

		Returns:
			Nullable: 
		"""
		pass

	@overload
	def IHammerNodeResults(self) -> Union[float, None]:
		"""Method Description

		Returns:
			Nullable: 
		"""
		pass

	@overload
	def IHammerNodeResults(self, timeStepIndex: int) -> Union[float, None]:
		"""Method Description

		Args:
			timeStepIndex(int): timeStepIndex

		Returns:
			Nullable: 
		"""
		pass

	def Pressures(self) -> array(Union[float, None]):
		"""Method Description

		Returns:
			Nullable[]: 
		"""
		pass

	def PressureHeads(self) -> array(Union[float, None]):
		"""Method Description

		Returns:
			Nullable[]: 
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
		"""Method Description

		Returns:
			Dict[int,int]: 
		"""
		pass

	@overload
	def IHammerNodesResults(self, timeStepIndex: int) -> Dict[int,int]:
		"""Method Description

		Args:
			timeStepIndex(int): timeStepIndex

		Returns:
			Dict[int,int]: 
		"""
		pass

	@overload
	def IHammerNodesResults(self, ids: List[int], timeStepIndex: int) -> Dict[int,int]:
		"""Method Description

		Args:
			ids(List[int]): ids
			timeStepIndex(int): timeStepIndex

		Returns:
			Dict[int,int]: 
		"""
		pass

	@overload
	def IHammerNodesResults(self) -> Dict[int,int]:
		"""Method Description

		Returns:
			Dict[int,int]: 
		"""
		pass

	@overload
	def IHammerNodesResults(self, timeStepIndex: int) -> Dict[int,int]:
		"""Method Description

		Args:
			timeStepIndex(int): timeStepIndex

		Returns:
			Dict[int,int]: 
		"""
		pass

	@overload
	def IHammerNodesResults(self, ids: List[int], timeStepIndex: int) -> Dict[int,int]:
		"""Method Description

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
		"""
		Returns:
			IUnit: No Description
		"""
		pass

	@property
	def PressureHeadUnit(self) -> IUnit:
		"""
		Returns:
			IUnit: No Description
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
		"""Method Description

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
		"""
		Returns:
			float: No Description
		"""
		pass

	@property
	def Flow(self) -> float:
		"""
		Returns:
			float: No Description
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
		"""
		Returns:
			IUnit: No Description
		"""
		pass

	@property
	def FlowUnit(self) -> IUnit:
		"""
		Returns:
			IUnit: No Description
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
		"""Method Description

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
		"""
		Returns:
			bool: No Description
		"""
		pass

	@property
	def HeadMeanValue(self) -> float:
		"""
		Returns:
			float: No Description
		"""
		pass

	@property
	def HeadAmplitude(self) -> float:
		"""
		Returns:
			float: No Description
		"""
		pass

	@property
	def Phase(self) -> float:
		"""
		Returns:
			float: No Description
		"""
		pass

	@property
	def Period(self) -> float:
		"""
		Returns:
			float: No Description
		"""
		pass

	@property
	def FlowMeanValue(self) -> float:
		"""
		Returns:
			float: No Description
		"""
		pass

	@property
	def FlowAmplitude(self) -> float:
		"""
		Returns:
			float: No Description
		"""
		pass

	@property
	def TransientParameter(self) -> TransientParameterType:
		"""
		Returns:
			TransientParameterType: No Description
		"""
		pass

	@property
	def FlowPatternCollection(self) -> IFlowPatternCollection:
		"""
		Returns:
			IFlowPatternCollection: No Description
		"""
		pass

	@property
	def HeadPatternCollection(self) -> IHeadPatternCollection:
		"""
		Returns:
			IHeadPatternCollection: No Description
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
		"""Method Description

		Returns:
			Dict[int,int]: 
		"""
		pass

	@overload
	def IPeriodicHeadFlowsInput(self, ids: List[int]) -> Dict[int,int]:
		"""Method Description

		Args:
			ids(List[int]): ids

		Returns:
			Dict[int,int]: 
		"""
		pass

	@overload
	def IPeriodicHeadFlowsInput(self) -> Dict[int,int]:
		"""Method Description

		Returns:
			Dict[int,int]: 
		"""
		pass

	@overload
	def IPeriodicHeadFlowsInput(self, ids: List[int]) -> Dict[int,int]:
		"""Method Description

		Args:
			ids(List[int]): ids

		Returns:
			Dict[int,int]: 
		"""
		pass

	@overload
	def IPeriodicHeadFlowsInput(self) -> Dict[int,int]:
		"""Method Description

		Returns:
			Dict[int,int]: 
		"""
		pass

	@overload
	def IPeriodicHeadFlowsInput(self, ids: List[int]) -> Dict[int,int]:
		"""Method Description

		Args:
			ids(List[int]): ids

		Returns:
			Dict[int,int]: 
		"""
		pass

	@overload
	def IPeriodicHeadFlowsInput(self) -> Dict[int,int]:
		"""Method Description

		Returns:
			Dict[int,int]: 
		"""
		pass

	@overload
	def IPeriodicHeadFlowsInput(self, ids: List[int]) -> Dict[int,int]:
		"""Method Description

		Args:
			ids(List[int]): ids

		Returns:
			Dict[int,int]: 
		"""
		pass

	@overload
	def IPeriodicHeadFlowsInput(self) -> Dict[int,int]:
		"""Method Description

		Returns:
			Dict[int,int]: 
		"""
		pass

	@overload
	def IPeriodicHeadFlowsInput(self, ids: List[int]) -> Dict[int,int]:
		"""Method Description

		Args:
			ids(List[int]): ids

		Returns:
			Dict[int,int]: 
		"""
		pass

	@overload
	def IPeriodicHeadFlowsInput(self) -> Dict[int,int]:
		"""Method Description

		Returns:
			Dict[int,int]: 
		"""
		pass

	@overload
	def IPeriodicHeadFlowsInput(self, ids: List[int]) -> Dict[int,int]:
		"""Method Description

		Args:
			ids(List[int]): ids

		Returns:
			Dict[int,int]: 
		"""
		pass

	@overload
	def IPeriodicHeadFlowsInput(self) -> Dict[int,int]:
		"""Method Description

		Returns:
			Dict[int,int]: 
		"""
		pass

	@overload
	def IPeriodicHeadFlowsInput(self, ids: List[int]) -> Dict[int,int]:
		"""Method Description

		Args:
			ids(List[int]): ids

		Returns:
			Dict[int,int]: 
		"""
		pass

	@overload
	def IPeriodicHeadFlowsInput(self) -> Dict[int,int]:
		"""Method Description

		Returns:
			Dict[int,int]: 
		"""
		pass

	@overload
	def IPeriodicHeadFlowsInput(self, ids: List[int]) -> Dict[int,int]:
		"""Method Description

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
		"""Method Description

		Returns:
			Nullable: 
		"""
		pass

	@overload
	def IPeriodicHeadFlowResults(self, timeStepIndex: int) -> Union[float, None]:
		"""Method Description

		Args:
			timeStepIndex(int): timeStepIndex

		Returns:
			Nullable: 
		"""
		pass

	def CalculatedDischarges(self) -> array(Union[float, None]):
		"""Method Description

		Returns:
			Nullable[]: 
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
		"""Method Description

		Returns:
			Dict[int,int]: 
		"""
		pass

	@overload
	def IPeriodicHeadFlowsResults(self, timeStepIndex: int) -> Dict[int,int]:
		"""Method Description

		Args:
			timeStepIndex(int): timeStepIndex

		Returns:
			Dict[int,int]: 
		"""
		pass

	@overload
	def IPeriodicHeadFlowsResults(self, ids: List[int], timeStepIndex: int) -> Dict[int,int]:
		"""Method Description

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
		"""
		Returns:
			IUnit: No Description
		"""
		pass

	@property
	def AngleUnit(self) -> IUnit:
		"""
		Returns:
			IUnit: No Description
		"""
		pass

	@property
	def PeriodUnit(self) -> IUnit:
		"""
		Returns:
			IUnit: No Description
		"""
		pass

	@property
	def FlowUnit(self) -> IUnit:
		"""
		Returns:
			IUnit: No Description
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
		"""
		Returns:
			float: No Description
		"""
		pass

	@property
	def SmallAirOutflowOrificeDiameter(self) -> float:
		"""
		Returns:
			float: No Description
		"""
		pass

	@property
	def TransitionVolume(self) -> float:
		"""
		Returns:
			float: No Description
		"""
		pass

	@property
	def LargeAirOutflowOrificeDiameter(self) -> float:
		"""
		Returns:
			float: No Description
		"""
		pass

	@property
	def AirInflowOrificeDiameter(self) -> float:
		"""
		Returns:
			float: No Description
		"""
		pass

	@property
	def AirOutflowOrificeDiameter(self) -> float:
		"""
		Returns:
			float: No Description
		"""
		pass

	@property
	def TransitionPressure(self) -> float:
		"""
		Returns:
			float: No Description
		"""
		pass

	@property
	def SmallAirFlowCurve(self) -> IAirFlowCurve:
		"""
		Returns:
			IAirFlowCurve: No Description
		"""
		pass

	@property
	def LargeAirFlowCurve(self) -> IAirFlowCurve:
		"""
		Returns:
			IAirFlowCurve: No Description
		"""
		pass

	@property
	def AirValveType(self) -> AirValveTypeEnum:
		"""
		Returns:
			AirValveTypeEnum: No Description
		"""
		pass

	@property
	def AirValveTransitionType(self) -> AirValveTransitionType:
		"""
		Returns:
			AirValveTransitionType: No Description
		"""
		pass

	@property
	def TimeToClose(self) -> float:
		"""
		Returns:
			float: No Description
		"""
		pass

	@property
	def ReportPeriod(self) -> int:
		"""
		Returns:
			int: No Description
		"""
		pass

	@property
	def TreatAirValveAsJunction(self) -> bool:
		"""
		Returns:
			bool: No Description
		"""
		pass

	@property
	def InflowOrificeAirFlowCurve(self) -> IAirFlowCurve:
		"""
		Returns:
			IAirFlowCurve: No Description
		"""
		pass

	@property
	def OutflowOrificeAirFlowCurve(self) -> IAirFlowCurve:
		"""
		Returns:
			IAirFlowCurve: No Description
		"""
		pass

	@property
	def AirFlowCalculationMethod(self) -> AirFlowCalculationMethod:
		"""
		Returns:
			AirFlowCalculationMethod: No Description
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
		"""Method Description

		Returns:
			Dict[int,int]: 
		"""
		pass

	def SmallAirOutflowOrificeDiameters(self) -> Dict[int,int]:
		"""Method Description

		Returns:
			Dict[int,int]: 
		"""
		pass

	def TransitionVolumes(self) -> Dict[int,int]:
		"""Method Description

		Returns:
			Dict[int,int]: 
		"""
		pass

	def LargeAirOutflowOrificeDiameters(self) -> Dict[int,int]:
		"""Method Description

		Returns:
			Dict[int,int]: 
		"""
		pass

	def AirInflowOrificeDiameters(self) -> Dict[int,int]:
		"""Method Description

		Returns:
			Dict[int,int]: 
		"""
		pass

	def AirOutflowOrificeDiameters(self) -> Dict[int,int]:
		"""Method Description

		Returns:
			Dict[int,int]: 
		"""
		pass

	def TransitionPressures(self) -> Dict[int,int]:
		"""Method Description

		Returns:
			Dict[int,int]: 
		"""
		pass

	def SmallAirflowCurves(self) -> Dict[int,int]:
		"""Method Description

		Returns:
			Dict[int,int]: 
		"""
		pass

	def LargeAirFlowCurves(self) -> Dict[int,int]:
		"""Method Description

		Returns:
			Dict[int,int]: 
		"""
		pass

	def AirValveTypes(self) -> Dict[int,int]:
		"""Method Description

		Returns:
			Dict[int,int]: 
		"""
		pass

	def AirValveTransitionTypes(self) -> Dict[int,int]:
		"""Method Description

		Returns:
			Dict[int,int]: 
		"""
		pass

	def TimeToClose(self) -> Dict[int,int]:
		"""Method Description

		Returns:
			Dict[int,int]: 
		"""
		pass

	def ReportPeriods(self) -> Dict[int,int]:
		"""Method Description

		Returns:
			Dict[int,int]: 
		"""
		pass

	def TreatAirValvesAsJunctions(self) -> Dict[int,int]:
		"""Method Description

		Returns:
			Dict[int,int]: 
		"""
		pass

	def InflowOrificeAirFlowCurves(self) -> Dict[int,int]:
		"""Method Description

		Returns:
			Dict[int,int]: 
		"""
		pass

	def OutflowOrificeAirFlowCurves(self) -> Dict[int,int]:
		"""Method Description

		Returns:
			Dict[int,int]: 
		"""
		pass

	def AirFlowCalculationMethods(self) -> Dict[int,int]:
		"""Method Description

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
		"""
		Returns:
			IUnit: No Description
		"""
		pass

	@property
	def DiameterUnit(self) -> IUnit:
		"""
		Returns:
			IUnit: No Description
		"""
		pass

	@property
	def TimeTocloseUnit(self) -> IUnit:
		"""
		Returns:
			IUnit: No Description
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
		"""
		Returns:
			float: No Description
		"""
		pass

	@property
	def SavThresholdPressure(self) -> float:
		"""
		Returns:
			float: No Description
		"""
		pass

	@property
	def TimeForSAVToOpen(self) -> float:
		"""
		Returns:
			float: No Description
		"""
		pass

	@property
	def TimeSAVStaysFullyOpen(self) -> float:
		"""
		Returns:
			float: No Description
		"""
		pass

	@property
	def TimeForSAVToClose(self) -> float:
		"""
		Returns:
			float: No Description
		"""
		pass

	@property
	def SavDischargeCoefficient(self) -> float:
		"""
		Returns:
			float: No Description
		"""
		pass

	@property
	def SrvDiameter(self) -> float:
		"""
		Returns:
			float: No Description
		"""
		pass

	@property
	def SrvThresholdPressure(self) -> float:
		"""
		Returns:
			float: No Description
		"""
		pass

	@property
	def SrvSpringConstant(self) -> float:
		"""
		Returns:
			float: No Description
		"""
		pass

	@property
	def TimeForSRVToOpen(self) -> float:
		"""
		Returns:
			float: No Description
		"""
		pass

	@property
	def TimeForSRVToClose(self) -> float:
		"""
		Returns:
			float: No Description
		"""
		pass

	@property
	def SrvDischargeCoefficient(self) -> float:
		"""
		Returns:
			float: No Description
		"""
		pass

	@property
	def SavSrvType(self) -> SAV_SRVTypeEnum:
		"""
		Returns:
			SAV_SRVTypeEnum: No Description
		"""
		pass

	@property
	def SavType(self) -> SAVValveTypeEnum:
		"""
		Returns:
			SAVValveTypeEnum: No Description
		"""
		pass

	@property
	def SavClosureTriggerType(self) -> SavClosureTriggerEnum:
		"""
		Returns:
			SavClosureTriggerEnum: No Description
		"""
		pass

	@property
	def SrvControlType(self) -> SRVControlTypeEnum:
		"""
		Returns:
			SRVControlTypeEnum: No Description
		"""
		pass

	@property
	def SrvValveType(self) -> SRVValveTypeEnum:
		"""
		Returns:
			SRVValveTypeEnum: No Description
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
		"""Method Description

		Returns:
			Dict[int,int]: 
		"""
		pass

	def SavThresholdPressure(self) -> Dict[int,int]:
		"""Method Description

		Returns:
			Dict[int,int]: 
		"""
		pass

	def TimeForSAVToOpen(self) -> Dict[int,int]:
		"""Method Description

		Returns:
			Dict[int,int]: 
		"""
		pass

	def TimeSAVStaysFullyOpen(self) -> Dict[int,int]:
		"""Method Description

		Returns:
			Dict[int,int]: 
		"""
		pass

	def TimeForSAVToClose(self) -> Dict[int,int]:
		"""Method Description

		Returns:
			Dict[int,int]: 
		"""
		pass

	def SavDischargeCoefficient(self) -> Dict[int,int]:
		"""Method Description

		Returns:
			Dict[int,int]: 
		"""
		pass

	def SrvDiameter(self) -> Dict[int,int]:
		"""Method Description

		Returns:
			Dict[int,int]: 
		"""
		pass

	def SrvThresholdPressure(self) -> Dict[int,int]:
		"""Method Description

		Returns:
			Dict[int,int]: 
		"""
		pass

	def SrvSpringConstant(self) -> Dict[int,int]:
		"""Method Description

		Returns:
			Dict[int,int]: 
		"""
		pass

	def TimeForSRVToOpen(self) -> Dict[int,int]:
		"""Method Description

		Returns:
			Dict[int,int]: 
		"""
		pass

	def TimeForSRVToClose(self) -> Dict[int,int]:
		"""Method Description

		Returns:
			Dict[int,int]: 
		"""
		pass

	def SrvDischargeCoefficient(self) -> Dict[int,int]:
		"""Method Description

		Returns:
			Dict[int,int]: 
		"""
		pass

	def SavSrvType(self) -> Dict[int,int]:
		"""Method Description

		Returns:
			Dict[int,int]: 
		"""
		pass

	def SavType(self) -> Dict[int,int]:
		"""Method Description

		Returns:
			Dict[int,int]: 
		"""
		pass

	def SavClosureTriggerType(self) -> Dict[int,int]:
		"""Method Description

		Returns:
			Dict[int,int]: 
		"""
		pass

	def SrvControlType(self) -> Dict[int,int]:
		"""Method Description

		Returns:
			Dict[int,int]: 
		"""
		pass

	def SRVValveType(self) -> Dict[int,int]:
		"""Method Description

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
		"""
		Returns:
			IUnit: No Description
		"""
		pass

	@property
	def TimeOpenUnit(self) -> IUnit:
		"""
		Returns:
			IUnit: No Description
		"""
		pass

	@property
	def DischargeCoefficient(self) -> IUnit:
		"""
		Returns:
			IUnit: No Description
		"""
		pass

	@property
	def SpringConstantUnit(self) -> IUnit:
		"""
		Returns:
			IUnit: No Description
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
		"""
		Returns:
			float: No Description
		"""
		pass

	@property
	def OrificeFlow(self) -> float:
		"""
		Returns:
			float: No Description
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
		"""Method Description

		Returns:
			Dict[int,int]: 
		"""
		pass

	def OrificeFlow(self) -> Dict[int,int]:
		"""Method Description

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
		"""
		Returns:
			IUnit: No Description
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
		"""Method Description

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
		"""
		Returns:
			float: No Description
		"""
		pass

	@property
	def Flow(self) -> float:
		"""
		Returns:
			float: No Description
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
		"""
		Returns:
			IUnit: No Description
		"""
		pass

	@property
	def FlowUnit(self) -> IUnit:
		"""
		Returns:
			IUnit: No Description
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
		"""
		Returns:
			DischargeToAtmosphereTypeEnum: No Description
		"""
		pass

	@property
	def InitialGaseVolume(self) -> float:
		"""
		Returns:
			float: No Description
		"""
		pass

	@property
	def TimeToStartOperating(self) -> float:
		"""
		Returns:
			float: No Description
		"""
		pass

	@property
	def TimeToFullyOpenOrClose(self) -> float:
		"""
		Returns:
			float: No Description
		"""
		pass

	@property
	def PressureHeadFlowCollection(self) -> IPressureHeadFlowCollection:
		"""
		Returns:
			IPressureHeadFlowCollection: No Description
		"""
		pass

	@property
	def InitialStatus(self) -> ValveTypeInitialStatusEnum:
		"""
		Returns:
			ValveTypeInitialStatusEnum: No Description
		"""
		pass

	@property
	def ReportPeriod(self) -> int:
		"""
		Returns:
			int: No Description
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
		"""Method Description

		Returns:
			Dict[int,int]: 
		"""
		pass

	def InitialGasVolume(self) -> Dict[int,int]:
		"""Method Description

		Returns:
			Dict[int,int]: 
		"""
		pass

	def TimeToStartOpening(self) -> Dict[int,int]:
		"""Method Description

		Returns:
			Dict[int,int]: 
		"""
		pass

	def TimeToFullyOpenOrClose(self) -> Dict[int,int]:
		"""Method Description

		Returns:
			Dict[int,int]: 
		"""
		pass

	def InitialStatus(self) -> Dict[int,int]:
		"""Method Description

		Returns:
			Dict[int,int]: 
		"""
		pass

	def ReportPeriod(self) -> Dict[int,int]:
		"""Method Description

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
		"""Method Description

		Returns:
			Nullable: 
		"""
		pass

	@overload
	def IDischargeToAtmosphereNodeResults(self, timeStepIndex: int) -> Union[float, None]:
		"""Method Description

		Args:
			timeStepIndex(int): timeStepIndex

		Returns:
			Nullable: 
		"""
		pass

	def CalculatedDischarges(self) -> array(Union[float, None]):
		"""Method Description

		Returns:
			Nullable[]: 
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
		"""Method Description

		Returns:
			Dict[int,int]: 
		"""
		pass

	@overload
	def IDischargeToAtmosphereNodesResults(self, timeStepIndex: int) -> Dict[int,int]:
		"""Method Description

		Args:
			timeStepIndex(int): timeStepIndex

		Returns:
			Dict[int,int]: 
		"""
		pass

	@overload
	def IDischargeToAtmosphereNodesResults(self, ids: List[int], timeStepIndex: int) -> Dict[int,int]:
		"""Method Description

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
		"""
		Returns:
			IUnit: No Description
		"""
		pass

	@property
	def TimeUnit(self) -> IUnit:
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
		"""
		Returns:
			float: No Description
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
		"""Method Description

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
		"""Method Description

		Returns:
			Dict[int,int]: 
		"""
		pass

	@overload
	def IBaseNodesResults(self, timeStepIndex: int) -> Dict[int,int]:
		"""Method Description

		Args:
			timeStepIndex(int): timeStepIndex

		Returns:
			Dict[int,int]: 
		"""
		pass

	@overload
	def IBaseNodesResults(self, ids: List[int], timeStepIndex: int) -> Dict[int,int]:
		"""Method Description

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
		"""
		Returns:
			float: No Description
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
		"""Method Description

		Returns:
			Dict[int,int]: 
		"""
		pass

	@overload
	def IPhysicalNodeElementsInput(self, ids: List[int]) -> Dict[int,int]:
		"""Method Description

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
		"""Method Description

		Returns:
			Nullable: 
		"""
		pass

	@overload
	def IBaseNodeResults(self, timeStepIndex: int) -> Union[float, None]:
		"""Method Description

		Args:
			timeStepIndex(int): timeStepIndex

		Returns:
			Nullable: 
		"""
		pass

	def HydraulicGrades(self) -> array(Union[float, None]):
		"""Method Description

		Returns:
			Nullable[]: 
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
		"""
		Returns:
			IUnit: No Description
		"""
		pass

	@property
	def InitialAgeUnit(self) -> IUnit:
		"""
		Returns:
			IUnit: No Description
		"""
		pass

	@property
	def InitialConcentrationUnit(self) -> IUnit:
		"""
		Returns:
			IUnit: No Description
		"""
		pass

	@property
	def InitialTraceUnit(self) -> IUnit:
		"""
		Returns:
			IUnit: No Description
		"""
		pass

	@property
	def BaseConcentrationUnit(self) -> IUnit:
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
		"""Method Description

		Returns:
			Dict[int,int]: 
		"""
		pass

	@overload
	def IReservoirsResults(self, timeStepIndex: int) -> Dict[int,int]:
		"""Method Description

		Args:
			timeStepIndex(int): timeStepIndex

		Returns:
			Dict[int,int]: 
		"""
		pass

	@overload
	def IReservoirsResults(self, ids: List[int], timeStepIndex: int) -> Dict[int,int]:
		"""Method Description

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
		"""Method Description

		Returns:
			Nullable: 
		"""
		pass

	@overload
	def IReservoirResults(self, timeStepIndex: int) -> Union[float, None]:
		"""Method Description

		Args:
			timeStepIndex(int): timeStepIndex

		Returns:
			Nullable: 
		"""
		pass

	def Flows(self) -> array(Union[float, None]):
		"""Method Description

		Returns:
			Nullable[]: 
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
		"""
		Returns:
			IUnit: No Description
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
		"""
		Returns:
			IPipe: No Description
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
		"""Method Description

		Returns:
			Dict[int,int]: 
		"""
		pass

	@overload
	def ITapsInput(self, ids: List[int]) -> Dict[int,int]:
		"""Method Description

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
		"""
		Returns:
			IPipe: No Description
		"""
		pass

	@property
	def ValveDiameter(self) -> float:
		"""
		Returns:
			float: No Description
		"""
		pass

	@property
	def MinorLossCoefficient(self) -> float:
		"""
		Returns:
			float: No Description
		"""
		pass

	@property
	def IsOperable(self) -> bool:
		"""
		Returns:
			bool: No Description
		"""
		pass

	@property
	def InitialStatus(self) -> IsolationValveInitialSetting:
		"""
		Returns:
			IsolationValveInitialSetting: No Description
		"""
		pass

	@property
	def InstallationYear(self) -> int:
		"""
		Returns:
			int: No Description
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
		"""Method Description

		Returns:
			Dict[int,int]: 
		"""
		pass

	@overload
	def IIsolationValveElementsInput(self, ids: List[int]) -> Dict[int,int]:
		"""Method Description

		Args:
			ids(List[int]): ids

		Returns:
			Dict[int,int]: 
		"""
		pass

	@overload
	def IIsolationValveElementsInput(self) -> Dict[int,int]:
		"""Method Description

		Returns:
			Dict[int,int]: 
		"""
		pass

	@overload
	def IIsolationValveElementsInput(self, ids: List[int]) -> Dict[int,int]:
		"""Method Description

		Args:
			ids(List[int]): ids

		Returns:
			Dict[int,int]: 
		"""
		pass

	@overload
	def IIsolationValveElementsInput(self) -> Dict[int,int]:
		"""Method Description

		Returns:
			Dict[int,int]: 
		"""
		pass

	@overload
	def IIsolationValveElementsInput(self, ids: List[int]) -> Dict[int,int]:
		"""Method Description

		Args:
			ids(List[int]): ids

		Returns:
			Dict[int,int]: 
		"""
		pass

	@overload
	def IIsolationValveElementsInput(self) -> Dict[int,int]:
		"""Method Description

		Returns:
			Dict[int,int]: 
		"""
		pass

	@overload
	def IIsolationValveElementsInput(self, ids: List[int]) -> Dict[int,int]:
		"""Method Description

		Args:
			ids(List[int]): ids

		Returns:
			Dict[int,int]: 
		"""
		pass

	@overload
	def IIsolationValveElementsInput(self) -> Dict[int,int]:
		"""Method Description

		Returns:
			Dict[int,int]: 
		"""
		pass

	@overload
	def IIsolationValveElementsInput(self, ids: List[int]) -> Dict[int,int]:
		"""Method Description

		Args:
			ids(List[int]): ids

		Returns:
			Dict[int,int]: 
		"""
		pass

	@overload
	def IIsolationValveElementsInput(self) -> Dict[int,int]:
		"""Method Description

		Returns:
			Dict[int,int]: 
		"""
		pass

	@overload
	def IIsolationValveElementsInput(self, ids: List[int]) -> Dict[int,int]:
		"""Method Description

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
		"""Method Description

		Returns:
			Nullable: 
		"""
		pass

	@overload
	def IIsolatioNValveElementResults(self, timeStepIndex: int) -> Union[float, None]:
		"""Method Description

		Args:
			timeStepIndex(int): timeStepIndex

		Returns:
			Nullable: 
		"""
		pass

	@overload
	def IIsolatioNValveElementResults(self) -> Union[float, None]:
		"""Method Description

		Returns:
			Nullable: 
		"""
		pass

	@overload
	def IIsolatioNValveElementResults(self, timeStepIndex: int) -> Union[float, None]:
		"""Method Description

		Args:
			timeStepIndex(int): timeStepIndex

		Returns:
			Nullable: 
		"""
		pass

	@overload
	def IIsolatioNValveElementResults(self) -> Union[float, None]:
		"""Method Description

		Returns:
			Nullable: 
		"""
		pass

	@overload
	def IIsolatioNValveElementResults(self, timeStepIndex: int) -> Union[float, None]:
		"""Method Description

		Args:
			timeStepIndex(int): timeStepIndex

		Returns:
			Nullable: 
		"""
		pass

	@overload
	def IIsolatioNValveElementResults(self) -> Union[float, None]:
		"""Method Description

		Returns:
			Nullable: 
		"""
		pass

	@overload
	def IIsolatioNValveElementResults(self, timeStepIndex: int) -> Union[float, None]:
		"""Method Description

		Args:
			timeStepIndex(int): timeStepIndex

		Returns:
			Nullable: 
		"""
		pass

	@overload
	def IIsolatioNValveElementResults(self) -> Union[bool, None]:
		"""Method Description

		Returns:
			Nullable: 
		"""
		pass

	@overload
	def IIsolatioNValveElementResults(self, timeStepIndex: int) -> Union[bool, None]:
		"""Method Description

		Args:
			timeStepIndex(int): timeStepIndex

		Returns:
			Nullable: 
		"""
		pass

	def HydraulicGrades(self) -> array(Union[float, None]):
		"""Method Description

		Returns:
			Nullable[]: 
		"""
		pass

	def Pressures(self) -> array(Union[float, None]):
		"""Method Description

		Returns:
			Nullable[]: 
		"""
		pass

	def Flows(self) -> array(Union[float, None]):
		"""Method Description

		Returns:
			Nullable[]: 
		"""
		pass

	def Velocities(self) -> array(Union[float, None]):
		"""Method Description

		Returns:
			Nullable[]: 
		"""
		pass

	def DistanceFromEndPoint(self) -> Union[float, None]:
		"""Method Description

		Returns:
			Nullable: 
		"""
		pass

	def IsCloseds(self) -> array(Union[bool, None]):
		"""Method Description

		Returns:
			Nullable[]: 
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
		"""Method Description

		Returns:
			Dict[int,int]: 
		"""
		pass

	@overload
	def IIsolationValveElementsResults(self, timeStepIndex: int) -> Dict[int,int]:
		"""Method Description

		Args:
			timeStepIndex(int): timeStepIndex

		Returns:
			Dict[int,int]: 
		"""
		pass

	@overload
	def IIsolationValveElementsResults(self, ids: List[int], timeStepIndex: int) -> Dict[int,int]:
		"""Method Description

		Args:
			ids(List[int]): ids
			timeStepIndex(int): timeStepIndex

		Returns:
			Dict[int,int]: 
		"""
		pass

	@overload
	def IIsolationValveElementsResults(self) -> Dict[int,int]:
		"""Method Description

		Returns:
			Dict[int,int]: 
		"""
		pass

	@overload
	def IIsolationValveElementsResults(self, timeStepIndex: int) -> Dict[int,int]:
		"""Method Description

		Args:
			timeStepIndex(int): timeStepIndex

		Returns:
			Dict[int,int]: 
		"""
		pass

	@overload
	def IIsolationValveElementsResults(self, ids: List[int], timeStepIndex: int) -> Dict[int,int]:
		"""Method Description

		Args:
			ids(List[int]): ids
			timeStepIndex(int): timeStepIndex

		Returns:
			Dict[int,int]: 
		"""
		pass

	@overload
	def IIsolationValveElementsResults(self) -> Dict[int,int]:
		"""Method Description

		Returns:
			Dict[int,int]: 
		"""
		pass

	@overload
	def IIsolationValveElementsResults(self, timeStepIndex: int) -> Dict[int,int]:
		"""Method Description

		Args:
			timeStepIndex(int): timeStepIndex

		Returns:
			Dict[int,int]: 
		"""
		pass

	@overload
	def IIsolationValveElementsResults(self, ids: List[int], timeStepIndex: int) -> Dict[int,int]:
		"""Method Description

		Args:
			ids(List[int]): ids
			timeStepIndex(int): timeStepIndex

		Returns:
			Dict[int,int]: 
		"""
		pass

	@overload
	def IIsolationValveElementsResults(self) -> Dict[int,int]:
		"""Method Description

		Returns:
			Dict[int,int]: 
		"""
		pass

	@overload
	def IIsolationValveElementsResults(self, timeStepIndex: int) -> Dict[int,int]:
		"""Method Description

		Args:
			timeStepIndex(int): timeStepIndex

		Returns:
			Dict[int,int]: 
		"""
		pass

	@overload
	def IIsolationValveElementsResults(self, ids: List[int], timeStepIndex: int) -> Dict[int,int]:
		"""Method Description

		Args:
			ids(List[int]): ids
			timeStepIndex(int): timeStepIndex

		Returns:
			Dict[int,int]: 
		"""
		pass

	@overload
	def IIsolationValveElementsResults(self) -> Dict[int,int]:
		"""Method Description

		Returns:
			Dict[int,int]: 
		"""
		pass

	@overload
	def IIsolationValveElementsResults(self, ids: List[int]) -> Dict[int,int]:
		"""Method Description

		Args:
			ids(List[int]): ids

		Returns:
			Dict[int,int]: 
		"""
		pass

	@overload
	def IIsolationValveElementsResults(self) -> Dict[int,int]:
		"""Method Description

		Returns:
			Dict[int,int]: 
		"""
		pass

	@overload
	def IIsolationValveElementsResults(self, timeStepIndex: int) -> Dict[int,int]:
		"""Method Description

		Args:
			timeStepIndex(int): timeStepIndex

		Returns:
			Dict[int,int]: 
		"""
		pass

	@overload
	def IIsolationValveElementsResults(self, ids: List[int], timeStepIndex: int) -> Dict[int,int]:
		"""Method Description

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
		"""
		Returns:
			IUnit: No Description
		"""
		pass

	@property
	def CoefficientUnit(self) -> IUnit:
		"""
		Returns:
			IUnit: No Description
		"""
		pass

	@property
	def ElevationUnit(self) -> IUnit:
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
	def FlowUnit(self) -> IUnit:
		"""
		Returns:
			IUnit: No Description
		"""
		pass

	@property
	def VelocityUnit(self) -> IUnit:
		"""
		Returns:
			IUnit: No Description
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
		"""
		Returns:
			float: No Description
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
		"""Method Description

		Returns:
			Dict[int,int]: 
		"""
		pass

	@overload
	def ISpotElevationsInput(self, ids: List[int]) -> Dict[int,int]:
		"""Method Description

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
		"""Method Description

		Returns:
			Nullable: 
		"""
		pass

	@overload
	def ISpotElevationResults(self, timeStepIndex: int) -> Union[float, None]:
		"""Method Description

		Args:
			timeStepIndex(int): timeStepIndex

		Returns:
			Nullable: 
		"""
		pass

	@overload
	def ISpotElevationResults(self) -> Union[float, None]:
		"""Method Description

		Returns:
			Nullable: 
		"""
		pass

	@overload
	def ISpotElevationResults(self, timeStepIndex: int) -> Union[float, None]:
		"""Method Description

		Args:
			timeStepIndex(int): timeStepIndex

		Returns:
			Nullable: 
		"""
		pass

	def EnhancedHydraulicGrades(self) -> array(Union[float, None]):
		"""Method Description

		Returns:
			Nullable[]: 
		"""
		pass

	def EnhancedPressures(self) -> array(Union[float, None]):
		"""Method Description

		Returns:
			Nullable[]: 
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
		"""Method Description

		Returns:
			Dict[int,int]: 
		"""
		pass

	@overload
	def ISpotElevationsResults(self, timeStepIndex: int) -> Dict[int,int]:
		"""Method Description

		Args:
			timeStepIndex(int): timeStepIndex

		Returns:
			Dict[int,int]: 
		"""
		pass

	@overload
	def ISpotElevationsResults(self, ids: List[int], timeStepIndex: int) -> Dict[int,int]:
		"""Method Description

		Args:
			ids(List[int]): ids
			timeStepIndex(int): timeStepIndex

		Returns:
			Dict[int,int]: 
		"""
		pass

	@overload
	def ISpotElevationsResults(self) -> Dict[int,int]:
		"""Method Description

		Returns:
			Dict[int,int]: 
		"""
		pass

	@overload
	def ISpotElevationsResults(self, timeStepIndex: int) -> Dict[int,int]:
		"""Method Description

		Args:
			timeStepIndex(int): timeStepIndex

		Returns:
			Dict[int,int]: 
		"""
		pass

	@overload
	def ISpotElevationsResults(self, ids: List[int], timeStepIndex: int) -> Dict[int,int]:
		"""Method Description

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
		"""
		Returns:
			IPattern: No Description
		"""
		pass

	@property
	def BaseDemand(self) -> float:
		"""
		Returns:
			float: No Description
		"""
		pass

	@property
	def StartDemandDistribution(self) -> float:
		"""
		Returns:
			float: No Description
		"""
		pass

	@property
	def AssociatedElement(self) -> IWaterNetworkElement:
		"""
		Returns:
			IWaterNetworkElement: No Description
		"""
		pass

	@property
	def UnitDemand(self) -> IUnitDemandLoad:
		"""
		Returns:
			IUnitDemandLoad: No Description
		"""
		pass

	@property
	def UnitDemandPattern(self) -> IPattern:
		"""
		Returns:
			IPattern: No Description
		"""
		pass

	@property
	def NumberOfUnitDemands(self) -> float:
		"""
		Returns:
			float: No Description
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
	def AssociatedElement(self, associatedelement: IWaterNetworkElement) -> None:
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
		"""Method Description

		Returns:
			Dict[int,int]: 
		"""
		pass

	@overload
	def ICustomerMetersInput(self, ids: List[int]) -> Dict[int,int]:
		"""Method Description

		Args:
			ids(List[int]): ids

		Returns:
			Dict[int,int]: 
		"""
		pass

	@overload
	def ICustomerMetersInput(self) -> Dict[int,int]:
		"""Method Description

		Returns:
			Dict[int,int]: 
		"""
		pass

	@overload
	def ICustomerMetersInput(self, ids: List[int]) -> Dict[int,int]:
		"""Method Description

		Args:
			ids(List[int]): ids

		Returns:
			Dict[int,int]: 
		"""
		pass

	@overload
	def ICustomerMetersInput(self) -> Dict[int,int]:
		"""Method Description

		Returns:
			Dict[int,int]: 
		"""
		pass

	@overload
	def ICustomerMetersInput(self, ids: List[int]) -> Dict[int,int]:
		"""Method Description

		Args:
			ids(List[int]): ids

		Returns:
			Dict[int,int]: 
		"""
		pass

	@overload
	def ICustomerMetersInput(self) -> Dict[int,int]:
		"""Method Description

		Returns:
			Dict[int,int]: 
		"""
		pass

	@overload
	def ICustomerMetersInput(self, ids: List[int]) -> Dict[int,int]:
		"""Method Description

		Args:
			ids(List[int]): ids

		Returns:
			Dict[int,int]: 
		"""
		pass

	@overload
	def ICustomerMetersInput(self) -> Dict[int,int]:
		"""Method Description

		Returns:
			Dict[int,int]: 
		"""
		pass

	@overload
	def ICustomerMetersInput(self, ids: List[int]) -> Dict[int,int]:
		"""Method Description

		Args:
			ids(List[int]): ids

		Returns:
			Dict[int,int]: 
		"""
		pass

	@overload
	def ICustomerMetersInput(self) -> Dict[int,int]:
		"""Method Description

		Returns:
			Dict[int,int]: 
		"""
		pass

	@overload
	def ICustomerMetersInput(self, ids: List[int]) -> Dict[int,int]:
		"""Method Description

		Args:
			ids(List[int]): ids

		Returns:
			Dict[int,int]: 
		"""
		pass

	@overload
	def ICustomerMetersInput(self) -> Dict[int,int]:
		"""Method Description

		Returns:
			Dict[int,int]: 
		"""
		pass

	@overload
	def ICustomerMetersInput(self, ids: List[int]) -> Dict[int,int]:
		"""Method Description

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
		"""Method Description

		Returns:
			Nullable: 
		"""
		pass

	@overload
	def ICustomerMeterResults(self, timeStepIndex: int) -> Union[float, None]:
		"""Method Description

		Args:
			timeStepIndex(int): timeStepIndex

		Returns:
			Nullable: 
		"""
		pass

	@overload
	def ICustomerMeterResults(self) -> Union[float, None]:
		"""Method Description

		Returns:
			Nullable: 
		"""
		pass

	@overload
	def ICustomerMeterResults(self, timeStepIndex: int) -> Union[float, None]:
		"""Method Description

		Args:
			timeStepIndex(int): timeStepIndex

		Returns:
			Nullable: 
		"""
		pass

	def HydraulicGrades(self) -> array(Union[float, None]):
		"""Method Description

		Returns:
			Nullable[]: 
		"""
		pass

	def Pressures(self) -> array(Union[float, None]):
		"""Method Description

		Returns:
			Nullable[]: 
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
		"""Method Description

		Returns:
			Dict[int,int]: 
		"""
		pass

	@overload
	def ICustomerMetersResults(self, timeStepIndex: int) -> Dict[int,int]:
		"""Method Description

		Args:
			timeStepIndex(int): timeStepIndex

		Returns:
			Dict[int,int]: 
		"""
		pass

	@overload
	def ICustomerMetersResults(self, ids: List[int], timeStepIndex: int) -> Dict[int,int]:
		"""Method Description

		Args:
			ids(List[int]): ids
			timeStepIndex(int): timeStepIndex

		Returns:
			Dict[int,int]: 
		"""
		pass

	@overload
	def ICustomerMetersResults(self) -> Dict[int,int]:
		"""Method Description

		Returns:
			Dict[int,int]: 
		"""
		pass

	@overload
	def ICustomerMetersResults(self, timeStepIndex: int) -> Dict[int,int]:
		"""Method Description

		Args:
			timeStepIndex(int): timeStepIndex

		Returns:
			Dict[int,int]: 
		"""
		pass

	@overload
	def ICustomerMetersResults(self, ids: List[int], timeStepIndex: int) -> Dict[int,int]:
		"""Method Description

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
	def TargetElement(self) -> IWaterNetworkElement:
		"""
		Returns:
			IWaterNetworkElement: No Description
		"""
		pass

	@property
	def RealtimeSignal(self) -> ISCADASignal:
		"""
		Returns:
			ISCADASignal: No Description
		"""
		pass

	@property
	def HistoricalSignal(self) -> ISCADASignal:
		"""
		Returns:
			ISCADASignal: No Description
		"""
		pass

	@property
	def TargetAttribute(self) -> SCADATargetAttribute:
		"""
		Returns:
			SCADATargetAttribute: No Description
		"""
		pass

	@TargetElement.setter
	def TargetElement(self, targetelement: IWaterNetworkElement) -> None:
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
		"""Method Description

		Returns:
			Dict[int,int]: 
		"""
		pass

	@overload
	def ISCADAElementsInput(self, ids: List[int]) -> Dict[int,int]:
		"""Method Description

		Args:
			ids(List[int]): ids

		Returns:
			Dict[int,int]: 
		"""
		pass

	@overload
	def ISCADAElementsInput(self) -> Dict[int,int]:
		"""Method Description

		Returns:
			Dict[int,int]: 
		"""
		pass

	@overload
	def ISCADAElementsInput(self, ids: List[int]) -> Dict[int,int]:
		"""Method Description

		Args:
			ids(List[int]): ids

		Returns:
			Dict[int,int]: 
		"""
		pass

	@overload
	def ISCADAElementsInput(self) -> Dict[int,int]:
		"""Method Description

		Returns:
			Dict[int,int]: 
		"""
		pass

	@overload
	def ISCADAElementsInput(self, ids: List[int]) -> Dict[int,int]:
		"""Method Description

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
		"""
		Returns:
			IPumpStationPumpIDsCollection: No Description
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
		"""Method Description

		Args:
			pump(IPump): pump
			pumpDefinition(IPumpDefinition): pumpDefinition

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
		"""
		Returns:
			IElement: No Description
		"""
		pass

	@property
	def PumpDefinition(self) -> IPumpDefinition:
		"""
		Returns:
			IPumpDefinition: No Description
		"""
		pass

	@Pump.setter
	def Pump(self, pump: IElement) -> None:
		pass

	@PumpDefinition.setter
	def PumpDefinition(self, pumpdefinition: IPumpDefinition) -> None:
		pass

