import sys, string, math

def maxAltSeq(s) :
    c = s[0]
    L = [c]
    n = len(s)
    maxL = [c]
    for i in range(1,n) :
        if s[i] != c :
            c = s[i]
            L.append(c)
            if len(L) > len(maxL) :
                maxL = L[:]
        else :
            c = s[i]
            L = [c]
        s1 = ''.join(maxL)
        #print(i,s1,s[i])
    s2 = ''.join(maxL)
    i1 = s.index(s2)
    i2 = i1 + len(s2) - 1
    return [i1,i2,s2]

def cherry2(s) :
    L = list(s)
    n = len(s)
    i1,i2,x = maxAltSeq(s)
    #print(s,'x=',x,i1,i2)
    sum1 = 0
    if i1 > 0 :
        c = s[i1]
        for k1 in range(i1-1,-1,-1) :
            if s[k1] == c:
                if c == 'A':
                    L[k1] = 'B'
                    sum1 += 5
                    c = 'B'
                else:
                    L[k1] = 'A'
                    sum1 += 3
                    c = 'A'
            else:
                c = s[k1]
    if i2 < n-1 :
        c = s[i2]
        for k1 in range(i2+1,n) :
            if s[k1] == c :
                if c == 'A' :
                    L[k1] = 'B'
                    sum1 += 5
                    c = 'B'
                else :
                    L[k1] = 'A'
                    sum1 += 3
                    c = 'A'
            else :
                c = s[k1]
        s3 = ''.join(L)
        #print('cherry2 : ',s,s3,sum1)
    return sum1

n,k = input().split()
n,k = int(n),int(k)
sum1 = 0
L = [ input() for i in range(0,n)]
for i in range(0,n) :
    s = L[i]
    s1 = s.replace('R','A')
    s2 = s1.replace('G','B')
    sum1 += cherry2(s2)
print(sum1)
