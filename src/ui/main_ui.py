from typing import Union

import PySimpleGUI as sg
from PySimpleGUI import Button, Text

from bluetooth_service import BluetoothService
from database_service import DatabaseService


class UIService:

    def __init__(self, db_service: DatabaseService, bt_service: BluetoothService) -> None:
        self.user_id = -1
        self.db_service = db_service
        self.bt_service = bt_service

    def start(self) -> None:
        layout = [
            [self.get_button('Register'), self.get_button('Delete')],
            [self.get_button('Settings'), self.get_button('Activate')],
            [self.get_button('Users'), self.get_button('Deactivate')]
        ]
        window = sg.Window(title='The Smart Door', layout=layout)

        while True:
            event, values = window.read()

            if event == "OK" or event == sg.WIN_CLOSED:
                break

            if event == '-REGISTER-':
                print('Register')
                self.register_window()

            if event == '-SETTINGS-':
                print('Settings')
                self.login_window(self.settings_window)

            if event == '-USERS-':
                print('Users')
                self.login_window(lambda x: x)

            if event == '-DELETE-':
                print('Delete')
                self.login_window(self.delete_confirm_window)

            if event == '-ACTIVATE-':
                print('Activate')
                self.login_window(self.activate_confirm_window)

            if event == '-DEACTIVATE-':
                print('Deactivate')
                self.login_window(self.deactivate_confirm_window)

        window.close()

    # TODO Make bd address observe changes
    def register_window(self):
        devices: list = self.bt_service.devices_in_range_registrable.copy()
        names: list = [devices[i].get('name') for i in range(len(devices))]

        _layout_register = [
            [self.get_text('Username'), self.get_text('Open command')],
            [sg.Input(key='USER'), sg.Input(key='OPEN_COMMAND')],
            [self.get_text('Password'), self.get_text('Close command')],
            [sg.Input(key='PASSWORD'), sg.Input(key='CLOSE_COMMAND')],
            [self.get_text('Bluetooth Device'), self.get_text('Lock command')],
            [sg.Combo(key='BD_ADDRESS', values=names, size=(43, 1), readonly=True), sg.Input(key='LOCK_COMMAND')],
            [self.get_text('Unlock command')],
            [sg.Input(key='UNLOCK_COMMAND')],
            [sg.Submit(), sg.Cancel()]
        ]

        window = sg.Window(title='Login', layout=_layout_register)

        while True:
            event, values = window.read()
            if event in (sg.WINDOW_CLOSED, "Cancel"):
                break
            elif event == "Submit":
                username = values['USER']
                password = values['PASSWORD']
                device_name = values['BD_ADDRESS']

                # TODO Make check class or method
                if not 3 < len(username) < 16:
                    sg.popup("Username length is invalid!")
                    continue

                if self.db_service.username_exists(username):
                    sg.popup("Username already used!")
                    continue

                if len(password) < 8:
                    sg.popup("Password is too short!")
                    continue

                if self.db_service.bd_addr_exists(device_name):
                    sg.popup("Devices already used by another account!")
                    continue

                bd_addr: str = ''
                for device in devices:
                    if device.get('name') == device_name:
                        bd_addr = device.get('bd_addr')
                        break

                if len(bd_addr) == 0:
                    sg.popup("Registration failed")
                    continue

                self.db_service.insert_user((username, password, bd_addr),
                                            (values['OPEN_COMMAND'], values['CLOSE_COMMAND'],
                                             values['LOCK_COMMAND'], values['UNLOCK_COMMAND']))
                self.bt_service.devices_in_range_registrable.remove(dict({'name': device_name, 'bd_addr': bd_addr}))
                self.bt_service.devices_in_range.append(dict({'name': device_name, 'bd_addr': bd_addr}))
                sg.popup("User created!")
            break
        window.close()

    # TODO Make a bluetooth controller
    def _get_bluetooth_device_entry(self) -> Union[dict[str, str], bool]:
        user = self.db_service.get_user(self.user_id)
        user_bd_name = None

        for device in self.bt_service.devices_in_range.copy():
            if device.get('bd_addr') == user.get('bd_addr'):
                user_bd_name = device.get('name')

        if user_bd_name is None:
            sg.popup("Please activate Bluetooth on your device and keep it nearby!")
            return False

        return dict({'name': user_bd_name, 'bd_addr': user.get('bd_addr')})

    def settings_window(self):
        devices: list = self.bt_service.devices_in_range_registrable.copy()
        user = self.db_service.get_user(self.user_id)
        device_entry = self._get_bluetooth_device_entry()

        if not device_entry:
            return

        devices.append(device_entry)
        names: list = [devices[i].get('name') for i in range(len(devices))]

        _layout_register = [
            [self.get_text('Username'), self.get_text('Open command')],
            [sg.Input(key='USER', default_text=user.get('username')),
             sg.Input(key='OPEN_COMMAND', default_text=user.get('cmd_open'))],
            [self.get_text('Password'), self.get_text('Close command')],
            [sg.Input(key='PASSWORD'), sg.Input(key='CLOSE_COMMAND', default_text=user.get('cmd_close'))],
            [self.get_text('Bluetooth Device'), self.get_text('Lock command')],
            [sg.Combo(key='BD_ADDRESS', values=names, size=(43, 1), default_value=device_entry.get('name'),
                      readonly=True),
             sg.Input(key='LOCK_COMMAND', default_text=user.get('cmd_lock'))],
            [self.get_text('Unlock command')],
            [sg.Input(key='UNLOCK_COMMAND', default_text=user.get('cmd_unlock'))],
            [sg.Submit(), sg.Cancel()]
        ]

        window = sg.Window(title='Login', layout=_layout_register)

        while True:
            event, values = window.read()
            if event in (sg.WINDOW_CLOSED, "Cancel"):
                break
            elif event == "Submit":
                username = values['USER']
                password = values['PASSWORD']
                device_name = values['BD_ADDRESS']

                if not username == user.get('username'):
                    if not 3 < len(username) < 16:
                        sg.popup("Username length is invalid!")
                        continue

                    if self.db_service.username_exists(username):
                        sg.popup("Username already used!")
                        continue

                if len(password) < 8:
                    sg.popup("Password is too short!")
                    continue

                if self.db_service.bd_addr_exists(device_name):
                    sg.popup("Devices already used by another account!")
                    continue

                bd_addr: str = ''
                for device in devices:
                    if device.get('name') == device_name:
                        bd_addr = device.get('bd_addr')
                        break

                if len(bd_addr) == 0:
                    sg.popup("Updating failed")
                    continue

                self.db_service.update_user(self.user_id, (username, password, bd_addr),
                                            (values['OPEN_COMMAND'], values['CLOSE_COMMAND'],
                                             values['LOCK_COMMAND'], values['UNLOCK_COMMAND']))
                sg.popup("User updated!")
            break
        window.close()

    def login_window(self, forward_to):
        _layout_login = [
            [self.get_text('Username')],
            [sg.Input(key='LOGIN_USERNAME')],
            [self.get_text('Password')],
            [sg.Input(key='LOGIN_PW', password_char='*')],
            [sg.Submit(), sg.Cancel()]
        ]

        window = sg.Window(title='Login', layout=_layout_login)

        while True:
            event, values = window.read()
            if event in (sg.WINDOW_CLOSED, "Cancel"):
                window.close()
                return
            elif event == "Submit":
                self.user_id = self.db_service.get_user_id(values['LOGIN_USERNAME'], values['LOGIN_PW'])

                if self.user_id == -1:
                    sg.popup("Invalid login. Try again!")
                else:
                    break

        if not self.user_id == -1:
            window.close()
            forward_to()

    def delete_confirm_window(self):
        _layout_delete_confirm = [
            [self.get_text('Are you sure you want to delete your account?')],
            [sg.Submit(), sg.Cancel()]
        ]

        window = sg.Window(title='Delete account', layout=_layout_delete_confirm)

        while True:
            event, values = window.read()
            if event in (sg.WINDOW_CLOSED, "Cancel"):
                break
            elif event == "Submit":
                device_entry = self._get_bluetooth_device_entry()

                if not device_entry:
                    return

                self.db_service.delete_user(self.user_id)
                self.bt_service.devices_in_range.remove(device_entry)
                self.bt_service.devices_in_range_registrable.append(device_entry)
            break
        window.close()

    def activate_confirm_window(self):
        if self._check_account_activation(True):
            return

        _layout_activate_confirm = [
            [self.get_text('Are you sure you want to activate your account?')],
            [sg.Submit(), sg.Cancel()]
        ]

        window = sg.Window(title='Activate account', layout=_layout_activate_confirm)

        while True:
            event, values = window.read()
            if event in (sg.WINDOW_CLOSED, "Cancel"):
                break
            elif event == "Submit":
                self.db_service.change_account_activation(self.user_id, True)
            break
        window.close()

    def deactivate_confirm_window(self):
        if self._check_account_activation(False):
            return

        _layout_deactivate_confirm = [
            [self.get_text('Are you sure you want to deactivate your account?')],
            [sg.Submit(), sg.Cancel()]
        ]

        window = sg.Window(title='Deactivate account', layout=_layout_deactivate_confirm)

        while True:
            event, values = window.read()
            if event in (sg.WINDOW_CLOSED, "Cancel"):
                break
            elif event == "Submit":
                self.db_service.change_account_activation(self.user_id, False)
            break
        window.close()

    def _check_account_activation(self, activate: bool) -> bool:
        message: str = 'Your account is already activated!' if activate else 'Your account is already deactivated!'
        _layout_activated = [[self.get_text(message)], [sg.OK()]]

        if not self.db_service.is_user_activated(self.user_id) and activate:
            return False
        if self.db_service.is_user_activated(self.user_id) and not activate:
            return False

        window = sg.Window(title='Activate account', layout=_layout_activated)

        while True:
            event, values = window.read()
            if event in (sg.WINDOW_CLOSED, "Cancel"):
                break
            elif event == "OK":
                break

        window.close()
        return True

    def get_button(self, text: str) -> Button:
        return sg.Button(text, size=(10, 1), border_width=4, font=("Arial", 20), key='-%s-' % text.upper())

    def get_text(self, text: str) -> Text:
        return sg.Text(text, size=(40, 1))
