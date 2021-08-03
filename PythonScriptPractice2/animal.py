"""
1.写一个面向对象的例子：
    比如创建一个类（Animal）【动物类】，类里有属性（名称，颜色，年龄，性别），类方法（会叫，会跑）
    创建子类【猫】，继承【动物类】
    重写父类的__init__方法，继承父类的属性
    添加一个新的属性，毛发=短毛
    添加一个新的方法， 会捉老鼠，
    重写父类的‘【会叫】的方法，改成【喵喵叫】
    创建子类【狗】，继承【动物类】
    复写父类的__init__方法，继承父类的属性
    添加一个新的属性，毛发=长毛
    添加一个新的方法， 会看家
    复写父类的【会叫】的方法，改成【汪汪叫】
2.在入口函数中创建类的实例
    创建一个猫猫实例
    调用捉老鼠的方法
    打印【猫猫的姓名，颜色，年龄，性别，毛发，捉到了老鼠】
    创建一个狗狗实例
    调用【会看家】的方法
    打印【狗狗的姓名，颜色，年龄，性别，毛发】
"""


class Animal:
    def __init__(self, name, color, age, gender):
        self.name = name
        self.color = color
        self.age = age
        self.gender = gender

    def cry(self):
        print('i can cry')

    def run(self):
        print('i can run')


class Cat(Animal):
    def __init__(self, name, color, age, gender):
        super().__init__(name, color, age, gender)
        self.hair = 'short hair'

    def catch_mice(self):
        print('i can catch mice')

    def cry(self):
        print('miao~')


class Dog(Animal):
    def __init__(self, name, color, age, gender):
        super().__init__(name, color, age, gender)
        self.hair = 'long hair'

    def house_keeping(self):
        print('i will keeping our house')

    def cry(self):
        print('wow!')


if __name__ == '__main__':
    cat = Cat("kitty", "yellow", "one", "male")
    print(f"i am {cat.name},my color is {cat.color},i am {cat.age}years old,i have {cat.hair},i am {cat.gender}")
    cat.catch_mice()

    dog = Dog("half", "black", "two", "female")
    print(f"i am {dog.name},my color is {dog.color},i am {dog.age}years old,i have {cat.hair},i am {cat.gender}")
    dog.house_keeping()
