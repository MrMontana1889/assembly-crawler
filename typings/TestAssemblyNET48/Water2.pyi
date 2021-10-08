# encoding: utf-8
# module TestAssemblyNET48.Water calls itself Water
# from TestAssemblyNET48, Version=1.0.0.0, Culture=neutral, PublicKeyToken=null
# by generator 1.145
# no doc
# no imports

# no functions
# classes

class IElement:
    # no doc
    def __init__(self, *args): #cannot find CLR method
        """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
        pass

    Id = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Id(self: IElement) -> int



"""

    Label = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Label(self: IElement) -> str



Set: Label(self: IElement) = value

"""

    Notes = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Notes(self: IElement) -> str



Set: Notes(self: IElement) = value

"""

class ElementBase(IElement):
    """ ElementBase(id: int) """
    def __init__(self, *args): #cannot find CLR method
        """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
        pass

    @staticmethod # known case of __new__
    def __new__(self, id):
        """ __new__(cls: type, id: int) """
        pass

    def __repr__(self, *args): #cannot find CLR method
        """ __repr__(self: object) -> str """
        pass

    Id = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Id(self: ElementBase) -> int



"""

    Label = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Label(self: ElementBase) -> str



Set: Label(self: ElementBase) = value

"""

    Notes = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Notes(self: ElementBase) -> str



Set: Notes(self: ElementBase) = value

"""

class IElementManager:
    # no doc
    def Create(self) -> object:
# Error generating skeleton for function Create: Method must be called on a Type for which Type.IsGenericParameter is false.
        pass

    def Delete(self, id):
        """ Delete(self: IElementManager[TElementType], id: int) """
        pass

    def Element(self, *__args):
# Error generating skeleton for function Element: Method must be called on a Type for which Type.IsGenericParameter is false.
        pass

    def ElementIDs(self):
        """ ElementIDs(self: IElementManager[TElementType]) -> List[int] """
        pass

    def Elements(self):
        """ Elements(self: IElementManager[TElementType]) -> List[TElementType] """
        pass

    def Exists(self, id):
        """ Exists(self: IElementManager[TElementType], id: int) -> bool """
        pass

    def __init__(self, *args): #cannot find CLR method
        """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
        pass

    Count = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Count(self: IElementManager[TElementType]) -> int



"""

class ElementManagerBase(IElementManager):
    """ ElementManagerBase[TElementType]() """
    def Create(self):
# Error generating skeleton for function Create: Method must be called on a Type for which Type.IsGenericParameter is false.
        pass

    def Delete(self, id):
        """ Delete(self: ElementManagerBase[TElementType], id: int) """
        pass

    def Element(self, *__args):
# Error generating skeleton for function Element: Method must be called on a Type for which Type.IsGenericParameter is false.
        pass

    def ElementIDs(self):
        """ ElementIDs(self: ElementManagerBase[TElementType]) -> List[int] """
        pass

    def Elements(self):
        """ Elements(self: ElementManagerBase[TElementType]) -> List[TElementType] """
        pass

    def Exists(self, id):
        """ Exists(self: ElementManagerBase[TElementType], id: int) -> bool """
        pass

    def NewElement(self, *args): #cannot find CLR method
# Error generating skeleton for function NewElement: Method must be called on a Type for which Type.IsGenericParameter is false.
        pass

    def __init__(self, *args): #cannot find CLR method
        """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
        pass

    def __repr__(self, *args): #cannot find CLR method
        """ __repr__(self: object) -> str """
        pass

    Count = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Count(self: ElementManagerBase[TElementType]) -> int



"""

    ElementList = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default



class IElementInput:
    # no doc
    def __init__(self, *args): #cannot find CLR method
        """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
        pass


class IActiveElementInput(IElementInput):
    # no doc
    def __init__(self, *args): #cannot find CLR method
        """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
        pass

    IsActive = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: IsActive(self: IActiveElementInput) -> bool



Set: IsActive(self: IActiveElementInput) = value

"""



class IBaseLinkInput(IActiveElementInput, IElementInput):
    # no doc
    def GetPoints(self):
        """ GetPoints(self: IBaseLinkInput) -> List[GeometryPoint] """
        pass

    def SetPoints(self, points):
        """ SetPoints(self: IBaseLinkInput, points: List[GeometryPoint]) """
        pass

    def __init__(self, *args): #cannot find CLR method
        """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
        pass

    IsUserDefinedLength = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: IsUserDefinedLength(self: IBaseLinkInput) -> bool



Set: IsUserDefinedLength(self: IBaseLinkInput) = value

"""

    Length = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Length(self: IBaseLinkInput) -> float



Set: Length(self: IBaseLinkInput) = value

"""

    StartNode = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: StartNode(self: IBaseLinkInput) -> IElement



Set: StartNode(self: IBaseLinkInput) = value

"""

    StopNode = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: StopNode(self: IBaseLinkInput) -> IElement



Set: StopNode(self: IBaseLinkInput) = value

"""









class IElementResults:
    # no doc
    def __init__(self, *args): #cannot find CLR method
        """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
        pass


class IElementsInput:
    # no doc
    def __init__(self, *args): #cannot find CLR method
        """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
        pass


class IElementsResults:
    # no doc
    def __init__(self, *args): #cannot find CLR method
        """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
        pass


class INetwork:
    # no doc
    def __init__(self, *args): #cannot find CLR method
        """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
        pass

    Pipes = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Pipes(self: INetwork) -> IPipes



"""



class IPipeInput(IBaseLinkInput, IActiveElementInput, IElementInput):
    # no doc
    def __init__(self, *args): #cannot find CLR method
        """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
        pass

    Diameter = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Diameter(self: IPipeInput) -> float



Set: Diameter(self: IPipeInput) = value

"""

class IPipe(IElement):
    # no doc
    def __init__(self, *args): #cannot find CLR method
        """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
        pass

    @property
    def Input(self) -> IPipeInput:
        """Get: Input(self: IPipe) -> IPipeInput

        """
        pass

    Results = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Results(self: IPipe) -> IPipeResults"""


class IPipeResults(IElementResults):
    # no doc
    def Flow(self, timeStepIndex=None):
        """
        Flow(self: IPipeResults) -> Nullable[float]

        Flow(self: IPipeResults, timeStepIndex: int) -> Nullable[float]
        """
        pass

    def __init__(self, *args): #cannot find CLR method
        """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
        pass


class IPipes(IElementManager):
    # no doc
    def __init__(self, *args): #cannot find CLR method
        """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
        pass

    def Create() -> IPipe:
        pass

    Input = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Input(self: IPipes) -> IPipesInput



"""

    Results = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Results(self: IPipes) -> IPipesResults



"""



class IPipesInput(IElementsInput):
    # no doc
    def Diameters(self):
        """ Diameters(self: IPipesInput) -> IDictionary[int, float] """
        pass

    def __init__(self, *args): #cannot find CLR method
        """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
        pass


class IPipesResults(IElementsResults):
    # no doc
    def Flows(self, timeStepIndex=None, ids=None):
        """
        Flows(self: IPipesResults) -> IDictionary[int, Nullable[float]]

        Flows(self: IPipesResults, timeStepIndex: int) -> IDictionary[int, Nullable[float]]

        Flows(self: IPipesResults, timeStepIndex: int, ids: List[int]) -> IDictionary[int, Nullable[float]]
        """
        pass

    def __init__(self, *args): #cannot find CLR method
        """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
        pass


class ITestModel:
    # no doc
    def __init__(self, *args): #cannot find CLR method
        """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
        pass

    @property
    def Network(self) -> INetwork:
        """Get: Network(self: ITestModel) -> INetwork"""
        pass



class Network(INetwork):
    """ Network() """
    def __init__(self, *args): #cannot find CLR method
        """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
        pass

    def __repr__(self, *args): #cannot find CLR method
        """ __repr__(self: object) -> str """
        pass

    Pipes = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Pipes(self: Network) -> IPipes



"""



class Pipe(ElementBase, IPipe, IPipeInput, IBaseLinkInput, IActiveElementInput, IElementInput, IPipeResults, IElementResults):
    """ Pipe(id: int) """
    def Flow(self, timeStepIndex=None):
        """
        Flow(self: Pipe) -> Nullable[float]

        Flow(self: Pipe, timeStepIndex: int) -> Nullable[float]
        """
        pass

    def GetPoints(self):
        """ GetPoints(self: Pipe) -> List[GeometryPoint] """
        pass

    def SetPoints(self, points):
        """ SetPoints(self: Pipe, points: List[GeometryPoint]) """
        pass

    def __init__(self, *args): #cannot find CLR method
        """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
        pass

    @staticmethod # known case of __new__
    def __new__(self, id):
        """ __new__(cls: type, id: int) """
        pass

    Diameter = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Diameter(self: Pipe) -> float



Set: Diameter(self: Pipe) = value

"""

    Input = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Input(self: Pipe) -> IPipeInput



"""

    IsActive = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: IsActive(self: Pipe) -> bool



Set: IsActive(self: Pipe) = value

"""

    IsUserDefinedLength = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: IsUserDefinedLength(self: Pipe) -> bool



Set: IsUserDefinedLength(self: Pipe) = value

"""

    Length = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Length(self: Pipe) -> float



Set: Length(self: Pipe) = value

"""

    Results = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Results(self: Pipe) -> IPipeResults



"""

    StartNode = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: StartNode(self: Pipe) -> IElement



Set: StartNode(self: Pipe) = value

"""

    StopNode = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: StopNode(self: Pipe) -> IElement



Set: StopNode(self: Pipe) = value

"""



class Pipes(IPipes, IPipesInput, IElementsInput, IPipesResults, IElementsResults):
    """ Pipes() """
    def Diameters(self):
        """ Diameters(self: Pipes) -> IDictionary[int, float] """
        pass

    def Flows(self, timeStepIndex=None, ids=None):
        """
        Flows(self: Pipes) -> IDictionary[int, Nullable[float]]

        Flows(self: Pipes, timeStepIndex: int) -> IDictionary[int, Nullable[float]]

        Flows(self: Pipes, timeStepIndex: int, ids: List[int]) -> IDictionary[int, Nullable[float]]
        """
        pass

    def NewElement(self, *args): #cannot find CLR method
        """ NewElement(self: Pipes) -> IPipe """
        pass

    def __init__(self, *args): #cannot find CLR method
        """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
        pass

    ElementList = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    Input = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Input(self: Pipes) -> IPipesInput



"""

    Results = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Results(self: Pipes) -> IPipesResults



"""



class TestModel(ITestModel):
    """ TestModel(filenmae: str) """
    def __init__(self, *args): #cannot find CLR method
        """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
        pass

    @staticmethod # known case of __new__
    def __new__(self, filenmae):
        """ __new__(cls: type, filenmae: str) """
        pass

    def __repr__(self, *args): #cannot find CLR method
        """ __repr__(self: object) -> str """
        pass

    Network = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Network(self: TestModel) -> INetwork



"""

class EntryPoint(object):
    # no doc
    @staticmethod
    def EndSession():
        """ EndSession() """
        pass

    @staticmethod
    def Open(filename: str) -> ITestModel:
        """ Open(filename: str) -> ITestModel """
        return ITestModel()

    @staticmethod
    def GetModel():
        """ GetModel() -> TestModel"""
        pass

    @staticmethod
    def StartSession():
        """ StartSession() """
        pass

    __all__ = [
        'EndSession',
        'Open',
        'StartSession',
    ]
