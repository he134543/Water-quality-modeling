from __future__ import division
import numpy as np
import pandas as pd
import csv
import matplotlib.pyplot as plt

def reverse_timediff(c, c_new, im, it, r):
    
    # 创建文件
    f = open('Reverse_timediff.csv', 'a')
    f.seek(0)
    f.truncate()

    # 300个时间步长
    for t in range(it):
        
        # 设置L, U
        l = np.zeros(im)
        u = np.zeros(im)
        u[0] = 1
        u[1] = 1
        l[1] = -0.5*r/u[0]
        for i in range(2, im-1):
            l[i] = -0.5*r/u[i-1]
            u[i] = 1 - 0.5 * l[i] * r
        
        l[im-1] = -1 / u[im-2]
        u[im-1] = 1 - 0.5 * r * l[im-1]

        # 设置b,y
        b = c
        b[0] = 100
        b[im-1] = 0

        y = b
        for i in range(1,im):
            y[i] = b[i] - l[i] * y[i-1]
        

        # calculate c_new and c
        c_new[im-1] = y[im-1]/u[im-1]

        for i in range(im-2, 0, -1):
            c_new[i] = (y[i] - 0.5 * r * c_new[i+1])/u[i]
        c_new[0] = c_new[1]

        # 交换c_n和c
        c = c_new

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


if __name__ == '__main__':
    
    im = 100
    it = 300
    dx = 100
    dt = 150
    v = 1.0
    r = v * dt / dx


    c = np.zeros(im)
    c_new = np.zeros(im)


    reverse_timediff(c, c_new, im, it, r)

    plot_conc('Reverse_timediff.csv')




    
