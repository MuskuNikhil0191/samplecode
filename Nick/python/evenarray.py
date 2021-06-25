#evenarrray
for t in range(int(input())):
    n=int(input())
    a=list(map(int,input().split()))
    o=[]
    e=[]
    for i in range(n):
        if i%2==0:
            if a[i]%2!=0:
                o.append(a[i])
        else:
            if a[i]%2==0:
                e.append(a[i])
    if len(e)!=len(o):
        print('-1')
    else:
        print(len(e))