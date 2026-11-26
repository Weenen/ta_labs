# Трасування сортування злиттям (ітеративна та рекурсивна версії)
def merge_iter(a, left, mid, right):
    comparisons = 0
    assignments = 0
    n1 = mid - left
    n2 = right - mid
    L = a[left:mid]
    R = a[mid:right]
    assignments += n1 + n2
    it1 = 0
    it2 = 0
    k = left
    assignments += 3
    print(f"Об'єднуємо підмасиви: a[{left}:{mid}] ({L}) і a[{mid}:{right}] ({R})")
    while it1 < n1 and it2 < n2:
        comparisons += 1
        print(f"  Порівняння: {L[it1]} < {R[it2]}")
        if L[it1] < R[it2]:
            a[k] = L[it1]
            it1 += 1
        else:
            a[k] = R[it2]
            it2 += 1
        assignments += 1
        k += 1
        assignments += 1
    while it1 < n1:
        a[k] = L[it1]
        it1 += 1
        k += 1
        assignments += 1
    while it2 < n2:
        a[k] = R[it2]
        it2 += 1
        k += 1
        assignments += 1
    print(f"Масив після об'єднання: {a}")
    print("-" * 50)
    return comparisons, assignments


def merge_sort_iterative_trace(a):
    print("--- ІТЕРАТИВНА ВЕРСІЯ ---")
    print("Початковий масив:", a)
    print("-" * 50)
    n = len(a)
    comparisons = 0
    assignments = 0
    i = 1
    while i < n:
        j = 0
        while j < n - i:
            c, ac = merge_iter(a, j, j + i, min(j + 2 * i, n))
            comparisons += c
            assignments += ac
            j += 2 * i
        i *= 2
    print("Фінальний відсортований список:", a)
    print("Загальна кількість порівнянь:", comparisons)
    print("Загальна кількість присвоювань:", assignments)


def merge_rec(left, right, depth):
    pad = "  " * depth
    merged_arr = []
    comparisons = 0
    assignments = 0
    i = 0
    j = 0
    print(f"{pad}Зливаємо {left} та {right}")
    while i < len(left) and j < len(right):
        comparisons += 1
        ok = left[i] <= right[j]
        print(f"{pad}  Порівняння: {left[i]} <= {right[j]} -> {ok}. Додаємо {left[i] if ok else right[j]}")
        if ok:
            merged_arr.append(left[i])
            i += 1
        else:
            merged_arr.append(right[j])
            j += 1
        assignments += 1
    if i < len(left):
        print(f"{pad}  Додаємо залишок з лівого масиву: {left[i:]}")
    if j < len(right):
        print(f"{pad}  Додаємо залишок з правого масиву: {right[j:]}")
    while i < len(left):
        merged_arr.append(left[i])
        i += 1
        assignments += 1
    while j < len(right):
        merged_arr.append(right[j])
        j += 1
        assignments += 1
    print(f"{pad}Злиття завершено. Результат: {merged_arr}")
    return merged_arr, comparisons, assignments


def merge_sort_recursive_trace(arr, depth=0):
    pad = "  " * depth
    comparisons = 0
    assignments = 0
    recursive_calls = 0
    print(f"{pad}Розділяємо масив: {arr}")
    if len(arr) <= 1:
        return arr, comparisons, assignments, recursive_calls
    mid = len(arr) // 2
    assignments += 1
    recursive_calls += 2
    left_half, c1, a1, r1 = merge_sort_recursive_trace(arr[:mid], depth + 1)
    right_half, c2, a2, r2 = merge_sort_recursive_trace(arr[mid:], depth + 1)
    comparisons += c1 + c2
    assignments += a1 + a2
    recursive_calls += r1 + r2
    merged_arr, c_merge, a_merge = merge_rec(left_half, right_half, depth + 1)
    comparisons += c_merge
    assignments += a_merge
    return merged_arr, comparisons, assignments, recursive_calls


my_list = [90, 10, 15, 80, 100, 6, 57, 5, 29]
merge_sort_iterative_trace(my_list.copy())
print("=" * 50)
print("--- РЕКУРСИВНА ВЕРСІЯ ---")
res, c, a, r = merge_sort_recursive_trace(my_list.copy())
print("Фінальний відсортований список:", res)
print("Загальна кількість порівнянь:", c)
print("Загальна кількість присвоювань:", a)
print("Загальна кількість рекурсивних викликів:", r)
