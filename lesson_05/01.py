with open('d://lesia_Python/python_2/lesson_05/sales.txt', "r") as file:
    lines = file.readlines()

for line_number, line in enumerate(lines, start=1):
    if 'laptop' in line.lower():
        print(f"Номер рядка {line_number}: {line.strip()}")
        break
else:
    print("Інформація про товар 'laptop' відсутня в файлі.")
