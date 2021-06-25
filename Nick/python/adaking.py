for t in range(int(input())):
    a=[['1']*8 for w in range(8)]
    k=int(input())
    i,j=0,1
    c=1
    a[0][0]='o'
    while c<k:
        if j==8:
            j=0
            i+=1
        a[i][j]='.'
        c+=1
        j+=1
    if i==0:
        a[i][j]='x'
    else:
        for ind in range(j,8):
            a[i][ind]='x'
    i+=1
    for ind in range(0,j+1):
        a[i][ind]='x'
    for i in range(0,8):
        for j in range(0,8):
            if a[i][j]=='1':
                print('.',end=' ')
            else:
                print(a[i][j],end=' ')
        print()