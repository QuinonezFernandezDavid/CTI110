# This is a program that let the user manage their grades.
# Quinonez Fernaned


# This program takes a number grade , determines average and displays letter grade for average.

# Enter grades for six modules

mod_1 = float(input('Enter grade for Module 1: '))
mod_2 = float(input('Enter grade for Module 2: '))
mod_3 = float(input('Enter grade for Module 3: '))
mod_4 = float(input('Enter grade for Module 4: '))
mod_5 = float(input('Enter grade for Module 5: '))
mod_6 = float(input('Enter grade for Module 6: '))

# add grades entered to a list
Grades = [mod_1, mod_2, mod_3, mod_4, mod_5, mod_6]

print('------------Results------------')

# TO DO: determine lowest, highest , sum and average for grades
Lowest_Grade = min(Grades)
print(f'Lowest Grade:       {Lowest_Grade}')

Highest_Grade = max(Grades)
print(f'Highest Grade:      {Highest_Grade}')

Sum_of_Grade = sum(Grades)
print(f'Sum of Grades:      {Sum_of_Grade}')

Average = sum(Grades)/len(Grades)
print(f'Average:            {Average:.2f}')

print('----------------------------------------')

# determine letter grade for average

if Average >= 90:
 print('Your Grade is: A')
 
elif Average >= 80:
 print('Your Grade is: B')

elif Average >= 70:
 print('Your Grade is: C')
 
elif Average <= 65:
 print('Your Grade is: F') 
# end



