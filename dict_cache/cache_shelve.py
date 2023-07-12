from dict_cache.backup_shelve import BackupShelve
from dict_cache.cache_base import CacheBase


class CacheShelve(CacheBase):
    """
    A dict backed up by shelve persistent storage.
    Accessed key, values are stored in RAM as a dict for speedy access.
    Keys must be strings.
    Values must be Picklable.
    """
    def __init__(self, shelve_path: str):
        backup = BackupShelve(shelve_path)
        super().__init__(backup)