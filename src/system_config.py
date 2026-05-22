import os

class SystemConfig():
    """
    Singleton configuration manager for the File Backup and Sync Utility.
    Handles config persistence, loading, and global system settings.
    """

    _instance = None

    def __new__(cls,util_root_path,source_path=None,backup_path=None,sync_interval=10,config_file_name="config.txt",log_file_name="log.txt"):

        if not util_root_path:
            raise ValueError("util_root_path is required")
        cls._instance_initialized = False

        if cls._instance is None:
            cls._instance = super(SystemConfig, cls).__new__(cls)

            cls._instance.util_root_path = util_root_path
            cls._instance.config_file_name = config_file_name
            cls._instance.log_file_name = log_file_name

            cls._instance.config_file_path = os.path.join(util_root_path, config_file_name)
            cls._instance.log_file_path = os.path.join(util_root_path, log_file_name)

            cls._instance.source_path = source_path
            cls._instance.backup_path = backup_path
            cls._instance.sync_interval = sync_interval

        cls._instance_initialized = True

        return cls._instance

    def save_to_file(self)
    config_data = {"utility_root_path": util_root_path,
                   "config_file_name": config_file_name,
                   "log_file_name": log_file_name,
                   "config_file_path": config_file_path,
                   "log_file_path": log_file_path,
                   "source_path": source_path
                   "back_up": back_up
                   "sync_interval": sync_interval}

    with open(config_file, "w") as file:






