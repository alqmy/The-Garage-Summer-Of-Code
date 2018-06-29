
class Animal:
    def __init__(self, height, weight):
        self.height = height
        self.weight = weight
    
    def walk(self):
        print("Animal of height {0} and weight {1} is walking".format(self.height, self.weight))

small_animal = Animal(1, 5)

print(small_animal.height)
print(small_animal.weight)

small_animal.walk()

large_animal = Animal(10, 400)
large_animal.walk()
small_animal.walk()