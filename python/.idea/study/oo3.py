#Created by TTT
class myint(int):
    def __add__(self, other):
        return int.__sub__(self,other)
    def __sub__(self, other):
        return int.__add__(self,other)
    def __iadd__(self, other):
        return int.__add__(self,other)

a=myint('4')
b=myint('6')
print(a+b)