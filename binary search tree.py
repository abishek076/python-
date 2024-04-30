"""class Node:
    def __init__(self, data):
        self.data=data
        self.left=None
        self.right=None


class BST:
    def __init__(self):
        self.root=None

    def create(self,data):
        new=Node(data)
        if self.root is None:
            self.root=new
        else:
            temp=self.root
            while temp:
                if data<temp.data:
                    if temp.left is None:
                        temp.left = new
                        break
                    temp=temp.left
                elif data>temp.data:
                    if temp.right is None:
                        temp.right = new
                        break
                    temp=temp.right

    def display(self):
        self.inorder(self.root)

    def inorder(self, root):
        if root:
            self.inorder(root.left)
            print(root.data, end=" ")
            self.inorder(root.right)


bst=BST()
lst=[10,11,9,8,91,20,7]
for i in lst:
    bst.create(i)
bst.display()"""
class Node:
    def __init__(self, data):
        self.data=data
        self.left=None
        self.right=None

    def create(self,root,data):
        if root is None:
            return Node(data)
        elif root.data>data:
            root.left= self.create(root.left,data)
        elif root.data<data:
            root.right= self.create(root.right,data)
        return root

    def sea(self,n,temp):
        if temp.data==n:
            print("\nfound")
        elif temp.data>n:
            self.sea(n,temp.left)
        elif temp.data<n:
            self.sea(n,temp.right)

    def inorder(self, root):
        if root:
            self.inorder(root.left)
            print(root.data, end=" ")
            self.inorder(root.right)

    def preorder(self, root):
        if root:
            print(root.data, end=" ")
            self.preorder(root.left)
            self.preorder(root.right)

    def postorder(self, root):
        if root:
            self.postorder(root.left)
            self.postorder(root.right)
            print(root.data, end=" ")


bst=Node(10)
lst=[11,9,8,91,20,7]
for i in lst:
    bst.create(bst, i)
print("inorder")
bst.inorder(bst)
print("\npreorder")
bst.preorder(bst)
print("\npostorder")
bst.postorder(bst)
n=7
bst.sea(n,bst)
