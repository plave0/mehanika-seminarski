import numpy as np
import matplotlib.pyplot as plt

data = np.loadtxt("baseballforce.d")

T = data[:,0]
F = data[:,1]

dt = T[1] - T[0]
m = 0.145
alfa = np.deg2rad(0)

lena = 100
lenv = 100
lendt = 100

AX = np.zeros(lena)
AY = np.zeros(lena)

VX = np.zeros(lenv)
VY = np.zeros(lenv)

DT = np.zeros(lendt)

RX = np.array([])
RY = np.array([])

rx = 0
ry = 1.5

ax = 0
ay = 0

vx = 0
vy = 0

t = 0

a = 0

ia = 0 # brojac za AX i AY
iv = 0 # brojac za VX i VY
idt = 0

for f in F:

    a = f/m

    ax = a * np.cos(alfa)
    ay = a * np.sin(alfa) - 9.81

    AX[ia] = ax
    AY[ia] = ay

    ia += 1;

    if ia >= lena:
        lena *= 2
        AX = np.resize(AX, lena)
        AY = np.resize(AY, lena)

    vx += dt * ax
    vy += dt * ay

    VX[iv] = vx
    VY[iv] = vy

    iv += 1

    if iv >= lenv:
        lenv *= 2
        VX = np.resize(VX, lenv)
        VY = np.resize(VY, lenv)

    rx += vx * dt
    ry += vy * dt

    DT[idt] = t

    idt += 1

    if idt >= lendt:
        lendt *= 2
        DT = np.resize(DT, lendt)

    t += dt

AX = np.resize(AX, ia)
AY = np.resize(AY, ia)

print("Ubrzanje: " + str(ax) + " " + str (ay) + "\nBrzina: " + str(vx) + " " + str(vy) + "\nIntezitet ubrzanja: " + str(a) + "\nPolozaj: " + str(rx) + " " + str(ry) +
      "\nVreme: " + str(t))

ax = 0
ay = -9.81

brojac = 0
while ry >= 0:

    vx = vx + dt * ax
    vy = vy + dt * ay

    VX[iv] = vx
    VY[iv] = vy

    iv += 1

    if iv >= lenv:
        lenv *= 2
        VX = np.resize(VX, lenv)
        VY = np.resize(VY, lenv)

    rx = rx + dt * vx
    ry = ry + dt * vy

    DT[idt] = t

    idt += 1

    if idt >= lendt:
        lendt *= 2
        DT = np.resize(DT, lendt)

    t += dt

VX = np.resize(VX, iv)
VY = np.resize(VY, iv)

DT = np.resize(DT, idt)

print("Vreme: " + str(t) + "\nDolet: " + str(rx))
print(brojac)

plt.figure()
plt.ylabel("Ubrzanje [m/s^2]")
plt.xlabel("Vreme [s]")
plt.title("Ubrzianje u funkciji vremena")
plt.plot(T, AX)
plt.show()

plt.figure()
plt.ylabel("Brzina [m/s]")
plt.xlabel("Vreme [s]")
plt.title("Brzina u funkciji vremena")
plt.plot(DT, VY)
plt.show()
