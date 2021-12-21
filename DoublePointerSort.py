# aIndex=5
import math
#双指针索引算法
a = [1, 3, 5, 7, 9,34]
# bIndex=5
b = [2, 4, 6, 8, 10,56]
c = []
aIndex = 0
bIndex = 0

# b>a  时间复杂度  b  a> b    a     n
while True:
    if aIndex >= len(a) and bIndex < len(b):
        c.append(b[bIndex])
        bIndex += 1

    elif bIndex >= len(b) and aIndex < len(a):
        c.append(a[aIndex])
        aIndex += 1
    elif aIndex < len(a) and bIndex < len(b) and a[aIndex] >= b[bIndex]:
        c.append(b[bIndex])
        bIndex += 1
    elif aIndex < len(a) and bIndex < len(b) and a[aIndex] <= b[bIndex]:
        c.append(a[aIndex])
        aIndex += 1


    elif len(c) == aIndex + bIndex :
        break

if __name__ == '__main__':
    print(c)
