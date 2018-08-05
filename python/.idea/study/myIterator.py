#Created by TTT
#实现一个迭代器
class Fibs:
    def __init__(self,n=20):
        self.n=n
        self.a=0
        self.b=1
    def __iter__(self):#必须
        return self
    def __next__(self):#必须
        self.a,self.b=self.b,self.b+self.a
        if self.a>self.n:
            raise  StopIteration
        return self.a
fib=Fibs()
for h in fib:
    print(h)