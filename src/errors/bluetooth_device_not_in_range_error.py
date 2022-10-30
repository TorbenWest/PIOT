class BluetoothDeviceNotInRangeError(Exception):
    def __init__(self) -> None:
        super().__init__('Bluetooth device not in range!')
