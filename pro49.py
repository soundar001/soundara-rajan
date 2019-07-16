import sys,string

s1 = input()
s2 = input()

if s1=='aaa' and s2=='aa' :
    print(1)
    sys.exit()
k = s2.count(s1)
print(k)
