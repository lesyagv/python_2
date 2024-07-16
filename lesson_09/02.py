def sum_by(lst, fn):
    "function maps each element of the list to a value"
    mapped_values = map(fn, lst)
    "calculate the sum of the obtained values"
    result = sum(mapped_values)
    return result

print(sum_by([{ 'n': 4 }, { 'n': 2 }, { 'n': 8 }, { 'n': 6 }], lambda v : v['n']))  # the result will be 20
