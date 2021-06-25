for t in range(int(input())):
    n,m=map(int,input().split())
    a=list(map(int,input().split()))
    a.sort()
    low=a[0]
    high=sum(a[m-1:])
    res=[]
    while(low<=high):
        mid=(low+high)//2
        mi=0
        i,ind=0,0
        temp=[]
        while mi<m:
            s,e=0,0
            while i<n-(m-mi-1):
                if s<mid:
                    s+=a[i]
                    if i==n-1:
                        e=1
                    else:
                        i+=1
                elif s==mid:
                    temp.append(mid)
                    mi+=1
                    break
                elif s>mid:
                    i=ind+1
                    ind+=1
                    if e==1:
                        mi+=1
            if s<=mid:
                temp.append(s)
                mi+=1
            else:
                low=mid+1
        if max(temp)==mid:
            res.append(mid)
                
                    
                


