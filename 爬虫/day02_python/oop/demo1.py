class Persion():
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def show(self):
        print(f'name={self.name},age={self.age}')
        print(f'self={self}')


persion = Persion('猪八戒', 18)
persion2 = Persion('猪八戒', 18)

print(type(persion))
print(persion)
print(persion2)

persion.show()
persion2.show()

