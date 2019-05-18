print ( 'Hi Dear')
print('Welcome To Bayes Teoremi')
print('Purpose: The probability that a radar will find an airplane if there is an airplane.')
print ('At Each Step You Have Not Number, Use The Zero')

 #Print a blank line                          
print()

print ('P(A) : The Probability that there will be an Airplane')
P_A = float(input("Please Enter P(A) : "))
print("P(A) is =", P_A)

 #Print a blank line                          
print()

print ('P(B) : The probability that radar shows point')
P_B = float(input("Please Enter P(B) : "))
print("P(B) is =", P_B)

 #Print a blank line                          
print()

print('P(A∩B) : Probability Of Occurrence Of A and B Events')
P_AB = float(input("Please Enter P(A∩B) : "))
print("P(A∩B) is =", P_AB)

 #Print a blank line                          
print()

print('P(A│B) : The probability that an airplane exists, provided the radar shows a point')
P_A_B = float(input("Please Enter P(A│B) : "))
print("P(A│B) is =", P_A_B)

 #Print a blank line                          
print()

if P_A ==0 :
    print ('ERROR! P(A) Can Not Get zero value')

    
elif P_AB == 0 :
    P_B_A = (P_A_B*P_B)/ P_A
    print('The probability that a radar will find an airplane if there is an airplane : ', P_B_A )

    
else :
    P_B_A = (P_AB)/(P_A)
    print('The probability that a radar will find an airplane if there is an airplane : ', P_B_A )
