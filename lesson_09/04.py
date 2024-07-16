def average(*args):
    "calculates the average of two or more numbers"
    if len(args) < 2: # check whether the number of arguments is less than 2
       
        raise ValueError("Function requires at least two numbers to calculate the average") # If less, we cause an error with a message
    total_sum = sum(args) # use sum() to calculate the sum of all arguments
    avg = total_sum / len(args) # find the mean value
    
    return avg # Return the average value
print(average(*[1, 2, 3]))  
print(average(1, 2, 3))  
