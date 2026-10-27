text = input("Введите целые числа одной строкой: ")

numbers = []
for token in text.split():
    numbers.append(int(token))

if len(numbers) == 0:
    print("Нет данных")
else:
 
    maximum = numbers[0]
    for x in numbers:
        if x > maximum:
            maximum = x


    positions = []
    for index, value in enumerate(numbers):
        if value == maximum:
            positions.append(index)

    print(f"Максимум: {maximum}")
    print(f"Индексы: {positions}")
