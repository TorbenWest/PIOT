import customtkinter

from ui.ui_controller import UIController
from ui.utils import center_window
from ui.windows import Windows

customtkinter.set_appearance_mode("Dark")  # Modes: "System" (standard), "Dark", "Light"
customtkinter.set_default_color_theme("dark-blue")  # Themes: "blue" (standard), "green", "dark-blue"


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

        # Configure window
        self.title("The Smart Door")
        center_window(self, app_width, app_height)

        self.main_frame = customtkinter.CTkFrame(self, corner_radius=10)
        self.main_frame.grid(sticky="nsew", rowspan=3, columnspan=2, padx=15, pady=20)
        self.main_frame.grid_rowconfigure(3, weight=1)

        # Buttons
        self._create_button('Register', 0.04, 0.05, lambda: Windows.register(self))
        self._create_button('Delete', 0.52, 0.05, lambda: Windows.login(self, Windows.delete))
        self._create_button('Settings', 0.04, 0.375, lambda: Windows.login(self, Windows.settings))
        self._create_button('Activate', 0.52, 0.375, lambda: Windows.login(self, Windows.activate))
        self._create_button('Users', 0.04, 0.7, lambda: Windows.users(self))
        self._create_button('Deactivate', 0.52, 0.7, lambda: Windows.login(self, Windows.deactivate))
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