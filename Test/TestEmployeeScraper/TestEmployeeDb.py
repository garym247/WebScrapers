import unittest
from ddt import ddt, data, unpack
import shutil
import os
import sys
from TestEmployeeUtils import TestEmployeeUtils
from datetime import date
from Employee import Employee
from EmployeeDb import EmployeeDb
from EmployeePage import EmployeePage

TestEmployeesMaster = ".\Data\TestEmployeesMaster.db"
TestEmployeesWorking = ".\Data\TestEmployeesWorking.db"

@ddt
class Test_TestEmployeeDb(unittest.TestCase):
    def setUp(self):
        if os.path.isfile(TestEmployeesWorking):
            os.remove(TestEmployeesWorking)

        shutil.copyfile(TestEmployeesMaster, TestEmployeesWorking)

    def tearDown(self):
        os.remove(TestEmployeesWorking)
            
    def test_AddEmployee(self):
        # Arrange
        employeeDb = EmployeeDb(TestEmployeesWorking)
        employeeDb.Open()

        employee = Employee("mary o'rorke", "sales", "america")

        countBefore = employeeDb.Count()

        # Act
        employeeDb.Add(employee)

        # Assert
        countAfter = employeeDb.Count()
        (dateAdded, dateRemoved) = employeeDb.GetDates(employee.name, employee.department, employee.region)

        self.assertEqual(countAfter - countBefore, 1)
        self.assertEqual(dateAdded, str(date.today()))
        self.assertIsNone(dateRemoved)

        employeeDb = None

    def test_AddExistingEmployee(self):
        # Arrange
        employeeDb = EmployeeDb(TestEmployeesWorking)
        employeeDb.Open()

        countBefore = employeeDb.Count()

        # Act
        employee = Employee("fred", "sales", "america")
        employeeDb.Add(employee)

        # Assert
        countAfter = employeeDb.Count()
        self.assertEqual(countAfter - countBefore, 0)

        employeeDb = None

    def test_RemoveEmployee(self):
        #Arrange
        employeeDb = EmployeeDb(TestEmployeesWorking)
        employeeDb.Open()

        countBefore = employeeDb.Count()

        #Act
        employee = Employee("john", "finance", "uk")
        employeeDb.Remove(employee)

        #Assert
        countAfter = employeeDb.Count()
        (dateAdded, dateRemoved) = employeeDb.GetDates(employee.name, employee.department, employee.region)
        
        self.assertEqual(countAfter, countBefore)
        self.assertEqual(dateRemoved, str(date.today()))

        employeeDb = None

    def test_EmployeeAlreadyExists(self):
        #Arrange
        employeeDb = EmployeeDb(TestEmployeesWorking)
        employeeDb.Open()

        #Act
        employee = Employee("bob", "engineering", "dubai")
        exists = employeeDb.Exists(employee)

        #Assert
        self.assertTrue(exists)

        employeeDb = None

    def test_EmployeeDoesNotExist(self):
        #Arrange
        employeeDb = EmployeeDb(TestEmployeesWorking)
        employeeDb.Open()

        #Act
        employee = Employee("bob", "engineering", "uk")
        exists = employeeDb.Exists(employee)

        #Assert
        self.assertFalse(exists)

        employeeDb = None

    def test_GetNewEmployees(self):
        #Arrange
        testDataDir = TestEmployeeUtils.GetDataDir()
        employeePageFile = open(os.path.join(testDataDir, "TestEmployees.htm"), 'r')
        pageContent = employeePageFile.read()

        employeePage = EmployeePage(pageContent)
        employeeRows = [("bob", "engineering", "usa"), ("fred", "sales", "uk")]

        #Act
        newEmployees = EmployeeDb.GetNewEmployees(employeeRows, employeePage )

        #Assert
        self.assertEqual(len(newEmployees), 1)
        self.assertEqual(newEmployees[0].name, "lucy")
        self.assertEqual(newEmployees[0].department, "sales")
        self.assertEqual(newEmployees[0].region, "usa")

    def test_GetDeletedEmployees(self):
        #Arrange
        testDataDir = TestEmployeeUtils.GetDataDir()
        employeePageFile = open(os.path.join(testDataDir, "TestEmployees.htm"), 'r')
        pageContent = employeePageFile.read()

        employeePage = EmployeePage(pageContent)
        employeeRows = [("bob", "engineering", "usa"), ("fred", "sales", "uk"), ("andy", "finance", "germany")]

        #Act
        deletedEmployees = EmployeeDb.GetRemovedEmployees(employeeRows, employeePage )

        #Assert
        self.assertEqual(len(deletedEmployees), 1)
        self.assertEqual(deletedEmployees[0].name, "andy")
        self.assertEqual(deletedEmployees[0].department, "finance")
        self.assertEqual(deletedEmployees[0].region, "germany")

if __name__ == '__main__':
    try:
        unittest.main()
    except SystemExit:
        print("system exit")
    except:
        exception = sys.exc_info()[0]
        print("Unexpected error: ", sys.exc_info()[0])
        print("Exiting program: Unhandled exception")
