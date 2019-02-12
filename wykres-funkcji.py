import pylab
import matplotlib.pyplot as plt

x = pylab.arange(-10, 10.5, 0.5)
a = int(input("Podaj współczynnik a: "))
y1 = [i / -3 + a for i in x if i <= 0]

ax = plt.gca()
ax.spines['right'].set_color('none')
ax.spines['top'].set_color('none')
ax.xaxis.set_ticks_position('bottom')
ax.spines['bottom'].set_position(('data',0))
ax.yaxis.set_ticks_position('left')
ax.spines['left'].set_position(('data',0))



y2 = [i**2 / 3 for i in x if i >= 0]


plt.plot(x[:len(y1)], y1, label="x/(-3) + a")
plt.plot(x[-len(y2):], y2, label="x*x/3")

plt.title("Wykres funkcji")
plt.legend(loc='upper left')
plt.grid(True)
plt.show()
