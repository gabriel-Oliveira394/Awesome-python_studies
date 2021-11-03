class Circle:

    def __init__(self, radius=5):
        self.radius = radius
        self.color = 'Blue'


my_circle = Circle(10)
your_circle = Circle()
print(my_circle)

print(f'My radius: {my_circle.radius}')
print(f'Your radius: {your_circle.radius}')
