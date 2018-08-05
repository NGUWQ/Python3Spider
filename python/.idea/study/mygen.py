#Created by TTT
#生成器
'''
def fibs():
    a=0
    b=1
    while True:
        a,b=b,b+a
        yield a

for i in fibs():
    if i>100:
        break
    print(i)
for i in fibs():
    if i>200:
        break
    print(i)
'''
a=[i for i in range(100) if i%2 and i%3]
b={i:i%2!=0 for i in range(10) }
print(b)