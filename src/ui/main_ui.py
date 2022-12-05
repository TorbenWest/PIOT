import PySimpleGUI as sg
from PySimpleGUI import Button


def get_button(text: str) -> Button:
    return sg.Button(text, size=(10, 1), border_width=4, font=("Arial", 20), key='-%s-' % text.upper())

def get_text(text: str):
    return sg.Text(text, size=(15, 1))


# Horizontal layout
_layout = [
    [get_button('Register'), get_button('Delete')],
    [get_button('Settings'), get_button('Activate')],
    [get_button('Users'), get_button('Deactivate')]
]


def register_window():
    global values
    _layout_REGISTER = [
    [get_text('Username'), get_text('Open command')],
    [sg.Input(key='NEW_USER'), sg.Input(key='NEW_OPEN_COMMAND')],
    [get_text('Password'), get_text('Close command')],
    [sg.Input(key='NEW_PW'), sg.Input(key='NEW_CLOSE_COMMAND')],
    [get_text('Lock command'), get_text('Unlock command')],
    [sg.Input(key='NEW_LOCK_COMMAND'), sg.Input(key='NEW_UNLOCK_COMMAND')],
    [sg.Submit(), sg.Cancel()]
    ]

    REGISTER_window = sg.Window(title='Login', layout=_layout_REGISTER)
    
    while True:
        event, values = REGISTER_window.read()
        if event in (sg.WINDOW_CLOSED, "Cancel"):
            break
        elif event == "Submit":
            print(values['NEW_USER'])
            print(values['NEW_PW'])
        break
    REGISTER_window.close()


def login_window():
    global values
    _layout_LOGIN = [
    [get_text('Username')],
    [sg.Input(key='LOGIN_USERNAME')],
    [get_text('Password')],
    [sg.Input(key='LOGIN_PW', password_char='*')],
    [sg.Submit(), sg.Cancel()]
    ]

    LOGIN_window = sg.Window(title='Login', layout=_layout_LOGIN)
    print(values['NEW_USER'])
    print(values['NEW_PW'])
    while True:
        event, values = LOGIN_window.read()
        if event in (sg.WINDOW_CLOSED, "Cancel"):
            break
        elif event == "Submit":
            if values['LOGIN_USERNAME'] == values['NEW_USER'] and values['LOGIN_PW']== values['NEW_PW']:
                sg.popup("Welcome!")
                print(values['NEW_USER'])
                print(values['NEW_PW'])
                break
            elif values['LOGIN_PW'] != values['NEW_USER'] and values['LOGIN_PW'] != values['NEW_PW']:
                sg.popup("Invalid login. Try again")
                break
    LOGIN_window.close()


def delete_confirm_window():
    _layout_DELETE_CONFIRM = [
        [get_text('Are you sure you want to delete your account')],
        [sg.Submit(), sg.Cancel()]
    ]

    DELETE_CONFIRM_window = sg.Window(title='Delete account', layout=_layout_DELETE_CONFIRM)

    while True:
        event, values = DELETE_CONFIRM_window.read()
        if event in (sg.WINDOW_CLOSED, "Cancel"):
            break
        elif event == "Submit":
            values['NEW_USER'] =''
            values['NEW_PW']= ''
        break
    DELETE_CONFIRM_window.close()


def activate_confirm_window():
    _layout_ACTIVATE_CONFIRM = [
        [get_text('Are you sure you want to activate your account')],
        [sg.Submit(), sg.Cancel()]
    ]

    ACTIVATE_CONFIRM_window = sg.Window(title='Activate account', layout=_layout_ACTIVATE_CONFIRM)

    while True:
        event, values = ACTIVATE_CONFIRM_window.read()
        if event in (sg.WINDOW_CLOSED, "Cancel"):
            break
        elif event == "Submit":
            #*Code to activate user from database
            login_name = values['LOGIN_USERNAME']
            login_pw = values['LOGIN_PW']
        break
    ACTIVATE_CONFIRM_window.close()


def deactivate_confirm_window():
    _layout_DEACTIVATE_CONFIRM = [
        [get_text('Are you sure you want to deactivate your account')],
        [sg.Submit(), sg.Cancel()]
    ]

    DEACTIVATE_CONFIRM_window = sg.Window(title='Deactivate account', layout=_layout_DEACTIVATE_CONFIRM)

    while True:
        event, values = DEACTIVATE_CONFIRM_window.read()
        if event in (sg.WINDOW_CLOSED, "Cancel"):
            break
        elif event == "Submit":
            #*Code to remove user from database
            login_name = values['LOGIN_USERNAME']
            login_pw = values['LOGIN_PW']
        break
    DEACTIVATE_CONFIRM_window.close()


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
            register_window()
            
        if event == '-SETTINGS-':
            print('Settings')
            login_window()
            
        if event == '-USERS-':
            print('Users')
            login_window()

        if event == '-DELETE-':
            print('Delete')
            login_window()

        if event == '-ACTIVATE-':
            print('Activate')
            login_window()
        
        if event == '-DEACTIVATE-':
            print('Deactivate')
            login_window()

    window.close()

start_gui()