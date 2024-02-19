#!/usr/bin/python3
"""
For Initializes  the module global variables
"""


from models.engine.file_storage import FileStorage
"""
from models.engine import FileStorage
"""


storage = FileStorage()
storage.reload()
