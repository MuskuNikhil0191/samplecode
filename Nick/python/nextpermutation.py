#code
def find(x,a,ind):
    for i in range(len(a)-1,ind,-1):
        if a[i]>x:
            return i
        

a=list(map(int,input().split()))
flag=0
for i in range(len(a)-2,-1,-1):
    if a[i]<a[i+1]:
        flag=1
        mini=find(a[i],a,i)
        temp=a[i]
        a[i]=a[mini]
        a[mini]=temp
        a=a[:i+1]+a[i+1:][::-1]
        break
if flag==0:
    a=a[::-1]
    print(a)
else:
    print(a)
