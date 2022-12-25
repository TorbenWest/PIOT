from customtkinter import CTk

from database_service import DatabaseService


class UIController:

    def __init__(self, db_service: DatabaseService):
        self.db_service = db_service
        self.user_id = -1

    def login_user(self, root: CTk, window: CTk, username: str, password: str, navigate_to, on_failure) -> None:
        user_id = self.db_service.get_user_id(username, password)

        if user_id == -1:
            on_failure(root)
        else:
            window.destroy()
            navigate_to(root)

    def register(self):
        pass

    def settings(self):
        pass

    def activate(self):
        pass

    def deactivate(self):
        pass

    def delete(self):
        print('Delete')
        pass

    def users(self):
        pass
