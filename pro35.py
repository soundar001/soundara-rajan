import sys,string
def cfreq(s) :
    dic1 = {}
    for c in s :
        dic1[c] = dic1.get(c,0) + 1
    return dic1

s = input()
n = len(s)
dic1 = cfreq(s)
Lk = list(dic1.keys())
for j in range(n-2,-1,-1) :
  
    for c in Lk :
        k = 0
        for i in range(0,n-j) :
            li, ri = i,j+i
            s2 = s[li:ri + 1]
           
            if c in s2 :
                k += 1
        if k == n-j :
          
            c2 = c
            k2 = k
            len2 = j+1
print(len2)
