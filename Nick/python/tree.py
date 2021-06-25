class node:
    def __init__(self,value):
        self.value=value
        self.left=None
        self.right=None
        self.parent=None
class tree:
    def __init__(self):
        self.root=None
    def insert(self,value):
        if self.root==None:
            self.root=node(value)
        else:
            self._insert(value,self.root)
    def _insert(self,value,curnode):
        if value<curnode.value:
            if curnode.left==None:
                curnode.left=node(value)
                curnode.left.parent=curnode
            else:
                self._insert(value,curnode.left)
        else:
            if curnode.right==None:
                curnode.right=node(value)
                curnode.right.parent=curnode
            else:
                self._insert(value,curnode.right)
    def print_tree(self):
        if self.root!=None:
            self._print(self.root)
        else:
            print("tree is empty")
    def _print(self,curnode):
        if curnode!=None:
            self._print(curnode.left)
            print(curnode.value)
            self._print(curnode.right)
    def search(self,value):
        if self.root!=None:
            return self._search(value,self.root)
        else:
            return False
    def _search(self,value,curnode):
        if curnode.value==value:
            return True
        elif value<curnode.value and curnode.left!=None:
            return self._search(value,curnode.left)
        elif value>curnode.value and curnode.right!=None:
            return self._search(value,curnode.right)
        return False
    def height(self):
        if self.root==None:
            return 0
        else:
            return self._height(self.root,0)                #return self._height(self.root)
    def _height(self,curnode,curheight):                    #def _height(self,curnode):
        if curnode==None:
            return curheight-1                              # return -1
        leftheight=self._height(curnode.left,curheight+1)   #leftheight=self._height(curnode.left)
        rightheight=self._height(curnode.right,curheight+1) #rightheight=self._height(curnode.right)
        return max(leftheight,rightheight)                  #return 1+max(leftheight,rightheight)
    def findmin(self):
        if self.root!=None:
            return self._findmin(self.root,self.root)
        else:
            return None
    def _findmin(self,curnode,minnode):
        if curnode==None:
            return minnode
        x=self._findmin(curnode.left,curnode.value)
        return x
    def findmax(self):
        if self.root==None:
            return None
        else:
            return self._findmax(self.root,self.root)
    def _findmax(self,curnode,maxnode):
        if curnode==None:
            return maxnode
        y=self._findmax(curnode.right,curnode.value)
        return y
    def print_tree_inorderiteratively(self):
        s=[]
        cur=self.root
        while True:
            if cur!=None:
                s.append(cur)
                cur=cur.left
            elif(s):
                x=s.pop()
                print(x.value)
                if x.right!=None:
                    cur=x.right
            else:
                break
    def print_tree_preorder(self):
        s=[]
        if self.root!=None:
            s.append(self.root)
        while s:
            x=s.pop()
            print(x.value)
            if x.right!=None:
                s.append(x.right)
            if x.left!=None:
                s.append(x.left)
    def print_tree_postorder2(self):
        s1=[]
        s2=[]
        s1.append(self.root)
        while s1:
            x=s1.pop()
            s2.append(x.value)
            if x.left!=None:
                s1.append(x.left)
            if x.right!=None:
                s1.append(x.right)
        print(s2[::-1])
    def print_tree_postorder1(self):
        s=[]
        temp=self.root
        while True:
            while temp:
                if temp.right!=None:
                    s.append(temp.right)
                s.append(temp)
                temp=temp.left
            x=s.pop()
            if x.right!=None and x.right==peek(s):
                s.pop()
                s.append(x)
                temp=x.right
            else:
                print(x.value)
                temp=None
            if len(s)<=0:
                break
    def remove(self,value):
        return self.delete_node(self.find_value(value))
    def find_value(self,value):
        if self.root!=None:
            return self._find_value(value,self.root)
        else:
            return None
    def _find_value(self,value,curnode):
        if curnode.value==value:
            return curnode
        elif curnode.left!=None and value<curnode.value:
            return self._find_value(value,curnode.left)
        elif curnode.right!=None and value>cournode.value:
            return self._find_value(value,curnode.right)
    def delete_node(self,node):
        node_parent=node.parent
        def node_children(n):
            c=0
            if n.left!=None:
                c+=1
            if n.right!=None:
                c+=1
            return c
        def find_successor(n):
            temp=n
            while temp.left!=None:
                temp=temp.left
            return temp
        if node_children(node)==0:
            if node_parent.left==node:
                node_parent.left=None
            else:
                node_parent.right=None
        if node_children(node)==1:
            if node.left!=None:
                child=node.left
            else:
                child=node.right
            if node_parent.left==node:
                node_parent.left=child
            else:
                node_parent.right=child
            child.parent=node_parent
        if node_children(node)==2:
            successor=find_successor(node)
            node.value=successor.value
            self.delete_node(successor)
    def count(self):
        if self.root!=None:
            return self._count(self.root)
        else:
            return 0
    def _count(self,curnode):
        if curnode==None:
            return 0
        leftcount=self._count(curnode.left)
        rightcount=self._count(curnode.right)
        return 1+leftcount+rightcount
    def countleaf(self):
        if self.root!=None:
            return self._countleaf(self.root)
        else:
            return 0
    def _countleaf(self,curnode):
        if curnode==None:
            return 0
        leftcount=self._countleaf(curnode.left)
        rightcount=self._countleaf(curnode.right)
        if leftcount==0 and rightcount==0:
            return 1
        else:
            return leftcount+rightcount

def peek(s):
    if len(s)>0:
        return s[-1]
    else:
        return None
t=tree()
t.insert(8)
t.insert(6)
t.insert(10)
t.insert(4)
t.insert(7)
t.insert(2)
t.insert(5)
t.insert(9)
t.insert(11)
print("min value:",t.findmin())
print("max value:",t.findmax())
print(t.search(4))
print(t.search(5))
print("height:",t.height())
t.print_tree_postorder2()
t.remove(2)
t.remove(8)
print("after deletion:")
t.print_tree_postorder2()
print("nodes:",t.count())
print("leaf nodes:",t.countleaf())
