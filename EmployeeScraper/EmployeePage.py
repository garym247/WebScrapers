from bs4 import BeautifulSoup
from Employee import Employee

class EmployeePage(object):
    """description of class"""

    def __init__(self, pageData):
        self._employees = self.Parse(pageData)

    def Parse(self, pageData):
        soup = BeautifulSoup(pageData)
        #print(soup.prettify())

        employees = []

        rows = soup.find_all("tr")

        # The first two rows in the table are headers so ignore them.
        for row in rows[2:]:
            #print(row)
            cols = row.find_all("td")
            
            #print(len(cols))

            if self.IsEmployeeRow(cols):
                name = cols[0].a.get_text()
                dept = cols[1].get_text()
                region = cols[2].get_text()
            
                employee = Employee(name, dept, region)
            
                employees.append(employee)
        
        return employees

    def HasEmployee(self, name, department, region):
        for employee in self._employees:
            if name == employee.name and department == employee.department and region == employee.region:
                return True
        return False

    def IsEmployeeRow(self, cols):
        try:
            colText = cols[0].a.get_text().lower()
        except AttributeError:
            return False

        colWords = set(colText.split(" "))
        nonEmployeeWords = {"room", "lab", "conference", "sales", "support", "partner"}

        inter = colWords.intersection(nonEmployeeWords)
        if not colWords.intersection(nonEmployeeWords):
            return True
        else:
            return False

    def __iter__(self):
        return EmployeePageIter(self._employees)

    def __str__(self):
        outputString = ""
        for employee in self.employees:
            outputString += str(employee)
            outputString += "\n"
        return outputString

    @property
    def employees(self):
        return self._employees

    @property
    def count(self):
        return len(self._employees)


class EmployeePageIter(object):
    """description of class"""

    def __init__(self, employees):
        self._employees = employees
        self._current = 0

    def __next__(self):
        if self._current < len(self._employees):
            employee = self._employees[self._current]
            self._current += 1
            return employee
        else:
            raise StopIteration()
