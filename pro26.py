    
import sys, string, math


global maximum

def lis2(arr, n):

    global maximum

    if n == 1: return 1

    maxEndingHere = 1

    for i in range(1, n):
        res = lis2(arr, i)
        if arr[i - 1] < arr[n - 1] and res + 1 > maxEndingHere:
            maxEndingHere = res + 1
    maximum = max(maximum, maxEndingHere)
    return maxEndingHere

def lis(arr):
  
    global maximum
    n = len(arr)
    maximum = 1
    lis2(arr, n)
    return maximum

n = int(input())
L = [ int(x) for x in input().split()]
print(lis(L))
