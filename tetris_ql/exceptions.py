class GameNotFoundException(Exception):
    def __init__(self, *args):
        self.message = args[0] if args else None

    def __str__(self):
        if self.message:
            return f"GameNotFound, {self.message}"
        else:
            return "GameNotFound has been raised."

