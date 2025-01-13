import json


class ConfigReader:
    def __init__(self, config_path):
        with open(config_path, 'r') as f:
            self.config = json.load(f)

    def get_value(self, key):
        return self.config.get(key)
