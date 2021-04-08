'''
program for checking if graph is planar or not but it doesnt works for k(3,3)
'''
def main():
    vertices=int(input("no. of vertices are there in your graph "))
    edges=(vertices*(vertices-1))/2
    c=(3*vertices)-6
    status=(edges<=c)
    if status==False:
        print('the given graph is not planar')
    else:
        print('the given graph is planar')    
main()        
