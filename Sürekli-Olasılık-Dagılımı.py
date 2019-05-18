from scipy.integrate import quad


print (" ornek 1 :  f(x) = 2x/15  -->  1 < x < 4\n")
print (" ornek 2 :  f(x) = x/12   -->  1 < x < 5\n")

ornek = int(input("Please select one of them : "))

if ornek == 1 :
    def f1(x):
        return 2*x*x/15
    def f2(x):
        return 2*x*x*x/15
    
    answer1 , err = quad (f1,1,4)
    answer2 , err = quad (f2,1,4)
    
    answer = answer2 - (answer1*answer1)
    print ("\n\nYOU CHOOSE :   ornek 1 :  f(x) = 2x/15  -->  1 < x < 4\n")

    print( "Var[X] = E[X**2]-(E[X])**2\nAnswer is : ", answer)

    
if ornek == 2 :
    def f1(x):
        return x*x/12
    def f2(x):
        return x*x*x/12
    
    answer1 , err = quad (f1,1,5)
    answer2 , err = quad (f2,1,5)
    
    answer = answer2 - (answer1*answer1)
    
    print ("\n\nYOU CHOOSE :   ornek 2 :  f(x) = x/12   -->  1 < x < 5\n")
    print( "Var[X] = E[X**2]-(E[X])**2\n\nAnswer is : ", answer)
    
    
print ("\n\n--------------------END-------------------")
