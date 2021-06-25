def solve(a,ind,s,l,res):
    if ind==len(a):
        if s==0:
            l=tuple(l)
            res.append(l)
            print(res)
        return
    if a[ind]<=s:
        l.append(a[ind])
        solve(a,ind,s-a[ind],l,res)
        l.pop()
    solve(a,ind+1,s,l,res)
    
a=[2,3,5,7]
l,res=[],[]
solve(a,0,7,l,res)
print(res)