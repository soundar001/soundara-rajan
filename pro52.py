import sys, string, math

n = 4
L = []
for i in range(0,n) :
    L.append([])
L2 = []
for i in range(0,n) :
    L[i] = [ int(x) for x in input().split()]
x1 = L[0][0]
y1 = L[0][1]
for i in range(1,n) :
    if L[i][0] != x1 and L[i][1] != y1 :
        x3 = L[i][0]
        y3 = L[i][1]
        i2 = i
        break

L3 = [0,i2]
for i in range(1,n) :
    if i != i2  :
        x2 = L[i][0]
        y2 = L[i][1]
        L3.append(i)
        break
for i in range(1,n) :
    if i not in L3  :
        x4 = L[i][0]
        y4 = L[i][1]
        L3.append(i)
        break

if x1==x2 :
    if y2==y3 and x4==x3 and y4==y1 :
        print('yes')
        sys.exit()
    else :
        print('no')
        sys.exit()
elif x1==x4 :
    if y4==y3 and x2==x3 and y2==y1 :
        print('yes')
        sys.exit()
    else :
        print('no')
        sys.exit()
