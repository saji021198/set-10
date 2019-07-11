A,B=map(int,input().split())
C=list(map(int,input().split()))
count=0
for i in C:
    if ((i%2)!=0):
       count=count+1
    if(count==B):
       print(i)
       break
       
