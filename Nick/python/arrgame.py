import numpy as np
for _ in range(int(input())):
    n,k=map(int,input().split())
    a=np.array(list(map(int,input().split())))
    a[0:]-=k
    i=1
    a=np.cumsum(a)
    r=np.where(a<0)[0]
    if len(r)>0:
        print(r[0]+1)
    else:
        print(n+(a[-1]//k)+1)