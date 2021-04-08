'''
program to implement postorder of tree
'''
def postorder(root,tree,list1):
    
    traverse=tree[root]                             # root child in traverse
    for i in traverse:                              # traversing
        if tree[i]!=[]:                           # if has child
            
            postorder(i,tree,list1)                # recursive call
        else:
            list1.append(i)                         # if as no child then appending in list and deleting it
            del tree[i]
    if root in tree:                     
        tree[root]=[]               # making tree[root]=[] mhing root as childless
            
        list1.append(root)                # appending root
        del tree[root]                          # deleting root from tree
        
    elif root not in tree:                    # if not in tree

        list1.append(list_of_nodes[0])                 # then root node is appended in list
            
    return list1
              
    
            
    
nodes=int(input("no. of nodes are there in a tree"))

tree=dict()
print('please give node names by pressing enter every time')
list_of_nodes=[input(f'please tell node name {i} : ') for i in range(1,nodes+1)]
print("please tell connected node ")
for i in range(nodes):
    tree[list_of_nodes[i]]=input(f'please tell connection for node {list_of_nodes[i]}  in one line with space : ').split()
print(tree)

root=list_of_nodes[0]
print(" POSTORDER IS ->",postorder(root,tree,list1=[]))
