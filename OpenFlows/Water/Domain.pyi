from OpenFlows.Water.Units import INetworkElementUnits, IComponentElementUnits
from OpenFlows.Domain.DataObjects import IModelElementManager, IModelIOOperations, IDomainModel
from OpenFlows.Domain.DataObjects import IModel
from OpenFlows.Water.Domain.ModelingElements.NetworkElements import IWaterNetwork, IWaterNetworkElement
from OpenFlows.Water.Domain.ModelingElements.Components import IWaterModelSupport, IWaterComponent
from OpenFlows.Water.Domain.ModelingElements import IWaterScenario, IWaterScenarios, IWaterSelectionSet, IWaterSelectionSets
from OpenFlows.Water.Domain.ModelingElements.CalculationOptions import IWaterScenarioOptions, IWaterScenarioOptionsUnits
from OpenFlows.Units import IModelUnits
from OpenFlows.Domain.DataObjects import IModelScenarioManagement, IModelSelectionSetManagement
from OpenFlows.Water.Analysis import IAnalysisTools

class IWaterModel(IModel[IWaterNetwork, IWaterModelSupport, IWaterScenarios, IWaterScenario, IWaterScenarioOptions, IWaterScenarioOptionsUnits, 
	IWaterSelectionSets, IWaterSelectionSet, IWaterNetworkElement, IWaterNetworkElement, WaterNetworkElementType, IWaterComponent, WaterComponentType, 
	INetworkElementUnits, IComponentElementUnits], IDisposable, IModelElementManager, IModelIOOperations, 
	IModelUnits[INetworkElementUnits, IComponentElementUnits], IModelScenarioManagement[IWaterScenarios, IWaterScenario], IDomainModel, 
	IModelSelectionSetManagement[IWaterSelectionSets, IWaterSelectionSet, IWaterNetworkElement]):

	def __init__(self) -> None:
		"""Creating a new Instance of this class is not allowed


		Raises:
			Exception: if this class is instanciated
		"""
		raise Exception("Creating a new Instance of this class is not allowed")
		pass

	@property
	def AnalysisTools(self) -> IAnalysisTools:
		"""
		Returns:
			IAnalysisTools: No Description
		"""
		pass

