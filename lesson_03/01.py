def every_nth(list, n):
    "returns every n-element in the list"
    return list[n-1::n] #slice to select every n-element
list = [1, 2, 3, 4, 5, 6]
n = 2
result = every_nth(list, n)
print(result)