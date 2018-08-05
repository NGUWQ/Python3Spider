#Created by TTT
'''
一只青蛙一次可以跳上1级台阶，也可以跳上2级……它也可以跳上n级。
求该青蛙跳上一个n级的台阶总共有多少种跳法。
'''
def function(n):
    if n==1:
        return n
    return 2*function(n-1)
print(function(4))