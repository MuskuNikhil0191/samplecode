#python 3.6.9
def solve(a,ind,l,res,d,r,n):
    rr,cc=ind
    if rr==n-1 and cc==n-1:
        res.append(''.join(l))
    for i in r:
        tr,tc=i[0],i[1]
        nr,nc=rr+tr,cc+tc
        if nr<0 or nr>=n or nc<0 or nc>=n:
            continue
        if d[(nr,nc)]:
            continue
        if a[nr][nc]==0:
            continue
        l.append(i[2])
        d[(nr,nc)]=1
        solve(a,(nr,nc),l,res,d,r,n)
        l.pop()
        d[(nr,nc)]=0

a=[[1,0,0,0],[1,1,0,1],[1,1,0,0],[0,1,1,1]]
d={}
n=4
for i in range(n):
    for j in range(n):
        d[(i,j)]=0
d[(0,0)]=1
l,res=[],[]
r=[(1,0,'D'),(0,-1,'L'),(0,1,'R'),(-1,0,'U')]
solve(a,(0,0),l,res,d,r,n)
print(res)