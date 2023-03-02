"""Practice with lists."""

x:list[str] = ["Comp", "110"]
x[1] = "210"
y: list[str] = x
print(y)
#diagram this later

a: str = "24"
b: str = a
a += "6"
print(b)
#diagram

a: list[int] = [2,4]
b: list[int] = a
a.append(6)
print(b)
#diagram