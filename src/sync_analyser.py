import os
import filecmp


class DiffResult:
    def __init__(self):
        self.new_files = {}
        self.modified_files = {}
        self.deleted_files = {}
        self.unchanged_files = {}

        self.new_directories = []
        self.deleted_directories = []

    def __str__(self):
        return (
            f"DiffResult(\n"
            f"New Files: {self.new_files}\n"
            f"Modified Files: {self.modified_files}\n"
            f"Deleted Files: {self.deleted_files}\n"
            f"Unchanged Files: {self.unchanged_files}\n"
            f"New Directories: {self.new_directories}\n"
            f"Deleted Directories: {self.deleted_directories}"
        )


class SyncAnalyser:

    def __init__(self, config, logger):
        self._config = config
        self._logger = logger
        self.result = None

    @staticmethod
    def build_file_map(root_path):
        file_map = {}

        for root, dirs, files in os.walk(root_path):

            for file_name in files:

                absolute_path = os.path.join(root, file_name)

                relative_path = os.path.relpath(
                    absolute_path,
                    root_path
                )

                file_map[relative_path] = {
                    "absolute_path": absolute_path,
                    "size": os.path.getsize(absolute_path),
                    "modified_time": os.path.getmtime(absolute_path)
                }

        return file_map

    @staticmethod
    def build_directory_set(root_path):
        directory_set = set()

        for root, dirs, files in os.walk(root_path):

            for directory in dirs:

                absolute_path = os.path.join(root, directory)

                relative_path = os.path.relpath(
                    absolute_path,
                    root_path
                )

                directory_set.add(relative_path)

        return directory_set

    def compare(self):

        self._log(
            "INFO",
            f"Starting analysis | Source={self._config.source_path} | Backup={self._config.backup_path}"
        )

        self.result = DiffResult()

        source_files = self.build_file_map(self._config.source_path)
        backup_files = self.build_file_map(self._config.backup_path)

        source_set = set(source_files.keys())
        backup_set = set(backup_files.keys())

        new_files = source_set - backup_set
        for path in sorted(new_files):
            self.result.new_files[path] = source_files[path]

        self._log("INFO", f"New files detected: {len(new_files)}")

        deleted_files = backup_set - source_set
        for path in sorted(deleted_files):
            self.result.deleted_files[path] = backup_files[path]

        self._log("INFO", f"Deleted files detected: {len(deleted_files)}")

        modified = 0
        unchanged = 0

        for path in source_set & backup_set:

            source_info = source_files[path]
            backup_info = backup_files[path]

            if filecmp.cmp(
                source_info["absolute_path"],
                backup_info["absolute_path"],
                shallow=False
            ):
                self.result.unchanged_files[path] = source_info
                unchanged += 1
            else:
                self.result.modified_files[path] = {
                    "source": source_info,
                    "backup": backup_info
                }
                modified += 1

        self._log(
            "INFO",
            f"Modified={modified} | Unchanged={unchanged}"
        )

        source_dirs = self.build_directory_set(self._config.source_path)
        backup_dirs = self.build_directory_set(self._config.backup_path)

        self.result.new_directories = list(source_dirs - backup_dirs)
        self.result.deleted_directories = list(backup_dirs - source_dirs)

        self._log(
            "INFO",
            f"Directories | New={len(self.result.new_directories)} | Deleted={len(self.result.deleted_directories)}"
        )

        self._log("INFO", "Analysis completed successfully")

        return self.result


    def __str__(self):
        return (
            f"SyncAnalyser(\n"
            f"  config={self._config}\n"
            f"  result={self.result}\n"
            f")"
        )

    def _log(self, severity, message):
        if self._logger:
            self._logger.log_message(
                severity,
                message,
                self.__class__.__name__
            )
