# Допоміжні елементи (слова, алфавіт, хеш-функції) визначено в Лістингу 4.1
from lab4_open_hashing import (WORDS, M_DIV, M_MUL, key_sum,
                               hash_division, hash_multiplication)


def build_closed_hash_table(words: list, m: int, hash_func,
                            trace: bool = False) -> list:
    """
    Будує хеш-таблицю з відкритою адресацією (закрите хешування),
    використовуючи лінійне дослідження: h(K, i) = (h'(K) + i) mod m.
    """
    # 1. Ініціалізація таблиці: m порожніх комірок (None = "порожня")
    hash_table = [None] * m

    # 2. Обробка кожного слова
    for number, word in enumerate(words, start=1):
        k = key_sum(word)
        start_address = hash_func(k, m)
        visited = []

        # Лінійне дослідження: не більше m спроб
        for i in range(m):
            address = (start_address + i) % m
            if hash_table[address] is None:
                # Комірка вільна: вставляємо ключ
                hash_table[address] = word
                visited.append(f"{address} (вільна)")
                break
            # Комірка зайнята: фіксуємо її та переходимо до наступної
            visited.append(f"{address} ({hash_table[address]})")
        else:
            # Цей блок виконується, якщо цикл завершився без 'break'
            print(f"Помилка: таблиця заповнена. Не вдалося додати: {word}")

        if trace:
            path = ' -> '.join(visited)
            print(f"Крок {number}: {word:<8} K = {k:3d}  "
                  f"h = {start_address:2d}  дослідження: {path}")

    return hash_table


def display_hash_table(table: list, title: str):
    """Виводить хеш-таблицю у зручному форматі."""
    print(f"\n--- {title} ---")
    print("Індекс | Слово")
    print("-------|-------")
    for i, item in enumerate(table):
        value = item if item is not None else "(NULL)"
        print(f"{i:02d}     | {value}")


if __name__ == "__main__":
    # Метод ділення, m = 13
    print("=== Метод ділення: h(K) = K mod 13 ===")
    table_div = build_closed_hash_table(WORDS, M_DIV, hash_division,
                                        trace=True)
    display_hash_table(
        table_div, f"Хеш-таблиця (відкрита адресація, ділення, M={M_DIV})")

    # Метод множення, m = 16
    print("\n=== Метод множення: h(K) = floor(16 * (K*A mod 1)) ===")
    table_mul = build_closed_hash_table(WORDS, M_MUL, hash_multiplication,
                                        trace=True)
    display_hash_table(
        table_mul, f"Хеш-таблиця (відкрита адресація, множення, M={M_MUL})")
