from database_service import MySqlConnector, MySqlService
from bluetooth_service import BluetoothService

# Database
connector = MySqlConnector()
db_service = MySqlService(connector.con)

bt_service = BluetoothService(db_service)
bt_service.scan()

# db_service.insert_user(("torben", "password123", "A8:AB:B5:DC:DC:BF"), ("open", "close", "lock", "unlock"))

# bt_service.scan()
connector.close_connection()
