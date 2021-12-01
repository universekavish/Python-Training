import myModule

print(myModule.__doc__)
print(myModule.sayHi.__doc__)
print(myModule.Rectangle.__doc__)
print(myModule.Rectangle.area.__doc__)

print(myModule.version)

myModule.sayHi()

p = myModule.Person('abc', 'xyz', 'shksk@jnosag.com')
print(p)

fn = p.fullname()
print('p full name ', fn)