# from PIL import Image

import customtkinter

from ui.utils import cancel_button, create_toplevel, \
    font_label_window_header, font_label_form, \
    font_label_frame_header, font_textbox


class Windows:

    # TODO Show password button
    @staticmethod
    def login(app, navigate_to):
        window = create_toplevel(app, 400, 230, 'Login')

        # - Frame Login - #
        frame_login = customtkinter.CTkFrame(master=window, corner_radius=10)
        frame_login.grid(row=0, column=0, padx=15, pady=20)

        # Label username
        label_username = customtkinter.CTkLabel(frame_login, text='Username:', width=30, font=font_label_frame_header,
                                                height=25, corner_radius=7)
        label_username.grid(row=0, column=0, padx=10, pady=20)

        # Entry username
        entry_username = customtkinter.CTkEntry(frame_login, placeholder_text='Enter Username', width=200, height=30,
                                                border_width=2, corner_radius=10)
        entry_username.grid(row=0, column=1, padx=10, columnspan=2)

        # Label password
        label_password = customtkinter.CTkLabel(frame_login, text='Password:', width=30, font=font_label_frame_header,
                                                height=25, corner_radius=7)
        label_password.grid(row=1, column=0, padx=10, pady=5, sticky='e')

        # Entry password
        entry_password = customtkinter.CTkEntry(frame_login, placeholder_text='Enter Password', width=200, height=30,
                                                border_width=2, corner_radius=10, show='*')
        entry_password.grid(row=1, column=1, padx=10, pady=20, columnspan=2)

        # Button show / hide password
        # image_path = os.path.join(os.path.dirname(os.path.realpath(__file__)), '../resources/images')
        # show_pw_image = customtkinter.CTkImage(Image.open(os.path.join(image_path, 'CustomTkinter_logo_single.png')), size=(26, 26))
        # button_show_hide_password = customtkinter.CTkButton(window, width=30, image=show_pw_image, command=lambda: print())
        # button_show_hide_password.grid(row=1, column=2, padx=10, pady=20, sticky='e')

        # Button login
        button_login = customtkinter.CTkButton(window, text='Login', width=70, command=lambda: app.controller
                                               .login_user(app, window, entry_username.get(), entry_password.get(),
                                                           navigate_to))
        button_login.grid(row=2, column=0, padx=100, pady=(0, 5), sticky='e')

        # Button cancel
        cancel_button(root=window, row=2, column=0, padding_x=20)

    # TODO Make it resizable
    @staticmethod
    def popup(app, title: str, text: str):
        window = create_toplevel(app, 280, 150, title)

        customtkinter.CTkLabel(window, text=text, width=30, font=font_label_frame_header,
                               height=25, corner_radius=7, wraplength=250) \
            .grid(row=0, column=0, columnspan=2, padx=10, pady=(10, 5), sticky='w')

        cancel_button(root=window, text='Ok', row=1, padding_x=10)

    @staticmethod
    def register(app):
        Windows._user_ctk(app)

    @staticmethod
    def settings(app):
        Windows._user_ctk(app, user=app.db_service.get_user(app.controller.user_id))

    @staticmethod
    def _user_ctk(app, user=None) -> None:
        """
        This method handles the register and settings functionality.
        """
        devices: list = app.bt_service.devices_in_range_registrable.copy()
        device_entry = None

        if user is not None:
            device_entry = app.bt_service.get_bluetooth_device_entry(user.get('user_id'))
            if not device_entry:
                Windows.popup(app, 'Settings', 'Please activate Bluetooth on your device and keep it nearby!')
                return
            devices.append(device_entry)

        names: list = [devices[i].get('name') for i in range(len(devices))]

        if len(names) == 0:
            Windows.popup(app, 'Bluetooth devices', 'No Bluetooth devices found... Please activate your device!')
            return

        entry_width: int = 250
        padding_x: int = 10
        frame_width: int = entry_width + 2 * padding_x
        frame_padding_x: int = 15
        total_width: int = 2 * frame_width + 4 * frame_padding_x

        window = create_toplevel(app, total_width, 465, 'Register')

        # Label heading
        customtkinter.CTkLabel(window, text='Register An Account', width=30,
                               font=font_label_window_header,
                               height=25, corner_radius=7).grid(row=0, column=0, columnspan=2, padx=padding_x, pady=5)

        # - Left Frame - #
        left_frame_login = customtkinter.CTkFrame(master=window, corner_radius=10, width=frame_width)
        left_frame_login.grid(row=1, column=0, padx=frame_padding_x, pady=10, rowspan=7, sticky='nsew')
        left_frame_login.grid_rowconfigure(7, weight=1)

        # Label user settings
        customtkinter.CTkLabel(left_frame_login, text='User Settings', width=30,
                               font=font_label_frame_header,
                               height=25, corner_radius=7).grid(row=0, column=0, padx=padding_x, pady=(5, 5))

        # Label username
        customtkinter.CTkLabel(left_frame_login, text='Username:', width=30, font=font_label_form,
                               height=25, corner_radius=7).grid(row=1, column=0, padx=padding_x, pady=(15, 5),
                                                                sticky='w')

        # Entry username
        entry_username = customtkinter.CTkEntry(left_frame_login, placeholder_text='Enter Username', width=entry_width,
                                                height=30, border_width=2, corner_radius=10)
        entry_username.grid(row=2, column=0, padx=padding_x, sticky='w')

        # Label password
        customtkinter.CTkLabel(left_frame_login, text='Password:', width=30, font=font_label_form,
                               height=25, corner_radius=7).grid(row=3, column=0, padx=padding_x, pady=(55, 5),
                                                                sticky='w')

        # Entry password
        entry_password = customtkinter.CTkEntry(left_frame_login, placeholder_text='Enter Password', width=entry_width,
                                                height=30, border_width=2, corner_radius=10, show='*')
        entry_password.grid(row=4, column=0, padx=padding_x, sticky='w')

        # Label bluetooth device
        customtkinter.CTkLabel(left_frame_login, text='Select Bluetooth Device:', width=30,
                               font=font_label_form,
                               height=25, corner_radius=7).grid(row=5, column=0, padx=padding_x, pady=(55, 5),
                                                                sticky='w')

        # Entry bluetooth device
        entry_bluetooth_device = customtkinter.CTkOptionMenu(left_frame_login, dynamic_resizing=True,
                                                             values=names, width=entry_width)
        entry_bluetooth_device.grid(row=6, column=0, padx=padding_x, pady=(0, 15), sticky='w')
        # - Left Frame - #

        # - Right Frame - #
        right_frame_login = customtkinter.CTkFrame(master=window, corner_radius=10, width=frame_width)
        right_frame_login.grid(row=1, column=1, padx=frame_padding_x, pady=10, rowspan=9, sticky='nsew')
        right_frame_login.grid_rowconfigure(9, weight=1)

        # Label command settings
        customtkinter.CTkLabel(right_frame_login, text='Command Settings', width=30,
                               font=font_label_frame_header,
                               height=25, corner_radius=7).grid(row=0, column=0, padx=padding_x, pady=(5, 5))

        # Label open
        customtkinter.CTkLabel(right_frame_login, text='Open:', width=30, font=font_label_form,
                               height=25, corner_radius=7).grid(row=1, column=0, padx=padding_x, pady=(15, 5),
                                                                sticky='w')

        # Entry open
        entry_open = customtkinter.CTkEntry(right_frame_login, placeholder_text='Enter open command',
                                            width=entry_width,
                                            height=30,
                                            border_width=2, corner_radius=10)
        entry_open.grid(row=2, column=0, padx=padding_x, sticky='w')

        # Label close
        customtkinter.CTkLabel(right_frame_login, text='Close:', width=30, font=font_label_form,
                               height=25, corner_radius=7).grid(row=3, column=0, padx=padding_x, pady=(15, 5),
                                                                sticky='w')

        # Entry close
        entry_close = customtkinter.CTkEntry(right_frame_login, placeholder_text='Enter close command',
                                             width=entry_width,
                                             height=30,
                                             border_width=2, corner_radius=10)
        entry_close.grid(row=4, column=0, padx=padding_x, sticky='w')

        # Label lock
        customtkinter.CTkLabel(right_frame_login, text='Lock:', width=30, font=font_label_form,
                               height=25, corner_radius=7).grid(row=5, column=0, padx=padding_x, pady=(15, 5),
                                                                sticky='w')

        # Entry lock
        entry_lock = customtkinter.CTkEntry(right_frame_login, placeholder_text='Enter lock command',
                                            width=entry_width,
                                            height=30,
                                            border_width=2, corner_radius=10)
        entry_lock.grid(row=6, column=0, padx=padding_x, sticky='w')

        # Label unlock
        customtkinter.CTkLabel(right_frame_login, text='Unlock:', width=30, font=font_label_form,
                               height=25, corner_radius=7).grid(row=7, column=0, padx=padding_x, pady=(15, 5),
                                                                sticky='w')

        # Entry unlock
        entry_unlock = customtkinter.CTkEntry(right_frame_login, placeholder_text='Enter unlock command',
                                              width=entry_width,
                                              height=30,
                                              border_width=2, corner_radius=10)
        entry_unlock.grid(row=8, column=0, padx=padding_x, pady=(0, 15), sticky='w')

        # Fill in values if "Settings" was selected
        if user is not None:
            entry_username.insert(0, user.get('username'))
            entry_open.insert(0, user.get('cmd_open'))
            entry_close.insert(0, user.get('cmd_close'))
            entry_lock.insert(0, user.get('cmd_lock'))
            entry_unlock.insert(0, user.get('cmd_unlock'))
            entry_bluetooth_device.set(device_entry.get('name'))

        # Button submit
        button_submit = customtkinter.CTkButton(window, text='Submit', width=70,
                                                command=lambda: app.controller.user_ctk(app, window, devices,
                                                                                        entry_username.get(),
                                                                                        entry_password.get(),
                                                                                        entry_bluetooth_device.get(),
                                                                                        (entry_open.get(),
                                                                                         entry_close.get(),
                                                                                         entry_lock.get(),
                                                                                         entry_unlock.get()),
                                                                                        user is not None))
        button_submit.grid(row=10, column=0, padx=frame_padding_x, pady=(0, 5), sticky='ws')

        # Button cancel
        cancel_button(root=window, row=10, padding_x=frame_padding_x)

    @staticmethod
    def delete(app):
        window = create_toplevel(app, 280, 150, 'Confirmation')
        Windows._pop_up_window(window, 'Are you sure you want to delete your account?',
                               lambda: app.controller.delete(app, window))

    @staticmethod
    def activate(app):
        window = create_toplevel(app, 280, 150, 'Confirmation')
        Windows._pop_up_window(window, 'Are you sure you want to activate your account?',
                               lambda: app.controller.activate(app, window))

    @staticmethod
    def deactivate(app):
        window = create_toplevel(app, 280, 150, 'Confirmation')
        Windows._pop_up_window(window, 'Are you sure you want to deactivate your account?',
                               lambda: app.controller.deactivate(app, window))

    @staticmethod
    def users(app):
        entry_width: int = 220
        padding_x: int = 10
        frame_width: int = entry_width + 2 * padding_x
        frame_padding_x: int = 15
        total_width: int = 2 * frame_width + 4 * frame_padding_x

        window = create_toplevel(app, total_width, 410, 'Registered Users')

        # Label heading
        customtkinter.CTkLabel(window, text='Registered Users', width=30,
                               font=font_label_window_header,
                               height=25, corner_radius=7).grid(row=0, column=0, columnspan=2, padx=padding_x, pady=5)

        # - Left Frame - #
        left_frame_login = customtkinter.CTkFrame(master=window, corner_radius=10, width=frame_width)
        left_frame_login.grid(row=1, column=0, padx=frame_padding_x, pady=10, rowspan=2, sticky='nsew')
        left_frame_login.grid_rowconfigure(2, weight=1)

        # Label activated users
        customtkinter.CTkLabel(left_frame_login, text='Activated Users', width=30,
                               font=font_label_frame_header,
                               height=25, corner_radius=7).grid(row=0, column=0, padx=padding_x, pady=(10, 20))

        # Textbox activated users
        textbox_activated_users = customtkinter.CTkTextbox(left_frame_login, width=200, font=font_textbox)
        textbox_activated_users.grid(row=1, column=0, padx=20, pady=20, sticky='nsew')
        app.controller.users(textbox_activated_users, True)

        # - Right Frame - #
        right_frame_login = customtkinter.CTkFrame(master=window, corner_radius=10, width=frame_width)
        right_frame_login.grid(row=1, column=1, padx=frame_padding_x, pady=10, rowspan=2, sticky='nsew')
        right_frame_login.grid_rowconfigure(2, weight=1)

        # Label deactivated users
        customtkinter.CTkLabel(right_frame_login, text='Deactivated Users', width=30,
                               font=font_label_frame_header,
                               height=25, corner_radius=7).grid(row=0, column=0, padx=padding_x, pady=(10, 20))

        # Textbox activated users
        textbox_deactivated_users = customtkinter.CTkTextbox(right_frame_login, width=200, font=font_textbox)
        textbox_deactivated_users.grid(row=1, column=0, padx=20, pady=20, sticky='nsew')
        app.controller.users(textbox_deactivated_users, False)

        # Button back
        cancel_button(root=window, text='Back', row=3, padding_x=frame_padding_x)

    @staticmethod
    def _pop_up_window(window, text: str, action):
        # Label to confirm
        customtkinter.CTkLabel(window, text=text, width=30, font=font_label_frame_header,
                               height=25, corner_radius=7, wraplength=250) \
            .grid(row=0, column=0, columnspan=2, padx=10, pady=(10, 5), sticky='w')

        # Button confirm
        customtkinter.CTkButton(window, text='Confirm', width=70, command=action) \
            .grid(row=1, column=0, padx=10, pady=(0, 10), sticky='ws')

        # Button cancel
        cancel_button(root=window, row=1, padding_x=10)
