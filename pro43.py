import sys, string, math

n = int(input())
L1 = [ int(x) for x in input().split()]
Lno = []
Ldup = []
Lin = []
for i in range(1,n+1) :
    if i not in L1 :
        Lno.append(i)
for i in L1 :
    if L1.count(i) > 1 and i not in Ldup :
        Ldup.append(i)
for i in range(0,n) :
    if L1[i] in Ldup :
        Lin.append(i)
cnt = len(Lno)
for i in range(0,n) :
    if len(Lno) == 0 :
        break
    if i in Lin :
        if i == Lin[0] :
            if Lno[0] < L1[i] :
                L1[i] = Lno.pop(0)
                Lin.pop(0)
            elif L1[i] in Ldup :
                Lin.pop(0)
                Ldup.remove(L1[i])
            else :
                L1[i] = Lno.pop(0)
                Lin.pop(0)


print(cnt)
print(*L1)
