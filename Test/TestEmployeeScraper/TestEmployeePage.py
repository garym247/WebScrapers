import unittest
import os
from TestEmployeeUtils import TestEmployeeUtils
from EmployeePage import EmployeePage

class TestEmployeePage(unittest.TestCase):
    def test_Success(self):
        # Arrange
        testDataDir = TestEmployeeUtils.GetDataDir()
        urlFile = open(os.path.join(testDataDir, "TestEmployeesIndigo.htm"), 'r')
        urlContent = urlFile.read()

        # Act
        employeePage = EmployeePage(urlContent)

        # Assert
        self.assertEqual(employeePage.count, 156)

        #print(employeePage.count)
        #for employee in employeePage:
        #    print(employee)

if __name__ == '__main__':
    unittest.main()


