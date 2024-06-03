def roll(lst, n):
    "moves the start of the number of n elements in the list lst"
    return lst[-n:] + lst[:-n]

list = [1, 2, 3, 4, 5]
n = 2
result1 = roll(list, n)
print(result1)
list = [1, 2, 3, 4, 5]
n = -2
result2 = roll(list, n)
print(result2)