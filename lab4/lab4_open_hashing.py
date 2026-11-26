import math

# Розміри хеш-таблиць: m = 13 (метод ділення) та m = 16 (метод множення)
M_DIV = 13
M_MUL = 16
# Константа методу множення (за Кнутом): A = (sqrt(5) - 1) / 2 = 0.6180339887...
A = (math.sqrt(5) - 1) / 2

# Вхідні слова (варіант 13):
# "Людина без рідного краю — як соловей без гнізда"
WORDS = ["Людина", "без", "рідного", "краю", "як", "соловей", "без", "гнізда"]

# Словник позицій літер українського алфавіту (рисунок 4.3 методички)
LETTER_POSITIONS = {
    'А': 1, 'Б': 2, 'В': 3, 'Г': 4, 'Ґ': 5, 'Д': 6, 'Е': 7, 'Є': 8,
    'Ж': 9, 'З': 10, 'И': 11, 'І': 12, 'Ї': 13, 'Й': 14, 'К': 15,
    'Л': 16, 'М': 17, 'Н': 18, 'О': 19, 'П': 20, 'Р': 21, 'С': 22,
    'Т': 23, 'У': 24, 'Ф': 25, 'Х': 26, 'Ц': 27, 'Ч': 28, 'Ш': 29,
    'Щ': 30, 'Ь': 31, 'Ю': 32, 'Я': 33
}


def key_sum(word: str) -> int:
    """
    Перетворює слово на ціле невід'ємне число K:
    K = сума номерів позицій літер слова в алфавіті.
    """
    total = 0
    for char in word.upper():
        # Якщо символ не літера (наприклад, дефіс), повертаємо 0
        total += LETTER_POSITIONS.get(char, 0)
    return total


def hash_division(k: int, m: int) -> int:
    """Метод ділення: h(K) = K mod m."""
    return k % m


def hash_multiplication(k: int, m: int) -> int:
    """Метод множення: h(K) = floor(m * (K*A mod 1))."""
    fractional_part = (k * A) % 1
    return int(m * fractional_part)


def build_open_hash_table(words: list, m: int, hash_func,
                          trace: bool = False) -> list:
    """
    Будує хеш-таблицю з роздільними ланцюжками (відкрите хешування).
    """
    # 1. Ініціалізація таблиці: m порожніх ланцюжків
    hash_table = [[] for _ in range(m)]

    # 2. Обробка кожного слова
    for number, word in enumerate(words, start=1):
        k = key_sum(word)
        address = hash_func(k, m)
        if trace:
            print(f"Крок {number}: {word:<8} K = {k:3d}  h = {address:2d}  "
                  f"ланцюжок до вставки: {hash_table[address]}")
        # Додавання слова в кінець відповідного ланцюжка
        hash_table[address].append(word)

    return hash_table


def display_hash_table(table: list, title: str):
    """Виводить хеш-таблицю у зручному форматі."""
    print(f"\n--- {title} ---")
    for i, chain in enumerate(table):
        print(f"Індекс {i:02d}: {chain}")


if __name__ == "__main__":
    # Метод ділення, m = 13
    print("=== Метод ділення: h(K) = K mod 13 ===")
    table_div = build_open_hash_table(WORDS, M_DIV, hash_division, trace=True)
    display_hash_table(table_div,
                       f"Результат хешування (метод ділення, M={M_DIV})")

    # Метод множення, m = 16
    print("\n=== Метод множення: h(K) = floor(16 * (K*A mod 1)) ===")
    table_mul = build_open_hash_table(WORDS, M_MUL, hash_multiplication,
                                      trace=True)
    display_hash_table(table_mul,
                       f"Результат хешування (метод множення, M={M_MUL})")
