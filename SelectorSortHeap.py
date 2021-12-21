import random

def selectorSort(arr, n):
    for i in range(0, n):
        minIndex = i
        for j in range(i + 1, n):
            if arr[minIndex] > arr[j]:
                minIndex = j
        if minIndex != i:
            arr[minIndex], arr[i] = arr[i], arr[minIndex]
if __name__ == '__main__':
    arr = []
    for i in range(0, 10):
        arr.insert(i,random.randint(0, 10))
    selectorSort(arr, len(arr))
    print(arr)