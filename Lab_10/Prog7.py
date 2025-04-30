# Add Data

import pickle
class Employee:
    def __init__(self, empcode, empname, doj, salary):
        self.empcode = empcode
        self.empname = empname
        self.doj = doj  
        self.salary = salary

    def display(self):
        print(f"Employee Code: {self.empcode}")
        print(f"Name: {self.empname}")
        print(f"Date of Joining: {self.doj}")
        print(f"Salary: {self.salary}")


emp = Employee(100, "Dev", "22-07-2024", 55000)

with open("7.pkl", "wb") as file:
    pickle.dump(emp, file)

print(" Employee Object Successfully Serialized !")

with open("EM.pkl", "rb") as file:
    loaded_emp = pickle.load(file)

print(" Deserialized Employee object:")
loaded_emp.display()
