from __future__ import division
import numpy as np
import pandas as pd
import csv
import matplotlib.pyplot as plt

'''
Upwind格式，初始时刻全场浓度位0，流速为1.0
上游不断输入浓度为c0的污染物


0<r<1时，曲线平滑

'''


def Upwind(c, c_new, im, it, r):

    f = open('Upwind.csv', 'a')
    f.seek(0)
    f.truncate()
    
    # 300个时间步长
    for t in range(it):
        
        for i in range(1,im):
            c_new[i] = c[i] - r * (c[i] - c[i-1])
                        
        # 设置污染源
        c_new[0] = 100

        c = c_new

        # 存储浓度计算文件
        writer = csv.writer(f)
        writer.writerow(c)

    f.close()

def plot_conc(filename):
    data = pd.read_csv(filename, header=None).values
    plt.figure()

    plt.plot(data[9,:], label = 't = 10 dt')

    plt.plot(data[49,:], label = 't = 50 dt')

    plt.plot(data[99,:], label = 't = 100 dt')
    plt.plot(data[299,:], label = 't = 300 dt')
    plt.xlabel('x, dx')
    plt.ylabel('Concentration($kg/m^{-3}$)')
    plt.legend()
    plt.show()

def main():
    im = 100 # 100个格子
    it = 300 # 100个时间步长
    dx = 100 # 空间步长100m
    dt = 50 # 时间步长50s
    u = 1.0 # 流速1.0m/s
    r = u * dt / dx # 通量系数
    
    # 设置c和c_n+1
    c = np.zeros(im)
    c_new = np.zeros(im)

    Upwind(c, c_new, im, it, r)
    plot_conc('Upwind.csv')


main()

        


