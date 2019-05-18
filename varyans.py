

print("This program calculates grades Variance  of the two OLASILIK classes")
num1 = int(input("please Enter Number of first class students  : "))

print("\nEnter student score in first class and Press ENTER after each score")
n=1
ave1 = 0
score1 = {}
while num1+1>n :
    print("\nstudent [",n,"] : ")
    m = int(input())
    ave1 = ave1 + m
    score1[n] = m
    n = n+1
ave1 = ave1/num1 

m=1
sum1 = 0
while num1+1>m :
    sum1 = ((score1[m] - ave1)*(score1[m] - ave1))+ sum1
    m +=1
var1 = sum1/num1


num2 = int(input("please Enter Number of second class students : "))
n=1
ave2 = 0
score2 = {}
while num2+1>n :
    print("\nstudent [",n,"] : ")
    m = int(input())
    ave2 = ave2 + m
    score2[n] = m
    n = n+1
ave2 = ave2/num2
m=1
sum2 = 0
while num2+1>m :
    sum2 = ((score2[m] - ave2)*(score2[m] - ave2))+ sum2
    m +=1
var2 = sum2/num2


print("\n----------------------------------------------------\n")
print("varyans first class is  : " , var1)
print("varyans second class is : " , var2)

