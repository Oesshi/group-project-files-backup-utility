from src.system_config import SystemConfig




def main():
    """
    Entry point for the File Backup and Sync Utility.

    This script:
    - Initializes the SystemConfig Singleton
    """

    # 1. Create / load configuration
    config = SystemConfig(
        util_root_path= "log",
        source_path='RoveemaAena',
        backup_path='backup',
        log_file_name='logoon.txt',
        sync_interval=30
    )

    print(config)



if __name__ == "__main__":

    main()
