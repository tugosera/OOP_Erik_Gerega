class Student:
    def __init__ (self,name,title,age):
        self.name = name
        self.title = title
        self.age = age

    def hello (self):
        print ("Hello", self.name)

    def ShowAge(self):
        print(self.name, "is", self.age, "years old")

s = Student("ago", "Teacher", 16)
print(type(s))
print (s.name)
s.hello()
s.ShowAge()

t = Student("kah", "Teacher", 27)
print(type(t))
print (t.name)
t.hello()
t.ShowAge()

if s.name == t.name:
    print(True)
else:
    print(False)