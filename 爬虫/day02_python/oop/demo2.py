class Animal():
    def __init__(self, age):
        self.age = age

    def show(self):
        print(self.age)


# 双下划线开头结尾为特殊函数或属性（__init__）
# 单线划线开头为保护属性（只有本身和子类可以访问）(_age)
# 双线划线开头为私有属性（自由自己才能访问）(__age)

class Dog(Animal):
    def __init__(self, name, age=2):
        if age > 3:
            super().__init__(age)
        else:
            super().__init__(age)
        self.name = name

    def show(self):
        print(f'{self.name}{self.age}')

if __name__ == "__main__":
    dog = Dog('旺财', 3)
    dog.show()
