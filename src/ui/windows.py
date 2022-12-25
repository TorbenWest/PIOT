# from PIL import Image

import customtkinter

from ui.utils import cancel_button, create_toplevel, font_label_window_header, font_label_form, font_label_frame_header


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
                                                           navigate_to, Windows.login_failed))
        button_login.grid(row=2, column=0, padx=100, pady=(0, 5), sticky='e')

        # Button cancel
        cancel_button(root=window, row=2, column=0, padding_x=20)

    @staticmethod
    def login_failed(app):
        window = create_toplevel(app, 280, 150, 'Login failed')

        customtkinter.CTkLabel(window, text='Incorrect password or username!', width=30, font=font_label_frame_header,
                               height=25, corner_radius=7, wraplength=250) \
            .grid(row=0, column=0, columnspan=2, padx=10, pady=(10, 5), sticky='w')

        cancel_button(root=window, text='Ok', row=1, padding_x=10)

    @staticmethod
    def register(app):
        entry_width: int = 250
        padding_x: int = 10
        frame_width: int = entry_width + 2 * padding_x
        frame_padding_x: int = 15
        total_width: int = 2 * frame_width + 4 * frame_padding_x

        window = create_toplevel(app, total_width, 510, 'Register')

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
                               height=25, corner_radius=7).grid(row=0, column=0, padx=padding_x, pady=(10, 20))

        # Label username
        customtkinter.CTkLabel(left_frame_login, text='Username:', width=30, font=font_label_form,
                               height=25, corner_radius=7).grid(row=1, column=0, padx=padding_x, pady=(20, 5),
                                                                sticky='w')

        # Entry username
        entry_username = customtkinter.CTkEntry(left_frame_login, placeholder_text='Enter Username', width=entry_width,
                                                height=30,
                                                border_width=2, corner_radius=10)
        entry_username.grid(row=2, column=0, padx=padding_x, sticky='w')

        # Label password
        customtkinter.CTkLabel(left_frame_login, text='Password:', width=30, font=font_label_form,
                               height=25, corner_radius=7).grid(row=3, column=0, padx=padding_x, pady=(60, 5),
                                                                sticky='w')

        # Entry password
        entry_password = customtkinter.CTkEntry(left_frame_login, placeholder_text='Enter Password', width=entry_width,
                                                height=30,
                                                border_width=2, corner_radius=10, show='*')
        entry_password.grid(row=4, column=0, padx=padding_x, sticky='w')

        # Label bluetooth device
        customtkinter.CTkLabel(left_frame_login, text='Select Bluetooth Device:', width=30,
                               font=font_label_form,
                               height=25, corner_radius=7).grid(row=5, column=0, padx=padding_x, pady=(60, 5),
                                                                sticky='w')

        # Entry bluetooth device
        # TODO Entries!!
        entry_bluetooth_device = customtkinter.CTkOptionMenu(left_frame_login, dynamic_resizing=True,
                                                             values=['Value 1', 'Value 2', 'Value Long Long Long'],
                                                             width=entry_width)
        entry_bluetooth_device.grid(row=6, column=0, padx=padding_x, pady=(0, 15), sticky='w')
        # - Left Frame - #

        # - Right Frame - #
        right_frame_login = customtkinter.CTkFrame(master=window, corner_radius=10, width=frame_width)
        right_frame_login.grid(row=1, column=1, padx=frame_padding_x, pady=10, rowspan=9, sticky='nsew')
        right_frame_login.grid_rowconfigure(9, weight=1)

        # Label command settings
        customtkinter.CTkLabel(right_frame_login, text='Command Settings', width=30,
                               font=font_label_frame_header,
                               height=25, corner_radius=7).grid(row=0, column=0, padx=padding_x, pady=(10, 20))

        # Label open
        customtkinter.CTkLabel(right_frame_login, text='Open:', width=30, font=font_label_form,
                               height=25, corner_radius=7).grid(row=1, column=0, padx=padding_x, pady=(20, 5),
                                                                sticky='w')

        # Entry open
        entry_open = customtkinter.CTkEntry(right_frame_login, placeholder_text='Enter open command',
                                            width=entry_width,
                                            height=30,
                                            border_width=2, corner_radius=10)
        entry_open.grid(row=2, column=0, padx=padding_x, sticky='w')

        # Label close
        customtkinter.CTkLabel(right_frame_login, text='Close:', width=30, font=font_label_form,
                               height=25, corner_radius=7).grid(row=3, column=0, padx=padding_x, pady=(20, 5),
                                                                sticky='w')

        # Entry close
        entry_close = customtkinter.CTkEntry(right_frame_login, placeholder_text='Enter close command',
                                             width=entry_width,
                                             height=30,
                                             border_width=2, corner_radius=10)
        entry_close.grid(row=4, column=0, padx=padding_x, sticky='w')

        # Label lock
        customtkinter.CTkLabel(right_frame_login, text='Lock:', width=30, font=font_label_form,
                               height=25, corner_radius=7).grid(row=5, column=0, padx=padding_x, pady=(20, 5),
                                                                sticky='w')

        # Entry lock
        entry_lock = customtkinter.CTkEntry(right_frame_login, placeholder_text='Enter lock command',
                                            width=entry_width,
                                            height=30,
                                            border_width=2, corner_radius=10)
        entry_lock.grid(row=6, column=0, padx=padding_x, sticky='w')

        # Label unlock
        customtkinter.CTkLabel(right_frame_login, text='Unlock:', width=30, font=font_label_form,
                               height=25, corner_radius=7).grid(row=7, column=0, padx=padding_x, pady=(20, 5),
                                                                sticky='w')

        # Entry unlock
        entry_unlock = customtkinter.CTkEntry(right_frame_login, placeholder_text='Enter unlock command',
                                              width=entry_width,
                                              height=30,
                                              border_width=2, corner_radius=10)
        entry_unlock.grid(row=8, column=0, padx=padding_x, pady=(0, 15), sticky='w')

        # Button submit
        button_submit = customtkinter.CTkButton(window, text='Submit', width=70, command=lambda: print('Submit'))
        button_submit.grid(row=10, column=0, padx=frame_padding_x, pady=(0, 5), sticky='ws')

        # Button cancel
        cancel_button(root=window, row=10, padding_x=frame_padding_x)

    @staticmethod
    def delete(app):
        Windows._pop_up_window(app, 'Are you sure you want to delete your account?', app.controller.delete)

    @staticmethod
    def settings(app):
        pass

    @staticmethod
    def activate(app):
        Windows._pop_up_window(app, 'Are you sure you want to activate your account?', app.controller.activate)

    @staticmethod
    def deactivate(app):
        Windows._pop_up_window(app, 'Are you sure you want to deactivate your account?', app.controller.deactivate)

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
        textbox_activated_users = customtkinter.CTkTextbox(left_frame_login, width=200, state='disabled')
        textbox_activated_users.grid(row=1, column=0, padx=20, pady=20, sticky='nsew')
        # TODO Load accounts
        # textbox_activated_users.insert("0.0", "new text to insert")

        # - Right Frame - #
        right_frame_login = customtkinter.CTkFrame(master=window, corner_radius=10, width=frame_width)
        right_frame_login.grid(row=1, column=1, padx=frame_padding_x, pady=10, rowspan=2, sticky='nsew')
        right_frame_login.grid_rowconfigure(2, weight=1)

        # Label deactivated users
        customtkinter.CTkLabel(right_frame_login, text='Deactivated Users', width=30,
                               font=font_label_frame_header,
                               height=25, corner_radius=7).grid(row=0, column=0, padx=padding_x, pady=(10, 20))

        # Textbox activated users
        textbox_deactivated_users = customtkinter.CTkTextbox(right_frame_login, width=200, state='disabled')
        textbox_deactivated_users.grid(row=1, column=0, padx=20, pady=20, sticky='nsew')
        # TODO Load accounts
        # textbox_deactivated_users.insert("0.0", "new text to insert")

        # Button back
        cancel_button(root=window, text='Back', row=3, padding_x=frame_padding_x)

    @staticmethod
    def _pop_up_window(app, text: str, action):
        window = create_toplevel(app, 280, 150, 'Confirmation')

        # Label to confirm
        customtkinter.CTkLabel(window, text=text, width=30, font=font_label_frame_header,
                               height=25, corner_radius=7, wraplength=250) \
            .grid(row=0, column=0, columnspan=2, padx=10, pady=(10, 5), sticky='w')

        # Button confirm
        customtkinter.CTkButton(window, text='Confirm', width=70, command=action) \
            .grid(row=1, column=0, padx=10, pady=(0, 10), sticky='ws')

        # Button cancel
        cancel_button(root=window, row=1, padding_x=10)
