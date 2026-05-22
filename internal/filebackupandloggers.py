import filecmp
import shutil
import os
import logging
import sys

logging.basicConfig(
    format='%(asctime)s - %(levelname)s - %(message)s',
    level=logging.INFO
)

logging.info("This message timestamped?")

compare = filecmp.dircmp('branch', 'main')

root_src_dir = 'branch/'
root_dst_dir = 'main/'

compare.report()

backupMenu = f"""

====== BACKUP MENU ======

Enter a command:

        'status'

Provides file report

#########################

        'copy'

Copies files across

#########################

        'delete'

Deletes a file

#########################

        'exit'

Exits from the terminal

#########################

=========================

"""


c = input(backupMenu)



if c == 'status':
    compare.report()
    logging.info("Files compared.")

if c == 'copy':
    if os.listdir(root_src_dir):
        checker = input(f"Every file from {root_src_dir} will be moved to {root_dst_dir}! Are you sure? Yes/No: ")
        if checker == "Yes":
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
                    shutil.copy(src_file, dst_dir)
                    print(f"File '{src_file}' copied and replaced successfully.")
                    logging.info("File replacement logged.")
                compare.report()
        else:
            logging.info("Operation has been cancelled.")
    else:
        logging.info("No files to be synced.")

if c == 'delete':
    removie = input("Enter the name of the file you'd like to remove, include directory: ")
    if os.path.exists(removie):
        os.remove(removie)
        print(f"File {removie} has been successfully deleted.")
        logging.warn("File deletion logged.")
    else:
        print(f"The file does not exist.")
        logging.error("Bad input")
    compare.report()

if c == 'exit':
    logging.info("No changes found, exiting.")
    sys.exit()
