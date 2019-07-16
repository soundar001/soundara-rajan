import sys, string, math
def maxAltSeq(s1) :
    c = s1[0]
    L = [c]
    n = len(s1)
    maxL = [c]
    for i in range(1,n) :
        if s1[i] != c :
            c = s1[i]
            L.append(c)
            if len(L) > len(maxL) :
                maxL = L[:]
        else :
            c = s1[i]
            L = [c]
        s2 = ''.join(maxL)
    
    s3 = ''.join(maxL)
    i1 = s1.index(s3)
    i2 = i1 + len(s3) - 1
    return [i1,i2,s3]

def cherry2(s1) :
    L = list(s1)
    n = len(s1)
    i1,i2,x = maxAltSeq(s1)

    sum1 = 0
    if i1 > 0 :
        c = s1[i1]
        for k1 in range(i1-1,-1,-1) :
            if s1[k1] == c:
                if c == 'A':
                    L[k1] = 'B'
                    sum1 += 5
                    c = 'B'
                else:
                    L[k1] = 'A'
                    sum1 += 3
                    c = 'A'
            else:
                c = s1[k1]
    if i2 < n-1 :
        c = s1[i2]
        for k1 in range(i2+1,n) :
            if s1[k1] == c :
                if c == 'A' :
                    L[k1] = 'B'
                    sum1 += 5
                    c = 'B'
                else :
                    L[k1] = 'A'
                    sum1 += 3
                    c = 'A'
            else :
                c = s1[k1]
        s4 = ''.join(L)
       
    return sum1

n,k = input().split()
n,k = int(n),int(k)
sum1 = 0
L = [ input() for i in range(0,n)]
for i in range(0,n) :
    s1 = L[i]
    s2 = s1.replace('R','A')
    s3 = s2.replace('G','B')
    sum1 += cherry2(s3)
print(sum1)
