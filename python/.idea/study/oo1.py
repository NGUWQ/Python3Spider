# Created by TTT
class mystr(int):
    def __new__(cls,s):
        s=s.upper()
        return str.__new__(cls,s)
    def __init__(self, s):
        self.s = s
    def get(self):
        return self.s
m = mystr('uuuu')
print(m.get())
