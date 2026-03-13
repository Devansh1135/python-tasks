from dataclasses import dataclass
import re

@dataclass(frozen=True)
class Employee:
    id: int
    name: str
    email: str
    salary: int
    department: str
    hire_date: int
    depts = ['Python','Node','React','AIML']
    pattern = r"[a-zA-Z0-9]+@[a-zA-Z]+.[a-zA-Z]+"
    def __post_init__(self):
        if not re.fullmatch(r"[a-zA-Z]+\d+@[a-zA-Z]+.[a-zA-Z]+", self.email):
            raise TypeError("Invalid email!!!")

        if self.salary <= 0:
            raise ValueError("Salary has to vbe a positive value!!!")
        
        if self.department not in self.depts:
            raise ValueError("Department does not exist!!!")
        
    
    def __str__(self):
        return f'''
Employee name : {self.name}
Employee ID : {self.id}
email : {self.email}
salary : ${self.salary}
department: {self.department} 
'''
    
    @classmethod
    def order_salary(cls, employees):
        return sorted(employees, key = lambda emp : emp.salary, reverse=True)



        
