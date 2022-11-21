import PySimpleGUI as sg
from PySimpleGUI import Button


def get_button(text: str) -> Button:
    return sg.Button(text, size=(10, 1), border_width=4, font=("Arial", 20), key='-%s-' % text.upper())


# Horizontal layout
_layout = [
    [get_button('Register'), get_button('Delete')],
    [get_button('Settings'), get_button('Activate')],
    [get_button('Users'), get_button('Deactivate')]
]


def start_gui() -> None:
    # Create the window
    window = sg.Window(title='The Smart Door', layout=_layout)
    # Create an event loop
    while True:
        event, values = window.read()

        if event == "OK" or event == sg.WIN_CLOSED:
            break

        if event == '-REGISTER-':
            print('Register')
    window.close()
