from abc import ABC, abstractmethod

class Employee(ABC):

    def __init__(self, name, number, working):
        self.__name = name
        self.__number = number
        self.__working = working

    def getName(self):
        return self.__name

    def getNum(self):
        return self.__number

    def getWork(self):
        return self.__working

    def setName(self, name):
        self.__name = name

    def setNum(self, num):
        self.__number = num

    def setWork(self, work):
        self.__working = work

    @abstractmethod
    def getPay(self):
        pass

    def __str__(self):
        return "Name: "+ str(self.__name) + "\tID: " + str(self.__number) + "\tCurrently Working: " + str(self.__working)



class StudentEmployee(Employee):
    def __init__(self, name, num, working, hours, workstudy, rate):
        super().__init__(name, num, working)
        self.__hours = hours
        self.__workstudy = workstudy
        self.__rate = rate

    def getPay(self):
        return self.__hours * self.__rate

    def __str__(self):
        return super(StudentEmployee, self).__str__() + "\tHours Worked: " + str(self.__hours) + "\tEnrolled Workstudy: " + str(self.__workstudy) +"\tPay Rate: " + str(self.__rate)



class ClassifiedStaff(Employee):
    def __init__(self, name, num, working, sal, div):
        super().__init__(name, num, working)
        self.__sal = sal
        self.__div = div

    def getPay(self):
        return int(self.__sal) * 2

    def __str__(self):
        return super(ClassifiedStaff, self).__str__() +"\tBiweekly Pay: " +  str(self.getPay())


class Faculty(Employee):
    def __init__(self, name, num, working, sal, week, dept):
        super().__init__(name, num, working)
        self.__sal = sal
        self.__week = week
        self.__dept = dept

    def getPay(self):
        return (self.__sal / self.__week) * 2

    def __str__(self):
        return super(Faculty, self).__str__() + "\tSalary: " + str(self.__sal) + "\tPay Period: " + str(self.__week) + " weeks\tDepartment: " + str(self.__dept)
