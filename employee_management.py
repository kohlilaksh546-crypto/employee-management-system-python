import json
def load():
  try:
    with open("employee.json","r") as file:
        data=json.load(file)
        return data
  except:
    return []
def save():
    data=[]
    for employee in employees:
        data.append(employee.to_dict())
    with open("employee.json","w") as file:
           json.dump(data,file,indent=4)
class employee:
    def __init__(self,emp_id,name,department,salary):
        self.emp_id=emp_id
        self.name= name
        self.department=department
        self.salary=salary
    def to_dict(self):
        return {
        "emp_id":self.emp_id,
        "name":self.name ,
        "department":self.department,
        "salary":self.salary
        }
    def display(self):
         print("Emp_id=>",self.emp_id)
         print("Name =>",self.name)
         print("Department=>",self.department)
         print("Salary=>",self.salary)
    def update_salary(self):
        found=False
        search=input("Please enter the name of the employee to update salary")
        new_salary=int(input("Please enter the new salary"))
        for employee in employees:
            if employee.name.lower() ==search.lower():
                employee.salary=new_salary
                print("Salary updated")
                found=True
                save()
        if not found:
            print("No result found")
    def search_emp(self):
        found = False
        search = input("Please enter the name of the employee whom you want to search ==>")
        for employee in employees:
            if employee.name.lower() == search.lower():
                print("Employee found")
                employee.display()
                found = True
        if not found:
            print("No result found")
    def delete_emp(self):
            found = False
            search = input("Please enter the name of the employee whom you want to delete")
            for employee in employees:
                if employee.name.lower() == search.lower():
                    employees.remove(employee)
                    print("Employee deleted")
                    save()
                    for em in employees:
                      em.display()
                    found = True
            if not found:
                print("No result found")
employees=load()
while True:
    print("""
    1: Add Employee
    2: View Employee
    3: Update Salary
    4: Search employee
    5: Delete employee
    6:exit
    """)
    choice=int(input("Please enter the service you want to use==>"))
    if choice==1:
        emp_id = int(input("Please enter the employee id ==>"))
        name = input("Please enter the name ==>")
        department = input("Please enter your department==>")
        salary = int(input("Please enter your salary==>"))

        emp = employee(emp_id, name, department, salary)
        employees.append(emp)
        save()
    elif choice==2:
        for emplo in employees:
          emplo.display()
    elif choice==3:
        emp.update_salary()
    elif choice==4:
        emp.search_emp()
    elif choice==5:
        emp.delete_emp()
    elif choice==6:
        break