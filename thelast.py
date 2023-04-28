import random
import sys


below = [3,4,7,8,10,11,13,16,19,20,25,27,28,29,34,36,37,38,42,43,48,49]
above = [1,5,6,9,12,14,18,21,22,23,24,30,31,32,33,35,39,40,41,46,47]
new = []

if sys.argv[1] == "below" :
    for numbers in below:
        if len(new) < int(sys.argv[2]):
            x = random.choice(below)
            if x not in new:
                new.append(x)
            else:
                continue
        else:
            break

if sys.argv[1] == "above" :
    for numbers in above:
        if len(new) < int(sys.argv[2]):
            x = random.choice(above)
            if x not in new:
                new.append(x)
            else:
                continue
        else:
            break



print (sorted(new))