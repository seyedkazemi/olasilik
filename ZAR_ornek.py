from math import factorial


print("\n      --- --- ---ZAR Atma Örnegi --- --- ---")
print("               EHSAN SEYEDKAZEMI AR  \n\n")

print("normal zarın 6 boyutu var")
print(" x Zarin boyuto(Dimension) ")
x= int(input("Please Enter X : "))
print("\n6 in a normal zar means success \nIn fact, only one event leads to success")
print("\nY is number of successes")
y=int(input("Please Enter Y : "))
if x<y :
    print("ERORR..  x<y : it's not possible")
    

    
print("P(X=x) = (",y,"/",x,") ^x * (",x-y,"/",x,") ^x-1")

print("\nHope-mathematics is also equal : ",y/x)
      
print("variance : ",(y/x)*((x-y)/x) )





print("\n\n        ------------ END ---------- ")


