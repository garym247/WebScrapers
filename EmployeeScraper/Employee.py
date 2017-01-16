class Employee(object):
    """description of class"""

    def __init__(self, name, department, region):
        self.name = name
        self.department = department
        self.region = region
    
    def __str__(self):
        return "{0:28} {1:20} {2:15}".format(self.name, self.department, self.region)

    @property
    def name(self):
        return self._name
    @name.setter
    def name(self, value):
        self._name = value

    @property
    def department(self):
        return self._department
    @department.setter
    def department(self, value):
        self._department = value

    @property
    def region(self):
        return self._region
    @region.setter
    def region(self, value):
        self._region = value


