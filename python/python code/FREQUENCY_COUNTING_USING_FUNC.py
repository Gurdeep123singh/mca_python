def main():
    no = int(input("how many no you want to take in the list : "))
    l1=[]
    for i in range(0,no):
      print("enter element",i+1," : ")
      c=int(input())
      l1.append(c)
    print("the entered elements in the list :",l1)
    freq(l1)
def freq(l1):
    a= len(l1)
    d={}
    for i in range(a):
        count=0
        for j in range(a):
         if l1[i]==l1[j] and i!=j :
             count += 1
        d.append(count)     
     print(d)
main()