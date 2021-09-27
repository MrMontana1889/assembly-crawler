from OpenFlows.Water.NetworkElements import IWaterNetworkElement, WaterNetworkElementType
from OpenFlows.Water.ModelingElements import IWaterScenarios, IWaterScenario, IWaterSelectionSets, IWaterSelectionSet
from OpenFlows.Water.CalculationOptions import IWaterScenarioOptions, IWaterScenarioOptionsUnits
from OpenFlows.Interfaces import IModel
from NetworkElements import IWaterNetwork
from OpenFlows.Water.Components import IWaterModelSupport, IWaterComponent, WaterComponentType
from OpenFlows.Water.Units import INetworkElementUnits, IComponentElementUnits

class IWaterModel(IModel[IWaterNetwork, IWaterModelSupport, IWaterScenarios, IWaterScenario, IWaterScenarioOptions,
    IWaterScenarioOptionsUnits, IWaterSelectionSets, IWaterSelectionSet, IWaterNetworkElement, IWaterNetworkElement, WaterNetworkElementType,
    IWaterComponent, WaterComponentType, INetworkElementUnits, IComponentElementUnits]):
    pass
