# Python program to calculate heron's formula
#Author | Yogeshwar G
import math
print('\t\t\t Herons Formula ')
first_side = float(input('First Side of the triangle | '))
second_side = float(input('Second Side of the triangle | '))
third_side = float(input('Third Side of the triangle | '))
master = ((first_side + second_side + third_side)/2)
area = math.sqrt(master * ((master - first_side) * ( master - second_side) * (master - third_side)))
print('Given Sides | ', first_side,second_side,third_side)
print('\n\n The area of the triangle using herons formula is [', round(abs(area)), '] Sq.units \n')
          