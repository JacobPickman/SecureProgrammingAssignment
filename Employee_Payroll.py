from Employee_Class import Employee, StudentEmployee, ClassifiedStaff, Faculty

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

x = 1
while x  == 1:
    try:
        file = open(input("Enter file name: "), "r")


        numStu = input("Enter the number of students: ")
        numCS = input("Enter the number of Classified Staff: ")
        numFac = input("Enter the number of Faculty: ")

        employees = EmployeeAssignment(file)
        file.close()

        print("\t\t\t\t\t\tPay Table\n")
        for entry in employees:
            print(entry)
            
        x = 0
        
    except:
        print("There has been an error with the program. The file entered may not follow the appropriate format or could not be found. Plesae try again.")
