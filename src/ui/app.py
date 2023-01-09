import threading
import time

import customtkinter

from bluetooth_service import BluetoothService
from config_service import ConfigService
from database_service import DatabaseService
from ui.utils import center_window
from ui.windows import Windows
from ui.windows_controller import UIController


# https://github.com/TomSchimansky/CustomTkinter
# https://www.youtube.com/watch?v=vEfrIpj2NNw
class App(customtkinter.CTk):

    def __init__(self, bt_service: BluetoothService, db_service: DatabaseService, c_service: ConfigService) -> None:
        super().__init__()
        self.bt_service = bt_service
        self.db_service = db_service
        self.c_service = c_service
        self.main_frame = None
        self.controller = UIController(self.bt_service, self.db_service)
        customtkinter.set_appearance_mode(self.c_service.ui_config.get('appearance_mode'))
        customtkinter.set_default_color_theme(self.c_service.ui_config.get('color_theme'))

        app_width = 700
        app_height = 500

        self.grid_columnconfigure(0, weight=1)
        self.grid_rowconfigure((0, 1), weight=1)

        # Configure window
        self.title("The Smart Door")
        center_window(self, app_width, app_height)

        self.progressbar_frame = customtkinter.CTkFrame(self, corner_radius=10)
        self.progressbar_frame.grid(sticky="nsew", rowspan=2, columnspan=2, padx=15, pady=20)
        self.progressbar_frame.grid_rowconfigure(0, weight=1)
        self.progressbar = customtkinter.CTkProgressBar(self.progressbar_frame)
        self.progressbar.place(relx=0.1, rely=0.8, relwidth=0.80, relheight=0.05)
        self.protocol('WM_DELETE_WINDOW', self.destroy)

        self._thread = threading.Thread(target=self._update_progressbar)
        self._thread.start()

    def _update_progressbar(self):
        seconds: int = self.c_service.bluetooth_config.get('discover_duration') + 5

        t_start = time.time()
        t_end = t_start + seconds
        while time.time() < t_end:
            self.progressbar.set((time.time() - t_start) / seconds)

        self.progressbar_frame.destroy()
        self._main_window()

    def _main_window(self):
        # Configure grid layout (3x2)
        self.grid_columnconfigure((0, 1), weight=1)
        self.grid_rowconfigure((0, 1, 2), weight=1)

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

    def change_scaling_event(self, new_scaling: str) -> None:
        new_scaling_float = int(new_scaling.replace("%", "")) / 100
        customtkinter.set_widget_scaling(new_scaling_float)

    def _create_button(self, text: str, relx: float, rely: float, command) -> None:
        button = customtkinter.CTkButton(self.main_frame, text=text,
                                         border_width=2,
                                         corner_radius=8,
                                         font=('Roboto', 50),
                                         command=command)
        button.place(relx=relx, rely=rely, relwidth=0.44, relheight=0.25)
