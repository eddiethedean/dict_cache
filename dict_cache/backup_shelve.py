import shelve
from typing import Any


class BackupShelve:
    def __init__(self, path: str) -> None:
        self.path = path
        
    def __repr__(self) -> str:
        return f'BackupShelve("{self.path}")'
        
    def __getitem__(self, key: str) -> Any:
        with shelve.open(self.path) as d:
            return d[key]
        
    def __setitem__(self, key: str, value: Any) -> None:
        with shelve.open(self.path) as d:
            d[key] = value
            
    def __contains__(self, key: str) -> bool:
        with shelve.open(self.path) as d:
            return key in d
    
    def __len__(self) -> int:
        with shelve.open(self.path) as d:
            return len(d)
        
    def keys(self) -> tuple[str]:
        with shelve.open(self.path) as d:
            return tuple(d.keys())