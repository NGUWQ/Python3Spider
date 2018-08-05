#Created by TTT
class Retangle:
    def __init__(self,x=0,y=0):
        self.x=x
        self.y=y
    def __setattr__(self, key, value):
        if key=='square':
            self.x=value
            self.y=value
        else:#两种方法
            super().__setattr__(key,value)
            #self.__dict__[key]=value
    def squares(self):
        return self.x*self.y
r=Retangle(3,3)
#r.square=10
print(r.squares())