def sort_by_indexes(a, b, reverse=False):
    "combine elements of list a with indices from list b"
    paired = list(zip(a, b))
    "sort by indexes from list b"
    sorted_paired = sorted(paired, key=lambda x: x[1], reverse=reverse)
    "return the sorted elements from list a"
    sorted_a = [element[0] for element in sorted_paired]
    return sorted_a

a = ['eggs', 'bread', 'oranges', 'jam', 'apples', 'milk']
b = [3, 2, 6, 4, 1, 5]

print(sort_by_indexes(a, b))  # ['apples', 'bread', 'eggs', 'jam', 'milk', 'oranges']
print(sort_by_indexes(a, b, True))  # ['oranges', 'milk', 'jam', 'eggs', 'bread', 'apples']
