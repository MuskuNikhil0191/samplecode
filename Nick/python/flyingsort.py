#flyingsort
def less(a,s,j,n):
    c=0
    print(s)
    for i in range(j+1,n):
        if s[i]<a:
            c+=1
    return c
def indices(a,s,j,n):
    l=[]
    for i in range(j+1,n):
        print('c',s[i],a)
        if s[i]<a:
            l.append(i)
            print('x',l)
    return l
for t in range(int(input())):
    n=int(input())
    s=list(map(int,input().split()))
    i,tot=0,0
    while i!=n-1:
        no=less(s[i],s,i,n)
        print(no)
        if no==n-(i+1):
            #print('a')
            c=s.copy()
            s.clear()
            s.append(c[:i])
            s.append(c[i+1:])
            s.append(c[i])
            del c
            tot+=1
            n-=1
        elif no>0:
            if i==0:
                i+=no
                tot+=no
                ind=indices(s[i],s,i,n)
                print(ind)
                while len(ind)!=0:
                    c=s.copy()
                    s.clear()
                    s.append(c[ind[0]])
                    s.append(c[:ind[0]])
                    s.append(c[ind[0]+1:])
                    del c
                    ind.remove(ind[0])
            else:
                c=s.copy()
                s.clear()
                s.append(c[i])
                s.append(c[i+1:])
                s.append(c[i])
                del c
        else:
            i+=1
    print(tot)