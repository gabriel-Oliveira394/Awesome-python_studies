class Circle:

    def __init__(self, radius, color):
        self.radius = radius
        self.color = color


my_circle = Circle(6, "Yellow")
print(my_circle.radius)
print(my_circle.color)

my_circle.radius = 15
my_circle.color = "black"
print(my_circle.radius)
print(my_circle.color)