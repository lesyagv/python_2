def middle_three(line):
    "creating a new line from the middle three letters of the input line"
    length = len(line)
    middle_index = length // 2
    return line[middle_index - 1:middle_index + 2] # we get the middle three letters#

str1 = "JhonDipPeta"
rez1 = middle_three(str1)
print("Case 1:", rez1)

str2 = "JaSonAy"
rez2 = middle_three(str2)
print("Case 2:", rez2)