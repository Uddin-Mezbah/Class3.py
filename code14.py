class Employee:
    No_of_leavs = 8
    pass

carry = Employee()
Mezbah = Employee()

carry.name = "Carry"
carry.salary = "500$"
carry.role = "Instructor"

Mezbah.name = "Mezbah"
Mezbah.salary = "100$"
Mezbah.rolo = "Student"

print(carry.name)
print(Mezbah.salary)
print(Mezbah.No_of_leavs)
print(carry.__dict__)
carry.No_of_leavs = 10
print(carry.__dict__)
print(Employee.No_of_leavs)


