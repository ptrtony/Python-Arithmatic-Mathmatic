
import random
import math

# 二分查找法
def binarySearch(arr, n, t):
    l = 0
    r = n - 1
    # (l + r)/2
    while l <= r:
        mid = math.floor(r - (r - l) / 2)
        if arr[mid] == t:
            return mid

        if arr[mid] > t:
            #[l,mid-1]
            r = mid - 1

        else :
            #[mid+1,r]
            l = mid + 1

    return -1

if __name__ == '__main__':
    arr = []
    for i in range(0,100):
        arr.insert(i,random.randint(1,50))

    target = binarySearch(arr, len(arr),28)
    print(arr)
    print(target)