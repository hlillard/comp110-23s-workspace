""""Practice Instantiating Pizza Class"""

from lessons.pizza import Pizza

my_pizza: Pizza()
my_pizza.size = "large"
my_pizza.toppings = 1
my_pizza.gluten_free = False

print(Pizza)
print(my_pizza)
print(my_pizza.size)
