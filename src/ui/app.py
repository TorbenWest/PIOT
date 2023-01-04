import customtkinter
import asyncio
import threading

from database_service import DatabaseService, MySqlConnector
from periodic import Periodic
from ui.ui_controller import UIController
from ui.utils import center_window
from ui.windows import Windows

# TODO Put in config file
customtkinter.set_appearance_mode("Dark")  # Modes: "System" (standard), "Dark", "Light"
customtkinter.set_default_color_theme("dark-blue")  # Themes: "blue" (standard), "green", "dark-blue"


# https://github.com/TomSchimansky/CustomTkinter
# https://www.youtube.com/watch?v=vEfrIpj2NNw
class App(customtkinter.CTk):
    def __init__(self, event_loop, bluetooth_periodic: Periodic, db_service: DatabaseService, connector: MySqlConnector) -> None:
        super().__init__()
        self.async_loop = event_loop
        self.bluetooth_periodic = bluetooth_periodic
        self.connector = connector
        self.controller = UIController(db_service)

        # async_handler(_run_async, lambda: self._start())
        # self._run_task(self._start)
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
        self.protocol('WM_DELETE_WINDOW', lambda: self._run_task(self._stop()))

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

    """Stopping Bluetooth Service"""
    def _run_task(self, func) -> None:
        threading.Thread(target=self._asyncio_thread, args=(func,)).start()
        self.destroy()

    def _asyncio_thread(self, func):
        self.async_loop.run_until_complete(func)

    async def _stop(self) -> None:
        await self.bluetooth_periodic.stop()
        self.connector.close_connection()

    async def _start(self) -> None:
        await self.bluetooth_periodic.start()
        await asyncio.sleep(30)
        await self.bluetooth_periodic.stop()
        self.connector.close_connection()
