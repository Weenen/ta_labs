def insertion_sort_trace(arr):
    n = len(arr)
    comparisons = 0
    assignments = 0
    print("Початковий масив:", arr)
    print("-" * 30)

    for i in range(1, n):
        key = arr[i]
        assignments += 1
        print(f"Ітерація {i}:")
        print(f"  Елемент для вставки (key): {key}")
        print(f"  Відсортована частина: {arr[:i]}")

        j = i - 1
        assignments += 1

        while j >= 0 and arr[j] > key:
            comparisons += 1
            print(f"  Порівняння: {arr[j]} > {key}. True. Зсуваємо {arr[j]} вправо.")
            arr[j + 1] = arr[j]
            assignments += 1
            j -= 1
            assignments += 1

        if j >= 0:
            comparisons += 1
            print(f"  Порівняння: {arr[j]} > {key}. False. Цикл завершено.")
        else:
            print("  Досягнуто початку масиву. Цикл завершено.")

        arr[j + 1] = key
        assignments += 1
        print(f"  Вставка {key} на позицію {j + 1}.")
        print(f"  Масив після ітерації {i}:")
        print(f"  {arr}")
        print("-" * 30)

    print("Сортування завершено.")
    print("Фінальний відсортований масив:", arr)
    print("Загальна кількість порівнянь:", comparisons)
    print("Загальна кількість присвоєнь:", assignments)
    return arr, comparisons, assignments


insertion_sort_trace([90, 10, 15, 80, 100, 6, 57, 5, 29])
