from OpenFlows.Domain.DataObjects import IModel
from OpenFlows.Water.Units import INetworkElementUnits, IComponentElementUnits
from OpenFlows.Water.Enumerations import *
from OpenFlows.Water.Domain.ModelingElements.NetworkElements import IWaterNetwork, IWaterElement
from OpenFlows.Water.Domain.ModelingElements.Components import IWaterModelSupport, IWaterComponent
from OpenFlows.Water.Domain.ModelingElements import IWaterScenarios, IWaterScenario, IWaterSelectionSets, IWaterSelectionSet
from OpenFlows.Water.Domain.ModelingElements.CalculationOptions import IWaterScenarioOptions, IWaterScenarioOptionsUnits
from OpenFlows.Water.Analysis import IAnalysisTools

class IWaterModel(IModel[IWaterNetwork, IWaterModelSupport, IWaterScenarios, IWaterScenario, IWaterScenarioOptions, IWaterScenarioOptionsUnits, IWaterSelectionSets, IWaterSelectionSet, IWaterElement, IWaterElement, WaterNetworkElementType, IWaterComponent, WaterComponentType, INetworkElementUnits, IComponentElementUnits]):

	def __init__(self) -> None:
		"""Creating a new Instance of this class is not allowed


		Raises:
			Exception: if this class is instanciated
		"""
		raise Exception("Creating a new Instance of this class is not allowed")
		pass

	@property
	def AnalysisTools(self) -> IAnalysisTools:
		"""No Description

		Returns:
			IWaterModel: 
		"""
		pass

