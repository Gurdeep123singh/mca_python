'''
PROGRAM TO CHECK IF GIVEN GRAPH IS HAMILTONIAN CIRCUIT OR NOT 
IF IT IS HAMILTONIAN THEN IT GIVES PATH ALSO

'''
def  hamiltonian(path,adjacent,visited,nodes):              # fn for hamiltonian and returning true or false
    if len(path)==len(visited)  :
        if path[0]  in nodes[path[-1]]:             # checks if path list last element is connected to path last element in graph dictionary
            return True                             # then returns true

        else:
            return False    
    for i in adjacent:                              # adjacent values comes in i
        if visited[i]==False:                       # if visited = false then makes it as true

            visited[i]=True                         # and appends

            path.append(i)
            adjacent=nodes[i]                         # adjacent of node i 

            if hamiltonian(path,adjacent,visited,nodes) :   # then calling recursively if it goes on then return true
                return True                                 # oterwise returns false and visited i becomes false
            visited[i]=False
            path.remove(i)                         # then remove i from path
    return False


def main():
    no=int(input(" how many nodes are there in the graph : "))
    if no>0:
        nodes=dict()                                              # graph 
        
        
        print('\t\tNOTE:-- Please tell nodes names by pressing enter every time:')

        vertices_names=[input().lower() for i in range(no)]        # HAVE vertices NAMES
        
        print("NOW YOU HAVE TO TELL NODES CONNECTION :")

        
        for i in range(no):
            list1=[]

            print(f"please tell node {vertices_names[i]} connections->> ")


            c=int(input("  How many connections are there for it :   ")) # connections
            print(" PLEASE TELL NODES ")

            
                                          
            
            for j in range(c):
                
                list1.append(input().lower())
            nodes[vertices_names[i]]=list1 

        print("the given graph is : ",nodes)
        visited=dict()
        for i in range(no):
            visited[vertices_names[i]]=False                        # all nodes are false in visited dict.
            

        start=vertices_names[0]
        path=[start]
        visited[start]=True
        adjacent=nodes[start]
        status=hamiltonian(path,adjacent,visited,nodes)

        if status==True:                                          # if true
            print(' YES it is a hamiltonian circuit ')
            print('\t\tHAMILTONIAN PATH->>>>>>',path)
        else:
            print('!!! NO it is not a hamiltonian circuit !!! ')
    else:
        print("!!!!NOT A GRAPH!!!!")        
main()
