"""
imports FileStorage and creates  new instance of it and call reload method
"""
from .engine.file_storage import FileStorage
storage = FileStorage()
storage.reload()
