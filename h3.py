import sys, string, math
n1 = int(input())
L1 = list(map(int,input().split()))
L3 = []
for i in range(n1) :
    if L1[i] == i :
    L3.append(i)
L = sorted(L3)
if len(L) == 0 : 
  print(-1)
else :    
  print(*L)
