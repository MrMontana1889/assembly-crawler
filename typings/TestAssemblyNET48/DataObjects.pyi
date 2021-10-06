from NetworkElements import INetwork

class IWaterModel:
    @property
    def Network(self) -> INetwork:
        pass