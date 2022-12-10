N=int(input("Enter the number of eggs:"))
a=[]
for i in range(N):
  l=[] 
  for j in range(N):
    l.append(0)
  a.append(l)

k=1
i=0
j=N//2

while(k<=N*N):    
  a[i][j]=k
  k=k+1
  ni=(i-1)%N
  nj=(j+1)%N
  if(a[ni][nj]!=0):
    i=(i+2)%N
    j=(j-1)%N
  else:
    i=ni
    j=nj
print(a)

