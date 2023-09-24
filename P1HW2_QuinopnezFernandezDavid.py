# This will be my first python progrfan
# 10/1/23
# CTL-110 P1HW2 - Travel Expense
# Quinonez fernandez, David

#  Ask user to enter their budget
# Ask user to enter travel destination
# Ask user for amount they will spend on gas
# Ask user for amount they will spend on accommodation
# Ask user for amount they will spend on food
# Add expenses
# Subtract expenses from budget
# Display results

print('This progran calculate and display travel expenses')

print()

InitialBudget = input('Enter Budget: ')

print()

Location = input('Enter Your travel destination: ')

print()

Fuel = input('How much do you think you will spend on gas? ')

print()

Accomodation = input('Approximately, how much will you need for accomodation/hotel? ')

print()

Foot = input('Last, How much do you need for travel foot? ')

print()

print("------------Travel Expenses------------")

print("Location: " + Location)

print("Inicial Budget: " + InitialBudget)

print()

print("Fuel: " + Fuel)

print("Accomodation:" + Accomodation)

print("Foot: " + Foot)

print()

RemainingBalance = int(InitialBudget) - int(Fuel) - int(Accomodation) - int(Foot)
print("Remaining Balance: " , RemainingBalance)
