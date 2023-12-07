def naive_string_search(text, pattern):
    comparisons = 0
    found_index = -1

    # Знаходимо індекс останнього входження "pattern" в "text"
    for i in range(len(text) - len(pattern) + 1, -1, -1):
        if text[i] == pattern[0]:
            # Якщо знайдено перший символ, перевіряємо, чи збігаються всі наступні символи
            for j in range(1, len(pattern)):
                comparisons += 1
                if text[i + j] != pattern[j]:
                    break
            else:
                # Якщо всі символи збігаються, зберігаємо індекс
                found_index = i
                break

    return found_index, comparisons


text = "texttexttexttext"
pattern = "text"
result_index, comparisons_count = naive_string_search(text, pattern)

print(f"Останнє входження '{pattern}' в '{text}' знаходиться на індексі {result_index}.")
print(f"Кількість порівнянь: {comparisons_count}")
