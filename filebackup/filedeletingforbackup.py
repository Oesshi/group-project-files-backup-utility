import os
import shutil
def backup_and_cleanup(source_dir, backup_dir, extension=".bak", delete_originals=True):
  if not os.path.exists(backup_dir):
    os.makedirs(backup_dir)
    print(f"Created backup directory: {backup_dir}")
for filename in os.listdir(source_dir):
  if filename.endswith(extension):
    source_file = os.path.join(source_dir, filename)
    backup_file = os.path.join(backup_dir, filename)
  if not os.path.isfile(source_file)
   continue
try:
  shutil2.copy2(source_file, backup_file):
  print(f"Backed up: {filename} to {backup_dir}")

if delete_originals:
  os.remove(source_file)
  print(f"Deleted original : {source_file}")

except PermissionError:
  print(f"Error: permission denied when handling with {filename}")
except FileNotFoundError:
 print(f"error: {filename} is not found")
except Exception as e:
  print(f"An unexpected error occured with {filename} : {e}")

backup_and_cleanup(source_path, backup_path, extension=".bak", delete_originals=True):
