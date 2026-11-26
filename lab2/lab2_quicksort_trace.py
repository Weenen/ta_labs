# Трасування швидкого сортування за схемою Хоара
def partition_trace(a, l, r, depth):
    pad = "  " * (depth + 1)
    comparisons = 0
    assignments = 0
    pivot = a[l]
    assignments += 1
    print(f"{pad}Вибираємо опорний елемент (pivot): {pivot}")
    i = l - 1
    j = r + 1
    assignments += 2
    while True:
        i += 1
        assignments += 1
        while a[i] < pivot:
            comparisons += 1
            i += 1
            assignments += 1
        comparisons += 1
        j -= 1
        assignments += 1
        while a[j] > pivot:
            comparisons += 1
            j -= 1
            assignments += 1
        comparisons += 1
        comparisons += 1
        if i >= j:
            print(f"{pad}Поточні індекси: i = {i}, j = {j}. Масив: {a[l:r + 1]}")
            print(f"{pad}Індекси перетнулися. Поділ завершено. Повертаємо j={j}.")
            return j, comparisons, assignments
        old_i, old_j = a[i], a[j]
        a[i], a[j] = a[j], a[i]
        assignments += 3
        print(f"{pad}Поточні індекси: i = {i}, j = {j}. Обмінюємо a[{i}] ({old_i}) і a[{j}] ({old_j}). Масив: {a[l:r + 1]}")


def quicksort_trace(a, l, r, depth=0):
    pad = "  " * depth
    print(f"{pad}Quicksort виклик: масив = {a}, l = {l}, r = {r}")
    comparisons = 0
    assignments = 0
    recursive_calls = 1
    if l < r:
        q, c1, a1 = partition_trace(a, l, r, depth)
        comparisons += c1
        assignments += a1
        c2, a2, r2 = quicksort_trace(a, l, q, depth + 1)
        c3, a3, r3 = quicksort_trace(a, q + 1, r, depth + 1)
        comparisons += c2 + c3
        assignments += a2 + a3
        recursive_calls += r2 + r3
        print(f"{pad}Після Quicksort для l={l}, r={r}: масив = {a}")
    else:
        return 0, 0, 0
    return comparisons, assignments, recursive_calls


print("--- Quicksort за схемою Хоара з трасуванням ---")
my_list = [90, 10, 15, 80, 100, 6, 57, 5, 29]
print("Оригінальний список:", my_list)
comps, assigs, calls = quicksort_trace(my_list, 0, len(my_list) - 1)
print()
print("Фінальний відсортований список:", my_list)
print("Загальна кількість порівнянь:", comps)
print("Загальна кількість присвоювань:", assigs)
print("Загальна кількість рекурсивних викликів:", calls)
