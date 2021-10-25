# from file import Klass
from animal import Animal

# instance / object
dog = Animal(name='Lizzy', age=3)
cat = Animal(name='Zorka', age=10)
bird = Animal(name='Fufu', age=5)

print(dog.speak())
print(cat.speak())
print(bird.speak())


print(bird.intro())
print(dog.intro())
print(cat.intro())