class nodes:
    def __init__(self,data=None):
        self.data=data
        self.left_node=None
        self.right_node=None

class binary_tree:
    def __init__(self):
        self.root=root
    def inorder(self):
        if self.root==None:
            print(" TREE IS EMPTY ")
        else:
             self._inorder(self.root)
    def _inorder(self,current_node):
        
        if current_node:
            self._inorder(current_node.left_node)
            print(current_node.data,end='')
            self._inorder(current_node.right_node)
    def preorder(self):
        if self.root==None:
            print(" TREE IS EMPTY ")
        else:
             self._preorder(self.root)
    def _preorder(self,current_node):
        
        if current_node:
            print(current_node.data,end='')
            self._preorder(current_node.left_node)
            
            self._preorder(current_node.right_node)                               
    def postorder(self):
        if self.root==None:
            print(" TREE IS EMPTY ")
        else:
             self._postorder(self.root)
    def _postorder(self,current_node):
        
        if current_node:
            
            self._postorder(current_node.left_node)
            
            self._postorder(current_node.right_node)
            print(current_node.data,end='')

def main():
    obj=binary_tree()
    no_of_nodes=int(input(" HOW MANY NODES ARE THERE IN THE TREE "))
    print("tell the no's ")
    nodes_list=[node(int(input())) for _ in range(1,len(no_of_nodes)+1)]
    obj.root=node_list[0]
    nodes_list[0].left_node=int(input(f" left node of {nodes_list[0]}"))
    nodes_list[0].right_node=int(input)