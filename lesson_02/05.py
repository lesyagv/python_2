from decimal import Decimal
"calculates compound interest"
def complex_interest(P, r, n, t):

    A = P * (1 + (r / n)) ** (n * t)
    return A
P = Decimal(input("Основна сума: "))
r = Decimal(input("Річна відсоткова ставка: "))
n = int(input("Кількість разів наразування відсотків на рік: "))
t = int(input("Кількість років, за які нараховуються відсотки: "))

result = complex_interest(P, r, n, t)
print("Сума відсотків:", result)