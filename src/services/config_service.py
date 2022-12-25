import yaml
import os

from yaml.loader import BaseLoader

from services.console_service import print_config
from dotenv import load_dotenv
from pathlib import Path


class ConfigService:

    def __init__(self) -> None:
        dotenv_path = Path('../docker/.env')
        load_dotenv(dotenv_path=dotenv_path)

        with open('resources/config.yml', 'r') as f:
            print_config('Read config...')
            config: dict = dict(list(yaml.load_all(f, Loader=BaseLoader))[0])

            # Database
            print_config('Setup database config.')
            self.database_config = dict(config.get('mysql'))
            self.database_config.__setitem__('raise_on_warnings',
                                             True if self.database_config.get(
                                                 'raise_on_warnings') == 'true' else False)
            self._replace_env()

            # Bluetooth
            print_config('Setup Bluetooth config.')
            self.bluetooth_config = dict(config.get('bluetooth'))
            self.bluetooth_config.__setitem__('discover_duration',
                                              int(self.bluetooth_config.get('discover_duration')))
            self.bluetooth_config.__setitem__('scan_interval',
                                              int(self.bluetooth_config.get('scan_interval')))

            print_config('Config loaded!')

    def _replace_env(self) -> None:
        self._replace_entry('database', 'MARIADB_DATABASE')
        self._replace_entry('user', 'MARIADB_USER')
        self._replace_entry('password', 'MARIADB_SMARTDOOR_PASSWORD')
        self._replace_entry('host', 'MARIADB_HOST')
        self._replace_entry('port', 'MARIADB_PORT')

    def _replace_entry(self, key: str, env: str) -> None:
        if self.database_config.get(key) == '${' + env + '}':
            self.database_config.__setitem__(key, os.getenv(env))
