# 并查集
# 并查集在合并的时候 通过值的层级进行优化，
class UnionFind3:
    parent = []
    count = 0
    sz = []

    def __init__(self, n):
        self.count = n

        for i in range(0, n):
            self.parent.append(i)
            self.sz.append(1)

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
        if self.sz[rootP] < self.sz[rootQ]:
            self.parent[rootP] = rootQ
            self.sz[rootQ] += self.sz[rootP]
        else:
            self.parent[rootQ] = rootP
            self.sz[rootP] += self.sz[rootQ]
