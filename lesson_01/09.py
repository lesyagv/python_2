f = float(input("Enter the desired future value: "))
r = float(input("Enter the annual interest rate: "))
n = float(input("Enter the number of years the money will grow: "))
print("You will nee4d to deposit this amount:", round((f/(1+r)**n), 2))