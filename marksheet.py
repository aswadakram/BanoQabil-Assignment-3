name=input("Enter Student Name: ")
roll=int(input("Enter Roll Number: "))

#CHEMISTRY
marks1=int(input("Enter Your Chemistry Marks: "))

if (marks1>=80):
    grade= "A Grade"
elif (marks1>=70):
    grade= "B Grade"
elif  (marks1>=60):
     grade= "C Grade"
elif  (marks1>=50):
    grade= "D Grade"
elif  (marks1>=40):
    grade= "E Grade"
else:
	grade= "F Grade"
    
#PHYSICS    
marks2=int(input("Enter Your Physics Marks: "))

if (marks2>=80):
    grade= "A Grade"
elif (marks2>=70):
    grade= "B Grade"
elif  (marks2>=60):
     grade= "C Grade"
elif  (marks2>=50):
    grade= "D Grade"
elif  (marks2>=40):
    grade= "E Grade"
else:
	grade= "F Grade"
	
#ENGLISH
marks3=int(input("Enter Your English Marks: "))

if (marks3>=80):
    grade= "A Grade"
elif (marks3>=70):
    grade= "B Grade"
elif  (marks3>=60):
     grade= "C Grade"
elif  (marks3>=50):
    grade= "D Grade"
elif  (marks3>=40):
    grade= "E Grade"
else:
	grade= "F Grade"
    
#BIOLOGY  
marks4=int(input("Enter Your Biology Marks: "))

print("               ")

if (marks4>=80):
    grade= "A Grade"
elif (marks4>=70):
    grade= "B Grade"
elif  (marks4>=60):
     grade= "C Grade"
elif  (marks4>=50):
    grade= "D Grade"
elif  (marks4>=40):
    grade= "E Grade"
else:
	grade= "F Grade"


print("===========")
print("Marksheet")
print("===========")
print("               ")

print("Student Name:" ,name) 
print("Roll Number:" ,roll) 
print("Grade:" ,grade)

obtained= marks1+marks2+marks3+marks4

print("Total Obtained Marks:", obtained, "out of 400")
print("Percentage:", (obtained/400) *100,"%")