from lab6_graph import N, EDGES, build_weight_matrix, build_adjacency
from lab6_dijkstra import dijkstra
from lab6_floyd import floyd

if __name__ == "__main__":
    adjacency = build_adjacency(N, EDGES)
    d_floyd = floyd(build_weight_matrix(N, EDGES))

    all_equal = True
    print("Порівняння рядків матриці відстаней Флойда з результатами "
          "алгоритму Дейкстри:")
    for s in range(1, N + 1):
        _, dist = dijkstra(adjacency, s)
        row_dijkstra = [dist[v] for v in range(1, N + 1)]
        same = row_dijkstra == d_floyd[s - 1]
        all_equal = all_equal and same
        print(f"  стартова вершина {s}: {row_dijkstra}  "
              f"співпадає з D[{s}]: {same}")
    print(f"Усі {N} рядків співпадають: {all_equal}")
