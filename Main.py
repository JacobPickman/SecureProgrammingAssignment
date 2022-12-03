from Employee_Class import Employee, StudentEmployee, ClassifiedStaff, Faculty


file = open(input("Enter file name: "), "r")


numStu = input("Enter the number of students: ")
numCS = input("Enter the number of Classified Staff: ")
numFac = input("Enter the number of Faculty: ")

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

print("\t\t\t\t\t\tPay Table\n")
for entry in employees:
    print()
    print(entry, end = "")
