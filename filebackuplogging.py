# group-project
import os 
import shutil 
import hashlib 
import logging 
import time
source_dir = r"C:\path\to\your\source"
backup_dir = r"C:\path\to\yout\backup"
poll_interval = 10
log_file = "backup_utility.log" 

logging.basicConfig(level=logging, INFO, format='%(asctime)s - %(levelname)s - %(message)s,
handlers=[
  logging.FileHandler(Log_file),
  logging.StreamHandler()
]
) 

def get_file_hash(filepath):
  hasher=hashlib.md5()
  try:
    with open(filepath, 'rb') as f:
      buf = f.read(65536)
      while len(buf) > 0:
        hasher.update(buf)
return hasher.hexdigest()
except Exception as e:
logging.error(f"Error reading file {filepath}: {e}")
return None

