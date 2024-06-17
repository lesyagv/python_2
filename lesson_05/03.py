from pathlib import Path

def count_file_stats(file_path):
    try:
        path = Path(file_path)
        text = path.read_text()
        num_lines = text.count('\n') + 1 if text else 0
        num_words = len(text.split())
        num_chars = len(text)
        return f"Кількість рядків: {num_lines}\nКількість слів: {num_words}\nКількість символів: {num_chars}"
    except FileNotFoundError:
        return "Файл не знайдено."
    except Exception as e:
        return f"Помилка: {e}"

file_path = "d://lesia_Python/python_2/lesson_05/sales_2.txt"
result = count_file_stats(file_path)
print(result)
