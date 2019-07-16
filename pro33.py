import sys,string
s = input()
n = len(s)
for j in range(n-2,-1,-1) :
    for i in range(0,n-j) :
        li, ri = i,j+i
        s2 = s[li:ri + 1]
        if s2 > s :
            print(s2)
            sys.exit()
