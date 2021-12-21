import math


# reverses[indexes[i]] = i
# indexes[reverses[j]] = j
class ReverseIndexMaxHeap:
    count = 0
    capacity = 0
    data = [0]
    indexes = [0]
    reverses = [0]

    def initReverseIndexMaxHeap(self, capacity):
        self.capacity = capacity

        for i in range(1, capacity):
            self.reverses.insert(i, 0)

    def insert(self, i, item):
        assert 1 <= i + 1 <= self.capacity
        self.data.insert(i, item)
        self.indexes.insert(self.count + 1, i)
        self.reverses.append(self.count + 1)
        self.count += 1
        self.shiftUp(self.count)

    def isEmpty(self):
        return self.count == 0

    def size(self):
        return self.count

    def getItem(self, i):
        assert 1 <= i + 1 <= self.capacity
        assert (self.contain(i))
        return self.data[i]

    def shiftUp(self, k):
        while k > 1 and self.data[math.floor(k / 2)] < self.data[k]:
            self.indexes[math.floor(k / 2)], self.indexes[k] = self.indexes[k], self.indexes[math.floor(k / 2)]
            self.reverses[self.indexes[math.floor(k / 2)]] = math.floor(k / 2)
            self.reverses[self.indexes[k]] = k
            k = math.floor(k / 2)

    def extractMaxHeap(self):
        res = self.data[self.indexes[1]]
        self.indexes[1], self.indexes[self.count] = self.indexes[self.count], self.indexes[1]
        self.reverses[self.indexes[1]] = 1
        self.reverses[self.indexes[self.count]] = 0
        self.count -= 1
        self.shiftDown(1)
        return res

    def extractMaxHeapIndex(self):
        maxIndex = self.indexes[1]
        self.count -= 1
        self.shiftDown(1)
        return maxIndex

    def shiftDown(self, k):
        while 2 * k <= self.count:
            j = 2 * k
            if j + 1 <= self.count and self.data[self.indexes[j]] < self.data[self.indexes[j + 1]]:
                j = j + 1
            if self.data[self.indexes[j]] > self.data[self.indexes[k]]:
                self.indexes[j], self.indexes[k] = self.indexes[k], self.indexes[j]
                self.reverses[self.indexes[j]] = j
                self.reverses[self.indexes[k]] = k
                k = j

    def change(self, i, newItem):
        assert 1 <= i + 1 <= self.capacity
        assert (self.contain(i))
        self.data[i] = newItem
        j = self.reverses[i]
        self.shiftUp(j)
        self.shiftDown(j)

    def contain(self, i):
        return self.reverses[i + 1] != 0