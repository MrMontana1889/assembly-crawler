from enum import Enum
from OpenFlows.Domain.DataObjects import IModelAlternatives
from OpenFlows.Water.Domain.ModelingElements.NetworkElements import WaterNetworkElementType
from OpenFlows.Water.Units import INetworkElementUnits, IComponentElementUnits

class WaterAlternativeType(Enum):
	Physical = 4

class IWaterAlternatives(IModelAlternatives[WaterNetworkElementType, WaterAlternativeType, INetworkElementUnits, IComponentElementUnits]):

	def __init__(self) -> None:
		"""Creating a new Instance of this class is not allowed


		Raises
		--------
			Exception: if this class is instantiated
		"""
		raise Exception("Creating a new Instance of this class is not allowed")
		pass

