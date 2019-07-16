import sys, string, math
from itertools import permutations,combinations

n,k = input().split()
n,k = int(n),int(k)
Lw = [ int(x) for x in input().split()]
Lv = [ int(x) for x in input().split()]
dic1 = {}
for i in range(0,n) :
    if Lw[i] not in dic1 :
        dic1[Lw[i]] = [Lv[i]]
    else :
        dic1[Lw[i]].append(Lv[i])
L3 = []
for i in range(1,n+1) :
    L2 = list(combinations(Lw,i))
    for x in L2 :
        if sum(x) <= k :
            L3.append(x)
max1 = 0
for x in L3 :
    sum1 = 0
    dic2 = {}
    for i in x :
        if i not in dic2 :
            dic2[i]= dic1[i][:]
    for i in x :
        if len(dic2[i]) == 1 :
            sum1 += dic2[i][0]
        else :
            a = max(dic2[i])
            sum1 += a
            dic2[i].remove(a)
    if sum1 > max1 :
        max1 = sum1
print(max1)
