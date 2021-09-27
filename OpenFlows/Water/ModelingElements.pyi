from OpenFlows.Water.NetworkElements import IWaterNetworkElement
from OpenFlows.ModelingElements import IScenario, IScenarios, ISelectionSets, ISelectionSet
from OpenFlows.Water.CalculationOptions import IWaterScenarioOptions, IWaterScenarioOptionsUnits

class IWaterScenarios(IScenarios[IWaterScenarios, IWaterScenario, IWaterScenarioOptions, IWaterScenarioOptionsUnits]):
    pass

class IWaterScenario(IScenario[IWaterScenarios, IWaterScenario, IWaterScenarioOptions, IWaterScenarioOptionsUnits]):
    pass

class IWaterSelectionSets(ISelectionSets[IWaterSelectionSets, IWaterSelectionSet, IWaterNetworkElement]):
    pass

class IWaterSelectionSet(ISelectionSet[IWaterSelectionSets, IWaterSelectionSet, IWaterNetworkElement]):
    pass