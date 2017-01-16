import unittest
import os
import sys
from TestEmployeeUtils import TestEmployeeUtils
from EmployeeDb import EmployeeDb
from EmployeePage import EmployeePage

class Test_TestEmployeeDbUpdate(unittest.TestCase):
    def test_UpdateEmptyEmployeeDb(self):
        testDataDir = TestEmployeeUtils.GetDataDir()
        urlFile = open(os.path.join(testDataDir, "TestEmployeesIndigo.htm"), 'r')
        urlContent = urlFile.read()

        employeePage = EmployeePage(urlContent)
        
        self.assertEqual(employeePage.count, 138)

        if employeePage.count:
            newDbPath = os.path.join(testDataDir, "newEmployees.db")
            employeeDb = EmployeeDb(newDbPath)
            success = employeeDb.Open()

            self.assertTrue(success)

            if success:
                employeeDb.Update(employeePage)

        #os.remove(newDbPath)

if __name__ == '__main__':
    unittest.main()
