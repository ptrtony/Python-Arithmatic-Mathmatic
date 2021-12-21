import random
import math


class MaxHeapHelp:
    count = 0
    data = [0]

    def __init__(self, capacity):
        self.capacity = capacity

    def isEmpty(self):
        return self.count == 0

    def size(self):
        return self.count

    def insertHeap(self, item):
        assert self.capacity >= self.count
        self.data.insert(self.count + 1, item)
        # self.data[self.count + 1] = item
        self.count += 1
        self.shiftUp()

    def shiftUp(self):
        k = self.count
        while k > 1 and self.data[math.floor(k / 2)] < self.data[k]:
            self.data[math.floor(k / 2)], self.data[k] = self.data[k], self.data[math.floor(k / 2)]
            k = math.floor(k / 2)

    def MaxHeapHelper(self, arr, m):
        z = math.floor((m - 1) / 2)
        for j in range(z,0):
            self.shiftDown1(arr, j, m)
        for k in range(m - 1,0):
            arr[0], arr[k] = arr[k], arr[0]
            self.shiftDown1(arr,0,k)

    def extractHeap(self):
        max = self.data[1]
        self.data[self.count], self.data[1] = self.data[1], self.data[self.count]
        self.count = self.count - 1
        self.shiftDown()
        return max

    def shiftDown(self):
        k = 1
        while k * 2 <= self.count:
            j = k * 2
            if k * 2 + 1 <= self.count and self.data[k * 2 + 1] > self.data[k * 2]:
                j += 1
            if self.data[k] > self.data[j]:
                break
            self.data[k], self.data[j] = self.data[j], self.data[k]
            k = j

    def shiftDown1(self, arr, k, m):
        while k * 2 + 1 < m:
            j = k * 2 + 1
            if j + 1 < m and arr[j] < arr[j + 1]:
                j += 1
            if arr[k] >= arr[j]:
                break
            arr[k], arr[j] = arr[j], arr[k]
            k = j


maxHeap = MaxHeapHelp(100)

if __name__ == '__main__':
    data = []

    for i in range(0, 10):
        data.append(random.randint(0, 100))

    # n = len(data)
    print(data)

    # for i in data:
    #     maxHeap.insertHeap(i)
    #
    # print(maxHeap.data)
    # for i in range(0, 10):
    #     data[i] = maxHeap.extractHeap()
    maxHeap.MaxHeapHelper(data, len(data))
    print(data)
