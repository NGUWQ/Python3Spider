#Created by TTT
def function(n):
    if n==1 or n==2:
        return 1
    return function(n-2)+function(n-1)
print(function(7))
