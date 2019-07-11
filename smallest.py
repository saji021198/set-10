A,B=map(int,input().split())
C=list(map(int,input().split()))
count=0
for i in C:
    if (C[i]<C[i+1]):
       count=count+1
    if(count==B):
       print(i)
       break
