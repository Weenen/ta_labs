# Сортування купою з підрахунком базових операцій.
# Правила підрахунку - ті самі, що й у Лістингу 2.3 (швидке сортування):
#  - кожне обчислення порівняння в умовах if/while -> comparisons += 1;
#  - кожне присвоєння змінній (в т.ч. індексам) -> assignments += 1;
#  - обмін елементів -> assignments += 3.
def sink(arr, i, n):
    comparisons = 0
    assignments = 0

    k = i
    assignments += 1
    while True:
        j = 2 * k + 1  # Індекс лівого дочірнього елемента
        assignments += 1

        comparisons += 1  # j >= n
        if j >= n:
            break

        comparisons += 1  # j + 1 < n
        if j + 1 < n:
            comparisons += 1  # arr[j + 1] > arr[j]
            if arr[j + 1] > arr[j]:
                j += 1
                assignments += 1

        comparisons += 1  # arr[k] >= arr[j]
        if arr[k] >= arr[j]:
            break

        arr[k], arr[j] = arr[j], arr[k]
        assignments += 3
        k = j
        assignments += 1
    return comparisons, assignments


def heapsort(arr):
    comparisons = 0
    assignments = 0

    n = len(arr)
    assignments += 1

    # Фаза 1: Побудова максимальної купи
    for i in range(n // 2 - 1, -1, -1):
        c, a = sink(arr, i, n)
        comparisons += c
        assignments += a

    # Фаза 2: Сортування
    for i in range(n - 1, 0, -1):
        arr[0], arr[i] = arr[i], arr[0]
        assignments += 3
        n -= 1
        assignments += 1
        c, a = sink(arr, 0, n)
        comparisons += c
        assignments += a
    return arr, comparisons, assignments


# Приклад використання (варіант 13)
my_list = [90, 10, 15, 80, 100, 6, 57, 5, 29]
sorted_list, comps, assigs = heapsort(my_list.copy())
print("Оригінальний список:", my_list)
print("Відсортований список:", sorted_list)
print(f"Загальна кількість порівнянь: {comps}")
print(f"Загальна кількість присвоювань: {assigs}")
