from test.myModule import MyModule
from test.myModule import person1
from Person import Person

name = 'Birudeo'
address = "Solapur"

mymodule_instance = MyModule(name)
mymodule_instance.greeting()

person = Person(name, address)
person.display()

print(person1)
