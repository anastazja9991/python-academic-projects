import matplotlib.pyplot as plt
import pylab as p

a=int(input("Podaj a = "))
b=int(input("Podaj b = "))
x = p.arange(-20,20,0.5)
y = a*x
y2 = a*x + b
y3 = x**2

ax = plt.gca()
ax.spines['right'].set_color('none')
ax.spines['top'].set_color('none')
ax.xaxis.set_ticks_position('bottom')
ax.spines['bottom'].set_position(('data', 0))
ax.yaxis.set_ticks_position('left')
ax.spines['left'].set_position(('data', 0))

plt.plot(y, 'r:',linewidth=6, label = "Funkcja ax")
plt.plot(y2, label="Funkcja ax+b")
plt.plot(y3, 'g+',linewidth=5, label="Funkcja x^2")
plt.legend(loc='upper left')
plt.grid(True)
plt.show()



