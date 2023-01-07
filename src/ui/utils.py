from typing import Union

import customtkinter
from customtkinter import CTkButton, CTkToplevel, CTk

font_label_form: tuple[str, int] = ('Roboto', 20)
font_textbox: tuple[str, int] = ('Roboto', 20)
font_label_frame_header: tuple[str, int] = ('Roboto', 25)
font_label_window_header: tuple[str, int] = ('Roboto', 35)


def center_window(window, width: int, height: int) -> None:
    app_center_coordinate_x = (window.winfo_screenwidth() / 2) - (width / 2)
    app_center_coordinate_y = (window.winfo_screenheight() / 2) - (height / 2)
    window.geometry(f"{width}x{height}+{int(app_center_coordinate_x)}+{int(app_center_coordinate_y)}")


def create_toplevel(root: CTk, width: int, height: int, title: str = '', resizable: bool = False) -> CTkToplevel:
    window = customtkinter.CTkToplevel(root)
    window.title(f'The Smart Door - {title}')
    window.grab_set()
    center_window(window, width, height)
    if not resizable:
        window.resizable(width=False, height=False)
    return window


def cancel_button(root: Union[CTk, CTkToplevel], text: str = 'Cancel', row: int = 0, column: int = 1,
                  padding_x: int = 0) -> CTkButton:
    button: CTkButton = customtkinter.CTkButton(root, text=text, width=70, fg_color='gray74',
                                                hover_color='#EEE', text_color='#000', command=lambda: root.destroy())
    button.grid(row=row, column=column, padx=padding_x, pady=(0, 5), sticky='es')
    return button
