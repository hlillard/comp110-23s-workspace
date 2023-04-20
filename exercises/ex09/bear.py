"""File to define Bear class."""


class Bear:
    """Create and initialize a class to represent the bears living by the river."""
    age: int = 0
    hunger_score: int = 0

    def __init__(self):
        """Modify __init__ so that it initializes both self.age and hunger_score with the value 0."""
        self.age: int = 0
        hunger_score: int = 0
    
    def one_day(self):
        """Increases bear age and decreases hunger score."""
        self.age += 1
        hunger_score -= 1
    
    def eat(self, num_fish: int) -> None:
        """Update the Bear’s hunger_score so that it increases by num_fish."""
        hunger_score += num_fish