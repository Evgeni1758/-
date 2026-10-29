def common_topics(first, second):
    """Общие темы двух списков (отсортированный список)."""
    return sorted(set(first) & set(second))


def all_topics(first, second):
    """Все уникальные темы двух списков (отсортированный список)."""
    return sorted(set(first) | set(second))


if __name__ == "__main__":
    a = ["python", "math", "history"]
    b = ["math", "physics", "python"]

    print(common_topics(a, b))  
    print(all_topics(a, b))    