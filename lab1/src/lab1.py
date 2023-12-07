def find_kth_largest(arr, k):
    # Перевірка на некоректні значення k.
    if k <= 0 or k > len(arr):
        # Якщо k менше або дорівнює 0 або більше за розмір масиву, повертаємо None.
        return None, None

    counter = [0]

    # Визначення функції для реалізації квіксорту з лічильником.
    def quick_sort(arr, counter):
        if len(arr) <= 1:
            return arr
        pivot = arr[len(arr) // 2]
        left = []
        right = []
        middle = []

        # Розподіл елементів навколо опорного елементу.
        for x in arr:
            if x < pivot:
                left.append(x)
            elif x == pivot:
                middle.append(x)
            else:
                right.append(x)

        # Збільшуємо лічильник операцій на кількість операцій у цій ітерації.
        counter[0] += len(left) + len(right) + len(middle)

        return quick_sort(left, counter) + middle + quick_sort(right, counter)

    # Застосовуємо квіксорт до вхідного масиву.
    sorted_arr = quick_sort(arr, counter)
    print("Відсортований масив:", sorted_arr)
    print("Кількість операцій у квіксорті:", counter[0])

    # Знаходимо k-ий найбільший елемент.
    kth_largest = sorted_arr[k - 1]

    # Знаходимо позицію (індекс) k-го найбільшого елемента у вихідному масиві.
    kth_largest_index = arr.index(kth_largest)

    # Повертаємо k-ий найбільший елемент і його позицію в масиві.
    return kth_largest, kth_largest_index


# Вхідний масив даних.
input_array = [15, 7, 22, 9, 36, 2, 42, 18]

# Значення k для пошуку k-го найбільшого елемента.
k_value = 3

# Викликаємо функцію find_kth_largest з вхідним масивом і k.
result, index = find_kth_largest(input_array, k_value)

# Виведення результату.
if result is not None:
    # Вивід результату, якщо k-ий найбільший елемент знайдений.
    print(f"Знайдений {k_value}-й найбільший елемент: {result}")
    print(f"Позиція {k_value}-го найбільшого елемента в масиві: {index}")
else:
    # Вивід повідомлення, якщо неможливо знайти k-ий найбільший елемент у масиві.
    print(f"Неможливо знайти {k_value}-й найбільший елемент у масиві.")