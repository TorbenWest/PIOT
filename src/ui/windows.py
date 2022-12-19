# from PIL import Image

import customtkinter

from ui.utils import center_window


class Windows:

    # TODO Show password button
    @staticmethod
    def login(app, navigate_to):
        window = customtkinter.CTkToplevel(app)
        window.resizable(width=False, height=False)
        window.grab_set()
        window.title("Login")
        center_window(window, 400, 230)

        # - Frame Login - #
        frame_login = customtkinter.CTkFrame(master=window, corner_radius=10)
        frame_login.grid(row=0, column=0, padx=15, pady=20)

        # Label username
        label_username = customtkinter.CTkLabel(frame_login, text="Username:", width=30, font=("Roboto", 24),
                                                height=25, corner_radius=7)
        label_username.grid(row=0, column=0, padx=10, pady=20)

        # Entry username
        entry_username = customtkinter.CTkEntry(frame_login, placeholder_text="Enter Username", width=200, height=30,
                                                border_width=2, corner_radius=10)
        entry_username.grid(row=0, column=1, padx=10, columnspan=2)

        # Label password
        label_password = customtkinter.CTkLabel(frame_login, text="Password:", width=30, font=("Roboto", 24),
                                                height=25, corner_radius=7)
        label_password.grid(row=1, column=0, padx=10, pady=5, sticky='e')

        # Entry password
        entry_password = customtkinter.CTkEntry(frame_login, placeholder_text="Enter Password", width=200, height=30,
                                                border_width=2, corner_radius=10, show='*')
        entry_password.grid(row=1, column=1, padx=10, pady=20, columnspan=2)

        # Button show / hide password
        # image_path = os.path.join(os.path.dirname(os.path.realpath(__file__)), "../resources/images")
        # show_pw_image = customtkinter.CTkImage(Image.open(os.path.join(image_path, "CustomTkinter_logo_single.png")), size=(26, 26))
        # button_show_hide_password = customtkinter.CTkButton(window, width=30, image=show_pw_image, command=lambda: print())
        # button_show_hide_password.grid(row=1, column=2, padx=10, pady=20, sticky='e')

        # Button login
        button_login = customtkinter.CTkButton(window, text="Login", width=70, command=lambda: app.controller
                                               .login_user(app, window, entry_username.get(), entry_password.get(),
                                                           navigate_to))
        button_login.grid(row=2, column=0, padx=100, sticky='e')

        # Button cancel
        button_cancel = customtkinter.CTkButton(window, text="Cancel", width=70, fg_color='gray74',
                                                hover_color='#EEE', text_color='#000', command=lambda: window.destroy())
        button_cancel.grid(row=2, column=0, padx=20, sticky='e')

    @staticmethod
    def register(app):
        label_font: tuple = ("Roboto", 20)
        entry_width: int = 250
        padding_x: int = 10
        frame_width: int = entry_width + 2 * padding_x
        frame_padding_x: int = 15
        total_width: int = 2 * frame_width + 4 * frame_padding_x

        window = customtkinter.CTkToplevel(app)
        window.resizable(width=False, height=False)
        window.title("Register")
        window.grab_set()
        center_window(window, total_width, 510)

        # Label heading
        label_heading = customtkinter.CTkLabel(window, text="Register An Account", width=30,
                                               font=("Roboto", 35),
                                               height=25, corner_radius=7)
        label_heading.grid(row=0, column=0, columnspan=2, padx=padding_x, pady=5)

        # - Left Frame - #
        left_frame_login = customtkinter.CTkFrame(master=window, corner_radius=10, width=frame_width)
        left_frame_login.grid(row=1, column=0, padx=frame_padding_x, pady=10, rowspan=7, sticky="nsew")
        left_frame_login.grid_rowconfigure(7, weight=1)

        # Label user settings
        label_user_settings = customtkinter.CTkLabel(left_frame_login, text="User Settings", width=30,
                                                     font=("Roboto", 25),
                                                     height=25, corner_radius=7)
        label_user_settings.grid(row=0, column=0, padx=padding_x, pady=(10, 20))

        # Label username
        label_username = customtkinter.CTkLabel(left_frame_login, text="Username:", width=30, font=label_font,
                                                height=25, corner_radius=7)
        label_username.grid(row=1, column=0, padx=padding_x, pady=(20, 5), sticky="w")

        # Entry username
        entry_username = customtkinter.CTkEntry(left_frame_login, placeholder_text="Enter Username", width=entry_width,
                                                height=30,
                                                border_width=2, corner_radius=10)
        entry_username.grid(row=2, column=0, padx=padding_x, sticky="w")

        # Label password
        label_password = customtkinter.CTkLabel(left_frame_login, text="Password:", width=30, font=label_font,
                                                height=25, corner_radius=7)
        label_password.grid(row=3, column=0, padx=padding_x, pady=(60, 5), sticky="w")

        # Entry password
        entry_password = customtkinter.CTkEntry(left_frame_login, placeholder_text="Enter Password", width=entry_width,
                                                height=30,
                                                border_width=2, corner_radius=10, show='*')
        entry_password.grid(row=4, column=0, padx=padding_x, sticky="w")

        # Label bluetooth device
        label_bluetooth_device = customtkinter.CTkLabel(left_frame_login, text="Select Bluetooth Device:", width=30,
                                                        font=label_font,
                                                        height=25, corner_radius=7)
        label_bluetooth_device.grid(row=5, column=0, padx=padding_x, pady=(60, 5), sticky="w")

        # Entry bluetooth device
        # TODO Entries!!
        entry_bluetooth_device = customtkinter.CTkOptionMenu(left_frame_login, dynamic_resizing=True,
                                                             values=["Value 1", "Value 2", "Value Long Long Long"],
                                                             width=entry_width)
        entry_bluetooth_device.grid(row=6, column=0, padx=padding_x, pady=(0, 15), sticky="w")
        # - Left Frame - #

        # - Right Frame - #
        right_frame_login = customtkinter.CTkFrame(master=window, corner_radius=10, width=frame_width)
        right_frame_login.grid(row=1, column=1, padx=frame_padding_x, pady=10, rowspan=9, sticky="nsew")
        right_frame_login.grid_rowconfigure(9, weight=1)

        # Label command settings
        label_command_settings = customtkinter.CTkLabel(right_frame_login, text="Command Settings", width=30,
                                                        font=("Roboto", 25),
                                                        height=25, corner_radius=7)
        label_command_settings.grid(row=0, column=0, padx=padding_x, pady=(10, 20))

        # Label open
        label_open = customtkinter.CTkLabel(right_frame_login, text="Open:", width=30, font=label_font,
                                            height=25, corner_radius=7)
        label_open.grid(row=1, column=0, padx=padding_x, pady=(20, 5), sticky="w")

        # Entry open
        entry_open = customtkinter.CTkEntry(right_frame_login, placeholder_text="Enter open command",
                                            width=entry_width,
                                            height=30,
                                            border_width=2, corner_radius=10)
        entry_open.grid(row=2, column=0, padx=padding_x, sticky="w")

        # Label close
        label_close = customtkinter.CTkLabel(right_frame_login, text="Close:", width=30, font=label_font,
                                             height=25, corner_radius=7)
        label_close.grid(row=3, column=0, padx=padding_x, pady=(20, 5), sticky="w")

        # Entry close
        entry_close = customtkinter.CTkEntry(right_frame_login, placeholder_text="Enter close command",
                                             width=entry_width,
                                             height=30,
                                             border_width=2, corner_radius=10)
        entry_close.grid(row=4, column=0, padx=padding_x, sticky="w")

        # Label lock
        label_lock = customtkinter.CTkLabel(right_frame_login, text="Lock:", width=30, font=label_font,
                                            height=25, corner_radius=7)
        label_lock.grid(row=5, column=0, padx=padding_x, pady=(20, 5), sticky="w")

        # Entry lock
        entry_lock = customtkinter.CTkEntry(right_frame_login, placeholder_text="Enter lock command",
                                            width=entry_width,
                                            height=30,
                                            border_width=2, corner_radius=10)
        entry_lock.grid(row=6, column=0, padx=padding_x, sticky="w")

        # Label unlock
        label_unlock = customtkinter.CTkLabel(right_frame_login, text="Unlock:", width=30, font=label_font,
                                              height=25, corner_radius=7)
        label_unlock.grid(row=7, column=0, padx=padding_x, pady=(20, 5), sticky="w")

        # Entry unlock
        entry_unlock = customtkinter.CTkEntry(right_frame_login, placeholder_text="Enter unlock command",
                                              width=entry_width,
                                              height=30,
                                              border_width=2, corner_radius=10)
        entry_unlock.grid(row=8, column=0, padx=padding_x, pady=(0, 15), sticky="w")

        # Button submit
        button_submit = customtkinter.CTkButton(window, text="Submit", width=70, command=lambda: print('Submit'))
        button_submit.grid(row=10, column=0, padx=frame_padding_x, pady=(0, 5), sticky='ws')

        # Button cancel
        button_cancel = customtkinter.CTkButton(window, text="Cancel", width=70, fg_color='gray74',
                                                hover_color='#EEE', text_color='#000', command=lambda: window.destroy())
        button_cancel.grid(row=10, column=1, padx=frame_padding_x, pady=(0, 5), sticky='es')

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
        entry_width: int = 250
        padding_x: int = 10
        frame_width: int = entry_width + 2 * padding_x
        frame_padding_x: int = 15
        total_width: int = 2 * frame_width + 4 * frame_padding_x

        window = customtkinter.CTkToplevel(app)
        window.resizable(width=False, height=False)
        window.title("Registered Users")
        window.grab_set()
        center_window(window, total_width, 510)

        # Label heading
        label_heading = customtkinter.CTkLabel(window, text="Registered Users", width=30,
                                               font=("Roboto", 35),
                                               height=25, corner_radius=7)
        label_heading.grid(row=0, column=0, columnspan=2, padx=padding_x, pady=5)

        # - Left Frame - #
        left_frame_login = customtkinter.CTkFrame(master=window, corner_radius=10, width=frame_width)
        left_frame_login.grid(row=1, column=0, padx=frame_padding_x, pady=10, rowspan=2, sticky="nsew")
        left_frame_login.grid_rowconfigure(2, weight=1)

        # Label activated users
        label_activated_users = customtkinter.CTkLabel(left_frame_login, text="Activated Users", width=30,
                                                     font=("Roboto", 25),
                                                     height=25, corner_radius=7)
        label_activated_users.grid(row=0, column=0, padx=padding_x, pady=(10, 20))

        # Textbox activated users
        textbox_activated_users = customtkinter.CTkTextbox(window, width=200)
        textbox_activated_users.grid(row=1, column=0, padx=(20, 0), pady=(20, 0), sticky="nsew")

        # - Right Frame - #
        right_frame_login = customtkinter.CTkFrame(master=window, corner_radius=10, width=frame_width)
        right_frame_login.grid(row=1, column=1, padx=frame_padding_x, pady=10, rowspan=2, sticky="nsew")
        right_frame_login.grid_rowconfigure(2, weight=1)

        # Label deactivated users
        label_deactivated_users = customtkinter.CTkLabel(right_frame_login, text="Deactivated Users", width=30,
                                                     font=("Roboto", 25),
                                                     height=25, corner_radius=7)
        label_deactivated_users.grid(row=0, column=0, padx=padding_x, pady=(10, 20))

    @staticmethod
    def _pop_up_window(app, text: str, action):
        window = customtkinter.CTkToplevel(app)
        window.resizable(width=False, height=False)
        window.title("Confirmation")
        window.grab_set()
        center_window(window, 280, 150)

        # Label to confirm
        customtkinter.CTkLabel(window, text=text, width=30, font=('Roboto', 24),
                               height=25, corner_radius=7, wraplength=250) \
            .grid(row=0, column=0, columnspan=2, padx=10, pady=(10, 5), sticky="w")

        # Button confirm
        customtkinter.CTkButton(window, text="Confirm", width=70, command=action) \
            .grid(row=1, column=0, padx=10, pady=(0, 10), sticky='ws')

        # Button cancel
        customtkinter.CTkButton(window, text="Cancel", width=70, fg_color='gray74',
                                hover_color='#EEE', text_color='#000', command=lambda: window.destroy()) \
            .grid(row=1, column=1, padx=10, pady=(0, 10), sticky='es')
