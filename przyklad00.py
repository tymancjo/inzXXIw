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
dt = t_max / n      # [s]
m = a*b*l*ro        # [kg]


wektor_czasu = [i*dt for i in range(n)]
# wektor temperatury 
T = [T0]


# obliczenia dla każdego elemtu wektora czasu
for tx in wektor_czasu[1:]:
    Tx = T[-1]+(R0*(1+alfa*(T[-1]-20))*I*I*dt)/(m*cp)
    T.append(Tx)

print(f'{max(T)=}')

# generowanie przebiegu
import matplotlib.pyplot as plt
plt.plot(wektor_czasu,T)
plt.grid()
plt.xlabel('czas [s]')
plt.ylabel('temperatura [st C]')
plt.title(f'{max(T)=:.0f} [st C]')
plt.show()

