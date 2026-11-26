# Перевірка стійкості сортування купою: елементи - пари (ключ, мітка),
# порівнюється лише ключ
def sink(arr, i, n):
    k = i
    while True:
        j = 2 * k + 1
        if j >= n:
            break
        if j + 1 < n and arr[j + 1][0] > arr[j][0]:
            j += 1
        if arr[k][0] >= arr[j][0]:
            break
        arr[k], arr[j] = arr[j], arr[k]
        k = j


def heapsort(arr):
    n = len(arr)
    for i in range(n // 2 - 1, -1, -1):
        sink(arr, i, n)
    for i in range(n - 1, 0, -1):
        arr[0], arr[i] = arr[i], arr[0]
        n -= 1
        sink(arr, 0, n)
    return arr


data = [(2, "a"), (2, "b"), (1, "c")]
print("Вхідні дані:", data)
print("Сортування купою:", heapsort(data.copy()))
