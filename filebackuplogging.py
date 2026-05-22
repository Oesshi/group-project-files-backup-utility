# group-project
import os 
import shutil 
from abc import abc, abstractmethod
from datetime import datetime

class BackUpLogger:
  _instance = None

def __new__(cls):
  if cls._instance is None:
    cls._instance = super(Backkuplogger, cls).__new__(cls)
return cls._instance

def log(self, message):
  timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S)
  print(f"[{timestamp}] message")
        
class FileService(ABC):
  @abstractmethod 
  def sync_file(self, source, destination):
    pass import hashlib 
import logging 
import time

class OSfileAdapter(FileService):
  def sync_file(self, source, destination):
    if not os.path.exists(source)
    return "Error: Source is not found"

    if os.path.exists(destination):
     if os.path.getmtime(source) <= os.path.getmtime(destination)
     return "No changes made"

shutil.copy2(source,destination)
return "Copied file"


class Command(ABC):
  @abstractmethod 
def execute(self):
  pass 
class FileBackupCommand(Command):
  def __init__(self,service: FileService, src: str, dest: str):
    self.service = service
    self.src = src
    self.dest = dest
    self.logger = BackupLogger()
def execute(self):
  result = self.service.sync_file(self.src,self.dest)
  self.logger.log(f"Backup from {self.src} to {self.dest} : {result}")

if __name__ == "__main__":
  adapter = OSFileAdapter()
  cmd = FileBackupCommand(adapter, "source.txt", "backup_source.txt")
  cmd.execute()


  
  

