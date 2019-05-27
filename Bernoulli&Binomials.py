from math import factorial


print("\n      --- --- --- Para Örnegi --- --- ---")
print("             EHSAN SEYEDKAZEMI AR  \n\n")

print("X Para atılmış")
x= int(input("Please Enter X : "))
print("\nY Para Yazı Gelmiş")
y=int(input("Please Enter Y : "))
if x<y :
    print("ERORR..  x<y : it's not possible")
    

c = factorial(x)/(factorial(x-y)*factorial(y))
R = c*(0.5**y)*(0.5**(x-y))
print("\n\n")
print(x," Para atılmış ve ",y," Para Yazı Gelmiş Olasiliki : ",R)

print("\n\n        ------------ END ---------- ")
