import time
from imp import reload
import module1
print("program is entering to sleeping state")
time.sleep(30)
reload(module1)
print("This is the last line of the program")
print()
time.sleep(30)
reload(module1)
print("This is the last line of the program")
