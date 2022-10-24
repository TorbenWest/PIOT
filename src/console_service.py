# https://www.geeksforgeeks.org/print-colors-python-terminal/

def print_bluetooth(msg):
    print("\033[97m[\033[96mBluetooth\033[97m]\033[00m {}".format(msg))


def print_database(msg):
    print("\033[97m[\033[95mDatabase\033[97m]\033[00m {}".format(msg))


def print_microphone(msg):
    print("\033[97m[\033[92mMicrophone\033[97m]\033[00m {}".format(msg))
