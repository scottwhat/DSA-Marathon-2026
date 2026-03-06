"""Graph patterns: adjacency list, BFS/DFS, shortest path (unweighted), topological sort.

Run:
    python baseimplementations/graphs.py
"""

from __future__ import annotations

from collections import deque
from typing import Deque, Iterable


def build_adj_list(n: int, edges: Iterable[tuple[int, int]], *, directed: bool = False) -> list[list[int]]:
    g: list[list[int]] = [[] for _ in range(n)]
    for u, v in edges:
        g[u].append(v)
        if not directed:
            g[v].append(u)
    return g


def bfs_order(g: list[list[int]], start: int) -> list[int]:
    seen = [False] * len(g)
    q: Deque[int] = deque([start])
    seen[start] = True
    order: list[int] = []

    while q:
        u = q.popleft()
        order.append(u)
        for v in g[u]:
            if not seen[v]:
                seen[v] = True
                q.append(v)
    return order


def dfs_order(g: list[list[int]], start: int) -> list[int]:
    seen = [False] * len(g)
    order: list[int] = []

    def dfs(u: int) -> None:
        seen[u] = True
        order.append(u)
        for v in g[u]:
            if not seen[v]:
                dfs(v)

    dfs(start)
    return order


def shortest_path_unweighted(g: list[list[int]], start: int) -> list[int]:
    """Returns distances in unweighted graph; -1 if unreachable."""
    dist = [-1] * len(g)
    dist[start] = 0
    q: Deque[int] = deque([start])

    while q:
        u = q.popleft()
        for v in g[u]:
            if dist[v] == -1:
                dist[v] = dist[u] + 1
                q.append(v)
    return dist


def topo_sort_kahn(n: int, edges: Iterable[tuple[int, int]]) -> list[int]:
    """Topological sort for a DAG using Kahn's algorithm.

    Raises ValueError if a cycle exists.
    """
    g = [[] for _ in range(n)]
    indeg = [0] * n
    for u, v in edges:
        g[u].append(v)
        indeg[v] += 1

    q: Deque[int] = deque([i for i in range(n) if indeg[i] == 0])
    order: list[int] = []

    while q:
        u = q.popleft()
        order.append(u)
        for v in g[u]:
            indeg[v] -= 1
            if indeg[v] == 0:
                q.append(v)

    if len(order) != n:
        raise ValueError("Graph has a cycle; topological order does not exist")
    return order


def _test_graphs() -> None:
    # Undirected
    g = build_adj_list(6, [(0, 1), (0, 2), (1, 3), (3, 4)], directed=False)
    assert bfs_order(g, 0)[0] == 0
    assert dfs_order(g, 0)[0] == 0
    dist = shortest_path_unweighted(g, 0)
    assert dist[0] == 0
    assert dist[4] == 3
    assert dist[5] == -1

    # Directed DAG
    order = topo_sort_kahn(4, [(0, 1), (0, 2), (1, 3), (2, 3)])
    assert order.index(0) < order.index(1)
    assert order.index(0) < order.index(2)
    assert order.index(1) < order.index(3)
    assert order.index(2) < order.index(3)


if __name__ == "__main__":
    _test_graphs()
    print("graphs.py: OK")
