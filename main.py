import numpy as np
import matplotlib.pyplot as plt

# Učitavamo podatke iz fajla baseballforce.d
# U prvoj koloni se nalazi proteklo vreme od početka udarca
# a u drugoj koloni kojom silom palica deluje na lopticu u tom trenutku

# Podatke u vremenu smeštamo u niz T, a podatke o sili u niz F

data = np.loadtxt("baseballforce.d")

T = data[:,0]
F = data[:,1]

# Masa loptice u kilogramima (zadata u zadatku)
m = 0.145

# Vremenski korak je konstantan u nizu T, pa
# uzimamo razliku između prvo g i drugog
dt = T[1] - T[0]

# Ugao pod kojim se udara loptica u radijanima (nije zadata u zadaku)
alfa = np.deg2rad(30)

# Inicijalizujemo nizove gde čuvamo ubrzanje, brzinu i položaj.
# Za početak iz inicijalizujemo kao prazne nizove dužine 100

lena = 100
A = np.empty(shape=(lena, 2))

lenv = 100
V = np.empty(shape=(lenv, 2))

lendt = 100
DT = np.empty(lendt)

lenr = 100
R = np.empty(shape=(lenr, 2))

# Početni položaj
r = np.array([0, 1.5])

# Početna brzina
v = np.array([0,0])

# Početno ubrzanje
a = np.array([0, 0])

# Vreme proteklo od početka simulacije
t = 0

# Brojači za prolazak kroz nizove
ia = 0
iv = 0
ir = 0
idt = 0

# Brojač kroz petlju
brojac = 0

# U ovoj petlji prolazimo kroz sve vremenske trenutke iz fajla
while r[1] >= 0:

    # Ako i dalje deluje sila udarca na lopticu
    if brojac < len(F):
         # Računamo intezitet ubrzanja u tom trenutku
        a = F[brojac]/m

        # Računamo vektorz ubrzanja i čuvamo ga
        a = np.array([a * np.cos(alfa), a * np.sin(alfa) - 9.81])
        A[ia] = a

    # U suprotnom, ubrzanje je konstantno
    else:
        a = np.array([0, -9.81])
        # A[ia] = a

    # Uvećavamo brojač i proveravamo da li smo sitgli do kraja niza
    # Ako jesmo, širimo niz

    # Ojler-Kromerovom metodom računamo brzinu i položaj i čuvamo ih
    v = v + a * dt
    r = r + v * dt
    V[iv] = v
    R[ir] = r

    if brojac == len(F):
        print("U trenutku kada palica prestane da deluje na lopticu:")
        print("\tVektor brzine = " + str(v))
        print("\tIntenzitet brzine = " + str(np.sqrt(v[0]**2 + v[1]**2)) + " m/s")

    # Čuvamo trenutno proteklo vreme i ažuriramo proteklo vreme
    DT[idt] = t
    t += dt

    # Uvećavamo brojače i proveravamo da li smo sitgli do kraja niza
    # Ako jesmo, širimo niz

    if brojac < len(F):
        ia += 1
        if ia >= lena:
            lena *= 2
            A = np.resize(A, (lena, 2))

    iv += 1
    if iv >= lenv:
        lenv *= 2
        V = np.resize(V, (lenv, 2))

    ir += 1
    if ir >= lenr:
        lenr *= 2
        R = np.resize(R, (lenr, 2))

    idt += 1
    if idt >= lendt:
        lendt *= 2
        DT = np.resize(DT, lendt)

    brojac += 1


# Skrećujemo nizove tako da se uklope sa njihovim sadržajima
A = np.resize(A, (ia, 2))
V = np.resize(V, (iv, 2))
R = np.resize(R, (ir, 2))
DT = np.resize(DT, idt)

plt.figure()
plt.ylabel("Ubrzanje [m/s^2]")
plt.xlabel("Vreme [s]")
plt.title("Ubrzianje u funkciji vremena")
plt.plot(T, A)
plt.show()

plt.figure()
plt.ylabel("Brzina [m/s]")
plt.xlabel("Vreme [s]")
plt.title("Brzina u funkciji vremena")
plt.plot(DT, V)
plt.show()

plt.figure()
plt.ylabel("y")
plt.xlabel("x")
plt.title("Putanja loptice")
plt.plot(R[:,0], R[:,1])
plt.show()
