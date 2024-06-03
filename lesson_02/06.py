def EMI(P, r, n):
    "finds a fixed payment amount"
    r_decimal = r / (12*100)
    emi = P * (r_decimal * (1 + r_decimal) ** n) / ((1 + r_decimal) ** n - 1)
    return emi
P = 500000
r = 8
n = 24
result = EMI(P, r, n)
print(f"EMI for {n} months: {result}")