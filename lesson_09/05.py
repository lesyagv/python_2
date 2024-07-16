def average_by(lst, fn=lambda x: x):
    "calculates the average value of the list after matching each element to a value using the provided function"
    mapped_values = map(fn, lst) # use map to apply fn to each element of the list
       
    total = sum(mapped_values) # calculate the sum of the matched values
    
    average = total / len(lst) # calculate the average value
    
    return average
result = average_by([{ 'n': 4 }, { 'n': 2 }, { 'n': 8 }, { 'n': 6 }], lambda x: x['n'])
print(result)  # 5.0
