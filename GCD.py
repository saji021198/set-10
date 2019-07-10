a,b=map(int,input().split())
c=[]
d=[]
gcd=1
for i in range (1,a+1):
    if (a%i)==0:
        c.append(i)
for j in range (1,b+1):
    if (b%j)==0:
        d.append(j)
for p in c:
    if p in d:
        gcd=gcd*p
print(gcd)
        
        
