import sys, string, math
n1 = int(input())
L1 = list(map(int,input().split()))
for i in range(len(L1)) :
    if L1.count(L1[i]) == 1 :
        print(L1[i])
        break
