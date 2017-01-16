import sys
import time
import datetime
import EmployeeDb
from urllib.request import urlopen

from bs4 import BeautifulSoup

# DbUser = "guz"
# DbPassword = "guz"
# DbHost = "127.0.0.1"
DbPath = "G:\MyStuffProgramming\Python\EmployeeScan\EmployeeScan\Employees.db"

#SqlDropTable = "DROP TABLE IF EXISTS employees"
#SqlSelectAll = "SELECT COUNT(*) FROM employees"

#SqlCreateEmployees = "CREATE TABLE IF NOT EXISTS employees (name TEXT, department TEXT, region TEXT, dateAdded DATE, dateRemoved DATE)"
#SqlFindEmployee = "SELECT COUNT(*) FROM employees WHERE name = '{0}' AND department = '{1}' AND region = '{2}'"
#SqlAddEmployee = "INSERT INTO employees (name, department, region, dateAdded, dateRemoved) VALUES (?, ?, ?, ?, ?)"
#SqlRemoveEmployee = "UPDATE employees SET dateRemoved = '{0}' WHERE name = '{1}' AND department = '{2}' AND region = '{3}'"


def main():
    employeeDb = EmployeeDb(DbPath) 

    employeeDb.AddEmployee("x1", "x2", "x3")
    employeeDb.AddEmployee("y1", "y2", "y3")
    employeeDb.AddEmployee("z1", "z2", "z3")

    #dbConn = sqlite3.connect()
    
    #dbConn.execute(SqlCreateEmployees)

    
    #AddEmployee(dbConn, "b1", "b2", "b3")
    #AddEmployee(dbConn, "c1", "c2", "c3")
    #AddEmployee(dbConn, "b1", "b2", "b3")
    #AddEmployee(dbConn, "f1", "f2", "f3")
    
    #dbConn.close()

    #AddEmployee(db, "a1", "a2", "a3")
    #db.execute(SqlDropTable)
    #db.execute(SqlCreateTable)
    #db.commit()

if __name__ == '__main__':
    try:
        main()
    except:
        exception = sys.exc_info()[0]
        print("Unexpected error: ", sys.exc_info()[0])
        print("Exiting program: Unhandled exception")
