print ( " -------------ODEV------------- ")
print ( "       EHSAN SEYEDKAZEMI AR     ")
print ( " ------------------------------ ")

print ( "\n\n" )
x = int(input (" Bir Para X kez atılıyor\n Please Enter X (Between 1 and 3) :  "))
if x >= 4 or x<=0 :
    print(" ERROR!!!  ")
    
print("\n")
if(x == 1):
    print("S = {T, Y}\n")
    p0 = 1/2
    print("P(X=0) = ", p0)
    p1 = 1/2
    print("P(X=1) = ", p1)

    
if(x == 2):
    print("S = {TT, TY, YT, YY}\n")
    p0 = 1/2 * 1/2
    print("P(X=0) = ", p0)
    p1 = 2* 1/2 * 1/2
    print("P(X=1) = ", p1)
    p2 = 1/2 * 1/2
    print("P(X=2) = ", p2)

    
if(x == 3):
    print("S = {TTT, TTY, TYT, YTT, TYY, YTY, YYT, YYY}\n")
    p0 = 1/2 * 1/2 * 1/2
    print("P(X=0) = ", p0)
    p1 = 3* 1/2 * 1/2 * 1/2
    print("P(X=1) = ", p1)
    p2 = 3 * 1/2 * 1/2 * 1/2
    print("P(X=2) = ", p2)
    p3 = 1/2 * 1/2 * 1/2
    print("P(X=3) = ", p3)
    
    
print("\n\n")
print (" ............PMF............")
