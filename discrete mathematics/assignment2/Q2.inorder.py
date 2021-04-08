'''
program to implement inorder for tree
'''
def inorder(root,tree,list1,visited):               # fn for inorder
    traverse=tree[root]                  # root child in traverse
    
    
    for i in traverse:                          # traversing
        
        if tree[i]!=[]:                  # if has child
            
            inorder(i,tree,list1,visited)        # recursive call
                   
        else:
            list1.append(i)                      # if has no child then only appends in list
            
        if tree[root].index(i)+1==1:              # if  root index is 1 then appending 
            list1.append(root)
                 
    return list1           # returning list



nodes=int(input("no. of nodes are there in a tree"))

tree=dict()
print('please give node names by pressing enter every time')
list_of_nodes=[input(f'please tell node name {i} : ') for i in range(1,nodes+1)]
print("please tell connected node ")
for i in range(nodes):
    tree[list_of_nodes[i]]=input(f'please tell connection for node {list_of_nodes[i]}  in one line with space : ').split()
print(tree)
 
root=list_of_nodes[0]                  # root 

print(" INORDER IS ->",inorder(root,tree,list1=[],visited=[]))