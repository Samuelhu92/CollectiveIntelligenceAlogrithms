class TreeNode:
    def __init__(self):
        self.rightChild=right
        self.leftChild=left
        self.parent=parent
        self.balanceFactor=balanceFactor
        self.key=key
        self.payload=val
    def isLeaf(self):
        return not (self.leftChild and self.rightChild)
    def isRoot(self):
        return not self.parent
    def hasRightChild(self):
        return self.rightChild
    def hasLeftChild(self):
        return self.leftChild
    def isLeftChild(self):
        return self.parent and self.parent.hasRightChild==self
    def isRightChild(self):
        return self.parent and self.parent.hasLeftChild==self
    def hasAnyChildren(self):
        return self.hasRightChild or self.hasLeftChild
    def hasBothChildren(self):
        return self.hasRightChild and self.hasLeftChild
    def replaceNodeData(self,key,value,lc,rc):
        self.key=key
        self.payload=value
        self.rightChild=rc
        self.leftChild=lc
        if self.hasRightChild():
            self.rightChild.parent=self
        if self.hasLeftChild():
            self.leftChild.parent=self
class BinarySearchTree:
    def __init__(self):
        self.size=size
        self.root=root
    def length(self):
        return self.size
    def __len__(self):
        return self.size
    def inorder(self,node):
        if node.hasLeftChild:
            self.inorder(node.leftChild)
        self.print_node(node)
        if node.hasRightChild:
            self.inorder(node.rightChild)
    def levelorder(self,node):
        nodes=[]
        nodes.append(node)
        while len(nodes)>0:
            current_node=nodes.pop(0)
            self.print_node(current_node)
            if current.hasRightChild:
                nodes.append(current_node.rightChild)
            if current_node.hasLeftChild:
                nodes.append(current_node.leftChild)
    def print_node(self,node):
        if node.parent:
            print([node.key,node.payload,node.parent.key])
        else:
            print([node.key,node.payload])
    def put(self,key,val):
        if self.root:
            self._put(key,val,self.root)
        else:
            self.root=TreeNode(key,val)
        self.size+=1
    def _put(self,key,val,currentNode):
        if key<current_node:
            if currentNode.hasLeftChild:
                return self._put(key,val,currentNode.leftChild)
            else:
                currentNode.leftChild=TreeNode(key,val,parent=currentNode)
        else:
            if currentNode.hasRightChild:
                return self._put(key,val,currentNode.rightChild)
            else:
                currentNode.rightChild=TreeNode(key,val,parent=currentNode)
    def __setitem__(self,k,v):
        self.put(k,v)
    def get(self,key):
        if self.root:
            res=self._get(key,self.root)
            if res:
                return res.payload
            else:
                return None
        else:
            return None
    def _get(self,key,currentNode):
        if key<currentNode:
            if currentNode.hasLeftChild:
                return self._get(key,currentNode.leftChild)
            else:
                return None
        else:
            if currentNode.hasRightChild:
                return self._get(key,currentNode.rightChild)
            else:
                return None
    def __getitem__(self,k):
        return self.get(k)
    def __contains__(self,key):
        if self._get(key,self.root):
            return True
        else:
            return False
    def delete(self,key):
        if self.size>1:
            nodeToRemove=self._get(key,self.root)
            if nodeToRemove:
                self.remove(nodeToRemove)
                self.size-=1
            else:
                raise KeyError('Error, key not in tree.')
        elif self.size==1 and self.root.key==key:
            self.root=None
            self.size-=1
    def spliceOut(self):
        if self.isLeaf():
            if self.isLeftChild():
                self.parent.leftChild=None
            else:
                self.aprent.rightChild=None
        elif self.hasAnyChild():
                if self.hasRightChild():
                    if self.isLeftChild():
                        self.parent.leftChild=self.rightChild
                    else:
                        self.parent.rightChild=self.leftChild
                    self.rightChild.parent=self.parent
                else:
                    if self.isLeftChild():
                        self.parent.leftChild=self.leftChild
                    else:
                        self.parent.rightChild=self.leftChild
                    self.leftChild.parent=self.parent
    def finMin(self):
        current=self
        while current.hasLeftChild():
            current=current.leftChild
        return current

    def findSuccessor(self):
        if self.hasRightChild():
            succ=finMin(self.rightChild)
        else:
            if self.parent:
                if self.parent.leftChild==self:
                    succ=self.parent
            else:
                self.parent.rightChild=None
                succ=self.parent.findSuccessor()
                self.parent.rightChild=self

            #current=self
            #while current.parent.leftChild!=current:
                #current=current.parent
            #succ=current.parent

    def remove(currentNode):
        if currentNode.isLeaf():
            if currentNode.isLeftChild():
                currentNode.parent.leftChild=None
            else:
                currentNode.parent.rightChild=None
        elif currentNode.hasBothChildren():
            succ=currentNode.findSuccessor()
            succ.spliceOut()
            currentNode.key=succ.key
            currentNode.payload=succ.payload
        else:
            if currentNode.hasRightChild():
                currentNode.rightChild.spliceOut()
            else:
                currentNode.leftChild.spliceOut()

    def replaceNodeInParent(self,new_value=None):
        if self.parent:
            if self.parent.leftChild=self:
                self.parent.leftChild=new_value
            else:
                self.parent.rightChild=new_value
        if new_value:
            new_value.parent=self.parent
    def binarySearchDelete(self,key):
        if key<self.key:
            self.leftChild.binarySearchDelete(key)
        elif key>self.key:
            self.rightChild.binarySearchDelete(key)
        else:
            if self.hasBothChildren():
                succ=self.right.finMin()
                self.key=succ.key
                succ.binarySearchDelete(succ.key)
            elif self.hasLeftChild():
                self.replaceNodeInParent(self.leftChild)
            elif self.hasRightChild():
                self.replaceNodeInParent(self.rightChild)
            else:
                self.replaceNodeInParent(None)
class AVLTree(BinarySearchTree):
    def _put(self,key,val,currentNode):
        if key<currentNode:
            if currentNode.hasLeftChild():
                return self._put(key,val,currentNode.leftChild)
            else:
                currentNode.leftChild=TreeNode(key,val,parent=currentNode)
                self.updateBalance(currentNode.leftChild)
        else:
            if currentNode.hasRightChild():
                return self._put(key,val,currentNode.rightChild)
            else:
                currentNode.rightChild=TreeNode(key,val,parent=currentNode)
                self.updateBalance(currentNode.rightChild)
    def updateBalance(self,node):
        if node.balanceFactor>1 or node.balanceFactor<-1:
            self.rebalance(node)
            return
        if node.parent!=None:
            if node.isLeftChild():
                node.parent.balanceFactor+=1
            else:
                node.parent.balanceFactor-=1
            if node.parent.balanceFactor!=0:
                self.updateBalance(node.parent)
    def rotateLeft(self,rotRoot):
        newRoot=rotRoot.rightChild
        rotRoot.rightChild=newRoot.leftChild
        if newRoot.leftChild!=None:
            newRoot.leftChild.parent=rotRoot
        newRoot.parent=rotRoot.parent
        if rotRoot.isRoot():
            self.root=newRoot
        else:
            if rotRoot.isLeftChild():
                rotRoot.parent.leftChild=newRoot
            else:
                rotRoot.parent.rightChild=newRoot
        newRoot.leftChild=rotRoot
        rotRoot.parent=newRoot
        rotRoot.balanceFactor=rotRoot.balanceFactor+1-min(newRoot.balanceFactor,0)
        newRoot.balanceFactor=newRoot.balanceFactor+1+max(rotRoot.balanceFactor,0)
    def rotateRight(self,rotRoot):
        newRoot=rotRoot.leftChild
        rotRoot.leftChild=newRoot.rightChild
        if newRoot.rightChild!=None:
            newRoot.rightChild.parent=rotRoot
        newRoot.parent=rotRoot.parent
        if rotRoot.isRoot():
            self.root=newRoot
        else:
            if rotRoot.isLeftChild():
                rotRoot.parent.leftChild=newRoot
            else:
                rotRoot.parent.rightChild=newRoot
        newRoot.leftChild=rotRoot
        rotRoot.parent=newRoot
        rotRoot.balanceFactor=rotRoot.balanceFactor+1-min(newRoot.balanceFactor,0)
        newRoot.balanceFactor=newRoot.balanceFactor+1+max(rotRoot.balanceFactor,0)
    def rebalance(self,node):
        if node.balanceFactor<0:
            if node.rightChild.balanceFactor>0:
                self.rotateRight(node.rightChild)
                self.rotateLeft(node)
            else:
                self.rotateLeft(node)
        elif node.balanceFactor>0:
            if node.leftChild.balanceFactor<0:
                self.rotateLeft(node.leftChild)
                self.rotateRight(node)
            else:
                self.rotateRight(node)
def walk(G,s,S):
    P,Q=dict(),set()
    P[s]=None
    Q.add(s)
    while Q:
        u=Q.pop()
        for v in G[u].difference(P,S):
            Q.add(v)
            P[v]=u
    return P

def conponent(G,S):
    comp=[]
    seen=set()
    for u in G:
        if u in seen:
            continue
        seen.update(u)
        C=walk(G,u,S)
        comp.append(C)
    return comp

def res_dfs(G,s,S):
    if S is None: S=set()
    S.add(s)
    for u in G[s]:
        if u in S: continue
        res_dfs(G,u,S)
    return S

def traversal(G,s,qtype=set):
    S,Q=set(),qtype()
    Q.add(s)
    while Q:
        u=Q.pop()
        if u in S: continue
        S.add(u)
        for v in G[u]:
            Q.add(v)
        yield u
def res_dfs_time(G,s,d,f,S=None,t=0):
    if S is None: S=set()
    S.add(s)
    d[s]=t;t+=1
    for u in G[s]:
        if u in S:continue
        t=res_dfs_time(G,u,d,f,S,t)
    f[s]=t;t+=1
    return t
def traverse_time(G,s,qtype=set,t=0):
    S,Q=set(),qtype()
    Q.add((s,None))
    while Q:
        p=Q.pop()
        u=p[1]
        s=p[0]
        if u is None:
            f[s]=t;t+=1
            yield t
        d[u]=t;t+=1
        if u in S:continue
        Q.add((u,None))
        S.add(u)
        for v in G[u]:
            Q.add((u,v))

def res_topsort(G):
    S,res=set(),[]
    def rescure(u):
        if u in S: return
        S.add(u)
        for v in G[u]:
            rescure(v)
        res.append(u)
    for u in G:
        rescure(u)
    res.reverse()
    return res
def tr(G):
    res={}
    for u in G: res[u]=set()
    for u in G:
        for v in G[u]:
            res[v].add(u)
    return res
def sccs(G):
    GT=tr(G)
    sccs,seens=[],set()
    for u in GT:
        if u in seens:continue
        C=walk(G,u,seens)
        seens.update(C)
        sccs.append(C)
    return sccs
    

        













