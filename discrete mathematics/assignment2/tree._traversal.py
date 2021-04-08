def inorder(root,tree,list1,visited):    # fn for inorder
    traverse=tree[root]                   # root child nodes in traverse
    
    
    for i in traverse:                   # traversing
        
        if tree[i]!=[]:                  # if node has  child
            
            inorder(i,tree,list1,visited)    # recursive fn
                   
        else:                                  # only appending if no child is there
            list1.append(i)
            
        if tree[root].index(i)+1==1:                 # for root if root index =1 then appending
            list1.append(root)
                 
    return list1                                # returning

def postorder(root,tree,list1):                     # fn for postorder
    
    traverse=tree[root]                           # root childs in traverse
    for i in traverse:
        if tree[i]!=[]:                          # if child is there
            
            postorder(i,tree,list1)               # then recursive call and root=i
        else:
            list1.append(i)                      # if no child then only appending and deleting that node
            del tree[i]

    if root in tree:                            I # if root is there in tree then makes it childless
        tree[root]=[]
                
        list1.append(root)                          # appending root in list1  and delete that node from tree
        del tree[root]
        
    elif root not in tree:             

        list1.append(list_of_nodes[0])        
            
    return list1                                           # returning list1

def preorder(root,tree,list1):                             # fn for preorder
    traverse=tree[root]                                          # root child in traverse
     
    for i in traverse:           # traversing child
        list1.append(i)
        if tree[i]!=[]:
            
            preorder(i,tree,list1)   # root=i
        
    return list1

nodes=int(input("no. of nodes are there in a tree"))

tree=dict()
list_of_nodes=[input(f'please tell node name {i} : ') for i in range(1,nodes+1)]
print("please tell connected node ")
for i in range(nodes):
    tree[list_of_nodes[i]]=input(f'please tell connection for node{list_of_nodes[i]}  in one line with space : ').split()
print(tree)

root=list_of_nodes[0]            # root

print(" INORDER IS ->",inorder(root,tree,list1=[],visited=[])) 
print(" PREORDER IS ->",preorder(root,tree,list1=[root]))
print(" POSTORDER IS ->",postorder(root,tree,list1=[]))