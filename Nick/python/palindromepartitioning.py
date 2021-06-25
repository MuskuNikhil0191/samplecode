def solve(a,ind,s):
    if ind==len(a):
        print(s)
        return
    for i in range(ind,len(a)):
        if a[ind:i+1]==a[ind:i+1][::-1]:
            s.append(a[ind:i+1])
            solve(a,i+1,s)
            s.remove(a[ind:i+1])
    
a="aabb"
s=[]
solve(a,0,s)