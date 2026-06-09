from abc import ABC, abstractmethod

class AbstractEmployee(ABC):
  company_name = "Pluralsight"
  def __init__(self, name, employee_id, email):
    self.name = name
    self.employee_id = employee_id
    self.email = email
    return


  def get_contact_info(self):
    return f"{self.name} ({self.company_name}) can be reached at {self.email}"

  @abstractmethod 
  def get_role_description(self):
    pass

class Employee(AbstractEmployee):
  def get_role_description(self):
    return "General employee"

class FullTimeEmployee(AbstractEmployee):
  def __init__(self,name, employee_id, email, salary):
    super().__init__(name, employee_id, email)
    self.salary = salary

  def is_high_earner(self):
    if self.salary >= 100000:
      return True
    else:
      return False
  def get_role_description(self):
    return "Full-time employee"

class Intern(AbstractEmployee):
  def __init__(self, name, employee_id, email, school):
    super().__init__(name, employee_id, email)
    self.school = school

  def get_contact_info(self):
    return f"{self.name} (from {self.school} at {self.company_name}) can be reached at {self.email}"

  def get_role_description(self):
    return f"Intern from {self.school}"

employees = []
def add_employee(employee):
  employees.append(employee)


employee1 = Employee("Alice", 101, "alice@example.com")
employee2 = FullTimeEmployee("Bob", 102, "bob@example.com", 105000)
employee3 = Intern("Charlie", 103, "charlie@example.com", "State University")

add_employee(employee1)
add_employee(employee2)
add_employee(employee3)

for emp in employees:
    if isinstance(emp, FullTimeEmployee):
        if emp.is_high_earner():
            print(f"{emp.name} is a high earner.")
        else:
            print(f"{emp.name} is not a high earner.")
    else:
        print(f"{emp.name} does not have a salary attribute.")
