#naruto
import math
def gcd(a,b):
    if a==0:
        return b   
    return gcd(b%a,a)
for w in range(int(input())):
    n,m=map(int,input().split())
    a=list(map(int,input().split()))
    l1,h1=map(int,input().split())
    lcm=(a[0]*a[1])//gcd(a[0],a[1])
    for i in range(2,n):
        lcm=(lcm*a[i])//gcd(lcm,a[i])
    m1,res=0,0
    for i in range(1,m+1):
        ans=(lcm*i)//gcd(lcm,i)
        if ans>m1:
            m1=ans
            res=i
    s=[]
    for i in a:
        c=0
        while i%2==0:
            c+=1
            i=i/2
        if c==1:
            s.append(2)
        for j in range(3,int(math.sqrt(n))+1,2):
            c=0
            while(i%j==0):
                c+=1
                i=i/3
            if c==1:
                s.append(
        if i>2:
            s.append(i)
    s=list(dict.fromkeys(s))
    res=res+sum(s)     
    res1=l1&l1+1
    for i in range(l1+2,h1+1):
        res1=res1&i
    print(res,res1)
    print(res|res1)