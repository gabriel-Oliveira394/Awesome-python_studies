class Person:
    def __init__(self, name):
        self.name = name

    def about_me(self):
        print("My name is {}".format(self.name))
        print('My name is', self.name)
        print(f'My name is {self.name}')

    @staticmethod
    def speak(msg):
        print(msg)


d = Person('Gabriel')
d.about_me()
