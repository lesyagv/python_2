def sort_dict_by_key(d, reverse=False):
    "a function that sorts the dictionary by key"
    
    return dict(sorted(d.items(), key=lambda item: item[0], reverse=reverse))

d = {'one': 1, 'three': 3, 'five': 5, 'two': 2, 'four': 4}

print(sort_dict_by_key(d))

print(sort_dict_by_key(d, True))
