with open('d://lesia_Python/python_2/lesson_05/sales_2.txt', 'r') as file:
    lines = file.read().splitlines()

new_sentence = "If Peter Piper picked a peck of pickled peppers."

lines.insert(2, new_sentence)

with open('d://lesia_Python/python_2/lesson_05/sales_3.txt', 'w') as file:
    for line in lines:
        file.write(line + '\n')
