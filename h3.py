import sys, string, math
n1 = int(input())
L1 = list(map(int,input().split()))
L2 = []
for i in range(n1) :
    if L1[i] == i :
    L2.append(i)
L3 = sorted(L2)
if len(L3) == 0 : 
  print(-1)
else :    
  print(*L3)
