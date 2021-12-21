# 并查集
class UnionFind4:
    parent = []
    count = 0
    rank = []

    def __init__(self, n):
        self.count = n

        for i in range(0, n):
            self.parent.append(i)
            self.rank.append(1)

    def find(self, p):
        assert 0 <= p < self.count
        while p != self.parent[p]:
            p = self.parent[p]
        return p

    def isConnected(self, p, q):
        return self.find(p) == self.find(q)

    def unionElements(self, p, q):
        rootP = self.find(p)
        rootQ = self.find(q)
        if rootP == rootQ:
            return
        if self.rank[rootP] < self.rank[rootQ]:
            self.parent[rootP] = rootQ
        elif self.rank[rootP] > self.rank[rootQ]:
            self.parent[rootQ] = rootP
        else:
            self.parent[rootP] = rootQ
            self.rank[rootQ] += 1
