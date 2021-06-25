#A
for w in range(int(input())):
    n,x=map(int,input().split())
    a=list(map(int,input().split()))
    if sum(a)%x!=0:
        print(n)
    else:
        c=0
        for i in range(n):
            if a[i]%x!=0:
                if c==0:
                    f=i
                    c=1
                l=i
        if c==0:
            print('-1')
        else:
            x=min(f+1,n-l)
            print(n-x)