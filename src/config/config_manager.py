import configparser
import os
from pathlib import Path

from constants.app_directory import APP_DIRECTORY


class ConfigManager:
    """
    Singleton class # TODO keep it so ?
    """
    FILE = os.path.join(APP_DIRECTORY, 'resources', 'config', 'config.ini')

    _instance = None
    _config_values = None

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super(ConfigManager, cls).__new__(cls)
            cls._instance._load_config()
        return cls._instance

    def _load_config(self):
        config = configparser.ConfigParser()
        config.read(self.FILE)

        app_name = config.get('General', 'app_name')
        app_version = config.get('General', 'app_version')
        app_author = config.get('General', 'app_author')
        footswitch_vendor_id = config.get('Device', 'footswitch_vendor_id')
        footswitch_model_id = config.get('Device', 'footswitch_model_id')
        footswitch_key = config.get('Device', 'footswitch_key')

        self._config_values = {
            'app_name': app_name,
            'app_version': app_version,
            'app_author': app_author,
            'footswitch_vendor_id': footswitch_vendor_id,
            'footswitch_model_id': footswitch_model_id,
            'footswitch_key': footswitch_key,
        }

    def get(self, key: str) -> str:
        return self._config_values.get(key)