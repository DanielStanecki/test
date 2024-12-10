class Employee: 
    def __init__(self, name, salary, jobTitle): 
        self.name = name
        self.salary = salary
        self.jobTitle = jobTitle

    def increaseSalary(self): 
        self.salary += 10000
    
class Manager(Employee): 
    def __init__(self, name, salary, jobTitle, yearsOfExp): 
        super().__init__(name, jobTitle, salary)
        self.yearsOfExp = yearsOfExp
        self.employeesManaged = []
    
    def increaseSalary(self): 
        super().increaseSalary()
        super().increaseSalary()
    
    def getSum(self): 
        print(self.name, self.jobTitle, self.salary, self.yearsOfExp, self.employeesManaged)
    
class Boss(Manager): 
    def __init__(self, name, salary, jobTitle, yearsOfExp, age): 
        super().__init__(name, jobTitle, salary, yearsOfExp)
        self.Number = age

    def getSum(self):
        print(self.name, self.jobTitle, self.salary, self.yearsOfExp, self.employeesManaged, self.Number)

daniel = Boss("Daniel", 12390, "Boss", 12, 18 )
daniel.increaseSalary()
daniel.getSum()