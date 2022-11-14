import PySimpleGUI as sg

_layout: list[list] = [
    [sg.Text('The Smart Door', justification='top')],
    [sg.Button('OK')]
]


def start_gui() -> None:
    sg.Window(title='The Smart Door', layout=_layout, margins=(360, 250)).read()
