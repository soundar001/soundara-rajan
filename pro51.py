def ch(l):
        c=1
        
        for x in range(0,len(l)-1):
                if l[x]!=l[x+1]:
                        c=c+1
                else:
                    break
        return c
num=int(input())
lin=list(map(int,input().split()))

for x in range(0,len(lin)):
        if lin[x]>0:
                lin[x]=1
        else:
             lin[x]=0
A=""

for x in range(0,len(lin)):
        B=lin[x::]
        A=A+str(ch(B))+" "
print(A.strip())
