import os
import json
from datetime import datetime

class SystemConfig():
    """
    Singleton configuration manager for the File Backup and Sync Utility.
    Handles config persistence, loading, and global system settings.
    """
    _instance = None

    def __new__(cls,util_root_path,
               source_path=None,
               backup_path=None,
               sync_interval=10,
               config_file_name="config.txt",
               log_file_name="log.txt"):

        if not util_root_path:
            raise ValueError("util_root_path is required")

        if cls._instance is None:
            cls._instance = super(SystemConfig, cls).__new__(cls)
            cls._instance.util_root_path = util_root_path
            timestamp = datetime.now().strftime("%Y%m%d%H%M%S")
            cls._instance.config_file_path = os.path.join(cls._instance.util_root_path,timestamp, config_file_name)
            os.makedirs(os.path.dirname(cls._instance.config_file_path), exist_ok=True)

            try:
                cls._instance.load_from_file()

                if cls._instance.source_path != source_path and source_path:
                    cls._instance.source_path = source_path

                if cls._instance.backup_path != backup_path and backup_path:
                    cls._instance.backup_path = backup_path

                if cls._instance.sync_interval != sync_interval:
                    cls._instance.sync_interval = sync_interval


                if cls._instance.log_file_name != log_file_name:
                    cls._instance.log_file_name = log_file_name


            except:
                cls._instance.source_path = source_path
                cls._instance.backup_path = backup_path
                cls._instance.log_file_name = log_file_name
                cls._instance.sync_interval = sync_interval

            cls._instance.log_file_path = os.path.join(cls._instance.util_root_path ,timestamp, log_file_name)


            if not cls._instance.source_path:
                raise ValueError("source_path could not be found either in file nor in input.")

            if not cls._instance.backup_path:
                raise ValueError("backup_path could not be found either in file nor in input.")
            cls._instance.save_to_file()
        return cls._instance


    def load_from_file(self):
        with open(self.config_file_path, "r") as f:
            for line in f:
                key, value = line.strip().split("=")

                if key == "sync_interval":
                    value = int(value)
                setattr(self, key, value)

    def save_to_file(self):
        data = {
            "source_path": self.source_path,
            "backup_path": self.backup_path,
            "log_file_name":self.log_file_name,
            "sync_interval": self.sync_interval
        }

        with open(self.config_file_path, "w") as f:
            for key, value in data.items():
                f.write(f"{key}={value}\n")



    def __str__(self):
        return (
            f"""
            SystemConfig(
              util_root_path={self.util_root_path},
              config_file={self.config_file_path},
              log_file={self.log_file_path},
              source_path={self.source_path},
              backup_path={self.backup_path},
              sync_interval={self.sync_interval}
            )"""
        )
