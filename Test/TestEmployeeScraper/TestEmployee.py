import unittest
from ddt import ddt, data, unpack
from Employee import Employee

@ddt
class Test_TestEmployee(unittest.TestCase):
    @data(("name1", "department1", "region1"), 
          ("name2", "department2", "region2"))
    @unpack
    def test_CreateEmployee(self, name, department, region):
        # Act
        employee = Employee(name, department, region)

        # Assert
        self.assertEqual(employee.name, name)
        self.assertEqual(employee.department, department)
        self.assertEqual(employee.region, region)

    @data("name2", "name3")
    def test_EditEmployeeName(self, name):
        # Arrange
        employee = Employee("name1", "department1", "region1")

        # Act
        employee.name = name

        # Assert
        self.assertEqual(employee.name, name)
        self.assertEqual(employee.department, "department1")
        self.assertEqual(employee.region, "region1")

    @data("department2", "department3")
    def test_EditEmployeeDepartment(self, department):
        # Arrange
        employee = Employee("name1", "department1", "region1")

        # Act
        employee.department = department

        # Assert
        self.assertEqual(employee.name, "name1")
        self.assertEqual(employee.department, department)
        self.assertEqual(employee.region, "region1")

    @data("region2", "region3")
    def test_EditEmployeeRegion(self, region):
        # Arrange
        employee = Employee("name1", "department1", "region1")

        # Act
        employee.region = region

        # Assert
        self.assertEqual(employee.name, "name1")
        self.assertEqual(employee.department, "department1")
        self.assertEqual(employee.region, region)

if __name__ == '__main__':
    unittest.main()
