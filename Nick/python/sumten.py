def two(x,a):
    if ((x//10)+(x%10)<=10) and len(a)>1:
        return 1
    return 0
def threeb(x,a):
    if len(a)==3:
        u=x%10
        t=(x//10)%10
        h=x//100
        p=(10-h)-t
        if p>=0:
            if p==0:
                if u==0:
                    return 1
                return 0
            if t+u<=(10-h):
                return p+1
            return p
        return 0
    return 0
def threea(y):
    u=y%10
    t=(y//10)%10
    h=y//100
    p=(10-h)-t
    if p>=0:
        if t+u>=10-h:
            return t+1
        return t
    return 11-h
for t in range(int(input())):
    x,y=map(int,input().split())
    a=str(x)
    b=str(y)
    c=0
    for i in range(len(a),len(b)):
        if i==2:
            c+=9-(x//10)
            c+=two(x,a)
        if i==3:
            k=10-(x//100)
            for j in range(9-(x//100)):
                c+=k
                k-=1
            c+=threeb(x,a)
    if len(b)==2:
        c+=(y//10)-(x//10)-1
        c+=two(x,a)
        if (y//10)+(y%10)>=10:
            c+=1
    if len(b)==3:
        if len(a)==3:
            k=10-(x//100)
            for j in range((y//100)-(x//100)-1):
                c+=k
                k-=1
            c+=threeb(x,a)
            c+=threea(y)
        else:
            k=10
            for j in range((y//100)-1):
                c+=k
                k-=1
            c+=threea(y)
    print(c)
        
        

