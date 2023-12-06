# Initialize variables to keep track of totals
overtime_total = 0
regular_pay_total = 0
gross_pay_total = 0
employee_count = 0

# Create a loop to continuously enter employee information
while True:
    # Ask the user to enter the name of the employee or "Done" to terminate
    employee_name = input("Enter employee's or 'Done' to terminate: ")

    # Check if the user wants to terminate
    if employee_name.lower() == "done":
        break
    
    # Ask the user to enter the number of hours worked this week
    hours_worked = float(input('How many hours did {} work? '.format(employee_name)))
    
    # Ask the user to enter the employee's pay rate
    pay_rate = float(input("What is {}'s pay rate: ".format(employee_name)))
    
    # Check if the employee worked overtime (more than 40 hours)
    if hours_worked > 40:
        # Calculate the overtime hours
        overtime_hours = hours_worked - 40
        
        # Calculate the amount owed to the employee for overtime hours
        overtime_pay = overtime_hours * (pay_rate * 1.5)
        
        # Calculate the amount employee should be paid for regular hours worked
        regular_pay = 40 * pay_rate
    else:
        overtime_hours = 0
        overtime_pay = 0
        regular_pay = hours_worked * pay_rate
    
    # Calculate the gross pay (total amount that should be paid to the employee)
    gross_pay = regular_pay + overtime_pay
    
    # Display the employee's information and pay details
    print(f"Employee name: {employee_name}\n")
    print(f"Hours Worked\tPay Rate\tOverTime\tOverTime Pay\tRegHour Pay\tGross Pay")
    print("-" * 100)
    print(f"{hours_worked:.1f}\t\t{pay_rate:.2f}\t\t{overtime_hours:.1f}\t\t"
      f"${overtime_pay:.2f}\t\t${regular_pay:.2f}\t\t${gross_pay:.2f}\n")
    
    # Update the totals
    overtime_total += overtime_pay
    regular_pay_total += regular_pay
    gross_pay_total += gross_pay
    employee_count += 1

# Display the totals and the number of employees entered

print("Total number of Employees Entered: ", employee_count)
print("Total amount paid for overtime: $", overtime_total)
print("Total amount paid for regular hours: $", regular_pay_total)
print("Total amount paid in gross: $", gross_pay_total)
