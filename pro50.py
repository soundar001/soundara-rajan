A,B=map(int,input().split())
C=[]

for i in range(B):
  C.append(list(map(int,input().split())))
cost=10000000
h=0

for i in range(B):
  if C[i][0]==1:
    s1=C[i][1]
    p=C[i][2]
    for j in range(i+1,B):
      if C[j][0]==s1:
        s1=C[j][1]
        p=p+C[j][2]
    if p<cost and s1==A:
      cost=p
      h=h+1

if h==0:
  print(-1)
else:
  print(cost)
