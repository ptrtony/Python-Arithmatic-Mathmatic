import math

# 索引堆的数据结构
class IndexMaxHeap:
    data = [0]
    indexes = [0]
    capacity = 0
    count = 0

    def initIndexMaxHeap(self, n, capacity):
        self.capacity = capacity
        self.count = n + 1

    def isEmpty(self):
        return self.count == 0

    def size(self):
        return self.count

    def remove(self):
        self.count = 0
        self.capacity = 0
        self.data.clear()
        self.indexes.clear()

    # 传入的i对用户而言, 是从0开始索引的
    def insert(self, i, item):
        assert self.count + 1 < self.capacity
        assert 1 <= i + 1 < self.capacity
        self.data.insert(i, item)
        self.indexes.insert(self.count + 1, i)
        self.count += 1
        self.shiftUp(self.count)

    def shiftDown(self, k):
        while 2 * k <= self.count:
            j = 2 * k
            if j + 1 <= self.count and self.data[self.indexes[j]] < self.data[self.indexes[j + 1]]:
                j = j + 1
            if self.data[self.indexes[k]] < self.data[self.indexes[j]]:
                self.indexes[k], self.indexes[j] = self.indexes[j], self.indexes[k]
            k = j

    def shiftUp(self, k):
        while k > 1 and self.data[self.indexes[math.floor(k / 2)]] < self.data[self.indexes[k]]:
            self.indexes[math.floor(k / 2)], self.indexes[k] = self.indexes[k], self.indexes[math.floor(k / 2)]
            k = math.floor(k / 2)

    def extraMaxHeap(self):
        assert self.count > 0
        res = self.data[self.indexes[1]]
        self.indexes[1], self.indexes[self.count] = self.indexes[self.count], self.indexes[1]
        self.count -= 1
        self.shiftDown(1)
        return res

    def extractMaxIndex(self):
        maxIndex = self.indexes[1] - 1
        self.indexes[1], self.indexes[self.count] = self.indexes[self.count], self.indexes[1]
        self.count -= 1
        return maxIndex

    def change(self, i, newItem):
        i += 1
        self.data[i] = newItem
        for j in range(1, self.count + 1):
            if self.indexes[j] == i:
                self.shiftUp(j)
                self.shiftDown(j)
                return 
