import numpy as np
import matplotlib.pyplot as plt
#Переменные
a = 1
b = 1
#Функция
def func(x,y,a,b,N0):
    dx = y
    dy = - a*x - b*y + N0*np.random.normal()
    return dx,dy
#Уровни шума
N = [0, 0.5, 1]
#Начальные значения
x0 = 1.0
y0 = 0.0
#Время интегрирования
dt = 0.01
it = 10000
t = np.linspace(0, it*dt, it)
#Непосредственный расчёт и построение графика
plt.figure()
for N0 in N:
    x = np.zeros(it)
    y = np.zeros(it)
    x[0] = x0
    y[0] = y0
    for i in range(1, it):
        dx, dy = func(x[i-1], y[i-1], a, b, N0)
        x[i] = x[i-1] + dx * dt
        y[i] = y[i-1] + dy * dt
    plt.plot(t, x, label=f'N={N0}')
plt.xlabel('t')
plt.ylabel('x')
plt.legend()
plt.title('Zagolovok')
plt.grid()
plt.show()