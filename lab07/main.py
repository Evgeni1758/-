from functions import sum_digits, average, normalize_text, select_numbers


number = int(input("Введите целое число: "))
print(f"Сумма цифр: {sum_digits(number)}")


text = input("Введите целые числа одной строкой: ")
numbers = []
for token in text.split():
    numbers.append(int(token))

avg = average(numbers)
if avg is None:
    print("Среднее: Нет данных")
else:
    print(f"Среднее: {avg:.2f}")


raw_text = input("Введите произвольный текст: ")
print(f"Нормализованный текст: {normalize_text(raw_text)}")


threshold = int(input("Введите порог (целое неотрицательное): "))
result = select_numbers(numbers, threshold)
print(f"Выборка: {result}")
