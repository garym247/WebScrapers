import unittest
from EmployeeDb import EmployeeDb
from TestEmployeeUtils import TestEmployeeUtils
import shutil
import os
import sys
import sqlite3
 
class Test_TestEmployeeDbCreation(unittest.TestCase):
    def test_createNew(self):
        # Arrange
        testDataDir = TestEmployeeUtils.GetDataDir()
        newDbPath = os.path.join(testDataDir, "newEmployee.db")
        
        if os.path.exists(newDbPath):
            os.remove(newDbPath)

        # Act
        employeeDb = EmployeeDb(newDbPath)
        success = employeeDb.Open()
        employeeDb = None

        # Assert
        self.assertTrue(success)   
        self.assertTrue(os.path.exists(newDbPath))

        dbConn = sqlite3.connect(newDbPath)
        cursor = dbConn.cursor()
        cursor.execute("SELECT name FROM sqlite_master WHERE type='table'")
        tables = cursor.fetchall()
        cursor.close()
        dbConn.close()

        self.assertTrue("employees" in tables[0])

        # Tidy up
        os.remove(newDbPath)

    def test_openExistingValidDb(self):
        # Arrange
        testDataDir = TestEmployeeUtils.GetDataDir()
        validDbPath = os.path.join(testDataDir, "TestEmployeesMaster.db")

        # Act
        employeeDb = EmployeeDb(validDbPath)    
        success = employeeDb.Open()
        employeeDb = None

        # Assert
        self.assertTrue(success)

    def test_openExistingNotValidDb(self):
        # Arrange
        testDataDir = TestEmployeeUtils.GetDataDir()
        notValidDbPath = os.path.join(testDataDir, "TestInvalidEmployees.db")

        # Act
        employeeDb = EmployeeDb(notValidDbPath)    
        success = employeeDb.Open()
        employeeDb = None

        # Assert
        self.assertFalse(success)

    def test_createBadPath(self):
        # Arrange
        testDataDir = TestEmployeeUtils.GetDataDir()
        badDbPath = os.path.join(testDataDir, "Employees\%*?.db")

        # Act
        employeeDb = EmployeeDb(badDbPath)
        success = employeeDb.Open()
        employeeDb = None

        # Assert
        self.assertFalse(success)

    def test_openNonDb(self):
        # Arrange
        testDataDir = TestEmployeeUtils.GetDataDir()
        notDbPath = os.path.join(testDataDir, "TestNonDb.txt")

        # Act
        employeeDb = EmployeeDb(notDbPath)
        success = employeeDb.Open()
        employeeDb = None

        # Assert
        self.assertFalse(success)

if __name__ == '__main__':
    try:
        unittest.main()
    except SystemExit:
        print("system exit")
    except:
        exception = sys.exc_info()[0]
        print("Unexpected error: ", sys.exc_info()[0])
        print("Exiting program: Unhandled exception")
