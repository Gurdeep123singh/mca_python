myDict={}
synoymn={}
meaning=[]

while True:
    print("1.) enter word and meaning :")
    print("2.) check word and meaning :")
    print("3.) enter synonymn")
    print("4.) check synoymn")
    print("5.) quit :")


    choice=int(input())
    if(choice==1):
        word=input("enter word")
        
        if word in myDict.keys():
            print("already in dictionary")
        else:
            meaning=input("enter meaning")
            myDict[word]=meaning
    elif(choice==2):
        print("enter word for which you want to check meaning")
        word=input("enter word")
        if word not in myDict.keys():
            print("word is not in the dictionary ")
        else:
            print(f"the meaning of the {word} is :{myDict[word]}")
    elif(choice==3):
        print("enter word for which you want to give synomyn")
        word=input("enter word")
        n=int(input("no of meaning you have for a word"))
        for i in range(n):
         m=input(f"enter meaning {i+1}:")
         meaning.append(m)
        
        if word in synoymn.keys():
            print("already in dictionary")
        else:
            synoymn[word]=meaning  
    elif(choice==4):
         print("enter word for which you want to check synoymn")
         word=input("enter word")
         if word not in synoymn.keys():
             print("word is not in the dictionary ")
         else:
             print(f"the meaning of the {word} is :{synoymn[word]}")   
    elif(choice==5):
        quit()                       
