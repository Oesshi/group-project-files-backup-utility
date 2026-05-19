import filecmp
import shutil
import os

compare = filecmp.dircmp('branch', 'main')
compare.report()

root_src_dir = 'branch/'
root_dst_dir = 'main/'

backupMenu = """

=== BACKUP MENU ===

Enter a command:

'status'

'copy'

===             ===

"""

print(backupMenu)
compare.report()

c = input(backupMenu)

if c == 'status':
    compare.report()

if c == 'copy':
    print("Works")
    for src_dir, dirs, files in os.walk(root_src_dir):
        dst_dir = src_dir.replace(root_src_dir, root_dst_dir, 1)
        if not os.path.exists(dst_dir):
            os.makedirs(dst_dir)
        for file_ in files:
            src_file = os.path.join(src_dir, file_)
            dst_file = os.path.join(dst_dir, file_)
            if os.path.exists(dst_file):
                if os.path.samefile(src_file, dst_file):
                    continue
                os.remove(dst_file)
            shutil.move(src_file, dst_dir)
            print(f"File '{src_file}' copied and replaced successfully.")
        compare.report()

