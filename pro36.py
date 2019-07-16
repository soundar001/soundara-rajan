    
import sys,string
n1 = int(input())
L = [ int(x) for x in input().split()]
n1 = len(L)
cnt = 0
for i in range(0,n1-2) :
    for j in range(i+1, n1-1):
        for k in range(j+1, n1):
            if L[i] > L[j] > L[k] :
                cnt += 1
print(cnt)
