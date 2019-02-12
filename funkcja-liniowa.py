import matplotlib.pyplot as plt

a=int(input("Podaj a = "))
b=int(input("Podaj b = "))

x = range(-10, 11)

ax = plt.gca()
ax.spines['right'].set_color('none')
ax.spines['top'].set_color('none')
ax.xaxis.set_ticks_position('bottom')
ax.spines['bottom'].set_position(('data',0))
ax.yaxis.set_ticks_position('left')
ax.spines['left'].set_position(('data',0))

y = []
for i in x:
    y.append(a * i + b)

plt.plot(x, y, label="Funkcja liniowa")

if(a==0):
    plt.text(-3, 10, "Funkcja stała")
elif(a<0):
    plt.text(-3, 10, "Funkcja malejąca")
elif(a>0):
    plt.text(-3, 10, "Funkcja rosnąca")

plt.title('Wykres f(x) = a*x + b')
plt.grid(True)
plt.legend(loc='upper left')
plt.show()



#a=0 f.stala
#a<0 f.malejaca
