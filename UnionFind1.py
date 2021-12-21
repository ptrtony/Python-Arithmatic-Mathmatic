import random

#并查集  解决连接关系
class UnionFind1:
    id = []
    count = 0

    def __init__(self,n):
        self.count = n
        for i in range(0,n):
            self.id.append(i)

    def find(self,p):
        return self.id[p]

    def union(self,p,q):
        idP = self.id[p]
        idQ = self.id[q]

        if idP == idQ:
            return

        for i in range(0,self.count):
            if self.id[i] == idP:
                self.id[i] = idQ

    def isConnected(self,p,q):
        return self.id[p] == self.id[q]