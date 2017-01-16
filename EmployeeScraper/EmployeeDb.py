import os
import sys
import sqlite3
from Employee import Employee

EmployeesTableName = "employees"

SqlDropTable = "DROP TABLE IF EXISTS employees"
SqlSelectAll = "SELECT COUNT(*) FROM employees"
SqlListTables = "SELECT name FROM sqlite_master WHERE type='table'"
SqlCreateEmployees = "CREATE TABLE IF NOT EXISTS employees (name TEXT, department TEXT, region TEXT, dateAdded DATE, dateRemoved DATE)"
SqlEmployeeCount = "SELECT COUNT(*) FROM employees"
SqlSelectEmployees = "SELECT * FROM employees"
SqlAddEmployee = "INSERT INTO employees (name, department, region, dateAdded, dateRemoved) VALUES (?, ?, ?, date(), NULL)"
SqlRemoveEmployee = "UPDATE employees SET dateRemoved = date() WHERE name = ? AND department = ? AND region = ?"
SqlFindEmployee = "SELECT COUNT(*) FROM employees WHERE name = ? AND department = ? AND region = ?"
SqlGetEmployeeDates = "SELECT dateAdded, dateRemoved FROM employees WHERE name = ? AND department = ? AND region = ?"

class EmployeeDb(object):
    def __init__(self, dbPath):
        self.dbPath = dbPath
        self.dbConn = None

    def __del__(self):
        if self.dbConn:
            self.dbConn.close()

    def Open(self):
        if os.path.exists(self.dbPath):
            return self.OpenExisting()
        else:
            return self.CreateNew()

    def OpenExisting(self):
        isValid = False
        try:
            self.dbConn = sqlite3.connect( self.dbPath )
            cursor = self.dbConn.cursor()
            cursor.execute(SqlListTables)

            tables = cursor.fetchall()
            isValid = EmployeesTableName in tables[0]
        except sqlite3.DatabaseError:
            pass
        except sqlite3.OperationalError:
            pass
              
        return isValid

    def CreateNew(self):
        success = False
        try:
            self.dbConn = sqlite3.connect( self.dbPath )
            cursor = self.dbConn.cursor()
            cursor.execute(SqlCreateEmployees)
            success = True
        except sqlite3.OperationalError:
            pass

        return success

    def Update(self, employeePage):
        # Extract all the current employees from the database
        cursor = self.dbConn.cursor()
        cursor.execute(SqlSelectEmployees)
        employeeRows = cursor.fetchall()
        cursor.close()

        # Determine which employees have been added and removed.
        employeesToAdd = EmployeeDb.GetNewEmployees(employeeRows, employeePage)
        employeesToRemove = EmployeeDb.GetRemovedEmployees(employeeRows, employeePage)

        # Add the new employees tp the database
        for employee in employeesToAdd:
            self.Add(employee)

        # Remove the deleted employees from the database (i.e. populate the "dateRemoved" column)
        for employee in employeesToRemove:
            self.Remove(employee)

    def GetNewEmployees(employeeRows, employeePage):
        newEmployees = []

        for employee in employeePage:
            found = False
            for row in employeeRows:
                if employee.name == row[0] and employee.department == row[1] and employee.region == row[2]:
                    found = True
                    break
            
            if not found:
                newEmployees.append(employee)

        return newEmployees

    def GetRemovedEmployees(employeeRows, employeePage):
        removedEmployees = []

        for row in employeeRows:
            if not employeePage.HasEmployee(row[0], row[1], row[2]):
                employee = Employee(row[0], row[1], row[2])
                removedEmployees.append(employee)

        return removedEmployees        

    def Add(self, employee):
        if not self.Exists(employee):
            cursor = self.dbConn.cursor()
            cursor.execute(SqlAddEmployee, (employee.name, employee.department, employee.region))
            self.dbConn.commit()
            cursor.close()

    def Remove(self, employee):
        if self.Exists(employee):
            cursor = self.dbConn.cursor()
            cursor.execute(SqlRemoveEmployee, (employee.name, employee.department, employee.region))
            cursor.close()
        else:
            # TODO: raise an exception
            print("Employee not found {0}, {1}, {2}".format(employee.name, employee.department, employee.region))

    def Exists(self, employee):
        cursor = self.dbConn.cursor()
        cursor.execute(SqlFindEmployee, (employee.name, employee.department, employee.region) )
        result=cursor.fetchone()
        cursor.close()

        return True if result[0] else False

    def Count(self):
        cursor = self.dbConn.cursor()
        cursor.execute(SqlEmployeeCount)
        result=cursor.fetchone()
        cursor.close()

        return result[0]

    def GetDates(self, name, department, region):
        cursor = self.dbConn.cursor()
        cursor.execute(SqlGetEmployeeDates, (name, department, region))
        result=cursor.fetchone()
        cursor.close()

        return result

