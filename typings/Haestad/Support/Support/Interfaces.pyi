class ILabeled:
    @property
    def Label(self) -> str:
        pass

class IEditLabeled(ILabeled):
    @Label.setter
    def Label(self, label: str) -> None:
        pass

class INamable:
    @property
    def Name(self) -> str:
        pass