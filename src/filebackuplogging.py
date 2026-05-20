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
    return "Error: Source is not found:

   if os.path.exists(destination):
     if os.path.getmtime(source) <= os.path.getmtime(destination)
     return "No changes made"

shutil.copy2(source,destination)
return "Copied file"


class Command(ABC):
  @abstractmethod 
def execute(self):
  pass 

class BackUpCommand(Command):
  def __init__(self, source, destination, adapter):
    self.source = source 
    self.destination = destination import hashlib 
import logging 
import time
    self.adapter = adapter
    self.logger = BackupLogger()

def executer(self):
  result = self.adapter.sync_file(self.source, self.destination)
  filename = os.path.basename(self.source)
if result == "Copied file":
  self.logger.log(f"Success : {filename} backed up to {self.destination}
elif result == "No changes made":
   self.logger.log(f"Skipped : {filename} has made no changes")
else:
  self.logger.log(f"Failed : {result}")

class BackUpUtility:
  def __init__(self):
  self.queue = []
  def add_task(self,command):
  self.queue.append(command)
def run_monitoring_simulation(self):
self.logger = BackUpLogger()
  
  

