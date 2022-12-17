import os
# from PIL import Image

import customtkinter


class Windows:

    # TODO Show password button
    @staticmethod
    def login(app, navigate_to):
        window = customtkinter.CTkToplevel(app)
        window.resizable(width=False, height=False)
        window.geometry(f"{400}x{230}")
        window.title("Login")

        # - Frame Login - #
        frame_login = customtkinter.CTkFrame(master=window, corner_radius=10)
        frame_login.grid(row=1, column=0, padx=15, pady=20)

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
                                               .login_user(window, entry_username.get(), entry_password.get(),
                                                           navigate_to))
        button_login.grid(row=2, column=0, padx=100, sticky='e')

        # Button cancel
        button_cancel = customtkinter.CTkButton(window, text="Cancel", width=70, fg_color='gray74',
                                                hover_color='#EEE', text_color='#000', command=lambda: window.destroy())
        button_cancel.grid(row=2, column=0, padx=20, sticky='e')

    @staticmethod
    def register(app):
        pass

    @staticmethod
    def delete(app):
        pass

    @staticmethod
    def settings(app):
        pass

    @staticmethod
    def activate(app):
        pass

    @staticmethod
    def deactivate(app):
        pass

    @staticmethod
    def users(app):
        pass
