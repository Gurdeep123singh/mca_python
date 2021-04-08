'''
PROGRAM TO MAKE PERMUTATIONS OF A SET USING RECURSION
'''
def permutation(lst):

    if len(lst) == 0:                  # If lst is empty then there are no permutations
        return []


    if len(lst) == 1:               # If there is only one element in lst then, only

        return [lst]                   # one permuatation is possible

  
    
    # elements are more than 1

    l = []                                     # empty list that will store  permutation

    for i in range(len(lst)):

       m = lst[i]                                 # taking 1st element in m 

       # remaining list other than 1st element

       remLst = lst[:i] + lst[i+1:]

       for p in permutation(remLst):          # remaining elements permutations in p 

           l.append([m] + p)                 # appending permutations with first element in permutation list

    return l                                 # returning permutations

  

  

number=int(input("no of elements you want to enter :"))
setA=[]
for i in range(number):
    setA.append(input())
print("the entered set is :",setA)
 
print("PERMUTATIONS OF A SET ARE : ")
for p in permutation(setA):

    print(p)