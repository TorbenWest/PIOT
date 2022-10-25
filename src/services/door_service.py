from database_service import DatabaseService
from console_service import print_door


class DoorService:

    def __init__(self, database_service: DatabaseService) -> None:
        self.d_service: DatabaseService = database_service

    def open(self, user_id: int) -> None:
        self.d_service.insert_interaction_log(user_id, "cmd_open")
        print_door(f'User {user_id} opened the door!')

    def close(self, user_id: int) -> None:
        self.d_service.insert_interaction_log(user_id, "cmd_close")
        print_door(f'User {user_id} closed the door!')

    def lock(self, user_id: int) -> None:
        self.d_service.insert_interaction_log(user_id, "cmd_lock")
        print_door(f'User {user_id} locked the door!')

    def unlock(self, user_id: int) -> None:
        self.d_service.insert_interaction_log(user_id, "cmd_unlock")
        print_door(f'User {user_id} unlocked the door!')
