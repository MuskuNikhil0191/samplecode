def solve(n,s,ca,cb):
    if n<0:
        return
    if ca==0 and cb==0:
        print(s)
        return
    if ca>0:
        solve(n-1,s+"(",ca-1,cb)
    if cb>0 and ca!=cb:
        solve(n-1,s+")",ca,cb-1)
n=6
s="("
solve(n-1,s,(n//2)-1,n//2)