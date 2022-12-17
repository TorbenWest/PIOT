from customtkinter import CTk

from database_service import DatabaseService


class UIController:

    def __int__(self):
        pass

    # def __init__(self, db_service: DatabaseService):
    #     self.db_service = db_service

    def login_user(self, window: CTk, username: str, password: str, navigate_to) -> None:
        pass
        # user_id = self.db_service.get_user_id(username, password)
        #
        # if user_id == -1:
        #     # TODO TopLevel Dialog
        #     pass
        # else:
        #     window.destroy()
        #     navigate_to(user_id)

    def register(self):
        pass

    def settings(self):
        pass

    def activate(self):
        pass

    def deactivate(self):
        pass

    def delete(self):
        pass

    def users(self):
        pass
