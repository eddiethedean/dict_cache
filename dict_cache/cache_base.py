from copy import copy
from typing import Any

from dict_cache.backup_interface import BackupDict


class CacheBase:
    """
    A dict backed up by persistent storage.
    Accessed key, values are stored in RAM as a dict for speedy access.
    Not-accessed key, values are stored in persistent storage.

    Requires a BackupDict object to be passed in.
    """
    def __init__(self, backup_dict: BackupDict) -> None:
        self._backup_dict = backup_dict
        self._cache_dict = dict()
        
    def __repr__(self) -> str:
        return f'DictCache(backup_dict={self._backup_dict})'
        
    def __getitem__(self, key: str) -> Any:
        if key in self._cache_dict:
            return self._cache_dict[key]
        else:
            value = self._backup_dict[key]
            self._cache_dict[key] = value
            return value
        
    def __setitem__(self, key: str, value: Any) -> None:
        self._backup_dict[key] = value
        self._cache_dict[key] = value
        
    def __contains__(self, key: str) -> bool:
        out = True if key in self._cache_dict else key in self._backup_dict
        if out and key not in self._cache_dict:
            self._cache_dict[key] = self._backup_dict[key]
        return out
        
    def __len__(self) -> int:
        return len(self._backup_dict)
        
    def keys(self) -> tuple:
        return self._backup_dict.keys()
    
    @property
    def cache(self) -> dict:
        return copy(self._cache_dict)