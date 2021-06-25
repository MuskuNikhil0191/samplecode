#python 3.6.9
def solve(a,c,res,n,lr,td,bd):
    if c==n:
        temp=[]
        for i in a:
            temp.append(tuple(i))
        res.append(temp)
        return
    for r in range(n):
        if lr[r] and bd[r+c] and td[n-1+c-r]:
            a[r][c]='Q'
            lr[r]=0
            bd[r+c]=0
            td[n-1+c-r]=0
            solve(a,c+1,res,n,lr,td,bd)
            a[r][c]='.'
            lr[r]=1
            bd[r+c]=1
            td[n-1+c-r]=1

n=4
a=[['.' for i in range(n)]for j in range(n)]
res=[]
lr,td,bd={},{},{}
for i in range(n):
    lr[i]=1
for i in range((2*(n-1))+1):
    bd[i]=1
    td[i]=1
solve(a,0,res,n,lr,td,bd)
print(*res)