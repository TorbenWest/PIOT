import asyncio
import sys
import getopt

from services.bluetooth_service import BluetoothService
from services.config_service import ConfigService
from services.database_service import MySqlConnector, DatabaseService
from services.microphone_service import MicrophoneService
from periodic import Periodic
from ui.main_ui import start_gui


async def main(argv: list) -> None:
    try:
        opts, args = getopt.getopt(argv, "hbf", ["backend", "frontend"])
    except getopt.GetoptError:
        print('main.py -b')
        print('main.py -f')
        sys.exit(2)

    config_service = ConfigService()
    connector = MySqlConnector(config_service.database_config)
    db_service = DatabaseService(connector.con)

    # db_service.get_commands_for_bd_addresses(['A8:AB:B5:DC:DC:BF'])
    # db_service.insert_user(("torben", "password123", "A8:AB:B5:DC:DC:BF"), ("open", "close", "lock", "unlock"))
    # db_service.insert_user(("Jord", "password123", "C0:DC:DA:96:FF:D1"), ("open", "close", "lock", "unlock"))
    # id = db_service.get_user('torben', 'password123')
    # print(id)

    bt_service = BluetoothService(db_service)
    m_service = MicrophoneService(bt_service)

    p = Periodic(lambda: bt_service.scan(config_service.bluetooth_config.get('discover_duration')),
                 config_service.bluetooth_config.get('scan_interval'))

    microphone = None

    for opt, arg in opts:
        if opt == '-h':
            print('main.py -b')
            print('main.py -f')
            sys.exit()
        elif opt in ("-b", "--backend"):
            microphone = Periodic(lambda: m_service.listen(), 0.1)
        elif opt in ("-f", "--frontend"):
            # print("No UI provided yet!")
            start_gui()
            sys.exit(2)
            # microphone = GUI()

    if microphone is None:
        print('main.py -b')
        print('main.py -f')
        sys.exit()

    try:
        await p.start()
        await microphone.start()

        await asyncio.sleep(120)

        await p.stop()
        await microphone.stop()
        connector.close_connection()
    finally:
        await p.stop()
        await microphone.stop()


if __name__ == '__main__':
    loop = asyncio.get_event_loop()
    loop.run_until_complete(main(sys.argv[1:]))
