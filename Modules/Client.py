## Approach 1 -  ##
import A
import B
f=A.fruits()
f.disp()

g=B.animals()
g.disp()

print()

## Approach-2 - Import specific function ##

from A import fruits
from B import animals
f1=fruits()
f1.disp()

f2=animals()
f2.disp()

print()
## Approach-3 - Import all functions at a time ##

from A import *
f3=fruits()
f3.disp()
from B import *
f4=animals()
f4.disp()
