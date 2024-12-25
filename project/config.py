from typing import Any

import yaml

from . import CONFIG_FILE_PATH


class Config:
    def __init__(self):
        print("Initializing config...")
        self._config = self.__load_config()
        self.__dict__.update(self._config)

    @staticmethod
    def __load_config():
        with open(CONFIG_FILE_PATH) as f:
            cfg = yaml.load(f, Loader=yaml.FullLoader)
            return cfg

    def get(self, key: str, default: Any = None) -> Any:
        """Safely get a config value."""
        return self._config.get(key, default)

    def __getattr__(self, name: str) -> Any:
        """Allow falling back to dictionary access if attribute doesn't exist."""
        return self._config.get(name)
