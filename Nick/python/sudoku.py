import math

b = [[3, 0, 6, 5, 0, 8, 4, 0, 0],
        [5, 2, 0, 0, 0, 0, 0, 0, 0],
        [0, 8, 7, 0, 0, 0, 0, 3, 1],
        [0, 0, 3, 0, 1, 0, 0, 8, 0],
        [9, 0, 0, 8, 6, 3, 0, 0, 5],
        [0, 5, 0, 0, 9, 0, 6, 0, 0],
        [1, 3, 0, 0, 0, 0, 2, 5, 0],
        [0, 0, 0, 0, 0, 0, 0, 7, 4],
        [0, 0, 5, 2, 0, 6, 3, 0, 0]]

#solving
def solve(b):
    pos=find_empty(b)
    if pos is None:
        return True
    else:
        r,c=pos
    for i in range(1,len(b)+1):
        if valid(b,i,(r,c)):
            b[r][c]=i
            if solve(b):
                return True
            b[r][c]=0
    return False


#check valid num
def valid(b,num,pos):
    if num in b[pos[0]]:
        return False
    for i in range(len(b)):
        if b[i][pos[1]]==num:
            return False
    n=int(math.sqrt(len(b)))
    x=pos[0]//n
    y=pos[1]//n
    for i in range(x*n,(x*n)+n):
        for j in range(y*n,(y*n)+n):
            if b[i][j]==num:
                return False
    return True

#finding empty position
def find_empty(b):
    for i in range(len(b)):
        for j in range(len(b[0])):
            if b[i][j]==0:
                return (i,j)
    return None

#printing board
def print_board(b):
    for i in range(len(b)):
        if i%3==0 and i!=0:
            print('- - - - - - - - - - -')
        for j in range(len(b[0])):
            if j%3==0 and j!=0:
                print('|',end=" ")
            print(b[i][j],end=" ")
        print()
print_board(b)
print('<------------------>')
if solve(b):
    print_board(b)
else:
    print("No sudoku possible")


#another method

def solve(a,n):
    for i in range(n):
        for j in range(n):
            if a[i][j]==0:
                for val in range(1,n+1):
                    if possible(a,val,i,j,n):
                        a[i][j]=val
                        if solve(a,n):
                            return True
                        a[i][j]=0
                return False               
    return True

def possible(a,val,i,j,n):
    sq=int(n**0.5)
    x=sq*(i//sq)
    y=sq*(j//sq)
    for k in range(n):
        if a[k][j]==val:
            return False
        if a[i][k]==val:
            return False
        if a[x+(i//sq)][y+(i%sq)]==val:
            return False
    return True
    
n=9
a=[[3, 0, 6, 5, 0, 8, 4, 0, 0],
        [5, 2, 0, 0, 0, 0, 0, 0, 0],
        [0, 8, 7, 0, 0, 0, 0, 3, 1],
        [0, 0, 3, 0, 1, 0, 0, 8, 0],
        [9, 0, 0, 8, 6, 3, 0, 0, 5],
        [0, 5, 0, 0, 9, 0, 6, 0, 0],
        [1, 3, 0, 0, 0, 0, 2, 5, 0],
        [0, 0, 0, 0, 0, 0, 0, 7, 4],
        [0, 0, 5, 2, 0, 6, 3, 0, 0]]
if solve(a,n):
    print(*a)
else:
    print("sudoku not possible")