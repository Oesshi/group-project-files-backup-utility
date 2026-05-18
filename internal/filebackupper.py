import filecmp
import shutil
import os

comparison = filecmp.dircmp('branch', 'main')

comparison.report()

files_to_copy = comparison.left_only

for filename in files_to_copy:
    source_path = os.path.join('branch', filename)
    if os.path.isfile(source_path):
        shutil.copy2(source_path, 'main')
        print(f"Copied: {filename}")
