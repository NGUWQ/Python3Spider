#Created by TTT
class defined:
    '''
    def __init__(self,size=10):
        self.size=size
    def get(self):
        return self.size
    def set(self,value):
        self.size=value
    def dele(self):
        del self.size
    x=property(get,set,dele)
    '''
    def __getattribute__(self, item):
        print("gggg")
        return super().__getattribute__(item)
    def __getattr__(self, item):
        print("haha")
    def __setattr__(self, key, value):
        print('faafa')
        return super().__setattr__(key,value)
    def __delattr__(self, item):
        print('fafafafa')
        return super().__delattr__(item)
d=defined()
d.x=1
print(d.x)
#del d.x