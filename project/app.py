from config import Config


class App:
    def __init__(self):
        self.config = Config()


def create_app() -> None:
    """Initialize the app, register blueprints and intialize all libraries"""
    return App()
