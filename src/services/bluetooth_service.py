from typing import Union

import bluetooth

from services.console_service import print_bluetooth
from services.database_service import DatabaseService


class BluetoothService:
    """This list contains all devices that are related to an account and nearby!"""
    devices_in_range: list[dict[str, str]] = []

    """This list contains all devices that are not related to an account and nearby!"""
    devices_in_range_registrable: list[dict[str, str]] = []

    def __init__(self, service: DatabaseService) -> None:
        self.db_service: DatabaseService = service

    # https://github.com/pybluez/pybluez
    def scan(self, duration: int) -> None:
        print_bluetooth('Scanning for bluetooth devices...')
        # All devices that are nearby
        devices = bluetooth.discover_devices(duration=duration, lookup_names=True)

        # Remove device from "devices_in_range" if it was added before but now too far away
        for current in self.devices_in_range:
            if not any(device[0] == current.get('bd_addr') for device in devices):
                self._remove_device(current.get('name'), current.get('bd_addr'))

        # Remove device from "devices_in_range_registrable" if it was added before but now too far away
        for current in self.devices_in_range_registrable:
            if not any(device[0] == current.get('bd_addr') for device in devices):
                self.devices_in_range_registrable.remove(BluetoothService._convert_to_dict(current.get('name'),
                                                                                           current.get('bd_addr')))
        # If no devices are nearby; nothing to add
        if len(devices) == 0:
            print_bluetooth('No new device found!')
            return

        # Check whether new devices are nearby
        for addr, name in devices:
            if BluetoothService._convert_to_dict(name, addr) not in self.devices_in_range:
                self._add_device(name, addr)

    def register(self, device_name: str, bd_addr: str) -> None:
        self.devices_in_range_registrable.remove(self._convert_to_dict(device_name, bd_addr))
        self.devices_in_range.append(self._convert_to_dict(device_name, bd_addr))

    def update(self, old_device_entry: dict[str, str], new_device_name: str, new_bd_addr: str) -> None:
        self.register(new_device_name, new_bd_addr)
        self.delete(old_device_entry)

    def delete(self, device_entry: dict[str, str]) -> None:
        self.devices_in_range.remove(device_entry)
        self.devices_in_range_registrable.append(device_entry)

    def get_bluetooth_device_entry(self, user_id: int) -> Union[dict[str, str], bool]:
        user = self.db_service.get_user(user_id)
        user_bd_name = None

        for device in self.devices_in_range.copy():
            if device.get('bd_addr') == user.get('bd_addr'):
                user_bd_name = device.get('name')

        if user_bd_name is None:
            return False

        return self._convert_to_dict(user_bd_name, user.get('bd_addr'))

    def _add_device(self, name: str, bd_address: str) -> None:
        entry: dict = BluetoothService._convert_to_dict(name, bd_address)
        print_bluetooth('Found new device \"%s\"!' % name)

        if not self.db_service.bd_addr_exists(bd_address):
            if entry not in self.devices_in_range_registrable:
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
    def _convert_to_dict(name: str, bd_address: str) -> dict[str, str]:
        return dict({'name': name, 'bd_addr': bd_address})
