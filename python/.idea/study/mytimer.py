#Created by TTT
import  time
class Timer:
    def __init__(self):
        self.ls=0#起始时间
        self.lss=0#结束时间
        self.strs='还没有开始计时'#单个时间的输出
        self.strss=''#两个时间的输出
        self.result=0#时间差
    def __str__(self,ls,lss):
        return self.strs

    __repr__=__str__

    def __add__(self, other):
        self.strss='运行时间为'
        return self.strss+str(int(self.strs[-1])+int(other.strs[-1]))
    def start(self):
        self.ls=time.localtime()[5]
        self.strs='请调用end方法'
        print('计时开始')
    def end(self):
        print('计时结束')
        self.lss=time.localtime()[5]
        self.result=self.lss-self.ls
        self.strs='运行时间为'+str(self.result)
        self.strs='请直接输出对象'
        #print(self.strs)