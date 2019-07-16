tt1,tt2,tt3,tt4=map(int,input().split())
l=list(map(int,input().split()))
x=[]
for i in range(0,len(l)):
    for j in range(i,len(l)):
        for k in range(j,len(l)):
            x.append(tt2*l[i]+tt3*l[j]+tt4*l[k])
print(max(x))
