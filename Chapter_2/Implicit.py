import numpy as np
import matplotlib.pyplot as plt

'''
Implicit method, 古典隐格式
'''

def Implicit_method(im,it,R):
    c = np.zeros([im,it + 1])
    c[int(im/2)-2, 0] = 100

    # LU factorization products
    u = np.zeros(im)
    l = np.zeros(im) # l should be 1 less than u

    # y and b
    y = np.zeros(im)
    b = np.zeros(im)

    
    for t in range(it - 1):
        u[0] = 1
        l[1] = -R/u[0]
        u[1] = (1 + 2* R) + l[1]
        
        # 2.2.12
        for i in range(2, im -1):
            l[i] = -R/u[i-1]
            u[i] = (1 + 2 * R) + R * l[i]

        l[im-1] = 1/u[im-2]
        u[im-1] = -1 + R * l[im-1]


        # 2.2.13
        for i in range(1, im - 1):
            b[i] = c[i, t]

        b[0] = 0
        b[im-1] = 0

        y[0] = b[0]

        for i in range(1,im):
            y[i] = b[i] - l[i] * y[i-1]

        # 2.2.14
        c[im-1, t+1] = y[im-1]/u[im-1]

        for i in range(im - 2, 0, -1):
            c[i, t+1] = (y[i] + R * c[i, t+1])/u[i]

        c[0,t+1] = c[1,t+1]

    return c

def plot_conc(im,c):
    plt.figure()
    plt.plot(np.arange(im), c[:,10], label = '10dt')
    plt.plot(np.arange(im), c[:,100], label = '100dt')
    plt.plot(np.arange(im), c[:,1000], label = '1000dt')
    plt.plot(np.arange(im), c[:,10000], label = '10000dt')
    plt.legend()
    plt.show()



if __name__ == '__main__':
    im = 102
    it = 10000

    DX = 100
    DT = 100
    K = 10
    R = K * DT /(DX **2)

    c = Implicit_method(im,it,R)

    plot_conc(im,c)
