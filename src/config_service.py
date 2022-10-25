import yaml

from yaml.loader import BaseLoader

from console_service import print_config


class ConfigService:
    database_config: dict = None
    bluetooth_config: dict = None

    @staticmethod
    def read() -> None:
        with open('resources/config.yml', 'r') as f:
            print_config('Read config...')
            config: dict = dict(list(yaml.load_all(f, Loader=BaseLoader))[0])

            # Database
            print_config('Setup database config.')
            ConfigService.database_config = dict(config.get('mysql'))
            ConfigService.database_config.__setitem__('raise_on_warnings',
                                                      True if ConfigService.database_config.get(
                                                          'raise_on_warnings') == 'true' else False)

            # Bluetooth
            print_config('Setup Bluetooth config.')
            ConfigService.bluetooth_config = dict(config.get('bluetooth'))
            ConfigService.bluetooth_config.__setitem__('discover_duration',
                                                       int(ConfigService.bluetooth_config.get('discover_duration')))
            ConfigService.bluetooth_config.__setitem__('scan_interval',
                                                       int(ConfigService.bluetooth_config.get('scan_interval')))

            print_config('Config loaded!')
