import random


def margeSort1(arr, l, r):
    if l >= r:
        return
        middle = r - (r - l) / 2
        mergeSort1(arr, l, middle)
        mergeSort1(arr, middle + 1, r)
        merge(arr, l, middle, r)



def mergeSort(arr, n):
    margeSort1(arr, 0, n - 1)

# def mergeUP(arr, n):
#     i = 0
#     j = 0
#     for i in range(0, n, i + i):
#         for j in range(0, n, j + i + i):
#             merge(arr, i, i + j - 1,min(j + i + i - 1,n-1))


def merge(arr, l, middle, r):
    for i in range(l, r):
        aux = arr[i]

    i = l
    j = middle + 1
    for k in range(l, j):
        if i > middle:
            arr[k] = aux[j]
            j += 1

        elif j > r:
            arr[k] = aux[i]
            i += 1


        elif aux[i] > aux[j]:
            arr[k] = aux[j]
            j += 1

        else:
            arr[k] = aux[i]
            i += 1


if __name__ == '__main__':
    arr = set()
    for i in range(0, 100):
        arr.add(random.randint(0, 100))
    mergeSort(arr, 100)
    print(arr)
