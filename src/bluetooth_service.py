import bluetooth

from console_service import print_bluetooth
from database_service import MySqlService


class BluetoothService:
    devices_in_range: list = []

    def __init__(self, service: MySqlService) -> None:
        self.db_service: MySqlService = service

    # https://github.com/pybluez/pybluez
    def scan(self) -> None:
        print_bluetooth('Scanning for bluetooth devices...')
        devices = bluetooth.discover_devices(duration=10, lookup_names=True)

        for current in self.devices_in_range:
            if not any(device[0] == current.get('bd_addr') for device in devices):
                self.__remove_device__(current.get('name'), current.get('bd_addr'))

        if len(devices) == 0:
            print_bluetooth('No new device found!')
            return

        for addr, name in devices:
            if BluetoothService.__convert_to_dict(name, addr) not in self.devices_in_range:
                self.__add_device__(name, addr)

    def __add_device__(self, name: str, bd_address: str) -> None:
        print_bluetooth('Found new device \"%s\"!' % name)

        if not self.db_service.bd_addr_exists(bd_address):
            print_bluetooth('\tDevice not registered!')
            return

        self.devices_in_range.append(BluetoothService.__convert_to_dict(name, bd_address))
        print_bluetooth('\tAdded new device: ')
        print_bluetooth('\tName: %s' % name)
        print_bluetooth('\tBD address: %s' % bd_address)

    def __remove_device__(self, name: str, bd_address: str) -> None:
        print_bluetooth('Found old device!')
        self.devices_in_range.remove(BluetoothService.__convert_to_dict(name, bd_address))
        print_bluetooth('\tRemoved device: ')
        print_bluetooth('\tName: %s' % name)
        print_bluetooth('\tBD address: %s' % bd_address)

    @staticmethod
    def __convert_to_dict(name: str, bd_address: str) -> dict:
        return dict({'name': name, 'bd_addr': bd_address})
