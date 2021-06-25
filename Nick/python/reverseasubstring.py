#reverseasubstring
n=int(input())
l=['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
s=input()
a,b=0,0
for i in range(1,n-1):
    x=l.index(s[i])
    if s[i]=='a':
        continue
    for j in range(i+1,n):
        y=l.index(s[j])
        if y<x:
            b=j
            break
    if b!=0:     
        a=i
        break
if a!=0:
    print('Yes')
    print(a,b)
else:
    print('No')