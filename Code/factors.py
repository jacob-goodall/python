num = 0
def print_factors(x):
   print("The factors of",x,"are:")
   for i in range(1, x + 1):
       if x % i == 0:
           print(i)


num = float(input("Factors of what numbers:"))
num = round(num)
num = int(num)
num = abs(num)

print_factors(num)




