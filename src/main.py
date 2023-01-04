import asyncio
import getopt
import sys

from periodic import Periodic
from services.bluetooth_service import BluetoothService
from services.config_service import ConfigService
from services.database_service import MySqlConnector, DatabaseService
from services.microphone_service import MicrophoneService
from ui.app import App


def frontend(event_loop):
    config_service = ConfigService()
    connector = MySqlConnector(config_service.database_config)
    db_service = DatabaseService(connector.con)
    bt_service = BluetoothService(db_service)
    bluetooth_periodic = Periodic(lambda: bt_service.scan(config_service.bluetooth_config.get('discover_duration')),
                                  config_service.bluetooth_config.get('scan_interval'))

    # await bluetooth_periodic.start()
    # await asyncio.sleep(30)
    app = App(event_loop, bluetooth_periodic, db_service, connector)
    # async_mainloop(app)
    app.mainloop()


async def backend():
    config_service = ConfigService()
    connector = MySqlConnector(config_service.database_config)
    db_service = DatabaseService(connector.con)
    bt_service = BluetoothService(db_service)
    m_service = MicrophoneService(bt_service)

    bluetooth_periodic = Periodic(lambda: bt_service.scan(config_service.bluetooth_config.get('discover_duration')),
                                  config_service.bluetooth_config.get('scan_interval'))

    microphone = Periodic(lambda: m_service.listen(), 0.1)

    try:
        await bluetooth_periodic.start()
        await microphone.start()

        await asyncio.sleep(120)

        await bluetooth_periodic.stop()
        await microphone.stop()
        connector.close_connection()
    finally:
        await bluetooth_periodic.stop()
        await microphone.stop()
        connector.close_connection()


if __name__ == '__main__':
    argv = sys.argv[1:]

    try:
        opts, args = getopt.getopt(argv, "hbf", ["backend", "frontend"])
    except getopt.GetoptError:
        print('main.py -b')
        print('main.py -f')
        sys.exit(2)

    for opt, arg in opts:
        if opt == '-h':
            print('main.py -b')
            print('main.py -f')
            sys.exit(2)
        elif opt in ("-b", "--backend"):
            loop = asyncio.get_event_loop()
            loop.run_until_complete(backend())
        elif opt in ("-f", "--frontend"):
            loop = asyncio.get_event_loop()
            # loop.run_until_complete(frontend(loop))
            frontend(loop)
