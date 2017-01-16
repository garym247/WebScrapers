import sys
from urllib.request import urlopen
from EmployeePage import EmployeePage
from EmployeeDb import EmployeeDb

EmployeeDbPath = "G:\git\WebScrapers\EmployeeScraper\Employees.db"
EmployeeUrl = "http://www.rippingrecords.com/index.php"

def GetUrlContent(url):
    print("Openning url....{0}".format(url), end="")
    try:
        uf = urlopen(url, None, 5)
        content = uf.read()
    except urllib.request.URLError:
        print("...failed")
        return ""
    except:
        print("...caught an unhandled exception (OpenUrl)")
        return ""

    print("....success ({0} bytes read)".format(len(content)))

    return content

def GetContent():
    urlFile = open(r"G:\git\WebScrapers\Test\TestEmployeeScraper\Data\TestEmployeesIndigo.htm", 'r')
    urlContent = urlFile.read()

    return urlContent

def main():
    urlContent = GetContent()
    
    employeePage = EmployeePage(urlContent)

    if employeePage.count:
        employeeDb = EmployeeDb(EmployeeDbPath)
        success = employeeDb.Open()

        if success:
            employeeDb.Update(employeePage)

if __name__ == '__main__':
    try:
        main()
    except:
        exception = sys.exc_info()[0]
        print("Unexpected error: ", sys.exc_info()[0])
        print("Exiting program: Unhandled exception")
