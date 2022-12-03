from Employee_Class import *
import unittest

class TestEmployeeClasses(unittest.TestCase):
    def testStudentEmployeeCreation(self):
        test = StudentEmployee("Johnny", 10000, True, 40, True, 10)
        self.assertTrue(test.getName() == "Johnny")
        self.assertFalse(test.getName() == "Jimmy")
        
        
        
if __name__ == '__main__':
    unittest.main()