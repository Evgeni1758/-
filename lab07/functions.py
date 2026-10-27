def sum_digits(number):
    """Сумма цифр модуля целого числа. Для нуля — 0."""
    n = abs(number)
    total = 0
    while n > 0:
        total = total + n % 10
        n = n // 10
    return total


def average(numbers):
    """Среднее списка чисел или None, если список пуст."""
    if len(numbers) == 0:
        return None
    total = 0
    for x in numbers:
        total = total + x
    return total / len(numbers)


def normalize_text(text):
    """Нижний регистр, без пробелов по краям, один пробел между словами."""
    return " ".join(text.split()).lower()


def select_numbers(numbers, threshold):
    """Новый список чисел, у которых |x| > threshold. Порядок и повторы сохраняются."""
    selected = []
    for x in numbers:
        if abs(x) > threshold:
            selected.append(x)
    return selected
