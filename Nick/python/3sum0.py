a=[-1,0,1,2,-1,-4]
a=sorted(a)
n=len(a)
s=set()
for i in range(n-2):
    j=i+1
    k=n-1
    while j<k:
        if a[i]+a[j]+a[k]==0:
            s.add((a[i],a[j],a[k]))
            j+=1
            k-=1
        if a[i]+a[j]+a[k]<0:
            j+=1
        else:
            k-=1
print(s)
 

//another method without using set
a=[-1,0,1,2,-1,-4]
a=sorted(a)
print(a)
n=len(a)
l=[]
for i in range(n-2):
    if i==0 or (i>0 and a[i]!=a[i-1]):
        j=i+1
        k=n-1
        while j<k:
            if a[i]+a[j]+a[k]==0:
                l.append((a[i],a[j],a[k]))
                while j<k and a[j]==a[j+1]:
                    j+=1
                while j<k and a[k]==a[k-1]:
                    k-=1
                j+=1
                k-=1
            elif a[i]+a[j]+a[k]<0:
                j+=1
            else:
                k-=1        
print(l)
 