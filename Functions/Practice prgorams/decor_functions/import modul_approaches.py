##Approach-1 Import module and call every function ##
import division
division.add(3,4)
division.mul(4,5)

print()
##Approach-2 Import specific functions ##
from division import add,mul
add(3,3)
mul(4,4)

print()

##Approach-3 Import all functions ##
from division import *
add(10,20)
mul(10,20)
