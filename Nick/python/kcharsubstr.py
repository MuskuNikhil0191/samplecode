#python 3.6.9
a="helloworld"
k=3
d={}
n=len(a)
c=0
for i in a:
    d[i]=0
i,j=0,0
while i<n and j<n:
    if c<k:
        if d[a[j]]==0:
            c+=1
        d[a[j]]+=1
        j+=1
    else:
        print('y',c,a[i:j])
        d[a[i]]-=1
        if d[a[i]]==0:
            c-=1
        i+=1