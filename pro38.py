import sys, string, math

n,k1 = input().split()
n,k1 = int(n),int(k1)
L = [ int(x) for x in input().split()]
L.sort()
cnt = 0
a = n // 3
#print(a)
for i in range(0,a) :
    L2 = L[3*i : 3*(i+1)]
    #print(L2)
    if 5-max(L2) >= k1 :
        cnt += 1
print(cnt)
