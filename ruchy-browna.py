import numpy as np
import random
import matplotlib.pyplot as plt

a = int(input("Ile ruchów? "))
x = y = 0
lx = [0]
ly = [0]

for i in range(0, a):
    rad = float(random.randint(0, 360)) * np.pi / 180
    x = x + np.cos(rad)
    y = y + np.sin(rad)

    lx.append(x)
    ly.append(y)

print(lx, ly)

s = np.fabs(np.sqrt(x**2 + y**2))
print("Wektor przesunięcia:", s)

plt.plot(lx, ly, "o:", color="green", linewidth=2, alpha=0.5)

plt.plot([0,x], [0,y], color="blue")

plt.legend(["Dane x, y\nPrzemieszczenie: " + str(s)], loc="upper left")
plt.xlabel("oś x")
plt.ylabel("oś y")
plt.title("Ruchy Browna")
plt.grid(True)
plt.show()
