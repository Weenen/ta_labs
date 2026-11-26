from lab6_graph import N, EDGES, INF, build_weight_matrix, fmt


def show_matrix(d: list, title: str):
    """Виводить матрицю відстаней у зручному форматі."""
    n = len(d)
    print(title)
    print("     " + "".join(f"{j:>3}" for j in range(1, n + 1)))
    for i, row in enumerate(d, start=1):
        print(f"{i:>3}  " + "".join(f"{fmt(x):>3}" for x in row))


def floyd(w: list, trace: bool = False, steps: bool = False) -> list:
    """
    Алгоритм Флойда (Листинг 6.2 методички).
    Матриця D перезаписується: D[i][j] = min{D[i][j], D[i][k] + D[k][j]}.
    """
    n = len(w)
    d = [row[:] for row in w]          # D <- W
    if steps:
        show_matrix(d, "D(0) = W:")
    for k in range(n):
        changed = []
        for i in range(n):
            for j in range(n):
                through_k = d[i][k] + d[k][j]
                if through_k < d[i][j]:
                    changed.append(f"d[{i + 1},{j + 1}]: "
                                   f"{fmt(d[i][j])} -> {through_k}")
                    d[i][j] = through_k
        if trace:
            print(f"k = {k + 1}: змінено елементів: {len(changed)}")
        if steps:
            show_matrix(d, f"D({k + 1}):")
    return d


if __name__ == "__main__":
    weights = build_weight_matrix(N, EDGES)
    distances = floyd(weights, trace=True, steps=True)
    print()
    show_matrix(distances, "Матриця відстаней D = D(8):")
