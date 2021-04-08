'''
PROGRAM TO FIND DFS OF A GIVEN GRAPH 
'''
def dfs(adjacent,stack,output,no,nodes,visited):     # fn for dfs
    
    if len(output)!=no:                              # it works as a base case

        for i in adjacent:                           # adjacent value goes in i one by one

            if i in visited:                          # if i is already in visited then continue
                continue

            if nodes[i]==[] or (i not in visited):     # if node[i] is empty or not in visited
                output.append(i)
                visited.append(i)
                adjacent=nodes[i]
                if adjacent!=[]:                       # if i's adjacent is also have adjacent then recursive call
                    dfs(adjacent,stack,output,no,nodes,visited)
                
                
               

            elif nodes[i]!=[] and (i not in visited):   #if node[i] is not empty or not in visited
                stack.append(i)
                output.append(i)
                adjacent=nodes[i]
                dfs(adjacent,stack,output,no,nodes,visited)    # recursive call
    return output                                               # return output
def main():
    
    no=int(input(" how many nodes are there in the graph : "))         
    print('please tell all node names by using enter')
    vertices=[ input().lower() for _ in range(no)]                   # contain vertices names
    if no>0:
        nodes=dict()                                                # nodes dictionary
       
        no_of_connections=[]
        
        print("NOW YOU HAVE TO TELL NODES CONNECTION :")

        
        for i in range(no):                                           # making graph
            list1=[]

            print(f"please tell node {vertices[i]} connections->> ")
            

            c=int(input("  How many connections are there for it :   "))
            print(" PLEASE TELL NODES ")
            no_of_connections.append(c)
            for j in range(c):
                
                list1.append(input().lower())
            nodes[vertices[i]]=list1    
        print("the given graph is : ",nodes)
        
        start=input("enter starting node")
        stack=[start]
        output=[start]                                    # start in output
        
        adjacent=nodes[start]                              # start adjacent nodes

        print('DFS IS ->>>>>',dfs(adjacent,stack,output,no,nodes,visited=[start]) )  # dfs 

    else:
        print('graph can\'t be possible ')

main()        