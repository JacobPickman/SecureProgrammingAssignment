import unittest
from unittest import mock
from Employee_Payroll import EmployeeAssignment

class TestEmployeeClasses(unittest.TestCase):
    def testEmployeeAssignment(self):
        file = open(input("Enter file name"))
        test = EmployeeAssignment(file)
        for line in test:
            print(line)
    
    
if __name__ == '__main__':
    unittest.main()
