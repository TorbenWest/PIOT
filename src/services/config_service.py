import yaml

from yaml.loader import BaseLoader

from console_service import print_config


class ConfigService:

    def __init__(self) -> None:
        with open('resources/config.yml', 'r') as f:
            print_config('Read config...')
            config: dict = dict(list(yaml.load_all(f, Loader=BaseLoader))[0])

            # Database
            print_config('Setup database config.')
            self.database_config = dict(config.get('mysql'))
            self.database_config.__setitem__('raise_on_warnings',
                                             True if self.database_config.get(
                                                 'raise_on_warnings') == 'true' else False)

            # Bluetooth
            print_config('Setup Bluetooth config.')
            self.bluetooth_config = dict(config.get('bluetooth'))
            self.bluetooth_config.__setitem__('discover_duration',
                                              int(self.bluetooth_config.get('discover_duration')))
            self.bluetooth_config.__setitem__('scan_interval',
                                              int(self.bluetooth_config.get('scan_interval')))

            print_config('Config loaded!')
