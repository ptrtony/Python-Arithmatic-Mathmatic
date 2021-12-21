
import random
import time
import UnionFind2
def unionFind1Helper(n):
    startTime = time.clock()
    uf = UnionFind2.UnionFind2
    uf.__init__(n)
    for i in range(0 ,n):
        a = random.randint(0 ,n)
        b = random.randint(0 ,n)
        uf.unionElements(a ,b)

    for k in range(0 ,n):
        a = random.randint(0 ,n)
        b = random.randint(0 ,n)
        uf.isConnected(a ,b)
    endTime = time.clock()

    print("执行的时间 " +(endTime - startTime))