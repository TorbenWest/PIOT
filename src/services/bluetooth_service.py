import bluetooth

from services.console_service import print_bluetooth
from services.database_service import DatabaseService


class BluetoothService:
    devices_in_range: list = []
    devices_in_range_registrable: list = []

    def __init__(self, service: DatabaseService) -> None:
        self.db_service: DatabaseService = service

    # https://github.com/pybluez/pybluez
    def scan(self, duration: int) -> None:
        print_bluetooth('Scanning for bluetooth devices...')
        devices = bluetooth.discover_devices(duration=duration, lookup_names=True)

        for current in self.devices_in_range:
            if not any(device[0] == current.get('bd_addr') for device in devices):
                self._remove_device(current.get('name'), current.get('bd_addr'))

        for current in self.devices_in_range_registrable:
            if not any(device[0] == current.get('bd_addr') for device in devices):
                self.devices_in_range.remove(BluetoothService._convert_to_dict(current.get('name'),
                                                                               current.get('bd_addr')))

        if len(devices) == 0:
            print_bluetooth('No new device found!')
            return

        for addr, name in devices:
            if BluetoothService._convert_to_dict(name, addr) not in self.devices_in_range:
                self._add_device(name, addr)

    def _add_device(self, name: str, bd_address: str) -> None:
        entry: dict = BluetoothService._convert_to_dict(name, bd_address)
        print_bluetooth('Found new device \"%s\"!' % name)

        if not self.db_service.bd_addr_exists(bd_address):
            if entry not in self.devices_in_range:
                self.devices_in_range_registrable.append(entry)
            print_bluetooth('\tDevice not registered!')
            return

        self.devices_in_range.append(entry)
        print_bluetooth('\tAdded new device: ')
        print_bluetooth('\tName: %s' % name)
        print_bluetooth('\tBD address: %s' % bd_address)

    def _remove_device(self, name: str, bd_address: str) -> None:
        print_bluetooth('Found old device!')
        self.devices_in_range.remove(BluetoothService._convert_to_dict(name, bd_address))
        print_bluetooth('\tRemoved device: ')
        print_bluetooth('\tName: %s' % name)
        print_bluetooth('\tBD address: %s' % bd_address)

    @staticmethod
    def _convert_to_dict(name: str, bd_address: str) -> dict:
        return dict({'name': name, 'bd_addr': bd_address})
