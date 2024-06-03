def max_n(list, n):
    "returns the max n-elements"
    if n >= len(list):
        return sorted(list, reverse=True)
    return sorted(list, reverse=True)[:n]
list = [1, 2, 3]
n = 1
result1 = max_n(list, n)
print(result1)
n = 2
result2 = max_n(list, n)
print(result2)



