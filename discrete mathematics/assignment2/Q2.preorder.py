'''
program to implement prorder of tree
'''
def preorder(root,tree,list1):            # fn forpreorder
    traverse=tree[root]                   # root childs
    
    for i in traverse:                      # traversing
        list1.append(i)
        if tree[i]!=[]:
            
            preorder(i,tree,list1)   # root=i
        
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

print(" PREORDER IS ->",preorder(root,tree,list1=[root]))