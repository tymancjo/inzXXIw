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


delta = 1/1000 # [-] maksymalna dopuszczalna zmiana wyniku
T_max = 1      # [st C] wartość startowa

N = [n for n in range(20,1000,20)]
for n in N:
    T_prev = T0
    dt = t_max / n      

    for tx in range(n):
        T_prev = T_prev+(R0*(1+alfa*(T_prev-20))*I*I*dt)/(m*cp)

    d = abs((T_prev - T_max)/T_prev)

    if d < delta:
        print(f'Zakończono symulację dla {n=} kroków')
        break

    T_max = T_prev

print(f'Po czasie {t_max=}[s] osiąga {T_max=:.2f}[st C]')






