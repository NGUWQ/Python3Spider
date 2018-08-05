#Created by TTT
class Myproperty:
    def __init__(self,mset=None,mget=None,mdel=None):
        self.mset=mset
        self.mget=mget
        self.mdel=mdel
    def __get__(self, instance, owner):
        return self.mget(instance)
    def __set__(self, instance, value):
        self.mset(instance,value)
    def __delete__(self, instance):
        self.mdel(instance)
class sheshi:
    def __init__(self,x=26.0):
        self.x=float(x)
    def __get__(self, instance, owner):
        return self.x
    def __set__(self, instance, value):
        self.x=float(value)
class huashi:
    def __get__(self, instance, owner):
        return instance.c*1.8+32
    def __set__(self, instance, value):
        instance.c=(float(value)-32)/1.8
class Wram:
    c=sheshi()
    h=huashi()

w=Wram()
w.c=44
print(w.h)

