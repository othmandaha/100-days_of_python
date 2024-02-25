# we must import the modul random which is like a script that is available to us by default
import random 

from1_to_2 = random.randint(0, 1) 

if from1_to_2 == 0:
    print("Tails")
else:
    print("Heads")