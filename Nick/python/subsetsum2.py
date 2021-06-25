def solve(a,ind,l,res):
    res.append(tuple(l))
    for i in range(ind,len(a)):
        if i>ind and a[i]==a[i-1]:
            continue
        l.append(a[i])
        solve(a,i+1,l,res)
        l.pop()
    
a=[1,2,2]
a=sorted(a)
l,res=[],[]
s=0
solve(a,0,l,res)
print(res)