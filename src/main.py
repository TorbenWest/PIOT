import asyncio

from bluetooth_service import BluetoothService
from config_service import ConfigService
from database_service import MySqlConnector, DatabaseService
from microphone_service import MicrophoneService
from periodic import Periodic


async def main():
    ConfigService.read()
    connector = MySqlConnector()
    db_service = DatabaseService(connector.con)

    # db_service.get_commands_for_bd_addresses(['A8:AB:B5:DC:DC:BF'])
    # db_service.insert_user(("torben", "password123", "A8:AB:B5:DC:DC:BF"), ("open", "close", "lock", "unlock"))

    bt_service = BluetoothService(db_service)
    m_service = MicrophoneService(bt_service)
    p = Periodic(lambda: bt_service.scan(), ConfigService.bluetooth_config.get('scan_interval'))

    try:
        await p.start()
        await asyncio.sleep(30)
        m_service.match_word('close')
        await p.stop()
        connector.close_connection()
    finally:
        await p.stop()


if __name__ == '__main__':
    loop = asyncio.get_event_loop()
    loop.run_until_complete(main())
