#Program to implement ¬∀x P(x)  ≡ ∃x ¬P(x)
print('Enter P(x) s in 1 0 form ')
n=int(input("how many 1 and 0 you want to enter:"))
x=[bool(int(input())) for i in range(n)]
print(f"the entered binary is :\t\t{x}\n")
#print p(x)
for i in range(len(x)):
    print(f'\t\t\t\tP( {i} ) ={x[i]}')

#checking for ¬(∀xP(x)) ≡ ∃x(¬P(x))
print('\n\t\t\t\tTo Prove ¬∀x P(x) ≡ ∃x ¬P(x)')
print('\n\t\t\t\tLHS : \n\t\t\t\t\t ¬∀x P(x) = ¬(P(0)^P(1)^P(2)...^P(n))')

#evaluate LHS
Left_side=x[0]
for i in range(1,len(x)):
    Left_side = Left_side and x[i]
print('\t\t\t\t\t¬∀x P(x)=', (not Left_side) )

#evaluate RHS
print('\n\t\t\t\tRHS : \n\t\t\t\t\t ∃x ¬P(x) = (¬P(0)) V (¬P(1)) V (¬P(2))...(¬P(n)))')
Right_side=not x[0]
for i in range(1,len(x)):
    Right_side = Right_side or (not x[i])
print('\t\t\t\t\t∃x ¬P(x) =',Right_side)