#Created by TTT
class Person:
    name="wq"
p=Person()
#print(hasattr(p,'gg'))
setattr(p,'rr','fda')
print(getattr(p,'rr'))
print(dir(Person()))
print(dir(p))