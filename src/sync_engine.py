import time
import threading


class SyncEngine:
    def __init__(self, config, analyser, handler, logger):
        self._config = config
        self._logger = logger
        self._analyser = analyser
        self._handler = handler


        self._stop_event = threading.Event()
        self.thread = None

    def start(self):
        self._logger.log_message(
            "INFO",
            "SyncEngine started in background mode",
            "SyncEngine"
        )

        self.thread = threading.Thread(
            target=self._run_loop,
            daemon=True
        )
        self.thread.start()


    def stop(self):
        self._logger.log_message(
            "INFO",
            "SyncEngine stopping...",
            "SyncEngine"
        )

        self._stop_event.set()

        if self.thread:
            self.thread.join()

        self._logger.log_message(
            "INFO",
            "SyncEngine stopped",
            "SyncEngine"
        )


    def _run_loop(self):

        interval = self._config.sync_interval

        while not self._stop_event.is_set():

            try:
                self._logger.log_message(
                    "INFO",
                    "Starting sync cycle",
                    "SyncEngine"
                )


                diff = self._analyser.compare()


                self._handler.apply(diff)

                self._logger.log_message(
                    "INFO",
                    "Sync cycle completed successfully",
                    "SyncEngine"
                )

            except Exception as e:
                self._logger.log_message(
                    "ERROR",
                    f"Sync cycle failed: {str(e)}",
                    "SyncEngine"
                )


            time.sleep(interval)
