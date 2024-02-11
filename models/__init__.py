#!/usr/bin/python3
from .engine.file_storage import FileStorage
"""
Initializes  the module global (singleton) variables
"""

"""
Retrieves the storage instance
"""


storage = FileStorage()
storage.reload()
