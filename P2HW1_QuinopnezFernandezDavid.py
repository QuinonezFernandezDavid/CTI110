# This will be my first python progrfan
# 10/1/23
# CTL-110 P1HW2 - Travel Expense
# Quinonez fernandez, David

print('This progran calculate and display travel expenses')

print()

# Ask user to enter their budget
InitialBudget = float(input('Enter Budget: ')) 

print()

 # Ask user to enter travel destination
Location = input('Enter Your travel destination: ')

print()

# Ask user for amount they will spend on gas
Fuel = float(input('How much do you think you will spend on gas? '))

print()

 # Ask user for amount they will spend on accommodation
Accomodation = float(input('Approximately, how much will you need for accomodation/hotel? '))

print()

 # Ask user for amount they will spend on food
Foot = float(input('Last, How much do you need for travel foot? '))

print()

# Add expenses
print("------------Travel Expenses------------")

print(f'Location:            {Location}')

print(f'Initial Budget:      ${InitialBudget}')

print(f'Fuel:                ${Fuel}')

print(f'Accomodation:        ${Accomodation}')

print(f'Foot:                ${Foot}')

print('----------------------------------------')

print()

# Subtract expenses from budget
RemainingBalance = float(int(InitialBudget) - int(Fuel) - int(Accomodation) - int(Foot))

# Display results
print(f'Remaining Balance:   ${RemainingBalance}')


