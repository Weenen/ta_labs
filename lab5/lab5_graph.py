INF = float('inf')

# Кількість вершин графа варіанта 13 (вершини нумеруються від 1 до 8)
N = 8

# Ребра неорієнтованого зваженого графа варіанта 13: (u, v, вага).
# На рисунку варіанта вага ребер (1, 7) та (2, 5) не вказана, тому
# прийнято w(1, 7) = 1 та w(2, 5) = 6 (див. примітку до таблиці варіантів).
EDGES = [
    (1, 2, 2), (1, 3, 5), (1, 4, 7), (1, 7, 1),
    (2, 5, 6), (3, 5, 2), (3, 6, 4), (3, 7, 4),
    (4, 5, 9), (4, 6, 5), (4, 7, 9), (5, 6, 3),
    (6, 8, 1), (7, 8, 6),
]


def build_adjacency_matrix(n: int, edges: list) -> list:
    """
    Матриця суміжності зваженого графа: на перетині рядка i та стовпця j
    стоїть вага ребра (i, j), а за відсутності ребра - значення INF.
    """
    matrix = [[INF] * n for _ in range(n)]
    for u, v, w in edges:
        matrix[u - 1][v - 1] = w
        matrix[v - 1][u - 1] = w   # граф неорієнтований
    return matrix


# ---- Односпрямований список (структура даних з методички) ----
class ListNode:
    """Вузол списку: перша частина - дані, друга - покажчик на наступний."""
    def __init__(self, data, next_node=None):
        self.data = data
        self.next = next_node


def create_list():
    """L <- CreateList(): створює порожній список."""
    return None


def insert_in_list(head, data):
    """InsertInList(L, null, d): додає вузол з даними d на початок списку."""
    return ListNode(data, head)


def get_next_list_node(head, node):
    """GetNextListNode(L, node): перший вузол (node = None) або наступний."""
    return head if node is None else node.next


def build_adjacency_lists(n: int, edges: list) -> list:
    """
    Списки суміжності: для кожної вершини - список пар (сусід, вага).
    Сусіди додаються на початок списку в порядку зростання номерів,
    тому в списку вони йдуть у порядку спадання (як на рис. 5.2, в).
    """
    neighbours = [[] for _ in range(n)]
    for u, v, w in edges:
        neighbours[u - 1].append((v, w))
        neighbours[v - 1].append((u, w))
    lists = [create_list() for _ in range(n)]
    for i in range(n):
        for pair in sorted(neighbours[i]):
            lists[i] = insert_in_list(lists[i], pair)
    return lists


def display_matrix(matrix: list):
    """Виводить матрицю суміжності у зручному форматі."""
    n = len(matrix)
    print("Матриця суміжності (∞ - ребро відсутнє):")
    print("    " + "".join(f"{j:>3}" for j in range(1, n + 1)))
    for i, row in enumerate(matrix, start=1):
        cells = "".join(f"{('∞' if x == INF else x):>3}" for x in row)
        print(f"{i:>3} {cells}")


def display_lists(lists: list):
    """Виводить списки суміжності: вузол = (вершина, вага)."""
    print("Списки суміжності (вершина, вага):")
    for i, head in enumerate(lists, start=1):
        parts = []
        node = get_next_list_node(head, None)
        while node is not None:
            parts.append(f"({node.data[0]}, {node.data[1]})")
            node = get_next_list_node(head, node)
        print(f"{i}: " + " -> ".join(parts) + " -> null")


if __name__ == "__main__":
    display_matrix(build_adjacency_matrix(N, EDGES))
    print()
    display_lists(build_adjacency_lists(N, EDGES))
