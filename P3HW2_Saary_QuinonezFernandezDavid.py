# This program will process employess and their pay. The program read an employee's name, hourly pay rate, day of work, and the amount of hours.
# CTI-110
# P3HW2 - Salary
# Quinonez Fernandez, David 

# Enter name of employee
Employee_name = input("Enter employee's name: ")

# Enter number of hours the employee worked this week
hours_worked = float(input("Enter number of hours worked: "))

# Enter employee's pay rate
pay_rate = float(input("Enter employee's pay rate: "))
print()

print("-" * 40)


#Calculate regular pay (up to 40 hours) and over time
if hours_worked <= 40:
    regular_pay = hours_worked * pay_rate
    overtime_pay = 0
else:
    regular_pay = 40 * pay_rate
    overtime_hours = hours_worked - 40
    overtime_pay = overtime_hours * (pay_rate * 1.5)
    
gross_pay = regular_pay + overtime_pay
# Display employee details
print(f"Employee name: {Employee_name}\n")
print(f"Hours Worked\tPay Rate\tOverTime\tOverTime Pay\tRegHour Pay\tGross Pay")
print("-" * 100)
print(f"{hours_worked:.1f}\t\t{pay_rate:.2f}\t\t{overtime_hours:.1f}\t\t"
      f"${overtime_pay:.2f}\t\t${regular_pay:.2f}\t\t${gross_pay:.2f}\n")
