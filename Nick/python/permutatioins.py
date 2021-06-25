def solve(a,ind,l,res,d):
    if len(l)==3:
        print(l)
        res.append(tuple(l))
        return
    for i in range(ind,len(a)):
        if d[i]:
            l.append(a[i])
            d[i]=0
            solve(a,ind,l,res,d)
            l.pop()
            d[i]=1

n=3
a=[1,2,3]
l,res=[],[]
d={0:1,1:1,2:1}
solve(a,0,l,res,d)
print(res)

#optimized solution--not extra space complexity time complexity is n!*n

def solve(a,ind,res):
    if ind==len(a):
        res.append(tuple(a))
    for i in range(ind,len(a)):
        a[ind],a[i]=a[i],a[ind]
        solve(a,ind+1,res)
        a[i],a[ind]=a[ind],a[i]

n=3
a=[1,2,3]
res=[]
solve(a,0,res)
print(res)