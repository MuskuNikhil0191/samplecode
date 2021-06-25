arr=[[1,2,3],[4,5,6],[7,8,9]]
ans=0
def check(a):
    if sum(a[0])!=15 or sum(a[1]!=15) or sum(a[2])!=15:
        return False
    ds=0
    for i in range(3):
        s=0
        for j in range(3):
            if i==j:
                ds+=a[i][j]
            s+=a[j][i]
        if s!=15:
            return False
    if ds!=15:
        return False
    ds=0
    j=2
    for i in range(3):
        ds+=a[i][j]
    if ds!=15:
        return False
    return True
def cost(arr,a):
    c=0
    for i in range(3):
        for j in range(3):
            c+=abs(arr[i][j]-a[i][j])
    return c
def solve(a,b,ind):
    ans=0
    print(ind)
    for i in range(1,10):
        if ind[0]==3:
            if check(a):
                ans=min(ans,cost(arr,a))
            return
        if b[i]==False:
            a[ind[0]][ind[1]]=i
            b[i]=True
            ind[1]+=1
            if ind[1]==3:
                ind[0]+=1
                ind[1]=0
            solve(a,b,ind)
            a[ind[0]][ind[1]]=0
            b[i]=False
    return ans
            
a=[1,2,3,4,5,6,7,8,9]
b=[False for i in range(9)]
b.insert(0,True)
n=3
ind=[0,0]
a=[[0 for i in range(3)]for j in range(3)]
print(solve(a,b,ind))
