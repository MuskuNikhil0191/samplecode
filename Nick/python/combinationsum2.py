def solve(a,ind,s,l,res,d):
    if ind==len(a):
        if s==0:
            try:
                l=tuple(l)
                if d[l]:
                    pass
            except:
                l=tuple(l)
                d[l]=1
                res.append(l)
        return
    if a[ind]<=s:
        l.append(a[ind])
        solve(a,ind+1,s-a[ind],l,res,d)
        l.pop()
    solve(a,ind+1,s,l,res,d)
    
a=[1,1,1,2,2]
a=sorted(a)
l,res=[],[]
d={}
solve(a,0,4,l,res,d)
print(res)

optimizedmethod:

def solve(a,ind,s,l,res):
    if s==0:
        print(l)
        res.append(tuple(l))
        return
    for i in range(ind,len(a)):
        if a[i]>s:
            break
        if i>ind and a[i]==a[i-1]:
            continue
        if a[i]<=s:
            l.append(a[i])
            solve(a,i+1,s-a[i],l,res)
            l.pop()
    
a=[1,1,1,2,2]
l,res=[],[]
solve(a,0,4,l,res)
print(res)