 #  Percent average calculator with picks
    #### Video Demo:  https://youtu.be/-1UywCsMZ2o
    #### Description:
    TODO
This is a program that given a ".csv" file with integers, returns 2 splitted dictionaries that each 1 contains keys(the numbers from the csv file) and values(how many times the specific number have been repeated into the file).Before this it calculates the average to know where to put each key,value pairs and also sort the ".csv" file because originally a dict sort works like "LAST IN LAST OUT" so it will not sort it automatically. If desired it can pick the amount of numbers you want from the dictionary by randomness meanwhile the length of the numbers you ask for is not larger than the length of the dictionary itself.

What it does just by calling the program itself without extra commands:
   Returns the keys and values that are in the ".csv" file
   Shows the amount of numbers that are in the file
   Calculates the natural average percent
   Divides the original dictionary sorted into 2 dictionaries comparing them to the natural average percent.

IMPORTANT:
To use this program properly you might have 4 dictionaries:
dict1 : this is where the .csv file is gonna be saved with the key,value pairs being the value the count of key
dict2 : this dictionay works with through the dict1 just to return the same dict1 but sorted user friendly
dict3 : First, this dictionary must be called below_average, because this is how the average function recognize where to put the key value pairs that are under the average
dict4 : First, this dictionary must be called over_average, because this is how the average function recognize where to put the key value pairs that are above the average

The program goes through 4 paths: "reading the csv file and return a dictionary with pair of keys and values where value is the counting  of amount of same key" , "sorting the dictionary in a way that a human being would done it " , "calculates the natural percent average between all the values" and "split the dicitonary into 2 different ones adding the key value pairs where they belong in comparison with the natural percent average (below dictionary or above dictionary"above dictionary also contains the numbers that are equal to the natural percent average")

If desired, in the command line you can specify how many numbers you want from a specific dictionary(below or above). This number cant be greater than the number of keys into that dictionary. Lets call this "return random number"

How "return random number" works:
The length of sys.argv must be = 3 where:
   sys.argv[0] = the main file (also known as the program, in this case 'project.py')
   sys.argv[1] = choose between below or above so the program use 1 dictionary or other
   sys.argv[2] = the amount of numbers you want to get from the dictionary converted into a list and including only the keys(at this point percent values are not really needed). This is returned as a list

Example : python project.py below 3
This example would return 3 random numbers between the below dictionary in a list format.