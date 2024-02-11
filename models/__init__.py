#!/usr/bin/python3

"""
Initializes  the module global (singleton) variables
"""

"""
Retrieves the storage instance
"""
from .engine.file_storage import FileStorage


storage = FileStorage()
storage.reload()
