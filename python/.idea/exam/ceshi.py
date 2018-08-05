__author__ = 'WQ'
# *_*coding:utf-8 *_*
from flask import Flask
app=Flask(__name__)
@app.route('/')
def hello():
    return 'hello world'
if __name__=='__main__':
    app.run()