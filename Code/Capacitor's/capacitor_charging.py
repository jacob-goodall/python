import matplotlib.pyplot as plt
from tabulate import tabulate

global DT, T, graphs

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
# Inputs
S = input("Supply Voltage (V):")
C = input("Capacitance Value (F):")
DT = input("Time Interval (S):")
R = input("Resistance Value (Ω): ")
# Making INT's so it doesn't break
S = int(S)
C = int(C)
DT = int(DT)
R = int(R)

# Function so it can be callable
def tables():
    table.append([T, VD, CV, C, R, IC, CM, Q])
    graphs1.append(T)
    graphs2.append(VD)


# Very big for loop
for x in range(1000000000000):
    # voltage across capacitor is Q/C
    CV = Q / C
    CV = round(CV, 5)
    T = T + DT
    # the difference between the supply voltage and the capacitor is what determines the current
    VD = S - CV
    VD = round(VD, 5)
    IC = VD / R
    # the current changes the amount of charge carried on to the capacitor in the time interval
    DQ = IC * DT
    Q = Q + DQ
    # Calls Function
    tables()

    # Breaks when VD = 0
    if VD == 0:
        break


print(tabulate(table))
plt.plot(graphs1, graphs2)
plt.xlabel("Time (s)")
plt.ylabel("Voltage Diff (V)")

plt.show()
