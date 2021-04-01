from django.test import TestCase


# Create your tests here.
class Dog:
    name = '黑背'

    def run(self):
        print('run')


dog = Dog()

print(getattr(dog, 'name'))

fun = getattr(dog, 'run')

fun()
dog.name = 'loli'
print(dog.name)
