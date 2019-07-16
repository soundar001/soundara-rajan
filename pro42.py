import sys,string


def maxOfSegmentMins(L, n, k):
    if k == 1:
        return min(L)
    if k == 2 :
        return max(L[0], L[n - 1])
    return max(L)

n,k = input().split()
n,k = int(n),int(k)
L = [ int(x) for x in input().split()]
n = len(L)
ans = maxOfSegmentMins(L, n, k)
print(ans)
