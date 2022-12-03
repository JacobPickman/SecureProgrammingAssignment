from abc import ABC, abstractmethod

class Employee(ABC):
    
    def __init__(self, name, number, working):
        self.name = name
        self.number = number
        self.working = working
    
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
        return str(self.__name) + "\t" + str(self.__num) + "\t" + str(self.__working)
    
    
    
class StudentEmployee(Employee):
    def __init__(self, name, number, working, hours, workstudy, rate):
        self.name = name
        self.number = number
        self.working = working
        self.hours = hours
        self.workstudy = workstudy
        self.rate = rate

    def getPay(self):
        return self.__hours * self.__rate
    
    def __str__(self):
        return super()+ "\t" + self.__hours + "\t" + self.__workstudy + "\t" + self.__rate;
    


class ClassifiedStaff(Employee):
    def __init__(self, name, num, working, sal, div):
        self.__name = name
        self.__num = num
        self.__working = working
        self.__sal = sal
        self.__div = div
        
    def getPay(self):
        return self.__sal * 2
    
    def __str__(self):
        return super() +"\t" +  self.__sal +"\t" +  self.__div
    
    
class Faculty(Employee):
    def __init__(self, name, num, working, sal, week, dept):
        self.__name = name
        self.__num = num
        self.__working = working
        self.__sal = sal
        self.__week = week
        self.__dept = dept
        
    def getPay(self):
        return (sal / week) * 2
    
    def __str__(self):
        return super().__str__ + "\t" +  str(self.__sal) + "\t" + str(self.__week) + "\t" + str(self.__dept)