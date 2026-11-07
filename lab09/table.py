# table.py

def row_sums(matrix):
    """
    Возвращает список сумм строк.
    Для пустой матрицы [] возвращает [].
    """
    if not matrix:
        return []
    
    return [sum(row) for row in matrix]


def column_sums(matrix):
    """
    Возвращает список сумм столбцов.
    Для пустой матрицы [] возвращает [].
    """
    if not matrix:
        return []
    
    # Определяем количество столбцов по первой строке
    cols_count = len(matrix[0])
    
    # Для каждого индекса столбца собираем значения из всех строк и суммируем
    return [sum(matrix[row][col] for row in range(len(matrix))) 
            for col in range(cols_count)]


def diagonal_pattern(size):
    """
    Создаёт квадратную таблицу size x size.
    Главная диагональ (row == column) = 0,
    выше диагонали (row < column) = 1,
    ниже диагонали (row > column) = 2.
    """
    table = []
    for row in range(size):
        new_row = []
        for col in range(size):
            if row == col:
                new_row.append(0)
            elif row < col:
                new_row.append(1)
            else:  # row > col
                new_row.append(2)
        table.append(new_row)
    return table