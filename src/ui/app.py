import customtkinter

from ui.ui_controller import UIController
from ui.windows import Windows

customtkinter.set_appearance_mode("System")  # Modes: "System" (standard), "Dark", "Light"
customtkinter.set_default_color_theme("blue")  # Themes: "blue" (standard), "green", "dark-blue"


# https://github.com/TomSchimansky/CustomTkinter
# https://www.youtube.com/watch?v=vEfrIpj2NNw
class App(customtkinter.CTk):
    def __init__(self):
        super().__init__()
        self.controller = UIController()

        app_width = 700
        app_height = 500

        # Configure grid layout (3x2)
        self.grid_columnconfigure((0, 1), weight=1)
        self.grid_rowconfigure((0, 1, 2), weight=1)

        # Set Window to appear int the middle when program runs
        app_center_coordinate_x = (self.winfo_screenwidth() / 2) - (app_width / 2)
        app_center_coordinate_y = (self.winfo_screenheight() / 2) - (app_height / 2)

        # Configure window
        self.title("The Smart Door")
        self.geometry(f"{app_width}x{app_height}+{int(app_center_coordinate_x)}+{int(app_center_coordinate_y)}")
        # self.resizable(width=False, height=False)

        self.main_frame = customtkinter.CTkFrame(self, corner_radius=10)
        self.main_frame.grid(sticky="nsew", rowspan=3, columnspan=2, padx=15, pady=20)
        self.main_frame.grid_rowconfigure(3, weight=1)

        # Buttons
        self._create_button('Register', 0.04, 0.05, lambda: Windows.register(self))
        self._create_button('Delete', 0.52, 0.05, lambda: Windows.login(self, self.controller.delete))
        self._create_button('Settings', 0.04, 0.375, lambda: Windows.login(self, self.controller.settings))
        self._create_button('Activate', 0.52, 0.375, lambda: Windows.login(self, self.controller.activate))
        self._create_button('Users', 0.04, 0.7, lambda: Windows.users(self))
        self._create_button('Deactivate', 0.52, 0.7, lambda: Windows.login(self, self.controller.deactivate))
        # self.button_register = customtkinter.CTkButton(self.main_frame, text="Register",
        #                                                border_width=border_width,
        #                                                corner_radius=corner_radius,
        #                                                font=font)
        # self.button_register.place(relx=0.04, rely=0.05, relwidth=0.4, relheight=0.3)

        # Button login
        # button_delete = customtkinter.CTkButton(self.main_frame, text="Delete")#, width=button_width, height=50)
        # button_delete.grid(row=0, column=1, padx=10, pady=10, sticky='nsew')
        #
        # # Button login
        # button_settings = customtkinter.CTkButton(self.main_frame, text="Settings")#, width=button_width, height=50)
        # button_settings.grid(row=1, column=0, padx=10, pady=10, sticky='nsew')
        #
        # # Button login
        # button_activate = customtkinter.CTkButton(self.main_frame, text="Activate")#, width=button_width, height=50)
        # button_activate.grid(row=1, column=1, padx=10, pady=10, sticky='nsew')

        # Use CTkButton instead of tkinter Button
        # button = customtkinter.CTkButton(master=self, text="CTkButton",
        #                                  command=lambda: login_window(self, self.on_exit))
        # button.place(relx=0.5, rely=0.5, anchor=tkinter.CENTER)

        self.protocol('WM_DELETE_WINDOW', self.on_exit)

    def change_scaling_event(self, new_scaling: str):
        new_scaling_float = int(new_scaling.replace("%", "")) / 100
        customtkinter.set_widget_scaling(new_scaling_float)

    def on_exit(self):
        # TODO Stop Bluetooth service and close database connection
        self.destroy()

    def _create_button(self, text: str, relx: float, rely: float, command):
        button = customtkinter.CTkButton(self.main_frame, text=text,
                                         border_width=2,
                                         corner_radius=8,
                                         font=('Roboto', 50),
                                         command=command)
        button.place(relx=relx, rely=rely, relwidth=0.44, relheight=0.25)


if __name__ == "__main__":
    app = App()
    app.mainloop()
