from dict_cache.backup_json import BackupJSON
from dict_cache.cache_base import CacheBase


class CacheJSON(CacheBase):
    """
    A dict backed up by json file persistent storage.
    Accessed key, values are stored in RAM as a dict for speedy access.
    Keys must be JSONable.
    Values must be JSONable.
    """
    def __init__(self, path):
        backup = BackupJSON(path)
        super().__init__(backup)