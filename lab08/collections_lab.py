def word_counts(text):
    
    if not text:
        return {}
    counts = {}
    for raw in text.lower().split():
        word = raw.strip(".,!?;:")
        if word:
            counts[word] = counts.get(word, 0) + 1
    return counts


def sorted_pairs(counts):
    
    return sorted(counts.items())


if __name__ == "__main__":
    text = "Кот и пёс. Кот спит! Пёс, ест; кот — нет?"
    counts = word_counts(text)
    print(counts)
    for word, n in sorted_pairs(counts):
        print(f"{word}: {n}")

    print(word_counts(""))  # {}