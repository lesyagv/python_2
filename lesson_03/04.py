def includes_any(lst, values):
    "checks if any element from the values list is included in the lst"
    for value in values:
        if value in lst:
            return True
    return False

lst = [1, 2, 3, 4]
values = [2, 9]
result1 = includes_any(lst, values)
print(result1)
lst= [1, 2, 3, 4]
values = [8, 9]
result2 = includes_any(lst, values)
print(result2)