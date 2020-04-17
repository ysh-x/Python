#Python program to find if the triangle is a right angled triangle
#Author : Yogeshwar G

import math

hypodnus = float(input(' Hypotnuse | '))
first_leg = float(input('First Leg | '))
second_leg = float(input('Second Leg | '))

print('\n\n')
if(math.pow(hypodnus,2)==(math.pow(first_leg,2)+math.pow(second_leg,2))):
     print(' Yes! The configuration is a right angle triangle ')
else:
     print('No! The given configuration does not add upto a righta angle triangle')
     
     