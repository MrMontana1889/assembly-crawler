from typing import Generic
from ModelingElements import TElementType, TElementTypeEnum

class IModelComponents(Generic[TElementType, TElementTypeEnum]):
    def Elements(self) -> List[TElementType]:
        pass

    def ElementType(self, id: int) -> TElementTypeEnum:
        pass