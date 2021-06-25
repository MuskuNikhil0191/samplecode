n=int(input())
l=list(map(int,input().split()))
c=0
a=[]
b=[l[0]]
for i in range(1,n):
    if l[i-1]>l[i]:
        b.append(l[i])
    elif l[i]>l[i-1]:
        a.append(b)
        b=[]
        b.append(l[i])
    else:
        b.append(l[i])
a.append(b)
while(len(a)!=1):
    for i in range(1,len(a)):
        a[i].pop(0)
    j=0
    while(j<len(a)-1):
        if len(a[j])==0:
            a.pop(j)
        elif len(a[j+1])==0:
            a.pop(j+1)
        else:
            if a[j][-1]>=a[j+1][0]:
                a[j].extend(a[j+1])
                a.pop(j+1)
            j+=1
    c+=1
    if len(a[-1])==0:
        a.pop(-1)
print(c)
