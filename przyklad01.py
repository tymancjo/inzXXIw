# Definicje stałych
a = 10e-3           # [m]
b = 50e-3           # [m]
l = 1               # [m]
sigma = 56e6        # [S/m]
alfa = 3.9e-3       # [Om/K]
I = 50_000          # [A]
cp = 385            # [K/kg.K]
ro = 8900           # [kg/m3]
t_max = 3           # [s]
n = 200             # [-]
T0 = 20             # [st C]
R0 = l/(a*b*sigma)  # [Om]

# Wstępne obliczenia
m = a*b*l*ro        # [kg]

T_max = []
N = [n for n in range(20,2000,20)]

for n in N:
    T = [T0]
    dt = t_max / n      
    wektor_czasu = [i*dt for i in range(n)]

    for tx in wektor_czasu[1:]:
        Tx = T[-1]+(R0*(1+alfa*(T[-1]-20))*I*I*dt)/(m*cp)
        T.append(Tx)

    T_max.append(max(T))


# generowanie wykresu
import matplotlib.pyplot as plt
plt.plot(N,T_max)
plt.grid()
plt.xlabel('liczba iteracji [-]')
plt.ylabel('maksymalna temperatura [st C]')
plt.show()


