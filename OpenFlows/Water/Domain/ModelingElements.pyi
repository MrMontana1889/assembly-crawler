from typing import Generic
from OpenFlows.Domain.ModelingElements import IElement, IElementManager

class IWaterScenario(IScenario[IWaterScenarios, IWaterScenario, IWaterScenarioOptions, IWaterScenarioOptionsUnits], IModelingElementBase[IWaterScenarios, IWaterScenario, ModelingElementTypes], IElement, IEditLabeled, ILabeled):

	def __init__(self) -> None:
		"""Creating a new Instance of this class is not allowed


		Raises:
			Exception: if this class is instanciated
		"""
		raise Exception("Creating a new Instance of this class is not allowed")
		pass

class IWaterScenarios(IScenarios[IWaterScenarios, IWaterScenario, IWaterScenarioOptions, IWaterScenarioOptionsUnits], IModelingElementsBase[IWaterScenarios, IWaterScenario, ModelingElementTypes], IElements[IWaterScenario], IElementManager):

	def __init__(self) -> None:
		"""Creating a new Instance of this class is not allowed


		Raises:
			Exception: if this class is instanciated
		"""
		raise Exception("Creating a new Instance of this class is not allowed")
		pass

class IWaterSelectionSet(ISelectionSet[IWaterSelectionSets, IWaterSelectionSet, IWaterNetworkElement], IModelingElementBase[IWaterSelectionSets, IWaterSelectionSet, ModelingElementTypes], IElement, IEditLabeled, ILabeled):

	def __init__(self) -> None:
		"""Creating a new Instance of this class is not allowed


		Raises:
			Exception: if this class is instanciated
		"""
		raise Exception("Creating a new Instance of this class is not allowed")
		pass

class IWaterSelectionSets(ISelectionSets[IWaterSelectionSets, IWaterSelectionSet, IWaterNetworkElement], IModelingElementsBase[IWaterSelectionSets, IWaterSelectionSet, ModelingElementTypes], IElements[IWaterSelectionSet], IElementManager):

	def __init__(self) -> None:
		"""Creating a new Instance of this class is not allowed


		Raises:
			Exception: if this class is instanciated
		"""
		raise Exception("Creating a new Instance of this class is not allowed")
		pass

