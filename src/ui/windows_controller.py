from customtkinter import CTk, CTkTextbox

from bluetooth_service import BluetoothService
from database_service import DatabaseService
from ui.windows import Windows


class UIController:

    def __init__(self, bt_service: BluetoothService, db_service: DatabaseService):
        self.bt_service = bt_service
        self.db_service = db_service
        self.user_id = -1

    def reset_user(self) -> None:
        self.user_id = -1

    def login_user(self, root: CTk, window: CTk, username: str, password: str, navigate_to) -> None:
        self.user_id = self.db_service.get_user_id(username, password)

        if self.user_id == -1:
            Windows.popup(root, 'Login failed', 'Incorrect password or username!')
        else:
            window.destroy()
            navigate_to(root)

    def user_ctk(self, root: CTk, window: CTk, devices: list, username: str, password: str,
                 device_name: str, commands: tuple[str, str, str, str], update: bool) -> None:
        """This method handles the register and settings functionality."""
        user = self.db_service.get_user(self.user_id) if update else None

        if not 3 < len(username) < 16:
            Windows.popup(root, 'Username invalid', 'Username length is invalid!')
            return

        if (not update or update and not username == user.get('username')) \
                and self.db_service.username_exists(username):
            Windows.popup(root, 'Username invalid', 'Username already used!')
            return

        if len(password) < 8:
            Windows.popup(root, 'Password invalid', 'Password is too short!')
            return

        if self.db_service.bd_addr_exists(device_name):
            Windows.popup(root, 'Device invalid', 'Devices already used by another account!')
            return

        bd_addr: str = ''
        for device in devices:
            if device.get('name') == device_name:
                bd_addr = device.get('bd_addr')
                break

        if len(bd_addr) == 0:
            Windows.popup(root, 'Device invalid', 'Devices could not be determined!')
            return

        for command in commands:
            if len(command) == 0 or command.isspace():
                Windows.popup(root, 'Command invalid', 'Please fill out all command entries!')
                return

        if update:
            if not bd_addr == user.get('bd_addr'):
                old_device_entry = self.bt_service.get_bluetooth_device_entry(self.user_id)
                self.bt_service.update(old_device_entry, device_name, bd_addr)

            self.db_service.update_user(self.user_id, (username, password, bd_addr), commands)
            window.destroy()
            Windows.popup(root, 'Update Success', 'Your user account was updated successfully!')
        else:
            self.db_service.insert_user((username, password, bd_addr), commands)
            self.bt_service.register(device_name, bd_addr)
            window.destroy()
            Windows.popup(root, 'Registration Success', 'Your user account was created successfully!')

    def activate(self, root: CTk, window: CTk) -> None:
        if self.db_service.is_user_activated(self.user_id):
            Windows.popup(root, 'Activate account', 'Your account is already activated!')
        else:
            self.db_service.change_account_activation(self.user_id, True)
        self.reset_user()
        window.destroy()

    def deactivate(self, root: CTk, window: CTk) -> None:
        if not self.db_service.is_user_activated(self.user_id):
            Windows.popup(root, 'Activate account', 'Your account is already deactivated!')
        else:
            self.db_service.change_account_activation(self.user_id, False)
        self.reset_user()
        window.destroy()

    def delete(self, root: CTk, window: CTk) -> None:
        device_entry = self.bt_service.get_bluetooth_device_entry(self.user_id)

        if not device_entry:
            Windows.popup(root, 'Delete account', 'Please activate Bluetooth on your device and keep it nearby!')
            return

        self.db_service.delete_user(self.user_id)
        self.bt_service.delete(device_entry)
        self.reset_user()
        window.destroy()

    def users(self, textbox: CTkTextbox, is_activated: bool) -> None:
        users: list = [u for u in self.db_service.get_all_users() if u.get('is_activated') == int(is_activated)]

        if len(users) == 0:
            textbox.insert('0.0', 'No user found!')
        else:
            for i, user in enumerate(users):
                textbox.insert(f'{i}.0', user.get('username') + '\n')

        # If textbox is disabled, the "insert" function will also not work
        textbox.configure(state='disabled')
