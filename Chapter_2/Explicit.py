import numpy as np
import matplotlib.pyplot as plt

'''
Explicit
古典显格式，划分为102个单元的两端封闭河道，中心扩散
'''


def Explicit_method(im,it,r):
    # Set initial concentration: 50th cell was 100, the others were 0
    c = np.zeros([im, it + 1])
    c[int(im/2),0] = 100


    for t in range(it-1):
        
        # Start to diffuse
        for i in range(1, im-1):
            c[i,t+1] = (1 - 2*r) * c[i,t] + r * c[i+1,t] + r * c[i-1,t]
        
        # The virtual boundary setting
        c[0,t+1] = c[1,t+1]
        c[im - 1, t+1] = c[im-2, t+1]

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
    
    im = 102 # 100 + 2 cells
    it = 10000 # 100 time steps

    DX = 100 # step length = 1 (meter) spacially
    DT = 100 # step length = 1 (seconds) tempororally
    K = 10 # Diffusion coefficient
    r = K * DT/(DX**2)

    c = Explicit_method(im,it,r)

    plot_conc(im,c)