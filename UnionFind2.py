
#并查集 使用指针的方式，在合并的时候如果他们的parent不一样 那么被合并的那个值指向合并的那个值的parent
class UnionFind2:
    parent = []
    count = 0

    def __init__(self, n):
        self.count = n
        for i in range(0, n):
            self.parent.append(i)

    def find(self, p):
        assert 0 <= p < self.count
        while p != self.parent[p]:
            p = self.parent[p]
        return p

    def isConnected(self,p,q):
        return self.find(p) == self.find(q)

    def unionElements(self, p, q):
        rootP = self.find(p)
        rootQ = self.find(q)
        if rootP == rootQ:
            return
        self.parent[rootP] = rootQ
