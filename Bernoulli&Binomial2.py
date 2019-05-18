print("\n\n")
print (" ---------  -------  ODEV  , EHSAN SYD KAZEMI AR   -------  ---------  \n")

prbly_stdnt = float(input("Please enter probability that student can pass OLASILIK course : "))
while prbly_stdnt <0 or prbly_stdnt >1 :
    print("\nERORR..")
    prbly_stdnt = int(input("Please enter correct probability that student can pass OLASILIK course : "))
    

count_stdnt = int(input("Please enter the count of student that take OLASILIK course : "))

print("\n\n ***** We want to count the probability that X students will be passing this lesson ***** \n")

x_stdnt = int(input("Please Enter the count of student can pass OLASILIK course : "))
while count_stdnt < x_stdnt :
    print ("ERORR.. Number of student that get this course is less of student that will be passing the course")
    count_stdnt = int(input("Please enter the count of student that take OLASILIK course : "))
    x_stdnt = int(input("Please Enter the count of student can pass OLASILIK course"))
    

n = count_stdnt
fact_count_stdnt = 1
while n>1:
    fact_count_stdnt = n * fact_count_stdnt
    n -= 1

n = x_stdnt
fact_x_stdnt = 1
while n>1:
    fact_x_stdnt = n * fact_x_stdnt
    n -= 1

n = count_stdnt - x_stdnt
fact_count_x_stdnt = 1
while n>1:
    fact_count_x_stdnt = n * fact_count_x_stdnt
    n -= 1

Cmbtn = fact_count_stdnt/(fact_x_stdnt*fact_count_x_stdnt)
prblty = Cmbtn*(prbly_stdnt**x_stdnt)*((1-prbly_stdnt)**(count_stdnt-x_stdnt))
   
print("The Probability that",x_stdnt, "Students will be Passing this Lesson :", prblty)

print("\n\n\t\t         ----- The End ------  ")
