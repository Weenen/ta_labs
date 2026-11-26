from lab5_graph import N, EDGES, INF, build_adjacency_matrix


def edge_text(v: int, u: int, w: int) -> str:
    return f"({v},{u})={w}"


def prim(matrix: list, start: int = 1, trace: bool = False) -> list:
    """
    Алгоритм Пріма (варіант 1 з лекції). Повертає множину ребер E_T.
    На кожній ітерації обирається ребро з мінімальною вагою (v, u),
    де v належить V_T, а u належить V - V_T.
    """
    n = len(matrix)
    in_tree = [start]          # V_T: вершини, що вже включені до MST
    tree_edges = []            # E_T: ребра MST

    def show(last):
        """Рядок таблиці ходу алгоритму: V_T, E, V - V_T, e*, E_T."""
        tree_set = {frozenset((v, u)) for v, u, _ in tree_edges}
        border = []            # ребра, інцидентні вершинам V_T
        for v in range(1, n + 1):
            for u in range(v + 1, n + 1):
                w = matrix[v - 1][u - 1]
                if w == INF or frozenset((v, u)) in tree_set:
                    continue
                if v in in_tree and u not in in_tree:
                    border.append((v, u, w, ""))
                elif u in in_tree and v not in in_tree:
                    border.append((u, v, w, ""))
                elif v in in_tree and u in in_tree:
                    border.append((v, u, w, "c"))   # c - ребро утворює цикл
        border.sort(key=lambda e: (e[2], e[0], e[1]))   # за зростанням ваги
        rest = [v for v in range(1, n + 1) if v not in in_tree]
        print(f"V_T = {{{','.join(map(str, sorted(in_tree)))}}}")
        print("E   = " + (", ".join(edge_text(v, u, w) + (f" {m}" if m else "")
                                    for v, u, w, m in border) or "-"))
        print(f"V - V_T = {{{','.join(map(str, rest))}}}")
        print("e*  = " + (edge_text(*last) if last else "-"))
        print("E_T = " + (", ".join(edge_text(*e) for e in tree_edges) or "∅"))

    last = None
    if trace:
        print("--- Початковий стан ---")
        show(last)
    for step in range(1, n):
        # Пошук ребра з мінімальною вагою серед допустимих ребер
        best = None
        for v in in_tree:
            for u in range(1, n + 1):
                w = matrix[v - 1][u - 1]
                if u not in in_tree and w != INF:
                    if best is None or (w, v, u) < (best[2], best[0], best[1]):
                        best = (v, u, w)
        v, u, w = best
        in_tree.append(u)              # V_T <- V_T U {u*}
        tree_edges.append(best)        # E_T <- E_T U {e*}
        last = best
        if trace:
            print(f"--- Крок {step} ---")
            show(last)
    return tree_edges


if __name__ == "__main__":
    matrix = build_adjacency_matrix(N, EDGES)
    mst = prim(matrix, start=1, trace=True)
    print("\nМінімальне кістякове дерево (алгоритм Пріма):")
    for v, u, w in mst:
        print(f"({v},{u}) = {w}")
    print(f"Вартість МКД: {sum(w for _, _, w in mst)}")
