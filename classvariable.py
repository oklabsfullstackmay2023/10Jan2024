#1. class defination is one time process
class MyClass():
    #1 Property=Variable
    name='Vishal'
    surname='Mahawar'
    age=15
    address="Neemuch"
    pass

#2. create class object is many time process
ceo1=MyClass()
ceo2=MyClass()

print(ceo1.name)
print(ceo1.surname)
print(ceo1.age)
print(ceo1.address)


print(ceo2.name)
print(ceo2.surname)
print(ceo2.age)
print(ceo2.address)