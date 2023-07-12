from typing import Any, Protocol, Tuple
from abc import abstractmethod


class BackupDict(Protocol):
    """
    CacheDict requires an object that implements this interface.
    """
    @abstractmethod
    def __getitem__(self, key: str) -> Any:
        raise NotImplemented

    @abstractmethod  
    def __setitem__(self, key: str, value: Any) -> None:
        raise NotImplemented

    @abstractmethod   
    def __contains__(self, key: str) -> bool:
        raise NotImplemented
    
    @abstractmethod
    def __len__(self) -> int:
        raise NotImplemented
        
    @abstractmethod
    def keys(self) -> Tuple[str]:
        raise NotImplemented


