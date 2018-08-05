#象棋问题,L型（递归）
'''
tr表示棋盘的行位置
tc表示棋盘的列位置
dr表示当前所在棋盘的行位置
dc表示当前所在棋盘的列位置
s表示当前棋盘的尺寸
'''
steps=0
lists=[[]]*4
def move(n,a,b):
    global steps
    steps+=1
def qipan(tr,tc,dr,dc,s):
    if s==1:
        return
    cut=steps
    s=s/2
    #左上部分
    if dr<tr+s&dc<tc+size:
        qipan(tr,tc,dr,dc,s)
    else:
        lists[tr+s-1][tc+s-1]=cut
        qipan(tr,tc,dr,dc,s)
    #左下部分
    if dr<tr+s&dc<tc+size:
        qipan(tr,tc,dr,dc,s)
    else:
        lists[tr+s-1][tc+s]=cut
        qipan(tr,tc,dr,dc,s)
    #右上部分
    if dr<tr+s&dc<tc+size:
        qipan(tr,tc,dr,dc,s)
    else:
        lists[tr+s][tc+s-1]=cut
        qipan(tr,tc,dr,dc,s)
    #右下部分
    if dr<tr+s&dc<tc+size:
        qipan(tr,tc,dr,dc,s)
    else:
        lists[tr+s][tc+s]=cut
        qipan(tr,tc,dr,dc,s)
