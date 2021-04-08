import random

computer=random.randint(1,3)

if computer==1:
    computer='s'
elif computer==2:
    computer='p'
else:
    computer='sc'

print("what you want to choose  ->>>>")
player=input(" For stone:(s) For paper :(p) For scissor :(sc) ")


def win(computer,player):
    if player==computer:
        return None
    elif player=='s':
        if computer=='p':
         return False
        elif computer=='sc':
         return True
    elif player=='p':
        if computer=='sc':
         return False
        elif computer=='s':
         return True            
    elif player=='sc':
        if computer=='p':
         return True
        elif computer=='s':
         return False 

value=win(computer,player)
if value==None:
    print("thhe game is tie")
elif value==True:
    print("you win")       
else:
    print("you lose") 

dict1={'sc':'scissor','s':'stone','p':'paper'}     

print(f"computer chose {dict1[computer]}")
print(f"you chose {dict1[player]}")