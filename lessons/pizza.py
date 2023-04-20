"""Define Pizza Classs"""

class Pizza:

    #attributes
    size: str = #"small" or "large"
    toppings: int
    gluten_free: bool

    def __init__(self, size_input: str, topping_input: int, gluten_free_input: bool):
        self.size = size_input
        self.toppings = topping_input
        self.gluten_free = gluten_free_input