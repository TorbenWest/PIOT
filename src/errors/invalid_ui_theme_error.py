class InvalidUIThemeError(Exception):
    def __init__(self, theme: str) -> None:
        super().__init__(f'Unknown theme: {theme}')
