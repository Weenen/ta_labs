from lab6_graph import N, EDGES, INF, build_adjacency, weight, fmt


class PriorityQueue:
    """Черга з пріоритетами: пріоритет вершини - поточна відстань dist."""
    def __init__(self):                       # CreatePQ()
        self.items = {}

    def insert(self, v, priority):            # InsertInPQ(pq, v, dist[v])
        self.items[v] = priority

    def size(self):                           # SizePQ(pq)
        return len(self.items)

    def extract_min(self):                    # ExtractMinFromPQ(pq)
        # мінімальна відстань; при рівності - менший номер вершини
        v = min(self.items, key=lambda x: (self.items[x], x))
        del self.items[v]
        return v

    def update(self, v, priority):            # UpdatePQ(pq, v, dist[v])
        self.items[v] = priority

    def show(self):
        pairs = sorted(self.items.items(), key=lambda p: (p[1], p[0]))
        return "{" + ",".join(f"({v},{fmt(d)})" for v, d in pairs) + "}"


def dijkstra(adj: dict, s: int, trace: bool = False) -> tuple:
    """
    Алгоритм Дейкстри (Листинг 6.1 методички).
    Повертає (pred, dist): попередники вершин та довжини найкоротших шляхів
    від стартової вершини s.
    """
    pred, dist = {}, {}
    pq = PriorityQueue()
    for v in adj:                      # ініціалізація масивів pred та dist
        pred[v] = -1
        dist[v] = INF if v != s else 0
        pq.insert(v, dist[v])

    def state():
        d = ",".join(fmt(dist[v]) for v in sorted(dist))
        p = ",".join(str(pred[v]) for v in sorted(pred))
        return f"dist=[{d}]  pred=[{p}]\n  pq={pq.show()}"

    if trace:
        print("Ініціалізація:\n  " + state())
    done = set()                       # вершини, вилучені з черги
    step = 0
    while pq.size() != 0:
        u = pq.extract_min()
        step += 1
        marks = [f"{v}(оброблена)" if v in done else str(v) for v, _ in adj[u]]
        if trace:
            print(f"Крок {step}: u={u}, dist[{u}]={fmt(dist[u])}; "
                  f"Adj({u}): {', '.join(marks)}")
        for v, _ in adj[u]:            # перебір суміжних вершин
            new = dist[u] + weight(adj, u, v)
            if dist[v] > new:          # умова релаксації
                if trace:
                    print(f"  v={v}: {fmt(dist[v])} > {dist[u]}+"
                          f"{weight(adj, u, v)}={new} -> dist[{v}]<-{new}, "
                          f"pred[{v}]<-{u}")
                dist[v] = new
                pred[v] = u
                pq.update(v, dist[v])
            elif trace and v not in done:
                print(f"  v={v}: {fmt(dist[v])} > {dist[u]}+"
                      f"{weight(adj, u, v)}={new} -> ні, без змін")
        done.add(u)
        if trace:
            print("  " + state())
    return pred, dist


def restore_path(pred: dict, s: int, v: int) -> list:
    """Відновлює шлях від s до v за масивом попередників."""
    path = [v]
    while v != s:
        v = pred[v]
        path.append(v)
    return path[::-1]


if __name__ == "__main__":
    start = 1
    adjacency = build_adjacency(N, EDGES)
    pred, dist = dijkstra(adjacency, start, trace=True)
    print(f"\nНайкоротші шляхи від вершини {start}:")
    print("З  В  Шлях             Вага")
    for v in range(1, N + 1):
        if v != start:
            path = " -> ".join(map(str, restore_path(pred, start, v)))
            print(f"{start}  {v}  {path:<15}  {dist[v]}")
