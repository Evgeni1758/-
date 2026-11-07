

def word_counts(text):
    """
    Возвращает словарь «слово → количество».
    Нижний регистр, разбиение по пробелам, удаление .,!?;: с краёв,
    пропуск пустых результатов.
    """
    if not text:
        return {}
    
    counts = {}
    words = text.lower().split()
    
    for raw_word in words:
        clean_word = raw_word.strip(".,!?;:")
        if clean_word:
            counts[clean_word] = counts.get(clean_word, 0) + 1
            
    return counts

def sorted_pairs(counts_dict):
    """
    Возвращает пары (слово, количество), отсортированные по алфавиту.
    """
    return sorted(counts_dict.items())




def common_topics(first, second):
    """
    Возвращает отсортированный список общих тем.
    """
    return sorted(list(set(first) & set(second)))

def all_topics(first, second):
    """
    Возвращает отсортированный список всех уникальных тем.
    """
    return sorted(list(set(first) | set(second)))



if __name__ == "__main__":
    print("ЗАДАЧА 1: Частоты слов")
  
    

    text = "Кот и пёс. Кот спит! Пёс, ест; кот — нет?"
    print(f"Исходный текст: {text}\n")
    

    counts = word_counts(text)
    print("Словарь (слово → количество):")
    print(counts)
    

    print("\nПары по алфавиту:")
    for word, count in sorted_pairs(counts):
        print(f"  {word}: {count}")
        
  
    print("ЗАДАЧА 2: Учебные интересы")
    

    list1 = ["математика", "физика", "информатика"]
    list2 = ["информатика", "химия", "физика"]
    
    print(f"Список 1: {list1}")
    print(f"Список 2: {list2}\n")
    
    print(f"Общие темы: {common_topics(list1, list2)}")
    print(f"Все темы: {all_topics(list1, list2)}")