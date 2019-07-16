import sys, string, math
def lenOfLongIncSubArr(arr, n):
   
    max1 = 1
    len1 = 1

    for i in range(1, n):

        if (arr[i] > arr[i - 1]):
            len1 = len1 + 1
        else:
            if (max1 < len1):
                max1 = len1
            len1 = 1
   
    if (max1 < len1):
        max1 = len1
    return max1
n = int(input())
L = [ int(x) for x in input().split()]
print(lenOfLongIncSubArr(L, n))
