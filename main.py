from src.system_config import SystemConfig
from src.logger import Logger




def main():
    """
    Entry point for the File Backup and Sync Utility.

    This script:
    - Initializes the SystemConfig Singleton
    """

    # 1. Create / load configuration
    config = SystemConfig(
        util_root_path= "log",
        source_path='source',
        backup_path='backup',
        log_file_name='log.txt',
        sync_interval=30
    )


    logger = Logger(config)
    logger.log_message('INFO','ComParing files','file comparer')



if __name__ == "__main__":

    main()
