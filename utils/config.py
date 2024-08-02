import os
import json

class Config:
    def __init__(self, config_file: str = "config.json"):
        self.config_file = config_file
        self.config = self.load_config()

    def load_config(self) -> dict:
        if os.path.exists(self.config_file):
            with open(self.config_file, "r") as f:
                return json.load(f)
        else:
            return {}

    def get(self, key: str, default: str = None) -> str:
        return self.config.get(key, default)

    def set(self, key: str, value: str):
        self.config[key] = value
        self.save_config()

    def save_config(self):
        with open(self.config_file, "w") as f:
            json.dump(self.config, f, indent=4)

def get_config(config_file: str = "config.json") -> Config:
    return Config(config_file)
