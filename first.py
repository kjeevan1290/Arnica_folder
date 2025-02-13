class Person:
  def __init__(self, name, age):
    self.name = name
    self.age = age

  def myfunc(self):
    print("Hello my name is " + self.name)

p1 = Person("John", 36)
p1.myfunc()

class vehicale:
  def __init__(self,name,brand):
    self.name=name
    self.brand=brand

  def abc(self):
    return f"My Brand is {self.name}"

a=vehicale("nexon","tata")
print(a.abc())

print("starting function")

def abc(*a):
  return 100*a

x=abc(10,0)
print("a value",x)

