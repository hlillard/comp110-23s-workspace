"""File to define River class."""
__author__ = "730476613"

from exercises.ex09.fish import Fish
from exercises.ex09.bear import Bear


class River:
    """Gives River class day, fish, and bear, attributes."""
    day: int = 0
    fish: list = []
    bears: list = []
    
    def __init__(self, num_fish: int, num_bears: int):
        """New River with num_fish Fish and num_bears Bears."""
        self.day: int = 0
        self.fish: list[Fish] = []
        self.bears: list[Bear] = []
        for x in range(0, num_fish):
            self.fish.append(Fish())
        for x in range(0, num_bears):
            self.bears.append(Bear())   

    def bears_eating(self):
        """Defines what happens when a bear eats certain number of fish."""
        for bear in self.bears:
            if len(self.fish) >= 5:
                bear.eat(3)
                self.remove_fish(3)
        return None
    
    def check_hunger(self):
        """Removes Bears that have starved from the bears list by checking hunger_scores."""
        survived_bears: Bear = []
        for bear in self.bears:
            if bear.hunger_score >= 0:
                survived_bears.append(bear)
        self.bears = survived_bears    

    def check_ages(self):
        """Removes fish from River if older than 3 years."""
        bears_survived: Bear = []
        fish_survived: Fish = []
        for fish in self.fish: 
            if fish.age <= 3:
                fish_survived.append(fish)     
        for bear in self.bears: 
            if bear.age <= 5:
                bears_survived.append(bear)
        self.bears = bears_survived
        self.fish = fish_survived

    def repopulate_fish(self):
        """Increases fish population by 2 per fish pair."""
        increase_fish = Fish()
        num_fish_pair = (len(self.fish) // 2) * 4
        for f in range(num_fish_pair):
            self.fish.append(increase_fish)
    
    def repopulate_bears(self):
        """Increases the population of bears.""" 
        increase_bear = Bear()
        num_bpears = len(self.bears) // 2
        for b in range(num_bpears):
            self.bears.append(increase_bear)

    def view_river(self):
        """Allows us to view day number, fish population, and bear population."""
        print(f"~~~ Day {self.day}: ~~~")
        print(f"Fish population: {len(self.fish)}")
        print(f"Bear population: {len(self.bears)}")
        return None   

    def one_river_day(self):
        """Simulates one day in the river."""
        # Increase day by 1
        self.day += 1
        # Simulate one day for all Bears
        for bear in self.bears:
            bear.one_day()
        # Simulate one day for all Fish
        for fish in self.fish:
            fish.one_day()
        # Simulate Bear's eating
        self.bears_eating()
        # Remove hungry Bear's from River
        self.check_hunger()
        # Remove old Fish and Bear's from River
        self.check_ages()
        # Simulate Fish repopulation
        self.repopulate_fish()
        # Simulate Bear repopulation
        self.repopulate_bears()
        # Visualize River
        self.view_river()

    def one_river_week(self) -> None:
        """Calls one_river_day() seven times."""
        for d in range(7):
            self.one_river_day()

    def remove_fish(self, amount: int) -> None:
        """Remove amount many Fish from River."""
        for f in range(amount):
            self.fish.pop(f)     