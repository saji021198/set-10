s=int(input())
d=list(map(int,input().split()))
for i in range(s-1):
    if(d[i]>d[i+1]):
        print(i)
