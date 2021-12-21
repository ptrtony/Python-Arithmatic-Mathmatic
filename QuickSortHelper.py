import random


def quickSort(arr, n):
    __quickSort(arr, 0, n)


def __quickSort(data, l, r):
    if l >= r: return
    p = partition(data, l, r)
    __quickSort(data, l, p -1)
    __quickSort(data, p + 1, r)


def partition(data, l, r):
    randomIndex = random.randint(l, r)
    data[randomIndex], data[l] = data[l], data[randomIndex]
    v = data[l]
    j = l
    for i in range(l+1, r):
        if data[i] < v:
            data[i], data[j + 1] = data[j + 1], data[i]
            j += 1
    data[l], data[j] = data[j], data[l]
    return j

def quickSort1(data,n):
    __quickSort1(data,0,n)

def __quickSort1(data,l,r):
    if l >= r : return
    p = partition1(data,l,r)
    __quickSort1(data,l.p-1)
    __quickSort1(data,p+1,r)


def partition1(data,l,r):
    randomIndex = random.randint(l, r)
    data[l], data[randomIndex] = data[randomIndex], data[l]
    v = data[l]
    i = l + 1
    j = r
    while True:
        if i <= r and data[i] < v:
            i += 1
        if j >= l + 1 and data[j] > v:
            j -= 1
        if i > j: break
        data[i], data[j] = data[j], data[i]
        i += 1
        j -= 1
    data[l], data[j] = data[j], data[l]
    return j







if __name__ == '__main__':
    data = []
    for i in range(0, 100):
        data.append(random.randint(0, 100))
    print(data)
    quickSort1(data, len(data) - 1)
    print(data)
