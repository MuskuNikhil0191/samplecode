#python 3.6.9

n=4
k=12
a=[1,2,3,4]
fact=1
for i in range(1,n):
    fact*=i
k-=1
res=""
while True:
    res+=str(a[k//fact])
    a.pop(k//fact)
    if len(a)==0:
        break
    k=k%fact
    fact//=len(a)
print(res)
    
