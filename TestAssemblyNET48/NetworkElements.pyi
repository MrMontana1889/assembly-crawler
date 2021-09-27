from typing import List 
from Support import GeometryPoint
from ModelingObjects import IElement, IElementInput

class IActiveElementInput(IElementInput):
    @property
    def IsActive(self) -> bool:
        """ Set active state of element """
        pass

    @IsActive.setter
    def IsActive(self, b: bool) -> None:
        pass

class IBaseLinkInput(IActiveElementInput):
    """ Base link properties """

    @property
    def StartNode(self) -> IElement:
        pass
    @StartNode.setter
    def StartNode(self, sn: IElement) -> None:
        pass

    @property
    def StopNode(self) -> IElement:
        pass
    @StopNode.setter
    def StopNode(self, sn: IElement) -> None:
        pass

    @property
    def IsUserDefinedLength(self) -> bool:
        pass
    @IsUserDefinedLength.setter
    def IsUserDefinedLength(self, b: bool) -> None:
        pass

    @property
    def Length(self) -> float:
        pass
    @Length.setter
    def Length(self, l: float) -> None:
        pass

    def SetPoints(self, p: List[GeometryPoint]) -> None:
        pass
    def GetPoints(self) -> List[GeometryPoint]:
        pass

class IPipeInput(IBaseLinkInput, IActiveElementInput, IElementInput):
    
    @property
    def Diameter(self) -> float:
        pass
    @Diameter.setter
    def Diameter(self, d: float) -> None:
        pass

class IPipe(IElement):
    
    @property
    def Input(self) -> IPipeInput:
        pass

class IPipes:

    def Create(self) -> IPipe:
        pass

    def Element(self, param1: object) -> IPipe:
        """
        param1: Use an integer to retrieve a pipe by id
        param1: Use a string to query the pipes mangaer by label
        """
        pass

    @property
    def Count(self) -> int:
        pass

class INetwork:

    @property
    def Pipes(self) -> IPipes:
        pass
