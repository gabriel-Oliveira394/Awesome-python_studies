'''
Instructions
You're going to write some code to help you cook a gorgeous lasagna from your favorite cookbook.

You have five tasks, all related to cooking your recipe.

1. Define expected bake time in minutes
2. Calculate remaining bake time in minutes
3. Calculate preparation time in minutes
4. Calculate total elapsed cooking time (prep + bake) in minutes
'''


class Lasagna:
    EXPECTED_BAKE_TIME = 40

    def bake_time_remaining(self, time_passed):
        self.time_passed = time_passed
        print(f'Tempo para ficar pronto: {self.expected_bake_time - self.time_passed}.')

    def preparation_time_in_minutes(self, layers):
        self.layers = layers
        print(f'The preparation time is: {self.layers * 2}')

    def elapsed_time_in_minutes(self):




def main():
    lasagna_1 = Lasagna()
    print(f'Tempo de preparo: {lasagna_1.expected_bake_time}')
    lasagna_1.bake_time_remaining(30)
    lasagna_1.preparation_time_in_minutes(2)


if __name__ == '__main__':
    main()