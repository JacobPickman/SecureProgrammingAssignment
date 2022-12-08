from Employee_Class import Employee, StudentEmployee, ClassifiedStaff, Faculty
import re

def EmployeeAssignment(file):
    employees = []
    count = 0
    for line in file:
        templine = line.split(",")
        if count < int(numStu):
            employees.append(StudentEmployee(templine[0], templine[1], templine[2], templine[3], templine[4], templine[5]))
        elif count < int(numStu) + int(numCS) and count >= int(numStu):
            employees.append(ClassifiedStaff(templine[0], templine[1], templine[2], templine[3], templine[4]))
        else:
            employees.append(Faculty(templine[0], templine[1], templine[2], templine[3], templine[4], templine[5]))
        count+= 1
    return employees

def safeSetData(classname):
    pattern = re.compile("[0-9]+")
    temp = input("Enter the number of  " + classname + ": ")
    while not pattern.fullmatch(temp):
            temp = input("Number of " + classname + " must be a non negative number. Following those rules, please try again by entering the number of  " + classname + ": ")
    return temp
x = 1
while x  == 1:
    try:
        file = open(input("Enter file name: "), "r")

        numStu = safeSetData("Students")
        numCS = safeSetData("Classified Staff")
        numFac = safeSetData("Faculty")

        employees = EmployeeAssignment(file)
        file.close()

        print("\t\t\t\t\t\tPay Table\n")
        for entry in employees:
            print(entry)
            
        x = 0
        
    except:
        print("There has been an error with the program. The file entered may not follow the appropriate format or could not be found. Plesae try again.")
