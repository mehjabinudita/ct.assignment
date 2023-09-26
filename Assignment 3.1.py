h_worked = float(input("Enter the number of hours worked: "))
h_wage = float(input("Enter the hourly wage: "))

if h_worked <= 40:
    salary = h_worked * h_wage
else:
    regular_hours = 40
    overtime_hours = h_worked - 40
    salary = (regular_hours * h_wage) + (overtime_hours * (h_wage * 1.5))
print(f"The salary is: ${salary:.2f}")