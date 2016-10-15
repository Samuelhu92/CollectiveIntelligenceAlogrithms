class Stack:
    def __init__(self):
        self.items=[]
    def is_empty(self):
        return self.items==[]
    def push(self,item):
        self.items.append(item)
    def pop(self):
        return self.items.pop()
    def peek(self):
        return self.items[len(self.items)-1]
    def size(self):
        return len(self.items)

class Queue:
    def __init__(self):
        self.items=[]
    def is_empty(self):
        return self.items==[]
    def enqueue(self,item):
        self.items.insert(0,item)
    def dequeue(self):
        return self.items.pop()
    def size(self):
        return len(self.items)
class Deque:
    def __init__(self):
        self.items=[]
    def is_empty(self):
        return self.items==[]
    def add_front(self):
        return self.items.append()
    def add_rear(self):
        return self.items.insert(0,item)
    def remove_front(self):
        return self.items.pop()
    def remove_rear(self):
        return self.items.pop(0)
    def size(self):
        return len(self.items)

class BinaryTree:
    def __init__(self,root):
        self.key=root
        self.left_child=None
        self.right_child=None
    def insert_left(self,new_node):
        if self.left_child==None:
            self.left_child=BinaryTree(new_node)
        else:
            t=BinaryTree(new_node)
            t.left_child=self.left_child
            self.left_child=t
    def insert_right(self,new_node):
        if self.right_child==None:
            self.right_child=BinaryTree(new_node)
        else:
            t=BinaryTree(new_node)
            t.right_child=self.right_child
            self.right_child=t
    def get_right_child(self):
        return self.right_child
    def get_left_child(self):
        return self.left_child
    def get_root_val(self):
        return self.key

class BinHeap:
    def __init__(self):
        self.heap_list=[0]
        self.current_size=0
    def perc_up(self,i):
        while i//2>0:
            if self.heap_list[i]<self.heap_list[i//2]:
                temp=self.heap_list[i//2]
                self.heap_list[i//2]=self.heap_list[i]
                self.heap_list[i]=temp
            i=i//2
    def insert(self,k):
        self.heap_list.append(k)
        self.current_size+=1
        self.perc_up(self.current_size)
    def perc_down(self,i):
        while (i*2)<=self.current_size:
            mc=self.min_child(i)
            if self.heap_list[i]>self.heap_list[mcc]:
                temp=self.heap_list[i]
                self.heap_list[i]=self.heap_list[mc]
                self.heap_list[mc]=temp
            i=mc
    def min_child(self,i):
        if i*2+1>self.current_size:
            return i*2
        else:
            if self.heap_list[i*2]<self.heap_list[i*2+1]:
                return i*2
            else:
                return i*2+1
    def del_min(self):
        ret_val=self.heap_list[1]
        self.heap_list[1]=self.heap_list[current_size]
        self.current_size-=1
        self.heap_list.pop()
        self.perc_down(1)
        return ret_val
    def build_heap(self,a_list):
        i=len(a_list)//2
        self.current_size=len(a_list)
        self.heap_list=[0]+a_list[:]
        while i>0:
            self.perc_down(i)
            i-=1

class TreeNode:
    def __init__(self):
        self.key=key
        self.rightChild=right
        self.leftChild=left
        self.parent=parent
        self.payload=val
        self.balanceFactor=balanceFactor
    def isLeaf(self):
        return not (self.rightChild and self.leftChild)
    def isRoot(self):
        return not self.parent
    def hasRightChild(self):
        return self.rightChild
    def hasLeftChild(self):
        return self.leftChild
    def isRightChild(self):
        return self.parent and self.parent.hasRightChild==self
    def isLeftChild(self):
        return self.parent and self.parent.hasLeftChild==self
    def hasAnyChildren(self):
        return self.hasRightChild or self.hasLeftChild
    def hasBothCHildren(self):
        return self.hasRightChild and self.hasLeftChild 
    def replaceNodeData(self,key,value,lc,rc):
        self.key=key
        self.payload=value
        self.leftChild=lc
        self.rightChild=rc
        if self.hasLeftChild():
            self.leftChild.parent=self
        if self.hasRightChild():
            self.rightChild.parent=self
class BinarySearchTree:

    def __init__(self):
        self.root=None
        self.size=0
    def length(self):
        return self.size
    def __len__(self):
        return self.size
    def inorder(self,node):
        if node.leftChild:
            self.inorder(node.leftChild)
        self.print_node(node)
        if node.rightChild:
            self.inorder(node.rightChild)
    def levelorder(self,node):
        nodes=[]
        nodes.append(node)
        while len(nodes)>0:
            current_node=nodes.pop(0)
            self.print_node(current_node)
            if current_node.leftChild:
                nodes.append(current_node.leftChild)
            if current_node.rightChild:
                nodes.append(current_node.rightChild)
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
        if key<currentNode.key:
            if current_node.hasLeftChild():
                self._put(key,val,current_node.leftChild)
            else:
                currentNode.leftChild=TreeNode(key,val,parrent=currentNode)
        else:
            if currentNode.hasRightChild():
                self._put(key,val,currentNode.rightChild)
            else:
                currentNode.rightChild=TreeNode(key,val,parrent=currentNode)
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
        if not currentNode:
            return None
        elif currentNode.key==key:
            return currentNode
        elif key<currentNode.key:
            return self._get(key,currentNode.leftChild)
        else:
            return self._get(key,currentNode.rightChild)
    def __getitem__(self,key):
        return self.get(key)
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
                raise KeyError('Error,key not in tree')
        elif self.size==1 and self.root.key==key:
            self.root=None
            self.size-=1
        else:
            raise KeyError('Error, key not in tree')
    def __delitem__(self,key):
        self.delete(key)
    def spliceOut(self):
        if self.isLeaf():
            if self.isLeftChild():
                self.parent.leftChild=None
            else:
                self.parent.rightChild=None
        elif self.hasAnyChildren():
            if self.hasLeftChild():
                if self.isLeftChild():
                    self.parent.leftChild=self.leftChild
                else:
                    self.parent.rightChild=self.rightChild
                self.leftChild.parent=self.parent
            else:
                if self.isLeftChild():
                    self.parent.leftChild=self.rightChild
                else:
                    self.parent.rightChild=self.rightChild
                self.rightChild.parent=self.parent
    def replaceNodeInParent(self,new_value=None):
        if self.parent:
            if self=self.parent.leftChild:
                self.parent.leftChild=new_value
            else:
                self.parent.rightChild=new_value
        if new_value:
            new_value.parent=self.parent

    def findSuccessor(self):
        succ=None
        if self.hasRightChild():
            succ=self.rightChild.findMin()
        else:
            if self.parent:
                if self.isLeftChild():
                    succ=self.parent
                else:
                    self.parent.rightChild=None
                    succ=self.parent.findSuccessor()
                    self.parent.rightChild=self
        return succ
    def findMin(self):
        current=self
        while current.hasLeftChild():
            current=current.leftChild
        return current
    def remove(self,currentNode):
        if currentNode.isLeaf():
            if currentNode.isLeftChild():
                currentNode.parent.leftChild=None
            else:
                currentNode.parent.rightChild=None
        elif currentNode.hasBothCHildren():
            succ=currentNode.findSuccessor()
            succ.spliceOut()
            currentNode.key=succ.key
            currentNode.payload=succ.payload
        else:
            if currentNode.hasLeftChild():
                if currentNode.isLeftChild():
                    currentNode.leftChild.parent=currentNode.parent
                    currentNode.parent.leftChild=currentNode.leftChild
                elif currentNode.isRightChild():
                    currentNode.leftChild.parent
                    currentNode.parent.rightChild=currentNode.leftChild
                else:
                    currentNode.replaceNodeData(currentNode.leftChild.key,
                                                currentNode.leftChild.payload,
                                                currentNode.leftChild.leftChild,
                                                currentNode.leftChild.rightChild)
            else:
                if currentNode.isLeftChild():
                    currentNode.rightChild.parent=currentNode.parent
                    currentNode.parent.rightChild=currentNode.rightChild
                elif currentNode.isRightChild():
                    currentNode.rightChild.parent=currentNode.parent
                    currentNode.parent.rightChild=currentNode.rightChild
                else:
                    currentNode.replaceNodeData(currentNode.rightChild.key,
                                                currentNode.rightChild.payload,
                                                currentNode.rightChild.leftChild,
                                                currentNode.rightChild.rightChild)
    def binaryTreeDelete(self,key):
        if key<self.key:
            self.leftChild.binaryTreeDelete(key)
        elif key>self.key:
            self.rightChild.binaryTreeDelete(key)
        else:
            if self.hasLeftChild() and self.hasRightChild():
                succ=self.rightChild.findMin()
                self.key=succ.key
                succ.binaryTreeDelete(succ.key)
            elif self.hasRightChild():
                self.replaceNodeInParent(self.rightChild)
            elif self.hasLeftChild():
                self.replaceNodeInParent(self.leftChild)
            else:
                self.replaceNodeInParent(None)

class AVLTree(BinarySearchTree):
    def _put(self,key,val,currentNode):
        if key<currentNode:
            if currentNode.hasLeftChild():
                self._put(key,val,currentNode.leftChild)
            else:
                currentNode.leftChild=TreeNode(key,val,parent=currentNode)
                self.updateBalance(currentNode.leftChild)
        else:
            if currentNode.hasRightChild():
                self._put(key,val,currentNode.rightChild)
            else:
                currentNode.rightChild=TreeNode(key,val,parent=currentNode)
                self.updateBalance(currentNode.rightChild)
    def updataBlance(self,node):
        if node.balanceFactor>1 or node.balanceFactor<-1:
            self.rebalance(node)
            return
        if node.parent!=None:
            if node.isLeftChild():
                node.parent.balanceFactor+=1
            elif node.isRightChild():
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
        newRoot.rightChild=rotRoot
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



    

        