

from table import transform

def main():
    
    matrix = [[-2, 0, 3], [4, -5, 6]]
    
    
    new_matrix = transform(matrix)
    
    
    print("Исходная таблица:")
    print(matrix)
    
    print("\nНовая таблица (чётные удвоены):")
    print(new_matrix)

if __name__ == "__main__":
    main()