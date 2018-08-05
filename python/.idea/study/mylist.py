#Created by TTT
#定义自己的序列
class Mylist:
    def __init__(self,*args):
        self.values=[x for x in args]
        self.count={}.fromkeys(range(len(self.values)),0)
    def __len__(self):#必须
        return len(self.values)
    def __getitem__(self, item):#必须
        self.count[item]+=1
        return self.values[item]
c1=Mylist(1,2,4)
print(c1[0])
print(c1.count)