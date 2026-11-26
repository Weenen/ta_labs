from lab5_graph import N, EDGES


class DisjointSet:
    """Система неперетинних множин (Union-Find) для перевірки циклів."""
    def __init__(self, n: int):
        # на початку кожна вершина - окрема множина
        self.parent = list(range(n + 1))

    def find(self, x: int) -> int:
        if self.parent[x] != x:
            self.parent[x] = self.find(self.parent[x])
        return self.parent[x]

    def union(self, x: int, y: int):
        self.parent[self.find(x)] = self.find(y)


def kruskal(n: int, edges: list, trace: bool = False) -> list:
    """
    Алгоритм Крускала. Повертає множину ребер E_T.
    Ребра сортуються за неспадною вагою; ребро додається, якщо його кінці
    належать різним множинам (не утворюється цикл).
    """
    # Сортування ребер: за вагою, при рівності - за номерами вершин
    sorted_edges = sorted(edges, key=lambda e: (e[2], e[0], e[1]))
    if trace:
        print("Відсортовані ребра E: " +
              ", ".join(f"({u},{v})={w}" for u, v, w in sorted_edges))

    dsu = DisjointSet(n)
    tree_edges = []                # E_T
    ecounter = 0                   # лічильник ребер, доданих до E_T
    k = 0                          # індекс поточного ребра
    while ecounter < n - 1:
        u, v, w = sorted_edges[k]
        k += 1
        ru, rv = dsu.find(u), dsu.find(v)
        if ru != rv:               # E_T U {ребро} не створює цикл
            dsu.union(u, v)
            tree_edges.append((u, v, w))
            ecounter += 1
            decision = "додано до E_T"
        else:
            decision = "пропущено (цикл)"
        if trace:
            print(f"Крок {k:2d}: ребро ({u},{v})={w}: FIND({u})={ru}, "
                  f"FIND({v})={rv} -> {decision}")
    return tree_edges


if __name__ == "__main__":
    mst = kruskal(N, EDGES, trace=True)
    print("\nМінімальне кістякове дерево (алгоритм Крускала):")
    for u, v, w in mst:
        print(f"({u},{v}) = {w}")
    print(f"Вартість МКД: {sum(w for _, _, w in mst)}")
