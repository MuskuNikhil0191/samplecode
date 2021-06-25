s="helloworld"
t="rol"
a,b={},{}
for i in t:
    try:
        b[i]+=1
    except:
        b[i]=1
c=len(b)
tc=0
n=len(s)
j=-1
for i in range(n):
    try:
        if b[s[i]]:
            try:
                a[s[i]]+=1
            except:
                a[s[i]]=1
            if a[s[i]]==b[s[i]]:
                tc+=1
            if tc==c:
                j=i+1
                break
    except:
        pass
if j==-1:
    print('none')
i=0
ans=j-i
while i<n and j<=n:
    if tc==c:
        ans=min(ans,j-i)
        try:
            if b[s[i]]:
                a[s[i]]-=1
                if a[s[i]]<b[s[i]]:
                    tc-=1
        except:
            pass
        i+=1
    else:
        try:
            if b[s[j]]:
                try:
                    a[s[j]]+=1
                except:
                    a[s[j]]=1
                if a[s[j]]==b[s[j]]:
                    tc+=1
        except:
            pass
        j+=1
print(ans)
                    
        
    