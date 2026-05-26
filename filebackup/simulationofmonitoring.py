import time
import os
import shutil
import logging
from watchdog.observers import observer
from watchdog.events import FileSystemEventHandler

source_dir='/path/to/main/files'
backup_dir='/path/to/backup/destination'
log_file = 'backup_monitor.log'

logging.basicConfig(
  filename=log_file
  level=logging.info,
  format="%(asctime)s - %(message)s",
  datefmt ="%Y-%m-%d %H:%M:%S"
)
def backup_file(file_path):
  relative_path = os.path.relpath(file_path, source_dir)
  destination_path = os.path.join(backup_dir, relative_path)
dest_dir = os.path.dirname(destination_path)
if not os.path.exists(dest_dir):
  os.makedirs(dest_dir)

try:
  shutil2.copy2(file_path, destination_path)
  logging.info(f"Backup Success: {relative_path}")
except Exception as e:
  logging.error(f"Backup Failed : {relative_path} - {e}")

class BackupHandler(FileSystemEventHandler):
  def on_created(self,event):
    if not event.is_directory:
      print(f"[monitor] New file downloaded and detected: {event.src_path}")
      backup_file(event.src_path)
  def on_modified(self,event):
    if not event.is_directory:
      print(f"[monitor] file deleted: {event.src_path}")
      relative_path = os.path.relpath(event.src_path, source_dir)
      dest_file = os.path.join(backup_dir, relative_path)
      if os.path.exists(dest_file)
      logging.info(f"Deleted successfully : {relative_path}")

if __name__ == "__main__":
  if not os.path.exists(backup_dir):
    os.makedirs(backup_dir)
  event_handler = BackupHandler
  observer = Observer()
  observer.schedule(event_handler, path=source_dir, recursive=True)
  
  print(f"s Simulation Started, monitoring... '{source_dir}'...")
  observer.start()

try:
  while True:
   time.sleep(1)
except KeyboardInterrupt:
  observer.stop()
  print("\n[*] Simulation Stopped. ")
observer.join()

