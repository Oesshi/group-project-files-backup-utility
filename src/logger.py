from datetime import datetime
import os
import textwrap

class Logger():


    _instance = None

    def __new__(cls,config):

        if not config:
            raise ValueError("config is required")

        if cls._instance is None:
            cls._instance = super(Logger, cls).__new__(cls)
            cls._instance.config = config
            os.makedirs(os.path.dirname(config.log_file_path), exist_ok=True)
            header = f"|{'TIMESTAMP':<19}|{'SEVERITY':<8}|{'SENDER':<15}|{'MESSAGE':<50}|\n"
            with open(config.log_file_path, "w", encoding="utf-8") as f:
                f.write(header)


        return cls._instance


    def log_message(self, severity, message, sender):
        timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

        ts = f"{timestamp:<19}"
        sev = f"{severity:<8}"
        snd = f"{sender:<15}"

        MAX_WIDTH = 50
        wrapped_lines = textwrap.wrap(message, width=MAX_WIDTH)

        with open(self.config.log_file_path, "a", encoding="utf-8") as f:
            if wrapped_lines:
                f.write(f"|{ts}|{sev}|{snd}|{wrapped_lines[0]:<{MAX_WIDTH}}|\n")
                for line in wrapped_lines[1:]:
                    f.write(f"|{'':19}|{'':8}|{'':15}|{line:<{MAX_WIDTH}}|\n")
