import logging
import logging.config
import os
import json

class Logger:
    def __init__(self, name: str, log_level: str = "INFO"):
        self.name = name
        self.log_level = log_level
        self.logger = logging.getLogger(name)
        self.config_logging()

    def config_logging(self):
        log_config_file = "logging.json"
        if os.path.exists(log_config_file):
            with open(log_config_file, "r") as f:
                log_config = json.load(f)
            logging.config.dictConfig(log_config)
        else:
            logging.basicConfig(level=self.log_level)
        self.logger.setLevel(self.log_level)

    def debug(self, message: str):
        self.logger.debug(message)

    def info(self, message: str):
        self.logger.info(message)

    def warning(self, message: str):
        self.logger.warning(message)

    def error(self, message: str):
        self.logger.error(message)

    def critical(self, message: str):
        self.logger.critical(message)

def get_logger(name: str, log_level: str = "INFO") -> Logger:
    return Logger(name, log_level)
