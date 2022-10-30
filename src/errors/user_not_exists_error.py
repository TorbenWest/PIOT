class UserNotExistsError(Exception):
    def __init__(self, user_id: int) -> None:
        super().__init__(f'The user with the id {user_id} does not exists!')
