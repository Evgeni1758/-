# Фрагмент А: сумма чисел 5
print("=== Фрагмент А ===")
first = "2"
second = "3"
print("Типы до преобразования:", type(first).__name__, type(second).__name__)
first = int(first)
second = int(second)
print("Типы после преобразования:", type(first).__name__, type(second).__name__)
print("Сумма чисел:", first + second)

# Фрагмент Б: возраст через год
print("\n=== Фрагмент Б ===")
age = input("Возраст: ")
print("Тип до преобразования:", type(age).__name__)
age = int(age)
print("Тип после преобразования:", type(age).__name__)
print("Возраст через год:", age + 1)

# Фрагмент В: среднее трёх чисел
print("\n=== Фрагмент В ===")
first = 4
second = 7
third = 10
average = (first + second + third) / 3
print("Среднее:", average)
