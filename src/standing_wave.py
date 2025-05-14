import numpy as np 
import matplotlib.pyplot as plt
from matplotlib import animation

def sineWaveZeroPhi(x, t, A, omega, k):
    '''
    返回位置x和时间t的波函数值
    参数:
    x : 空间位置 (array)
    t : 时间 (float)
    A : 振幅 (float)
    omega : 角频率 (float)
    k : 波数 (float)
    '''
    return A * np.sin(k * x - omega * t)

# 创建动画所需的 Figure 和 Axes
fig = plt.figure()
subplot = plt.axes(xlim=(0, 10), xlabel="x", ylim=(-2, 2), ylabel="y")

# 创建空的line对象，用于动画显示
line1, = subplot.plot([], [], lw=2)
line2, = subplot.plot([], [], lw=2)
line3, = subplot.plot([], [], lw=2)

# 创建一个line对象列表，便于操作
lines = [line1, line2, line3]

def init():
    '''
    动画初始化函数
    '''
    for line in lines:
        line.set_data([], [])
    return lines

# 创建空间变量x
x = np.linspace(0, 10, 1000)

def animate(i):
    '''
    动画更新函数
    参数: i - 帧序号，自动递增
    '''
    # 定义波的参数
    A = 1
    omega = 2 * np.pi
    k = np.pi / 2
    t = 0.01 * i

    # 计算两个方向相反的波
    y1 = sineWaveZeroPhi(x, t, A, omega, k)
    y2 = sineWaveZeroPhi(x, t, A, -omega, k)  # 方向相反，omega取负
    
    # 计算驻波（两波之和）
    y3 = y1 + y2
    
    # 更新每个line的数据
    waveFunctions = [y1, y2, y3]
    for line, y in zip(lines, waveFunctions):
        line.set_data(x, y)
    
    return lines

if __name__ == '__main__':
    # 创建动画对象并显示
    anim = animation.FuncAnimation(fig, animate, init_func=init,
                                   frames=200, interval=50, blit=True)
    plt.title('Standing Wave Formation')
    plt.show()
