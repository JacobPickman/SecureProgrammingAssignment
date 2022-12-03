from Employee_Class import *
import unittest

class TestEmployeeClasses(unittest.TestCase):
    def testStudentEmployeeCreation(self):
        test = StudentEmployee("Johnny", 10000, True, 40, True, 10)
        self.assertTrue(test.getName() == "Johnny")
        self.assertFalse(test.getName() == "Jimmy")
        
        self.assertTrue(test.getNum() == 10000)
        self.assertFalse(test.getNum() == 1000)
        self.assertFalse(test.getNum() == 1)
        self.assertFalse(test.getNum() == 0)
        
        
        
if __name__ == '__main__':
    unittest.main()