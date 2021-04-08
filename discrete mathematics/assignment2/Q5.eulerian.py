'''
PROGRAM TO IDENTIFY IF GIVEN GRAPH IS EUCLEDIAN CIRCUIT OR NOT
BY USING DFS TRAVERSAL HAVING STACK , OUTPUT AND VISITED 
'''
def dfs(adjacent,stack,output,no,nodes,visited):    # FN OF DFS
    
    if len(output)!=no:                            # IF OUTPUT NOT EQUALS TO NO OF NODES

        for i in adjacent:                         # ADJACENT IN I

            if i in visited:                                  # IF ALREADY VISITED THEN CONTINUES
                continue

            if nodes[i]==[] or (i not in visited):              # IF NODE IS  EQUAL TO [] 
                output.append(i)
                visited.append(i)
                adjacent=nodes[i]
                
                if adjacent!=[]:

                    dfs(adjacent,stack,output,no,nodes,visited)      # CALLING RECURSIVELY
                
                
               

            elif nodes[i]!=[] and (i not in visited):        # IF NODE IS NOT EQUAL TO []
                stack.append(i)
                output.append(i)
                adjacent=nodes[i]
                dfs(adjacent,stack,output,no,nodes,visited)      # CALLING RECURSIVELY
    return output

def main():
    no=int(input(" how many nodes are there in the graph : "))           # NO OF NODES
    if no>0:
        nodes=dict()
        
        no_of_connections=[]
        zero_degree_nodes=[]                     # CONTAINING ZERO DEGREE NODES
        non_zero_degree_nodes=[]                 # CONTAINING NON ZERO DEGREE NODES

        
        print('\t\tNOTE:-- Please tell nodes names by pressing enter every time:')

        nodes_names=[input().lower() for i in range(no)]          # CONTAINING NODES NAMES

        print("NOW YOU HAVE TO TELL NODES CONNECTION :")
        
        for i in range(no):
            list1=[]

            print(f"please tell node {nodes_names[i]} connections->> ")


            c=int(input("  How many connections are there for it :   "))
            print(" PLEASE TELL NODES ")
            no_of_connections.append(c)
            for j in range(c):
                
                list1.append(input().lower())
            nodes[nodes_names[i]]=list1  
        print("the given graph is : ",nodes)

        for i in range(no):
            if nodes[nodes_names[i]]==[] :    # IF NODES DOESNT HAS CONNECTION MEANS EMPTY i.e ZERO DEGREE
                zero_degree_nodes.append(nodes_names[i])
            else:
                non_zero_degree_nodes.append(nodes_names[i])        
        
        start=non_zero_degree_nodes[0]
        stack=[start]
        output=[start]
        
        adjacent=nodes[start]                    # START =NODES[0] OF NON ZERO DEGREE

        status=dfs(adjacent,stack,output,no,nodes,visited=[start])
        
        flag=True
        if len(status)+len(zero_degree_nodes)==no:      # IF OUTPUT LIST AND LIST OF ZERO DEGREE NODES == NO.OF NODES
            for i in range(no):
                if no_of_connections[i]%2==0:    # IF ALL NODES HAS DEGREE EVEN
                    continue 
                else:
                    flag=False                   # IF ODD DEGREE BREAKS AND FLAG=FALSE
                    break
            if flag==True:
                print(' YES EUCLEDIAN CURCUIT ')    
            else:
                print("!!! NOT A EUCLEDIAN CURCUIT !!!")   
        else: 
            print("!!! NOT A EUCLEDIAN CURCUIT !!!") 
    else:
        print('!!! NOT A GRAPH !!!')                  

    
main()        

        