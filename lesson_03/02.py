def min_n(list, n):
    "returns the min n-elements"
    if n >= len(list):
        return sorted(list)
    return sorted(list)[:n]

list = [1, 2, 3]
n = 1
result1 = min_n(list, n)
print(result1)
n = 2
result2 = min_n(list, n)
print(result2)