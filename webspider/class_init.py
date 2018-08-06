# class_init.py

class Person:
    def __init__(self, name):
        self.name=name
    def sayHi(self):
        print('hello,my name is',self.name)

p=Person('xiaqijian')
p.sayHi()


