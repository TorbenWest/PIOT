import hashlib
from datetime import datetime

import mysql.connector
from mysql.connector import errorcode

from console_service import print_database


# https://dev.mysql.com/doc/connector-python/en/connector-python-example-connecting.html
class MySqlConnector:

    def __init__(self) -> None:
        config = {
            'user': 'smartdoor',
            'password': 'c$7^tvMaT7q51tZ0kY0w',
            'host': '45.142.115.34',
            'port': '3306',
            'database': 'smartdoor',
            'raise_on_warnings': False
        }

        try:
            self.con = mysql.connector.connect(**config)
            self.cur = self.con.cursor(dictionary=True)
            print_database('Database connection established!')

            if self.__schema_already_exists():
                print_database('Schema already created!')
            else:
                print_database('Creating schema...')
                self.__execute_script()
                print_database('Successfully created schema!')
        except mysql.connector.Error as err:
            if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
                print_database('Something is wrong with your user name or password!')
            elif err.errno == errorcode.ER_BAD_DB_ERROR:
                print_database('Database does not exist!')
            else:
                print_database(err)

    # https://www.w3schools.com/python/python_mysql_select.asp
    def __schema_already_exists(self) -> bool:
        query: str = ("SELECT COUNT(*) AS count "
                      "FROM information_schema.tables "
                      "WHERE table_schema = 'smartdoor' "
                      "AND table_name IN ('sd_user', 'sd_user_commands', 'sd_user_interaction_log')")
        cursor: any = self.con.cursor()
        cursor.execute(query)
        rs: tuple = cursor.fetchone()
        cursor.close()
        return rs[0] == 3

    def __execute_script(self) -> None:
        with open('schema.sql', 'r') as sql_file:
            result_iterator = self.cur.execute(sql_file.read(), multi=True)
            for res in result_iterator:
                print_database(f'Running query: \n{res.statement}')
                print_database(f'Affected {res.rowcount} rows')

            self.con.commit()

    def close_connection(self) -> None:
        self.cur.close()
        self.con.close()
        print_database('Database connection closed!')


# https://datagy.io/python-append-to-tuple/
class MySqlService:

    def __init__(self, con) -> None:
        self.con = con

    # https://dev.mysql.com/doc/connector-python/en/connector-python-example-cursor-select.html
    def bd_addr_exists(self, bd_addr: str) -> bool:
        query: str = ("SELECT bd_addr FROM sd_user "
                      "WHERE bd_addr = %s")
        rs: list = self.__select(query, tuple([bd_addr]))
        return len(rs) == 1

    # Example usage: insert_user((username, password, bd_addr), (cmd_open, cmd_close, cmd_close, cmd_unlock))
    def insert_user(self, data_user: tuple, data_commands: tuple) -> None:
        # Define queries
        add_user: str = ("INSERT INTO sd_user "
                         "(username, hashed_password, bd_addr) "
                         "VALUES (%s, %s, %s)")
        add_commands: str = ("INSERT INTO sd_user_commands "
                             "(user_id, cmd_open, cmd_close, cmd_lock, cmd_unlock) "
                             "VALUES (%s, %s, %s, %s, %s)")

        # Hashing the password
        data_user_list: list = list(data_user)
        data_user_list[1]: str = MySqlService.hash_password(data_user_list[1])

        # Inserting values
        user_id: int = self.__insert(add_user, tuple(data_user_list))
        self.__insert(add_commands, (user_id,) + data_commands)

    # https://flexiple.com/python/python-timestamp/
    def insert_interaction_log(self, user_id: int, command: str) -> None:
        # Define query
        add_interaction_log: str = ("INSERT INTO sd_user_interaction_log "
                                    "(user_id, command, cmd_timestamp) "
                                    "VALUES (%s, %s, %s)")

        # Inserting values
        self.__insert(add_interaction_log, (user_id, command, datetime.fromtimestamp(datetime.now().timestamp())))

    # https://dev.mysql.com/doc/connector-python/en/connector-python-example-cursor-transaction.html
    def __insert(self, statement: str, data: tuple) -> int:
        # Get cursor
        self.con.reconnect()
        cursor: any = self.con.cursor()
        # Execute statement
        cursor.execute(statement, data)
        # Commit query
        self.con.commit()
        # Store last created id
        last_id: int = cursor.lastrowid
        # Close cursor
        cursor.close()
        # Return generated id
        return last_id

    def __select(self, statement: str, data: tuple) -> list:
        self.con.reconnect()
        cursor: any = self.con.cursor()
        cursor.execute(statement, data)
        rs: list = cursor.fetchall()
        cursor.close()
        return rs

    # https://blog.devgenius.io/password-hashing-with-python-f3148692e8b9
    @staticmethod
    def hash_password(password: str) -> str:
        return hashlib.sha3_256(password.encode()).hexdigest()
