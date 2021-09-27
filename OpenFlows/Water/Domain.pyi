from NetworkElements import IWaterNetwork

class IWaterModel:
    @property
    def Network(self) -> IWaterNetwork:
        pass