from Employee_Class import *
import unittest

class TestEmployeeClasses(unittest.TestCase):
    def testStudentEmployee(self):
        test = StudentEmployee("Johnny", 10000, True, 40, True, 10)
        self.assertTrue(test.getName() == "Johnny")
        self.assertFalse(test.getName() == "Jimmy")
        
        self.assertTrue(test.getNum() == 10000)
        self.assertFalse(test.getNum() == 1000)
        self.assertFalse(test.getNum() == 1)
        self.assertFalse(test.getNum() == 0)
        
        self.assertTrue(test.getWork())
        self.assertFalse(test.getWork() == False)
        
        test.setName("Teddy")
        self.assertTrue(test.getName() == "Teddy")
        self.assertFalse(test.getName() == "Johnny")
        
        test.setNum(20000)
        self.assertTrue(test.getNum() == 20000)
        self.assertFalse(test.getNum() == 10000)
        
        test.setWork(False)
        self.assertTrue(test.getWork() == False)
        self.assertFalse(test.getWork() == True)
        
        self.assertTrue(test.getPay() == 400)
        self.assertFalse(test.getPay() == 500)
        self.assertFalse(test.getPay() == 0)
        self.assertFalse(test.getPay() == 1)
        
        testLine = print(test)
        #self.assertTrue(testLine == "Name: Teddy\tID: 20000\tCurrently Working: False\tHours Worked: 40\tEnrolled Workstudy: True\tPay Rate: 10")


        
        
        
        
if __name__ == '__main__':
    unittest.main()