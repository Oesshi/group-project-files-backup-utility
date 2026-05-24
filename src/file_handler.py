import os
import shutil


class FileHandler:
    def __init__(self, config, logger=None):
        self._config = config
        self._logger = logger

    def apply(self, diff_result):
        self._log("INFO", "Started syncing process")

        self._create_directories(diff_result.new_directories)
        self._delete_directories(diff_result.deleted_directories)

        self._copy_new_files(diff_result.new_files)
        self._update_modified_files(diff_result.modified_files)
        self._delete_files(diff_result.deleted_files)

        self._log("INFO", "Sync process completed successfully")


    def _create_directories(self, dirs):
        self._log("INFO", f"Creating {len(dirs)} new directories")

        for dir_path in dirs:
            full_path = os.path.join(self._config.backup_path, dir_path)
            os.makedirs(full_path, exist_ok=True)

            self._log("DEBUG", f"Created directory: {dir_path}")

    def _delete_directories(self, dirs):
        self._log("INFO", f"Deleting {len(dirs)} directories")

        for dir_path in dirs:
            full_path = os.path.join(self._config.backup_path, dir_path)

            if os.path.exists(full_path):
                shutil.rmtree(full_path)
                self._log("DEBUG", f"Deleted directory: {dir_path}")


    def _copy_new_files(self, files):
        self._log("INFO", f"Copying {len(files)} new files")

        for path, info in files.items():
            dest_path = os.path.join(self._config.backup_path, path)
            os.makedirs(os.path.dirname(dest_path), exist_ok=True)

            shutil.copy2(info["absolute_path"], dest_path)

            self._log("DEBUG", f"Copied file: {path}")

    def _update_modified_files(self, files):
        self._log("INFO", f"Updating {len(files)} modified files")

        for path, info in files.items():
            dest_path = os.path.join(self._config.backup_path, path)

            shutil.copy2(info["source"]["absolute_path"], dest_path)

            self._log("DEBUG", f"Updated file: {path}")

    def _delete_files(self, files):
        self._log("INFO", f"Deleting {len(files)} files")

        for path, info in files.items():
            target_path = os.path.join(self._config.backup_path, path)

            if os.path.exists(target_path):
                os.remove(target_path)
                self._log("DEBUG", f"Deleted file: {path}")


    def _log(self, severity, message):
        if self._logger:
            self._logger.log_message(
                severity,
                message,
                self.__class__.__name__
            )
