from lab4_open_hashing import (WORDS, M_DIV, M_MUL, key_sum, hash_division,
                               hash_multiplication, build_open_hash_table)
from lab4_closed_hashing import build_closed_hash_table


def search_open(table: list, key: str, m: int, hash_func) -> tuple:
    """
    Пошук у таблиці з ланцюжками. Повертає (знайдено, кількість порівнянь).
    Порівнянням вважаємо порівняння шуканого ключа з ключем елемента ланцюжка.
    """
    comparisons = 0
    for item in table[hash_func(key_sum(key), m)]:
        comparisons += 1
        if item == key:
            return True, comparisons
    return False, comparisons


def search_closed(table: list, key: str, m: int, hash_func) -> tuple:
    """
    Пошук у таблиці з відкритою адресацією (лінійне дослідження).
    Пошук зупиняється на знайденому ключі або на першій порожній комірці.
    """
    comparisons = 0
    start_address = hash_func(key_sum(key), m)
    for i in range(m):
        item = table[(start_address + i) % m]
        if item is None:           # порожня комірка: ключа в таблиці немає
            return False, comparisons
        comparisons += 1
        if item == key:
            return True, comparisons
    return False, comparisons


def analyze(title: str, table: list, m: int, hash_func, search_func,
            theory: float):
    """Кількість порівнянь для кожного слова, максимум і середнє значення."""
    print(f"\n=== {title} ===")
    print("№ слова | Слово    | h  | Порівнянь")
    results = []
    for number, word in enumerate(WORDS, start=1):
        found, comparisons = search_func(table, word, m, hash_func)
        results.append((word, comparisons))
        address = hash_func(key_sum(word), m)
        print(f"{number:<7} | {word:<8} | {address:2d} | {comparisons}")

    maximum = max(c for _, c in results)
    max_words = sorted({w for w, c in results if c == maximum})
    total = sum(c for _, c in results)
    alpha = len(WORDS) / m
    print(f"Максимум порівнянь: {maximum} (слово: {', '.join(max_words)})")
    average = total / len(results)
    print(f"Сума порівнянь: {total}, середнє: {total}/{len(results)} = "
          f"{average:.4f}")
    print(f"alpha = {len(WORDS)}/{m} = {alpha:.4f}; "
          f"теоретичне значення за лекцією: {theory:.4f}")


if __name__ == "__main__":
    for m, func, name in ((M_DIV, hash_division, "ділення, m=13"),
                          (M_MUL, hash_multiplication, "множення, m=16")):
        alpha = len(WORDS) / m
        # Відкрите хешування: S = 1 + alpha/2
        chains = build_open_hash_table(WORDS, m, func)
        analyze(f"Ланцюжки, метод {name}", chains, m, func, search_open,
                1 + alpha / 2)
        # Відкрита адресація, лінійне дослідження: S = 1/2 * (1 + 1/(1 - alpha))
        closed = build_closed_hash_table(WORDS, m, func)
        analyze(f"Відкрита адресація, метод {name}", closed, m, func,
                search_closed, 0.5 * (1 + 1 / (1 - alpha)))
