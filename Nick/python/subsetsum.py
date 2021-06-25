def solve(a,ind,s,l):
    if ind==len(a):
        print(s)
        l.append(s)
        return
    solve(a,ind+1,s+a[ind],l)
    solve(a,ind+1,s,l)
    
a=[2,3,4]
l,res=[],[]
s=0
solve(a,0,s,l)
print(l)