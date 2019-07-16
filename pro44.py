tt1,tt2,tt3,tt4=map(int,input().split())
li=list(map(int,input().split()))
xi=[]
for i in range(0,len(li)):
    for j in range(i,len(li)):
        for k in range(j,len(li)):
            xi.append(tt2*li[i]+tt3*li[j]+tt4*li[k])
print(max(xi))
