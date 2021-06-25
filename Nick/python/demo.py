from itertools import permutations
l=['0','1','2','3','4','5','6','7','8','9']
x=list(permutations(l,5))
l=' '.join(''.join(i) for i in x)
l=l.split()
c=0
for i in l:
    i=int(i)
    for j in l:
        j=int(j)
        if i>j:
            if int(i)/int(j)==1:
                print(i,j)
                c+=1
if c==0:
    print('There are no pairs')