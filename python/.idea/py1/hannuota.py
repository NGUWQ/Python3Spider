#汉诺塔问题(递归)
steps=0
def move():
    global steps
    steps+=1
def towers(n,x,y,z):
    if(n==1):
        print('{0} from '.format(n),x,' to ',z)
        move()
    else:
        towers(n-1,x,z,y)
        move()
        print('{0} from '.format(n),x,' to ',z)
        towers(n-1,y,x,z)
n=int(input("请输入要移动的层数:"))
towers(n,'A','B','C')
print('{0}层汉诺塔需要移动{1}次'.format(n,steps))
#64层需要2**64-1次移动
