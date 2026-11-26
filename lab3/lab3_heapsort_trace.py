def swap(arr, i, j):
    arr[i], arr[j] = arr[j], arr[i]


def sink_trace(arr, i, n):
    k = i
    print(f"Починаємо 'занурювати' елемент: {arr[i]} з індексу {i}")
    while True:
        j = 2 * k + 1
        if j >= n:
            print(f"Елемент {arr[k]} на індексі {k} досяг кінця купи. Завершуємо.")
            break
        if j + 1 < n and arr[j + 1] > arr[j]:
            print(f" Порівнюємо {arr[j]} (лівий) та {arr[j + 1]} (правий). Обираємо {arr[j + 1]}")
            j += 1
        else:
            print(f"  Обираємо лівий дочірній елемент: {arr[j]} на індексі {j}")
        if arr[k] >= arr[j]:
            print(f"  {arr[k]} (батько) >= {arr[j]} (найбільший дочірній). Елемент на своєму місці.")
            break
        print(f"  Міняємо місцями {arr[k]} (батько) та {arr[j]} (дочірній)")
        swap(arr, k, j)
        print(f"  Масив після обміну: {arr}")
        k = j


def heapsort_trace(arr):
    n = len(arr)
    print("Початковий масив:", arr)
    print()
    print("--- Фаза 1: Побудова максимальної купи ---")
    for i in range(n // 2 - 1, -1, -1):
        sink_trace(arr, i, n)
        print("-" * 33)
    print()
    print("Масив після побудови купи:", arr)
    print()
    print("--- Фаза 2: Сортування ---")
    for i in range(n - 1, 0, -1):
        print(f"Міняємо місцями корінь ({arr[0]}) та останній елемент ({arr[i]})")
        swap(arr, 0, i)
        n -= 1
        print(f"Розмір купи зменшився до {n}. Відновлюємо властивості купи.")
        sink_trace(arr, 0, n)
        print("Масив на поточному кроці:", arr)
        print()
    print("Відсортований масив:", arr)
    return arr


heapsort_trace([90, 10, 15, 80, 100, 6, 57, 5, 29])
