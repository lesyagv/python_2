def sym(line):
    "check the line for symmetry"
    str_length = len(line)
    if str_length % 2 == 0:
        half_length = str_length // 2
        for i in range(half_length):
            if line[i] != line[half_length + i]:
                return False
        return True
    else:
        return False
line = "khokho"
if sym(line):
    print("The entered string is symmetrical")
else:
    print("The entered string is not symmetrical")