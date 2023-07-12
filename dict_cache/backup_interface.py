from typing import Any, Protocol, Tuple


class BackupDict(Protocol):   
    def __getitem__(self, key: str) -> Any:
        ...
        
    def __setitem__(self, key: str, value: Any) -> None:
        ...
            
    def __contains__(self, key: str) -> bool:
        ...
    
    def __len__(self) -> int:
        ...
        
    def keys(self) -> Tuple[str]:
        ...


