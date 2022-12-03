from Employee_Class import Employee, StudentEmployee, ClassifiedStaff, Faculty

file = open(input("Enter file name: "), "w")

numStu = input("Enter the number of students: ")
numCS = input("Enter the number of Classified Staff: ")
numFac = input("Enter the number of Faculty: ")
numTot = numStu + numCS + numFac

myemp = Faculty("Jim", 10, True, 10 ,2, "Sci")
print(myemp)
