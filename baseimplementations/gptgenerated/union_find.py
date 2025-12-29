"""Union-Find / Disjoint Set Union (DSU) with path compression + union by size.

Run:
    python baseimplementations/union_find.py
"""

from __future__ import annotations


class UnionFind:
    def __init__(self, n: int):
        if n < 0:
            raise ValueError("n must be >= 0")
        self.parent = list(range(n))
        self.size = [1] * n
        self.components = n

    def find(self, x: int) -> int:
        while x != self.parent[x]:
            self.parent[x] = self.parent[self.parent[x]]
            x = self.parent[x]
        return x

    def union(self, a: int, b: int) -> bool:
        ra, rb = self.find(a), self.find(b)
        if ra == rb:
            return False
        if self.size[ra] < self.size[rb]:
            ra, rb = rb, ra
        self.parent[rb] = ra
        self.size[ra] += self.size[rb]
        self.components -= 1
        return True

    def connected(self, a: int, b: int) -> bool:
        return self.find(a) == self.find(b)


def _test_union_find() -> None:
    uf = UnionFind(5)
    assert uf.components == 5
    assert uf.union(0, 1)
    assert uf.union(1, 2)
    assert uf.connected(0, 2)
    assert not uf.connected(0, 3)
    assert not uf.union(0, 2)
    assert uf.components == 3


if __name__ == "__main__":
    _test_union_find()
    print("union_find.py: OK")
