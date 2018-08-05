# coding:utf-8
#笛卡尔心形图
import matplotlib.pyplot as plt
from matplotlib import animation
import numpy as np
import math

def drawHeart():
    t = np.linspace(0, math.pi, 1000)
    x = np.sin(t)
    y = np.cos(t) + np.power(x, 2.0/3)
    plt.plot(x, y, color='red', linewidth=2, label='h')
    plt.plot(-x, y, color='red', linewidth=2, label='-h')
    plt.xlabel('t')
    plt.ylabel('h')
    plt.ylim(-3, 3)
    plt.xlim(-3, 3)

    plt.legend()
    plt.savefig('heat.jpg')
    plt.show()

drawHeart()