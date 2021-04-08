'''
PROGRAM TO FIND BFS OF A GIVEN GRAPH
'''
def main():
    
    no=int(input(" how many nodes are there in the graph : "))        
    print('please tell all node names by using enter')
    vertices=[ input().lower() for _ in range(no)]                    # contains vertices names
    if no>0:
        nodes=dict()                                                  # nodes info 
       
        
        
        print("NOW YOU HAVE TO TELL NODES CONNECTION :")

        
        for i in range(no):
            list1=[]

            print(f"please tell node {vertices[i]} connections->> ")
            

            c=int(input("  How many connections are there for it :   "))
            print(" PLEASE TELL NODES ")
            
            for j in range(c):
                
                list1.append(input().lower())
            nodes[vertices[i]]=list1                             # contains vertices connections
        print("the given graph is : ",nodes)
        
        start=input("start node").lower()                      # taking start vertice
        queue=[start]
        output=[start]
        
        while len(queue)!=0:                                     
            currentVertex=queue.pop(0)                # currentVertex has first element of queue
            
            adjacent=nodes[currentVertex]               # adjacent of current vertex
            

            for i in adjacent:                         # adjacent in i
                if i not in output:
                    
                    queue.append(i)                        # appending in queue
                    output.append(i)                       # appending in output
                
            

        print('BFS IS ->>>>>',output)    

    else:
        print('graph can\'t be possible ')

    
    

main()        