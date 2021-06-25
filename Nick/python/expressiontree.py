def postfix(exp):
    s=[]
    d={
        '*':2,
        '/':2,
        '+':1,
        '-':1,
        '^':3
    }
    res=""
    for i in exp:
        if i=='(':
            s.append('(')
        elif i==')':
            while s[-1]!='(':
                res+=s.pop()
            s.pop()
        elif i.isalpha():
            res+=i
        else:
            if(s):
                while d.get(s[-1],0)>=d.get(i,0):
                    res+=s.pop()
                s.append(i)
            else:
                s.append(i)
    while s:
        x=s.pop()
        if x!='(' or x!=')':
            res+=x
    return res
exp="((a+b)*c)"
postfixexp=postfix(exp)
class node:
    def __init__(self,value):
        self.value=value
        self.left=None
        self.right=None
class binarytree:
    def __init__(self):
        self.root=None
    def printtree(self):
        if self.root!=None:
            self._printtree(self.root)
        else:
            print('tree is empty.')
    def _printtree(self,curnode):
        if curnode!=None:
            self._printtree(curnode.left)
            print(curnode.value)
            self._printtree(curnode.right)
t=binarytree()
s=[]
for i in postfixexp:
    if i.isalpha():
        new=node(i)
        s.append(new)
    else:
        new=node(i)
        new.right=s.pop()
        new.left=s.pop()
        s.append(new)
t.root=new
t.printtree()