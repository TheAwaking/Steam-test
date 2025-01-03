import json


class ConfigReader:
    def __init__(self, config_file_path):
        self.config_file_path = config_file_path
        self.config = self.load_config()

    def load_config(self):
        with open(self.config_file_path) as config_file:
            return json.load(config_file)

    def get_base_url(self):
        return self.config.get("base_url")

    def get_timeout(self):
        return self.config.get("timeout")

    def get_browser_options(self):
        return self.config.get("browser_options")
