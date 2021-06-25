#boxchallenge
for t in range(int(input())):
    n=int(input())
    a=[i for i in range(1,n+1)]
    b=[]
    for q in range(int(input())):
        l=list(map(int,input().split()))
        if l[0]==1:
            while l[1]<=n and l[2]>0:
                b.append(l[1])
                l[1]+=1
                l[2]-=1
        else:
            k=0
            while k!=1 and l[1]<=n:
                if l[1] not in b:
                    print(l[1])
                    k=1
                l[1]+=1
            if k==0:
                print('-1')