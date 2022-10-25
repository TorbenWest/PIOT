# https://www.geeksforgeeks.org/print-colors-python-terminal/

def print_bluetooth(msg):
    print(f"{_begin()}\033[96mBluetooth{_end() + msg}")


def print_database(msg):
    print(f"{_begin()}\033[95mDatabase{_end() + msg}")


def print_microphone(msg):
    print(f"{_begin()}\033[92mMicrophone{_end() + msg}")


def print_door(msg):
    print(f"{_begin()}\033[91mDoor{_end() + msg}")


def print_config(msg):
    print(f"{_begin()}\033[33mConfig{_end() + msg}")


def _begin() -> str:
    return '\033[90m['


def _end() -> str:
    return '\033[90m]\033[00m '
