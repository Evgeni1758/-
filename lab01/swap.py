# Ввод названий двух аудиторий
first_room = input("Название первой аудитории: ")
second_room = input("Название второй аудитории: ")

# Вывод исходных значений
print("Исходные значения:")
print("first_room =", first_room)
print("second_room =", second_room)

# Обмен значениями через третью переменную
temp = first_room
first_room = second_room
second_room = temp

# Вывод результата после обмена
print("После обмена:")
print("first_room =", first_room)
print("second_room =", second_room)
