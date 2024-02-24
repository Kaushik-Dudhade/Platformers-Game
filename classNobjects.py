class Human:
    def __init__(self, name, age, gender, height, weight):
        self.name = name
        self.age = age
        self.gender = gender
        self.height = height
        self.weight = weight

    def introduce_self(self):
        print('Hello, My name is ', self.name, '.')
        print('I am ', self.age, ' years old.')
        print('I am a', self.gender, '.')
        print('My height is', self.height, 'and my weight is', self.weight, 'Kg .')


human_1 = Human('Kaushik', 18, 'male', 175, 70)

human_2 = Human('Pradnya', 26, 'female', 165, 55)

human_1.introduce_self()
print()
human_2.introduce_self()