import json
from os.path import exists
from typing import Any, Tuple

from dict_cache.backup_interface import BackupDict


class BackupJSON(BackupDict):
    def __init__(self, json_path: str) -> None:
        self.json_path = json_path
        if not exists(json_path):
            with open(json_path, 'w') as j:
                json.dump({}, j)
        
    def __repr__(self) -> str:
        return f'BackupJSON("{self.json_path}")'
        
    def __getitem__(self, key: str) -> Any:
        with open(self.json_path, 'r') as j:
            return json.load(j)[key]
        
    def __setitem__(self, key: str, value: Any) -> None:
        with open(self.json_path, 'w') as j:
            d = json.load(j)
            d[key] = value
            json.dump(d, j)

    def __contains__(self, key: str) -> bool:
        with open(self.json_path, 'r') as j:
            return key in json.load(j)
        
    def __len__(self) -> int:
        with open(self.json_path, 'r') as j:
            return len(json.load(j))
        
    def keys(self) -> Tuple[str]:
        with open(self.json_path, 'r') as j:
            return tuple(json.load(j).keys())