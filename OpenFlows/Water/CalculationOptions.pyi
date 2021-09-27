from datetime import datetime
from OpenFlows.ModelingElements import IScenarioOptions, IElementUnits
from OpenFlows.Units import IUnit

class IWaterScenarioOptionsUnits(IElementUnits):
    @property
    def DurationUnit(self) -> IUnit:
        pass

    @property
    def HydraulicTimeStepUnit(self) -> IUnit:
        pass

class IWaterScenarioOptions(IScenarioOptions[IWaterScenarioOptionsUnits]):
    # CalculationType

    # FrictionMethod

    @property
    def SimulationStartDate(self) -> datetime:
        pass
    @SimulationStartDate.setter
    def SimulationStartDate(self, d: datetime) -> None:
        pass

    # TimeAnalysisType

    @property
    def StartTime(self) -> datetime:
        pass
    @StartTime.setter
    def StartTime(self, d: datetime) -> None:
        pass

    @property
    def Duration(self) -> float:
        pass
    @Duration.setter
    def Duration(self, d: float) -> None:
        pass

    # There's lots more