# CTI-110

# P2HW2 - List

# Quinonez Fernandez, David d

# 10/15/23

#Enter grade for module 1
Module_1 = float(input('Enter grade for Module 1: '))

#Enter grade for module 2
Module_2 = float(input('Enter grade for Module 2: '))

#Enter grade for module 3
Module_3 = float(input('Enter grade for Module 3: '))

#Enter grade for module 4
Module_4 = float(input('Enter grade for Module 4: '))

#Enter grade for module 5
Module_5 = float(input('Enter grade for Module 5: '))

#Enter grade for module 6
Module_6 = float(input('Enter grade for Module 6: '))

print()

print('------------Results------------')

#Get lowest grade in the list
Grade = [Module_1, Module_2, Module_3, Module_4, Module_5, Module_6]

Lowest_Grade = min(Grade)

print(f'Lowest Grade:       {Lowest_Grade}')
#Get highest grade in the list
Grade = [Module_1, Module_2, Module_3, Module_4, Module_5, Module_6]

Highest_Grade =max(Grade)

print(f'Highest Grade:      {Highest_Grade}')

#Sum all grade
Grade = [Module_1, Module_2, Module_3, Module_4, Module_5, Module_6]

Sum_of_Grade = sum(Grade)

print(f'Sum of Grades:      {Sum_of_Grade}')

#Get Grades' average      
Grade = [Module_1, Module_2, Module_3, Module_4, Module_5, Module_6]

Average = sum(Grade)/len(Grade)

print(f'Average:            {Average:.2f}')

print('----------------------------------------')
