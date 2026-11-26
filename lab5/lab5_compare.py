from lab5_graph import N, EDGES, build_adjacency_matrix
from lab5_prim import prim
from lab5_kruskal import kruskal


def normalize(edges: list) -> set:
    """Множина ребер без урахування порядку та напрямку."""
    return {(min(u, v), max(u, v), w) for u, v, w in edges}


if __name__ == "__main__":
    mst_prim = prim(build_adjacency_matrix(N, EDGES), start=1)
    mst_kruskal = kruskal(N, EDGES)

    print("Порядок додавання ребер за алгоритмом Пріма:")
    print("  " + ", ".join(f"({v},{u})={w}" for v, u, w in mst_prim))
    print("Порядок додавання ребер за алгоритмом Крускала:")
    print("  " + ", ".join(f"({u},{v})={w}" for u, v, w in mst_kruskal))

    print(f"Вартість за Прімом:    {sum(w for _, _, w in mst_prim)}")
    print(f"Вартість за Крускалом: {sum(w for _, _, w in mst_kruskal)}")
    same = normalize(mst_prim) == normalize(mst_kruskal)
    print(f"Множини ребер МКД співпадають: {same}")
