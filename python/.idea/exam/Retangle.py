# Created by TTT
'''
我们可以用2*1的小矩形横着或者竖着去覆盖更大的矩形。
请问用n个2*1的小矩形无重叠地覆盖一个2*n的大矩形，总共有多少种方法？
'''


def function(n):
    if n == 1 or n == 2:
        return n
    return function(n - 2) + function(n - 1)
print(function(5))
