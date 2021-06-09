import matplotlib.pyplot as plt
#not needed to make graph just for table
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
# RC is Time Constant
# RT is Max Run Time

#Initiating Lists
table = [['Time (s)', 'Voltage difference', 'Capacitor Voltage' , 'Capacitance(F)', 'Resistance', 'Current(A)', 'Charge moved (C)', 'Total Charge (C)']]
graphs1 = []
graphs2 = []
#Initiating Values
Q = 0
T = 0
CM = 0

#Inputs and error prevention with try except statment

try:
    S = input("Supply Voltage (V):")
    C = input("Capacitance Value (F):")
    DT = input("Time Interval (S):")
    R = input("Resistance Value (Ω): ")
    #Making Floats's so it doesn't break
    S = float(S)
    C = float(C)
    DT = float(DT)
    R = float(R)
except ValueError:
    print("Has to be an INT or a Float \n Exiting to Omit Error")
    quit()

#Time Constant
RC = R * C
RT = RC * 5
RT = int(RT)


#Function so it can be callable
def tables():
    table.append([T, VD, CV, C, R, IC, CM, Q])
    graphs1.append(T)
    graphs2.append(VD)
#While Less that Time Contant
while T < RT:
    # voltage across capacitor is Q/C
    CV = Q / C
    T = T + DT
    # the difference between the supply voltage and the capacitor is what determines the current
    VD = S - CV
    IC = VD / R
    # the current changes the amount of charge carried on to the capacitor in the time interval
    DQ = IC * DT
    Q = Q + DQ
    #Calls Function
    tables()


print(tabulate(table))
plt.plot(graphs1, graphs2)
plt.xlabel('Time (s)')
plt.ylabel('Voltage Diff (V)')

plt.show()
