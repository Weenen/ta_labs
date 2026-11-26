# Перевірка стійкості: елементи - пари (ключ, мітка), порівнюється лише ключ 

def selection_sort_key(arr): 

    n = len(arr) 

    for i in range(n - 1): 

        min_index = i 

        for j in range(i + 1, n): 

            if arr[j][0] < arr[min_index][0]: 

                min_index = j 

        if min_index != i: 

            arr[i], arr[min_index] = arr[min_index], arr[i] 

    return arr 

  

  

def insertion_sort_key(arr): 

    n = len(arr) 

    for i in range(1, n): 

        key = arr[i] 

        j = i - 1 

        while j >= 0 and arr[j][0] > key[0]: 

            arr[j + 1] = arr[j] 

            j -= 1 

        arr[j + 1] = key 

    return arr 

  

  

data = [(2, "a"), (2, "b"), (1, "c")] 

print("Вхідні дані:", data) 

print("Сортування вибором:", selection_sort_key(data.copy())) 

print("Сортування вставками:", insertion_sort_key(data.copy())) 