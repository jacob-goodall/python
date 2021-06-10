import matplotlib.pyplot as plt

# Not needed to make graph just for table
from tabulate import tabulate

# S = supply voltage Var
# C is capacitance value Var
# DT is time interval Var
# Q is Charge
# CV is Capacitor Voltage
# VD is voltage difference
# IC is Current
# CM is Charged Moved
# T = time (s)
# R is Resistance Var
# RC is Time Constant
# RT is Max Run Time
# P followed by Var letter is Prefix, Eg milli-volts

# Initiating Lists
table = [
    [
        "Time (s)",
        "Voltage difference",
        "Capacitor Voltage",
        "Capacitance(F)",
        "Resistance",
        "Current(A)",
        "Charge moved (C)",
        "Total Charge (C)",
    ]
]
graphs1 = []
graphs2 = []
# Initiating Values
Q = 0
T = 0
CM = 0
VD = 0
CV = 0
C = 0
R = 0
IC = 0

# Inputs
PS = input("Prefix for Voltage - kilo, mega, giga \nmilli, micro (µ), nano, volts:")
PS = PS.lower()
PS = PS.strip()
if PS != "volts":
    S = input("Supply Voltage (" + PS + "volts):")
    S = S.strip()
    S = float(S)
if PS == "volts":
    S = input("Supply Voltage (V):")
    S = S.strip()
    S = float(S)
if PS == "kilo":
    S = float(S)
    S = S * 10 ** 3
if PS == "mega":
    S = float(S)
    S = S * 10 ** 6
if PS == "giga":
    S = float(S)
    S = S * 10 ** 9
if PS == "milli":
    S = float(S)
    S = S * 10 ** -3
if PS == "micro (µ)":
    S = float(S)
    S = S * 10 ** -6
if PS == "nano":
    S = float(S)
    S = S * 10 ** -9

PC = input(
    "Prefix for Capacitance - kilo, mega, giga \nmilli, micro (µ), nano, pico, Farad:"
)
PC = PC.lower()
PC = PC.strip()
if PC != "farad":
    C = input("Capacitance (" + PC + "farad):")
    C = C.strip()
    C = float(C)
if PC == "farad":
    C = input("Capacitance (F)")
    C = C.strip()
    C = float(C)
if PC == "kilo":
    C = float(C)
    C = C * 10 ** 3
if PC == "mega":
    C = float(C)
    C = C * 10 ** 6
if PC == "giga":
    C = float(C)
    C = C * 10 ** 9
if PC == "milli":
    C = float(C)
    C = C * 10 ** -3
if PC == "micro (µ)":
    C = float(C)
    C = C * 10 ** -6
if PC == "nano":
    C = float(C)
    C = C * 10 ** -9
    print(C)
DT = input("Time Interval (S):")
DT = DT.strip()
DT = float(DT)

PR = input("Prefix for Resistance - kilo, mega, giga \nmilli, micro (µ), nano, Ohms:")
PR = PR.lower()
PR = PR.strip()
if PR != "ohms":
    R = input("Resistance (" + PR + "ohms):")
    R = R.strip()
    R = float(R)
if PR == "ohms":
    R = input("Resistance (V):")
    R = R.strip()
    R = float(R)
if PR == "kilo":
    R = float(R)
    R = R * 10 ** 3
if PR == "mega":
    R = float(R)
    R = R * 10 ** 6
if PR == "giga":
    R = float(R)
    R = R * 10 ** 9
if PR == "milli":
    R = float(R)
    R = R * 10 ** -3
if PR == "micro (µ) (µ)":
    R = float(R)
    R = R * 10 ** -6
if PR == "nano":
    R = float(R)
    R = R * 10 ** -9

# Time Constant
RC = R * C
RT = RC * 5
RT = int(RT)


def tabling():
    global T, VD, CV, C, R, IC, CM, Q
    table.append([T, VD, CV, C, R, IC, CM, Q])
    graphs1.append(T)
    graphs2.append(VD)


# While Less that Time Constant
while T <= RT:
    # voltage across capacitor is Q/C
    T = T + DT
    CV = Q / C
    # the difference between the supply voltage and the capacitor is what determines the current
    VD = S - CV
    VD = round(VD, 5)
    VD = float(VD)
    IC = VD / R
    # the current changes the amount of charge carried on to the capacitor in the time interval
    DQ = IC * DT
    Q = Q + DQ
    # Calls Function
    # Function so it can be callable
    tabling()


print(tabulate(table))
plt.plot(graphs1, graphs2)
plt.xlabel("Time (s)")
plt.ylabel("Voltage Diff (V)")

plt.show()
