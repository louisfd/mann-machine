class AbstractClassException(NotImplementedError):
    def __init__(self):
        super().__init__("Sub-classes must implement this method")


class TODOException(NotImplementedError):
    def __init__(self):
        super().__init__("TODO!")
