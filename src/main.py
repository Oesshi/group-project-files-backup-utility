from src.system_config import SystemConfig
from src.logger import Logger
from src.sync_analyser import SyncAnalyser
from src.file_handler import FileHandler
from src.sync_engine import SyncEngine


import time
import argparse

def parse_args():
    parser = argparse.ArgumentParser(
        description="File Backup and Sync Utility"
    )

    parser.add_argument("--root")
    parser.add_argument("--source")
    parser.add_argument("--backup")
    parser.add_argument("--interval",type=int,default=2)

    parser.add_argument("--logfile",default="log.txt")

    parser.add_argument("--config",default="config.txt")


    return parser.parse_args()


def main():
    args = parse_args()

    config = SystemConfig(
        util_root_path= args.root,
        source_path=args.source,
        backup_path=args.backup,
        log_file_name=args.logfile,
        sync_interval=args.interval,
        config_file_name= args.config
    )

    logger = Logger(config)

    analyser = SyncAnalyser(config, logger)
    handler = FileHandler(config, logger)

    engine = SyncEngine(config, analyser, handler, logger)

    engine.start()

    # keep main thread alive
    try:
        while True:
            time.sleep(1)
    except KeyboardInterrupt:
        engine.stop()

if __name__ == "__main__":
    main()
