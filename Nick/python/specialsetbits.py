#python 3.6.9
import math
def checkprime(k):
    if(k<=1):
        return False
    if(k==2 or k==3):
        return True
    if(k%2==0 or k%3==0):
        return False
    g=5
    while(g*g<=k):
        if(k%g==0 or k%(g+2)==0):
            return False
        g+=6
    return True
for t in range(int(input())):
    l,r=map(int,input().split())
    c=0
    rr=len(bin(r)[2:])
    ll=len(bin(l)[2:])
    if rr-ll<=1:
        for i in range(l,r+1):
            for j in range(0,31):
                if (1<<j)&i and checkprime(j+1):
                    c+=1
    else:
        for i in range(l,(1<<ll)):
            for j in range(0,31):
                if (1<<j)&i and checkprime(j+1):
                    c+=1
        for i in range((1<<(rr-1)),r+1):
            for j in range(0,31):
                if (1<<j)&i and checkprime(j+1):
                    c+=1
        for i in range(ll,rr-1):
            prev=0
            for j in range(1,i):
                temp=0
                temp+=(1<<j) if checkprime(j+1) else 0
                c=c+temp+prev
                prev=prev+temp+prev
            c+=(1<<i) if checkprime(i+1) else 0
    print(c)