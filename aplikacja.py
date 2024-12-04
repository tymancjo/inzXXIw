import argparse

def pobierz_parametry():
    parser = argparse.ArgumentParser(description="Pobieranie stałych z linii komend")
    parser.add_argument('--a', type=float, default=10e-3, help='Wartość a [m]')
    parser.add_argument('--b', type=float, default=50e-3, help='Wartość b [m]')
    parser.add_argument('--l', type=float, default=1, help='Wartość l [m]')
    parser.add_argument('--sigma', type=float, default=56e6, help='Wartość sigma [S/m]')
    parser.add_argument('--alfa', type=float, default=3.9e-3, help='Wartość alfa [Om/K]')
    parser.add_argument('--I', type=float, default=50_000, help='Wartość I [A]')
    parser.add_argument('--cp', type=float, default=385, help='Wartość cp [K/kg.K]')
    parser.add_argument('--ro', type=float, default=8900, help='Wartość ro [kg/m3]')
    parser.add_argument('--t_max', type=float, default=3, help='Wartość t_max [s]')
    parser.add_argument('--n', type=int, default=200, help='Wartość n [-]')
    parser.add_argument('--T0', type=float, default=20, help='Wartość T0 [st C]')
    parser.add_argument('--delta', type=float, default=1/1000, help='Maksymalna dopuszczalna zmiana wyniku [-]')

    return parser.parse_args()

def main():

    args = pobierz_parametry()

    R0 = args.l/(args.a*args.b*args.sigma)  # [Om]
    m = args.a*args.b*args.l*args.ro        # [kg]
    mcp = m*args.cp

    T0 = args.T0
    t_max = args.t_max
    alfa = args.alfa
    I = args.I
    delta = args.delta

    print()

    T_max = 1      # [st C] wartość startowa
    N = [n for n in range(20,10000,20)]
    for n in N:
        T_prev = T0
        dt = t_max / n      

        for _ in range(n):
            T_prev = T_prev+(R0*(1+alfa*(T_prev-20))*I*I*dt)/(mcp)

        d = abs((T_prev - T_max)/T_prev)

        if d < delta:
            print(f'Zakończono symulację dla {n=} kroków')
            break

        T_max = T_prev

    print(f'Po czasie {t_max=}[s] osiąga {T_max=:.2f}[st C]')
    print()


if __name__ == "__main__":
    main()




