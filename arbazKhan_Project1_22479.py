# Arbaz Khan (1940280)
# This project will be able to read three coeffiecnts, calculate both roots using eqn, display the coefficents and the roots

# import complex math module

import cmath


var1 = float(input('Enter Variable A: '))  
var2 = float(input('Enter Variable B: '))  
var3 = float(input('Enter Variable C: '))


# calculate the discriminant

discrm = (var2**2) - (4*var1*var3)

# find two solutions
root1 = (-var2-cmath.sqrt(discrm))/(2*var1)
root2 = (-var2+cmath.sqrt(discrm))/(2*var1)

print('The Roots for the iput numbers are {0} and {1}'.format(root1,root2))


  
