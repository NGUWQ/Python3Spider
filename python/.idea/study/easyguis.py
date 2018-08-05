#Created by TTT
import  easygui as e
import sys
e.msgbox("haha","hehe")
choice=['愿意','不愿意']
e.choicebox('你愿意嫁给我吗','haha',choices=choice)
e.msgbox('yyyyyyyyyyy',ok_button='enen')
if e.ccbox("do you want",choices=choice):
    e.choicebox('你愿意嫁给我吗','haha',choices=choice)
else:
    sys.exit(0)
e.enterbox()