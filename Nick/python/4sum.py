a=[1,0,-1,0,-2,2]
a=sorted(a)
n=len(a)
res=[]
i=0
t=0
while i<n-3:
    j=i+1
    while j<n-2:
        l=j+1
        h=n-1
        while l<h:
            s=a[i]+a[j]+a[l]+a[h]
            if s==t:
                res.append((a[i],a[j],a[l],a[h]))
                while l<h and a[l]==a[l+1]:
                    l+=1
                while l<h and a[h]==a[h-1]:
                    h-=1
                l+=1
                h-=1
            elif s<t:
                l+=1
            else:
                h-=1
        while j<n-2 and a[j]==a[j+1]:
            j+=1
        j+=1
    while i<n-3 and a[i]==a[i+1]:
        i+=1
    i+=1
print(res)