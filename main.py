from src.system_config import SystemConfig


def main():
    """
    Entry point for the File Backup and Sync Utility.

    This script:
    - Initializes the SystemConfig Singleton
    """

    # 1. Create / load configuration
    config = SystemConfig(
        util_root_path= "util_system",
        source_path= "C:/data/source",
        backup_path= "C:/data/backup",
        sync_interval=5
    )

    print(config.source_path)

    config1 = SystemConfig(
        util_root_path= "util_system",
    )
    print(config1.source_path)

if __name__ == "__main__":
    main()
