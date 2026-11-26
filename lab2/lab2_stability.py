# Перевірка стійкості: елементи - пари (ключ, мітка), порівнюється лише ключ
def merge(left, right):
    merged = []
    i = j = 0
    while i < len(left) and j < len(right):
        if left[i][0] <= right[j][0]:
            merged.append(left[i])
            i += 1
        else:
            merged.append(right[j])
            j += 1
    merged.extend(left[i:])
    merged.extend(right[j:])
    return merged


def merge_sort(arr):
    if len(arr) <= 1:
        return arr
    mid = len(arr) // 2
    return merge(merge_sort(arr[:mid]), merge_sort(arr[mid:]))


def partition(a, l, r):
    pivot = a[l][0]
    i = l - 1
    j = r + 1
    while True:
        i += 1
        while a[i][0] < pivot:
            i += 1
        j -= 1
        while a[j][0] > pivot:
            j -= 1
        if i >= j:
            return j
        a[i], a[j] = a[j], a[i]


def quicksort(a, l, r):
    if l < r:
        q = partition(a, l, r)
        quicksort(a, l, q)
        quicksort(a, q + 1, r)


def merge_iter(a, left, mid, right, strict):
    # допоміжна функція ітеративного злиття з Лістингу 2.1; strict=True - умова "<", False - умова "<="
    L = a[left:mid]
    R = a[mid:right]
    it1 = it2 = 0
    k = left
    while it1 < len(L) and it2 < len(R):
        take_left = L[it1][0] < R[it2][0] if strict else L[it1][0] <= R[it2][0]
        if take_left:
            a[k] = L[it1]
            it1 += 1
        else:
            a[k] = R[it2]
            it2 += 1
        k += 1
    while it1 < len(L):
        a[k] = L[it1]
        it1 += 1
        k += 1
    while it2 < len(R):
        a[k] = R[it2]
        it2 += 1
        k += 1


def merge_sort_iter(a, strict):
    n = len(a)
    i = 1
    while i < n:
        j = 0
        while j < n - i:
            merge_iter(a, j, j + i, min(j + 2 * i, n), strict)
            j += 2 * i
        i *= 2
    return a


data = [(2, "a"), (2, "b"), (1, "c")]
print("Вхідні дані:", data)
print("Сортування злиттям:", merge_sort(data.copy()))
qs = data.copy()
quicksort(qs, 0, len(qs) - 1)
print("Швидке сортування:", qs)
print("Ітеративне злиття, умова '<' (Лістинг 2.1):", merge_sort_iter(data.copy(), True))
print("Ітеративне злиття, умова '<=':", merge_sort_iter(data.copy(), False))
