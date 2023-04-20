"""File to define Fish class."""


class Fish:
    """Give fish the attribute age which is an integer."""
    age: int = 0

    def __init__(self):
        """Modify __init__ so that it initializes self.age with the value 0."""
        self.age: int = 0
    
    def one_day(self):
        """Increases fish age."""
        self.age += 1