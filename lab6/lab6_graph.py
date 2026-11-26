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


def build_weight_matrix(n: int, edges: list) -> list:
    """
    Вагова матриця W: w[i][j] - вага ребра (i, j), w[i][i] = 0,
    а за відсутності ребра - значення INF.
    """
    w = [[INF] * n for _ in range(n)]
    for i in range(n):
        w[i][i] = 0
    for u, v, weight in edges:
        w[u - 1][v - 1] = weight
        w[v - 1][u - 1] = weight   # граф неорієнтований
    return w


def build_adjacency(n: int, edges: list) -> dict:
    """
    Списки суміжності: для кожної вершини - список пар (сусід, вага),
    впорядкований за зростанням номера сусіда.
    """
    adj = {v: [] for v in range(1, n + 1)}
    for u, v, weight in edges:
        adj[u].append((v, weight))
        adj[v].append((u, weight))
    for v in adj:
        adj[v].sort()
    return adj


def weight(adj: dict, u: int, v: int) -> int:
    """Weight(G, u, v): вага ребра (u, v)."""
    for neighbour, w in adj[u]:
        if neighbour == v:
            return w
    return INF


def fmt(x) -> str:
    """Текстове подання числа: INF виводиться як символ нескінченності."""
    return "∞" if x == INF else str(x)
